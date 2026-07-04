# 三角函数：从单位圆到图像与恒等变换

三角函数不是一组需要硬背的公式，而是一条很清楚的链：

$$
\text{角}\longrightarrow \text{单位圆上的点}
\longrightarrow \text{函数值}
\longrightarrow \text{图像性质}
\longrightarrow \text{恒等变换与方程}.
$$

如果学生只背“奇变偶不变、符号看象限”，她遇到复杂题时会很容易散掉。真正可靠的学习方式，是让每一条公式都能回到单位圆、坐标、对称、内积或图像上去解释。

## 研究对象

本页研究四个对象：

1. **角**：角可以继续旋转，所以同一个终边对应无穷多个角。
2. **坐标**：角的终边与单位圆交于一点，横坐标给余弦，纵坐标给正弦。
3. **函数**：$\sin x,\cos x,\tan x$ 把角变成数，因此可以讨论定义域、值域、周期、单调和对称。
4. **变换**：三角恒等变换本质是把同一个几何关系写成不同代数形式。

课堂上先让学生回答一句话：三角函数到底在研究什么？较好的答案是：它研究角旋转到某个位置时，与单位圆交点的坐标及其变化规律。

## 核心知识结构

### 1. 任意角、终边相同角与弧度制

在平面直角坐标系中，以 $x$ 轴正半轴为始边，逆时针旋转为正角，顺时针旋转为负角。若两个角终边相同，则它们相差整圈：

$$
\beta=\alpha+2k\pi,\qquad k\in\mathbb Z.
$$

例如，与 $\frac{\pi}{6}$ 终边相同的角为

$$
\frac{\pi}{6}+2k\pi,\qquad k\in\mathbb Z.
$$

弧度制来自圆：若半径为 $r$ 的圆中，圆心角 $\theta$ 所对弧长为 $l$，则

$$
\theta=\frac lr.
$$

所以一整圈弧长为 $2\pi r$，对应角为 $2\pi$，即

$$
180^\circ=\pi,\qquad 360^\circ=2\pi.
$$

弧度制不是“把角度换个名字”，而是让角和弧长、周期、函数图像直接相连。高中三角函数一旦进入图像和方程，默认应优先使用弧度制。

### 2. 单位圆定义：公式从坐标来

设角 $\alpha$ 的终边与单位圆交于点

$$
P(x,y).
$$

定义

$$
\cos\alpha=x,\qquad \sin\alpha=y,\qquad
\tan\alpha=\frac yx\quad(x\ne0).
$$

若终边经过任意非原点 $P(x,y)$，令

$$
r=\sqrt{x^2+y^2},
$$

则

$$
\cos\alpha=\frac xr,\qquad
\sin\alpha=\frac yr,\qquad
\tan\alpha=\frac yx\quad(x\ne0).
$$

这里要强调三件事：

1. $\sin\alpha$ 是纵坐标，不是“斜边分之一”的死公式。直角三角形只是第一象限锐角情形。
2. $\cos\alpha$ 是横坐标，因此符号由横坐标决定。
3. $\tan\alpha$ 是斜率，所以当终边竖直时无定义。

由单位圆方程 $x^2+y^2=1$ 立刻得到

$$
\sin^2\alpha+\cos^2\alpha=1.
$$

这就是同角基本关系的源头。

### 3. 三角函数线：把不等式和大小比较画出来

三角函数线是单位圆上的几何表示：

1. $\sin\alpha$ 对应纵向长度；
2. $\cos\alpha$ 对应横向长度；
3. $\tan\alpha$ 对应过 $(1,0)$ 的切线与终边延长线的交点纵坐标。

它最有用的地方不是记定义，而是处理三类问题：

1. 比较大小，例如比较 $\sin1,\sin2,\sin3$；
2. 解三角不等式，例如 $\sin x>\frac12$；
3. 判断取值范围，例如由点在第一象限推出 $\sin x,\cos x$ 的符号。

课堂上可以让学生先画单位圆，再问：如果 $\sin x>\frac12$，单位圆上点的纵坐标应该在哪里？这样她会自然看到一个弧段，而不是机械背区间。

### 4. 同角关系与“弦的齐次”

同角三角函数关系有两条最基本：

$$
\sin^2\alpha+\cos^2\alpha=1,\qquad
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}.
$$

第一条来自单位圆方程，第二条来自斜率定义。由它们可以推出：

$$
1+\tan^2\alpha=\frac1{\cos^2\alpha}\quad(\cos\alpha\ne0).
$$

题目中若出现

$$
\frac{a\sin\alpha+b\cos\alpha}{c\sin\alpha+d\cos\alpha},
$$

并且已知 $\tan\alpha$，常把分子分母同除以 $\cos\alpha$，化成 $\tan\alpha$。这就是一类常见的“弦的齐次”题。

但要小心：开平方时必须由象限决定符号。比如由 $\sin^2\alpha=\frac49$ 只能得到 $\sin\alpha=\pm\frac23$，不能直接写正号。

### 5. 诱导公式：先看位置，再看名称

诱导公式本质是单位圆对称性。比如

$$
\sin(-\alpha)=-\sin\alpha,\qquad
\cos(-\alpha)=\cos\alpha,
$$

因为点关于 $x$ 轴对称，横坐标不变，纵坐标变号。

再比如

$$
\sin(\pi-\alpha)=\sin\alpha,\qquad
\cos(\pi-\alpha)=-\cos\alpha,
$$

因为点关于 $y$ 轴对称，纵坐标不变，横坐标变号。

系统处理诱导公式时，不要只背口诀，要按两步走：

1. **看位置**：把角化成某个象限内的参考角，判断正负号。
2. **看名称**：若是 $k\pi\pm\alpha$，函数名通常不变；若是 $\frac\pi2\pm\alpha$，正弦和余弦互换。

例如

$$
\sin\left(\frac\pi2+\alpha\right)=\cos\alpha,\qquad
\cos\left(\frac\pi2+\alpha\right)=-\sin\alpha.
$$

它不是神秘口诀，而是单位圆旋转 $90^\circ$ 后，横纵坐标交换并改变符号。

### 6. 两角和差公式：从坐标内积推出来

令

$$
\mathbf u=(\cos\alpha,\sin\alpha),\qquad
\mathbf v=(\cos\beta,\sin\beta).
$$

它们都是单位向量，夹角为 $\alpha-\beta$。一方面，

$$
\mathbf u\cdot\mathbf v
=|\mathbf u||\mathbf v|\cos(\alpha-\beta)
=\cos(\alpha-\beta).
$$

另一方面，按坐标做内积：

$$
\mathbf u\cdot\mathbf v
=\cos\alpha\cos\beta+\sin\alpha\sin\beta.
$$

所以

$$
\cos(\alpha-\beta)
=\cos\alpha\cos\beta+\sin\alpha\sin\beta.
$$

把 $\beta$ 换成 $-\beta$ 得

$$
\cos(\alpha+\beta)
=\cos\alpha\cos\beta-\sin\alpha\sin\beta.
$$

再用 $\sin\theta=\cos\left(\frac\pi2-\theta\right)$，可推出

$$
\sin(\alpha+\beta)
=\sin\alpha\cos\beta+\cos\alpha\sin\beta,
$$

$$
\sin(\alpha-\beta)
=\sin\alpha\cos\beta-\cos\alpha\sin\beta.
$$

这四条公式不应孤立背。要让学生知道：余弦差公式来自两个单位向量的内积，其他公式可以从它推出。

### 7. 二倍角、降幂与辅助角

令 $\beta=\alpha$，得到二倍角公式：

$$
\sin2\alpha=2\sin\alpha\cos\alpha,
$$

$$
\cos2\alpha=\cos^2\alpha-\sin^2\alpha
=1-2\sin^2\alpha
=2\cos^2\alpha-1.
$$

由它还可反向得到降幂公式：

$$
\sin^2\alpha=\frac{1-\cos2\alpha}{2},\qquad
\cos^2\alpha=\frac{1+\cos2\alpha}{2}.
$$

辅助角公式处理

$$
a\sin x+b\cos x
$$

这类表达。令

$$
R=\sqrt{a^2+b^2},\qquad
\cos\varphi=\frac aR,\qquad
\sin\varphi=\frac bR,
$$

则

$$
a\sin x+b\cos x
=R\sin(x+\varphi).
$$

它的意义是：两个同频率的正弦、余弦叠加后，仍然是同频率的正弦波，只是振幅和相位改变了。

### 8. 图像性质与图像变换

三角函数图像要抓五个指标：定义域、值域、周期、奇偶、单调。基础函数可以这样记：

1. $y=\sin x$：定义域 $\mathbb R$；值域 $[-1,1]$；最小正周期 $2\pi$；奇函数。
2. $y=\cos x$：定义域 $\mathbb R$；值域 $[-1,1]$；最小正周期 $2\pi$；偶函数。
3. $y=\tan x$：定义域 $x\ne\frac\pi2+k\pi$；值域 $\mathbb R$；最小正周期 $\pi$；奇函数。

对于

$$
y=A\sin(\omega x+\varphi)+b,
$$

要看四个参数：

1. $A$ 控制振幅，值域变为 $[b-|A|,b+|A|]$；
2. $\omega$ 控制周期，$T=\dfrac{2\pi}{|\omega|}$；
3. $\varphi$ 控制水平平移，平移量是 $-\dfrac{\varphi}{\omega}$；
4. $b$ 控制上下平移。

最容易错的是平移量。比如

$$
y=\sin(2x-\frac\pi3)
=\sin2\left(x-\frac\pi6\right),
$$

它是向右平移 $\frac\pi6$，不是 $\frac\pi3$。

单调区间不要直接背变形后的结论。核心做法是设

$$
u=\omega x+\varphi,
$$

先把 $u$ 放回母函数的单调区间，再解关于 $x$ 的不等式。常用母函数区间是：

1. $\sin u$ 在 $\left[-\frac\pi2+2k\pi,\frac\pi2+2k\pi\right]$ 上递增，在 $\left[\frac\pi2+2k\pi,\frac{3\pi}2+2k\pi\right]$ 上递减；
2. $\cos u$ 在 $\left[-\pi+2k\pi,2k\pi\right]$ 上递增，在 $\left[2k\pi,\pi+2k\pi\right]$ 上递减；
3. $\tan u$ 在 $\left(-\frac\pi2+k\pi,\frac\pi2+k\pi\right)$ 上递增。

如果前面有负号，例如 $-2\sin u+1$，递增和递减要互换；如果 $\omega<0$，解不等式时方向也要跟着改变。

对称轴和对称中心也不是另一套新公式，而是把母函数的特殊位置搬到 $u=\omega x+\varphi$ 里：

1. $y=A\sin u+b$：对称轴来自峰谷，$u=\frac\pi2+k\pi$；对称中心来自零点，$u=k\pi$，中心纵坐标是 $b$。
2. $y=A\cos u+b$：对称轴来自峰谷，$u=k\pi$；对称中心来自零点，$u=\frac\pi2+k\pi$，中心纵坐标是 $b$。
3. $y=A\tan u+b$：没有对称轴；对称中心来自 $u=k\pi$，中心纵坐标是 $b$。

由图像反求解析式时，先从最高点和最低点读出

$$
|A|=\frac{y_{\max}-y_{\min}}2,\qquad b=\frac{y_{\max}+y_{\min}}2,
$$

再由周期读出 $|\omega|=\frac{2\pi}{T}$，最后用一个特殊点（最大点、最小点或过中线点）确定 $\varphi$。

### 9. 三角方程、最值与参数

三角方程要写全体解。例如

$$
\sin x=\frac12
$$

在一个周期内有两个解：

$$
x=\frac\pi6,\quad x=\frac{5\pi}6.
$$

所以全体解为

$$
x=2k\pi+\frac\pi6
\quad\text{或}\quad
x=2k\pi+\frac{5\pi}6,\qquad k\in\mathbb Z.
$$

最值题通常有三种入口：

1. 直接由 $[-1,1]$ 得值域；
2. 化成 $R\sin(x+\varphi)+b$；
3. 换元成一元二次函数，但必须保留换元范围。

例如令 $t=\sin x$ 时，不能只说 $t$ 是实数，而要写

$$
-1\le t\le1.
$$

## 方法识别

看到三角函数题，先判断它属于哪一层：

1. **定义层**：终边经过点、象限、三角函数线。
2. **关系层**：同角关系、弦的齐次、诱导公式。
3. **公式层**：和差角、二倍角、降幂、辅助角。
4. **图像层**：周期、单调、对称、最值、参数。
5. **方程层**：基本角、周期、定义域、全体解。

失败信号：

- 忘记象限，只给绝对值；
- 把 $\sin^2x$ 写成 $\sin x^2$；
- 诱导公式只背口诀，不判断新角所在象限；
- 图像平移把 $-\frac{\varphi}{\omega}$ 写成 $-\varphi$；
- 三角方程只写一个特殊解；
- 换元后忘记新变量范围。

## 典型例题

### 例 1：终边经过点

角 $\alpha$ 的终边经过点 $P(-3,4)$，求 $\sin\alpha,\cos\alpha,\tan\alpha$。

解：先求

$$
r=\sqrt{(-3)^2+4^2}=5.
$$

所以

$$
\sin\alpha=\frac45,\qquad
\cos\alpha=-\frac35,\qquad
\tan\alpha=-\frac43.
$$

点在第二象限，所以正弦为正，余弦和正切为负。

### 例 2：弦的齐次

已知 $\tan\alpha=2$，求

$$
\frac{3\sin\alpha-\cos\alpha}{\sin\alpha+2\cos\alpha}.
$$

解：分子分母同除以 $\cos\alpha$：

$$
\frac{3\tan\alpha-1}{\tan\alpha+2}
=\frac{6-1}{2+2}
=\frac54.
$$

这种题的核心不是求 $\sin\alpha,\cos\alpha$，而是利用齐次结构直接化为 $\tan\alpha$。

### 例 3：角的拼凑

已知 $\sin\alpha=\frac35$，$\alpha$ 为锐角，$\cos\beta=\frac{12}{13}$，$\beta$ 为锐角，求 $\sin(\alpha+\beta)$。

解：先补出

$$
\cos\alpha=\frac45,\qquad \sin\beta=\frac5{13}.
$$

所以

$$
\sin(\alpha+\beta)
=\sin\alpha\cos\beta+\cos\alpha\sin\beta
=\frac35\cdot\frac{12}{13}+\frac45\cdot\frac5{13}
=\frac{56}{65}.
$$

### 例 4：辅助角求最值

求函数

$$
f(x)=\sqrt3\sin x+\cos x+1
$$

的最大值。

解：

$$
\sqrt3\sin x+\cos x
=2\sin\left(x+\frac\pi6\right).
$$

所以

$$
f(x)=2\sin\left(x+\frac\pi6\right)+1.
$$

最大值为 $3$。

### 例 5：图像参数

函数

$$
y=2\sin\left(3x-\frac\pi2\right)-1
$$

的周期和值域分别是什么？

解：

$$
T=\frac{2\pi}{3}.
$$

因为 $2\sin(\cdots)$ 的值域为 $[-2,2]$，整体下移 1 后值域为

$$
[-3,1].
$$

### 例 6：三角方程

解方程

$$
2\cos x-1=0.
$$

解：即 $\cos x=\frac12$。在一个周期内，

$$
x=\frac\pi3,\quad x=\frac{5\pi}3.
$$

所以

$$
x=2k\pi+\frac\pi3
\quad\text{或}\quad
x=2k\pi+\frac{5\pi}3,\qquad k\in\mathbb Z.
$$

## 自我训练

下面的训练按题型分层。课堂上不需要一次全做完，可以让学生每类挑一题讲解，再由你追问定义来源、符号条件和变形方向。

## 分层题型训练

### A. 单位圆与三角函数线

#### 训练 1

角 $\alpha$ 的终边经过点 $P(5,-12)$，求 $\sin\alpha,\cos\alpha,\tan\alpha$。

:::solution 查看解析
$r=\sqrt{5^2+(-12)^2}=13$，所以
$$
\sin\alpha=-\frac{12}{13},\qquad
\cos\alpha=\frac5{13},\qquad
\tan\alpha=-\frac{12}{5}.
$$
点在第四象限，符号也与结果一致。
:::

#### 训练 2

写出与 $-\frac{2\pi}{3}$ 终边相同的所有角。

:::solution 查看解析
终边相同的角相差 $2\pi$ 的整数倍，所以全体角为
$$
-\frac{2\pi}{3}+2k\pi,\qquad k\in\mathbb Z.
$$
:::

#### 训练 3

已知 $\sin\alpha=\frac23$，且 $\alpha$ 是第二象限角，求 $\cos\alpha$。

:::solution 查看解析
由同角关系：
$$
\cos^2\alpha=1-\sin^2\alpha=1-\frac49=\frac59.
$$
第二象限 $\cos\alpha<0$，所以
$$
\cos\alpha=-\frac{\sqrt5}{3}.
$$
:::

#### 训练 4

在 $[0,2\pi)$ 内解不等式 $\sin x>\frac12$。

:::solution 查看解析
在单位圆上，$\sin x$ 是纵坐标。纵坐标大于 $\frac12$ 的弧段位于
$$
\frac\pi6<x<\frac{5\pi}6.
$$
所以解集为 $\left(\frac\pi6,\frac{5\pi}6\right)$。
:::

### B. 恒等变换与角的拼凑

#### 训练 5

化简：

$$
\sin(\pi+x)+\cos\left(\frac\pi2+x\right).
$$

:::solution 查看解析
由诱导公式，
$$
\sin(\pi+x)=-\sin x,\qquad
\cos\left(\frac\pi2+x\right)=-\sin x.
$$
所以原式为
$$
-2\sin x.
$$
:::

#### 训练 6

已知 $\tan\alpha=3$，求

$$
\frac{2\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}.
$$

:::solution 查看解析
分子分母同除以 $\cos\alpha$：
$$
\frac{2\tan\alpha+1}{\tan\alpha-1}
=\frac{2\cdot3+1}{3-1}
=\frac72.
$$
:::

#### 训练 7

已知 $\sin\alpha=\frac{5}{13}$，$\alpha$ 为锐角，求 $\cos2\alpha$。

:::solution 查看解析
锐角时 $\cos\alpha=\frac{12}{13}$。使用
$$
\cos2\alpha=1-2\sin^2\alpha
$$
得
$$
\cos2\alpha=1-2\cdot\frac{25}{169}
=\frac{119}{169}.
$$
:::

#### 训练 8

已知 $\sin\alpha=\frac35$，$\alpha$ 为锐角，$\cos\beta=\frac45$，$\beta$ 为锐角，求 $\cos(\alpha+\beta)$。

:::solution 查看解析
先补出
$$
\cos\alpha=\frac45,\qquad \sin\beta=\frac35.
$$
所以
$$
\cos(\alpha+\beta)
=\cos\alpha\cos\beta-\sin\alpha\sin\beta
=\frac45\cdot\frac45-\frac35\cdot\frac35
=\frac7{25}.
$$
:::

### C. 图像性质与参数

#### 训练 9

求函数

$$
y=3\sin\left(2x+\frac\pi3\right)-4
$$

的周期、值域和水平平移量。

:::solution 查看解析
周期
$$
T=\frac{2\pi}{2}=\pi.
$$
值域为
$$
[-4-3,-4+3]=[-7,-1].
$$
又
$$
2x+\frac\pi3=2\left(x+\frac\pi6\right),
$$
所以相对 $y=3\sin2x$ 向左平移 $\frac\pi6$。
:::

#### 训练 10

求函数

$$
f(x)=2\sin x-2\cos x
$$

的最大值和最小值。

:::solution 查看解析
辅助角化简：
$$
2\sin x-2\cos x
=2\sqrt2\sin\left(x-\frac\pi4\right).
$$
所以最大值为 $2\sqrt2$，最小值为 $-2\sqrt2$。
:::

#### 训练 11

解方程

$$
\cos x=-\frac12.
$$

:::solution 查看解析
在一个周期内，
$$
x=\frac{2\pi}{3},\quad x=\frac{4\pi}{3}.
$$
所以全体解为
$$
x=2k\pi+\frac{2\pi}{3}
\quad\text{或}\quad
x=2k\pi+\frac{4\pi}{3},\qquad k\in\mathbb Z.
$$
:::

#### 训练 12

求函数

$$
f(x)=2\sin^2x-4\sin x+1
$$

的值域。

:::solution 查看解析
令 $t=\sin x$，则 $-1\le t\le1$。函数变为
$$
f=2t^2-4t+1=2(t-1)^2-1.
$$
在 $[-1,1]$ 上，最小值在 $t=1$ 处取得，为 $-1$；最大值在 $t=-1$ 处取得，为
$$
2(-2)^2-1=7.
$$
所以值域为 $[-1,7]$。关键是不能忘记 $t$ 的范围。
:::

## 费曼讲题任务

让学生从训练 4、训练 8、训练 10、训练 12 中任选一道讲给你听。你可以只追问四句话：

1. 这道题的对象是角、坐标、公式、图像还是方程？
2. 你用了哪条定义或公式？它从哪里来？
3. 有没有象限、定义域或换元范围需要检查？
4. 如果题目把角的范围改掉，答案会不会变？
