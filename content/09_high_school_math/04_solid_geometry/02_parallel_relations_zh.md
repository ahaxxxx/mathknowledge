# 空间平行：线线、线面、面面

空间平行题的核心是“把高维关系降到低维关系”。线面平行通常转化为线线平行，面面平行通常转化为两组相交直线分别平行。

## 线线平行

线线平行要求两件事同时成立：

1. 两条直线共面。
2. 两条直线没有公共点。

在证明中，最常用的来源是中位线、平行四边形、矩形、正方形、相似三角形。

## 线面平行

定义：直线 $l$ 与平面 $\alpha$ 没有公共点，则 $l\parallel \alpha$。

判定定理：如果 $l\not\subset\alpha$，且平面 $\alpha$ 内存在直线 $m$ 使 $l\parallel m$，那么 $l\parallel\alpha$。

性质定理：如果 $l\parallel\alpha$，过 $l$ 的平面 $\beta$ 与 $\alpha$ 相交于 $m$，那么 $l\parallel m$。

判定定理用于“证明线面平行”。性质定理用于“已知线面平行，推出线线平行”。

:::diagram
<svg viewBox="0 0 640 300" role="img" aria-label="线面平行的判定">
  <polygon points="90,210 420,210 520,125 190,125" fill="#f8f3ea" stroke="#d7c7aa" stroke-width="2"/>
  <line x1="155" y1="178" x2="390" y2="178" stroke="#0f766e" stroke-width="4"/>
  <line x1="130" y1="86" x2="365" y2="86" stroke="#dc2626" stroke-width="4"/>
  <text x="245" y="200" font-size="18" fill="#0f766e">m 在平面 α 内</text>
  <text x="220" y="70" font-size="18" fill="#dc2626">l ∥ m</text>
  <text x="430" y="230" font-size="18" fill="#1f2937">所以 l ∥ α</text>
</svg>
:::

## 面面平行

定义：两个平面没有公共点，则它们平行。

判定定理：如果一个平面内两条相交直线分别平行于另一个平面内的两条直线，那么这两个平面平行。

常用形式：在平面 $\alpha$ 内找两条相交直线 $a,b$，证明 $a\parallel\beta$ 且 $b\parallel\beta$，即可推出 $\alpha\parallel\beta$。

性质定理：如果两个平行平面被第三个平面所截，那么所得交线平行。

## 证明链模板

证明线面平行：

1. 先说明目标直线不在目标平面内。
2. 在目标平面内找一条直线。
3. 证明这两条直线平行。
4. 用线面平行判定。

证明面面平行：

1. 在第一个平面内找两条相交直线。
2. 分别证明它们平行于第二个平面。
3. 用面面平行判定。

## 常见入口

1. 中点给中位线。
2. 平行四边形给对边平行。
3. 正方体和长方体给对应棱平行。
4. 截面题常用“第三平面截平行平面，交线平行”。

## 训练题

1. 在三棱锥 $P-ABC$ 中，$D,E$ 分别为 $PA,PB$ 的中点，证明 $DE\parallel$ 平面 $ABC$。

:::solution 查看解析
在三角形 $PAB$ 中，$D,E$ 为两边中点，所以 $DE\parallel AB$。又 $AB\subset$ 平面 $ABC$，且 $DE\not\subset$ 平面 $ABC$，因此 $DE\parallel$ 平面 $ABC$。
:::

2. 在正方体 $ABCD-A_1B_1C_1D_1$ 中，证明 $A_1B_1\parallel$ 平面 $ABCD$。

:::solution 查看解析
$A_1B_1\parallel AB$，且 $AB\subset$ 平面 $ABCD$，$A_1B_1$ 不在平面 $ABCD$ 内，所以 $A_1B_1\parallel$ 平面 $ABCD$。
:::

3. 在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为平行四边形。证明 $AB\parallel$ 平面 $PCD$。

:::solution 查看解析
因为 $ABCD$ 是平行四边形，所以 $AB\parallel CD$。又 $CD\subset$ 平面 $PCD$，$AB\not\subset$ 平面 $PCD$，所以 $AB\parallel$ 平面 $PCD$。
:::

4. 在三棱柱 $ABC-A_1B_1C_1$ 中，证明平面 $ABC\parallel$ 平面 $A_1B_1C_1$。

:::solution 查看解析
棱柱对应棱平行，有 $AB\parallel A_1B_1$，$AC\parallel A_1C_1$。又 $AB,AC$ 相交于 $A$，所以平面 $ABC\parallel$ 平面 $A_1B_1C_1$。
:::

5. 已知平面 $\alpha\parallel\beta$，平面 $\gamma$ 与它们分别交于 $a,b$，证明 $a\parallel b$。

:::solution 查看解析
这是平行平面的性质定理：两个平行平面被第三个平面所截，所得交线平行。
:::

## 讲题追问

让学生每次证明线面平行时都补一句：我在目标平面内找到了哪一条“替身直线”？如果说不出来，说明证明链还没有闭合。
