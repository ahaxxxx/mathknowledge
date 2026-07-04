# 平面向量：从几何语言到代数工具

平面向量研究的不是“箭头怎么画”，而是：怎样把平面上的长度、方向、平移、夹角、垂直和共线，用统一的代数对象表达出来。它连接三角函数、解三角形、解析几何和立体几何，是高中数学里很典型的工具型模块。

## 研究对象

向量是有大小、有方向的量。两个向量只要长度相等、方向相同，就相等；它们不依赖于画在平面上的具体位置。因此向量也叫自由向量。

必须区分三种对象：

1. 点：例如 $A,B,C$，表示位置。
2. 有向线段：例如 $\overrightarrow{AB}$，从 $A$ 指向 $B$。
3. 自由向量：例如 $\vec a,\vec b$，只看长度和方向，不看起点。

位置向量是把点放到原点坐标系里看：若 $A(x_1,y_1)$，则

$$
\overrightarrow{OA}=(x_1,y_1).
$$

而

$$
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
$$

这句话非常重要：**从 A 到 B 的位移，等于终点位置向量减起点位置向量。**

## 核心知识结构

### 1. 向量加法：首尾相接

若先从 $A$ 到 $B$，再从 $B$ 到 $C$，总效果就是从 $A$ 到 $C$：

$$
\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}.
$$

这不是公式技巧，而是位移的合成。

:::diagram
<svg viewBox="0 0 520 210" role="img" aria-label="向量加法首尾相接示意图">
  <defs>
    <marker id="arrow-vector-add" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#0f6d69"></path>
    </marker>
  </defs>
  <rect x="1" y="1" width="518" height="208" rx="8" fill="#fffaf0" stroke="#d8c7a5"></rect>
  <circle cx="90" cy="150" r="4" fill="#263247"></circle>
  <circle cx="235" cy="70" r="4" fill="#263247"></circle>
  <circle cx="410" cy="135" r="4" fill="#263247"></circle>
  <line x1="90" y1="150" x2="235" y2="70" stroke="#0f6d69" stroke-width="4" marker-end="url(#arrow-vector-add)"></line>
  <line x1="235" y1="70" x2="410" y2="135" stroke="#0f6d69" stroke-width="4" marker-end="url(#arrow-vector-add)"></line>
  <line x1="90" y1="150" x2="410" y2="135" stroke="#c85c2b" stroke-width="4" marker-end="url(#arrow-vector-add)"></line>
  <text x="78" y="173" font-size="18" fill="#263247">A</text>
  <text x="226" y="52" font-size="18" fill="#263247">B</text>
  <text x="414" y="139" font-size="18" fill="#263247">C</text>
  <text x="135" y="93" font-size="16" fill="#0f6d69">AB</text>
  <text x="315" y="88" font-size="16" fill="#0f6d69">BC</text>
  <text x="235" y="169" font-size="16" fill="#c85c2b">AC = AB + BC</text>
</svg>
:::

### 2. 向量减法：转成加相反向量

$$
\vec a-\vec b=\vec a+(-\vec b).
$$

在图形里，最常用的减法形式是：

$$
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
$$

如果题目里有很多点，先把所有点写成同一个原点下的位置向量，往往就清楚了。

### 3. 数乘与共线

数乘 $k\vec a$ 改变长度和方向：

1. $k>0$：方向不变，长度变为 $|k|$ 倍。
2. $k<0$：方向相反，长度变为 $|k|$ 倍。
3. $k=0$：变成零向量。

共线的核心判定是：

$$
\vec a\parallel \vec b
\quad\Longleftrightarrow\quad
\vec a=\lambda\vec b
$$

其中 $\vec b\ne\vec 0$。坐标形式为：

$$
(x_1,y_1)\parallel(x_2,y_2)
\quad\Longleftrightarrow\quad
x_1y_2-x_2y_1=0.
$$

### 4. 基底表示：把图形拆成两个方向

若 $\vec e_1,\vec e_2$ 不共线，则平面内任意向量都能唯一写成

$$
\vec v=x\vec e_1+y\vec e_2.
$$

这就是“基底”。在三角形中，经常取

$$
\overrightarrow{AB}=\vec a,\qquad \overrightarrow{AC}=\vec b,
$$

然后把中点、重心、分点都表示成 $\vec a,\vec b$ 的组合。

例如 $M$ 是 $BC$ 中点，则

$$
\overrightarrow{AM}
=\frac12(\overrightarrow{AB}+\overrightarrow{AC})
=\frac12(\vec a+\vec b).
$$

### 5. 坐标表示：把向量变成有序数对

若 $\vec a=(x_1,y_1),\vec b=(x_2,y_2)$，则

$$
\vec a+\vec b=(x_1+x_2,y_1+y_2),
$$

$$
k\vec a=(kx_1,ky_1),
$$

$$
|\vec a|=\sqrt{x_1^2+y_1^2}.
$$

坐标法的优点是稳定：共线、垂直、长度、夹角都能转成方程。

### 6. 数量积：把夹角和长度变成乘法

数量积定义为

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta,
$$

其中 $\theta$ 是 $\vec a,\vec b$ 的夹角。

坐标形式为

$$
(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2.
$$

数量积负责四类问题：

1. 求夹角：

$$
\cos\theta=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|}.
$$

2. 判垂直：

$$
\vec a\perp\vec b\quad\Longleftrightarrow\quad \vec a\cdot\vec b=0.
$$

3. 求长度平方：

$$
|\vec a+\vec b|^2=(\vec a+\vec b)^2.
$$

4. 求投影：

$$
\vec a\text{ 在 }\vec b\text{ 方向上的投影数量}
=\frac{\vec a\cdot\vec b}{|\vec b|}.
$$

### 7. 向量与三角形

向量进入三角形后，最常见的翻译是：

1. 中点：$M$ 是 $AB$ 中点，则 $\overrightarrow{OM}=\dfrac{\overrightarrow{OA}+\overrightarrow{OB}}2$。
2. 重心：$G$ 是 $\triangle ABC$ 重心，则 $\overrightarrow{OG}=\dfrac{\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}}3$。
3. 共线：$A,B,C$ 共线等价于 $\overrightarrow{AB}=\lambda\overrightarrow{AC}$。
4. 垂直：$AB\perp AC$ 等价于 $\overrightarrow{AB}\cdot\overrightarrow{AC}=0$。
5. 角：$\angle BAC$ 由 $\overrightarrow{AB}$ 与 $\overrightarrow{AC}$ 的夹角决定。

## 方法识别

| 题目信号 | 优先方法 |
| --- | --- |
| 出现中点、重心、分点 | 用位置向量平均或基底表示 |
| 证明三点共线 | 写成 $\overrightarrow{AB}=\lambda\overrightarrow{AC}$ |
| 出现垂直、夹角、投影 | 用数量积 |
| 出现长度或最值 | 先平方，转成数量积或坐标二次式 |
| 图形中点很多 | 选基底，统一表示 |
| 坐标已给出 | 直接坐标化，不要硬画图 |

## 典型例题

### 例 1：中点向量

在 $\triangle ABC$ 中，$M$ 是 $BC$ 的中点。设 $\overrightarrow{AB}=\vec a,\overrightarrow{AC}=\vec b$，求 $\overrightarrow{AM}$。

:::solution 查看解析
从 $A$ 看，$B$ 的位置是 $\vec a$，$C$ 的位置是 $\vec b$。中点的位置向量取平均：

$$
\overrightarrow{AM}=\frac{\vec a+\vec b}{2}.
$$

这不是记忆公式，而是“中点坐标等于两个端点坐标平均”的向量版本。
:::

### 例 2：共线参数

已知 $\vec a=(2,3),\vec b=(4,t)$，若 $\vec a\parallel\vec b$，求 $t$。

:::solution 查看解析
共线等价于坐标行列式为 0：

$$
2t-3\cdot4=0.
$$

所以

$$
t=6.
$$
:::

### 例 3：数量积求夹角

已知 $\vec a=(1,2),\vec b=(2,1)$，求 $\vec a,\vec b$ 的夹角。

:::solution 查看解析

$$
\vec a\cdot\vec b=1\cdot2+2\cdot1=4,
$$

$$
|\vec a|=\sqrt5,\qquad |\vec b|=\sqrt5.
$$

所以

$$
\cos\theta=\frac4{5}.
$$

因此夹角为

$$
\theta=\arccos\frac45.
$$
:::

## 自我训练

学习平面向量时，学生每做一道题都要说出：

1. 我现在处理的是点、线段还是自由向量？
2. 我选的基底或坐标系是什么？
3. 哪些条件被翻译成了共线、垂直、长度或夹角？
4. 我的参数范围有没有漏？

## 费曼讲题任务

每次课后让学生准备 1 道向量题讲解，讲解必须包含：

1. 为什么想到用向量，而不是纯几何？
2. 选择基底或坐标的理由是什么？
3. 关键等式是哪一个？
4. 如果把中点改成三等分点、把垂直改成夹角，方法怎样变化？

专项练习入口：[平面向量专项练习](./02_plane_vectors_exercises_zh.md)。
