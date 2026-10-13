from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from fractions import Fraction as F
from itertools import combinations, product
import re

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'docs/notes/09-high-school-math/08-probability'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.answers = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'img' and 'src' in attrs:
            self.links.append(attrs['src'])
        if tag == 'details':
            assert 'open' not in attrs, 'Solution exposed by default'
            self.answers += 1


def main():
    pages = list(NOTES.glob('*.html'))
    assert len(pages) == 19
    for path in pages + [ROOT/'docs/high-school-math.html', ROOT/'docs/probability.html']:
        data = path.read_text(encoding='utf-8')
        assert '\ufffd' not in data
        assert ':::solution' not in data
        parsed = Page()
        parsed.feed(data)
        for href in parsed.links:
            u = urlsplit(href)
            if u.scheme or u.netloc or not u.path:
                continue
            target = (ROOT/'docs'/unquote(u.path.lstrip('/'))) if u.path.startswith('/') else path.parent/unquote(u.path)
            assert target.exists(), (path, href)
        if path.name == '06-exercises-zh.html':
            assert parsed.answers == 72, parsed.answers
    source = (ROOT/'content/09_high_school_math/08_probability/06_exercises_zh.md').read_text(encoding='utf-8')
    assert len(re.findall(r'^## [A-L]\.',source,re.M)) == 12
    assert len(re.findall(r'^### 题 \d+',source,re.M)) == 72
    lessons = list((ROOT/'content/09_high_school_math/08_probability').glob('1[0-5]_lesson_*.md'))
    assert len(lessons) == 6
    for lesson in lessons:
        content = lesson.read_text(encoding='utf-8')
        assert len(re.findall(r'^### 作业 [1-4]', content, re.M)) == 4
        assert content.count(':::solution 一级提示') == 4
        assert content.count(':::solution 完整解析') == 4
    assessment = (ROOT/'content/09_high_school_math/08_probability/16_assessment_zh.md').read_text(encoding='utf-8')
    assert len(re.findall(r'^### 先修 ',assessment,re.M)) == 8
    assert len(re.findall(r'^### 复测 ',assessment,re.M)) == 4
    assert len(re.findall(r'^### 阶段 ',assessment,re.M)) == 4
    # Independently enumerate finite models used in the exercise bank.
    for n,m,r in [(6,2,3),(7,3,3),(8,3,4),(9,4,3),(10,4,4),(11,5,4)]:
        counts = [sum(i<m for i in chosen) for chosen in combinations(range(n),r)]
        mean = sum(F(x,len(counts)) for x in counts)
        variance = sum((F(x)-mean)**2/len(counts) for x in counts)
        assert mean == F(r*m,n)
        assert variance == F(r*m*(n-m)*(n-r),n*n*(n-1))
    for m,p in [(3,F(1,2)),(4,F(1,3)),(5,F(2,5)),(3,F(1,4)),(4,F(3,5)),(6,F(1,2))]:
        mean = F(0)
        total = F(0)
        for seq in product([0,1],repeat=m):
            weight = p**sum(seq)*(1-p)**(m-sum(seq))
            t = next((i+1 for i,x in enumerate(seq) if x),m)
            mean += t*weight
            total += weight
        assert total == 1
        assert mean == (1-(1-p)**m)/p
    print('PASS: 19 pages, 6 lessons, 24 core exercises, 8+4+4 assessments, 72 practice solutions, links and model checks.')


if __name__ == '__main__':
    main()
