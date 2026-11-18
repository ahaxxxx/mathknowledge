"""After building question pages, apply display widths from matching Writer ODT exports.

Usage: python size_probability_formulas.py HTML_EXPORT_DIR ODT_EXPORT_DIR
Export both formats from the same solution documents with LibreOffice.
"""
import base64
import hashlib
import re
import sys
from pathlib import Path
from zipfile import ZipFile

from lxml import etree, html

docs = Path(__file__).resolve().parents[1] / 'docs'
draw = '{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}'
svg = '{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}'


def formula_widths(source, odt_dir):
    with ZipFile(odt_dir / source.with_suffix('.odt').name) as archive:
        document = etree.fromstring(archive.read('content.xml'))
    frames = {f.get(draw+'name'): f for f in document.iter(draw+'frame')}
    sizes = {}
    for image in html.parse(str(source)).iter('img'):
        name = image.get('name', '')
        if not name.startswith('Object'):
            continue
        width = frames[name].get(svg+'width')
        assert width.endswith('cm'), width
        data = base64.b64decode(image.get('src').split(',', 1)[1])
        key = hashlib.sha256(data).hexdigest()[:20]
        # Express the physical width relative to a 12 pt body font.
        sizes[key] = float(width[:-2]) * 72 / 2.54 / 12
    return sizes


def format_page(page, widths):
    text = page.read_text()
    def set_width(match):
        key = match[2]
        if key not in widths:
            return match[0]
        return f'<img src="{match[1]}" class="formula" style="width:{widths[key]:.3f}em">'
    text = re.sub(r'<img src="([^"<>]*/([a-f0-9]{20})\.png)"[^>]*>', set_width, text)
    text = re.sub(r'(class="formula" style="[^"]+">)\s*([.,，。；：、])', r'\1\2', text)
    def format_options(match):
        body = match[1].strip()
        labels = list(re.finditer(r'(?<![A-Za-z])([ABCD])[．、.]', body))
        if [m[1] for m in labels] != list('ABCD') or labels[0].start() != 0:
            return match[0]
        starts = [m.start() for m in labels] + [len(body)]
        options = [body[a:b].strip() for a,b in zip(starts,starts[1:])]
        return '<div class="choices">'+''.join('<div>'+v+'</div>' for v in options)+'</div>'
    page.write_text(re.sub(r'<p>(.*?)</p>', format_options, text, flags=re.S))


if __name__ == '__main__':
    for source in sorted(Path(sys.argv[1]).glob('*-solution.html')):
        widths = formula_widths(source, Path(sys.argv[2]))
        for name in (source.name, source.name.replace('-solution', '-questions')):
            format_page(docs/'probability-reader'/name, widths)
