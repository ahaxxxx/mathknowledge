# 三角函数与解三角形：本地一轮复习补充

这一页根据本地 2021 高考一轮复习资料中的考点 13 到考点 17 重写整理，补充三角函数定义、同角关系、诱导恒等变换、图像性质与解三角形的题型方法。

返回专题首页：[三角专题](./README.md)。基础题库入口：[三角专题分层题库](./03_trig_exercise_bank_zh.md)。

## 本地资料梳理

当前文件夹中和三角专题直接相关的资料有五组：

1. 考点 13：三角函数定义。题组集中在终边相同角、角所在区域、终边点与三角函数值。
2. 考点 14：同角三角函数。题组集中在公式直接运用、象限定符号、弦的齐次、参数范围。
3. 考点 15：诱导公式及恒等变化。题组集中在诱导公式、终边直线、象限化简和恒等式化简。
4. 考点 16：三角函数性质。题组集中在周期、定义域、单调性、对称性、图像变换、值域和参数。
5. 考点 17：正余弦定理。题组集中在定理选择、边角互换、面积、外接圆、多解和取值范围。

这五组资料的共同特点是：小题不难，但很考“先识别对象”。三角函数题先判断是在处理角、函数图像、恒等式还是三角形；解三角形题先判断已知量结构，再决定正弦定理、余弦定理或面积公式。

## 方法补充

1. **终边相同角**：先在一个周期内描述，再加 $2k\pi$。如果区域跨过 $0$，要分两段写。
2. **终边点定义**：设终边上一点 $P(x,y)$，先算 $r=\sqrt{x^2+y^2}$，再写 $\sin\alpha=\frac yr,\cos\alpha=\frac xr,\tan\alpha=\frac yx$。
3. **同角关系**：先用 $\sin^2\alpha+\cos^2\alpha=1$，再用象限定符号。不要只开平方不判符号。
4. **弦的齐次**：如果式子每一项都是同次，可以除以 $\cos^n\alpha$ 或 $\sin^n\alpha$，把问题转成 $\tan\alpha$。
5. **诱导公式**：不要只背“奇变偶不变”，要能解释为终边位置变化；符号由化简后角所在象限决定。
6. **图像性质**：令 $u=\omega x+\varphi$，先在 $u$ 上写标准函数的周期、单调、对称，再解回 $x$。
7. **解三角形定理选择**：两角一边优先正弦定理；两边夹角或三边优先余弦定理；面积出现“两边夹角”优先 $S=\frac12bc\sin A$。
8. **边角互换**：三角形中 $\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R$，所以正弦比可以转成边比。
9. **SSA 多解**：已知 $A,a,b$ 时，由 $\sin B=\frac{b\sin A}{a}$ 得到的 $B$ 可能有两个候选，必须检查 $A+B<180^\circ$。

## A. 终边相同角、象限与区域

### 题 1：终边相同角

写出与 $-\frac{7\pi}{6}$ 终边相同的所有角，并指出它在 $[0,2\pi)$ 内的代表角。

:::solution 查看解析
终边相同角相差 $2\pi$ 的整数倍：

$$
\alpha=-\frac{7\pi}{6}+2k\pi,\qquad k\in\mathbb Z.
$$

把 $-\frac{7\pi}{6}$ 加上 $2\pi$：

$$
-\frac{7\pi}{6}+2\pi=\frac{5\pi}{6}.
$$

所以在 $[0,2\pi)$ 内的代表角是

$$
\frac{5\pi}{6}.
$$
:::

### 题 2：象限角范围

写出第二象限角 $\alpha$ 的一般形式。

:::solution 查看解析
第二象限对应一个周期内

$$
\frac{\pi}{2}<\alpha<\pi.
$$

加上周期 $2k\pi$，得到

$$
\frac{\pi}{2}+2k\pi<\alpha<\pi+2k\pi,\qquad k\in\mathbb Z.
$$
:::

### 题 3：终边在直线上

角 $\alpha$ 的终边在直线 $y=x$ 上，且终边位于第三象限。写出 $\alpha$ 的一般形式。

:::solution 查看解析
直线 $y=x$ 上有两条终边方向：第一象限方向为 $\frac{\pi}{4}$，第三象限方向为

$$
\frac{\pi}{4}+\pi=\frac{5\pi}{4}.
$$

所以

$$
\alpha=\frac{5\pi}{4}+2k\pi,\qquad k\in\mathbb Z.
$$
:::

### 题 4：区域描述

若角 $\alpha$ 的终边落在从 $30^\circ$ 到 $120^\circ$ 的区域内，包含边界，用弧度制写出 $\alpha$ 的范围。

:::solution 查看解析
先把角度化成弧度：

$$
30^\circ=\frac{\pi}{6},\qquad 120^\circ=\frac{2\pi}{3}.
$$

一个周期内的范围为

$$
\frac{\pi}{6}\le \alpha\le \frac{2\pi}{3}.
$$

所有角为

$$
\frac{\pi}{6}+2k\pi\le \alpha\le \frac{2\pi}{3}+2k\pi,\qquad k\in\mathbb Z.
$$
:::

## B. 三角函数定义与终边点

### 题 5：终边点直接求值

角 $\alpha$ 的终边经过点 $P(3,-4)$，求 $\sin\alpha,\cos\alpha,\tan\alpha$。

:::solution 查看解析
先算

$$
r=\sqrt{3^2+(-4)^2}=5.
$$

由定义：

$$
\sin\alpha=\frac yr=-\frac45,\qquad
\cos\alpha=\frac xr=\frac35,\qquad
\tan\alpha=\frac yx=-\frac43.
$$
:::

### 题 6：由正弦值反求坐标参数

角 $\alpha$ 的终边经过点 $P(-5,m)$，且 $\sin\alpha=\frac{12}{13}$。求 $m$。

:::solution 查看解析
因为

$$
\sin\alpha=\frac{m}{\sqrt{25+m^2}}=\frac{12}{13}.
$$

正弦为正，且 $x=-5<0$，终边在第二象限，所以 $m>0$。

平方：

$$
\frac{m^2}{25+m^2}=\frac{144}{169}.
$$

整理：

$$
169m^2=144(25+m^2),
$$

$$
25m^2=3600,
$$

所以

$$
m=12.
$$
:::

### 题 7：由正切值补全正余弦

已知 $\tan\alpha=-\frac34$，且 $\alpha$ 是第二象限角，求 $\sin\alpha,\cos\alpha$。

:::solution 查看解析
第二象限中 $\sin\alpha>0,\cos\alpha<0$。由

$$
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}=-\frac34
$$

可设

$$
\sin\alpha=3t,\qquad \cos\alpha=-4t,\qquad t>0.
$$

代入平方关系：

$$
9t^2+16t^2=1,
$$

所以 $t=\frac15$。因此

$$
\sin\alpha=\frac35,\qquad \cos\alpha=-\frac45.
$$
:::

### 题 8：定义法求组合值

角 $\alpha$ 的终边经过点 $P(-2,1)$，求 $2\sin\alpha-\cos\alpha$。

:::solution 查看解析

$$
r=\sqrt{(-2)^2+1^2}=\sqrt5.
$$

所以

$$
\sin\alpha=\frac1{\sqrt5},\qquad
\cos\alpha=-\frac2{\sqrt5}.
$$

代入：

$$
2\sin\alpha-\cos\alpha
=\frac2{\sqrt5}+\frac2{\sqrt5}
=\frac4{\sqrt5}.
$$
:::

## C. 同角关系与弦的齐次

### 题 9：由余弦求正弦和正切

已知 $\cos\alpha=-\frac5{13}$，且 $\alpha$ 是第三象限角，求 $\sin\alpha,\tan\alpha$。

:::solution 查看解析
第三象限中正弦、余弦都为负，正切为正。

$$
\sin^2\alpha=1-\cos^2\alpha
=1-\frac{25}{169}
=\frac{144}{169}.
$$

因此

$$
\sin\alpha=-\frac{12}{13}.
$$

所以

$$
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}
=\frac{-12/13}{-5/13}
=\frac{12}{5}.
$$
:::

### 题 10：齐次式求值

已知 $\tan\alpha=3$，求

$$
\frac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}.
$$

:::solution 查看解析
分子分母都是一次齐次式，除以 $\cos\alpha$：

$$
\frac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}
=\frac{\tan\alpha+1}{\tan\alpha-1}.
$$

代入 $\tan\alpha=3$：

$$
\frac{3+1}{3-1}=2.
$$
:::

### 题 11：由和求积

已知 $\sin\alpha+\cos\alpha=\frac13$，求 $\sin\alpha\cos\alpha$。

:::solution 查看解析
两边平方：

$$
(\sin\alpha+\cos\alpha)^2=\frac19.
$$

展开：

$$
\sin^2\alpha+\cos^2\alpha+2\sin\alpha\cos\alpha=\frac19.
$$

所以

$$
1+2\sin\alpha\cos\alpha=\frac19.
$$

因此

$$
\sin\alpha\cos\alpha=-\frac49.
$$
:::

### 题 12：由差求二倍角

已知 $\sin\alpha-\cos\alpha=\frac{\sqrt2}{2}$，求 $\sin2\alpha$。

:::solution 查看解析
两边平方：

$$
(\sin\alpha-\cos\alpha)^2=\frac12.
$$

展开：

$$
\sin^2\alpha+\cos^2\alpha-2\sin\alpha\cos\alpha=\frac12.
$$

所以

$$
1-2\sin\alpha\cos\alpha=\frac12,
$$

得到

$$
2\sin\alpha\cos\alpha=\frac12.
$$

而

$$
\sin2\alpha=2\sin\alpha\cos\alpha,
$$

所以

$$
\sin2\alpha=\frac12.
$$
:::

## D. 诱导公式与恒等化简

### 题 13：诱导公式求值

已知 $\sin\alpha=\frac13$，求

$$
\sin(\pi+\alpha)+\cos\left(\frac{3\pi}{2}-\alpha\right).
$$

:::solution 查看解析
分别化简：

$$
\sin(\pi+\alpha)=-\sin\alpha,
$$

$$
\cos\left(\frac{3\pi}{2}-\alpha\right)=-\sin\alpha.
$$

所以原式为

$$
-2\sin\alpha=-\frac23.
$$
:::

### 题 14：终边直线与诱导

角 $\alpha$ 的终边在直线 $y=-x$ 上，且 $\alpha$ 在第四象限。求 $\tan(\pi-\alpha)$。

:::solution 查看解析
直线 $y=-x$ 在第四象限对应方向角为

$$
\frac{7\pi}{4}.
$$

所以

$$
\tan\alpha=-1.
$$

又

$$
\tan(\pi-\alpha)=-\tan\alpha,
$$

因此

$$
\tan(\pi-\alpha)=1.
$$
:::

### 题 15：带象限的根式化简

已知 $\alpha$ 是第四象限角，化简

$$
\sqrt{(1-\sin\alpha)^2}+\sqrt{(1+\cos\alpha)^2}.
$$

:::solution 查看解析
第四象限中

$$
\sin\alpha<0,\qquad \cos\alpha>0.
$$

所以

$$
1-\sin\alpha>0,\qquad 1+\cos\alpha>0.
$$

因此

$$
\sqrt{(1-\sin\alpha)^2}=1-\sin\alpha,
$$

$$
\sqrt{(1+\cos\alpha)^2}=1+\cos\alpha.
$$

原式为

$$
2-\sin\alpha+\cos\alpha.
$$
:::

### 题 16：恒等化简

化简

$$
\frac{1-\cos2x}{\sin2x}.
$$

:::solution 查看解析
使用二倍角：

$$
1-\cos2x=2\sin^2x,
$$

$$
\sin2x=2\sin x\cos x.
$$

所以

$$
\frac{1-\cos2x}{\sin2x}
=\frac{2\sin^2x}{2\sin x\cos x}
=\tan x.
$$

这里默认分母有意义，即 $\sin2x\ne0$。
:::

## E. 三角函数性质：周期、定义域、单调、对称

### 题 17：正弦型周期

求函数

$$
y=\sin\left(2x-\frac{\pi}{3}\right)
$$

的最小正周期。

:::solution 查看解析
对 $y=\sin(\omega x+\varphi)$，周期为

$$
T=\frac{2\pi}{|\omega|}.
$$

本题中 $\omega=2$，所以

$$
T=\pi.
$$
:::

### 题 18：正切型周期

求函数

$$
y=\tan\left(3x+\frac{\pi}{6}\right)
$$

的最小正周期。

:::solution 查看解析
正切函数本身周期为 $\pi$。对 $y=\tan(\omega x+\varphi)$，

$$
T=\frac{\pi}{|\omega|}.
$$

所以

$$
T=\frac{\pi}{3}.
$$
:::

### 题 19：定义域

求函数

$$
y=\sqrt{2\sin x-1}
$$

在 $[0,2\pi]$ 上的定义域。

:::solution 查看解析
根式要求

$$
2\sin x-1\ge0,
$$

即

$$
\sin x\ge\frac12.
$$

在 $[0,2\pi]$ 上，

$$
\sin x\ge\frac12
$$

对应

$$
x\in\left[\frac{\pi}{6},\frac{5\pi}{6}\right].
$$
:::

### 题 20：单调区间

求函数

$$
y=\sin\left(2x-\frac{\pi}{3}\right)
$$

的单调递增区间。

:::solution 查看解析
令

$$
u=2x-\frac{\pi}{3}.
$$

$\sin u$ 的递增区间为

$$
-\frac{\pi}{2}+2k\pi\le u\le \frac{\pi}{2}+2k\pi.
$$

代回：

$$
-\frac{\pi}{2}+2k\pi
\le 2x-\frac{\pi}{3}
\le \frac{\pi}{2}+2k\pi.
$$

两边加 $\frac{\pi}{3}$ 后除以 2：

$$
-\frac{\pi}{12}+k\pi
\le x\le
\frac{5\pi}{12}+k\pi.
$$

所以递增区间为

$$
\left[-\frac{\pi}{12}+k\pi,\frac{5\pi}{12}+k\pi\right],\qquad k\in\mathbb Z.
$$
:::

## F. 图像变换、值域与参数

### 题 21：对称中心

求函数

$$
y=\sin\left(2x-\frac{\pi}{3}\right)
$$

的对称中心。

:::solution 查看解析
$\sin u$ 的对称中心为

$$
(u,y)=(k\pi,0).
$$

令

$$
2x-\frac{\pi}{3}=k\pi,
$$

得到

$$
x=\frac{\pi}{6}+\frac{k\pi}{2}.
$$

所以对称中心为

$$
\left(\frac{\pi}{6}+\frac{k\pi}{2},0\right),\qquad k\in\mathbb Z.
$$
:::

### 题 22：对称轴

求函数

$$
y=\cos\left(2x+\frac{\pi}{4}\right)
$$

的对称轴。

:::solution 查看解析
$\cos u$ 的对称轴为

$$
u=k\pi.
$$

令

$$
2x+\frac{\pi}{4}=k\pi,
$$

得到

$$
x=-\frac{\pi}{8}+\frac{k\pi}{2}.
$$

所以对称轴为

$$
x=-\frac{\pi}{8}+\frac{k\pi}{2},\qquad k\in\mathbb Z.
$$
:::

### 题 23：最值

求函数

$$
y=2\sin\left(x-\frac{\pi}{6}\right)+1
$$

的最大值与最小值。

:::solution 查看解析
因为

$$
-1\le \sin\left(x-\frac{\pi}{6}\right)\le1,
$$

所以

$$
-2\le2\sin\left(x-\frac{\pi}{6}\right)\le2.
$$

加 1 得

$$
-1\le y\le3.
$$

最大值为 $3$，最小值为 $-1$。
:::

### 题 24：换元值域

求函数

$$
y=\sin^2x-2\sin x
$$

的值域。

:::solution 查看解析
令

$$
t=\sin x,\qquad -1\le t\le1.
$$

则

$$
y=t^2-2t=(t-1)^2-1.
$$

在 $[-1,1]$ 上，最小值在 $t=1$ 处取得，为

$$
-1.
$$

最大值比较端点：

$$
t=-1\Rightarrow y=3,\qquad t=1\Rightarrow y=-1.
$$

所以值域为

$$
[-1,3].
$$
:::

## G. 正余弦定理选择、面积与外接圆

### 题 25：两角一边

在 $\triangle ABC$ 中，$A=45^\circ,B=75^\circ,a=\sqrt2$，求 $b$。

:::solution 查看解析
两角一边，且有边角对应，优先正弦定理：

$$
\frac a{\sin A}=\frac b{\sin B}.
$$

因为

$$
\frac{\sqrt2}{\sin45^\circ}
=\frac{\sqrt2}{\sqrt2/2}=2,
$$

所以

$$
b=2\sin75^\circ.
$$

又

$$
\sin75^\circ=\frac{\sqrt6+\sqrt2}{4},
$$

因此

$$
b=\frac{\sqrt6+\sqrt2}{2}.
$$
:::

### 题 26：两边夹角

在 $\triangle ABC$ 中，$a=5,b=7,C=60^\circ$，求 $c$。

:::solution 查看解析
已知两边及夹角，优先余弦定理：

$$
c^2=a^2+b^2-2ab\cos C.
$$

代入：

$$
c^2=25+49-2\cdot5\cdot7\cdot\frac12=39.
$$

所以

$$
c=\sqrt{39}.
$$
:::

### 题 27：面积公式

在 $\triangle ABC$ 中，$a=4,b=6,C=30^\circ$，求面积。

:::solution 查看解析
面积公式：

$$
S=\frac12ab\sin C.
$$

代入：

$$
S=\frac12\cdot4\cdot6\cdot\sin30^\circ
=12\cdot\frac12=6.
$$
:::

### 题 28：外接圆半径

在 $\triangle ABC$ 中，$A=30^\circ,a=4$，求外接圆半径 $R$ 以及外接圆面积。

:::solution 查看解析
正弦定理给出

$$
\frac a{\sin A}=2R.
$$

所以

$$
2R=\frac4{\sin30^\circ}=\frac4{1/2}=8.
$$

因此

$$
R=4.
$$

外接圆面积为

$$
\pi R^2=16\pi.
$$
:::

## H. 边角互换、多解与范围

### 题 29：正弦比判断形状

在 $\triangle ABC$ 中，

$$
\sin A:\sin B:\sin C=3:4:5.
$$

判断三角形形状。

:::solution 查看解析
由正弦定理，

$$
a:b:c=\sin A:\sin B:\sin C=3:4:5.
$$

因为

$$
3^2+4^2=5^2,
$$

所以三角形为直角三角形，且最大边 $c$ 对应的角 $C=90^\circ$。
:::

### 题 30：SSA 两解

在 $\triangle ABC$ 中，$A=30^\circ,a=5,b=6$。判断三角形个数。

:::solution 查看解析
由正弦定理：

$$
\frac{\sin B}{b}=\frac{\sin A}{a},
$$

所以

$$
\sin B=\frac{b\sin A}{a}
=\frac{6\cdot\frac12}{5}
=\frac35.
$$

在 $0^\circ$ 到 $180^\circ$ 内，满足 $\sin B=\frac35$ 的角有两个：一个锐角 $B_1$，一个钝角 $B_2=180^\circ-B_1$。

还要检查 $A+B<180^\circ$。因为 $B_1<90^\circ$，显然满足；$B_2<180^\circ$ 且约为 $143^\circ$，所以

$$
30^\circ+B_2<180^\circ.
$$

两个候选都成立，因此有两个三角形。
:::

### 题 31：SSA 无解

在 $\triangle ABC$ 中，$A=30^\circ,a=4,b=10$。判断三角形是否存在。

:::solution 查看解析
由正弦定理：

$$
\sin B=\frac{b\sin A}{a}
=\frac{10\cdot\frac12}{4}
=\frac54.
$$

但正弦值不可能大于 1，所以不存在这样的三角形。
:::

### 题 32：投影恒等式

在 $\triangle ABC$ 中，证明

$$
b\cos C+c\cos B=a.
$$

:::solution 查看解析
这道题可以理解为“两个投影相加等于底边”，也可以用余弦定理代数证明。

由余弦定理：

$$
\cos C=\frac{a^2+b^2-c^2}{2ab},
$$

所以

$$
b\cos C=\frac{a^2+b^2-c^2}{2a}.
$$

同理

$$
c\cos B=\frac{a^2+c^2-b^2}{2a}.
$$

相加：

$$
b\cos C+c\cos B
=\frac{a^2+b^2-c^2+a^2+c^2-b^2}{2a}
=a.
$$
:::

## 使用建议

1. A、B 两组适合作为三角函数第一讲后的口算复习。
2. C、D 两组适合训练“符号、象限、齐次”的严谨性。
3. E、F 两组适合讲三角函数性质后布置，要求学生每题先说 $u=\omega x+\varphi$ 的标准问题是什么。
4. G、H 两组适合解三角形课堂讲评，尤其要让学生口头判断定理选择和是否存在多解。
