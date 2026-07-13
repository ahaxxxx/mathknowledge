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
TRIG_LOCAL_SUPPLEMENT_FILE = CONTENT_DIR / "02_trigonometry" / "04_trig_local_review_supplement_zh.md"
TRIG_README_FILE = CONTENT_DIR / "02_trigonometry" / "README.md"
VECTOR_README_FILE = CONTENT_DIR / "03_plane_vectors" / "README.md"
VECTOR_LESSON_FILE = CONTENT_DIR / "03_plane_vectors" / "01_plane_vectors_zh.md"
VECTOR_EXERCISES_FILE = CONTENT_DIR / "03_plane_vectors" / "02_plane_vectors_exercises_zh.md"
VECTOR_ADVANCED_EXERCISES_FILE = CONTENT_DIR / "03_plane_vectors" / "03_plane_vectors_advanced_exercises_zh.md"
SOLID_README_FILE = CONTENT_DIR / "04_solid_geometry" / "README.md"
SOLID_LESSON_FILE = CONTENT_DIR / "04_solid_geometry" / "01_solid_geometry_spatial_vectors_zh.md"
SOLID_EXERCISES_FILE = CONTENT_DIR / "04_solid_geometry" / "02_solid_geometry_exercises_zh.md"
SOLID_FULL_EXERCISES_FILE = CONTENT_DIR / "04_solid_geometry" / "03_solid_geometry_local_full_exercises_zh.md"

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
                "单调区间不要直接背变形后的结论",
                "对称轴和对称中心也不是另一套新公式",
                "由图像反求解析式时",
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
            "单调区间",
            "对称轴与对称中心",
            "给定区间上的值域",
            "由图像性质反求解析式",
            "## E. 正余弦定理与解三角形",
            "## 使用建议",
        ],
        errors,
    )
    solution_count = len(SOLUTION_PATTERN.findall(text))
    if solution_count < 145:
        errors.append(
            f"{TRIG_EXERCISE_BANK_FILE.name}: expected at least 145 solution blocks, found {solution_count}"
        )
    html_path = OUTPUT_DIR / "02-trigonometry" / "03-trig-exercise-bank-zh.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        if html_solution_count < 145:
            errors.append(
                f"{html_path.name}: expected at least 145 generated solution toggles, found {html_solution_count}"
            )
        if re.search(r"<p>\s*\|", html):
            errors.append(f"{html_path.name}: generated HTML leaked an unrendered Markdown table")


def check_trigonometry_local_supplement(errors: list[str]) -> None:
    text = read_utf8(TRIG_LOCAL_SUPPLEMENT_FILE, errors)
    if not text:
        return
    require_contains(
        TRIG_LOCAL_SUPPLEMENT_FILE,
        text,
        [
            "# 三角函数与解三角形：本地一轮复习补充",
            "## 本地资料梳理",
            "## 方法补充",
            "## A. 终边相同角、象限与区域",
            "## B. 三角函数定义与终边点",
            "## C. 同角关系与弦的齐次",
            "## D. 诱导公式与恒等化简",
            "## E. 三角函数性质：周期、定义域、单调、对称",
            "## F. 图像变换、值域与参数",
            "## G. 正余弦定理选择、面积与外接圆",
            "## H. 边角互换、多解与范围",
        ],
        errors,
    )
    solution_count = len(SOLUTION_PATTERN.findall(text))
    if solution_count < 32:
        errors.append(
            f"{TRIG_LOCAL_SUPPLEMENT_FILE.name}: expected at least 32 solution blocks, found {solution_count}"
        )

    html_path = OUTPUT_DIR / "02-trigonometry" / "04-trig-local-review-supplement-zh.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        if html_solution_count < 32:
            errors.append(
                f"{html_path.name}: expected at least 32 generated solution toggles, found {html_solution_count}"
            )


def check_plane_vectors(errors: list[str]) -> None:
    readme = read_utf8(VECTOR_README_FILE, errors)
    if readme:
        require_contains(
            VECTOR_README_FILE,
            readme,
            [
                "# 平面向量",
                "平面向量：从几何语言到代数工具",
                "平面向量专项练习：每类至少 5 题",
                "平面向量进阶题库：本地资料梳理与高考题型补充",
            ],
            errors,
        )

    lesson = read_utf8(VECTOR_LESSON_FILE, errors)
    if lesson:
        require_contains(
            VECTOR_LESSON_FILE,
            lesson,
            [
                "## 研究对象",
                "## 核心知识结构",
                "向量加法：首尾相接",
                "数乘与共线",
                "基底表示",
                "数量积",
                "## 费曼讲题任务",
                ":::diagram",
            ],
            errors,
        )
        if len(SOLUTION_PATTERN.findall(lesson)) < 3:
            errors.append(f"{VECTOR_LESSON_FILE.name}: expected at least 3 solution blocks")

    exercises = read_utf8(VECTOR_EXERCISES_FILE, errors)
    if exercises:
        require_contains(
            VECTOR_EXERCISES_FILE,
            exercises,
            [
                "## A. 向量线性运算与几何意义",
                "## B. 共线与基底分解",
                "## C. 坐标运算与点的位置",
                "## D. 数量积、夹角与投影",
                "## E. 长度、垂直与最值",
                "## F. 向量与三角形综合",
            ],
            errors,
        )
        solution_count = len(SOLUTION_PATTERN.findall(exercises))
        if solution_count < 30:
            errors.append(f"{VECTOR_EXERCISES_FILE.name}: expected at least 30 solution blocks, found {solution_count}")

    html_path = OUTPUT_DIR / "03-plane-vectors" / "02-plane-vectors-exercises-zh.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        if html_solution_count < 30:
            errors.append(
                f"{html_path.name}: expected at least 30 generated solution toggles, found {html_solution_count}"
            )

    advanced = read_utf8(VECTOR_ADVANCED_EXERCISES_FILE, errors)
    if advanced:
        require_contains(
            VECTOR_ADVANCED_EXERCISES_FILE,
            advanced,
            [
                "# 平面向量进阶题库：本地资料梳理与高考题型补充",
                "## 本地资料梳理",
                "## 题型地图",
                "## A. 线性运算、相等向量与命题辨析",
                "## B. 基底分解、分点与参数表示",
                "## C. 共线、三点共线与取值范围",
                "## D. 坐标法、数量积与夹角",
                "## E. 投影、垂直与长度平方",
                "## F. 向量与三角形形状判断",
                "## G. 向量应用：最值、范围与轨迹",
                "## H. 高考小题速度训练",
                "## 本地考法对照表",
            ],
            errors,
        )
        solution_count = len(SOLUTION_PATTERN.findall(advanced))
        if solution_count < 40:
            errors.append(
                f"{VECTOR_ADVANCED_EXERCISES_FILE.name}: expected at least 40 solution blocks, found {solution_count}"
            )

    advanced_html_path = OUTPUT_DIR / "03-plane-vectors" / "03-plane-vectors-advanced-exercises-zh.html"
    if advanced_html_path.exists():
        html = advanced_html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        if html_solution_count < 40:
            errors.append(
                f"{advanced_html_path.name}: expected at least 40 generated solution toggles, found {html_solution_count}"
            )


def check_solid_geometry(errors: list[str]) -> None:
    readme = read_utf8(SOLID_README_FILE, errors)
    if readme:
        require_contains(
            SOLID_README_FILE,
            readme,
            [
                "# 立体几何与空间向量",
                "立体几何与空间向量：讲义",
                "立体几何与空间向量：图形题库",
                "立体几何与空间向量：考点 22-28 全量本地题库",
            ],
            errors,
        )

    lesson = read_utf8(SOLID_LESSON_FILE, errors)
    if lesson:
        require_contains(
            SOLID_LESSON_FILE,
            lesson,
            [
                "# 立体几何与空间向量：从图形到坐标",
                "## 本地资料梳理",
                "## 方法地图",
                "## 图形语言",
                "## 空间向量语言",
                "## 费曼讲题任务",
                ":::diagram",
            ],
            errors,
        )

    exercises = read_utf8(SOLID_EXERCISES_FILE, errors)
    if exercises:
        require_contains(
            SOLID_EXERCISES_FILE,
            exercises,
            [
                "# 立体几何与空间向量：图形题库",
                "## 本地资料题型地图",
                "## A. 空间平行",
                "## B. 空间垂直",
                "## C. 体积、表面积与等体积",
                "## D. 几何法求空间角",
                "## E. 空间向量求角",
                "## F. 空间向量求距离",
                "## G. 外接球模型",
            ],
            errors,
        )
        solution_count = len(SOLUTION_PATTERN.findall(exercises))
        diagram_count = exercises.count(":::diagram")
        if solution_count < 21:
            errors.append(f"{SOLID_EXERCISES_FILE.name}: expected at least 21 solution blocks, found {solution_count}")
        if diagram_count < 21:
            errors.append(f"{SOLID_EXERCISES_FILE.name}: expected at least 21 diagrams, found {diagram_count}")

    html_path = OUTPUT_DIR / "04-solid-geometry" / "02-solid-geometry-exercises-zh.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        html_diagram_count = html.count("math-diagram")
        if html_solution_count < 21:
            errors.append(
                f"{html_path.name}: expected at least 21 generated solution toggles, found {html_solution_count}"
            )
        if html_diagram_count < 21:
            errors.append(
                f"{html_path.name}: expected at least 21 generated diagrams, found {html_diagram_count}"
            )

    full_exercises = read_utf8(SOLID_FULL_EXERCISES_FILE, errors)
    if full_exercises:
        require_contains(
            SOLID_FULL_EXERCISES_FILE,
            full_exercises,
            [
                "# 立体几何与空间向量：考点 22-28 全量本地题库",
                "## 考点 22：空间几何平行问题",
                "## 考点 23：空间几何垂直问题",
                "## 考点 24：空间几何体体积及表面积",
                "## 考点 25：几何法解空间角",
                "## 考点 26：空间向量求空间角",
                "## 考点 27：空间向量求空间距离",
                "## 考点 28：空间几何体外接球",
                "全量原卷题目：132 道",
            ],
            errors,
        )
        question_count = len(re.findall(r"^### 题\s+\d+", full_exercises, re.MULTILINE))
        solution_count = len(SOLUTION_PATTERN.findall(full_exercises))
        image_count = full_exercises.count("local-docx-image")
        if question_count < 132:
            errors.append(f"{SOLID_FULL_EXERCISES_FILE.name}: expected at least 132 questions, found {question_count}")
        if solution_count < 132:
            errors.append(f"{SOLID_FULL_EXERCISES_FILE.name}: expected at least 132 solution blocks, found {solution_count}")
        if image_count < 300:
            errors.append(f"{SOLID_FULL_EXERCISES_FILE.name}: expected at least 300 embedded images, found {image_count}")

    full_html_path = OUTPUT_DIR / "04-solid-geometry" / "03-solid-geometry-local-full-exercises-zh.html"
    if full_html_path.exists():
        html = full_html_path.read_text(encoding="utf-8")
        question_count = html.count("<h3>题 ")
        html_solution_count = html.count("<details class=\"solution-toggle\">")
        html_image_count = html.count("local-docx-image")
        if question_count < 132:
            errors.append(f"{full_html_path.name}: expected at least 132 generated questions, found {question_count}")
        if html_solution_count < 132:
            errors.append(
                f"{full_html_path.name}: expected at least 132 generated solution toggles, found {html_solution_count}"
            )
        if html_image_count < 300:
            errors.append(f"{full_html_path.name}: expected at least 300 generated images, found {html_image_count}")


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
    check_trigonometry_local_supplement(errors)
    check_plane_vectors(errors)
    check_solid_geometry(errors)
    readme = read_utf8(TRIG_README_FILE, errors)
    if readme and "03_trig_exercise_bank_zh.md" not in readme:
        errors.append("README.md: missing trigonometry exercise bank link")
    if readme and "04_trig_local_review_supplement_zh.md" not in readme:
        errors.append("README.md: missing local trigonometry supplement link")

    if errors:
        print("High-school math content check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: summation, trigonometry, plane vectors, and solid geometry content are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
