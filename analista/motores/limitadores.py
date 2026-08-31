#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DEFAULT_UNITS=ROOT/'analista/generado/unidades.jsonl'; DEFAULT_OUT=ROOT/'analista/generado'
PILOTO='AA-SP-V1';VERSION='1.1.0';SCHEMA='1.0.0'
NO=re.compile(r'(?<![\w-])no(?![\w-])',re.I); CLAUSE_END=re.compile(r'[.;?!:](?=\s|$)'); SENT_END=re.compile(r'[.;?!](?=\s|$)')

def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def dump(p,rows): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
def sid(prefix,*parts): return prefix+'-'+hashlib.sha1('\x1f'.join(parts).encode()).hexdigest()[:12].upper()
def lr(u,t,a,b): base=u['localizacion']['linea_inicio'];return base+t[:a].count('\n'),base+t[:b].count('\n')
def base(kind,uid,lit,li,lf,classification,char_start,char_end):
 explicit=classification.endswith('_explicita')
 return {'id':sid({'distincion':'DIS','negacion':'NEG','excepcion':'EXC','restriccion_alcance':'RES'}[kind],uid,str(li),str(lf),str(char_start),str(char_end),lit,classification),'tipo_registro':kind,'schema_version':SCHEMA,'texto_literal':lit,'normalizacion_formal':None,'normalizacion_lexica':None,'estatus_enunciativo':'no_determinado','estado_extraccion':'extraido' if explicit else 'candidato','estado_verificacion':'pendiente','estado_auditoria':'pendiente','producido_por':{'motor':'limitadores','version':VERSION},'fuente_id':PILOTO,'unidad_id':uid,'localizacion':{'ruta':None,'linea_inicio':li,'linea_fin':lf}}
def spans(t,rx):
 out=[];s=0
 for m in rx.finditer(t):out.append((s,m.end(),True));s=m.end()
 if s<len(t):out.append((s,len(t),False))
 return out
def negations(u):
 t=u['texto_literal'];out=[]
 for a,b,complete in spans(t,CLAUSE_END):
  cl=t[a:b];ms=[m for m in NO.finditer(cl) if not re.match(r'(?i)no\s+s[oó]lo\b',cl[m.start():])]
  if not ms:continue
  start=a+ms[0].start();tail=t[start:b];sm=re.search(r'(?i)\s+sino\b',tail)
  if sm:tail=tail[:sm.start()]
  lit=tail.strip(' \n\t.,;:!?');lit=re.sub(r'\n[IVXLCDM]+\s*$','',lit).rstrip()
  if not lit:continue
  end=start+len(lit);li,lf=lr(u,t,start,end);cls='negacion_explicita' if complete else 'negacion_candidata';r=base('negacion',u['id'],lit,li,lf,cls,start,end);r['localizacion']['ruta']=u['archivo'];r.update({'objeto_negado_literal':lit,'alcance_literal':None,'clasificacion_negacion':cls});out.append(r)
 return out
def distinctions(u):
 t=u['texto_literal'];out=[]
 for a,b,complete in spans(t,SENT_END):
  seg=t[a:b]
  if not re.search(r'\bsino\b',seg,re.I):continue
  for nm in NO.finditer(seg):
   tail=seg[nm.start():]
   if re.match(r'(?i)no\s+s[oó]lo\b',tail):continue
   sm=re.search(r'\bsino\b',tail,re.I)
   if not sm:continue
   start=a+nm.start();lit=t[start:b].strip(' \n\t.,;?!');lit=re.sub(r'^[IVXLCDM]+\s*\n','',lit)
   si=re.search(r'\bsino\b',lit,re.I)
   if si:
    col=lit.find(':',si.end())
    if col>=0:lit=lit[:col].rstrip()
    si=re.search(r'\bsino\b',lit,re.I);comma=lit.find(',',si.end()) if si else -1
    if comma>=0:lit=lit[:comma].rstrip()
    si=re.search(r'\bsino\b',lit,re.I);em=lit.find('— es',si.end()) if si else -1
    if em>=0:lit=lit[:em].rstrip()
   m=re.search(r'(?is)\bno\b\s*(.*?)\s*\bsino\b\s*(.*)$',lit)
   if not m:break
   A=m.group(1).strip(' ,:');B=m.group(2).strip(' ,:')
   if B.lower().startswith('que '):B=B[4:]
   A=re.sub(r'(?i)^(?:es|son)\s+','',A);A=re.sub(r'(?i)^lo\s+hizo\s+','',A)
   end=start+len(lit);li,lf=lr(u,t,start,end);cls='distincion_explicita' if complete else 'distincion_candidata';r=base('distincion',u['id'],lit,li,lf,cls,start,end);r['localizacion']['ruta']=u['archivo'];r.update({'termino_a_literal':A,'termino_b_literal':B,'marcador_literal':'sino','clasificacion_distincion':cls});out.append(r);break
 return out
def restrictions(u):
 t=u['texto_literal'];out=[]
 for a,b,_ in spans(t,SENT_END):
  seg=t[a:b]
  for m in re.finditer(r'(?i)(?<!\w)s[oó]lo(?=\s)',seg):
   pre=seg[max(0,m.start()-4):m.start()].casefold()
   if re.search(r'no\s*$',pre):continue
   rest=seg[m.start():]
   if not re.match(r'(?is)s[oó]lo\s+(?:pued[eo]|desde)\b',rest):continue
   lit=rest.strip(' \n\t.,;?!');mm=re.match(r'(?is)(solo puede encontrarse en los actos)\b',lit)
   if mm:lit=mm.group(1)
   st=a+m.start();end=st+len(lit);li,lf=lr(u,t,st,end);cls='restriccion_explicita';r=base('restriccion_alcance',u['id'],lit,li,lf,cls,st,end);r['localizacion']['ruta']=u['archivo'];r.update({'afirmacion_limitada_id':None,'tipo_restriccion':'no_determinada','fragmento_restriccion_literal':lit,'clasificacion_restriccion':cls});out.append(r);break
  mm=re.search(r'(?is)((?:el|este)\s+sistema\s+no\s+describe\s+aquí.*?excede\s+el\s+alcance\s+de\s+(?:este|esta)\s+\w+)',seg)
  if mm:
   lit=mm.group(1);st=a+mm.start();end=st+len(lit);li,lf=lr(u,t,st,end);cls='restriccion_explicita';r=base('restriccion_alcance',u['id'],lit,li,lf,cls,st,end);r['localizacion']['ruta']=u['archivo'];r.update({'afirmacion_limitada_id':None,'tipo_restriccion':'no_determinada','fragmento_restriccion_literal':lit,'clasificacion_restriccion':cls});out.append(r)
 return out
def exceptions(u):
 t=u['texto_literal'];out=[]
 for m in re.finditer(r'(?i)\bexcepto\s+[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚáéíóúÑñ-]*',t):
  lit=m.group(0);li,lf=lr(u,t,m.start(),m.end());cls='excepcion_explicita';r=base('excepcion',u['id'],lit,li,lf,cls,m.start(),m.end());r['localizacion']['ruta']=u['archivo'];r.update({'afirmacion_limitada_id':None,'fragmento_exceptivo_literal':lit,'clasificacion_excepcion':cls});out.append(r)
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--unidades',type=Path,default=DEFAULT_UNITS);ap.add_argument('--output-root',type=Path,default=DEFAULT_OUT);a=ap.parse_args();units=[u for u in load(a.unidades) if u.get('fuente_id')==PILOTO];outs={'distinciones.jsonl':[],'negaciones.jsonl':[],'excepciones.jsonl':[],'restricciones-alcance.jsonl':[]}
 for u in units:
  outs['distinciones.jsonl']+=distinctions(u);outs['negaciones.jsonl']+=negations(u);outs['excepciones.jsonl']+=exceptions(u);outs['restricciones-alcance.jsonl']+=restrictions(u)
 key=lambda r:(r['localizacion']['ruta'],r['localizacion']['linea_inicio'],r['localizacion']['linea_fin'],r['id'])
 for n,rows in outs.items():rows.sort(key=key);dump(a.output_root/n,rows)
 cov={'id':sid('COB',PILOTO,'limitadores',VERSION),'tipo_registro':'reporte_cobertura','schema_version':SCHEMA,'texto_literal':None,'normalizacion_formal':None,'normalizacion_lexica':None,'estatus_enunciativo':None,'estado_extraccion':'extraido','estado_verificacion':'pendiente','estado_auditoria':'no_aplica','producido_por':{'motor':'limitadores','version':VERSION},'obra_id':PILOTO,'motor':'limitadores','version_motor':VERSION,'unidades_totales':len(units),'unidades_procesadas':len(units),'unidades_omitidas':[],'errores':[]};dump(a.output_root/'cobertura-limitadores.jsonl',[cov]);print({k:len(v) for k,v in outs.items()},'units',len(units));return 0
if __name__=='__main__':raise SystemExit(main())
