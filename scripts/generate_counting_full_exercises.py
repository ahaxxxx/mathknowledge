from __future__ import annotations

from pathlib import Path

import generate_analytic_geometry_full_exercises as base


SITE_ROOT = Path(__file__).resolve().parents[1]
CONTENT_FILE = (
    SITE_ROOT
    / "content"
    / "09_high_school_math"
    / "06_counting_combinatorics"
    / "07_counting_local_full_exercises_zh.md"
)
ASSET_DIR = SITE_ROOT / "docs" / "assets" / "counting-local"
ASSET_HREF_PREFIX = "../../../assets/counting-local"

POINTS = [
    ("33", "两个计数原理"),
    ("34", "排列、组合"),
    ("35", "二项式定理"),
]


def main() -> int:
    base.ASSET_DIR = ASSET_DIR
    base.ASSET_HREF_PREFIX = ASSET_HREF_PREFIX
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    CONTENT_FILE.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "# 计数原理与排列组合：考点 33-35 全量本地题库",
        "",
        "这一页把本地一轮复习资料中考点 33 到考点 35 的练习题按原考点整理出来。题干中的公式、图形和原 Word 图片会一起呈现；解析版内容折叠在“查看解析版原文”里，适合课后抽题、限时训练和查漏补缺。",
        "",
        "返回专题首页：[计数原理与排列组合](./README.md)。配套训练：[计数原理与排列组合：分层训练题库](./06_counting_expression_drills_zh.md)。",
        "",
        "## 使用说明",
        "",
        "1. 这页是本地资料池，不建议第一次学习时直接通刷。",
        "2. 课堂上先用讲义建立分类、分步、有序、无序和二项式通项，再按考点从这里抽题。",
        "3. 学生讲题时必须说出：对象是什么、先分类还是先分步、是否有序、有没有重复或遗漏。",
        "",
    ]

    global_index = 1
    summary: list[tuple[str, str, int, int, int]] = []
    for point, title in POINTS:
        print(f"processing 考点 {point} {title}", flush=True)
        original = base.find_docx(point, source="练习", version="原卷版")
        solved = base.find_docx(point, source="练习", version="解析版")
        _, questions = base.split_questions(base.docx_blocks(original, f"ct{point}-q"))
        _, solutions = base.split_questions(base.docx_blocks(solved, f"ct{point}-a"))
        print(f"  extracted questions={len(questions)} solutions={len(solutions)}", flush=True)
        aligned_solutions = min(len(questions), len(solutions))
        summary.append((point, title, len(questions), len(solutions), aligned_solutions))

        lines.extend([f"## 考点 {point}：{title}", ""])
        lines.extend(
            [
                f"本组来自 `{original.name}`；原卷共抽取 {len(questions)} 道题，解析版原始抽取 {len(solutions)} 道，可对齐显示 {aligned_solutions} 道。",
                "",
            ]
        )
        for index, question in enumerate(questions):
            lines.append(base.question_to_markdown(question, global_index))
            lines.append("")
            solution = solutions[index] if index < len(solutions) else None
            if solution:
                lines.append(base.solution_to_markdown(solution))
                lines.append("")
            global_index += 1

    total_questions = sum(item[2] for item in summary)
    total_solutions = sum(item[4] for item in summary)
    lines.extend(
        [
            "## 抽取统计",
            "",
            f"- 全量原卷题目：{total_questions} 道。",
            f"- 可折叠解析版题块：{total_solutions} 道。",
            "",
        ]
    )
    for point, title, q_count, raw_a_count, aligned_count in summary:
        lines.append(f"- 考点 {point} {title}：原卷 {q_count} 道，解析版原始抽取 {raw_a_count} 道，可对齐显示 {aligned_count} 道。")

    CONTENT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {CONTENT_FILE}")
    print(f"questions={total_questions} solutions={total_solutions} assets={sum(1 for _ in ASSET_DIR.iterdir())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
