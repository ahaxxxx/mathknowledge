from __future__ import annotations

import argparse
import html
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = ROOT / "content"
DOCS_ROOT = ROOT / "docs"
NOTES_ROOT = DOCS_ROOT / "notes"

NAV_ITEMS = [
    ("首页", "index.html", False),
    ("关于", "about.html", False),
    ("方法", "method.html", False),
    ("高中数学", "high-school-math.html", False),
    ("高数", "calculus.html", False),
    ("线代", "linear-algebra.html", False),
    ("概率", "probability.html", False),
    ("书目", "references.html", False),
    ("路线", "roadmap.html", False),
    ("答疑", "live.html", False),
    ("FAQ", "faq.html", False),
    ("笔记", "notes/index.html", True),
]

SECTION_LABELS = {
    "00_about": "关于",
    "01_method": "方法",
    "02_calculus": "高数",
    "03_linear_algebra": "线代",
    "04_probability": "概率",
    "05_bridge": "Bridge",
    "06_live": "答疑",
    "07_faq": "FAQ",
    "08_roadmap": "路线",
    "09_high_school_math": "高中数学",
    "01_sequences": "数列",
}

BLOCK_STARTERS = (
    "#",
    "- ",
    "* ",
    "> ",
    "```",
    "---",
    ":::",
    "$$",
)


@dataclass
class Note:
    source_path: Path
    source_rel: Path
    output_rel: Path
    title: str
    excerpt: str
    content: str
    is_readme: bool
    source_dir: Path


@dataclass
class DirectoryNode:
    source_dir: Path
    title: str
    output_rel: Path
    notes: list[Note] = field(default_factory=list)
    readme: Note | None = None
    children: list["DirectoryNode"] = field(default_factory=list)


def slug_segment(name: str) -> str:
    text = name.strip().replace("_", "-").replace(" ", "-")
    text = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff\-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "note"


def strip_number_prefix(name: str) -> str:
    return re.sub(r"^\d+[_-]?", "", name)


def order_key(name: str) -> tuple[int, str]:
    match = re.match(r"^(\d+)", name)
    index = int(match.group(1)) if match else 10**9
    return index, name.lower()


def humanize_segment(name: str) -> str:
    if name in SECTION_LABELS:
        return SECTION_LABELS[name]
    cleaned = strip_number_prefix(name).replace("_", " ").replace("-", " ").strip()
    return cleaned or name


def source_dir_to_output_rel(source_dir: Path) -> Path:
    parts = [slug_segment(part) for part in source_dir.parts]
    return Path("notes", *parts)


def source_to_output_rel(source_rel: Path) -> Path:
    directory_rel = source_rel.parent
    if source_rel.name.lower() == "readme.md":
        return source_dir_to_output_rel(directory_rel) / "index.html"
    stem = slug_segment(source_rel.stem)
    return source_dir_to_output_rel(directory_rel) / f"{stem}.html"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def extract_excerpt(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#") or line.startswith("- ") or re.match(r"^\d+\.\s+", line):
            i += 1
            continue
        if line.startswith(">") or line.startswith("```") or re.fullmatch(r"-{3,}", line):
            i += 1
            continue
        paragraph: list[str] = [line]
        i += 1
        while i < len(lines):
            current = lines[i].strip()
            if not current:
                break
            if current.startswith(BLOCK_STARTERS) or re.match(r"^\d+\.\s+", current):
                break
            paragraph.append(current)
            i += 1
        return " ".join(paragraph)
    return ""


def strip_leading_h1(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].strip().startswith("# "):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
    return "\n".join(lines)


def nav_html(root_prefix: str) -> str:
    anchors: list[str] = []
    for label, href, is_notes in NAV_ITEMS:
        active = ' class="is-active"' if is_notes else ""
        anchors.append(f'<a{active} href="{root_prefix}{href}">{label}</a>')
    return "".join(anchors)


def page_shell(
    *,
    title: str,
    description: str,
    body_html: str,
    root_prefix: str,
    crumbs: list[tuple[str, str | None]],
) -> str:
    crumb_parts: list[str] = []
    for label, href in crumbs:
        if href:
            crumb_parts.append(f'<a href="{href}">{html.escape(label)}</a>')
        else:
            crumb_parts.append(f"<span>{html.escape(label)}</span>")
    crumbs_html = "<span>/</span>".join(crumb_parts)
    description_meta = html.escape(description or title)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | math.bozhanli.com</title>
  <meta name="description" content="{description_meta}">
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <link rel="stylesheet" href="{root_prefix}assets/site.css">
</head>
<body>
  <div class="shell page">
    <div class="topbar">
      <div class="topbar-inner">
        <a class="brand" href="{root_prefix}index.html"><strong>math.bozhanli.com</strong><span>数学重建与共学</span></a>
        <nav class="nav">
          {nav_html(root_prefix)}
        </nav>
      </div>
    </div>
    <div class="page-head">
      <div class="crumbs">{crumbs_html}</div>
      <h1>{html.escape(title)}</h1>
      <p>{html.escape(description)}</p>
    </div>
    {body_html}
  </div>
</body>
</html>
"""


def relative_href(from_output: Path, to_output: Path) -> str:
    return Path(os.path.relpath(DOCS_ROOT / to_output, (DOCS_ROOT / from_output).parent)).as_posix()


def root_prefix_for(output_rel: Path) -> str:
    return "../" * len(output_rel.parent.parts)


def rewrite_link(target: str, source_path: Path, output_rel: Path) -> str:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
        return html.escape(target, quote=True)

    base, anchor = (target.split("#", 1) + [""])[:2]
    target_path = Path(base)
    if target_path.suffix.lower() == ".md":
        resolved_source = (source_path.parent / target_path).resolve()
        try:
            resolved_rel = resolved_source.relative_to(CONTENT_ROOT)
        except ValueError:
            return html.escape(target, quote=True)
        destination = source_to_output_rel(resolved_rel)
        href = relative_href(output_rel, destination)
        if anchor:
            href = f"{href}#{anchor}"
        return html.escape(href, quote=True)

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        href = Path(target).as_posix()
        return html.escape(href, quote=True)
    return html.escape(target, quote=True)


def render_inline(text: str, source_path: Path, output_rel: Path) -> str:
    code_tokens: list[str] = []
    link_tokens: list[str] = []

    def store_code(match: re.Match[str]) -> str:
        token = f"@@CODE{len(code_tokens)}@@"
        code_tokens.append(f"<code>{html.escape(match.group(1))}</code>")
        return token

    protected = re.sub(r"`([^`]+)`", store_code, text)
    escaped = html.escape(protected)

    def store_link(match: re.Match[str]) -> str:
        token = f"@@LINK{len(link_tokens)}@@"
        label = render_inline(match.group(1), source_path, output_rel)
        href = rewrite_link(match.group(2), source_path, output_rel)
        link_tokens.append(f'<a href="{href}">{label}</a>')
        return token

    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", store_link, escaped)

    def bare_url(match: re.Match[str]) -> str:
        url = match.group(1)
        return f'<a href="{html.escape(url, quote=True)}">{html.escape(url)}</a>'

    escaped = re.sub(r"(https?://[^\s<]+)", bare_url, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)

    for index, token_html in enumerate(code_tokens):
        escaped = escaped.replace(f"@@CODE{index}@@", token_html)
    for index, token_html in enumerate(link_tokens):
        escaped = escaped.replace(f"@@LINK{index}@@", token_html)
    return escaped


def render_list(items: Iterable[str], ordered: bool, source_path: Path, output_rel: Path) -> str:
    tag = "ol" if ordered else "ul"
    rendered = "".join(
        f"<li>{render_inline(item.strip(), source_path, output_rel)}</li>"
        for item in items
    )
    return f"<{tag}>{rendered}</{tag}>"


def render_text_paragraph(text: str, source_path: Path, output_rel: Path) -> str:
    return f"<p>{render_inline(text, source_path, output_rel)}</p>"


def render_paragraph(lines: list[str], source_path: Path, output_rel: Path) -> str:
    raw_chunks: list[str] = []
    html_chunks: list[str] = []
    for index, raw_line in enumerate(lines):
        stripped = raw_line.rstrip()
        raw_chunks.append(stripped.rstrip())
        html_chunks.append(render_inline(stripped.rstrip(), source_path, output_rel))
        if stripped.endswith("  "):
            raw_chunks.append("\n")
            html_chunks.append("<br>")
        elif index < len(lines) - 1:
            raw_chunks.append(" ")
            html_chunks.append(" ")

    raw_text = "".join(raw_chunks)
    if "$$" not in raw_text:
        return f"<p>{''.join(html_chunks)}</p>"

    blocks: list[str] = []
    for part in re.split(r"(\$\$.*?\$\$)", raw_text, flags=re.S):
        if not part:
            continue
        if part.startswith("$$") and part.endswith("$$"):
            blocks.append(render_math_block([part]))
            continue
        text_part = part.strip()
        if text_part:
            blocks.append(render_text_paragraph(text_part, source_path, output_rel))
    return "\n".join(blocks)


def render_math_block(math_lines: list[str]) -> str:
    content = "\n".join(html.escape(line.rstrip()) for line in math_lines)
    return f'<div class="math-display">{content}</div>'


def collect_list_items(lines: list[str], start_index: int, ordered: bool) -> tuple[list[str], int]:
    items: list[str] = []
    index = start_index
    list_pattern = r"^\d+\.\s+" if ordered else r"^-\s+"
    while index < len(lines):
        stripped = lines[index].strip()
        if not re.match(list_pattern, stripped):
            break

        item_text = re.sub(list_pattern, "", stripped, count=1)
        item_lines = [item_text]
        index += 1

        while index < len(lines):
            current = lines[index]
            current_stripped = current.strip()
            if not current_stripped:
                index += 1
                break
            if re.match(list_pattern, current_stripped):
                break
            if (
                current_stripped.startswith("```")
                or current_stripped.startswith("#")
                or current_stripped.startswith(">")
                or (ordered and current_stripped.startswith("- "))
                or (not ordered and re.match(r"^\d+\.\s+", current_stripped))
                or re.fullmatch(r"-{3,}", current_stripped)
                or current_stripped.startswith(":::solution")
                or current_stripped == ":::"
                or current_stripped.startswith("$$")
            ):
                break
            if current.startswith("  ") or current.startswith("\t"):
                item_lines.append(current_stripped)
                index += 1
                continue
            break

        items.append(" ".join(item_lines))
    return items, index


def render_markdown(markdown_text: str, source_path: Path, output_rel: Path) -> str:
    lines = markdown_text.splitlines()
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("$$"):
            math_lines = [line]
            single_line = stripped.endswith("$$") and len(stripped) > 2
            i += 1
            if not single_line:
                while i < len(lines):
                    math_lines.append(lines[i])
                    current_stripped = lines[i].strip()
                    i += 1
                    if current_stripped.endswith("$$"):
                        break
            blocks.append(render_math_block(math_lines))
            continue

        if stripped.startswith(":::solution"):
            summary = stripped[len(":::solution"):].strip() or "查看解答"
            solution_lines: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                solution_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            inner_html = render_markdown("\n".join(solution_lines), source_path, output_rel)
            blocks.append(
                '<details class="solution-toggle">'
                f'<summary>{render_inline(summary, source_path, output_rel)}</summary>'
                f'<div class="solution-body">{inner_html}</div>'
                '</details>'
            )
            continue

        if stripped.startswith("```"):
            language = stripped[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            code_class = f' class="language-{html.escape(language)}"' if language else ""
            code_html = html.escape("\n".join(code_lines))
            blocks.append(f"<pre><code{code_class}>{code_html}</code></pre>")
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            content = render_inline(heading_match.group(2).strip(), source_path, output_rel)
            blocks.append(f"<h{level}>{content}</h{level}>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            blocks.append("<hr>")
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].lstrip())
                i += 1
            inner_html = render_markdown("\n".join(quote_lines), source_path, output_rel)
            blocks.append(f"<blockquote>{inner_html}</blockquote>")
            continue

        if stripped.startswith("- "):
            items, i = collect_list_items(lines, i, ordered=False)
            blocks.append(render_list(items, False, source_path, output_rel))
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items, i = collect_list_items(lines, i, ordered=True)
            blocks.append(render_list(items, True, source_path, output_rel))
            continue

        paragraph_lines = [line]
        i += 1
        while i < len(lines):
            current = lines[i]
            current_stripped = current.strip()
            if not current_stripped:
                break
            if (
                current_stripped.startswith("```")
                or current_stripped.startswith("#")
                or current_stripped.startswith(">") 
                or current_stripped.startswith("- ")
                or re.match(r"^\d+\.\s+", current_stripped)
                or re.fullmatch(r"-{3,}", current_stripped)
                or current_stripped.startswith(":::solution")
                or current_stripped == ":::"
                or current_stripped.startswith("$$")
            ):
                break
            paragraph_lines.append(current)
            i += 1
        blocks.append(render_paragraph(paragraph_lines, source_path, output_rel))
    return "\n".join(blocks)


def gather_notes() -> list[Note]:
    notes: list[Note] = []
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        source_rel = path.relative_to(CONTENT_ROOT)
        output_rel = source_to_output_rel(source_rel)
        content = read_text(path)
        fallback = humanize_segment(path.stem)
        title = extract_title(content, fallback)
        excerpt = extract_excerpt(content)
        notes.append(
            Note(
                source_path=path,
                source_rel=source_rel,
                output_rel=output_rel,
                title=title,
                excerpt=excerpt,
                content=content,
                is_readme=path.name.lower() == "readme.md",
                source_dir=source_rel.parent,
            )
        )
    return notes


def build_directory_nodes(notes: list[Note]) -> dict[Path, DirectoryNode]:
    directory_paths: set[Path] = {Path()}
    for note in notes:
        current = note.source_dir
        while True:
            directory_paths.add(current)
            if current == Path():
                break
            current = current.parent

    nodes: dict[Path, DirectoryNode] = {}
    for source_dir in sorted(directory_paths, key=lambda path: (len(path.parts), [order_key(part) for part in path.parts])):
        if source_dir == Path():
            title = "笔记库"
            output_rel = Path("notes/index.html")
        else:
            title = humanize_segment(source_dir.name)
            output_rel = source_dir_to_output_rel(source_dir) / "index.html"
        nodes[source_dir] = DirectoryNode(source_dir=source_dir, title=title, output_rel=output_rel)

    for note in notes:
        node = nodes[note.source_dir]
        if note.is_readme:
            node.readme = note
        else:
            node.notes.append(note)

    for source_dir, node in nodes.items():
        if source_dir == Path():
            continue
        nodes[source_dir.parent].children.append(node)

    for node in nodes.values():
        node.notes.sort(key=lambda note: order_key(note.source_path.name))
        node.children.sort(key=lambda child: order_key(child.source_dir.name if child.source_dir != Path() else ""))
    return nodes


def breadcrumb_items_for_dir(node: DirectoryNode) -> list[tuple[str, str | None]]:
    crumbs: list[tuple[str, str | None]] = [
        ("首页", relative_href(node.output_rel, Path("index.html"))),
        ("笔记", relative_href(node.output_rel, Path("notes/index.html"))),
    ]
    if node.source_dir == Path():
        crumbs[-1] = ("笔记", None)
        return crumbs

    path_accumulator = Path()
    for index, part in enumerate(node.source_dir.parts):
        path_accumulator = path_accumulator / part
        title = humanize_segment(part)
        is_last = index == len(node.source_dir.parts) - 1
        href = None if is_last else relative_href(node.output_rel, source_dir_to_output_rel(path_accumulator) / "index.html")
        crumbs.append((title, href))
    return crumbs


def breadcrumb_items_for_note(note: Note) -> list[tuple[str, str | None]]:
    crumbs: list[tuple[str, str | None]] = [
        ("首页", relative_href(note.output_rel, Path("index.html"))),
        ("笔记", relative_href(note.output_rel, Path("notes/index.html"))),
    ]
    path_accumulator = Path()
    for part in note.source_dir.parts:
        path_accumulator = path_accumulator / part
        href = relative_href(note.output_rel, source_dir_to_output_rel(path_accumulator) / "index.html")
        crumbs.append((humanize_segment(part), href))
    crumbs.append((note.title, None))
    return crumbs


def render_note_links(note: Note, current_output: Path) -> str:
    href = relative_href(current_output, note.output_rel)
    excerpt = html.escape(note.excerpt) if note.excerpt else "自动从 Markdown 源稿生成。"
    return (
        '<div class="note-item">'
        f'<h3><a href="{href}">{html.escape(note.title)}</a></h3>'
        f"<p>{excerpt}</p>"
        "</div>"
    )


def render_directory_link(node: DirectoryNode, current_output: Path) -> str:
    href = relative_href(current_output, node.output_rel)
    summary = html.escape(node.readme.excerpt) if node.readme and node.readme.excerpt else "自动汇总这个目录下的 Markdown 页面。"
    return (
        '<div class="note-item">'
        f'<h3><a href="{href}">{html.escape(node.title)}</a></h3>'
        f"<p>{summary}</p>"
        "</div>"
    )


def render_directory_page(node: DirectoryNode, nodes: dict[Path, DirectoryNode]) -> str:
    root_prefix = root_prefix_for(node.output_rel)
    description = node.readme.excerpt if node.readme and node.readme.excerpt else "这个目录下的 Markdown 会自动发布到网页。"
    source_dir_label = f"content/{node.source_dir.as_posix()}".rstrip("/.")
    if source_dir_label == "content":
        source_dir_label = "content/"

    sections: list[str] = []
    if node.readme:
        article_html = render_markdown(strip_leading_h1(node.readme.content), node.readme.source_path, node.output_rel)
        sections.append(f'<section class="page-section article">{article_html}</section>')

    if node.children:
        child_items = "".join(render_directory_link(child, node.output_rel) for child in node.children)
        sections.append(
            '<section class="page-section">'
            "<h2>子目录</h2>"
            f'<div class="note-grid">{child_items}</div>'
            "</section>"
        )

    if node.notes:
        note_items = "".join(render_note_links(note, node.output_rel) for note in node.notes)
        sections.append(
            '<section class="page-section">'
            "<h2>本目录文章</h2>"
            f'<div class="note-grid">{note_items}</div>'
            "</section>"
        )

    if not sections:
        sections.append(
            '<section class="page-section">'
            "<h2>还没有内容</h2>"
            '<p class="tiny">这个目录还没有可发布的 Markdown。</p>'
            "</section>"
        )

    article_count = len(node.notes) + (1 if node.readme else 0)
    child_count = len(node.children)
    meta_html = (
        '<section class="page-section">'
        "<h2>自动发布说明</h2>"
        "<ul>"
        f"<li>源目录：<code>{source_dir_label}</code></li>"
        f"<li>当前文章数：{article_count}</li>"
        f"<li>子目录数：{child_count}</li>"
        "<li>这个页面由 <code>scripts/build_notes.py</code> 自动生成。</li>"
        "</ul>"
        "</section>"
    )

    body_html = (
        '<div class="subject-grid">'
        f'<div class="rail">{"".join(sections)}</div>'
        f'<aside class="rail">{meta_html}</aside>'
        "</div>"
    )
    return page_shell(
        title=node.title,
        description=description,
        body_html=body_html,
        root_prefix=root_prefix,
        crumbs=breadcrumb_items_for_dir(node),
    )


def render_note_page(note: Note, nodes: dict[Path, DirectoryNode]) -> str:
    root_prefix = root_prefix_for(note.output_rel)
    directory_node = nodes[note.source_dir]
    article_html = render_markdown(strip_leading_h1(note.content), note.source_path, note.output_rel)
    sibling_notes = [item for item in directory_node.notes if item.output_rel != note.output_rel]
    sibling_links = "".join(render_note_links(item, note.output_rel) for item in sibling_notes[:8])
    sibling_section = (
        '<section class="page-section">'
        "<h2>同目录其他文章</h2>"
        f'<div class="note-grid">{sibling_links}</div>'
        "</section>"
        if sibling_links
        else ""
    )
    directory_href = relative_href(note.output_rel, directory_node.output_rel)
    meta_html = (
        '<section class="page-section">'
        "<h2>页面信息</h2>"
        "<ul>"
        f"<li>所属目录：<a href=\"{directory_href}\">{html.escape(directory_node.title)}</a></li>"
        f"<li>源文件：<code>content/{note.source_rel.as_posix()}</code></li>"
        "<li>这篇页面由 <code>scripts/build_notes.py</code> 自动生成。</li>"
        "</ul>"
        "</section>"
    )
    body_html = (
        '<div class="subject-grid">'
        f'<section class="page-section article">{article_html}</section>'
        f'<aside class="rail">{meta_html}{sibling_section}</aside>'
        "</div>"
    )
    return page_shell(
        title=note.title,
        description=note.excerpt or "自动从 Markdown 源稿生成。",
        body_html=body_html,
        root_prefix=root_prefix,
        crumbs=breadcrumb_items_for_note(note),
    )


def write_output(output_rel: Path, content: str) -> None:
    output_path = DOCS_ROOT / output_rel
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


def reset_notes_root() -> None:
    NOTES_ROOT.mkdir(parents=True, exist_ok=True)
    for html_path in NOTES_ROOT.rglob("*.html"):
        html_path.unlink()
    for path in sorted(NOTES_ROOT.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if not path.is_dir():
            continue
        try:
            path.rmdir()
        except OSError:
            pass


def build() -> None:
    reset_notes_root()

    notes = gather_notes()
    nodes = build_directory_nodes(notes)

    for node in nodes.values():
        write_output(node.output_rel, render_directory_page(node, nodes))

    for note in notes:
        if note.is_readme:
            continue
        write_output(note.output_rel, render_note_page(note, nodes))

    note_pages = len([note for note in notes if not note.is_readme])
    directory_pages = len(nodes)
    print(f"Generated {note_pages} note pages and {directory_pages} directory pages under docs/notes.")


def content_snapshot() -> dict[str, int]:
    snapshot: dict[str, int] = {}
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        snapshot[str(path.relative_to(CONTENT_ROOT))] = path.stat().st_mtime_ns
    return snapshot


def watch(interval: float) -> None:
    build()
    last_snapshot = content_snapshot()
    print(f"Watching content/*.md every {interval:.1f}s. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(interval)
            current_snapshot = content_snapshot()
            if current_snapshot != last_snapshot:
                build()
                last_snapshot = current_snapshot
    except KeyboardInterrupt:
        print("Stopped watching.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build or watch Markdown notes under content/.")
    parser.add_argument("--watch", action="store_true", help="Watch content/*.md and rebuild when files change.")
    parser.add_argument("--interval", type=float, default=2.0, help="Polling interval in seconds for watch mode.")
    args = parser.parse_args()

    if args.watch:
        watch(max(args.interval, 0.5))
    else:
        build()

