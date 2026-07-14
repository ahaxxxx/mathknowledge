from __future__ import annotations

import hashlib
import html
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SITE_ROOT = Path(__file__).resolve().parents[1]
LOCAL_ROOT_CANDIDATES = [
    ROOT / "考点讲解2021年高考数学复习一轮复习笔记（65个考点讲解全）",
    Path(r"C:\Users\liboz\研究生学习\Latex\Chenyue\考点讲解2021年高考数学复习一轮复习笔记（65个考点讲解全）"),
]
LOCAL_ROOT = next((path for path in LOCAL_ROOT_CANDIDATES if path.exists()), LOCAL_ROOT_CANDIDATES[0])
CONTENT_FILE = (
    SITE_ROOT
    / "content"
    / "09_high_school_math"
    / "04_solid_geometry"
    / "03_solid_geometry_local_full_exercises_zh.md"
)
ASSET_DIR = SITE_ROOT / "docs" / "assets" / "solid-geometry-local"
ASSET_HREF_PREFIX = "../../../assets/solid-geometry-local"

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

POINTS = [
    ("22", "空间几何平行问题"),
    ("23", "空间几何垂直问题"),
    ("24", "空间几何体体积及表面积"),
    ("25", "几何法解空间角"),
    ("26", "空间向量求空间角"),
    ("27", "空间向量求空间距离"),
    ("28", "空间几何体外接球"),
]


@dataclass
class Unit:
    kind: str
    value: str
    width: int | None = None
    height: int | None = None


@dataclass
class Block:
    text: str
    units: list[Unit]


@dataclass
class Question:
    number: int
    title: str
    blocks: list[Block]


def rel_targets(archive: zipfile.ZipFile) -> dict[str, str]:
    rel_path = "word/_rels/document.xml.rels"
    tree = ET.fromstring(archive.read(rel_path))
    result: dict[str, str] = {}
    for rel in tree.findall("rel:Relationship", NS):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            result[rel_id] = posixpath.normpath(posixpath.join("word", target))
    return result


def image_dimensions(data: bytes) -> tuple[int | None, int | None]:
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data.startswith(b"\xff\xd8"):
        offset = 2
        while offset + 9 < len(data):
            if data[offset] != 0xFF:
                offset += 1
                continue
            marker = data[offset + 1]
            offset += 2
            if marker in {0xD8, 0xD9}:
                continue
            if offset + 2 > len(data):
                break
            length = int.from_bytes(data[offset : offset + 2], "big")
            if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                if offset + 7 <= len(data):
                    height = int.from_bytes(data[offset + 3 : offset + 5], "big")
                    width = int.from_bytes(data[offset + 5 : offset + 7], "big")
                    return width, height
                break
            offset += length
    return None, None


def copy_image(archive: zipfile.ZipFile, target: str, prefix: str, index: int) -> tuple[str, int | None, int | None]:
    suffix = Path(target).suffix.lower() or ".png"
    data = archive.read(target)
    digest = hashlib.sha1(data).hexdigest()[:10]
    filename = f"{prefix}-{index:03d}-{digest}{suffix}"
    destination = ASSET_DIR / filename
    if not destination.exists():
        destination.write_bytes(data)
    width, height = image_dimensions(data)
    return f"{ASSET_HREF_PREFIX}/{filename}", width, height


def paragraph_units(para: ET.Element, rels: dict[str, str], archive: zipfile.ZipFile, prefix: str, counter: list[int]) -> Block:
    units: list[Unit] = []
    text_parts: list[str] = []
    for node in para.iter():
        if node.tag == f"{{{NS['w']}}}t" and node.text:
            units.append(Unit("text", node.text))
            text_parts.append(node.text)
        elif node.tag == f"{{{NS['a']}}}blip":
            embed = node.attrib.get(f"{{{NS['r']}}}embed")
            target = rels.get(embed or "")
            if target and target in archive.namelist():
                counter[0] += 1
                href, width, height = copy_image(archive, target, prefix, counter[0])
                units.append(Unit("image", href, width, height))
    return Block("".join(text_parts).strip(), units)


def docx_blocks(path: Path, prefix: str) -> list[Block]:
    with zipfile.ZipFile(path) as archive:
        rels = rel_targets(archive)
        tree = ET.fromstring(archive.read("word/document.xml"))
        counter = [0]
        blocks: list[Block] = []
        for para in tree.findall(".//w:p", NS):
            block = paragraph_units(para, rels, archive, prefix, counter)
            if block.text or any(unit.kind == "image" for unit in block.units):
                blocks.append(block)
        return blocks


def clean_question_text(text: str) -> str:
    text = re.sub(r"^\s*\d+[．.]\s*", "", text)
    return text.strip()


def split_questions(blocks: list[Block]) -> tuple[list[str], list[Question]]:
    intro: list[str] = []
    questions: list[Question] = []
    current: Question | None = None
    for block in blocks:
        match = re.match(r"^\s*(\d+)[．.]\s*(.*)", block.text)
        if match:
            current = Question(
                number=int(match.group(1)),
                title=clean_question_text(block.text),
                blocks=[block],
            )
            questions.append(current)
            continue
        if current is None:
            if block.text:
                intro.append(block.text)
            continue
        current.blocks.append(block)
    return intro, questions


def find_docx(point: str, *, source: str, version: str) -> Path:
    candidates = [
        path
        for path in LOCAL_ROOT.rglob("*.docx")
        if f"考点{point}" in str(path)
        and source in path.name
        and version in path.name
    ]
    if not candidates:
        raise FileNotFoundError(f"missing 考点{point} {source} {version}")
    return sorted(candidates, key=lambda path: len(str(path)))[0]


def is_block_image(unit: Unit) -> bool:
    if unit.width is None or unit.height is None:
        return True
    return unit.width >= 260 or unit.height >= 120


def image_tag(unit: Unit, *, block: bool) -> str:
    class_name = "local-docx-image local-docx-block-image" if block else "local-docx-image local-docx-inline-image"
    attrs = [
        f'class="{class_name}"',
        f'src="{html.escape(unit.value, quote=True)}"',
        'alt="本地资料图片"',
    ]
    if unit.width is not None:
        attrs.append(f'width="{unit.width}"')
    if unit.height is not None:
        attrs.append(f'height="{unit.height}"')
    return "<img " + " ".join(attrs) + ">"


def block_to_html(block: Block) -> str:
    parts: list[str] = []
    inline_parts: list[str] = []

    def flush_inline() -> None:
        content = "".join(inline_parts).strip()
        if content:
            parts.append(f'<p class="local-docx-line">{content}</p>')
        inline_parts.clear()

    for unit in block.units:
        if unit.kind == "text":
            inline_parts.append(html.escape(unit.value))
            continue
        if unit.kind != "image":
            continue
        block_image = is_block_image(unit)
        if block_image:
            flush_inline()
            parts.append(f'<div class="local-docx-figure">{image_tag(unit, block=True)}</div>')
        else:
            inline_parts.append(image_tag(unit, block=False))
    flush_inline()
    return "\n".join(parts)


def question_to_markdown(question: Question, global_index: int) -> str:
    body = "\n".join(rendered for block in question.blocks if (rendered := block_to_html(block)))
    lines = [f"### 题 {global_index}｜原题 {question.number}", ""]
    if body:
        lines.extend(
            [
                ":::diagram",
                '<div class="local-docx-card local-docx-question">',
                body,
                "</div>",
                ":::",
            ]
        )
    return "\n".join(lines).rstrip()


def solution_to_markdown(question: Question | None) -> str:
    if question is None:
        return ""
    body = "\n".join(rendered for block in question.blocks if (rendered := block_to_html(block)))
    lines = [":::solution 查看解析版原文", ""]
    if body:
        lines.extend(
            [
                ":::diagram",
                '<div class="local-docx-card local-docx-answer">',
                body,
                "</div>",
                ":::",
                "",
            ]
        )
    lines.append(":::")
    return "\n".join(lines).rstrip()


def main() -> int:
    if ASSET_DIR.exists():
        for child in ASSET_DIR.iterdir():
            if child.is_file():
                child.unlink()
    else:
        ASSET_DIR.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "# 立体几何与空间向量：考点 22-28 全量本地题库",
        "",
        "这一页把本地一轮复习资料中考点 22 到考点 28 的练习题按原考点完整整理出来。题干中的公式、图形和原 Word 图片会一起呈现；解析版内容折叠在“查看解析版原文”里，适合课后补充训练和查漏补缺。",
        "",
        "返回专题首页：[立体几何与空间向量](./README.md)。精选入门题库：[立体几何与空间向量：图形题库](./02_solid_geometry_exercises_zh.md)。",
        "",
        "## 使用说明",
        "",
        "1. 这页是全量题库，不适合一次性布置完；课堂上先用精选题库建立方法，再从这里按考点抽题。",
        "2. 学生讲题时，优先要求她说清楚“图形模型、目标类型、关键辅助线或坐标系”。",
        "3. Word 中不少数学公式和空间图形本身就是图片，所以本页保留原图，避免抽文字时丢失关键信息。",
        "",
    ]

    global_index = 1
    summary: list[tuple[str, str, int, int]] = []
    for point, title in POINTS:
        original = find_docx(point, source="练习", version="原卷版")
        solved = find_docx(point, source="练习", version="解析版")
        _, questions = split_questions(docx_blocks(original, f"kp{point}-q"))
        _, solutions = split_questions(docx_blocks(solved, f"kp{point}-a"))
        summary.append((point, title, len(questions), len(solutions)))

        lines.extend([f"## 考点 {point}：{title}", ""])
        lines.extend(
            [
                f"本组来自 `{original.name}`；原卷共抽取 {len(questions)} 道题，解析版可对齐 {len(solutions)} 道。",
                "",
            ]
        )
        for index, question in enumerate(questions):
            lines.append(question_to_markdown(question, global_index))
            lines.append("")
            solution = solutions[index] if index < len(solutions) else None
            if solution:
                lines.append(solution_to_markdown(solution))
                lines.append("")
            global_index += 1

    total_questions = sum(item[2] for item in summary)
    total_solutions = sum(item[3] for item in summary)
    lines.extend(
        [
            "## 抽取统计",
            "",
            f"- 全量原卷题目：{total_questions} 道。",
            f"- 可折叠解析版题块：{total_solutions} 道。",
            "",
        ]
    )
    for point, title, q_count, a_count in summary:
        lines.append(f"- 考点 {point} {title}：原卷 {q_count} 道，解析版 {a_count} 道。")

    CONTENT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {CONTENT_FILE}")
    print(f"questions={total_questions} solutions={total_solutions} assets={sum(1 for _ in ASSET_DIR.iterdir())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
