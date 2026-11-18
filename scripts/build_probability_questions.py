"""Run from repository root, passing the directory of embedded-image HTML exports of the 16 solution DOCX files. Run after build_probability_reader.py when refreshing source material."""
from pathlib import Path
import re,sys,hashlib,base64
from html import escape
from lxml import etree,html
from PIL import Image
import pdfplumber
from lxml import html
from pathlib import Path
import re
def groups(f):
 b=html.parse(str(f)).find('body'); groups=[]; section='';ans=False
 for e in b:
  s=''.join(e.itertext()).strip().replace('\n','')
  if e.tag=='div' and e.get('title') in ('header','footer'):continue
  if re.match(r'^(【?题组|考法[一二三四五]|考点[一二三四五])',s):section=s;continue
  if e.tag=='p' and re.match(r'^\d+[.．、]',s):
   groups.append((section,[],[]));ans=False
  if not groups:continue
  if re.match(r'^(【(答案|解析|解答)】|解[：:])',s):ans=True
  if s or list(e.iter('img')):groups[-1][1+ans].append(e)
 return groups

root=Path('docs'); out=root/'probability-reader'; assets=root/'assets/probability-questions';assets.mkdir(exist_ok=True)
def clean(nodes):
 parts=[]
 for e in nodes:
  for x in list(e.iter()):
   if not isinstance(x.tag,str):continue
   if x.tag=='img':
    src=x.get('src');assert src.startswith('data:image/png;base64,');data=base64.b64decode(src.split(',',1)[1]);name=hashlib.sha256(data).hexdigest()[:20]+'.png';p=assets/name
    if not p.exists():p.write_bytes(data)
    x.set('src','../assets/probability-questions/'+name)
   for k in list(x.attrib):
    if k not in ('src','width','height','rowspan','colspan','alt'):del x.attrib[k]
   if x.tag in ('font','span','a'):x.drop_tag()
  parts.append(html.tostring(e,encoding='unicode'))
 return ''.join(parts)
def write(key,title,rows,credit):
 cards=[]
 for i,(q,a) in enumerate(rows,1):
  assert q and a
  cards.append(f'<article id="q{i}"><h2>第 {i} 题</h2>{q}<details><summary>查看答案与解析</summary>{a}</details></article>')
 page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><link rel="stylesheet" href="../assets/probability-questions.css"><main><a href="../notes/09-high-school-math/08-probability/07-local-sources-zh.html">← 概率资料目录</a><h1>{title}</h1><p>{credit} · 共 {len(rows)} 题</p><nav aria-label="题号">{' '.join(f'<a href="#q{i}">{i}</a>' for i in range(1,len(rows)+1))}</nav>{''.join(cards)}</main></html>'''
 (out/(key+'.html')).write_text(page)
for f in sorted(Path(sys.argv[1]).glob('*-solution.html')):
 key=f.stem;original=html.parse(str(out/(key+'.html'))).find('.//h1').text
 rows=[(clean(q),clean(a)) for section,q,a in groups(f)]
 for target in [key,key.replace('solution','questions')]: write(target,original.removesuffix('解析'),rows,'资料来源：学科网一轮复习笔记')
 print(key,len(rows))
key='probability-hotspots-2020'
with pdfplumber.open(root/f'assets/probability-sources/{key}.pdf') as doc:
 starts=[]
 for j,p in enumerate(doc.pages):
  for m in p.search(r'(\d{1,2})\s*[．.]\s*[（(]\s*2020'):starts.append((int(m['groups'][0]),j,m['top']-3))
 assert [n for n,j,t in starts]==list(range(1,31))*2
 def fragment(i):
  _,j,top=starts[i];_,k,end=starts[i+1] if i+1<len(starts) else (0,81,0)
  if i==29:k,end=31,0
  result=[]
  for pg in range(j,min(k+1,81)):
   page=doc.pages[pg];t=top if pg==j else 65;b=end if pg==k else page.height-55
   if b-t<15:continue
   with Image.open(root/f'assets/probability-reader/{key}/{pg+1}.webp') as im:
    scale=im.height/page.height;part=im.crop((int(48*scale),round(t*scale),im.width-int(48*scale),round(b*scale)))
    name=f'hotspot-{i+1}-{pg+1}.webp';part.save(assets/name,quality=91)
   result.append(f'<img class="sheet" loading="lazy" src="../assets/probability-questions/{name}" alt="原资料第 {pg+1} 页节选">')
  return ''.join(result)
 write(key,'统计概率综合热点题',[(fragment(i),fragment(i+30)) for i in range(30)],'资料来源：《2020 高考统计概率大题必刷热点题型》')
