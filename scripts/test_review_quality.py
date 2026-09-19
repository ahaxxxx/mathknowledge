"""Behavioral regressions for numbering, navigation and safe answer matching."""
import json
import html as html_module
import re
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import build_notes as build
from solution_matching import match_solutions

ROOT = Path(__file__).resolve().parents[1]

class QualityTests(unittest.TestCase):
    def test_numbering_survives_solution_blocks(self):
        source = ROOT/'content/09_high_school_math/00_functions/README.md'
        out = build.render_markdown('1. first\n\n:::solution answer\nyes\n:::\n\n2. second', source, Path('notes/test.html'))
        self.assertIn('<ol start="1">', out)
        self.assertIn('<ol start="2">', out)

    def test_missing_middle_answer_does_not_shift_later_answers(self):
        def q(n,t): return NS(number=n,blocks=[NS(units=[NS(kind='text',value=t)])])
        questions=[q(1,'A'),q(2,'B'),q(3,'C')]
        solutions=[q(1,'A'),q(3,'C')]
        matched=match_solutions(questions,solutions)
        self.assertEqual(matched,[solutions[0],None,solutions[1]])
        self.assertEqual(match_solutions([q(1,'different')],solutions),[None])
        self.assertEqual(match_solutions([q(1,'A')],[q(1,'A'),q(1,'A')]),[None])

    def test_repeated_numbers_need_unique_stems(self):
        def q(t):return NS(number=1,blocks=[NS(units=[NS(kind='text',value=t)])])
        a,b=q('A'),q('B')
        self.assertEqual(match_solutions([a,b],[b,a]),[a,b])

    def test_heading_ids_are_unique(self):
        article,toc=build.article_navigation('<h2>A</h2><h2>A</h2><h3>B</h3>')
        self.assertEqual(re.findall('id="([^"]+)"',article),['section-1','section-2','section-3'])
        for target in ['section-1','section-2','section-3']:self.assertIn('#'+target,toc)

    def test_counts_exclude_readmes_and_include_descendants(self):
        notes=build.gather_notes();nodes=build.build_directory_nodes(notes)
        root=nodes[Path()];out=build.render_directory_page(root,nodes)
        count=sum(not n.is_readme for n in notes)
        self.assertIn(f'文章总数（含子目录，不含目录介绍）：{count}',out)

    def test_all_imported_questions_preserved_and_audited(self):
        audit=json.loads((ROOT/'review/question-pairing-audit.json').read_text())
        self.assertEqual(len(audit),464)
        self.assertEqual(sum(x['status']=='pending' for x in audit),93)
        for file in {r['file'] for r in audit}:
            source=(ROOT/file).read_text()
            rows=[r for r in audit if r['file']==file]
            self.assertEqual(len(re.findall(r'^### 题 ',source,re.M)),len(rows))
            self.assertEqual(source.count(':::solution 解析待核验'),sum(x['status']=='pending' for x in rows))

    def test_every_visible_imported_answer_repeats_full_question(self):
        def normalize(text):
            text = re.sub(r'<img\b[^>]*>', lambda m: 'IMG:' + re.search(r'-([0-9a-f]{10})\.', m.group()).group(1), text)
            return re.sub(r'\s+', '', html_module.unescape(re.sub('<[^>]+>', '', text)))
        visible = 0
        for file in (ROOT/'content/09_high_school_math').rglob('*local_full_exercises_zh.md'):
            for chunk in re.split(r'(?=^### 题 )', file.read_text(), flags=re.M)[1:]:
                if 'local-docx-answer' not in chunk:
                    continue
                question, answer = chunk.split(':::solution', 1)
                question = question[question.index('<div'):question.rindex('</div>') + 6]
                answer = answer[answer.index('<div'):]
                self.assertTrue(normalize(answer).startswith(normalize(question)), file.name)
                visible += 1
        self.assertEqual(visible, 371)

    def test_generated_internal_links_assets_and_anchors(self):
        class Links(HTMLParser):
            def __init__(self):super().__init__();self.links=[];self.ids=[]
            def handle_starttag(self,tag,attrs):
                attrs=dict(attrs)
                if 'id' in attrs:self.ids.append(attrs['id'])
                for name in ('href','src'):
                    if name in attrs:self.links.append(attrs[name])
        cache={}
        def parsed(p):
            if p not in cache:
                obj=Links();obj.feed(p.read_text());cache[p]=obj
            return cache[p]
        paths=list((ROOT/'docs/notes/09-high-school-math').rglob('*.html'))
        paths.append(ROOT/'docs/high-school-math.html')
        errors=[]
        for p in paths:
            obj=parsed(p)
            self.assertEqual(len(obj.ids),len(set(obj.ids)),str(p))
            for link in obj.links:
                url=urlsplit(link)
                if url.scheme or url.netloc:continue
                dest=(p.parent/unquote(url.path)).resolve() if url.path else p
                if not dest.exists():errors.append(f'{p.name}: missing {link}')
                elif url.fragment and dest.suffix=='.html' and unquote(url.fragment) not in parsed(dest).ids:
                    errors.append(f'{p.name}: missing anchor {link}')
        self.assertEqual(errors,[])

if __name__=='__main__':unittest.main()
