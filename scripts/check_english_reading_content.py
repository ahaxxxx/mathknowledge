from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "10_english" / "01_grammar_reading"
OUTPUT_DIR = ROOT / "docs" / "notes" / "10-english" / "01-grammar-reading"

MODULE_FILES = [
    "01_clause_skeletons_zh.md",
    "02_tense_aspect_zh.md",
    "03_modality_counterfactuals_zh.md",
    "04_noun_phrases_reference_zh.md",
    "05_complement_subordinate_clauses_zh.md",
    "06_relatives_apposition_zh.md",
    "07_nonfinite_clauses_zh.md",
    "08_negation_scope_zh.md",
    "09_comparison_parallelism_ellipsis_zh.md",
    "10_information_structure_zh.md",
    "11_nominalization_compression_zh.md",
    "12_cohesion_reference_zh.md",
    "13_stance_evidentiality_zh.md",
    "14_academic_argument_zh.md",
]
MORPHOLOGY_FILE = "15_morphology_reference_zh.md"

REQUIRED_HEADINGS = [
    "## 本章研究的问题",
    "## 核心原理",
    "## 逐句精读",
    "## 精读材料",
    "## 自我训练",
    "## 迁移与反思",
]

SENTENCE_PATTERN = re.compile(r"^### 句子\s+\d+", re.MULTILINE)
EXERCISE_PATTERN = re.compile(r"^### 训练\s+\d+", re.MULTILINE)
SOLUTION_PATTERN = re.compile(r"^:::solution\b", re.MULTILINE)

ACADEMIC_CONTEXT = "**训练语境：学术科研**"
EVERYDAY_CONTEXT = "**训练语境：真实生活**"


class ParagraphTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_paragraph = False
        self.current: list[str] = []
        self.paragraphs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "p":
            self.in_paragraph = True
            self.current = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "p" and self.in_paragraph:
            text = "".join(self.current)
            self.paragraphs.append(normalize_space(text))
            self.in_paragraph = False
            self.current = []

    def handle_data(self, data: str) -> None:
        if self.in_paragraph:
            self.current.append(data)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def canonical_visible_text(text: str) -> str:
    return re.sub(r"\s+", "", text.replace("`", ""))


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{path.name}: not valid UTF-8 ({exc})")
        return ""
    if "\ufffd" in text:
        errors.append(f"{path.name}: contains Unicode replacement characters")
    return text


def check_core_module(path: Path, text: str, errors: list[str]) -> None:
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{path.name}: missing heading {heading}")

    sentence_count = len(SENTENCE_PATTERN.findall(text))
    exercise_count = len(EXERCISE_PATTERN.findall(text))
    solution_count = len(SOLUTION_PATTERN.findall(text))
    academic_count = text.count(ACADEMIC_CONTEXT)
    everyday_count = text.count(EVERYDAY_CONTEXT)

    if sentence_count < 8:
        errors.append(f"{path.name}: expected at least 8 sentence analyses, found {sentence_count}")
    if exercise_count != 10:
        errors.append(f"{path.name}: expected 10 exercises, found {exercise_count}")
    if solution_count != 10:
        errors.append(f"{path.name}: expected 10 solution blocks, found {solution_count}")
    if academic_count != 6 or everyday_count != 4:
        errors.append(
            f"{path.name}: expected 6 academic and 4 everyday exercise contexts, "
            f"found {academic_count} and {everyday_count}"
        )
    check_generated_intro_not_duplicated(path, text, errors)


def first_plain_paragraph(markdown_text: str) -> str:
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
        paragraph = [line]
        i += 1
        while i < len(lines):
            current = lines[i].strip()
            if not current or current.startswith("#") or current.startswith(">"):
                break
            paragraph.append(current)
            i += 1
        return " ".join(paragraph)
    return ""


def output_html_path(source_path: Path) -> Path:
    return OUTPUT_DIR / f"{source_path.stem.replace('_', '-')}.html"


def check_generated_intro_not_duplicated(path: Path, text: str, errors: list[str]) -> None:
    output_path = output_html_path(path)
    if not output_path.exists():
        return
    intro = first_plain_paragraph(text)
    if not intro:
        return
    html_text = output_path.read_text(encoding="utf-8")
    parser = ParagraphTextParser()
    parser.feed(html_text)
    expected_intro = canonical_visible_text(intro)
    occurrences = sum(
        1 for paragraph in parser.paragraphs if canonical_visible_text(paragraph) == expected_intro
    )
    if occurrences != 1:
        errors.append(
            f"{output_path.name}: expected intro paragraph once in generated HTML, found {occurrences}"
        )


def check_morphology(path: Path, text: str, errors: list[str]) -> None:
    required = [
        "## 词形推断的边界",
        "## 前缀系统",
        "## 词根系统",
        "## 后缀系统",
        "## 词族系统",
        "## 自我训练",
    ]
    for heading in required:
        if heading not in text:
            errors.append(f"{path.name}: missing heading {heading}")

    exercise_count = len(EXERCISE_PATTERN.findall(text))
    solution_count = len(SOLUTION_PATTERN.findall(text))
    academic_count = text.count(ACADEMIC_CONTEXT)
    everyday_count = text.count(EVERYDAY_CONTEXT)
    if exercise_count != 10:
        errors.append(f"{path.name}: expected 10 exercises, found {exercise_count}")
    if solution_count != 10:
        errors.append(f"{path.name}: expected 10 solution blocks, found {solution_count}")
    if academic_count != 6 or everyday_count != 4:
        errors.append(
            f"{path.name}: expected 6 academic and 4 everyday exercise contexts, "
            f"found {academic_count} and {everyday_count}"
        )


def main() -> int:
    errors: list[str] = []
    total_exercises = 0
    total_solutions = 0
    total_academic = 0
    total_everyday = 0

    for filename in MODULE_FILES:
        path = CONTENT_DIR / filename
        if not path.exists():
            errors.append(f"missing module: {filename}")
            continue
        text = read_utf8(path, errors)
        check_core_module(path, text, errors)
        total_exercises += len(EXERCISE_PATTERN.findall(text))
        total_solutions += len(SOLUTION_PATTERN.findall(text))
        total_academic += text.count(ACADEMIC_CONTEXT)
        total_everyday += text.count(EVERYDAY_CONTEXT)

    morphology_path = CONTENT_DIR / MORPHOLOGY_FILE
    if not morphology_path.exists():
        errors.append(f"missing reference: {MORPHOLOGY_FILE}")
    else:
        morphology_text = read_utf8(morphology_path, errors)
        check_morphology(morphology_path, morphology_text, errors)
        total_exercises += len(EXERCISE_PATTERN.findall(morphology_text))
        total_solutions += len(SOLUTION_PATTERN.findall(morphology_text))
        total_academic += morphology_text.count(ACADEMIC_CONTEXT)
        total_everyday += morphology_text.count(EVERYDAY_CONTEXT)

    if total_exercises != 150:
        errors.append(f"curriculum: expected 150 exercises, found {total_exercises}")
    if total_solutions != 150:
        errors.append(f"curriculum: expected 150 solutions, found {total_solutions}")
    if total_academic != 90 or total_everyday != 60:
        errors.append(
            "curriculum: expected exact 60/40 context balance "
            f"(90 academic, 60 everyday), found {total_academic} and {total_everyday}"
        )

    if errors:
        print("English reading content check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: 14 modules, 1 morphology reference, 150 exercises, 150 solutions.")
    print("PASS: exercise contexts are exactly 60% academic and 40% everyday.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
