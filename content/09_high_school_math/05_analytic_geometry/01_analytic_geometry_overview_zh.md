# 解析几何：从坐标到曲线

解析几何研究的是“图形与方程之间的翻译”。几何里看见点、线、圆和圆锥曲线；代数里写成坐标、方程、参数和不等式。高考解析几何大题的本质，就是在这两种语言之间来回切换。

## 一句话主线

解析几何不是背曲线公式，而是用方程控制图形。

1. 点：用坐标表示位置。
2. 直线：用一次方程表示方向和位置。
3. 圆：用到定点距离相等表示。
4. 圆锥曲线：用动点满足的距离关系表示轨迹。
5. 交点：用联立方程表示。
6. 弦长、面积、角度、最值：用代数式表达后化简。

## 知识树

1. 坐标基础：距离、中点、斜率、向量。
2. 直线：方程形式、平行垂直、交点、距离。
3. 圆：标准方程、一般方程、切线、弦长、圆与圆。
4. 椭圆：到两定点距离和为常数。
5. 双曲线：到两定点距离差的绝对值为常数。
6. 抛物线：到焦点距离等于到准线距离。
7. 直线与曲线联立：判别式、韦达、弦长、中点弦。
8. 三定问题：定点、定值、定直线。
9. 最值范围：判别式、函数法、参数法、几何法。

:::diagram
<svg viewBox="0 0 820 260" role="img" aria-label="解析几何知识路线图">
  <rect x="35" y="95" width="120" height="70" rx="8" fill="#f8f3ea" stroke="#d7c7aa"/>
  <rect x="205" y="45" width="120" height="70" rx="8" fill="#eef7f4" stroke="#8ab7ad"/>
  <rect x="205" y="145" width="120" height="70" rx="8" fill="#eef7f4" stroke="#8ab7ad"/>
  <rect x="375" y="45" width="140" height="70" rx="8" fill="#fff7ed" stroke="#e0b36a"/>
  <rect x="375" y="145" width="140" height="70" rx="8" fill="#fff7ed" stroke="#e0b36a"/>
  <rect x="565" y="45" width="120" height="70" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
  <rect x="565" y="145" width="120" height="70" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="75" y="136" font-size="18">坐标语言</text>
  <text x="240" y="86" font-size="18">直线</text>
  <text x="252" y="186" font-size="18">圆</text>
  <text x="410" y="86" font-size="18">圆锥曲线</text>
  <text x="400" y="186" font-size="18">联立与韦达</text>
  <text x="593" y="86" font-size="18">三定</text>
  <text x="592" y="186" font-size="18">最值</text>
  <line x1="155" y1="130" x2="205" y2="80" stroke="#64748b" stroke-width="3"/>
  <line x1="155" y1="130" x2="205" y2="180" stroke="#64748b" stroke-width="3"/>
  <line x1="325" y1="80" x2="375" y2="80" stroke="#64748b" stroke-width="3"/>
  <line x1="325" y1="180" x2="375" y2="180" stroke="#64748b" stroke-width="3"/>
  <line x1="515" y1="80" x2="565" y2="80" stroke="#64748b" stroke-width="3"/>
  <line x1="515" y1="180" x2="565" y2="180" stroke="#64748b" stroke-width="3"/>
</svg>
:::

## 高考大题的稳定流程

1. 明确曲线方程和参数范围。
2. 设直线，注意斜率不存在是否需要单独处理。
3. 联立直线和曲线，得到一元二次方程。
4. 写出判别式 $\Delta>0$、根和、根积。
5. 把题目目标转成 $x_1+x_2$、$x_1x_2$ 或 $y_1+y_2$、$y_1y_2$。
6. 化简，观察是否出现定值、定点、范围或最值。
7. 回到几何意义，检查特殊情况。

## 常见失分点

1. 设直线时漏掉斜率不存在的情况。
2. 联立后忘记判别式条件。
3. 用了韦达，却没有说明两个交点确实存在。
4. 弦长公式中把 $x$ 差和 $y$ 差混乱。
5. 定点定值题没有完成“任意参数都成立”的证明。
6. 最值题只求出代数最值，没有检查参数范围。

## 费曼讲题任务

学生讲解析几何题时，必须先讲“我为什么这样设”。如果她只会说“答案这么做”，说明还没有控制题目。建议每题用下面模板：

1. 这题的曲线是：
2. 我设直线为：
3. 联立后保留的核心量是：
4. 题目目标可以转成：
5. 最后需要检查：

## 模块入口

1. [坐标、距离、斜率与直线基础](./02_coordinates_lines_zh.md)
2. [圆的方程与直线圆问题](./03_circle_equations_zh.md)
3. [圆锥曲线统一入口](./04_conic_unified_zh.md)
4. [椭圆](./05_ellipse_zh.md)
5. [双曲线](./06_hyperbola_zh.md)
6. [抛物线](./07_parabola_zh.md)
7. [直线与圆锥曲线的代数引擎](./08_line_conic_engine_zh.md)
8. [定点、定值、定直线](./09_three_constants_zh.md)
9. [最值与范围](./10_extreme_range_zh.md)
10. [圆锥曲线大题十个大招](./11_conic_big_problem_strategies_zh.md)

## 题库入口

1. [模块分层训练题库](./12_analytic_geometry_module_drills_zh.md)
2. [考点 40-46 全量本地题库](./13_analytic_geometry_local_full_exercises_zh.md)
