# 空间垂直：线线、线面、面面

空间垂直比空间平行更容易出错，因为“看起来垂直”不可靠。垂直证明必须说明垂直发生在哪里，是线线垂直、线面垂直，还是面面垂直。

## 线线垂直

两条相交直线所成角为 $90^\circ$，称为垂直。两条异面直线也可以定义所成角；若它们平移到同一点后的夹角为 $90^\circ$，也说这两条异面直线互相垂直。

在高中证明中，线线垂直常来自：

1. 正方形、矩形、直角三角形。
2. 勾股定理或勾股逆定理。
3. 线面垂直的性质。
4. 面面垂直的性质。

## 线面垂直

定义：如果直线 $l$ 垂直于平面 $\alpha$ 内经过垂足的任意一条直线，则 $l\perp\alpha$。

判定定理：如果直线 $l$ 垂直于平面 $\alpha$ 内两条相交直线，那么 $l\perp\alpha$。

性质定理：如果 $l\perp\alpha$，那么 $l$ 垂直于平面 $\alpha$ 内任意一条过垂足的直线。实际做题时，常用来推出线线垂直。

:::diagram
<svg viewBox="0 0 640 300" role="img" aria-label="线面垂直判定示意图">
  <polygon points="110,220 430,220 535,140 215,140" fill="#f8f3ea" stroke="#d7c7aa" stroke-width="2"/>
  <line x1="320" y1="180" x2="320" y2="60" stroke="#dc2626" stroke-width="5"/>
  <line x1="205" y1="180" x2="435" y2="180" stroke="#0f766e" stroke-width="4"/>
  <line x1="260" y1="215" x2="380" y2="145" stroke="#0f766e" stroke-width="4"/>
  <circle cx="320" cy="180" r="5" fill="#1f2937"/>
  <text x="330" y="75" font-size="18" fill="#dc2626">l</text>
  <text x="410" y="200" font-size="18" fill="#0f766e">a</text>
  <text x="382" y="145" font-size="18" fill="#0f766e">b</text>
  <text x="170" y="260" font-size="18" fill="#1f2937">l 垂直平面内两条相交直线 ⇒ l ⟂ 平面</text>
</svg>
:::

## 面面垂直

定义：两个平面相交，若它们所成的二面角是直二面角，则两个平面垂直。

判定定理：如果一个平面内有一条直线垂直于另一个平面，那么这两个平面垂直。

性质定理：若 $\alpha\perp\beta$，交线为 $l$，在 $\alpha$ 内作直线 $m\perp l$，则 $m\perp\beta$。

这个性质很重要，因为它把面面垂直转化为线面垂直。

## 证明链模板

证明线面垂直：

1. 在目标平面内找两条相交直线。
2. 证明目标直线分别垂直这两条直线。
3. 用线面垂直判定。

证明面面垂直：

1. 在一个平面内找一条直线。
2. 证明这条直线垂直另一个平面。
3. 用面面垂直判定。

从面面垂直推出线面垂直：

1. 找两个平面的交线。
2. 在其中一个平面内作一条垂直交线的直线。
3. 得到这条直线垂直另一个平面。

## 训练题

1. 在三棱锥 $P-ABC$ 中，若 $PA\perp AB$，$PA\perp AC$，且 $AB,AC$ 相交，证明 $PA\perp$ 平面 $ABC$。

:::solution 查看解析
$AB,AC$ 都在平面 $ABC$ 内，且相交于 $A$。直线 $PA$ 同时垂直 $AB,AC$，所以由线面垂直判定，$PA\perp$ 平面 $ABC$。
:::

2. 若 $PA\perp$ 平面 $ABC$，证明 $PA\perp BC$。

:::solution 查看解析
因为 $BC\subset$ 平面 $ABC$，而 $PA\perp$ 平面 $ABC$，所以 $PA$ 垂直于平面 $ABC$ 内任意直线，特别地 $PA\perp BC$。
:::

3. 已知平面 $\alpha\perp\beta$，交线为 $l$。若 $m\subset\alpha$ 且 $m\perp l$，证明 $m\perp\beta$。

:::solution 查看解析
这是面面垂直的性质定理：两个垂直平面中，在一个平面内垂直交线的直线，垂直于另一个平面。
:::

4. 在正方体 $ABCD-A_1B_1C_1D_1$ 中，证明 $AA_1\perp$ 平面 $ABCD$。

:::solution 查看解析
$AA_1\perp AB$，$AA_1\perp AD$，且 $AB,AD$ 是平面 $ABCD$ 内两条相交直线，所以 $AA_1\perp$ 平面 $ABCD$。
:::

5. 已知 $l\perp\alpha$，且 $m\parallel l$。证明 $m\perp\alpha$。

:::solution 查看解析
取平面 $\alpha$ 内过垂足的两条相交直线 $a,b$。由 $l\perp\alpha$ 得 $l\perp a$，$l\perp b$。又 $m\parallel l$，所以 $m\perp a$，$m\perp b$，因此 $m\perp\alpha$。
:::

## 讲题追问

让学生说清楚：我现在要证明的是线线垂直、线面垂直，还是面面垂直？如果对象说不清，后面的定理就一定会乱。
