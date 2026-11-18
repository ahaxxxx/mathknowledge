"""Restore the introductory diagram from each original probability lesson."""
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile

DOCS = Path(__file__).resolve().parents[1] / "docs"


def extract_map(point):
    source = DOCS / f"assets/probability-sources/point-{point}-lesson-solution.docx"
    with ZipFile(source) as archive:
        document = ElementTree.fromstring(archive.read("word/document.xml"))
        targets = {r.get("Id"): r.get("Target") for r in
                   ElementTree.fromstring(archive.read("word/_rels/document.xml.rels"))}
        in_map = False
        for p in document.findall(".//{*}body/{*}p"):
            text = "".join(t.text or "" for t in p.findall(".//{*}t"))
            if "常见考法" in text:
                break
            if "思维导图" in text:
                in_map = True
            if in_map:
                for node in p.iter():
                    for key, value in node.attrib.items():
                        if key.endswith(("}embed", "}id")) and value in targets:
                            return archive.read("word/" + targets[value])
    return None


def restore_maps():
    folder = DOCS / "assets/probability-questions"
    for source in sorted((DOCS / "assets/probability-sources").glob("point-*-lesson-solution.docx")):
        point = source.name.split("-")[1]
        data = extract_map(point)
        if data is None:
            continue
        assert data.startswith(b"\x89PNG")
        name = f"point-{point}-mind-map.png"
        (folder / name).write_bytes(data)
        url = f"../assets/probability-questions/{name}"
        for page in (DOCS / "probability-reader").glob(f"point-{point}-*.html"):
            body = page.read_text()
            title = re.search(r"<h1>(.*?)</h1>", body)[1].split("·")[1].strip()
            figure = (f'<figure class="mind-map"><figcaption>{title}思维导图</figcaption>'
                      f'<a href="{url}" aria-label="放大查看{title}思维导图">'
                      f'<img src="{url}" alt="{title}思维导图（原讲义）"></a>'
                      '<small>点击图片查看原图</small></figure>')
            if '<figure class="mind-map">' not in body:
                page.write_text(body.replace("<nav ", figure + "<nav ", 1))


if __name__ == "__main__":
    restore_maps()
