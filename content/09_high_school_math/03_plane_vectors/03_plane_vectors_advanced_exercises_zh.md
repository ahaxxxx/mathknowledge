# 平面向量进阶题库：本地资料梳理与高考题型补充

这一页把本地考点 56、57、58 的平面向量资料整理成一套进阶题库，并补充数量积、投影、轨迹与范围等高考常见题型。

返回专题首页：[平面向量](./README.md)。基础题入口：[平面向量专项练习](./02_plane_vectors_exercises_zh.md)。

这一页不是把题目原样堆上来，而是先把本地资料中的题型结构抽出来，再重新写成适合课堂讲解和课后复述的题库。学生做题时不要只算答案，要能说出：这道题到底把哪个几何关系翻译成了向量关系。

## 本地资料梳理

当前文件夹中可用的平面向量资料主要来自 `考点讲解2021年高考数学复习一轮复习笔记（65个考点讲解全）`，对应三组资料：

1. 考点 56：平面向量的线性运算及基本定理。重点是相等向量、共线向量、线性表示、基底分解、分点和参数。
2. 考点 57：平面向量数量积。重点是数量积计算、夹角、投影、垂直、长度平方和参数。
3. 考点 58：平面向量的应用。重点是判断三角形形状、向量与几何图形结合、最值范围和简单轨迹。

网上资料补充时，我主要校验了三个标准对象：线性组合、数量积、向量投影。可以把它们看成三条主线：

1. 线性组合：把几何图形中的点和线段放进同一组基底里。
2. 数量积：把夹角、垂直、投影、长度平方统一成一个代数运算。
3. 投影：把“一个方向上的分量”从图形语言转成数量积公式。

参考入口：[linear combination](https://en.wikipedia.org/wiki/Linear_combination)、[dot product](https://en.wikipedia.org/wiki/Dot_product)、[vector projection](https://en.wikipedia.org/wiki/Vector_projection)。

## 题型地图

1. 看到“向量相等、单位向量、命题真假”，先回到定义，不要拿长度代替方向。
2. 看到“点在线段上、三点共线、分点”，优先设基底，把点写成 $\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}$。
3. 看到“夹角、垂直、投影、长度”，优先想到数量积。
4. 看到“最值、范围、轨迹”，把目标写成平方或坐标，再看二次函数、距离公式或圆。
5. 看到“三角形形状”，把等腰、直角、钝角、等边翻译成长度平方和数量积。

## A. 线性运算、相等向量与命题辨析

### 题 1：向量命题真假

判断下列命题的真假，并写出错误命题的序号。

1. 两个有公共起点的非零向量一定共线。
2. 若 $\vec a=\vec b$，则 $|\vec a|=|\vec b|$。
3. 若 $|\vec a|=|\vec b|$，则 $\vec a=\vec b$。
4. 若 $\lambda \vec a=\vec 0$ 且 $\vec a\ne \vec 0$，则 $\lambda=0$。

:::solution 查看解析
命题 1 错。公共起点只说明两支箭头从同一点出发，不说明方向相同或相反。

命题 2 对。相等向量要求长度相等、方向相同，所以模一定相等。

命题 3 错。长度相等不代表方向相同。

命题 4 对。非零向量乘一个实数得到零向量，只能是实数为 0。

所以错误命题是 1 和 3。
:::

### 题 2：单位向量与投影

已知 $\vec a,\vec b$ 都是单位向量，且夹角为 $120^\circ$。求 $|\vec a+\vec b|$，并求 $\vec a$ 在 $\vec b$ 方向上的投影。

:::solution 查看解析
先算数量积：

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos120^\circ=-\frac12.
$$

于是

$$
|\vec a+\vec b|^2
=|\vec a|^2+|\vec b|^2+2\vec a\cdot\vec b
=1+1-1=1,
$$

所以

$$
|\vec a+\vec b|=1.
$$

$\vec a$ 在 $\vec b$ 方向上的投影是有符号长度：

$$
\frac{\vec a\cdot\vec b}{|\vec b|}=-\frac12.
$$
:::

### 题 3：首尾相接与反向

在四边形 $ABCD$ 中，化简

$$
\overrightarrow{AB}+\overrightarrow{BC}-\overrightarrow{DC}.
$$

:::solution 查看解析
先把减法变成加反向量：

$$
-\overrightarrow{DC}=\overrightarrow{CD}.
$$

所以原式为

$$
\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}.
$$

首尾相接：

$$
\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC},
$$

再接上 $\overrightarrow{CD}$：

$$
\overrightarrow{AC}+\overrightarrow{CD}=\overrightarrow{AD}.
$$

答案是 $\overrightarrow{AD}$。
:::

### 题 4：由线性关系判断方向

已知 $\vec b\ne \vec 0$，且

$$
2\vec a-3\vec b=\vec 0.
$$

判断 $\vec a,\vec b$ 是否共线，并说明方向关系。

:::solution 查看解析
由题意

$$
2\vec a=3\vec b,
$$

所以

$$
\vec a=\frac32\vec b.
$$

一个向量是另一个非零向量的实数倍，所以二者共线。因为系数 $\frac32>0$，所以方向相同。
:::

### 题 5：平行四边形中的对角线

在平行四边形 $ABCD$ 中，设 $\overrightarrow{AB}=\vec a,\overrightarrow{AD}=\vec b$，$O$ 是对角线交点。用 $\vec a,\vec b$ 表示 $\overrightarrow{AO}$ 和 $\overrightarrow{BD}$。

:::solution 查看解析
平行四边形对角线互相平分，所以

$$
\overrightarrow{AC}=\vec a+\vec b,\qquad
\overrightarrow{AO}=\frac12\overrightarrow{AC}
=\frac{\vec a+\vec b}{2}.
$$

从 $B$ 到 $D$ 可以走 $B\to A\to D$：

$$
\overrightarrow{BD}
=\overrightarrow{BA}+\overrightarrow{AD}
=-\vec a+\vec b
=\vec b-\vec a.
$$
:::

## B. 基底分解、分点与参数表示

### 题 6：内分点表示

在 $\triangle ABC$ 中，$D$ 在 $BC$ 上，且 $BD:DC=2:1$。设 $\overrightarrow{AB}=\vec b,\overrightarrow{AC}=\vec c$，用 $\vec b,\vec c$ 表示 $\overrightarrow{AD}$。

:::solution 查看解析
$BD:DC=2:1$，说明 $D$ 更靠近 $C$，从 $B$ 到 $C$ 走了全程的 $\frac23$。

$$
\overrightarrow{AD}
=\overrightarrow{AB}+\overrightarrow{BD}
=\vec b+\frac23\overrightarrow{BC}.
$$

而

$$
\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}
=\vec c-\vec b.
$$

所以

$$
\overrightarrow{AD}
=\vec b+\frac23(\vec c-\vec b)
=\frac13\vec b+\frac23\vec c.
$$
:::

### 题 7：两边分点连线

在 $\triangle ABC$ 中，点 $E$ 在 $AB$ 上，$AE:EB=1:2$；点 $F$ 在 $AC$ 上，$AF:FC=2:1$。设 $\overrightarrow{AB}=\vec b,\overrightarrow{AC}=\vec c$，求 $\overrightarrow{EF}$。

:::solution 查看解析
由 $AE:EB=1:2$ 得

$$
\overrightarrow{AE}=\frac13\vec b.
$$

由 $AF:FC=2:1$ 得

$$
\overrightarrow{AF}=\frac23\vec c.
$$

于是

$$
\overrightarrow{EF}
=\overrightarrow{AF}-\overrightarrow{AE}
=-\frac13\vec b+\frac23\vec c.
$$
:::

### 题 8：重心向量

在 $\triangle ABC$ 中，$G$ 是重心。设 $\overrightarrow{AB}=\vec b,\overrightarrow{AC}=\vec c$，求 $\overrightarrow{AG}$。

:::solution 查看解析
以 $A$ 为原点理解，$B$ 的位置向量是 $\vec b$，$C$ 的位置向量是 $\vec c$，$A$ 的位置向量是 $\vec 0$。

重心的位置向量是三个顶点位置向量的平均：

$$
\overrightarrow{AG}
=\frac{\vec 0+\vec b+\vec c}{3}
=\frac{\vec b+\vec c}{3}.
$$
:::

### 题 9：平行四边形边上中点

在平行四边形 $ABCD$ 中，$\overrightarrow{AB}=\vec a,\overrightarrow{AD}=\vec b$。点 $E$ 是 $BC$ 的中点，求 $\overrightarrow{AE}$。

:::solution 查看解析
因为 $BC\parallel AD$ 且相等，所以

$$
\overrightarrow{BC}=\vec b.
$$

点 $E$ 是 $BC$ 的中点：

$$
\overrightarrow{BE}=\frac12\vec b.
$$

于是

$$
\overrightarrow{AE}
=\overrightarrow{AB}+\overrightarrow{BE}
=\vec a+\frac12\vec b.
$$
:::

### 题 10：中线上的参数

在 $\triangle ABC$ 中，点 $P$ 在从 $A$ 到 $BC$ 中点 $M$ 的中线段上。设

$$
\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}.
$$

说明 $x,y$ 满足什么关系。

:::solution 查看解析
先写出中点 $M$：

$$
\overrightarrow{AM}
=\frac{\overrightarrow{AB}+\overrightarrow{AC}}2.
$$

因为 $P$ 在中线段 $AM$ 上，所以存在 $0\le t\le 1$，使

$$
\overrightarrow{AP}=t\overrightarrow{AM}
=\frac t2\overrightarrow{AB}+\frac t2\overrightarrow{AC}.
$$

因此

$$
x=y,\qquad 0\le x=y\le \frac12.
$$
:::

## C. 共线、三点共线与取值范围

### 题 11：非共线基底下的共线参数

已知 $\vec a,\vec b$ 不共线，

$$
\vec u=\vec a+(t-1)\vec b,\qquad
\vec v=2\vec a+(3t-1)\vec b.
$$

若 $\vec u\parallel \vec v$，求 $t$。

:::solution 查看解析
在基底 $\vec a,\vec b$ 下，两个向量共线等价于对应系数成比例，即

$$
\begin{vmatrix}
1 & t-1\\
2 & 3t-1
\end{vmatrix}=0.
$$

所以

$$
1(3t-1)-2(t-1)=0,
$$

即

$$
3t-1-2t+2=0.
$$

因此

$$
t=-1.
$$
:::

### 题 12：点在边上的判定

在 $\triangle ABC$ 中，设

$$
\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}.
$$

写出 $P$ 在直线 $BC$ 上、在线段 $BC$ 上分别对应的条件。

:::solution 查看解析
点在直线 $BC$ 上时，可以写成

$$
\overrightarrow{AP}=(1-s)\overrightarrow{AB}+s\overrightarrow{AC}
$$

其中 $s$ 为实数。

所以直线 $BC$ 上的条件是

$$
x+y=1.
$$

如果 $P$ 在线段 $BC$ 上，还要 $0\le s\le 1$，也就是两个权重都非负：

$$
x+y=1,\qquad x\ge0,\qquad y\ge0.
$$
:::

### 题 13：平行线中的比例

在 $\triangle ABC$ 中，$P$ 在 $AB$ 上，$AP:PB=m:1$；$Q$ 在 $AC$ 上，$AQ:QC=2:3$。若 $PQ\parallel BC$，求 $m$。

:::solution 查看解析
设 $\overrightarrow{AB}=\vec b,\overrightarrow{AC}=\vec c$。

由 $AP:PB=m:1$ 得

$$
\overrightarrow{AP}=\frac{m}{m+1}\vec b.
$$

由 $AQ:QC=2:3$ 得

$$
\overrightarrow{AQ}=\frac25\vec c.
$$

于是

$$
\overrightarrow{PQ}
=-\frac{m}{m+1}\vec b+\frac25\vec c.
$$

又

$$
\overrightarrow{BC}=-\vec b+\vec c.
$$

若 $PQ\parallel BC$，两个系数要按同一比例对应：

$$
\frac{m}{m+1}=\frac25.
$$

解得

$$
5m=2m+2,\qquad m=\frac23.
$$
:::

### 题 14：延长线上的系数

在 $\triangle ABC$ 中，点 $P$ 在 $BC$ 的延长线上，且在 $C$ 的外侧。若

$$
\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC},
$$

写出 $x,y$ 应满足的条件。

:::solution 查看解析
点在直线 $BC$ 上，先有

$$
x+y=1.
$$

如果 $P$ 在 $C$ 的外侧，说明从 $B$ 到 $C$ 的参数超过 1：

$$
\overrightarrow{AP}=(1-s)\overrightarrow{AB}+s\overrightarrow{AC},\qquad s>1.
$$

因此

$$
y>1,\qquad x=1-y<0.
$$

条件可以写成

$$
x+y=1,\qquad x<0,\qquad y>1.
$$
:::

### 题 15：三角形内部点的范围

在 $\triangle ABC$ 中，

$$
\overrightarrow{AP}=m\overrightarrow{AB}+(2-3m)\overrightarrow{AC}.
$$

若 $P$ 在 $\triangle ABC$ 的内部，求 $m$ 的取值范围。

:::solution 查看解析
若

$$
\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC},
$$

则 $P$ 在三角形内部的条件是

$$
x>0,\qquad y>0,\qquad x+y<1.
$$

本题中

$$
x=m,\qquad y=2-3m.
$$

所以

$$
m>0,\qquad 2-3m>0,\qquad m+2-3m<1.
$$

整理得

$$
m>0,\qquad m<\frac23,\qquad m>\frac12.
$$

因此

$$
\frac12<m<\frac23.
$$
:::

## D. 坐标法、数量积与夹角

### 题 16：坐标数量积

已知 $\vec a=(2,-1),\vec b=(1,3)$，求 $\vec a\cdot\vec b$ 以及两向量夹角的余弦值。

:::solution 查看解析
数量积为

$$
\vec a\cdot\vec b=2\cdot1+(-1)\cdot3=-1.
$$

模长为

$$
|\vec a|=\sqrt5,\qquad |\vec b|=\sqrt{10}.
$$

因此

$$
\cos\theta
=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|}
=-\frac{1}{\sqrt{50}}.
$$
:::

### 题 17：坐标判断直角

已知 $A(1,1),B(4,1),C(4,5)$。求 $\angle ABC$ 的大小。

:::solution 查看解析
角 $ABC$ 的两条边对应向量是

$$
\overrightarrow{BA}=A-B=(-3,0),
$$

$$
\overrightarrow{BC}=C-B=(0,4).
$$

数量积

$$
\overrightarrow{BA}\cdot\overrightarrow{BC}=(-3)\cdot0+0\cdot4=0.
$$

所以两向量垂直，

$$
\angle ABC=90^\circ.
$$
:::

### 题 18：参数垂直

已知 $\vec a=(1,2),\vec b=(t,-1)$。若 $\vec a\perp\vec b$，求 $t$。

:::solution 查看解析
垂直等价于数量积为 0：

$$
\vec a\cdot\vec b=1\cdot t+2\cdot(-1)=t-2.
$$

令

$$
t-2=0,
$$

得

$$
t=2.
$$
:::

### 题 19：夹角为 $60^\circ$

已知 $\vec a=(2,0),\vec b=(1,t)$，若 $\vec a,\vec b$ 的夹角为 $60^\circ$，求 $t$。

:::solution 查看解析
先写余弦公式：

$$
\cos60^\circ
=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|}.
$$

其中

$$
\vec a\cdot\vec b=2,\qquad
|\vec a|=2,\qquad
|\vec b|=\sqrt{1+t^2}.
$$

所以

$$
\frac12=\frac{2}{2\sqrt{1+t^2}}
=\frac1{\sqrt{1+t^2}}.
$$

因此

$$
\sqrt{1+t^2}=2,\qquad t^2=3.
$$

所以

$$
t=\pm\sqrt3.
$$
:::

### 题 20：组合向量的数量积

已知 $\vec a=(1,2),\vec b=(2,-1)$，求

$$
(2\vec a-\vec b)\cdot(\vec a+\vec b).
$$

:::solution 查看解析
先观察：

$$
\vec a\cdot\vec b=1\cdot2+2\cdot(-1)=0,
$$

并且

$$
|\vec a|^2=5,\qquad |\vec b|^2=5.
$$

展开：

$$
(2\vec a-\vec b)\cdot(\vec a+\vec b)
=2|\vec a|^2+2\vec a\cdot\vec b-\vec b\cdot\vec a-|\vec b|^2.
$$

代入得

$$
2\cdot5+0-0-5=5.
$$
:::

## E. 投影、垂直与长度平方

### 题 21：投影长度和投影向量

已知 $\vec a=(3,4),\vec b=(1,0)$。求 $\vec a$ 在 $\vec b$ 方向上的投影长度，并求 $\vec a$ 在 $\vec b$ 方向上的投影向量。

:::solution 查看解析
$\vec b$ 是 $x$ 轴正方向单位向量，所以可以直接看出投影长度是 3。

用公式验证：

$$
\frac{\vec a\cdot\vec b}{|\vec b|}
=\frac{3}{1}=3.
$$

投影向量为

$$
\frac{\vec a\cdot\vec b}{|\vec b|^2}\vec b
=3(1,0)=(3,0).
$$
:::

### 题 22：加一个倍数使垂直

已知 $\vec a=(2,1),\vec b=(1,1)$。求实数 $k$，使

$$
\vec a+k\vec b\perp \vec b.
$$

:::solution 查看解析
垂直等价于数量积为 0：

$$
(\vec a+k\vec b)\cdot\vec b=0.
$$

展开：

$$
\vec a\cdot\vec b+k|\vec b|^2=0.
$$

计算

$$
\vec a\cdot\vec b=3,\qquad |\vec b|^2=2.
$$

所以

$$
3+2k=0,\qquad k=-\frac32.
$$
:::

### 题 23：长度平方展开

已知 $|\vec a|=3,|\vec b|=2$，且 $\vec a,\vec b$ 的夹角为 $60^\circ$。求 $|2\vec a-\vec b|$。

:::solution 查看解析
先算

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos60^\circ=3.
$$

然后展开长度平方：

$$
|2\vec a-\vec b|^2
=(2\vec a-\vec b)\cdot(2\vec a-\vec b).
$$

所以

$$
|2\vec a-\vec b|^2
=4|\vec a|^2-4\vec a\cdot\vec b+|\vec b|^2
=36-12+4=28.
$$

因此

$$
|2\vec a-\vec b|=2\sqrt7.
$$
:::

### 题 24：距离平方和最小

已知 $A(-1,0),B(3,0)$，点 $P=(x,2)$ 在直线 $y=2$ 上。求

$$
|PA|^2+|PB|^2
$$

的最小值。

:::solution 查看解析
设 $AB$ 的中点为 $M(1,0)$。有恒等式

$$
|PA|^2+|PB|^2
=2|PM|^2+\frac12|AB|^2.
$$

这里

$$
|AB|=4,\qquad |PM|^2=(x-1)^2+4.
$$

所以

$$
|PA|^2+|PB|^2
=2[(x-1)^2+4]+8.
$$

当 $x=1$ 时最小，最小值为

$$
2\cdot4+8=16.
$$
:::

### 题 25：中线长度

在 $\triangle ABC$ 中，$AB=5,AC=7,\angle BAC=60^\circ$。$M$ 是 $BC$ 的中点，求 $AM$。

:::solution 查看解析
令

$$
\vec u=\overrightarrow{AB},\qquad \vec v=\overrightarrow{AC}.
$$

则

$$
\overrightarrow{AM}=\frac{\vec u+\vec v}{2}.
$$

所以

$$
AM^2=\frac14|\vec u+\vec v|^2
=\frac14(|\vec u|^2+|\vec v|^2+2\vec u\cdot\vec v).
$$

而

$$
\vec u\cdot\vec v=5\cdot7\cos60^\circ=\frac{35}{2}.
$$

于是

$$
AM^2=\frac14(25+49+35)=\frac{109}{4}.
$$

因此

$$
AM=\frac{\sqrt{109}}2.
$$
:::

## F. 向量与三角形形状判断

### 题 26：坐标判断三角形形状

已知 $A(0,0),B(4,0),C(1,\sqrt{15})$。判断 $\triangle ABC$ 的形状。

:::solution 查看解析
计算三边平方：

$$
AB^2=16.
$$

$$
AC^2=1^2+(\sqrt{15})^2=16.
$$

$$
BC^2=(1-4)^2+(\sqrt{15}-0)^2=9+15=24.
$$

所以 $AB=AC$，但不满足直角关系。因此 $\triangle ABC$ 是等腰三角形。
:::

### 题 27：由数量积等式判断等腰

在 $\triangle ABC$ 中，若

$$
(\overrightarrow{AB}+\overrightarrow{AC})\cdot
(\overrightarrow{AB}-\overrightarrow{AC})=0,
$$

判断三角形形状。

:::solution 查看解析
利用平方差结构：

$$
(\vec u+\vec v)\cdot(\vec u-\vec v)
=|\vec u|^2-|\vec v|^2.
$$

令 $\vec u=\overrightarrow{AB},\vec v=\overrightarrow{AC}$，题设变成

$$
AB^2-AC^2=0.
$$

所以

$$
AB=AC.
$$

因此 $\triangle ABC$ 是以 $A$ 为顶点的等腰三角形。
:::

### 题 28：等腰直角

在 $\triangle ABC$ 中，若

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}=0,
\qquad
|\overrightarrow{AB}|=|\overrightarrow{AC}|,
$$

判断 $\triangle ABC$ 的形状。

:::solution 查看解析
数量积为 0 说明

$$
AB\perp AC.
$$

又因为

$$
AB=AC,
$$

所以 $\angle A=90^\circ$，且两条直角边相等。

因此 $\triangle ABC$ 是以 $A$ 为直角顶点的等腰直角三角形。
:::

### 题 29：由数量积判断等边

在 $\triangle ABC$ 中，已知

$$
|\overrightarrow{AB}|=|\overrightarrow{AC}|=2,
\qquad
\overrightarrow{AB}\cdot\overrightarrow{AC}=2.
$$

判断 $\triangle ABC$ 的形状。

:::solution 查看解析
设 $\angle BAC=\theta$，则

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}
=|\overrightarrow{AB}||\overrightarrow{AC}|\cos\theta.
$$

代入：

$$
2=2\cdot2\cos\theta,
$$

所以

$$
\cos\theta=\frac12,\qquad \theta=60^\circ.
$$

两边相等且夹角为 $60^\circ$，第三边也为 2，所以三角形为等边三角形。
:::

### 题 30：钝角判断

在 $\triangle ABC$ 中，若

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}<0,
$$

说明 $\angle A$ 的类型，并判断三角形形状。

:::solution 查看解析
数量积公式为

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}
=AB\cdot AC\cdot \cos A.
$$

因为 $AB,AC>0$，所以数量积的符号由 $\cos A$ 决定。

题设数量积小于 0，说明

$$
\cos A<0.
$$

因此

$$
90^\circ<A<180^\circ.
$$

$\triangle ABC$ 是钝角三角形，钝角为 $\angle A$。
:::

## G. 向量应用：最值、范围与轨迹

### 题 31：带参数的长度范围

已知 $\vec a,\vec b$ 都是单位向量，夹角为 $120^\circ$。当 $0\le t\le2$ 时，求

$$
|\vec a+t\vec b|
$$

的取值范围。

:::solution 查看解析
先平方：

$$
|\vec a+t\vec b|^2
=|\vec a|^2+t^2|\vec b|^2+2t\vec a\cdot\vec b.
$$

因为

$$
\vec a\cdot\vec b=\cos120^\circ=-\frac12,
$$

所以

$$
|\vec a+t\vec b|^2
=1+t^2-t
=\left(t-\frac12\right)^2+\frac34.
$$

当 $0\le t\le2$ 时，平方的最小值在 $t=\frac12$ 处，为 $\frac34$。

最大值比较端点：

$$
t=0\Rightarrow 1,\qquad t=2\Rightarrow 3.
$$

所以

$$
\frac{\sqrt3}{2}\le |\vec a+t\vec b|\le \sqrt3.
$$
:::

### 题 32：直径所对圆周角

已知 $A(0,0),B(4,0)$。动点 $P(x,y)$ 满足

$$
\overrightarrow{PA}\cdot\overrightarrow{PB}=0.
$$

求点 $P$ 的轨迹方程。

:::solution 查看解析
先写向量：

$$
\overrightarrow{PA}=A-P=(-x,-y),
$$

$$
\overrightarrow{PB}=B-P=(4-x,-y).
$$

数量积为 0：

$$
(-x)(4-x)+(-y)(-y)=0.
$$

整理：

$$
x^2-4x+y^2=0.
$$

配方：

$$
(x-2)^2+y^2=4.
$$

所以轨迹是以 $(2,0)$ 为圆心、半径为 2 的圆。几何意义是：以 $AB$ 为直径的圆上，$\angle APB=90^\circ$。
:::

### 题 33：点到直线的最短距离

点 $P(x,y)$ 在直线 $x+y=4$ 上。求 $|\overrightarrow{OP}|^2=x^2+y^2$ 的最小值。

:::solution 查看解析
要让 $x^2+y^2$ 最小，就是找直线 $x+y=4$ 上离原点最近的点。

最近点在法向量方向上。直线 $x+y=4$ 的法向量是 $(1,1)$，所以最近点形如

$$
P=(t,t).
$$

代入直线：

$$
2t=4,\qquad t=2.
$$

所以最近点是 $(2,2)$，最小值为

$$
2^2+2^2=8.
$$
:::

### 题 34：夹角变化时的长度范围

已知 $|\vec a|=2,|\vec b|=3$，$\vec a,\vec b$ 的夹角可以变化。求

$$
|\vec a+\vec b|
$$

的取值范围。

:::solution 查看解析
设夹角为 $\theta$，则

$$
|\vec a+\vec b|^2
=|\vec a|^2+|\vec b|^2+2|\vec a||\vec b|\cos\theta.
$$

代入：

$$
|\vec a+\vec b|^2=4+9+12\cos\theta.
$$

因为

$$
-1\le\cos\theta\le1,
$$

所以

$$
1\le|\vec a+\vec b|^2\le25.
$$

因此

$$
1\le|\vec a+\vec b|\le5.
$$
:::

### 题 35：点在线段上时的最短距离

在 $\triangle ABC$ 中，$AB=6,AC=8,\angle BAC=60^\circ$。点 $P$ 在线段 $BC$ 上，求 $AP$ 的最小值。

:::solution 查看解析
点 $P$ 在线段 $BC$ 上，$AP$ 的最小值就是 $A$ 到直线 $BC$ 的距离。先求面积：

$$
S_{\triangle ABC}
=\frac12\cdot AB\cdot AC\cdot\sin60^\circ
=\frac12\cdot6\cdot8\cdot\frac{\sqrt3}{2}
=12\sqrt3.
$$

再求 $BC$：

$$
BC^2=6^2+8^2-2\cdot6\cdot8\cos60^\circ
=36+64-48=52.
$$

所以

$$
BC=2\sqrt{13}.
$$

设高为 $h$，则

$$
S=\frac12BC\cdot h.
$$

于是

$$
h=\frac{2S}{BC}
=\frac{24\sqrt3}{2\sqrt{13}}
=12\sqrt{\frac3{13}}.
$$

所以 $AP$ 的最小值为

$$
12\sqrt{\frac3{13}}.
$$
:::

## H. 高考小题速度训练

### 题 36：共线填空

已知 $\vec a=(m,2),\vec b=(3,6)$，若 $\vec a\parallel\vec b$，求 $m$。

:::solution 查看解析
共线等价于坐标行列式为 0：

$$
6m-2\cdot3=0.
$$

所以

$$
6m-6=0,\qquad m=1.
$$
:::

### 题 37：单位向量差的长度

已知 $|\vec a|=|\vec b|=1$，且 $\vec a\cdot\vec b=\frac12$。求 $|\vec a-\vec b|$。

:::solution 查看解析
平方：

$$
|\vec a-\vec b|^2
=|\vec a|^2+|\vec b|^2-2\vec a\cdot\vec b.
$$

代入：

$$
|\vec a-\vec b|^2
=1+1-2\cdot\frac12=1.
$$

所以

$$
|\vec a-\vec b|=1.
$$
:::

### 题 38：中点位置向量

已知 $A(1,2),B(5,6)$，$M$ 是 $AB$ 的中点。求 $\overrightarrow{OM}$。

:::solution 查看解析
中点坐标为

$$
M\left(\frac{1+5}{2},\frac{2+6}{2}\right)=(3,4).
$$

所以

$$
\overrightarrow{OM}=(3,4).
$$
:::

### 题 39：由系数读线段比

在 $\triangle ABC$ 中，

$$
\overrightarrow{AP}
=\frac14\overrightarrow{AB}
+\frac34\overrightarrow{AC}.
$$

判断 $P$ 在哪条边上，并求 $BP:PC$。

:::solution 查看解析
两个系数相加：

$$
\frac14+\frac34=1.
$$

所以 $P$ 在直线 $BC$ 上；两个系数都非负，所以 $P$ 在线段 $BC$ 上。

把式子写成

$$
\overrightarrow{AP}
=(1-s)\overrightarrow{AB}+s\overrightarrow{AC}.
$$

可见

$$
s=\frac34.
$$

这表示从 $B$ 到 $C$ 走了全程的 $\frac34$，所以

$$
BP:PC=3:1.
$$
:::

### 题 40：由数量积判断同向

已知 $|\vec a|=2,|\vec b|=1$，且

$$
\vec a\cdot(\vec a-2\vec b)=0.
$$

求 $\vec a,\vec b$ 的夹角。

:::solution 查看解析
展开题设：

$$
\vec a\cdot\vec a-2\vec a\cdot\vec b=0.
$$

即

$$
|\vec a|^2=2\vec a\cdot\vec b.
$$

因为 $|\vec a|=2$，所以

$$
4=2\vec a\cdot\vec b,
$$

从而

$$
\vec a\cdot\vec b=2.
$$

设夹角为 $\theta$：

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta
=2\cdot1\cdot\cos\theta.
$$

所以

$$
2=2\cos\theta,\qquad \cos\theta=1.
$$

因此

$$
\theta=0^\circ.
$$
:::

## 使用建议

1. A、B、C 三组适合在讲完“基底与共线”之后当天布置。
2. D、E 两组适合在讲完数量积之后布置，要求学生每题都说出“数量积翻译了什么”。
3. F、G 两组适合周日 2 小时课做综合讲评。
4. H 组适合作为上课前 10 分钟口算或小测，训练题型识别速度。
