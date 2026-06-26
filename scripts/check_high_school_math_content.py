from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "09_high_school_math"
OUTPUT_DIR = ROOT / "docs" / "notes" / "09-high-school-math"

SUMMATION_FILE = CONTENT_DIR / "01_sequences" / "02_summation_zh.md"
TRIG_FUNCTION_FILE = CONTENT_DIR / "02_trigonometry" / "01_trig_functions_zh.md"
SOLVE_TRIANGLES_FILE = CONTENT_DIR / "02_trigonometry" / "02_solving_triangles_zh.md"
TRIG_README_FILE = CONTENT_DIR / "02_trigonometry" / "README.md"

SOLUTION_PATTERN = re.compile(r"^:::solution\b", re.MULTILINE)


def read_utf8(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT).as_posix()}")
        return ""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{path.name}: not valid UTF-8 ({exc})")
        return ""
    if "\ufffd" in text:
        errors.append(f"{path.name}: contains Unicode replacement characters")
    return text


def require_contains(path: Path, text: str, required: list[str], errors: list[str]) -> None:
    for item in required:
        if item not in text:
            errors.append(f"{path.name}: missing required content: {item}")


def check_summation(errors: list[str]) -> None:
    text = read_utf8(SUMMATION_FILE, errors)
    if not text:
        return
    require_contains(
        SUMMATION_FILE,
        text,
        [
            "## 2. 方法选择地图",
            "## 3. 公式法",
            "## 4. 分组求和与并项求和",
            "## 5. 裂项相消",
            "## 6. 错位相减法",
            "## 7. 倒序相加法",
            "## 8. 奇偶、周期与绝对值分段",
            "a_n=S_n-S_{n-1}",
            "## 14. 今晚课堂讲法",
            "## 15. 课后作业建议",
            "\\sum_{k=1}^{n}kq^{k-1}",
            "\\sum_{k=1}^{n}[a+(k-1)d]q^{k-1}",
        ],
        errors,
    )


def check_trigonometry_page(path: Path, html_path: Path, errors: list[str]) -> None:
    text = read_utf8(path, errors)
    if not text:
        return
    require_contains(
        path,
        text,
        [
            "## 研究对象",
            "## 核心知识结构",
            "## 方法识别",
            "## 典型例题",
            "## 自我训练",
            "## 费曼讲题任务",
        ],
        errors,
    )
    solution_count = len(SOLUTION_PATTERN.findall(text))
    if solution_count < 6:
        errors.append(f"{path.name}: expected at least 6 solution blocks, found {solution_count}")
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        if "<details class=\"solution-toggle\">" not in html:
            errors.append(f"{html_path.name}: generated HTML has no solution toggles")


def main() -> int:
    errors: list[str] = []
    check_summation(errors)
    read_utf8(TRIG_README_FILE, errors)
    check_trigonometry_page(
        TRIG_FUNCTION_FILE,
        OUTPUT_DIR / "02-trigonometry" / "01-trig-functions-zh.html",
        errors,
    )
    check_trigonometry_page(
        SOLVE_TRIANGLES_FILE,
        OUTPUT_DIR / "02-trigonometry" / "02-solving-triangles-zh.html",
        errors,
    )

    if errors:
        print("High-school math content check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: summation, trigonometric functions, and solving triangles content are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
