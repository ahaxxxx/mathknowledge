"""Build browser-native page readers from source documents rendered to PDFs.
Use the bundled soffice with CJK fonts to create --pdf-dir first; intermediate
PDFs stay outside docs. Original source files are never linked by this reader.
"""
from pathlib import Path
import argparse, hashlib, html, json, os, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
TITLES={29:'抽样',30:'用样本估计总体',31:'古典概型',32:'线性回归与列联表',36:'超几何分布与二项分布',37:'独立事件与独立重复试验',38:'正态分布和条件概率',39:'均值与方差在生活中运用'}
INDEX='../notes/09-high-school-math/08-probability/07-local-sources-zh.html'
def build(source,pdf,poppler):
    key=source.stem
    if key.startswith('point-'):
        _,point,kind,version=key.split('-')
        title=f'考点 {point} · {TITLES[int(point)]} · '+('讲解' if kind=='lesson' else '练习')+('解析' if version=='solution' else '试题')
        other=key.rsplit('-',1)[0]+('-questions' if version=='solution' else '-solution')
        companion=f'<a href="{other}.html">'+('返回试题' if version=='solution' else '查看对应解析')+'</a>'
    else:
        title='2026年高考统计概率大题必刷热点题型';companion=''
    reader=PdfReader(pdf);count=len(reader.pages)
    assert count>0
    dest=ROOT/'docs/assets/probability-reader'/key;dest.mkdir(parents=True,exist_ok=True)
    figures=[]
    with tempfile.TemporaryDirectory(prefix='probability-pages-') as tmp:
        batch = source.suffix == '.pdf' and any(not (dest/f'{i}.webp').exists() for i in range(1,count+1))
        if batch:
            subprocess.run([poppler,'-scale-to','2600','-png',str(pdf),str(Path(tmp)/'batch')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        for i,page in enumerate(reader.pages,1):
            target=dest/f'{i}.webp'
            if not target.exists():
                prefix=str(Path(tmp)/'page')
                if batch:
                    png = next(Path(tmp).glob(f'batch-{i:0{len(str(count))}d}.png'))
                else:
                    subprocess.run([poppler,'-f',str(i),'-l',str(i),'-singlefile','-scale-to','2600','-png',str(pdf),prefix],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
                    png = prefix+'.png'
                with Image.open(png) as im:im.convert('RGB').save(target,'WEBP',quality=88,method=4)
            with Image.open(target) as im:w,h=im.size
            figures.append(f'<figure id="page-{i}"><figcaption>第 {i} / {count} 页</figcaption><img src="../assets/probability-reader/{key}/{i}.webp" width="{w}" height="{h}" loading="'+('eager' if i==1 else 'lazy')+f'" alt="{html.escape(title)}，第 {i} 页"></figure>')
    options=''.join(f'<option value="{i}">第 {i} 页</option>' for i in range(1,count+1))
    body=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | 在线阅读</title><link rel="stylesheet" href="../assets/probability-reader.css"><script src="../assets/probability-reader.js" defer></script></head><body>
<header><a href="{INDEX}">← 概率资料目录</a><h1>{title}</h1><p>直接在线阅读，共 {count} 页。保留原资料公式与配图；试题与解析分别阅读。手机上可点击放大，再横向滑动。</p>{companion}</header>
<nav aria-label="阅读控制"><button id="prev" type="button">上一页</button><label>跳转到 <select id="page-select">{options}</select></label><button id="next" type="button">下一页</button><button id="zoom" type="button" aria-pressed="false">放大阅读</button><span id="status" aria-live="polite">第 1 / {count} 页</span></nav>
<main>{''.join(figures)}</main><footer><a href="{INDEX}">返回概率资料目录</a></footer></body></html>'''
    out=ROOT/'docs/probability-reader';out.mkdir(exist_ok=True)
    (out/f'{key}.html').write_text(body)
    print(key,count,flush=True)
    return {'id':key,'pages':count,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pdf-dir',type=Path,required=True);ap.add_argument('--pdftoppm',required=True);args=ap.parse_args()
    sources=sorted((ROOT/'docs/assets/probability-sources').glob('*.docx'))
    assert len(sources)==32
    jobs=[(s,args.pdf_dir/(s.stem+'.pdf'),args.pdftoppm) for s in sources]
    pdf=ROOT/'docs/assets/probability-sources/probability-hotspots-2020.pdf';jobs.append((pdf,pdf,args.pdftoppm))
    for _,p,_ in jobs:assert p.exists(),p
    with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(lambda a:build(*a),jobs))
    (ROOT/'docs/assets/probability-reader/manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print('TOTAL',sum(x['pages'] for x in records),'pages')
if __name__=='__main__':main()
