# 立体几何与空间向量：从图形到坐标

这一页用于上课讲解主线：先让学生看懂空间图形，再决定用几何法还是空间向量法。立体几何的图一定要画出来，因为很多条件不是文字本身，而是点、线、面之间的位置关系。

返回专题首页：[立体几何与空间向量](./README.md)。配套练习：[立体几何与空间向量：图形题库](./02_solid_geometry_exercises_zh.md)。

## 本地资料梳理

本地 2021 高考一轮复习资料中，立体几何与空间向量覆盖七类考点：

1. 考点 22：空间几何平行问题，常见方法有平行传递、中位线、构造平行四边形、线面平行判定。
2. 考点 23：空间几何垂直问题，常见方法有线面垂直判定、面面垂直判定、面面垂直性质、折叠中的垂直保持。
3. 考点 24：空间几何体体积及表面积，常见方法有直接公式、等体积法、换顶点、点面距。
4. 考点 25：几何法解空间角，常见对象是异面直线所成角、线面角、二面角。
5. 考点 26：空间向量求空间角，常见方法是建立坐标系、求方向向量、求平面法向量。
6. 考点 27：空间向量求空间距离，常见对象是两点距、点线距、点面距。
7. 考点 28：空间几何体外接球，常见模型有长方体模型、墙角模型、汉堡模型、正棱锥模型。

## 方法地图

1. **证明平行**：优先找中点、中位线、平行四边形、已知平行线；目标是转化为“线线平行”，再推出线面平行。
2. **证明垂直**：优先找“垂直于平面内两条相交直线”；如果题目给面面垂直，常用性质是“一个平面内垂直交线的直线垂直另一个平面”。
3. **求体积**：先确定底面和高；如果高不好找，换顶点或换底面，用等体积法。
4. **求空间角**：几何法要先把角搬到同一个平面内；向量法要先确定方向向量或法向量。
5. **求距离**：点线距看投影，点面距看法向量，异面线距离看公垂线或向量混合积。
6. **求外接球**：先识别模型。长方体模型看体对角线，墙角模型看三条两两垂直棱，正棱锥模型看底面外心和高。

## 图形语言

立体几何的第一步不是计算，而是把条件翻译到图上：

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="四棱锥图形语言示意">
  <rect x="60" y="40" width="400" height="220" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="130,210 310,210 390,155 210,155" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="130" y2="210" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="310" y2="210" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="390" y2="155" stroke="#253044" stroke-width="3"/>
  <line x1="250" y1="70" x2="210" y2="155" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="130" y1="210" x2="390" y2="155" stroke="#0f766e" stroke-width="2" stroke-dasharray="7 5"/>
  <line x1="210" y1="155" x2="310" y2="210" stroke="#0f766e" stroke-width="2" stroke-dasharray="7 5"/>
  <text x="245" y="58" font-size="20" fill="#111827">P</text>
  <text x="112" y="232" font-size="20" fill="#111827">A</text>
  <text x="312" y="235" font-size="20" fill="#111827">B</text>
  <text x="397" y="158" font-size="20" fill="#111827">C</text>
  <text x="190" y="151" font-size="20" fill="#111827">D</text>
  <text x="136" y="86" font-size="16" fill="#0f766e">先看点、线、面位置，再决定辅助线</text>
</svg>
:::

看图时要问：

1. 哪些点共面？
2. 哪些线可能平行或垂直？
3. 哪些点是中点、重心、外心或垂足？
4. 哪条线是高？哪个面能当底面？

## 空间向量语言

空间向量法的核心是把图形放进坐标系。最常用的建系场景是：正方体、长方体、直棱柱、底面为矩形或直角三角形的棱锥。

:::diagram
<svg viewBox="0 0 520 320" role="img" aria-label="正方体空间坐标系示意">
  <rect x="50" y="35" width="420" height="250" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <polygon points="145,215 285,215 360,160 220,160" fill="#eef3e8" stroke="#253044" stroke-width="3"/>
  <polygon points="145,95 285,95 360,40 220,40" fill="#f8fafc" stroke="#253044" stroke-width="3"/>
  <line x1="145" y1="215" x2="145" y2="95" stroke="#253044" stroke-width="3"/>
  <line x1="285" y1="215" x2="285" y2="95" stroke="#253044" stroke-width="3"/>
  <line x1="360" y1="160" x2="360" y2="40" stroke="#253044" stroke-width="3"/>
  <line x1="220" y1="160" x2="220" y2="40" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="145" y1="215" x2="285" y2="215" stroke="#dc2626" stroke-width="4"/>
  <line x1="145" y1="215" x2="220" y2="160" stroke="#2563eb" stroke-width="4"/>
  <line x1="145" y1="215" x2="145" y2="95" stroke="#16a34a" stroke-width="4"/>
  <text x="126" y="238" font-size="20">O</text>
  <text x="292" y="222" font-size="18" fill="#dc2626">x</text>
  <text x="222" y="153" font-size="18" fill="#2563eb">y</text>
  <text x="125" y="92" font-size="18" fill="#16a34a">z</text>
  <text x="85" y="280" font-size="16" fill="#475569">正交三方向清楚时，空间向量法最稳</text>
</svg>
:::

常用公式：

1. 两点距：

$$
AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.
$$

2. 线线角：

$$
\cos\theta=\frac{|\vec u\cdot\vec v|}{|\vec u||\vec v|}.
$$

3. 线面角。若直线方向向量为 $\vec v$，平面法向量为 $\vec n$，直线与平面所成角为 $\theta$，则

$$
\sin\theta=\frac{|\vec v\cdot\vec n|}{|\vec v||\vec n|}.
$$

4. 点面距。若平面法向量为 $\vec n$，点 $P$ 到平面上一点 $A$ 的向量为 $\overrightarrow{AP}$，则

$$
d=\frac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}.
$$

## 外接球模型

外接球题不是每次都重新找球心，而是先识别模型：

1. 长方体模型：外接球直径等于体对角线。
2. 墙角模型：三条两两垂直的棱可以补成长方体。
3. 汉堡模型：上下两个平面中的圆心上下对齐，球心在两圆心连线上。
4. 正棱锥模型：球心在高线上，由底面外接圆半径和高建立方程。

:::diagram
<svg viewBox="0 0 520 300" role="img" aria-label="长方体外接球模型示意">
  <rect x="60" y="35" width="400" height="230" fill="#fffaf0" stroke="#d8c8a5" rx="10"/>
  <ellipse cx="260" cy="150" rx="126" ry="112" fill="#e0f2fe" stroke="#0284c7" stroke-width="3" opacity="0.55"/>
  <polygon points="150,210 310,210 375,160 215,160" fill="none" stroke="#253044" stroke-width="3"/>
  <polygon points="150,90 310,90 375,40 215,40" fill="none" stroke="#253044" stroke-width="3"/>
  <line x1="150" y1="210" x2="150" y2="90" stroke="#253044" stroke-width="3"/>
  <line x1="310" y1="210" x2="310" y2="90" stroke="#253044" stroke-width="3"/>
  <line x1="375" y1="160" x2="375" y2="40" stroke="#253044" stroke-width="3"/>
  <line x1="215" y1="160" x2="215" y2="40" stroke="#253044" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="150" y1="210" x2="375" y2="40" stroke="#dc2626" stroke-width="4"/>
  <circle cx="262" cy="125" r="5" fill="#dc2626"/>
  <text x="176" y="246" font-size="16" fill="#dc2626">体对角线 = 外接球直径</text>
</svg>
:::

## 费曼讲题任务

学生讲立体几何题时，必须说清楚：

1. 题干图是什么模型？
2. 要证明或计算的对象是什么？
3. 几何法的关键辅助线在哪里？
4. 向量法的坐标系怎么选，法向量怎么求？
5. 结果有没有回到几何意义上解释？

配套练习入口：[立体几何与空间向量：图形题库](./02_solid_geometry_exercises_zh.md)。
