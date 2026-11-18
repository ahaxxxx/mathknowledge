"""Validate direct links, original question counts and closed answer panels."""
from pathlib import Path
from urllib.parse import urlsplit
from lxml import html

ROOT = Path(__file__).resolve().parents[1] / 'docs'
counts = {29:(9,11), 30:(13,20), 31:(7,16), 32:(10,14), 36:(8,8), 37:(8,11), 38:(10,14), 39:(11,12)}
expected = {'probability-hotspots-2020':30}
for point, pair in counts.items():
    for kind, count in zip(('lesson','practice'),pair):
        for version in ('questions','solution'):
            expected[f'point-{point}-{kind}-{version}'] = count
for name, count in expected.items():
    path = ROOT/'probability-reader'/f'{name}.html'
    page = html.parse(str(path))
    items = page.findall('.//article')
    assert len(items) == count, name
    for item in items:
        answers = item.findall('details')
        assert len(answers) == 1 and 'open' not in answers[0].attrib
        assert len(answers[0]) > 1
    for url in page.xpath('//@src | //@href'):
        if not url.startswith('#'):
            assert (path.parent/urlsplit(url).path).is_file(), (name,url)
print('Validated all 33 original reader addresses and their inline answers.')
