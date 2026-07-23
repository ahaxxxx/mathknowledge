# 立体几何与空间向量：图形题库

这一页按本地考点 22 到考点 28 重写整理。每道题先给题干图形；解析中的辅助线、坐标系和计算过程放在“查看解析”里。

## 使用方式

这页不是原题堆叠，而是精选训练页。建议先学完对应模块，再做同类题。

1. 学 [空间图形语言与基本公理](./01_space_language_axioms_zh.md) 后，先做读图、共面、异面判断。
2. 学 [空间平行](./02_parallel_relations_zh.md) 后，做 A 组空间平行。
3. 学 [空间垂直](./03_perpendicular_relations_zh.md) 后，做 B 组空间垂直。
4. 学 [体积、表面积与等体积法](./04_volume_surface_equivolume_zh.md) 后，做 C 组体积表面积。
5. 学 [空间角的几何法](./05_space_angles_geometric_zh.md) 后，做 D 组空间角。
6. 学 [空间向量求角](./07_spatial_vectors_angles_zh.md) 后，做 E 组向量求角。
7. 学 [空间向量求距离](./08_spatial_vectors_distances_zh.md) 后，做 F 组向量求距离。
8. 学 [外接球模型](./09_circumsphere_models_zh.md) 后，做 G 组外接球。

如果需要刷量，再进入 [考点 22-28 全量本地题库](./03_solid_geometry_local_full_exercises_zh.md)。全量题库保留原资料图像，适合课后抽题，不适合第一次建立体系时直接通刷。

返回讲义：[立体几何与空间向量：从图形到坐标](./01_solid_geometry_spatial_vectors_zh.md)。

## 本地资料题型地图

1. 考点 22 对应 A 组：空间平行。
2. 考点 23 对应 B 组：空间垂直。
3. 考点 24 对应 C 组：体积、表面积与等体积。
4. 考点 25 对应 D 组：几何法求空间角。
5. 考点 26 对应 E 组：空间向量求角。
6. 考点 27 对应 F 组：空间向量求距离。
7. 考点 28 对应 G 组：外接球模型。

## A. 空间平行

### 题 1：中位线证明线面平行

如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为平行四边形，$E$ 为 $PA$ 的中点。求证：$PC\parallel$ 平面 $BDE$。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="四棱锥中位线证明线面平行">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="125,220 305,220 395,155 215,155" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="125" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="305" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="395" y2="155" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="215" y2="155" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="305" y1="220" x2="215" y2="155" stroke="#0f766e" stroke-width="3"/>
  <circle cx="188" cy="145" r="5" fill="#dc2626"/>
  <text x="248" y="58" font-size="19">P</text><text x="105" y="242" font-size="19">A</text><text x="308" y="242" font-size="19">B</text><text x="402" y="158" font-size="19">C</text><text x="197" y="151" font-size="19">D</text><text x="172" y="140" font-size="19" fill="#dc2626">E</text>
</svg>
:::

:::solution 查看解析
连接 $AC,BD$，设交点为 $O$。因为 $ABCD$ 是平行四边形，所以 $O$ 是 $AC$ 的中点。

在 $\triangle PAC$ 中，$E$ 是 $PA$ 的中点，$O$ 是 $AC$ 的中点，所以

$$
EO\parallel PC.
$$

又因为 $E,O$ 都在平面 $BDE$ 内，所以 $EO\subset$ 平面 $BDE$。因此

$$
PC\parallel \text{平面 }BDE.
$$
:::

### 题 2：两中点构造平行

如图，在四棱锥 $S-ABCD$ 中，底面 $ABCD$ 为矩形，$O$ 是 $AC$ 的中点，$M$ 是 $SC$ 的中点。求证：$OM\parallel$ 平面 $SAB$。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="四棱锥两中点构造平行">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="120,225 320,225 400,165 200,165" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="120" y2="225" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="320" y2="225" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="400" y2="165" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="200" y2="165" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="120" y1="225" x2="400" y2="165" stroke="#64748b" stroke-width="2" stroke-dasharray="7 5"/>
  <circle cx="260" cy="195" r="5" fill="#dc2626"/>
  <circle cx="325" cy="118" r="5" fill="#dc2626"/>
  <line x1="260" y1="195" x2="325" y2="118" stroke="#dc2626" stroke-width="3"/>
  <text x="248" y="58" font-size="19">S</text><text x="100" y="247" font-size="19">A</text><text x="324" y="247" font-size="19">B</text><text x="408" y="168" font-size="19">C</text><text x="182" y="161" font-size="19">D</text><text x="245" y="215" font-size="19" fill="#dc2626">O</text><text x="333" y="115" font-size="19" fill="#dc2626">M</text>
</svg>
:::

:::solution 查看解析
在 $\triangle SAC$ 中，$O$ 是 $AC$ 的中点，$M$ 是 $SC$ 的中点，所以

$$
OM\parallel SA.
$$

而 $SA\subset$ 平面 $SAB$，且 $OM$ 不在平面 $SAB$ 内，所以

$$
OM\parallel \text{平面 }SAB.
$$
:::

### 题 3：棱柱中构造平行四边形

如图，在直三棱柱 $ABC-A_1B_1C_1$ 中，$D$ 是 $AB$ 的中点，$E$ 是 $A_1B_1$ 的中点。求证：$DE\parallel CC_1$。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="直三棱柱中点连线平行侧棱">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="135,225 315,225 225,155" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="135,105 315,105 225,35" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="135" y1="225" x2="135" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="315" y1="225" x2="315" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="225" y1="155" x2="225" y2="35" stroke="#253044" stroke-width="3"/>
  <circle cx="225" cy="225" r="5" fill="#dc2626"/>
  <circle cx="225" cy="105" r="5" fill="#dc2626"/>
  <line x1="225" y1="225" x2="225" y2="105" stroke="#dc2626" stroke-width="4"/>
  <text x="118" y="247" font-size="18">A</text><text x="318" y="247" font-size="18">B</text><text x="230" y="157" font-size="18">C</text><text x="105" y="105" font-size="18">A₁</text><text x="319" y="105" font-size="18">B₁</text><text x="230" y="35" font-size="18">C₁</text><text x="206" y="246" fill="#dc2626" font-size="18">D</text><text x="205" y="98" fill="#dc2626" font-size="18">E</text>
</svg>
:::

:::solution 查看解析
在三棱柱中，$AA_1\parallel BB_1\parallel CC_1$。

点 $D,E$ 分别是 $AB,A_1B_1$ 的中点。由于直三棱柱中 $AA_1\parallel BB_1\parallel CC_1$，而 $E$ 正是 $D$ 沿侧棱方向平移得到的点，所以

$$
DE\parallel AA_1.
$$

又 $AA_1\parallel CC_1$，所以

$$
DE\parallel CC_1.
$$
:::

## B. 空间垂直

### 题 4：线面垂直判定

如图，四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为矩形，且 $PA\perp AB,\ PA\perp AD$。求证：$PA\perp$ 平面 $ABCD$。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="线面垂直判定">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="125,225 325,225 405,165 205,165" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="225" x2="125" y2="75" stroke="#dc2626" stroke-width="4"/>
  <line x1="125" y1="75" x2="325" y2="225" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="75" x2="405" y2="165" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="75" x2="205" y2="165" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <path d="M125 205 L145 205 L145 225" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="115" y="67" font-size="19">P</text><text x="105" y="247" font-size="19">A</text><text x="330" y="247" font-size="19">B</text><text x="412" y="168" font-size="19">C</text><text x="187" y="161" font-size="19">D</text>
</svg>
:::

:::solution 查看解析
在矩形 $ABCD$ 中，$AB$ 与 $AD$ 是平面 $ABCD$ 内两条相交直线。

题设给出

$$
PA\perp AB,\qquad PA\perp AD.
$$

一条直线垂直于一个平面内两条相交直线，则这条直线垂直于该平面。因此

$$
PA\perp \text{平面 }ABCD.
$$
:::

### 题 5：由线面垂直推出线线垂直

如图，在直四棱柱 $ABCD-A_1B_1C_1D_1$ 中，底面 $ABCD$ 为矩形。求证：$AA_1\perp BD$。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="直四棱柱线面垂直性质">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="135,235 315,235 390,180 210,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="135,105 315,105 390,50 210,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="135" y1="235" x2="135" y2="105" stroke="#dc2626" stroke-width="4"/>
  <line x1="315" y1="235" x2="315" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="390" y1="180" x2="390" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="210" y1="180" x2="210" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="315" y1="235" x2="210" y2="180" stroke="#0f766e" stroke-width="4"/>
  <text x="118" y="258" font-size="18">A</text><text x="318" y="258" font-size="18">B</text><text x="397" y="183" font-size="18">C</text><text x="190" y="176" font-size="18">D</text><text x="107" y="103" font-size="18">A₁</text>
</svg>
:::

:::solution 查看解析
直四棱柱的侧棱垂直于底面，所以

$$
AA_1\perp \text{平面 }ABCD.
$$

而 $BD\subset$ 平面 $ABCD$，因此由线面垂直的性质得

$$
AA_1\perp BD.
$$
:::

### 题 6：面面垂直性质

如图，平面 $\alpha\perp$ 平面 $\beta$，交线为 $l$。直线 $a\subset\alpha$，且 $a\perp l$。求证：$a\perp\beta$。

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="面面垂直属性定理">
  <rect x="55" y="35" width="410" height="230" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="115,210 380,210 430,155 165,155" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="210,230 320,190 320,70 210,110" fill="#e0f2fe" stroke="#2563eb" stroke-width="3" opacity="0.75"/>
  <line x1="210" y1="210" x2="320" y2="190" stroke="#dc2626" stroke-width="4"/>
  <line x1="265" y1="200" x2="265" y2="95" stroke="#0f766e" stroke-width="4"/>
  <path d="M260 194 L275 191 L275 205" fill="none" stroke="#0f766e" stroke-width="2"/>
  <text x="342" y="220" font-size="18">β</text><text x="328" y="95" font-size="18">α</text><text x="223" y="229" font-size="18" fill="#dc2626">l</text><text x="274" y="117" font-size="18" fill="#0f766e">a</text>
</svg>
:::

:::solution 查看解析
这是面面垂直的常用性质定理：

如果两个平面互相垂直，那么在其中一个平面内，垂直于交线的直线，垂直于另一个平面。

已知 $\alpha\perp\beta$，交线为 $l$，且

$$
a\subset\alpha,\qquad a\perp l.
$$

因此

$$
a\perp \beta.
$$
:::

## C. 体积、表面积与等体积

### 题 7：四棱锥体积

如图，四棱锥 $P-ABCD$ 的底面 $ABCD$ 为矩形，$AB=4,AD=3$，$PA\perp$ 平面 $ABCD$，且 $PA=6$。求四棱锥体积。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="四棱锥体积">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="125,225 325,225 405,165 205,165" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="225" x2="125" y2="75" stroke="#dc2626" stroke-width="4"/>
  <line x1="125" y1="75" x2="325" y2="225" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="75" x2="405" y2="165" stroke="#253044" stroke-width="3"/>
  <line x1="125" y1="75" x2="205" y2="165" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <text x="112" y="67" font-size="19">P</text><text x="105" y="247" font-size="19">A</text><text x="330" y="247" font-size="19">B</text><text x="412" y="168" font-size="19">C</text><text x="187" y="161" font-size="19">D</text><text x="212" y="250" font-size="16">AB=4</text><text x="78" y="150" fill="#dc2626" font-size="16">PA=6</text>
</svg>
:::

:::solution 查看解析
底面积为

$$
S_{ABCD}=AB\cdot AD=4\cdot3=12.
$$

因为 $PA\perp$ 平面 $ABCD$，所以高为 $PA=6$。

四棱锥体积：

$$
V=\frac13 S_{ABCD}\cdot PA
=\frac13\cdot12\cdot6=24.
$$
:::

### 题 8：直三棱柱体积与表面积

如图，直三棱柱 $ABC-A_1B_1C_1$ 中，底面 $\triangle ABC$ 是直角三角形，$AB=3,AC=4,AA_1=5$。求体积。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="直三棱柱体积">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="135,225 315,225 135,145" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="135,105 315,105 135,25" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="135" y1="225" x2="135" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="315" y1="225" x2="315" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="135" y1="145" x2="135" y2="25" stroke="#253044" stroke-width="3"/>
  <path d="M135 205 L155 205 L155 225" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="118" y="247" font-size="18">A</text><text x="318" y="247" font-size="18">B</text><text x="116" y="142" font-size="18">C</text><text x="105" y="105" font-size="18">A₁</text><text x="205" y="250" font-size="16">3</text><text x="90" y="186" font-size="16">4</text><text x="145" y="170" font-size="16">高 5</text>
</svg>
:::

:::solution 查看解析
底面直角三角形面积为

$$
S_{\triangle ABC}=\frac12\cdot3\cdot4=6.
$$

直三棱柱的高为 $AA_1=5$，所以体积为

$$
V=S_{\triangle ABC}\cdot AA_1=6\cdot5=30.
$$
:::

### 题 9：等体积换顶点

如图，在三棱锥 $P-ABC$ 中，$D$ 为 $BC$ 的中点。若 $V_{P-ABC}=18$，求 $V_{P-ABD}$。

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="三棱锥等体积换底">
  <rect x="55" y="35" width="410" height="230" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="130,220 340,220 235,145" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="245" y1="65" x2="130" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="245" y1="65" x2="340" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="245" y1="65" x2="235" y2="145" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <circle cx="287" cy="183" r="5" fill="#dc2626"/>
  <line x1="245" y1="65" x2="287" y2="183" stroke="#dc2626" stroke-width="3"/>
  <text x="242" y="55" font-size="19">P</text><text x="112" y="242" font-size="19">B</text><text x="347" y="242" font-size="19">C</text><text x="218" y="142" font-size="19">A</text><text x="292" y="181" fill="#dc2626" font-size="19">D</text>
</svg>
:::

:::solution 查看解析
两个三棱锥 $P-ABC$ 与 $P-ABD$ 具有同一个顶点 $P$，底面都在平面 $ABC$ 内，所以相对于底面所在平面的高相同。

因为 $D$ 是 $BC$ 的中点，所以

$$
S_{\triangle ABD}=\frac12S_{\triangle ABC}.
$$

因此体积也为一半：

$$
V_{P-ABD}=\frac12V_{P-ABC}=9.
$$
:::

## D. 几何法求空间角

### 题 10：异面直线所成角

如图，正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$。求异面直线 $A_1B$ 与 $AC$ 所成角的余弦值。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="正方体异面直线所成角">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="145" y1="105" x2="285" y2="235" stroke="#dc2626" stroke-width="4"/>
  <line x1="145" y1="235" x2="360" y2="180" stroke="#0f766e" stroke-width="4"/>
  <text x="126" y="258" font-size="18">A</text><text x="290" y="258" font-size="18">B</text><text x="365" y="183" font-size="18">C</text><text x="116" y="103" font-size="18">A₁</text>
</svg>
:::

:::solution 查看解析
可以用平移法，也可以直接用坐标理解。设

$$
A(0,0,0),\quad B(2,0,0),\quad C(2,2,0),\quad A_1(0,0,2).
$$

则

$$
\overrightarrow{A_1B}=(2,0,-2),\qquad \overrightarrow{AC}=(2,2,0).
$$

所以

$$
\cos\theta
=\frac{|\overrightarrow{A_1B}\cdot\overrightarrow{AC}|}{|\overrightarrow{A_1B}||\overrightarrow{AC}|}
=\frac{4}{2\sqrt2\cdot2\sqrt2}
=\frac12.
$$
:::

### 题 11：线面角

如图，正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $1$。求直线 $A_1C$ 与平面 $ABCD$ 所成角的正弦值。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="正方体线面角">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="145" y1="105" x2="360" y2="180" stroke="#dc2626" stroke-width="4"/>
  <line x1="145" y1="235" x2="360" y2="180" stroke="#0f766e" stroke-width="3" stroke-dasharray="7 5"/>
  <text x="126" y="258" font-size="18">A</text><text x="365" y="183" font-size="18">C</text><text x="116" y="103" font-size="18">A₁</text>
</svg>
:::

:::solution 查看解析
直线 $A_1C$ 在底面 $ABCD$ 上的射影是 $AC$，所以线面角为 $\angle A_1CA$。

在直角三角形 $A_1AC$ 中，

$$
A_1A=1,\qquad A_1C=\sqrt3.
$$

因此

$$
\sin\theta=\frac{A_1A}{A_1C}=\frac1{\sqrt3}.
$$
:::

### 题 12：二面角

如图，正方体 $ABCD-A_1B_1C_1D_1$ 中，求平面 $ADD_1A_1$ 与平面 $ABCD$ 所成二面角。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="正方体相邻面二面角">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <polygon points="145,235 220,180 220,50 145,105" fill="#e0f2fe" stroke="#2563eb" stroke-width="3" opacity="0.75"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="220" y2="180" stroke="#dc2626" stroke-width="4"/>
  <text x="126" y="258" font-size="18">A</text><text x="205" y="177" font-size="18">D</text><text x="116" y="103" font-size="18">A₁</text><text x="226" y="50" font-size="18">D₁</text>
</svg>
:::

:::solution 查看解析
平面 $ADD_1A_1$ 是正方体的一个侧面，平面 $ABCD$ 是底面，两者沿 $AD$ 相交。

正方体中侧面垂直于底面，所以所成二面角为

$$
90^\circ.
$$
:::

## E. 空间向量求角

### 题 13：向量求异面直线夹角

在棱长为 $1$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，求直线 $A_1C$ 与 $B_1D$ 所成角的余弦值。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="空间向量求异面直线夹角">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="145" y1="105" x2="360" y2="180" stroke="#dc2626" stroke-width="4"/>
  <line x1="285" y1="105" x2="220" y2="180" stroke="#0f766e" stroke-width="4"/>
  <text x="116" y="103" font-size="18">A₁</text><text x="365" y="183" font-size="18">C</text><text x="290" y="103" font-size="18">B₁</text><text x="202" y="177" font-size="18">D</text>
</svg>
:::

:::solution 查看解析
建立坐标：

$$
A(0,0,0),\ B(1,0,0),\ C(1,1,0),\ D(0,1,0),\ A_1(0,0,1),\ B_1(1,0,1).
$$

则

$$
\overrightarrow{A_1C}=(1,1,-1),
$$

$$
\overrightarrow{B_1D}=(-1,1,-1).
$$

点积为

$$
\overrightarrow{A_1C}\cdot\overrightarrow{B_1D}
=-1+1+1=1.
$$

两个向量模长都是 $\sqrt3$，所以

$$
\cos\theta=\frac{|1|}{3}=\frac13.
$$
:::

### 题 14：向量求线面角

在棱长为 $1$ 的正方体中，求直线 $A_1C$ 与底面 $ABCD$ 所成角的正弦值。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="空间向量求线面角">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="145" y1="105" x2="360" y2="180" stroke="#dc2626" stroke-width="4"/>
  <text x="116" y="103" font-size="18">A₁</text><text x="365" y="183" font-size="18">C</text><text x="120" y="255" font-size="18">A</text>
</svg>
:::

:::solution 查看解析
底面 $ABCD$ 的法向量可取

$$
\vec n=(0,0,1).
$$

直线 $A_1C$ 的方向向量为

$$
\vec v=\overrightarrow{A_1C}=(1,1,-1).
$$

若线面角为 $\theta$，则

$$
\sin\theta=\frac{|\vec v\cdot\vec n|}{|\vec v||\vec n|}
=\frac{1}{\sqrt3}.
$$
:::

### 题 15：向量求二面角

已知平面 $\alpha$ 的法向量为 $\vec n_1=(1,0,0)$，平面 $\beta$ 的法向量为 $\vec n_2=(1,1,0)$。求两个平面所成锐二面角的余弦值。

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="法向量求二面角">
  <rect x="55" y="35" width="410" height="230" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="115,220 375,220 430,155 170,155" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="190,230 390,185 330,80 130,125" fill="#e0f2fe" stroke="#2563eb" stroke-width="3" opacity="0.7"/>
  <line x1="245" y1="185" x2="335" y2="185" stroke="#dc2626" stroke-width="4" marker-end="url(#arrow15a)"/>
  <line x1="245" y1="185" x2="315" y2="130" stroke="#16a34a" stroke-width="4" marker-end="url(#arrow15b)"/>
  <defs><marker id="arrow15a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#dc2626"/></marker><marker id="arrow15b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#16a34a"/></marker></defs>
  <text x="342" y="182" fill="#dc2626" font-size="16">n₁</text><text x="318" y="126" fill="#16a34a" font-size="16">n₂</text>
</svg>
:::

:::solution 查看解析
两个平面的夹角等于两个法向量夹角或其补角。锐二面角取余弦绝对值：

$$
\cos\theta=\frac{|\vec n_1\cdot\vec n_2|}{|\vec n_1||\vec n_2|}.
$$

计算：

$$
\vec n_1\cdot\vec n_2=1,\qquad |\vec n_1|=1,\qquad |\vec n_2|=\sqrt2.
$$

所以

$$
\cos\theta=\frac1{\sqrt2}.
$$
:::

## F. 空间向量求距离

### 题 16：点线距

在长方体 $ABCD-A_1B_1C_1D_1$ 中，$AB=2,BC=2,AA_1=2$。求点 $A$ 到直线 $B_1C$ 的距离。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="点到直线距离">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="235" x2="145" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="285" y1="105" x2="360" y2="180" stroke="#dc2626" stroke-width="4"/>
  <circle cx="145" cy="235" r="5" fill="#0f766e"/>
  <text x="126" y="258" font-size="18" fill="#0f766e">A</text><text x="290" y="103" font-size="18">B₁</text><text x="365" y="183" font-size="18">C</text>
</svg>
:::

:::solution 查看解析
设

$$
A(0,0,0),\quad B_1(2,0,2),\quad C(2,2,0).
$$

直线 $B_1C$ 的方向向量为

$$
\vec v=\overrightarrow{B_1C}=(0,2,-2).
$$

取

$$
\overrightarrow{B_1A}=(-2,0,-2).
$$

点到直线距离：

$$
d=\frac{|\overrightarrow{B_1A}\times \vec v|}{|\vec v|}.
$$

计算得

$$
|\overrightarrow{B_1A}\times \vec v|=4\sqrt3,\qquad |\vec v|=2\sqrt2.
$$

因此

$$
d=\sqrt6.
$$
:::

### 题 17：点面距

在棱长为 $1$ 的正方体中，求点 $A_1$ 到平面 $ABCD$ 的距离。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="点到平面距离">
  <rect x="55" y="35" width="410" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,235 285,235 360,180 220,180" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,105 285,105 360,50 220,50" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="105" x2="145" y2="235" stroke="#dc2626" stroke-width="4"/>
  <line x1="285" y1="235" x2="285" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="180" x2="360" y2="50" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="180" x2="220" y2="50" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <text x="116" y="103" font-size="18">A₁</text><text x="125" y="258" font-size="18">A</text>
</svg>
:::

:::solution 查看解析
正方体中

$$
AA_1\perp \text{平面 }ABCD.
$$

所以点 $A_1$ 到平面 $ABCD$ 的距离就是垂线段 $A_1A$ 的长度。

棱长为 $1$，因此距离为

$$
1.
$$
:::

### 题 18：用法向量求点面距

点 $P(1,2,3)$ 到平面

$$
x+y+z=0
$$

的距离是多少？

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="法向量求点面距">
  <rect x="55" y="35" width="410" height="230" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="120,220 390,220 440,150 170,150" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <circle cx="265" cy="80" r="6" fill="#dc2626"/>
  <line x1="265" y1="80" x2="285" y2="175" stroke="#dc2626" stroke-width="4" stroke-dasharray="7 5"/>
  <text x="273" y="78" font-size="18" fill="#dc2626">P</text>
</svg>
:::

:::solution 查看解析
平面 $x+y+z=0$ 的法向量为

$$
\vec n=(1,1,1).
$$

点面距公式：

$$
d=\frac{|1+2+3|}{\sqrt{1^2+1^2+1^2}}
=\frac6{\sqrt3}=2\sqrt3.
$$
:::

## G. 外接球模型

### 题 19：长方体模型

长方体的长、宽、高分别为 $2,3,6$。求其外接球半径和表面积。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="长方体外接球模型">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <ellipse cx="260" cy="155" rx="125" ry="110" fill="#e0f2fe" stroke="#0284c7" stroke-width="3" opacity="0.55"/>
  <polygon points="150,225 310,225 380,175 220,175" fill="none" stroke="#253044" stroke-width="3"/>
  <polygon points="150,105 310,105 380,55 220,55" fill="none" stroke="#253044" stroke-width="3"/>
  <line x1="150" y1="225" x2="150" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="310" y1="225" x2="310" y2="105" stroke="#253044" stroke-width="3"/>
  <line x1="380" y1="175" x2="380" y2="55" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="175" x2="220" y2="55" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
</svg>
:::

:::solution 查看解析
长方体外接球的直径等于体对角线：

$$
d=\sqrt{2^2+3^2+6^2}=\sqrt{49}=7.
$$

所以半径为

$$
R=\frac72.
$$

表面积：

$$
S=4\pi R^2=4\pi\cdot\frac{49}{4}=49\pi.
$$
:::

### 题 20：墙角模型

三棱锥 $P-ABC$ 中，$PA,PB,PC$ 两两垂直，且 $PA=2,PB=3,PC=6$。求该三棱锥外接球半径。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="墙角模型外接球">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <line x1="170" y1="230" x2="330" y2="230" stroke="#dc2626" stroke-width="4"/>
  <line x1="170" y1="230" x2="250" y2="165" stroke="#2563eb" stroke-width="4"/>
  <line x1="170" y1="230" x2="170" y2="85" stroke="#16a34a" stroke-width="4"/>
  <line x1="330" y1="230" x2="250" y2="165" stroke="#253044" stroke-width="3"/>
  <line x1="330" y1="230" x2="170" y2="85" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="165" x2="170" y2="85" stroke="#253044" stroke-width="3"/>
  <path d="M170 210 L190 210 L190 230" fill="none" stroke="#111827" stroke-width="2"/>
  <text x="151" y="252" font-size="18">P</text><text x="336" y="233" font-size="18">A</text><text x="254" y="162" font-size="18">B</text><text x="152" y="82" font-size="18">C</text><text x="225" y="252" font-size="16">2</text><text x="198" y="178" font-size="16">3</text><text x="142" y="155" font-size="16">6</text>
</svg>
:::

:::solution 查看解析
三条棱 $PA,PB,PC$ 两两垂直，可以把它补成长方体的一条体对角线模型。

外接球直径为

$$
\sqrt{PA^2+PB^2+PC^2}
=\sqrt{2^2+3^2+6^2}=7.
$$

所以外接球半径为

$$
R=\frac72.
$$
:::

### 题 21：正四面体外接球

正四面体 $ABCD$ 的棱长为 $2$。求其外接球表面积。已知正四面体外接球半径公式为 $R=\frac{\sqrt6}{4}a$。

:::diagram
<svg viewBox="0 0 520 310" role="img" aria-label="正四面体外接球">
  <rect x="55" y="35" width="410" height="240" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <ellipse cx="260" cy="155" rx="115" ry="110" fill="#e0f2fe" stroke="#0284c7" stroke-width="3" opacity="0.55"/>
  <polygon points="150,220 370,220 260,120" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="260" y1="55" x2="150" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="260" y1="55" x2="370" y2="220" stroke="#253044" stroke-width="3"/>
  <line x1="260" y1="55" x2="260" y2="120" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <circle cx="260" cy="150" r="5" fill="#dc2626"/>
  <text x="258" y="48" font-size="18">D</text><text x="132" y="240" font-size="18">A</text><text x="374" y="240" font-size="18">B</text><text x="263" y="121" font-size="18">C</text><text x="270" y="152" fill="#dc2626" font-size="16">O</text>
</svg>
:::

:::solution 查看解析
正四面体棱长 $a=2$，外接球半径为

$$
R=\frac{\sqrt6}{4}\cdot2=\frac{\sqrt6}{2}.
$$

表面积为

$$
S=4\pi R^2
=4\pi\cdot\frac{6}{4}
=6\pi.
$$
:::

## 使用建议

1. A、B 两组适合讲完平行垂直判定后立即布置，要求学生说出“关键辅助线”或“平面内两条相交直线”。
2. C 组适合体积课使用，重点训练“底面与高”的选择。
3. D、E 两组适合对比几何法和向量法，学生要能说明为什么换方法。
4. F、G 两组适合复习课或周日两小时课，题目计算量不大，但模型识别很关键。
