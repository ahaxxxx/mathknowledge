"""Check online-only source navigation and every rendered page asset."""
from pathlib import Path
from html.parser import HTMLParser
import json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):super().__init__();self.urls=[];self.images=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='img':self.images+=1
        for key in ('href','src'):
            if key in a:self.urls.append(a[key])
def main():
    records=json.loads((ROOT/'docs/assets/probability-reader/manifest.json').read_text())
    assert len(records)==33
    for row in records:
        p=ROOT/'docs/probability-reader'/f"{row['id']}.html"
        parser=Links();parser.feed(p.read_text());assert parser.images==row['pages']
        for url in parser.urls:
            assert not url.endswith(('.docx','.pdf')),url
            assert (p.parent/url.split('#')[0]).exists(),(p,url)
        for n in range(1,row['pages']+1):
            asset=ROOT/'docs/assets/probability-reader'/row['id']/f'{n}.webp'
            with Image.open(asset) as im:
                assert im.width>1000 and im.height>1000
                im.verify()
    index=ROOT/'docs/notes/09-high-school-math/08-probability/07-local-sources-zh.html'
    parser=Links();parser.feed(index.read_text())
    readers=[u for u in parser.urls if '/probability-reader/' in u]
    assert len(readers)==33
    assert not any(u.endswith(('.docx','.pdf')) for u in parser.urls)
    print(f"PASS: 33 online readers, {sum(r['pages'] for r in records)} page images, no file-download links")
if __name__=='__main__':main()
