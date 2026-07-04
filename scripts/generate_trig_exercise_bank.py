from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "09_high_school_math" / "02_trigonometry" / "03_trig_exercise_bank_zh.md"


def sol(text: str) -> str:
    return f":::solution 查看解析\n{text.strip()}\n:::"


def item(no: int, title: str, stem: str, answer: str) -> str:
    return f"#### 题 {no:03d}：{title}\n\n{stem.strip()}\n\n{sol(answer)}\n"


def frac(n: int, d: int) -> str:
    f = Fraction(n, d)
    if f.denominator == 1:
        return str(f.numerator)
    sign = "-" if f.numerator < 0 else ""
    return rf"{sign}\frac{{{abs(f.numerator)}}}{{{f.denominator}}}"


def sq(v: int) -> str:
    return f"({v})^2" if v < 0 else f"{v}^2"


def signed_tex(s: str) -> str:
    return s if s.startswith("-") else f"+{s}"


def signed_int(n: int) -> str:
    if n == 0:
        return ""
    return f"{n:+d}"


def x_term(w: int) -> str:
    if w == 1:
        return "x"
    if w == -1:
        return "-x"
    return f"{w}x"


def diagram(svg: str) -> str:
    return "\n\n:::diagram\n" + svg.strip() + "\n:::\n"


def area_triangle_svg(a: int, b: int, C: int) -> str:
    def fmt(value: float) -> str:
        return f"{value:.1f}".rstrip("0").rstrip(".")

    scale = min(32.0, 270.0 / max(a, 1), 145.0 / max(b, 1))
    cx, cy = 180.0, 176.0
    rad = math.radians(C)
    bx, by = cx + a * scale, cy
    ax, ay = cx + b * scale * math.cos(rad), cy - b * scale * math.sin(rad)

    xs = [ax, bx, cx]
    ys = [ay, by, cy]
    dx = 0.0
    if min(xs) < 42:
        dx = 42 - min(xs)
    if max(xs) + dx > 478:
        dx -= max(xs) + dx - 478
    dy = 0.0
    if min(ys) < 34:
        dy = 34 - min(ys)
    if max(ys) + dy > 205:
        dy -= max(ys) + dy - 205
    ax, bx, cx = ax + dx, bx + dx, cx + dx
    ay, by, cy = ay + dy, by + dy, cy + dy

    arc_r = 34
    arc_start_x, arc_start_y = cx + arc_r, cy
    arc_end_x = cx + arc_r * math.cos(rad)
    arc_end_y = cy - arc_r * math.sin(rad)
    angle_label_x = cx + 46 * math.cos(rad / 2)
    angle_label_y = cy - 46 * math.sin(rad / 2) + 5
    side_b_label_x = (ax + cx) / 2 - 34
    side_b_label_y = (ay + cy) / 2 - 4
    return f"""
<svg viewBox="0 0 520 230" role="img" aria-label="三角形面积公式示意图">
  <polygon points="{fmt(cx)},{fmt(cy)} {fmt(bx)},{fmt(by)} {fmt(ax)},{fmt(ay)}" fill="rgba(15,109,105,0.08)" stroke="#263247" stroke-width="3"></polygon>
  <path d="M {fmt(arc_start_x)} {fmt(arc_start_y)} A {arc_r} {arc_r} 0 0 0 {fmt(arc_end_x)} {fmt(arc_end_y)}" fill="none" stroke="#c85c2b" stroke-width="3"></path>
  <text x="{fmt(ax - 8)}" y="{fmt(ay - 12)}" font-size="18" fill="#263247">A</text>
  <text x="{fmt(bx + 8)}" y="{fmt(by + 6)}" font-size="18" fill="#263247">B</text>
  <text x="{fmt(cx - 18)}" y="{fmt(cy + 24)}" font-size="18" fill="#263247">C</text>
  <text x="{fmt((bx + cx) / 2 - 28)}" y="{fmt(cy + 24)}" font-size="17" fill="#0f6d69">a = {a}</text>
  <text x="{fmt(side_b_label_x)}" y="{fmt(side_b_label_y)}" font-size="17" fill="#0f6d69">b = {b}</text>
  <text x="{fmt(angle_label_x)}" y="{fmt(angle_label_y)}" font-size="17" fill="#c85c2b">C = {C}°</text>
</svg>
"""


def ssa_triangle_svg(A: int, a: int, b: int) -> str:
    def fmt(value: float) -> str:
        return f"{value:.1f}".rstrip("0").rstrip(".")

    scale = min(24.0, 180.0 / max(a, b, 1))
    ax, ay = 96.0, 184.0
    rad = math.radians(A)
    cx = ax + b * scale * math.cos(rad)
    cy = ay - b * scale * math.sin(rad)
    radius = a * scale
    vertical = abs(ay - cy)
    candidates: list[tuple[float, str]] = []
    if radius + 1e-6 >= vertical:
        horizontal = math.sqrt(max(radius * radius - vertical * vertical, 0.0))
        for x in sorted({round(cx - horizontal, 6), round(cx + horizontal, 6)}):
            if x >= ax - 1e-6:
                candidates.append((x, f"B{len(candidates) + 1}"))

    xs = [ax, cx, ax + 390, cx - radius, cx + radius, *(x for x, _ in candidates)]
    ys = [ay, cy, cy - radius, cy + radius]
    dx = 0.0
    if min(xs) < 36:
        dx = 36 - min(xs)
    if max(xs) + dx > 484:
        dx -= max(xs) + dx - 484
    dy = 0.0
    if min(ys) < 36:
        dy = 36 - min(ys)
    if max(ys) + dy > 214:
        dy -= max(ys) + dy - 214
    ax, cx = ax + dx, cx + dx
    ay, cy = ay + dy, cy + dy
    candidates = [(x + dx, label) for x, label in candidates]
    ray_end_x = min(484.0, ax + 390)
    ray_end_y = ay
    angle_end_x = ax + 38 * math.cos(rad)
    angle_end_y = ay - 38 * math.sin(rad)
    points_svg = "\n".join(
        f'  <circle cx="{fmt(x)}" cy="{fmt(ay)}" r="4" fill="#c85c2b"></circle>\n'
        f'  <text x="{fmt(x - 10)}" y="{fmt(ay + 24)}" font-size="16" fill="#c85c2b">{label}</text>'
        for x, label in candidates
    )
    solution_hint = "无交点" if not candidates else ("一个交点" if len(candidates) == 1 else "两个交点")
    return f"""
<svg viewBox="0 0 520 240" role="img" aria-label="SSA 多解判断示意图">
  <line x1="{fmt(ax)}" y1="{fmt(ay)}" x2="{fmt(ray_end_x)}" y2="{fmt(ray_end_y)}" stroke="#263247" stroke-width="3"></line>
  <line x1="{fmt(ax)}" y1="{fmt(ay)}" x2="{fmt(cx)}" y2="{fmt(cy)}" stroke="#263247" stroke-width="3"></line>
  <circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(radius)}" fill="none" stroke="#c85c2b" stroke-width="3" stroke-dasharray="7 7"></circle>
  <line x1="{fmt(cx)}" y1="{fmt(cy)}" x2="{fmt(cx)}" y2="{fmt(ay)}" stroke="#0f6d69" stroke-width="2" stroke-dasharray="5 5"></line>
  <circle cx="{fmt(ax)}" cy="{fmt(ay)}" r="4" fill="#263247"></circle>
  <circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="4" fill="#263247"></circle>
{points_svg}
  <path d="M {fmt(ax + 38)} {fmt(ay)} A 38 38 0 0 0 {fmt(angle_end_x)} {fmt(angle_end_y)}" fill="none" stroke="#0f6d69" stroke-width="3"></path>
  <text x="{fmt(ax - 14)}" y="{fmt(ay + 24)}" font-size="18" fill="#263247">A</text>
  <text x="{fmt(cx + 8)}" y="{fmt(cy - 8)}" font-size="18" fill="#263247">C</text>
  <text x="{fmt((ax + cx) / 2 - 28)}" y="{fmt((ay + cy) / 2 - 8)}" font-size="16" fill="#0f6d69">b = {b}</text>
  <text x="{fmt(cx + 8)}" y="{fmt((cy + ay) / 2)}" font-size="16" fill="#0f6d69">h</text>
  <text x="{fmt(cx + radius * 0.35)}" y="{fmt(cy - radius * 0.2)}" font-size="16" fill="#c85c2b">a = {a}</text>
  <text x="{fmt(ax + 44 * math.cos(rad / 2))}" y="{fmt(ay - 44 * math.sin(rad / 2) + 4)}" font-size="16" fill="#0f6d69">A = {A}°</text>
  <text x="50" y="28" font-size="15" fill="#596579">解析图：以 C 为圆心、a 为半径截射线 AB，得到{solution_hint}</text>
</svg>
"""


def term_tex(coef: int, var: str, *, first: bool = False) -> str:
    if coef == 0:
        return ""
    sign = "-" if coef < 0 else ("" if first else "+")
    mag = abs(coef)
    if var:
        body = var if mag == 1 else f"{mag}{var}"
    else:
        body = str(mag)
    return sign + body


def linear_tex(pairs: list[tuple[int, str]]) -> str:
    out = ""
    for coef, var in pairs:
        if coef == 0:
            continue
        out += term_tex(coef, var, first=not out)
    return out or "0"


def build() -> str:
    parts: list[str] = []
    add = parts.append

    add(
        """# 三角专题分层题库

本页是三角专题的训练库，不替代讲义页。讲义页负责把概念讲透，题库页负责让学生反复练“识别题型、选择方法、检查条件”。

题库按你本地资料中的五个主线重编：三角函数定义、同角三角函数、诱导公式及恒等变化、三角函数性质、正余弦定理。这里先上线 148 道课堂精选题，每道都配可展开解析；本地原题库剩余题目后续可以继续精修进来。

## 使用建议

1. **课堂前**：每次布置 8 到 12 道，要求学生至少准备 1 道讲解。
2. **课堂中**：不要只问答案，追问“为什么选这个公式”“有没有象限或多解条件”。
3. **课堂后**：错题按模块回流，例如错在符号就回到单位圆，错在多解就回到 SSA。
4. **节奏**：先做 A、B、C 打基础，再做 D、E 提升综合。
"""
    )

    no = 1

    add("\n## A. 三角函数定义与单位圆\n")
    points = [(3, 4), (-5, 12), (8, -15), (-7, -24), (5, -12)]
    for x, y in points:
        r2 = x * x + y * y
        r = int(r2**0.5)
        add(
            item(
                no,
                "终边经过点求三角函数值",
                rf"角 $\alpha$ 的终边经过点 $P({x},{y})$，求 $\sin\alpha,\cos\alpha,\tan\alpha$。",
                rf"""先求 $r=\sqrt{{{sq(x)}+{sq(y)}}}={r}$。所以
$$
\sin\alpha={frac(y, r)},\qquad
\cos\alpha={frac(x, r)},\qquad
\tan\alpha={frac(y, x)}.
$$
最后用点所在象限检查符号。""",
            )
        )
        no += 1

    same_terminal = [
        (r"\frac{\pi}{4}", r"\frac{\pi}{4}+2k\pi"),
        (r"-\frac{2\pi}{3}", r"-\frac{2\pi}{3}+2k\pi"),
        (r"\frac{7\pi}{6}", r"\frac{7\pi}{6}+2k\pi"),
        (r"-\frac{5\pi}{4}", r"-\frac{5\pi}{4}+2k\pi"),
        (r"\frac{11\pi}{3}", r"\frac{11\pi}{3}+2k\pi"),
    ]
    for angle, ans in same_terminal:
        add(
            item(
                no,
                "终边相同角",
                rf"写出与角 ${angle}$ 终边相同的所有角。",
                rf"""终边相同的角相差 $2\pi$ 的整数倍，所以全体角为
$$
{ans},\qquad k\in\mathbb Z.
$$""",
            )
        )
        no += 1

    quadrant_tasks = [
        (r"\sin\alpha=\frac35", "第二象限", r"\cos\alpha=-\frac45", r"\tan\alpha=-\frac34"),
        (r"\cos\alpha=-\frac{12}{13}", "第三象限", r"\sin\alpha=-\frac5{13}", r"\tan\alpha=\frac5{12}"),
        (r"\sin\alpha=-\frac{8}{17}", "第四象限", r"\cos\alpha=\frac{15}{17}", r"\tan\alpha=-\frac8{15}"),
        (r"\cos\alpha=\frac7{25}", "第四象限", r"\sin\alpha=-\frac{24}{25}", r"\tan\alpha=-\frac{24}{7}"),
        (r"\sin\alpha=-\frac7{25}", "第三象限", r"\cos\alpha=-\frac{24}{25}", r"\tan\alpha=\frac7{24}"),
    ]
    for given, quad, first, tanv in quadrant_tasks:
        add(
            item(
                no,
                "由一个函数值和象限补全",
                rf"已知 ${given}$，且 $\alpha$ 是{quad}角，求另一个基本函数值与 $\tan\alpha$。",
                rf"""先用 $\sin^2\alpha+\cos^2\alpha=1$ 得到绝对值，再由{quad}决定符号：
$$
{first},\qquad {tanv}.
$$""",
            )
        )
        no += 1

    intervals = [
        (r"\sin x>\frac12", r"\left(\frac\pi6,\frac{5\pi}6\right)"),
        (r"\cos x\le -\frac12", r"\left[\frac{2\pi}3,\frac{4\pi}3\right]"),
        (r"\sin x<0", r"(\pi,2\pi)"),
        (r"\tan x>0", r"\left(0,\frac\pi2\right)\cup\left(\pi,\frac{3\pi}2\right)"),
        (r"\cos x>\frac{\sqrt2}{2}", r"\left[0,\frac\pi4\right)\cup\left(\frac{7\pi}4,2\pi\right)"),
    ]
    for cond, ans in intervals:
        add(
            item(
                no,
                "单位圆解三角不等式",
                rf"在 $[0,2\pi)$ 内解不等式 ${cond}$。",
                rf"""回到单位圆看坐标或斜率符号，可得解集为
$$
{ans}.
$$""",
            )
        )
        no += 1

    misc_a = [
        (
            "弧度角互化",
            r"把 $150^\circ$ 化为弧度，并把 $\frac{7\pi}{6}$ 化为角度。",
            r"$150^\circ=150\cdot\frac{\pi}{180}=\frac{5\pi}{6}$；$\frac{7\pi}{6}=210^\circ$。",
        ),
        (
            "弧度角互化",
            r"把 $225^\circ$ 化为弧度，并把 $\frac{3\pi}{4}$ 化为角度。",
            r"$225^\circ=225\cdot\frac{\pi}{180}=\frac{5\pi}{4}$；$\frac{3\pi}{4}=135^\circ$。",
        ),
        (
            "弧度角互化",
            r"把 $-60^\circ$ 化为弧度，并把 $-\frac{5\pi}{6}$ 化为角度。",
            r"$-60^\circ=-\frac{\pi}{3}$；$-\frac{5\pi}{6}=-150^\circ$。",
        ),
        (
            "弧度角互化",
            r"把 $330^\circ$ 化为弧度，并把 $\frac{4\pi}{3}$ 化为角度。",
            r"$330^\circ=\frac{11\pi}{6}$；$\frac{4\pi}{3}=240^\circ$。",
        ),
        (
            "弧度角互化",
            r"把 $72^\circ$ 化为弧度，并把 $\frac{5\pi}{3}$ 化为角度。",
            r"$72^\circ=\frac{2\pi}{5}$；$\frac{5\pi}{3}=300^\circ$。",
        ),
        (
            "正切定义域",
            r"写出 $y=\tan x$ 的定义域。",
            r"正切为 $\frac{\sin x}{\cos x}$，所以 $\cos x\ne0$。定义域为 $x\ne\frac\pi2+k\pi,\ k\in\mathbb Z$。",
        ),
        (
            "正切定义域",
            r"写出 $y=\tan 2x$ 的定义域。",
            r"令 $2x\ne\frac\pi2+k\pi$，得 $x\ne\frac\pi4+\frac{k\pi}{2},\ k\in\mathbb Z$。",
        ),
        (
            "正切定义域",
            r"写出 $y=\tan(x+\frac\pi3)$ 的定义域。",
            r"令 $x+\frac\pi3\ne\frac\pi2+k\pi$，得 $x\ne\frac\pi6+k\pi,\ k\in\mathbb Z$。",
        ),
        (
            "正切定义域",
            r"写出 $y=\tan(3x-\frac\pi6)$ 的定义域。",
            r"令 $3x-\frac\pi6\ne\frac\pi2+k\pi$，得 $x\ne\frac{2\pi}{9}+\frac{k\pi}{3},\ k\in\mathbb Z$。",
        ),
        (
            "正切定义域",
            r"写出 $y=\tan(\frac\pi4-x)$ 的定义域。",
            r"令 $\frac\pi4-x\ne\frac\pi2+k\pi$，得 $x\ne-\frac\pi4+k\pi,\ k\in\mathbb Z$。",
        ),
        (
            "象限判断",
            r"若 $\sin\alpha<0,\ \cos\alpha>0$，判断 $\alpha$ 终边所在象限。",
            r"纵坐标为负、横坐标为正，终边在第四象限。",
        ),
        (
            "象限判断",
            r"若 $\sin\alpha>0,\ \cos\alpha<0$，判断 $\alpha$ 终边所在象限。",
            r"纵坐标为正、横坐标为负，终边在第二象限。",
        ),
        (
            "象限判断",
            r"若 $\tan\alpha>0,\ \sin\alpha<0$，判断 $\alpha$ 终边所在象限。",
            r"$\tan\alpha>0$ 说明正弦、余弦同号；又 $\sin\alpha<0$，所以二者都为负，终边在第三象限。",
        ),
        (
            "象限判断",
            r"若 $\cos\alpha<0,\ \tan\alpha<0$，判断 $\alpha$ 终边所在象限。",
            r"$\tan\alpha<0$ 说明正弦、余弦异号；又 $\cos\alpha<0$，所以 $\sin\alpha>0$，终边在第二象限。",
        ),
        (
            "象限判断",
            r"若 $\sin\alpha\cos\alpha>0,\ \cos\alpha<0$，判断 $\alpha$ 终边所在象限。",
            r"$\sin\alpha\cos\alpha>0$ 说明正弦、余弦同号；又 $\cos\alpha<0$，所以终边在第三象限。",
        ),
    ]
    for title, stem, answer in misc_a:
        add(item(no, title, stem, answer))
        no += 1

    add("\n## B. 同角关系与弦的齐次\n")
    hom = [
        (2, 3, -1, 1, 2),
        (3, -2, 2, 1, -1),
        (1, 4, 2, -3, 3),
        (5, 1, 1, -1, 2),
        (2, -5, 3, 1, -2),
        (4, 3, 1, 2, 1),
        (1, -2, 2, 5, 4),
        (3, 4, -1, 2, -3),
    ]
    for a, b, c, d, t in hom:
        val = Fraction(a * t + b, c * t + d)
        numerator = linear_tex([(a, r"\sin\alpha"), (b, r"\cos\alpha")])
        denominator = linear_tex([(c, r"\sin\alpha"), (d, r"\cos\alpha")])
        tan_numerator = linear_tex([(a, r"\tan\alpha"), (b, "")])
        tan_denominator = linear_tex([(c, r"\tan\alpha"), (d, "")])
        add(
            item(
                no,
                "弦的齐次",
                rf"""已知 $\tan\alpha={t}$，求
$$
\frac{{{numerator}}}{{{denominator}}}.
$$""",
                rf"""分子分母同除以 $\cos\alpha$，得
$$
\frac{{{tan_numerator}}}{{{tan_denominator}}}
={frac(val.numerator, val.denominator)}.
$$""",
            )
        )
        no += 1

    b_more = [
        (
            r"\sin\alpha=\frac{7}{25}",
            "第二象限",
            r"\cos\alpha=-\frac{24}{25}",
            r"\tan\alpha=-\frac7{24}",
        ),
        (
            r"\cos\alpha=-\frac35",
            "第二象限",
            r"\sin\alpha=\frac45",
            r"\tan\alpha=-\frac43",
        ),
        (
            r"\tan\alpha=-\frac34",
            "第四象限",
            r"\sin\alpha=-\frac35",
            r"\cos\alpha=\frac45",
        ),
        (
            r"\tan\alpha=\frac{12}{5}",
            "第三象限",
            r"\sin\alpha=-\frac{12}{13}",
            r"\cos\alpha=-\frac5{13}",
        ),
        (
            r"\cos\alpha=\frac5{13}",
            "第四象限",
            r"\sin\alpha=-\frac{12}{13}",
            r"\tan\alpha=-\frac{12}{5}",
        ),
    ]
    for given, quad, s1, s2 in b_more:
        add(
            item(
                no,
                "同角关系补值",
                rf"已知 ${given}$，且 $\alpha$ 是{quad}角，求其余两个基本三角函数值。",
                rf"""用同角关系先求绝对值，再由{quad}决定符号：
$$
{s1},\qquad {s2}.
$$""",
            )
        )
        no += 1

    sumdiff = [
        (r"\sin\alpha+\cos\alpha=\frac65", r"\sin\alpha\cos\alpha", r"\frac{11}{50}"),
        (r"\sin\alpha-\cos\alpha=\frac13", r"\sin\alpha\cos\alpha", r"\frac49"),
        (r"\tan\alpha=2", r"\sin\alpha\cos\alpha", r"\frac25"),
        (r"\tan\alpha=-3", r"\frac{1+\tan^2\alpha}{1-\tan^2\alpha}", r"-\frac54"),
        (r"\sin\alpha+\cos\alpha=\sqrt2", r"\sin\alpha\cos\alpha", r"\frac12"),
    ]
    for given, target, ans in sumdiff:
        add(
            item(
                no,
                "同角关系变形",
                rf"已知 ${given}$，求 ${target}$。",
                rf"""把已知式平方或化为 $\tan\alpha$。由 $\sin^2\alpha+\cos^2\alpha=1$ 整理可得
$$
{target}={ans}.
$$""",
            )
        )
        no += 1

    b_last = [
        (
            r"\frac{\sin^2\alpha-\cos^2\alpha}{\sin^2\alpha+\cos^2\alpha}",
            r"\tan\alpha=2",
            r"\frac{4-1}{4+1}=\frac35",
        ),
        (
            r"\frac{2\sin\alpha\cos\alpha}{\sin^2\alpha+\cos^2\alpha}",
            r"\tan\alpha=\frac12",
            r"\frac{2t}{1+t^2}=\frac{1}{1+\frac14}=\frac45",
        ),
        (
            r"\sin^2\alpha",
            r"\cos\alpha=-\frac{8}{17}",
            r"1-\frac{64}{289}=\frac{225}{289}",
        ),
        (
            r"\cos^2\alpha",
            r"\sin\alpha=-\frac{9}{41}",
            r"1-\frac{81}{1681}=\frac{1600}{1681}",
        ),
        (
            r"\frac{\sin^2\alpha}{\cos^2\alpha}",
            r"\tan\alpha=-2",
            r"\tan^2\alpha=4",
        ),
    ]
    for target, given, ans in b_last:
        add(
            item(
                no,
                "平方关系与齐次化",
                rf"已知 ${given}$，求 ${target}$。",
                rf"""使用 $\sin^2\alpha+\cos^2\alpha=1$ 或令 $t=\tan\alpha$，得
$$
{target}={ans}.
$$""",
            )
        )
        no += 1

    add("\n## C. 诱导公式与恒等变换\n")
    induce = [
        (r"\sin(\pi+x)+\cos(\frac\pi2+x)", r"-2\sin x"),
        (r"\cos(\pi-x)-\sin(\frac\pi2-x)", r"-2\cos x"),
        (r"\sin(2\pi-x)+\cos(\pi+x)", r"-\sin x-\cos x"),
        (r"\cos(-x)+\sin(\pi+x)", r"\cos x-\sin x"),
        (r"\sin(\frac{3\pi}{2}-x)+\cos(\pi+x)", r"-\cos x-\cos x=-2\cos x"),
    ]
    for expr, ans in induce:
        add(
            item(
                no,
                "诱导公式化简",
                rf"化简：$${expr}$$。",
                rf"""逐项回到单位圆对称关系：
$$
{expr}={ans}.
$$""",
            )
        )
        no += 1

    double = [
        (r"\sin\alpha=\frac35,\ \alpha\text{为锐角}", r"\cos2\alpha", r"\frac7{25}"),
        (r"\cos\alpha=\frac{12}{13},\ \alpha\text{为锐角}", r"\sin2\alpha", r"\frac{120}{169}"),
        (r"\sin\alpha=\frac{5}{13},\ \alpha\text{为锐角}", r"\cos2\alpha", r"\frac{119}{169}"),
        (r"\tan\alpha=2", r"\tan2\alpha", r"-\frac43"),
        (r"\cos2\alpha=\frac13", r"\sin^2\alpha", r"\frac13"),
    ]
    for given, target, ans in double:
        add(
            item(
                no,
                "二倍角与降幂",
                rf"已知 ${given}$，求 ${target}$。",
                rf"""选择二倍角或降幂公式：
$$
{target}={ans}.
$$""",
            )
        )
        no += 1

    angle_sum = [
        (r"\sin\alpha=\frac35,\ \cos\beta=\frac{12}{13}", r"\alpha,\beta\text{均为锐角}", r"\sin(\alpha+\beta)", r"\frac{56}{65}"),
        (r"\cos\alpha=\frac45,\ \sin\beta=\frac5{13}", r"\alpha,\beta\text{均为锐角}", r"\cos(\alpha+\beta)", r"\frac{33}{65}"),
        (r"\sin\alpha=\frac{8}{17},\ \sin\beta=\frac35", r"\alpha,\beta\text{均为锐角}", r"\cos(\alpha-\beta)", r"\frac{84}{85}"),
        (r"\tan\alpha=2,\ \tan\beta=3", r"\alpha,\beta\text{均为锐角}", r"\tan(\alpha+\beta)", r"-1"),
        (r"\tan\alpha=\frac12,\ \tan\beta=\frac13", r"\alpha,\beta\text{均为锐角}", r"\tan(\alpha-\beta)", r"\frac17"),
    ]
    for given, cond, target, ans in angle_sum:
        add(
            item(
                no,
                "角的拼凑",
                rf"已知 ${given}$，且 ${cond}$，求 ${target}$。",
                rf"""先补出对应的正弦、余弦或正切，再用和差角公式，得到
$$
{target}={ans}.
$$""",
            )
        )
        no += 1

    aux = [
        (r"\sqrt3\sin x+\cos x", r"2\sin(x+\frac\pi6)", "最大值 2，最小值 -2"),
        (r"\sin x-\cos x", r"\sqrt2\sin(x-\frac\pi4)", r"最大值 $\sqrt2$，最小值 $-\sqrt2$"),
        (r"3\sin x+4\cos x", r"5\sin(x+\varphi)", "最大值 5，最小值 -5"),
        (r"5\cos x-12\sin x", r"13\cos(x+\varphi)", "最大值 13，最小值 -13"),
        (r"2\sin x+2\cos x+1", r"2\sqrt2\sin(x+\frac\pi4)+1", r"最大值 $2\sqrt2+1$"),
    ]
    for expr, form, ans in aux:
        add(
            item(
                no,
                "辅助角公式",
                rf"把 ${expr}$ 化成一个三角函数，并写出最值信息。",
                rf"""辅助角化为
$$
{expr}={form}.
$$
所以 {ans}。""",
            )
        )
        no += 1

    add("\n## D. 三角函数图像性质\n")
    graphs = [
        (2, 3, r"-\frac\pi2", -1, r"\frac{2\pi}{3}", "[-3,1]", r"\frac\pi6\text{ 向右}"),
        (3, 2, r"\frac\pi3", 1, r"\pi", "[-2,4]", r"\frac\pi6\text{ 向左}"),
        (1, 4, r"-\pi", 2, r"\frac\pi2", "[1,3]", r"\frac\pi4\text{ 向右}"),
        (4, 1, r"\frac\pi2", -3, r"2\pi", "[-7,1]", r"\frac\pi2\text{ 向左}"),
        (5, 2, r"-\frac\pi4", 0, r"\pi", "[-5,5]", r"\frac\pi8\text{ 向右}"),
    ]
    for A, w, phi, b, T, rng, shift in graphs:
        amp = "" if A == 1 else str(A)
        graph_expr = rf"{amp}\sin({x_term(w)}{signed_tex(phi)}){signed_int(b)}"
        add(
            item(
                no,
                "周期、值域与平移",
                rf"求函数 $y={graph_expr}$ 的周期、值域和水平平移量。",
                rf"周期 $T={T}$。值域为 ${rng}$。水平平移量要先提出系数 ${w}$，所以是 ${shift}$。",
            )
        )
        no += 1

    monotonic_tasks = [
        (
            r"y=\sin(2x+\frac\pi3)",
            "单调递增区间",
            r"\left[-\frac{5\pi}{12}+k\pi,\frac\pi{12}+k\pi\right]",
            r"$\sin u$ 在 $\left[-\frac\pi2+2k\pi,\frac\pi2+2k\pi\right]$ 上递增。令 $u=2x+\frac\pi3$ 后解不等式即可。",
        ),
        (
            r"y=\cos(2x-\frac\pi3)",
            "单调递减区间",
            r"\left[\frac\pi6+k\pi,\frac{2\pi}3+k\pi\right]",
            r"$\cos u$ 在 $[2k\pi,\pi+2k\pi]$ 上递减。令 $u=2x-\frac\pi3$。",
        ),
        (
            r"y=\tan(2x+\frac\pi4)",
            "单调递增区间",
            r"\left(-\frac{3\pi}8+\frac{k\pi}2,\frac\pi8+\frac{k\pi}2\right)",
            r"$\tan u$ 在每个定义区间 $\left(-\frac\pi2+k\pi,\frac\pi2+k\pi\right)$ 上递增。",
        ),
        (
            r"y=-2\sin(x-\frac\pi6)+1",
            "单调递增区间",
            r"\left[\frac{2\pi}3+2k\pi,\frac{5\pi}3+2k\pi\right]",
            r"前面的负号会把正弦的递减区间变成原函数的递增区间。令 $u=x-\frac\pi6$，取 $u\in\left[\frac\pi2+2k\pi,\frac{3\pi}2+2k\pi\right]$。",
        ),
        (
            r"y=\sin(3x-\frac\pi2)",
            "单调递增区间",
            r"\left[\frac{2k\pi}{3},\frac\pi3+\frac{2k\pi}{3}\right]",
            r"令 $u=3x-\frac\pi2$，把 $u$ 放进正弦的递增区间，再除以 3。",
        ),
        (
            r"y=\cos(x+\frac\pi4)",
            "单调递增区间",
            r"\left[-\frac{5\pi}4+2k\pi,-\frac\pi4+2k\pi\right]",
            r"$\cos u$ 在 $[-\pi+2k\pi,2k\pi]$ 上递增。令 $u=x+\frac\pi4$。",
        ),
    ]
    for expr, target, ans, reason in monotonic_tasks:
        add(
            item(
                no,
                "单调区间",
                rf"求函数 ${expr}$ 的{target}。",
                rf"""核心不是背结论，而是令 $u=\omega x+\varphi$，回到母函数单调区间。
{reason}
所以{target}为
$$
{ans},\qquad k\in\mathbb Z.
$$""",
            )
        )
        no += 1

    symmetry_tasks = [
        (
            r"y=\sin(2x+\frac\pi3)",
            r"x=\frac\pi{12}+\frac{k\pi}{2}",
            r"\left(-\frac\pi6+\frac{k\pi}{2},0\right)",
            r"$\sin u$ 的对称轴来自 $u=\frac\pi2+k\pi$，对称中心来自 $u=k\pi$。",
        ),
        (
            r"y=\cos(3x-\frac\pi2)",
            r"x=\frac\pi6+\frac{k\pi}{3}",
            r"\left(\frac\pi3+\frac{k\pi}{3},0\right)",
            r"$\cos u$ 的对称轴来自 $u=k\pi$，对称中心来自 $u=\frac\pi2+k\pi$。",
        ),
        (
            r"y=\tan(2x-\frac\pi6)+1",
            r"\text{无对称轴}",
            r"\left(\frac\pi{12}+\frac{k\pi}{2},1\right)",
            r"$\tan u$ 没有对称轴；中心来自 $u=k\pi$，上下平移后中心纵坐标为 1。",
        ),
        (
            r"y=2\sin(x-\frac\pi4)-3",
            r"x=\frac{3\pi}4+k\pi",
            r"\left(\frac\pi4+k\pi,-3\right)",
            r"$\sin u$ 的轴是峰谷位置 $u=\frac\pi2+k\pi$，中心纵坐标随 $b=-3$ 下移。",
        ),
        (
            r"y=-\cos(2x+\frac\pi6)+2",
            r"x=-\frac\pi{12}+\frac{k\pi}{2}",
            r"\left(\frac\pi6+\frac{k\pi}{2},2\right)",
            r"$\cos u$ 的轴仍来自 $u=k\pi$；负号只交换峰谷，不改变轴和中心的位置。",
        ),
        (
            r"y=\tan(3x+\frac\pi3)",
            r"\text{无对称轴}",
            r"\left(-\frac\pi9+\frac{k\pi}{3},0\right)",
            r"$\tan u$ 的对称中心来自 $u=k\pi$。令 $u=3x+\frac\pi3$ 后解出 $x$。",
        ),
    ]
    for expr, axis, center, reason in symmetry_tasks:
        add(
            item(
                no,
                "对称轴与对称中心",
                rf"求函数 ${expr}$ 的对称轴和对称中心。",
                rf"""{reason}
所以对称轴为
$$
{axis},
$$
对称中心为
$$
{center},\qquad k\in\mathbb Z.
$$""",
            )
        )
        no += 1

    interval_ranges = [
        (
            r"y=\sin x,\quad x\in\left[\frac\pi6,\frac{5\pi}6\right]",
            r"\left[\frac12,1\right]",
            r"这个区间经过 $\frac\pi2$，所以 $\sin x$ 能取到最大值 1，端点值都是 $\frac12$。",
        ),
        (
            r"y=2\sin(2x-\frac\pi3)+1,\quad x\in\left[0,\frac\pi2\right]",
            r"[1-\sqrt3,3]",
            r"令 $u=2x-\frac\pi3$，则 $u\in\left[-\frac\pi3,\frac{2\pi}3\right]$，$\sin u\in\left[-\frac{\sqrt3}2,1\right]$。",
        ),
        (
            r"y=\cos(x+\frac\pi4),\quad x\in\left[0,\frac\pi2\right]",
            r"\left[-\frac{\sqrt2}{2},\frac{\sqrt2}{2}\right]",
            r"令 $u=x+\frac\pi4$，则 $u\in\left[\frac\pi4,\frac{3\pi}4\right]$，余弦从正到负且经过 $\frac\pi2$。",
        ),
        (
            r"y=\tan(x-\frac\pi4),\quad x\in\left[\frac\pi4,\frac\pi3\right]",
            r"[0,2-\sqrt3]",
            r"令 $u=x-\frac\pi4$，则 $u\in\left[0,\frac\pi{12}\right]$，正切在该区间递增，$\tan\frac\pi{12}=2-\sqrt3$。",
        ),
        (
            r"y=\sin^2x,\quad x\in\left[\frac\pi6,\frac{2\pi}3\right]",
            r"\left[\frac14,1\right]",
            r"区间内包含 $\frac\pi2$，所以 $\sin^2x$ 最大为 1；端点平方分别是 $\frac14$ 与 $\frac34$，最小为 $\frac14$。",
        ),
    ]
    for expr, ans, reason in interval_ranges:
        add(
            item(
                no,
                "给定区间上的值域",
                rf"求函数 ${expr}$ 的值域。",
                rf"""给定区间值域题必须先看内层角的实际范围，不能直接套全局值域。
{reason}
所以值域为
$$
{ans}.
$$""",
            )
        )
        no += 1

    reconstruction_tasks = [
        (
            r"函数形如 $y=A\sin(\omega x)+b$，其中 $A>0,\omega>0$。已知最大值为 3，最小值为 -1，最小正周期为 $\pi$，求解析式。",
            r"y=2\sin2x+1",
            r"$A=\frac{3-(-1)}2=2$，$b=\frac{3+(-1)}2=1$，$T=\pi$ 给出 $\omega=2$。",
        ),
        (
            r"函数形如 $y=A\cos(\omega x)+b$，其中 $A>0,\omega>0$。已知最大值为 4，最小值为 0，最小正周期为 $\frac{2\pi}{3}$，求解析式。",
            r"y=2\cos3x+2",
            r"$A=2,\ b=2$，且 $\omega=\frac{2\pi}{T}=3$。",
        ),
        (
            r"函数形如 $y=A\sin(2x+\varphi)+b$，其中 $A>0$。已知最大值为 5，最小值为 -1，且 $x=\frac\pi{12}$ 时取得最大值，求一个解析式。",
            r"y=3\sin(2x+\frac\pi3)+2",
            r"$A=3,\ b=2$。最大值要求 $2\cdot\frac\pi{12}+\varphi=\frac\pi2$，所以 $\varphi=\frac\pi3$。",
        ),
        (
            r"函数形如 $y=A\cos(2x+\varphi)+b$，其中 $A>0$。已知最大值为 1，最小值为 -5，且 $x=\frac\pi6$ 时取得最小值，求一个解析式。",
            r"y=3\cos(2x+\frac{2\pi}3)-2",
            r"$A=3,\ b=-2$。最小值要求 $2\cdot\frac\pi6+\varphi=\pi$，所以 $\varphi=\frac{2\pi}3$。",
        ),
        (
            r"函数形如 $y=A\sin(\omega x+\varphi)$，其中 $A>0,\omega>0$。已知最大值为 2，相邻两个最大点的距离为 $\pi$，且 $x=\frac\pi6$ 时取得最大值，求一个解析式。",
            r"y=2\sin(2x+\frac\pi6)",
            r"$A=2$，相邻最大点距离就是周期，所以 $T=\pi,\omega=2$。最大值要求 $2\cdot\frac\pi6+\varphi=\frac\pi2$，得 $\varphi=\frac\pi6$。",
        ),
    ]
    for stem, ans, reason in reconstruction_tasks:
        add(
            item(
                no,
                "由图像性质反求解析式",
                stem,
                rf"""先由最高点、最低点、周期和特殊点依次确定 $A,b,\omega,\varphi$。
{reason}
所以可取
$$
{ans}.
$$""",
            )
        )
        no += 1

    equations = [
        (r"\sin x=\frac12", r"x=2k\pi+\frac\pi6\text{ 或 }x=2k\pi+\frac{5\pi}6"),
        (r"\cos x=-\frac12", r"x=2k\pi+\frac{2\pi}3\text{ 或 }x=2k\pi+\frac{4\pi}3"),
        (r"\tan x=1", r"x=k\pi+\frac\pi4"),
        (r"2\sin x-1=0", r"x=2k\pi+\frac\pi6\text{ 或 }x=2k\pi+\frac{5\pi}6"),
        (r"\cos 2x=0", r"x=\frac\pi4+\frac{k\pi}{2}"),
    ]
    for eq, ans in equations:
        add(
            item(
                no,
                "三角方程",
                rf"解方程 ${eq}$。",
                rf"""先写一个周期内的基本解，再加周期。全体解为
$$
{ans},\qquad k\in\mathbb Z.
$$""",
            )
        )
        no += 1

    ranges = [
        (r"2\sin^2x-4\sin x+1", "[-1,7]"),
        (r"\cos^2x+2\cos x", "[-1,3]"),
        (r"3-2\sin x", "[1,5]"),
        (r"1+4\cos^2x", "[1,5]"),
        (r"2\sin x\cos x+1", "[0,2]"),
    ]
    for expr, ans in ranges:
        add(
            item(
                no,
                "值域",
                rf"求函数 $f(x)={expr}$ 的值域。",
                rf"""根据题型使用换元、平方范围或二倍角。注意换元范围，如 $-1\le\sin x\le1$。值域为
$$
{ans}.
$$""",
            )
        )
        no += 1

    sym = [
        (r"y=\sin(2x+\frac\pi3)", r"$T=\pi$"),
        (r"y=\cos(3x-\frac\pi2)", r"$T=\frac{2\pi}{3}$"),
        (r"y=|\sin x|", r"$T=\pi$"),
        (r"y=\tan(2x)", r"$T=\frac\pi2$"),
        (r"y=2\cos x+1", r"关于 $y$ 轴对称"),
    ]
    for stem, ans in sym:
        add(
            item(
                no,
                "周期与对称",
                rf"判断函数 ${stem}$ 的周期或对称性。",
                rf"从基础函数的周期和变换出发，结论为：{ans}。",
            )
        )
        no += 1

    add("\n## E. 正余弦定理与解三角形\n")
    sine_law = [
        (30, 45, 4, r"4\sqrt2"),
        (45, 60, 6, r"3\sqrt6"),
        (30, 60, 5, r"5\sqrt3"),
        (60, 45, 8, r"\frac{8\sqrt6}{3}"),
        (30, 90, 4, "8"),
    ]
    for A, B, a, bval in sine_law:
        add(
            item(
                no,
                "正弦定理",
                rf"在 $\triangle ABC$ 中，$A={A}^\circ,\ B={B}^\circ,\ a={a}$，求 $b$。",
                rf"""已有边角对应 $(a,A)$，用正弦定理：
$$
b=a\frac{{\sin B}}{{\sin A}}={bval}.
$$""",
            )
        )
        no += 1

    cosine_law = [
        (3, 4, 60, r"\sqrt{13}"),
        (5, 7, 60, r"\sqrt{39}"),
        (6, 8, 120, r"2\sqrt{37}"),
        (4, 6, 60, r"2\sqrt7"),
        (7, 8, 60, r"\sqrt{57}"),
    ]
    for b, c, A, aval in cosine_law:
        add(
            item(
                no,
                "余弦定理",
                rf"在 $\triangle ABC$ 中，$b={b},\ c={c},\ A={A}^\circ$，求 $a$。",
                rf"""两边夹角，用余弦定理：
$$
a^2=b^2+c^2-2bc\cos A,\qquad a={aval}.
$$""",
            )
        )
        no += 1

    area_tasks = [
        (5, 6, 120, r"\frac{15\sqrt3}{2}"),
        (8, 6, 30, "12"),
        (4, 5, 60, r"5\sqrt3"),
        (7, 10, 45, r"\frac{35\sqrt2}{2}"),
        (9, 4, 30, "9"),
    ]
    for a, b, C, area in area_tasks:
        add(
            item(
                no,
                "面积公式",
                rf"在 $\triangle ABC$ 中，$a={a},\ b={b},\ C={C}^\circ$，求面积。"
                + diagram(area_triangle_svg(a, b, C)),
                rf"""$C$ 是边 $a,b$ 的夹角，所以
$$
S=\frac12ab\sin C={area}.
$$""",
            )
        )
        no += 1

    ssa = [
        (30, 4, 10, "无解，因为 $\\sin B=\\frac54>1$"),
        (30, 5, 6, "两解，因为高 $h=3$，且 $h<a<b$"),
        (30, 3, 6, "一解，因为 $a=h=3$"),
        (120, 5, 4, "一解，因为钝角 $A$ 已知且 $a>b$"),
        (30, 8, 4, "一解，因为 $a>b$，对边更长，另一边不会再摆出第二个交点"),
    ]
    for A, a, b, ans in ssa:
        add(
            item(
                no,
                "SSA 多解判断",
                rf"在 $\triangle ABC$ 中，$A={A}^\circ,\ a={a},\ b={b}$，判断三角形个数。",
                diagram(ssa_triangle_svg(A, a, b))
                + rf"这是 SSA 情形，要用高或正弦值检查。结论：{ans}。",
            )
        )
        no += 1

    shapes = [
        (r"a:b:c=3:4:5", "直角三角形"),
        (r"a^2=b^2+c^2", "$A=90^\\circ$，直角三角形"),
        (r"\sin A=\sin B", "在三角形中 $A=B$，所以 $a=b$，为等腰三角形"),
        (r"a=b=c", "等边三角形"),
        (r"a=2,\ b=3,\ \triangle ABC\text{为锐角三角形}", r"$\sqrt5<c<\sqrt{13}$"),
        (r"a=4,\ b=5,\ c=6", r"$\cos C=\frac18$，最大角为锐角"),
        (r"\sin A:\sin B:\sin C=2:3:4", r"$a:b:c=2:3:4$"),
        (r"S=12,\ a=8,\ b=6", r"$\sin C=\frac12$，所以 $C=30^\circ$ 或 $150^\circ$，还需结合其他条件判断"),
    ]
    for given, ans in shapes:
        add(
            item(
                no,
                "形状、范围与边角互换",
                rf"已知 ${given}$，写出可推出的结论。",
                rf"把条件翻译成边、角或面积关系，得到：{ans}。",
            )
        )
        no += 1

    assert no == 149, no
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT}")
