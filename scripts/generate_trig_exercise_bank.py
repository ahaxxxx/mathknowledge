from __future__ import annotations

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

题库按你本地资料中的五个主线重编：三角函数定义、同角三角函数、诱导公式及恒等变化、三角函数性质、正余弦定理。这里先上线 104 道课堂精选题，每道都配可展开解析；本地原题库剩余题目后续可以继续精修进来。

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
            "正切定义域",
            r"写出 $y=\tan x$ 的定义域。",
            r"正切为 $\frac{\sin x}{\cos x}$，所以 $\cos x\ne0$。定义域为 $x\ne\frac\pi2+k\pi,\ k\in\mathbb Z$。",
        ),
        (
            "象限判断",
            r"若 $\sin\alpha<0,\ \cos\alpha>0$，判断 $\alpha$ 终边所在象限。",
            r"纵坐标为负、横坐标为正，终边在第四象限。",
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
        graph_expr = rf"{amp}\sin({w}x{signed_tex(phi)}){signed_int(b)}"
        add(
            item(
                no,
                "周期、值域与平移",
                rf"求函数 $y={graph_expr}$ 的周期、值域和水平平移量。",
                rf"周期 $T={T}$。值域为 ${rng}$。水平平移量要先提出系数 ${w}$，所以是 ${shift}$。",
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
    ]
    for a, b, C, area in area_tasks:
        add(
            item(
                no,
                "面积公式",
                rf"在 $\triangle ABC$ 中，$a={a},\ b={b},\ C={C}^\circ$，求面积。",
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
    ]
    for A, a, b, ans in ssa:
        add(
            item(
                no,
                "SSA 多解判断",
                rf"在 $\triangle ABC$ 中，$A={A}^\circ,\ a={a},\ b={b}$，判断三角形个数。",
                rf"这是 SSA 情形，要用高或正弦值检查。结论：{ans}。",
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

    assert no == 105, no
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT}")
