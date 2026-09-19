from __future__ import annotations

from pathlib import Path
from solution_matching import match_solutions, PENDING

import generate_analytic_geometry_full_exercises as base


SITE_ROOT = Path(__file__).resolve().parents[1]
CONTENT_FILE = (
    SITE_ROOT
    / "content"
    / "09_high_school_math"
    / "07_derivatives"
    / "09_derivative_local_full_exercises_zh.md"
)
ASSET_DIR = SITE_ROOT / "docs" / "assets" / "derivative-local"
ASSET_HREF_PREFIX = "../../../assets/derivative-local"

POINTS = [
    ("49", "利用导数求切线方程"),
    ("50", "利用导数求单调性"),
    ("51", "单调性中的分类讨论"),
    ("52", "构造函数常见方法"),
    ("53", "利用导数求极值与最值"),
    ("54", "导数与不等式"),
    ("55", "导数与函数零点"),
]


def main() -> int:
    base.ASSET_DIR = ASSET_DIR
    base.ASSET_HREF_PREFIX = ASSET_HREF_PREFIX
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    CONTENT_FILE.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "# 导数：考点 49-55 全量本地题库",
        "",
        "这一页保留本地一轮复习资料的原题、公式图片与图形。它是课后抽题资料池，不替代前面的讲义和手写推导：第一次学习请先完成定义、定理和方法来源，再到这里限时训练。",
        "",
        "返回专题首页：[导数](./README.md)。优先训练：[导数：分层训练与费曼讲题](./08_derivative_drills_zh.md)。",
        "",
        "## 使用纪律",
        "",
        "1. 先写定义域，再写导函数与符号表；不能跳过参数分类或端点检查。",
        "2. 遇到恒成立、存在、唯一、恰有几个零点，先把量词翻译成范围、最值或函数图像语言。",
        "3. 解析版原文只在点击后显示；其中的图片是原 Word 公式或图形，用于保留题目条件。",
        "",
    ]

    global_index = 1
    summary: list[tuple[str, str, int, int, int]] = []
    for point, title in POINTS:
        print(f"processing 考点 {point} {title}", flush=True)
        original = base.find_docx(point, source="练习", version="原卷版")
        solved = base.find_docx(point, source="练习", version="解析版")
        _, questions = base.split_questions(base.docx_blocks(original, f"dv{point}-q"))
        _, solutions = base.split_questions(base.docx_blocks(solved, f"dv{point}-a"))
        matched_solutions = match_solutions(questions, solutions)
        aligned = sum(item is not None for item in matched_solutions)
        summary.append((point, title, len(questions), len(solutions), aligned))
        print(f"  questions={len(questions)} solutions={len(solutions)}", flush=True)

        lines.extend(
            [
                f"## 考点 {point}：{title}",
                "",
                f"原卷抽取 {len(questions)} 道，解析版抽取 {len(solutions)} 道。",
                "",
            ]
        )
        for index, question in enumerate(questions):
            lines.append(base.question_to_markdown(question, global_index))
            lines.append("")
            if matched_solutions[index] is not None:
                lines.append(base.solution_to_markdown(matched_solutions[index]))
                lines.append("")
            else:
                lines.extend(
                    [
                        ":::solution 查看教师补充说明",
                        "",
                        "解析待核验：原题号或完整题干未能唯一匹配，不能按顺序猜配。请由教师核对题源后补充。",
                        "",
                        ":::",
                        "",
                    ]
                )
            global_index += 1

    total_questions = sum(item[2] for item in summary)
    total_solutions = sum(item[4] for item in summary)
    lines.extend(["## 抽取统计", "", f"- 原卷题目：{total_questions} 道。", f"- 对应解析题块：{total_solutions} 道。", ""])
    for point, title, q_count, solution_count, aligned in summary:
        lines.append(f"- 考点 {point} {title}：原卷 {q_count} 道，解析 {solution_count} 道，题号与完整题干匹配 {aligned} 道。")

    CONTENT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {CONTENT_FILE}")
    print(f"questions={total_questions} solutions={total_solutions} assets={sum(1 for _ in ASSET_DIR.iterdir())}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
