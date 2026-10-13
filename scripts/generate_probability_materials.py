from pathlib import Path
from fractions import Fraction as F
from math import comb
import shutil

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT.parent
OUT = ROOT / 'content/09_high_school_math/08_probability'
ASSETS = ROOT / 'docs/assets/probability-sources'


def tex(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else rf'\frac{{{x.numerator}}}{{{x.denominator}}}'


def main():
    groups = []
    def group(title, prompt, items):
        assert len(items) == 6
        groups.append((title, prompt, items))

    items = []
    for n, k in [(5, 2), (6, 2), (6, 3), (7, 3), (8, 4), (9, 4)]:
        good = sum(comb(k, j)*comb(n-k, 2-j) for j in range(1, 3) if j <= k and 2-j <= n-k)
        p = F(good, comb(n, 2))
        items.append((f'{n} 人中有 {k} 名女生，所有二人小组等可能被选中。求至少一名女生的概率，并分别用正面分类和对立事件计算。',
          rf'样本点为无序二人集合，共 $\binom{{{n}}}2={comb(n,2)}$ 个。至少一女的对立是全男，故 $P=1-\binom{{{n-k}}}2/\binom{{{n}}}2={tex(p)}$。正面分为恰一女和两女，计数为 ${k}\times{n-k}+\binom{{{k}}}2={good}$，除以相同分母得到同一结果。两类互斥且覆盖目标事件，概率在 0 与 1 之间。'))
    group('A. 等可能计数与对立事件', '解释为什么不能把“全男”和“有女生”看成两个等可能样本点。', items)

    items = []
    for a, b, c in [(F(1,2),F(1,3),F(1,6)), (F(3,5),F(2,5),F(1,5)),(F(2,3),F(1,2),F(1,3)),(F(3,4),F(1,4),F(1,8)),(F(2,5),F(3,10),F(1,10)),(F(4,5),F(1,2),F(2,5))]:
        union = a+b-c
        items.append((rf'已知 $P(A)={tex(a)},P(B)={tex(b)},P(A\cap B)={tex(c)}$。求恰有一个发生、至少一个发生、都不发生的概率，并判断互斥与独立。',
          rf'把全集分成仅 A、交集、仅 B、都不发生四块，权重依次为 ${tex(a-c)},{tex(c)},{tex(b-c)},{tex(1-union)}$，均非负且和为 1。恰一发生为 $P(A)+P(B)-2P(A\cap B)={tex(a+b-2*c)}$；至少一发生为 ${tex(union)}$；都不发生为 ${tex(1-union)}$。交集为正，所以不互斥。乘积 $P(A)P(B)={tex(a*b)}$ '+('等于交集，故独立。' if a*b == c else '不等于交集，故不独立。')))
    group('B. 事件运算与概念辨析', '指出互斥、对立、独立的判据各是什么。', items)

    items = []
    for red, white in [(3,2),(4,3),(5,2),(5,4),(6,3),(7,4)]:
        n = red+white
        den = comb(n,2)-comb(white,2)
        num = comb(red,2)
        items.append((f'袋中 {red} 红 {white} 白，球可区分且任意二球集合等可能。不放回抽 2 球，已知至少有一红，求两球均红的条件概率。',
          rf'记 $A$ 为两红，$B$ 为至少一红。$A\subset B$ 且 $P(B)>0$。原样本点等可能，条件样本空间含 $\binom{{{n}}}2-\binom{{{white}}}2={den}$ 个结果；其中 A 含 $\binom{{{red}}}2={num}$ 个。因此 $P(A\mid B)={tex(F(num,den))}$。无条件概率为 ${tex(F(num,comb(n,2)))}$，条件概率不小于它，符合已排除全白结果的事实。'))
    group('C. 条件概率与缩小样本空间', '比较“至少一红”与“第一球为红”：为何两种条件一般给出不同答案？', items)

    items = []
    for a, u, v in [(F(1,2),F(1,10),F(1,5)),(F(3,5),F(1,10),F(1,5)),(F(2,3),F(1,4),F(1,2)),(F(3,4),F(1,5),F(2,5)),(F(2,5),F(1,8),F(1,4)),(F(4,5),F(1,20),F(1,10))]:
        d=a*u+(1-a)*v
        items.append((rf'随机产品来自甲厂的概率为 ${tex(a)}$，其余来自乙厂。甲乙次品率为 ${tex(u)},{tex(v)}$。求抽到次品的概率，以及已知次品来自甲厂的概率。',
          rf'来源是互斥完备分类，甲次品路径权重为 ${tex(a*u)}$，乙次品路径权重为 ${tex((1-a)*v)}$。全概率 $P(D)={tex(a)}\cdot{tex(u)}+{tex(1-a)}\cdot{tex(v)}={tex(d)}>0$。按条件概率 $P(甲\mid D)=P(甲\cap D)/P(D)={tex(a*u/d)}$。两种来源的后验概率之和为 1；甲的次品率更低，观察次品后甲来源概率下降。'))
    group('D. 全概率与贝叶斯追溯', '画两层来源树，说明为什么不能只把两个次品率相加。', items)

    items=[]
    for m in range(1,7):
        items.append((rf'$X$ 的不同取值为 $0,{m},{3*m}$，概率依次为 $1/4,1/2,c$。求 $c,E(X),D(X)$，再求 $Y=2X-{m}$ 的期望与方差。',
          rf'概率归一给出 $c=1-1/4-1/2=1/4$，各项非负。$E(X)=0/4+{m}/2+{3*m}/4={tex(F(5*m,4))}$；$E(X^2)={m*m}/2+{9*m*m}/4={tex(F(11*m*m,4))}$，所以 $D(X)={tex(F(11*m*m,4))}-({tex(F(5*m,4))})^2={tex(F(19*m*m,16))}$。由线性变换 $E(Y)=2E(X)-{m}={tex(F(3*m,2))}$，$D(Y)=4D(X)={tex(F(19*m*m,4))}$。期望落在最小与最大取值之间，方差非负。'))
    group('E. 分布列与线性变换', '为什么方差变为四倍，而不是两倍再减去常数？', items)

    items=[]
    for n,p,k in [(3,F(1,2),1),(4,F(1,3),2),(5,F(2,5),2),(6,F(1,4),3),(7,F(3,5),4),(8,F(2,3),5)]:
        val=F(comb(n,k))*p**k*(1-p)**(n-k)
        items.append((rf'进行 {n} 次相互独立的试验，每次成功概率 ${tex(p)}$。令 X 为成功次数，求恰好 {k} 次成功、至少一次成功的概率，以及期望和方差。',
          rf'次数固定、成功率恒定且相互独立，所以 $X\sim B({n},{tex(p)})$。指定 {k} 个成功位置的概率为 $({tex(p)})^{k}({tex(1-p)})^{n-k}$，共有 $\binom{{{n}}}{{{k}}}$ 个互斥位置集合。因此 $P(X={k})={tex(val)}$。至少一次的对立是全部失败，概率为 $1-({tex(1-p)})^{n}={tex(1-(1-p)**n)}$。$E(X)={tex(n*p)},D(X)={tex(n*p*(1-p))}$。分布列的一般项对 k=0 到 n 求和为 1，来自二项式定理。'))
    group('F. 二项分布与至少一次', '从成功位置的选择解释组合系数，逐条核对二项分布条件。', items)

    items=[]
    for n,m,r in [(6,2,3),(7,3,3),(8,3,4),(9,4,3),(10,4,4),(11,5,4)]:
        lo=max(0,r-n+m); hi=min(r,m)
        values=[(k,F(comb(m,k)*comb(n-m,r-k),comb(n,r))) for k in range(lo,hi+1)]
        assert sum(x[1] for x in values)==1
        distribution='，'.join(rf'$P(X={k})={tex(p)}$' for k,p in values)
        items.append((f'{n} 个产品中恰有 {m} 个次品，所有 {r} 件子集等可能被抽中。令 X 为抽中的次品数，求完整分布列、期望和方差。',
          rf'不放回、总体次品数固定，使用超几何模型。可取值从 $\max(0,{r}-{n-m})={lo}$ 到 $\min({r},{m})={hi}$。恰 k 件次品需选 k 件次品和 {r}-k 件正品，所以 $P(X=k)=\binom{{{m}}}k\binom{{{n-m}}}{{{r}-k}}/\binom{{{n}}}{{{r}}}$。逐项为：{distribution}。概率和为 1。$E(X)={r}\cdot{m}/{n}={tex(F(r*m,n))}$；$D(X)={tex(F(r*m*(n-m)*(n-r),n*n*(n-1)))}$。各次抽取不独立，不能用二项方差替代。'))
    group('G. 超几何分布与支持集', '解释上下界分别来自哪一种球或产品数量限制。', items)

    items=[]
    for a,b in [(10,30),(20,60),(30,50),(15,45),(25,75),(40,80)]:
        items.append((f'袋中装有 4 个可区分的奖励球，面值为 {a}、{a}、{b}、{b} 元。所有两球集合等可能被选中，奖金 Y 为面值之和。求分布列、期望、方差；再与固定发放同一期望奖金的方案比较。',
          rf'共有 $\binom42=6$ 个集合。奖金取 ${2*a},{a+b},{2*b}$，对应集合数为 1、4、1，概率为 $1/6,2/3,1/6$，和为 1。期望为 ${a+b}$；围绕此中心的偏差为 $-{b-a},0,{b-a}$，所以方差为 $2\times({b-a})^2/6={tex(F((b-a)**2,3))}$。固定奖金 {a+b} 元的方差为零。如果目标是同一期望下稳定发放，固定方案更稳；若目标另含抽奖吸引力，还需额外评价标准。'))
    group('H. 奖金合并与期望决策', '为什么同面值球仍需编号？为什么固定方案并非所有目标下都最优？', items)

    items=[]
    intervals=[('-1','1','0.6827'),('0','1','0.34135'),('1','2','0.1359'),('2','3','0.0214'),('2','+∞','0.02275'),('-∞','-3','0.00135')]
    explanations=['一个标准差中心区间，直接用所给面积。','由对称性，把中心一个标准差面积除以 2。','两个与一个标准差中心区间的面积之差，再除以 2。','三个与两个标准差中心区间的面积之差，再除以 2。','两个标准差中心区间的补集面积，再除以 2。','三个标准差中心区间的补集面积，再除以 2。']
    for i,((l,u,ans),why) in enumerate(zip(intervals,explanations)):
        mu=60+5*i; sd=2+i
        lower='-\\infty' if l=='-∞' else str(mu+int(l)*sd)
        upper='+\\infty' if u=='+∞' else str(mu+int(u)*sd)
        items.append((rf'$X\sim N({mu},{sd**2})$。已知标准正态中心 1、2、3 个标准差内概率近似为 0.6827、0.9545、0.9973。求 $P({lower}<X<{upper})$，并估计 10000 个同分布对象中落入该区间的数量。',
          rf'第二参数是方差，所以标准差为 {sd}。标准化 $Z=(X-{mu})/{sd}$，目标变为 Z 在端点 {l} 与 {u} 之间。{why} 概率约为 {ans}，数量期望约为 ${ans}\times10000={float(ans)*10000:g}$；若按人数报告可四舍五入。此数量是估计值，不是保证结果，期望人数的计算不需要各对象独立。'))
    group('I. 正态对称性与标准化', '第二参数为什么要开方？估计人数和实际人数有什么区别？', items)

    items=[]
    for m,p in [(3,F(1,2)),(4,F(1,3)),(5,F(2,5)),(3,F(1,4)),(4,F(3,5)),(6,F(1,2))]:
        q=1-p; values=[(k,q**(k-1)*p if k<m else q**(m-1)) for k in range(1,m+1)]
        assert sum(v for k,v in values)==1
        dist='，'.join(rf'$P(T={k})={tex(v)}$' for k,v in values)
        items.append((rf'每次试验相互独立，成功概率 ${tex(p)}$；遇成功即停，最多做 {m} 次。T 为实际次数。求分布列、期望，以及最后一次因成功而停止的概率。',
          rf'对 $k<{m}$，T=k 要求前 k-1 次失败并在第 k 次成功；T={m} 只要求前 {m-1} 次失败。分布列为 {dist}，和为 1。尾和公式给 $E(T)=\sum_{{k=1}}^{{{m}}}({tex(q)})^{{k-1}}={tex((1-q**m)/p)}$。第 {m} 次因成功停止的无条件概率为 $({tex(q)})^{{{m-1}}}\cdot{tex(p)}={tex(q**(m-1)*p)}$，它比 $P(T={m})$ 小，因为后者还含最后失败。'))
    group('J. 有上限的停止试验', '写出最后一次成功与失败两条路径，解释合并后为何少乘一次 p。', items)

    items=[]
    for stay,back in [(F(1,2),F(1,4)),(F(1,3),F(2,3)),(F(3,4),F(1,4)),(F(1,5),F(2,5)),(F(2,3),F(1,6)),(F(1,4),F(1,2))]:
        lam=stay-back; fixed=back/(1-stay+back)
        items.append((rf'过程有 A、B 两个状态，每步转移只由当前状态决定。从 A 下一步留 A 的概率 ${tex(stay)}$，从 B 下一步到 A 的概率 ${tex(back)}$，初始在 A。令 $p_n$ 为 n 步后在 A 的概率，求递推、通项和 $p_2$。',
          rf'按当前状态分成互斥完备的 A、B 两类，全概率给 $p_{{n+1}}={tex(stay)}p_n+{tex(back)}(1-p_n)={tex(back)}+({tex(lam)})p_n$，$p_0=1$。解固定值 $L={tex(back)}+({tex(lam)})L$ 得 $L={tex(fixed)}$，分母 $1-({tex(lam)})>0$。于是 $p_{{n+1}}-L=({tex(lam)})(p_n-L)$，故 $p_n={tex(fixed)}+{tex(1-fixed)}({tex(lam)})^n$，$p_2={tex(fixed+(1-fixed)*lam**2)}$。初值和递推均满足；$|{tex(lam)}|<1$，所以 $p_n$ 趋近固定值。'))
    group('K. 状态递推与数列衔接', '说明按当前状态分类的依据；为什么不能把“在 A”当成每步独立事件？', items)

    items=[]
    for n,k in [(3,1),(4,2),(5,2),(6,4),(8,3),(10,7)]:
        p=F(k,n); maximum=comb(n,k)*p**k*(1-p)**(n-k)
        items.append((f'固定 {n} 次独立同概率试验，每次成功率 p 可取 [0,1]。求恰好 {k} 次成功的概率何时最大，并求最大值。说明为何“成功率越大越好”在此题不成立。',
          rf'$h(p)=\binom{{{n}}}{{{k}}}p^{{{k}}}(1-p)^{{{n-k}}}$，端点值均为零。在 $(0,1)$ 内 h>0，可用对数：$(\ln h)\prime={k}/p-{n-k}/(1-p)=({k}-{n}p)/(p(1-p))$。分母正，导数在 $p={tex(p)}$ 左正右负，故唯一最大点为 ${tex(p)}$，最大值 ${tex(maximum)}$。目标是恰好 {k} 次，成功过多也不满足；当 p=1 时成功 {n} 次，目标概率为零。'))
    group('L. 概率函数的参数最优化', '解释对数为什么合法；把目标改成至少 k 次后原结论是否还成立？', items)

    lines=['# 高中概率专项训练：12 类 72 题', '', '本页为根据本地考点结构重新编写的训练题，不冒充原卷逐字转录。每组前两题建立模型，后四题改变参数巩固计算与表达；综合迁移请继续使用原资料中的情境大题。所有答案默认折叠。', '', '返回[概率专题](./README.md)。原始情境与完整本地题量见[资料索引](./07_local_sources_zh.md)。', '']
    number=0
    for title,prompt,items in groups:
        lines += ['## '+title, '', '讲题追问：'+prompt, '']
        for question,answer in items:
            number+=1
            lines += [f'### 题 {number}', '', question, '', ':::solution 查看完整解析', '', answer, '', ':::', '']
    assert number == 72
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'06_exercises_zh.md').write_text('\n'.join(lines),encoding='utf-8')

    ASSETS.mkdir(parents=True,exist_ok=True)
    lines=['# 本地概率资料：原卷、解析与教学对应', '', '网页讲义根据以下材料组织知识和改编例题。原文件中的嵌入公式、表格和图形保留在下载文件中；下载原卷做综合训练，完成后再打开对应解析。部分旧题采用旧教材术语，应结合当前课堂要求选用。', '', '## 一轮复习考点', '']
    base=LOCAL/'考点讲解2021年高考数学复习一轮复习笔记（65个考点讲解全）'
    mapping={31:'古典概型',36:'超几何分布与二项分布',37:'独立事件与独立重复试验',38:'正态分布和条件概率',39:'均值与方差在生活中运用',29:'抽样：统计接口',30:'用样本估计总体：统计接口',32:'线性回归与列联表：统计接口'}
    count=0
    for point,title in mapping.items():
        lines += [f'### 考点 {point}：{title}', '']
        matches=sorted(p for p in base.rglob('*.docx') if p.name.startswith(f'考点{point} '))
        for p in matches:
            lesson='lesson' if '讲解' in p.name else 'practice'
            solved='solution' if '解析版' in p.name else 'questions'
            target=f'point-{point}-{lesson}-{solved}.docx'
            shutil.copy2(p,ASSETS/target)
            label=('讲解' if lesson=='lesson' else '练习')+('解析版' if solved=='solution' else '原卷版')
            lines += [f'- [{label}](../../../assets/probability-sources/{target})']
            count+=1
        lines += ['']
    pdf=next((LOCAL/'导数、圆锥曲线、数列和概率与统计').glob('*统计概率*.pdf'))
    shutil.copy2(pdf,ASSETS/'probability-hotspots-2020.pdf')
    lines += ['## 综合热点题集', '', '[2020 高考统计概率大题必刷热点题型：81 页 PDF](../../../assets/probability-sources/probability-hotspots-2020.pdf)', '', '已查阅开篇情境，包括回归与多阶段检测、正四面体随机游走、直方图与正态估计、轮流摸球及检验决策。建议先完成对应讲义，再选这些题训练跨模块表达；正文的随机游走例题给出重写的完整推导。', '', '## 选题与讲题安排', '', '古典概型讲完后选考点 31 练习；分布讲完后选 36；独立性选 37；条件与正态选 38；停止、期望和方案比较选 39。综合课使用热点 PDF，按样本与概率、分布、期望、决策四层组织解答。', '', '同一道题建议先由学生口头说明随机机制，再写分布列与计算。若只会套公式，就回到具体事件路径和取值对应关系。', '']
    (OUT/'07_local_sources_zh.md').write_text('\n'.join(lines),encoding='utf-8')
    print(f'Generated {number} exercises in {len(groups)} groups; copied {count} DOCX files and one PDF.')


if __name__ == '__main__':
    main()
