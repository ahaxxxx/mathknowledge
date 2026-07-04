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
TRIG_EXERCISE_BANK_FILE = CONTENT_DIR / "02_trigonometry" / "03_trig_exercise_bank_zh.md"
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
    if path == TRIG_FUNCTION_FILE:
        require_contains(
            path,
            text,
            [
                "### 1. 任意角、终边相同角与弧度制",
                "### 2. 单位圆定义：公式从坐标来",
                "### 3. 三角函数线：把不等式和大小比较画出来",
                "### 4. 同角关系与“弦的齐次”",
                "### 5. 诱导公式：先看位置，再看名称",
                "### 6. 两角和差公式：从坐标内积推出来",
                "### 7. 二倍角、降幂与辅助角",
                "### 8. 图像性质与图像变换",
                "### 9. 三角方程、最值与参数",
                "## 分层题型训练",
                "单位圆与三角函数线",
                "恒等变换与角的拼凑",
                "图像性质与参数",
            ],
            errors,
        )
    if path == SOLVE_TRIANGLES_FILE:
        require_contains(
            path,
            text,
            [
                "### 1. 记号系统：先把边角对应钉死",
                "### 2. 正弦定理：有一对边角对应时建立比例",
                "### 3. 余弦定理：夹角、三边和锐钝判断",
                "### 4. 面积公式：把“边边角”转成面积",
                "### 5. 边角互换：把三角函数式翻译成边的语言",
                "### 6. SSA 多解：为什么会有 0、1、2 个三角形",
                "### 7. 形状判断、取值范围与综合题",
                "## 定理选择算法",
                "## 分层题型训练",
                "正余弦定理选择",
                "面积与边角互换",
                "多解、形状与范围",
            ],
            errors,
        )
    solution_count = len(SOLUTION_PATTERN.findall(text))
    if solution_count < 12:
        errors.append(f"{path.name}: expected at least 12 solution blocks, found {solution_count}")
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        if "<details class=\"solution-toggle\">" not in html:
            errors.append(f"{html_path.name}: generated HTML has no solution toggles")
        if re.search(r"<p>\s*\|", html):
            errors.append(f"{html_path.name}: generated HTML leaked an unrendered Markdown table")


def check_trigonometry_exercise_bank(errors: list[str]) -> None:
    text = read_utf8(TRIG_EXERCISE_BANK_FILE, errors)
    if not text:
        return
    require_contains(
        TRIG_EXERCISE_BANK_FILE,
        text,
        [
            "# 三角专题分层题库",
            "## A. 三角函数定义与单位圆",
            "## B. 同角关系与弦的齐次",
            "## C. 诱导公式与恒等变换",
            "## D. 三角函数图像性质",
            "## E. 正余弦定理与解三角形",
            "## 使用建议",
        ],
        errors,
    )
    solution_count = len(SOLUTION_PATTERN.findall(text))
    if solution_count < 100:
        errors.append(
            f"{TRIG_EXERCISE_BANK_FILE.name}: expected at least 100 solution blocks, found {solution_count}"
        )
    html_path = OUTPUT_DIR / "02-trigonometry" / "03-trig-exercise-bank-zh.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        if html_solution_count < 100:
            errors.append(
                f"{html_path.name}: expected at least 100 generated solution toggles, found {html_solution_count}"
            )
        if re.search(r"<p>\s*\|", html):
            errors.append(f"{html_path.name}: generated HTML leaked an unrendered Markdown table")


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
    check_trigonometry_exercise_bank(errors)
    readme = read_utf8(TRIG_README_FILE, errors)
    if readme and "03_trig_exercise_bank_zh.md" not in readme:
        errors.append("README.md: missing trigonometry exercise bank link")

    if errors:
        print("High-school math content check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: summation, trigonometric functions, and solving triangles content are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
