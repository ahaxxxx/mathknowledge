# 平面向量专项练习

返回讲义：[平面向量：从几何语言到代数工具](./01_plane_vectors_zh.md)。

这份练习按题型识别编排，共 6 类，每类 5 题。做题时先判断题型，再写计算；点开解析前，先尝试把“为什么这样翻译”讲出来。

## A. 向量线性运算与几何意义

### 题 1：首尾相接

在四边形 $ABCD$ 中，化简 $\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}$。

:::solution 查看解析
首尾相接：

$$
\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC},
$$

再加 $\overrightarrow{CD}$：

$$
\overrightarrow{AC}+\overrightarrow{CD}=\overrightarrow{AD}.
$$

所以结果为 $\overrightarrow{AD}$。
:::

### 题 2：减法转位移

化简 $\overrightarrow{OA}-\overrightarrow{OB}$。

:::solution 查看解析

$$
\overrightarrow{OA}-\overrightarrow{OB}
=\overrightarrow{OA}+\overrightarrow{BO}
=\overrightarrow{BA}.
$$

也可以记成“终点减起点”：

$$
\overrightarrow{BA}=\overrightarrow{OA}-\overrightarrow{OB}.
$$
:::

### 题 3：平行四边形法则

在平行四边形 $ABCD$ 中，已知 $\overrightarrow{AB}=\vec a,\overrightarrow{AD}=\vec b$，用 $\vec a,\vec b$ 表示 $\overrightarrow{AC}$。

:::solution 查看解析
对角线 $\overrightarrow{AC}$ 等于从 $A$ 到 $B$ 再从 $B$ 到 $C$。平行四边形中 $\overrightarrow{BC}=\overrightarrow{AD}=\vec b$，所以

$$
\overrightarrow{AC}=\vec a+\vec b.
$$
:::

### 题 4：相反向量

已知 $\overrightarrow{AB}=3\vec p-2\vec q$，求 $\overrightarrow{BA}$。

:::solution 查看解析
方向反过来就是相反向量：

$$
\overrightarrow{BA}=-\overrightarrow{AB}
=-3\vec p+2\vec q.
$$
:::

### 题 5：线性组合

已知 $\vec a=(2,-1),\vec b=(-3,4)$，求 $2\vec a-\vec b$。

:::solution 查看解析

$$
2\vec a=(4,-2),
$$

所以

$$
2\vec a-\vec b=(4,-2)-(-3,4)=(7,-6).
$$
:::

## B. 共线与基底分解

### 题 6：坐标共线判定

已知 $\vec a=(3,6),\vec b=(1,2)$，判断 $\vec a,\vec b$ 是否共线。

:::solution 查看解析
因为

$$
\vec a=3\vec b,
$$

所以二者共线。同样也可用

$$
3\cdot2-6\cdot1=0
$$

判断。
:::

### 题 7：求共线参数

已知 $\vec a=(2,5),\vec b=(6,t)$，若 $\vec a\parallel\vec b$，求 $t$。

:::solution 查看解析
共线条件：

$$
2t-5\cdot6=0.
$$

所以

$$
t=15.
$$
:::

### 题 8：三点共线

已知 $A(1,2),B(3,6),C(4,8)$，判断 $A,B,C$ 是否共线。

:::solution 查看解析

$$
\overrightarrow{AB}=(2,4),\qquad \overrightarrow{AC}=(3,6).
$$

因为

$$
\overrightarrow{AC}=\frac32\overrightarrow{AB},
$$

所以 $A,B,C$ 共线。
:::

### 题 9：基底表示中点

在 $\triangle ABC$ 中，$M$ 是 $BC$ 中点，设 $\overrightarrow{AB}=\vec a,\overrightarrow{AC}=\vec b$，求 $\overrightarrow{AM}$。

:::solution 查看解析
从 $A$ 看，$B$ 的位置为 $\vec a$，$C$ 的位置为 $\vec b$。中点取平均：

$$
\overrightarrow{AM}=\frac12(\vec a+\vec b).
$$
:::

### 题 10：分点表示

在 $\triangle ABC$ 中，点 $P$ 在 $BC$ 上，且 $BP:PC=2:1$。设 $\overrightarrow{AB}=\vec a,\overrightarrow{AC}=\vec b$，求 $\overrightarrow{AP}$。

:::solution 查看解析
$P$ 把 $BC$ 按 $2:1$ 内分，靠近 $C$，所以位置是端点加权平均：

$$
\overrightarrow{AP}
=\frac{1\cdot\overrightarrow{AB}+2\cdot\overrightarrow{AC}}{3}
=\frac13\vec a+\frac23\vec b.
$$

检查：当 $BP:PC=2:1$ 时，$P$ 离 $C$ 更近，因此 $\vec b$ 权重大，结果合理。
:::

## C. 坐标运算与点的位置

### 题 11：向量坐标

已知 $A(-1,3),B(4,-2)$，求 $\overrightarrow{AB}$。

:::solution 查看解析
终点减起点：

$$
\overrightarrow{AB}=(4-(-1),-2-3)=(5,-5).
$$
:::

### 题 12：中点坐标

已知 $A(2,-1),B(8,5)$，求 $AB$ 中点 $M$ 的坐标。

:::solution 查看解析
中点坐标取平均：

$$
M\left(\frac{2+8}{2},\frac{-1+5}{2}\right)=(5,2).
$$
:::

### 题 13：重心坐标

已知 $\triangle ABC$ 的三个顶点为 $A(1,2),B(4,-1),C(7,5)$，求重心 $G$。

:::solution 查看解析
重心坐标为三个顶点坐标平均：

$$
G\left(\frac{1+4+7}{3},\frac{2-1+5}{3}\right)=(4,2).
$$
:::

### 题 14：点的参数表示

已知 $A(1,1),B(7,4)$，点 $P$ 满足 $\overrightarrow{AP}=\frac13\overrightarrow{AB}$，求 $P$。

:::solution 查看解析

$$
\overrightarrow{AB}=(6,3),
$$

所以

$$
\overrightarrow{AP}=(2,1).
$$

因此

$$
P=A+\overrightarrow{AP}=(3,2).
$$
:::

### 题 15：由向量求点

已知 $A(2,3)$，且 $\overrightarrow{AB}=(-5,4)$，求 $B$。

:::solution 查看解析

$$
B=A+\overrightarrow{AB}=(2,3)+(-5,4)=(-3,7).
$$
:::

## D. 数量积、夹角与投影

### 题 16：数量积坐标公式

已知 $\vec a=(2,3),\vec b=(-1,4)$，求 $\vec a\cdot\vec b$。

:::solution 查看解析

$$
\vec a\cdot\vec b=2\cdot(-1)+3\cdot4=10.
$$
:::

### 题 17：夹角余弦

已知 $\vec a=(1,2),\vec b=(2,1)$，求两向量夹角的余弦值。

:::solution 查看解析

$$
\vec a\cdot\vec b=4,\qquad |\vec a|=|\vec b|=\sqrt5.
$$

所以

$$
\cos\theta=\frac4{\sqrt5\sqrt5}=\frac45.
$$
:::

### 题 18：垂直判定

已知 $\vec a=(3,-2),\vec b=(2,3)$，判断 $\vec a,\vec b$ 是否垂直。

:::solution 查看解析

$$
\vec a\cdot\vec b=3\cdot2+(-2)\cdot3=0.
$$

数量积为 0，所以 $\vec a\perp\vec b$。
:::

### 题 19：求垂直参数

已知 $\vec a=(m,2),\vec b=(4,-6)$，若 $\vec a\perp\vec b$，求 $m$。

:::solution 查看解析
垂直等价于数量积为 0：

$$
4m+2\cdot(-6)=0.
$$

所以

$$
m=3.
$$
:::

### 题 20：投影数量

已知 $\vec a=(3,4),\vec b=(1,0)$，求 $\vec a$ 在 $\vec b$ 方向上的投影数量。

:::solution 查看解析
投影数量为

$$
\frac{\vec a\cdot\vec b}{|\vec b|}
=\frac{3}{1}=3.
$$

这表示 $\vec a$ 沿 $x$ 轴正方向的分量是 3。
:::

## E. 长度、垂直与最值

### 题 21：向量长度

已知 $\vec a=(6,8)$，求 $|\vec a|$。

:::solution 查看解析

$$
|\vec a|=\sqrt{6^2+8^2}=10.
$$
:::

### 题 22：长度平方展开

已知 $|\vec a|=2,|\vec b|=3,\vec a\cdot\vec b=1$，求 $|\vec a+\vec b|^2$。

:::solution 查看解析

$$
|\vec a+\vec b|^2
=(\vec a+\vec b)\cdot(\vec a+\vec b)
=|\vec a|^2+2\vec a\cdot\vec b+|\vec b|^2.
$$

代入得

$$
4+2+9=15.
$$
:::

### 题 23：求参数使长度固定

已知 $\vec a=(t,1)$，若 $|\vec a|=\sqrt{10}$，求 $t$。

:::solution 查看解析

$$
t^2+1=10,
$$

所以

$$
t=\pm3.
$$
:::

### 题 24：垂直转方程

已知点 $A(1,0),B(5,2),C(3,t)$，若 $AB\perp AC$，求 $t$。

:::solution 查看解析

$$
\overrightarrow{AB}=(4,2),\qquad \overrightarrow{AC}=(2,t).
$$

垂直给出数量积为 0：

$$
4\cdot2+2t=0.
$$

所以

$$
t=-4.
$$
:::

### 题 25：二次式最值

已知 $\vec a=(x,2)$，求 $|\vec a|^2$ 的最小值。

:::solution 查看解析

$$
|\vec a|^2=x^2+4.
$$

当 $x=0$ 时最小，最小值为 4。
:::

## F. 向量与三角形综合

### 题 26：向量证明中线

在 $\triangle ABC$ 中，$M$ 是 $BC$ 中点。证明

$$
\overrightarrow{AB}+\overrightarrow{AC}=2\overrightarrow{AM}.
$$

:::solution 查看解析
由中点公式：

$$
\overrightarrow{AM}=\frac12(\overrightarrow{AB}+\overrightarrow{AC}).
$$

两边乘以 2，即得

$$
\overrightarrow{AB}+\overrightarrow{AC}=2\overrightarrow{AM}.
$$
:::

### 题 27：重心向量

在 $\triangle ABC$ 中，$G$ 是重心。设原点为 $O$，证明

$$
\overrightarrow{OG}=\frac{\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}}3.
$$

:::solution 查看解析
重心坐标等于三个顶点坐标平均。把坐标平均写成位置向量形式，就是

$$
\overrightarrow{OG}=\frac{\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}}3.
$$

这个公式不依赖坐标系选择，是仿射平均的向量表达。
:::

### 题 28：三角形直角判断

已知 $A(0,0),B(3,1),C(1,7)$，判断 $\angle ABC$ 是否为直角。

:::solution 查看解析
判断 $\angle ABC$，要看从 $B$ 出发的两个向量：

$$
\overrightarrow{BA}=(-3,-1),\qquad \overrightarrow{BC}=(-2,6).
$$

数量积为

$$
(-3)(-2)+(-1)6=0.
$$

所以 $\overrightarrow{BA}\perp\overrightarrow{BC}$，即 $\angle ABC=90^\circ$。
:::

### 题 29：三角形边长

已知 $A(1,1),B(5,4),C(2,5)$，求 $AB,AC$ 的长度，并判断 $AB$ 与 $AC$ 是否垂直。

:::solution 查看解析

$$
\overrightarrow{AB}=(4,3),\qquad \overrightarrow{AC}=(1,4).
$$

所以

$$
AB=5,\qquad AC=\sqrt{17}.
$$

数量积

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}=4\cdot1+3\cdot4=16\ne0.
$$

因此 $AB$ 与 $AC$ 不垂直。
:::

### 题 30：向量与夹角

在 $\triangle ABC$ 中，已知 $\overrightarrow{AB}=(2,1),\overrightarrow{AC}=(1,3)$，求 $\cos A$。

:::solution 查看解析
$A$ 是 $\overrightarrow{AB}$ 与 $\overrightarrow{AC}$ 的夹角。

$$
\overrightarrow{AB}\cdot\overrightarrow{AC}=2\cdot1+1\cdot3=5.
$$

$$
|\overrightarrow{AB}|=\sqrt5,\qquad |\overrightarrow{AC}|=\sqrt{10}.
$$

所以

$$
\cos A=\frac5{\sqrt5\sqrt{10}}=\frac1{\sqrt2}=\frac{\sqrt2}{2}.
$$
:::

## 讲题任务

从本页任选 2 道题让学生讲解。讲解时必须说清楚：

1. 这道题为什么可以用向量？
2. 用的是几何向量、基底表示，还是坐标法？
3. 哪个条件被翻译成了共线、垂直、长度或数量积？
4. 如果题目里的点或参数改变，方法是否仍然成立？
