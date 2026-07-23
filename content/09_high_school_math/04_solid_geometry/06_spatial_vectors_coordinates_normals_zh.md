# 空间向量：建系、坐标与法向量

空间向量的意义不是逃避图形，而是把图形关系变成稳定计算。平行变成向量共线，垂直变成内积为 0，平面变成法向量，角和距离变成公式。

## 坐标系怎么建

好的坐标系有三个标准：

1. 原点放在垂直关系最多、边长最明确的点。
2. 坐标轴沿互相垂直的边或高来取。
3. 尽量让更多点的坐标出现 $0$。

正方体、长方体、直棱柱通常最适合直接沿三条棱建系。正棱锥常把底面中心作为原点，把底面放在 $xOy$ 平面，把高放在 $z$ 轴上。

:::diagram
<svg viewBox="0 0 640 330" role="img" aria-label="长方体建系示意图">
  <line x1="140" y1="250" x2="360" y2="250" stroke="#1f2937" stroke-width="3"/>
  <line x1="140" y1="250" x2="140" y2="80" stroke="#1f2937" stroke-width="3"/>
  <line x1="140" y1="250" x2="260" y2="170" stroke="#1f2937" stroke-width="3"/>
  <line x1="360" y1="250" x2="480" y2="170" stroke="#1f2937" stroke-width="3"/>
  <line x1="260" y1="170" x2="480" y2="170" stroke="#1f2937" stroke-width="3"/>
  <line x1="140" y1="80" x2="260" y2="0" stroke="#1f2937" stroke-width="3"/>
  <line x1="260" y1="0" x2="480" y2="0" stroke="#1f2937" stroke-width="3"/>
  <line x1="480" y1="0" x2="480" y2="170" stroke="#1f2937" stroke-width="3"/>
  <line x1="260" y1="0" x2="260" y2="170" stroke="#1f2937" stroke-width="3"/>
  <line x1="140" y1="250" x2="420" y2="250" stroke="#dc2626" stroke-width="4"/>
  <line x1="140" y1="250" x2="140" y2="45" stroke="#0f766e" stroke-width="4"/>
  <line x1="140" y1="250" x2="290" y2="150" stroke="#2563eb" stroke-width="4"/>
  <text x="424" y="255" font-size="18" fill="#dc2626">x</text>
  <text x="122" y="42" font-size="18" fill="#0f766e">z</text>
  <text x="296" y="150" font-size="18" fill="#2563eb">y</text>
  <text x="118" y="273" font-size="18">O</text>
</svg>
:::

## 向量基本运算

若 $A(x_1,y_1,z_1)$，$B(x_2,y_2,z_2)$，则

$$
\overrightarrow{AB}=(x_2-x_1,\ y_2-y_1,\ z_2-z_1).
$$

内积：

$$
\mathbf a\cdot\mathbf b=x_1x_2+y_1y_2+z_1z_2.
$$

模长：

$$
|\mathbf a|=\sqrt{x^2+y^2+z^2}.
$$

垂直判定：

$$
\mathbf a\perp\mathbf b\quad\Longleftrightarrow\quad \mathbf a\cdot\mathbf b=0.
$$

平行判定：

$$
\mathbf a\parallel\mathbf b\quad\Longleftrightarrow\quad \mathbf a=\lambda\mathbf b.
$$

## 平面与法向量

一个向量 $\mathbf n$ 如果垂直于平面 $\alpha$ 内的两条相交直线，就叫平面 $\alpha$ 的法向量。

求法向量的基本方法：

1. 在平面内取两条不平行向量 $\mathbf u,\mathbf v$。
2. 设法向量 $\mathbf n=(x,y,z)$。
3. 列方程

$$
\mathbf n\cdot\mathbf u=0,\qquad \mathbf n\cdot\mathbf v=0.
$$

4. 解出一个非零向量即可。法向量不唯一，成比例都可以。

## 建系题流程

1. 先写出所有关键点坐标。
2. 再写方向向量。
3. 如果涉及平面，求法向量。
4. 最后根据目标选择角公式或距离公式。

## 训练题

1. 已知 $A(1,2,3)$，$B(4,0,5)$，求 $\overrightarrow{AB}$。

:::solution 查看解析
$$
\overrightarrow{AB}=(4-1,\ 0-2,\ 5-3)=(3,-2,2).
$$
:::

2. 判断 $\mathbf a=(1,2,-1)$ 与 $\mathbf b=(2,-1,0)$ 是否垂直。

:::solution 查看解析
$$
\mathbf a\cdot\mathbf b=1\cdot2+2\cdot(-1)+(-1)\cdot0=0.
$$
所以二者垂直。
:::

3. 判断 $\mathbf a=(2,-4,6)$ 与 $\mathbf b=(-1,2,-3)$ 是否平行。

:::solution 查看解析
$\mathbf a=-2\mathbf b$，所以二者平行。
:::

4. 平面内有向量 $\mathbf u=(1,0,1)$，$\mathbf v=(0,1,1)$，设法向量 $\mathbf n=(x,y,z)$，写出求 $\mathbf n$ 的方程。

:::solution 查看解析
由法向量垂直平面内两条方向向量，得
$$
x+z=0,\qquad y+z=0.
$$
可取 $z=1$，得到 $\mathbf n=(-1,-1,1)$。
:::

5. 正方体棱长为 $1$，以 $A$ 为原点，$AB,AD,AA_1$ 分别为 $x,y,z$ 轴，写出 $C_1$ 的坐标。

:::solution 查看解析
$C_1$ 从 $A$ 出发沿 $AB,AD,AA_1$ 各走 $1$，所以坐标为 $(1,1,1)$。
:::

## 讲题追问

建系后让学生解释：为什么这个坐标系让点的坐标最简单？如果坐标系只是随便建的，后面计算会越来越重。
