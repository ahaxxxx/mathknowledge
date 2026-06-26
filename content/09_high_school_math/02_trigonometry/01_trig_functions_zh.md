# 三角函数：单位圆、图像与恒等变换

三角函数的核心不是背 $\sin,\cos,\tan$ 的一堆公式，而是把“角”变成可以运算、比较、作图和变形的函数对象。真正学懂以后，诱导公式、同角关系、图像性质和三角恒等变换都会变成同一套语言。

## 研究对象

本页研究三个对象：

1. **角**：可以用角度制，也可以用弧度制。高考中更常用弧度制，因为它让函数周期和图像表达更自然。
2. **单位圆上的点**：角 $\alpha$ 的终边与单位圆交于点 $P(\cos\alpha,\sin\alpha)$。
3. **三角函数**：把角 $\alpha$ 映射到数 $\sin\alpha,\cos\alpha,\tan\alpha$。

定义必须先于公式。若 $P(x,y)$ 是单位圆上的点，则

$$
\cos\alpha=x,\qquad \sin\alpha=y,\qquad \tan\alpha=\frac yx\quad(x\ne0).
$$

所以 $\tan\alpha$ 的定义域要排除 $\alpha=\frac{\pi}{2}+k\pi$，不能只把它看成“正弦除以余弦”的记忆公式。

## 核心知识结构

### 1. 弧度制

弧度把角定义为弧长与半径之比：

$$
\theta=\frac lr.
$$

因此 $180^\circ=\pi$，$360^\circ=2\pi$。弧度不是新的单位名称，而是让角和圆的长度关系直接相连。

### 2. 同角三角函数关系

由单位圆方程 $x^2+y^2=1$ 得

$$
\sin^2\alpha+\cos^2\alpha=1.
$$

当 $\cos\alpha\ne0$ 时，

$$
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}.
$$

这两条关系的来源分别是单位圆方程和斜率定义。讲课时要让学生知道“为什么成立”，而不是只记结论。

### 3. 诱导公式的来源

诱导公式本质上是单位圆对称性：

$$
\sin(-\alpha)=-\sin\alpha,\qquad \cos(-\alpha)=\cos\alpha,
$$

$$
\sin(\pi-\alpha)=\sin\alpha,\qquad \cos(\pi-\alpha)=-\cos\alpha,
$$

$$
\sin(\pi+\alpha)=-\sin\alpha,\qquad \cos(\pi+\alpha)=-\cos\alpha.
$$

教学口诀可以用，但第一次讲必须回到象限和坐标符号。学生真正要掌握的是：角变换后，单位圆上的点落到哪个象限，横坐标和纵坐标怎么变。

### 4. 图像与性质

基础图像：

$$
y=\sin x,\qquad y=\cos x,\qquad y=\tan x.
$$

重点性质：

1. $\sin x$：定义域 $\mathbb R$，值域 $[-1,1]$，周期 $2\pi$，奇函数。
2. $\cos x$：定义域 $\mathbb R$，值域 $[-1,1]$，周期 $2\pi$，偶函数。
3. $\tan x$：定义域 $x\ne\frac\pi2+k\pi$，值域 $\mathbb R$，周期 $\pi$，奇函数。

对于

$$
y=A\sin(\omega x+\varphi)+b,
$$

要分别识别：

- $A$ 控制振幅，值域长度变为 $2|A|$；
- $\omega$ 控制周期，周期为 $\dfrac{2\pi}{|\omega|}$；
- $\varphi$ 控制水平平移，但平移量不是 $\varphi$，而是 $-\dfrac{\varphi}{\omega}$；
- $b$ 控制上下平移。

### 5. 恒等变换的主线

三角恒等变换不是机械套公式，而是在不同表达之间选择更适合的形式。常用公式：

$$
\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta,
$$

$$
\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta,
$$

$$
\sin2\alpha=2\sin\alpha\cos\alpha,
$$

$$
\cos2\alpha=\cos^2\alpha-\sin^2\alpha=1-2\sin^2\alpha=2\cos^2\alpha-1.
$$

常见目标有三类：

1. **化同角**：把不同角变成同一个角。
2. **化同名**：把正弦、余弦、正切统一成一种函数。
3. **降次或升次**：根据题目需要，在平方式和一次式之间转换。

## 方法识别

看到题目先判断对象：

1. **求值题**：看已知角在哪个象限，先确定符号，再用同角关系。
2. **化简题**：看角是否互余、互补、相差 $\pi$ 或 $2\pi$，优先用诱导公式。
3. **图像题**：先找周期、振幅、平移，再判断单调区间和最值。
4. **恒等证明题**：通常从复杂一边入手，把角、函数名、次数逐步统一。
5. **方程题**：先化为基本三角函数值，再结合定义域和周期写全解。

失败信号：

- 忘记象限，只算绝对值；
- 把 $\sin^2 x$ 误写成 $\sin x^2$；
- 图像平移把 $-\dfrac{\varphi}{\omega}$ 写成 $-\varphi$；
- 三角方程只写一个解，漏掉周期解；
- 用平方消去符号后不回代检查。

## 典型例题

### 例 1：由一个三角函数值求另一个

已知 $\sin\alpha=\dfrac35$，且 $\alpha$ 是第二象限角，求 $\cos\alpha$ 与 $\tan\alpha$。

解：由

$$
\sin^2\alpha+\cos^2\alpha=1
$$

得

$$
\cos^2\alpha=1-\frac9{25}=\frac{16}{25}.
$$

因为 $\alpha$ 在第二象限，$\cos\alpha<0$，所以

$$
\cos\alpha=-\frac45.
$$

于是

$$
\tan\alpha=\frac{\sin\alpha}{\cos\alpha}
=\frac{3/5}{-4/5}=-\frac34.
$$

本题关键不是开方，而是开方后必须由象限决定符号。

### 例 2：图像变换

求函数

$$
y=2\sin\left(3x-\frac\pi2\right)+1
$$

的周期和值域。

解：周期为

$$
T=\frac{2\pi}{3}.
$$

因为 $\sin$ 的值域是 $[-1,1]$，所以 $2\sin(\cdots)$ 的值域是 $[-2,2]$，再整体上移 1，值域为

$$
[-1,3].
$$

注意：水平平移量是 $\dfrac{\pi/2}{3}=\dfrac\pi6$ 向右，但本题问周期和值域，不必先画完整图像。

### 例 3：恒等化简

化简：

$$
\sin x\cos x+\sin x\cos x.
$$

解：

$$
\sin x\cos x+\sin x\cos x=2\sin x\cos x=\sin2x.
$$

这道题看起来简单，但它展示了恒等变换的方向：当题目中出现 $2\sin x\cos x$，可以把它压缩成 $\sin2x$；当需要展开时，也可以反向使用。

## 自我训练

### 训练 1

已知 $\cos\alpha=-\dfrac{12}{13}$，且 $\alpha$ 是第三象限角，求 $\sin\alpha$ 与 $\tan\alpha$。

:::solution 查看解析
由 $\sin^2\alpha+\cos^2\alpha=1$ 得 $\sin^2\alpha=1-\frac{144}{169}=\frac{25}{169}$。第三象限中 $\sin\alpha<0$，所以 $\sin\alpha=-\frac5{13}$。于是 $\tan\alpha=\frac{\sin\alpha}{\cos\alpha}=\frac{-5/13}{-12/13}=\frac5{12}$。
:::

### 训练 2

化简 $\sin(\pi-x)+\cos(\pi+x)$。

:::solution 查看解析
$\sin(\pi-x)=\sin x$，$\cos(\pi+x)=-\cos x$，所以原式为 $\sin x-\cos x$。关键是回到单位圆对称，而不是只背“奇变偶不变”。
:::

### 训练 3

求 $y=3\cos(2x+\pi)-2$ 的周期和值域。

:::solution 查看解析
周期 $T=\frac{2\pi}{2}=\pi$。因为 $\cos$ 的值域是 $[-1,1]$，乘以 3 得 $[-3,3]$，再下移 2 得 $[-5,1]$。
:::

### 训练 4

证明：

$$
\frac{1-\cos2x}{\sin2x}=\tan x
$$

其中 $\sin2x\ne0$ 且 $\cos x\ne0$。

:::solution 查看解析
由 $1-\cos2x=2\sin^2x$，$\sin2x=2\sin x\cos x$，所以左边
$$
\frac{2\sin^2x}{2\sin x\cos x}=\frac{\sin x}{\cos x}=\tan x.
$$
化简中约去 $\sin x$ 时要注意原式 $\sin2x\ne0$ 已经保证 $\sin x\ne0$ 且 $\cos x\ne0$。
:::

### 训练 5

解方程：

$$
\sin x=\frac12.
$$

:::solution 查看解析
在一个周期内，$x=\frac\pi6$ 或 $x=\frac{5\pi}6$。因此全体解为
$$
x=2k\pi+\frac\pi6
\quad\text{或}\quad
x=2k\pi+\frac{5\pi}6,\qquad k\in\mathbb Z.
$$
不能只写一个特殊角。
:::

### 训练 6

若 $\tan\alpha=2$，求

$$
\frac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}.
$$

:::solution 查看解析
分子分母同除以 $\cos\alpha$，需有 $\cos\alpha\ne0$。由 $\tan\alpha=2$ 可知 $\cos\alpha\ne0$，所以
$$
\frac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}
=\frac{\tan\alpha+1}{\tan\alpha-1}
=\frac{2+1}{2-1}=3.
$$
:::

## 费曼讲题任务

下节课让学生选训练 1、训练 4 或训练 5 中任意一道讲给你听。你只追问三点：

1. 这个题研究的是角、图像、恒等式还是方程？
2. 哪个条件决定了符号、周期或定义域？
3. 如果把角的范围改变，答案会不会变？
