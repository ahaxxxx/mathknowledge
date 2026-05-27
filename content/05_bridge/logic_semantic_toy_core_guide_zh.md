# Logic-Net 与 Semantic Loss toy 代码核心观看材料

## 0. 今晚的目标

今晚不需要把所有论文和所有代码一次看完。

今晚真正要做到的是：

1. 你能说清 `Logic-Net` 和 `Semantic Loss` 各自把知识接进模型的哪一环。
2. 你能找到 toy 代码里最关键的 2 个文件，而不是在整个目录里漫游。
3. 你能用自己的话解释：
   - `Logic-Net` 为什么会先出现 `teacher`
   - `Semantic Loss` 为什么不需要 `teacher`
   - 无标签样本在两种方法里分别是怎么发挥作用的

如果今晚结束时，你已经能把上面三件事讲顺，这次阅读就是有效的。

---

## 1. 先记住两条主链

### 1.1 Logic-Net

`rule -> rule distribution -> teacher distribution -> KL distillation -> student parameters`

更具体一点：

- 规则先被变成一个“偏向哪一类”的软分布
- 这个规则分布再和当前 student 的输出合成一个 `teacher`
- student 不直接优化“规则真假”，而是去模仿这个 `teacher`

你今晚看 `Logic-Net` 时，脑子里只要一直盯住一句话：

> 它不是直接把规则写成最终 loss，而是先改目标分布，再让参数去追这个被规则修正过的目标。

### 1.2 Semantic Loss

`constraint -> valid assignments -> satisfaction mass -> semantic loss -> parameters`

更具体一点：

- 先定义哪些输出赋值是合法的
- 再计算当前模型到底给这些合法赋值分了多少总概率质量
- 最后直接把这个总质量变成 loss

你今晚看 `Semantic Loss` 时，只要一直盯住一句话：

> 它不造 teacher，它直接问“当前输出分布有多少概率落在合法世界里”。

---

## 2. 今晚最推荐的阅读顺序

先不要从 `run.py` 开始，也不要先盯画图代码。

最稳的顺序是：

1. `repro/01_logic_net_toy/README.md`
2. `repro/01_logic_net_toy/rules.py`
3. `repro/01_logic_net_toy/trainer.py`
4. `repro/03_semantic_loss_toy/README.md`
5. `repro/03_semantic_loss_toy/constraints.py`
6. `repro/03_semantic_loss_toy/trainer.py`

如果你还有精力，再往下补：

7. `research_activation_system/notes/logic_net_notes_zh.md`
8. `research_activation_system/notes/semantic_loss_notes_zh.md`
9. `repro/01_logic_net_toy/logic_net_toy_代码逐行解析.md`
10. `repro/03_semantic_loss_toy/semantic_loss_toy_代码逐行解析.md`

今晚的原则是：

- 先看“知识进入模型的核心接口”
- 再看“训练循环里怎么真正用起来”
- 最后才看更长的逐行解析

---

## 3. Logic-Net toy：严格总览

这一节的目标不是展开所有细节，而是先给出一条严格、闭合的推导主线。你应该先在这里获得“结构正确的总图”，再进入第 10 节看完整细推导。

> 注释：第 3 节像“定理摘要版”，第 10 节像“完整证明版”。

### 3.1 主战场与对象

本节只盯两个文件：

- `repro/01_logic_net_toy/rules.py`
- `repro/01_logic_net_toy/trainer.py`

其余文件如 `data.py`、`model.py`、`experiment.py` 暂时只当背景。

在这个 toy 里，我们只关心下面三个对象：

- 输入 $x \in \mathbb{R}^2$
- student 分布 $p_\theta(\cdot \mid x)$
- 规则集合 $\mathcal{R}$

整个问题的核心不是“模型结构有多复杂”，而是：

$$
\mathcal{R}
\longrightarrow
q_{\mathcal{R}}(\cdot \mid x)
\longrightarrow
t_\theta(\cdot \mid x)
\longrightarrow
\mathcal{L}_{\mathrm{distill}}.
$$

> 注释：你只要先抓住“rule distribution -> teacher -> distillation”这条链，后面的细节就有地方安放。

### 3.2 `rules.py` 的严格角色

`rules.py` 负责把自然语言式规则变成可参与训练的概率对象。

更精确地说，它完成下面四步。

#### 3.2.1 定义：单条规则

一条规则写成：

$$
r = (a_r, b_r, c_r, \kappa_r, w_r, \alpha_r),
$$

其中：

- $(a_r,b_r,c_r)$ 决定线性边界
- $\kappa_r$ 决定正侧支持哪个类别
- $w_r$ 决定规则聚合时的话语权
- $\alpha_r$ 决定该规则相对全局温度的软硬程度

这正对应 `RuleSpec`。

> 注释：`RuleSpec` 是“规则的数学最小封装”。

#### 3.2.2 定义：margin 与边界

单条规则的 margin 定义为：

$$
m_r(x) = a_r x_1 + b_r x_2 + c_r.
$$

于是边界由

$$
m_r(x)=0
$$

给出。

这一步对应 `rule_margin`。

> 注释：先把规则变成一条线，再问样本相对这条线在哪里。

#### 3.2.3 定义：单条规则的软概率

设有效温度为

$$
\tau_r = T \alpha_r,
$$

则规则正侧概率是：

$$
\rho_r(x)=\sigma(\tau_r m_r(x)).
$$

再由 `positive_class` 决定 class $1$ 概率：

$$
q_r(y=1 \mid x)
=
\begin{cases}
\rho_r(x), & \kappa_r = 1, \\
1-\rho_r(x), & \kappa_r = 0.
\end{cases}
$$

于是单条规则分布为：

$$
q_r(\cdot \mid x)
=
\bigl(1-q_r(y=1 \mid x), q_r(y=1 \mid x)\bigr).
$$

这一步对应 `soft_rule_probability_for_rule` 与 `rule_distribution`。

> 注释：这里最重要的是别把“在规则正侧”误认成“属于 class 1”。中间还隔着一个 `positive_class` 的语义翻译。

#### 3.2.4 命题：多规则聚合

对规则集合 $\mathcal{R}$，聚合 log-score 定义为：

$$
\ell_{\mathcal{R}}(y \mid x)
=
\sum_{r \in \mathcal{R}} w_r \log q_r(y \mid x).
$$

归一化后得到聚合规则分布：

$$
q_{\mathcal{R}}(y \mid x)
=
\frac{\exp(\ell_{\mathcal{R}}(y \mid x))}
{\sum_{k \in \{0,1\}} \exp(\ell_{\mathcal{R}}(k \mid x))}.
$$

等价地：

$$
q_{\mathcal{R}}(y \mid x)
\propto
\prod_{r \in \mathcal{R}} q_r(y \mid x)^{w_r}.
$$

这一步对应 `aggregate_rule_distribution`。

> 注释：这不是“投票平均”，而是“加权乘法型证据融合”。

#### 3.2.5 定义：teacher

设 student 分布为 $p_\theta(\cdot \mid x)$，规则强度为 $\lambda$，则 teacher 定义为：

$$
t_\theta(y \mid x)
=
\frac{p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda}
{\sum_{k \in \{0,1\}} p_\theta(k \mid x)\, q_{\mathcal{R}}(k \mid x)^\lambda}.
$$

这一步对应 `build_teacher_probs`。

于是可以得到本节最核心的结论：

$$
\text{teacher}
=
\text{student distribution}
\times
\text{rule reweighting}.
$$

> 注释：teacher 不是外部老师，而是“当前 student 被规则改写后的老师”。

### 3.3 `trainer.py` 的严格角色

`trainer.py` 负责把 teacher 真正接到参数更新里。

#### 3.3.1 定义：监督损失

对 labeled batch $B_l = \{(x_i,y_i)\}_{i=1}^{n_l}$，监督损失是：

$$
\mathcal{L}_{\mathrm{sup}}
=
\frac{1}{n_l}
\sum_{i=1}^{n_l}
-\log p_\theta(y_i \mid x_i).
$$

对应代码中的 `F.cross_entropy(...)`。

#### 3.3.2 定义：蒸馏损失

把 labeled 与 unlabeled 输入拼接成：

$$
X_r = \mathrm{concat}(X_l, X_u).
$$

在这个 batch 上，蒸馏损失为：

$$
\mathcal{L}_{\mathrm{distill}}
=
\frac{1}{|X_r|}
\sum_{x \in X_r}
\mathrm{KL}\!\bigl(t_\theta(\cdot \mid x)\,\|\,p_\theta(\cdot \mid x)\bigr).
$$

这一步对应 `F.kl_div(F.log_softmax(...), teacher_probs, ...)`。

> 注释：代码的 KL 方向是 teacher 到 student，不是反过来。

#### 3.3.3 定义：总损失

设蒸馏权重为 $\pi_t$，则总损失为：

$$
\mathcal{L}_t
=
(1-\pi_t)\,\mathcal{L}_{\mathrm{sup}}
+ \pi_t\,\mathcal{L}_{\mathrm{distill}}.
$$

其中：

$$
\pi_t
=
\texttt{max\_distill\_weight}
\cdot
\min\left(1,\frac{t}{\max(1,\texttt{ramp\_up\_epochs})}\right).
$$

这对应 `distill_weight_at`。

> 注释：训练早期先更信标签，后期再逐步增强规则 teacher 的牵引力。

#### 3.3.4 推论：无标签样本如何进入训练

因为无标签样本不在 $\mathcal{L}_{\mathrm{sup}}$ 中，但出现在 $X_r$ 中，所以它只通过下面这条路径进入训练：

$$
x_u
\longrightarrow
q_{\mathcal{R}}(\cdot \mid x_u)
\longrightarrow
t_\theta(\cdot \mid x_u)
\longrightarrow
\mathcal{L}_{\mathrm{distill}}.
$$

> 注释：无标签样本没有真标签，但它们仍然可以“学习去模仿规则修正后的 teacher”。

### 3.4 本节应得结论

读完第 3 节，你至少应该能严格说出下面四句话：

1. Logic-Net toy 的规则不是直接写成最终标量 loss，而是先变成 $q_{\mathcal{R}}$。
2. teacher 是 $p_\theta$ 与 $q_{\mathcal{R}}$ 融合后的分布，而不是外部给定的分布。
3. 多规则聚合是 log-space 加权求和，等价于加权乘法型证据融合。
4. 无标签样本通过 teacher 蒸馏路径，而不是通过监督标签路径进入训练。

> 注释：如果这四句讲不顺，就先不要急着往第 10 节细节里钻。

---

## 4. Semantic Loss toy：严格总览

这一节也采用与第 3 节相同的口径：先给对象，再给公式，再给训练路径。

> 注释：Logic-Net 的核心中间对象是 teacher；Semantic Loss 的核心中间对象不是 teacher，而是“满足约束的总概率质量”。

### 4.1 主战场与对象

本节只盯两个文件：

- `repro/03_semantic_loss_toy/constraints.py`
- `repro/03_semantic_loss_toy/trainer.py`

这里的输出不是普通 softmax 多分类，而是 $C$ 个相互独立的 Bernoulli 位。若类别数为 $C$，则单个输出赋值写成：

$$
a = (a_1,\dots,a_C) \in \{0,1\}^C.
$$

模型输出 logits：

$$
z_\theta(x) \in \mathbb{R}^C.
$$

每一位的激活概率是：

$$
p_\theta(a_c=1 \mid x)=\sigma(z_\theta^{(c)}(x)).
$$

> 注释：这里每一位都独立做 sigmoid，所以语义上更像“多个开关位”，而不是 softmax 里“只能选一个格子”。

### 4.2 `constraints.py` 的严格角色

`constraints.py` 负责把逻辑约束变成一个“合法赋值集合”，再计算当前输出对这个集合分配了多少总概率质量。

#### 4.2.1 定义：合法赋值集合

先枚举所有二值赋值：

$$
\{0,1\}^C.
$$

再根据约束 $\phi$ 选出合法子集：

$$
\mathcal{V}_\phi \subseteq \{0,1\}^C.
$$

这一步对应 `get_constraint_spec`。

例如：

- `exactly_one` 对应恰有一位为 $1$
- `at_least_one` 对应至少一位为 $1$
- `exactly_two_bad` 对应恰有两位为 $1$

> 注释：这里的“逻辑”不是 teacher，而是一个合法世界集合。

#### 4.2.2 定义：单个赋值的概率

由于各位独立，某个具体赋值 $a \in \{0,1\}^C$ 的概率为：

$$
P_\theta(a \mid x)
=
\prod_{c=1}^{C}
\sigma(z_\theta^{(c)}(x))^{a_c}
\cdot
\bigl(1-\sigma(z_\theta^{(c)}(x))\bigr)^{1-a_c}.
$$

取对数后得到：

$$
\log P_\theta(a \mid x)
=
\sum_{c=1}^{C}
\left[
a_c \log \sigma(z_\theta^{(c)}(x))
+ (1-a_c)\log \sigma(-z_\theta^{(c)}(x))
\right].
$$

这正对应 `log_satisfaction_mass` 里对 `log_prob_one` 与 `log_prob_zero` 的构造。

> 注释：先算“某一个具体世界”的概率，再谈“所有合法世界加起来”的总质量。

#### 4.2.3 定义：满足概率质量

约束 $\phi$ 的满足概率定义为：

$$
P_\theta(\phi \mid x)
=
\sum_{a \in \mathcal{V}_\phi} P_\theta(a \mid x).
$$

其对数形式为：

$$
\log P_\theta(\phi \mid x)
=
\log \sum_{a \in \mathcal{V}_\phi} P_\theta(a \mid x).
$$

这一步对应 `log_satisfaction_mass`，数值上用 `logsumexp` 实现。

> 注释：不在看某一条规则真假，而是在看“当前输出总共有多少概率落在合法世界里”。

#### 4.2.4 定义：semantic loss

对一个 batch，semantic loss 定义为：

$$
\mathcal{L}_{\mathrm{sem}}
=
-\frac{1}{n}
\sum_{i=1}^{n}
\log P_\theta(\phi \mid x_i).
$$

这对应：

$$
\texttt{return -log\_satisfaction\_mass(logits, spec).mean()}.
$$

> 注释：概率质量越多地落在合法世界里，loss 就越小。

#### 4.2.5 命题：为什么这里必须用独立 sigmoid

若直接使用 softmax，多类 one-hot 结构会先天地偏向“恰有一个类激活”，从而削弱 `exactly_one` 这类约束的辨识度。

使用独立 sigmoid 时，模型可以产生很多“非法世界”，例如：

- 多位同时高
- 所有位都低

于是 semantic loss 才真的有事情可做：

$$
\text{illegal outputs}
\longrightarrow
\text{semantic penalty}
\longrightarrow
\text{probability mass shift to } \mathcal{V}_\phi.
$$

> 注释：这个 toy 故意不让结构先天满足约束，否则你就看不到约束项到底在推什么。

### 4.3 `trainer.py` 的严格角色

#### 4.3.1 定义：监督项

对 labeled batch $B_l$，先把标签变成 one-hot：

$$
e(y_i) \in \{0,1\}^C.
$$

监督损失写成：

$$
\mathcal{L}_{\mathrm{sup}}
=
\frac{1}{|B_l|}
\sum_{(x_i,y_i)\in B_l}
\mathrm{BCEWithLogits}\bigl(z_\theta(x_i), e(y_i)\bigr).
$$

这对应 `_one_hot_targets` 与 `F.binary_cross_entropy_with_logits(...)`。

> 注释：这里仍然是“每一位单独受监督”，不是 softmax 交叉熵。

#### 4.3.2 定义：无标签语义项

对 unlabeled batch $B_u$，语义项定义为：

$$
\mathcal{L}_{\mathrm{sem}}(\theta; B_u)
=
-\frac{1}{|B_u|}
\sum_{x \in B_u}
\log P_\theta(\phi \mid x).
$$

这对应：

$$
\texttt{semantic\_term = semantic\_loss(unlabeled\_logits, constraint\_spec)}.
$$

> 注释：无标签样本不需要 teacher，也不需要伪标签，只需要“约束本身”。

#### 4.3.3 定义：总损失

若语义权重为 $\lambda_t$，则总损失为：

$$
\mathcal{L}_t
=
\mathcal{L}_{\mathrm{sup}}
+ \lambda_t \mathcal{L}_{\mathrm{sem}}.
$$

其中权重调度为：

$$
\lambda_t
=
\texttt{lambda\_semantic}
\cdot
\min\left(1,\frac{t}{\max(1,\texttt{ramp\_up\_epochs})}\right).
$$

这对应 `semantic_weight_at`。

> 注释：训练早期先用标签把模型拉出最乱阶段，再逐步加强约束影响。

#### 4.3.4 推论：无标签样本的进入路径

无标签样本通过下面这条链进入训练：

$$
x_u
\longrightarrow
z_\theta(x_u)
\longrightarrow
P_\theta(\phi \mid x_u)
\longrightarrow
\mathcal{L}_{\mathrm{sem}}.
$$

与 Logic-Net 不同，这里没有 teacher。

> 注释：Logic-Net 是“无标签样本先过 teacher”；Semantic Loss 是“无标签样本直接过约束满足质量”。

### 4.4 本节应得结论

读完第 4 节，你至少应该能严格说出下面四句话：

1. Semantic Loss toy 的中间对象是合法赋值集合 $\mathcal{V}_\phi$，不是 teacher。
2. 核心概率量是 $P_\theta(\phi \mid x)$，即“满足约束的总概率质量”。
3. `log_satisfaction_mass` 的本质是对所有合法赋值概率做 `logsumexp` 聚合。
4. 无标签样本通过 $\mathcal{L}_{\mathrm{sem}}$ 直接进入训练，而不是通过蒸馏进入训练。

---

## 5. 两个 toy 的严格对比

第 3 节和第 4 节现在已经给出两条严格链条。这里把它们并排对齐。

### 5.1 中间对象对比

| 维度 | Logic-Net toy | Semantic Loss toy |
| --- | --- | --- |
| 规则进入点 | 单条规则分布 $q_r$ | 合法赋值集合 $\mathcal{V}_\phi$ |
| 聚合对象 | $q_{\mathcal{R}}(\cdot \mid x)$ | $P_\theta(\phi \mid x)$ |
| 中间机制 | teacher $t_\theta(\cdot \mid x)$ | satisfaction mass |
| 训练接口 | $\mathrm{KL}(t_\theta \,\|\, p_\theta)$ | $-\log P_\theta(\phi \mid x)$ |

> 注释：一个是“先改目标分布”，一个是“直接罚不满足约束的概率结构”。

### 5.2 命题：两者的核心差别不在“有没有规则”，而在“规则进入模型的数学接口不同”

Logic-Net 的路径是：

$$
\mathcal{R}
\longrightarrow
q_{\mathcal{R}}
\longrightarrow
t_\theta
\longrightarrow
\mathrm{KL}(t_\theta \,\|\, p_\theta).
$$

Semantic Loss 的路径是：

$$
\phi
\longrightarrow
\mathcal{V}_\phi
\longrightarrow
P_\theta(\phi \mid x)
\longrightarrow
-\log P_\theta(\phi \mid x).
$$

因此两者的本质差别是：

- Logic-Net 先构造分布型 teacher；
- Semantic Loss 直接构造约束满足型目标函数。

### 5.3 命题：两者对无标签样本的利用路径也不同

Logic-Net：

$$
x_u
\longrightarrow
q_{\mathcal{R}}(\cdot \mid x_u)
\longrightarrow
t_\theta(\cdot \mid x_u)
\longrightarrow
\mathcal{L}_{\mathrm{distill}}.
$$

Semantic Loss：

$$
x_u
\longrightarrow
P_\theta(\phi \mid x_u)
\longrightarrow
\mathcal{L}_{\mathrm{sem}}.
$$

所以两者都能利用无标签样本，但“利用机制”不是同一种。

> 注释：一个是“模仿规则教师”，一个是“直接提高合法世界概率”。

### 5.4 本节应得结论

如果只压缩成两句：

- Logic-Net：先改目标分布，再通过蒸馏改参数。
- Semantic Loss：直接通过约束满足概率质量改参数。

---

## 6. 统一口径后的阅读执行版

这一节不再只是“今晚怎么读”，而是给出一个和前面推导口径一致的阅读协议。

### 6.1 阶段 A：先建立 Logic-Net 的严格主链

操作顺序：

1. 读 `repro/01_logic_net_toy/README.md`
2. 读 `repro/01_logic_net_toy/rules.py`
3. 在 `repro/01_logic_net_toy/trainer.py` 中定位 `train_logic_guided`

你必须先得到下面这条链：

$$
r
\longrightarrow
m_r(x)
\longrightarrow
q_r(\cdot \mid x)
\longrightarrow
q_{\mathcal{R}}(\cdot \mid x)
\longrightarrow
t_\theta(\cdot \mid x)
\longrightarrow
\mathcal{L}_{\mathrm{distill}}.
$$

阶段完成标准：

你能独立写出一句总结：

`Logic-Net toy 先把规则变成聚合规则分布，再与 student 分布融合成 teacher，最后用 teacher 作为 target 去蒸馏 student。`

### 6.2 阶段 B：再建立 Semantic Loss 的严格主链

操作顺序：

1. 读 `repro/03_semantic_loss_toy/README.md`
2. 读 `repro/03_semantic_loss_toy/constraints.py`
3. 在 `repro/03_semantic_loss_toy/trainer.py` 中定位 `train_semantic_guided`

你必须先得到下面这条链：

$$
\phi
\longrightarrow
\mathcal{V}_\phi
\longrightarrow
P_\theta(\phi \mid x)
\longrightarrow
\mathcal{L}_{\mathrm{sem}}.
$$

阶段完成标准：

你能独立写出一句总结：

`Semantic Loss toy 先定义合法赋值集合，再计算当前输出在合法赋值集合上的总概率质量，并把它的负对数直接作为约束损失。`

### 6.3 阶段 C：最后做形式对比

只回答下面四个问题：

1. 两者的中间对象分别是什么？
2. 两者的无标签路径分别是什么？
3. 哪一个更像“规则蒸馏”？
4. 哪一个更像“语义直接进 loss”？

如果你回答时能把公式路径一起写出来，那么这一步才算真正完成。

### 6.4 最低完成标准

如果时间不够，你至少要能在纸上写出下面两条式子：

Logic-Net：

$$
t_\theta(y \mid x)
\propto
p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda.
$$

Semantic Loss：

$$
\mathcal{L}_{\mathrm{sem}}
=
-\frac{1}{n}
\sum_{i=1}^{n}
\log P_\theta(\phi \mid x_i).
$$

> 注释：这两条式子一旦抓住，整份笔记的主骨架就抓住了。

---

## 7. 今晚不要先陷进去的地方

1. 不要先从 `run.py` 开始。
2. 不要先研究画图函数。
3. 不要先纠结每个超参数。
4. 不要一开始就追原论文全部细节。

今晚先抓的是：

- `Logic-Net` 的 `teacher`
- `Semantic Loss` 的 `satisfaction mass`

这两个东西抓住了，后面论文、实验、结果解释才会逐渐顺。

---

## 8. 如果今晚还有余力，再往下补什么

先补这两份长笔记：

- `research_activation_system/notes/logic_net_notes_zh.md`
- `research_activation_system/notes/semantic_loss_notes_zh.md`

再补这两份逐行解析：

- `repro/01_logic_net_toy/logic_net_toy_代码逐行解析.md`
- `repro/03_semantic_loss_toy/semantic_loss_toy_代码逐行解析.md`

建议顺序仍然是：

- 先 `Logic-Net`
- 再 `Semantic Loss`
- 最后再回到 `DL2`

原因很简单：

- `Logic-Net` 让你先看清 `teacher-student`
- `Semantic Loss` 让你再看清 `constraint -> loss`
- 等这两条线稳了，`DL2` 的系统化位置会更容易看懂

---

## 9. 今晚结束时的最低完成标准

如果你最后只写下下面这 6 句话，也算完成得很好：

1. `Logic-Net` 的核心不是直接罚规则，而是构造 teacher。
2. `Logic-Net` toy 里 teacher 由 student 分布和 rule 分布融合得到。
3. `Semantic Loss` 的核心不是 teacher，而是合法赋值集合的总概率质量。
4. `Semantic Loss` toy 里最关键的函数是 `log_satisfaction_mass`。
5. 两种方法都能利用 unlabeled 数据，但利用方式不同。
6. 今晚我已经知道该盯哪几个文件，而不是继续泛读。

---

## 10. Logic-Net toy 的严格推导式讲解

这一节只讨论两个文件：

- `repro/01_logic_net_toy/rules.py`
- `repro/01_logic_net_toy/trainer.py`

这一节的组织方式会刻意更“数学化”：

1. 先下定义。
2. 再从定义推出单条规则的概率形式。
3. 再从单条规则推出多规则聚合。
4. 再从规则聚合推出 teacher。
5. 最后再从 teacher 推出训练目标与代码实现。

为了方便你在 VS Code Preview 里定位，我把标题切得比较细。每一个核心概念、命题、函数都单独成节。

> 注释：你可以把这一节当成“代码版证明”。上面是严格推导，下面的注释是大白话翻译。

### 10.1 问题设定

我们先把这个 toy 的学习问题写清楚。

输入空间是二维欧氏空间：

$$
\mathcal{X} = \mathbb{R}^2.
$$

标签空间是二分类空间：

$$
\mathcal{Y} = \{0,1\}.
$$

有标签数据集记为：

$$
\mathcal{D}_l = \{(x_i, y_i)\}_{i=1}^{N_l}.
$$

无标签数据集记为：

$$
\mathcal{D}_u = \{u_j\}_{j=1}^{N_u}.
$$

student 模型记为 $f_\theta$，它把输入映射到二分类 logits：

$$
f_\theta : \mathbb{R}^2 \to \mathbb{R}^2,
\qquad
f_\theta(x) = z_\theta(x).
$$

其中

$$
z_\theta(x) = \bigl(z_\theta^{(0)}(x), z_\theta^{(1)}(x)\bigr).
$$

对 logits 做 softmax，得到 student 的预测分布：

$$
p_\theta(y=k \mid x)
=
\frac{\exp(z_\theta^{(k)}(x))}
{\exp(z_\theta^{(0)}(x))+\exp(z_\theta^{(1)}(x))},
\qquad k \in \{0,1\}.
$$

> 注释：模型先给两个分数，再把它们归一化成“属于 0 类/1 类”的概率。

### 10.2 `RuleSpec` 的数学角色

一条规则不是一句自然语言，而是一个可计算对象。

在这个 toy 中，一条规则 $r$ 被抽象成：

$$
r = (a_r, b_r, c_r, \kappa_r, w_r, \alpha_r),
$$

其中：

- $(a_r, b_r)$ 是线性系数，对应 `coefficients`
- $c_r$ 是偏置，对应 `bias`
- $\kappa_r \in \{0,1\}$ 是正侧支持的类别，对应 `positive_class`
- $w_r > 0$ 是规则权重，对应 `weight`
- $\alpha_r > 0$ 是规则自己的温度缩放，对应 `temperature_scale`

如果把工程字段也写进来，那么 `name` 与 `description` 只是标识和说明，不参与核心数学计算。

> 注释：`RuleSpec` 不是“零碎参数堆一起”，而是在说一条规则至少要回答 5 个问题：线在哪、哪边是正侧、正侧支持哪一类、这条规则有多重要、这条规则有多硬。

### 10.3 定义 1：规则边界与 margin

对任意规则 $r$，定义它的 margin 函数为：

$$
m_r(x) = a_r x_1 + b_r x_2 + c_r.
$$

于是规则边界定义为：

$$
\partial r = \{x \in \mathbb{R}^2 : m_r(x)=0\}.
$$

规则正侧定义为：

$$
H_r^+ = \{x \in \mathbb{R}^2 : m_r(x) > 0\}.
$$

规则负侧定义为：

$$
H_r^- = \{x \in \mathbb{R}^2 : m_r(x) < 0\}.
$$

这正对应 `rules.py` 里的 `rule_margin`。

> 注释：先画一条线，再问样本在线的哪一边，这就是 margin 的第一层意思。

### 10.4 命题 1：为什么它叫 margin

`margin` 这个名字不是随便起的，而是因为 $m_r(x)$ 同时提供了三种信息：

1. 符号信息：$m_r(x)$ 的正负号告诉我们 $x$ 在边界哪一侧。
2. 边界信息：$m_r(x)=0$ 恰好定义了规则边界。
3. 远近信息：$|m_r(x)|$ 越大，$x$ 离边界越“远”。

严格地说，这里是未归一化的 signed margin，而不是欧氏距离。真正的有符号距离应当写成：

$$
d_r(x) = \frac{a_r x_1 + b_r x_2 + c_r}{\sqrt{a_r^2+b_r^2}}.
$$

代码没有做这一步归一化，因此 `rule_margin` 更准确地说是线性分数形式的 margin。

> 注释：它已经够表达“边界位置 + 左右方向 + 离边界多远”，所以在这个 toy 里完全够用。

### 10.5 定义 2：规则温度

设全局基础温度为 $T > 0$，单条规则自己的缩放为 $\alpha_r > 0$，则规则 $r$ 的有效温度定义为：

$$
\tau_r = T \alpha_r.
$$

这正对应代码中的：

$$
\texttt{temperature = base\_temperature * rule.temperature\_scale}.
$$

> 注释：全局温度是“总开关”，规则自己的缩放是“局部微调”。

### 10.6 命题 2：温度不会改变边界，只会改变软硬程度

考虑函数：

$$
s_r(x) = \sigma(\tau_r m_r(x)),
$$

其中 $\sigma(t)=\frac{1}{1+e^{-t}}$ 是 sigmoid。

因为 $\tau_r > 0$，所以有：

$$
\tau_r m_r(x)=0
\iff
m_r(x)=0.
$$

因此，$s_r(x)=0.5$ 的位置恰好仍然是规则边界：

$$
\{x : s_r(x)=0.5\} = \{x : m_r(x)=0\}.
$$

这说明温度不改变边界位置。

另一方面，$\tau_r$ 越大，sigmoid 在 $0$ 附近的斜率越大，于是从 $0$ 到 $1$ 的过渡越陡；$\tau_r$ 越小，过渡越平缓。

因此可以推出：

- 大温度对应更硬的规则；
- 小温度对应更软的规则。

> 注释：温度不负责“把线挪走”，只负责“过了线以后语气有多坚决”。

### 10.7 定义 3：规则正侧概率

先只看几何，不看类别语义。定义规则正侧概率为：

$$
\rho_r(x) = \sigma(\tau_r m_r(x)).
$$

于是：

- 当 $m_r(x) \gg 0$ 时，$\rho_r(x) \approx 1$
- 当 $m_r(x) \ll 0$ 时，$\rho_r(x) \approx 0$
- 当 $m_r(x)=0$ 时，$\rho_r(x)=0.5$

这正是 `soft_rule_probability_for_rule` 中 `positive_prob` 的几何含义。

> 注释：这里的 `positive_prob` 还不是“属于 class 1 的概率”，而只是“落在规则正侧的概率”。

### 10.8 定义 4：从几何正侧到类别语义

规则还必须说明：正侧到底支持哪个类别。

若 $\kappa_r = 1$，则正侧支持 class $1$；若 $\kappa_r = 0$，则正侧支持 class $0$。

因此，规则对 class $1$ 的支持概率定义为：

$$
q_r(y=1 \mid x)
=
\begin{cases}
\rho_r(x), & \kappa_r = 1, \\
1-\rho_r(x), & \kappa_r = 0.
\end{cases}
$$

进一步，规则诱导出的完整二分类分布为：

$$
q_r(\cdot \mid x)
=
\bigl(q_r(y=0 \mid x), q_r(y=1 \mid x)\bigr)
=
\bigl(1-q_r(y=1 \mid x), q_r(y=1 \mid x)\bigr).
$$

这正对应 `rule_distribution`。

> 注释：先由几何判断“在哪一侧”，再由 `positive_class` 解释“这一侧代表哪个类”。

### 10.9 推论 1：同一条边界可以对应两条语义相反的规则

若两条规则 $r_1,r_2$ 满足

$$
(a_{r_1}, b_{r_1}, c_{r_1}) = (a_{r_2}, b_{r_2}, c_{r_2}),
$$

但

$$
\kappa_{r_1} \neq \kappa_{r_2},
$$

则它们拥有同一条边界，却对应不同的类别偏向。

这正是 `diag_positive` 与 `diag_wrong` 的关系。

> 注释：几何形状一样，不代表语义一样。线还是那条线，但“线的上面支持哪一类”可以反过来。

### 10.10 定义 5：单条规则的硬预测

代码里的 `hard_rule_prediction_for_rule` 定义为：

$$
\hat y_r(x)
=
\mathbf{1}\!\left[q_r(y=1 \mid x)\ge 0.5\right].
$$

结合前面的定义，可以推出：

- 当 $\kappa_r=1$ 时，$\hat y_r(x)=1 \iff m_r(x)\ge 0$
- 当 $\kappa_r=0$ 时，$\hat y_r(x)=1 \iff m_r(x)\le 0$

所以硬预测本质上是在用边界做二值判决。

> 注释：soft 版本是“有多像”，hard 版本就是“最终判成哪一类”。

### 10.11 定义 6：多规则聚合的 log 形式

设规则集合为：

$$
\mathcal{R} = \{r_1,\dots,r_M\}.
$$

对每一个类别 $y \in \{0,1\}$，定义聚合 log-score：

$$
\ell_{\mathcal{R}}(y \mid x)
=
\sum_{j=1}^M w_{r_j}\,\log q_{r_j}(y \mid x).
$$

于是聚合规则分布定义为：

$$
q_{\mathcal{R}}(y \mid x)
=
\frac{\exp(\ell_{\mathcal{R}}(y \mid x))}
{\sum_{k \in \{0,1\}} \exp(\ell_{\mathcal{R}}(k \mid x))}.
$$

这正对应 `aggregate_rule_distribution`。

> 注释：代码不是把规则“平均一下”，而是先把每条规则的对数证据加起来，再统一归一化。

### 10.12 命题 3：多规则聚合等价于加权乘法型证据融合

由上一节定义直接展开可得：

$$
\exp(\ell_{\mathcal{R}}(y \mid x))
=
\exp\left(\sum_{j=1}^M w_{r_j}\log q_{r_j}(y \mid x)\right)
=
\prod_{j=1}^M q_{r_j}(y \mid x)^{w_{r_j}}.
$$

因此：

$$
q_{\mathcal{R}}(y \mid x)
=
\frac{\prod_{j=1}^M q_{r_j}(y \mid x)^{w_{r_j}}}
{\sum_{k \in \{0,1\}} \prod_{j=1}^M q_{r_j}(k \mid x)^{w_{r_j}}}.
$$

这就是加权 product-of-experts 形式。

所以可以推出：

- 如果多条规则同时支持同一类别，该类别概率会被乘法式放大；
- 如果某条高权重规则强烈反对某类别，该类别概率会被明显压低。

> 注释：这就是为什么 `weight` 很重要。它不是“可有可无的系数”，而是在决定哪条规则更有发言权。

### 10.13 定义 7：聚合规则的硬预测

由聚合分布定义整体规则系统的硬预测：

$$
\hat y_{\mathcal{R}}(x)
=
\arg\max_{y \in \{0,1\}} q_{\mathcal{R}}(y \mid x).
$$

这正对应 `aggregated_hard_rule_prediction`。

> 注释：单条规则可以错，多条规则融合后可能会变好，也可能因为坏规则太强而变差。

### 10.14 定义 8：student 分布

重新记一下 student 分布。对任意样本 $x$，student 给出：

$$
p_\theta(y \mid x)
=
\mathrm{softmax}(z_\theta(x))_y.
$$

这是代码里 `student_probs = F.softmax(student_logits, dim=1)` 的数学形式。

> 注释：teacher 还没出来之前，student 只是“模型当前自己的想法”。

### 10.15 定义 9：teacher 的 log 形式

设规则强度参数为 $\lambda > 0$，对应 `rule_strength`。

teacher 的未归一化 log-score 定义为：

$$
\tilde \ell_\theta(y \mid x)
=
\log p_\theta(y \mid x)
+ \lambda \log q_{\mathcal{R}}(y \mid x).
$$

于是 teacher 分布定义为：

$$
t_\theta(y \mid x)
=
\frac{\exp(\tilde \ell_\theta(y \mid x))}
{\sum_{k \in \{0,1\}} \exp(\tilde \ell_\theta(k \mid x))}.
$$

这正对应 `build_teacher_probs`。

> 注释：teacher 不是凭空来的，它是“student 当前分布”和“规则分布”合成出来的。

### 10.16 命题 4：teacher 是 student 被规则重加权后的分布

由上一节直接展开：

$$
\exp(\tilde \ell_\theta(y \mid x))
=
\exp(\log p_\theta(y \mid x))
\cdot
\exp(\lambda \log q_{\mathcal{R}}(y \mid x))
=
p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda.
$$

因此：

$$
t_\theta(y \mid x)
=
\frac{p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda}
{\sum_{k \in \{0,1\}} p_\theta(k \mid x)\, q_{\mathcal{R}}(k \mid x)^\lambda}.
$$

这条式子是整个 Logic-Net toy 的中心公式。

它直接说明：

1. teacher 依赖 student；
2. teacher 也依赖规则；
3. `rule_strength` 越大，规则分布对 teacher 的扭转越强。

> 注释：teacher 不是外部老师，而是“当前 student 被规则校正后”的老师。

### 10.17 推论 2：为什么这里不是“直接把规则加到 loss 上”

因为代码的逻辑不是直接构造某个规则罚项 $\mathcal{L}_{\mathrm{rule}}$ 与监督损失相加，而是先通过

$$
p_\theta \quad\text{和}\quad q_{\mathcal{R}}
$$

构造新的目标分布

$$
t_\theta.
$$

然后再让 student 去逼近这个 teacher。

所以这份代码的逻辑是：

$$
\text{rule}
\rightarrow
q_{\mathcal{R}}
\rightarrow
t_\theta
\rightarrow
\text{distillation}.
$$

而不是：

$$
\text{rule}
\rightarrow
\text{direct scalar penalty}.
$$

> 注释：规则先改“目标长什么样”，再间接改参数，而不是直接上来罚参数。

### 10.18 定义 10：监督损失

在有标签 batch $B_l = \{(x_i,y_i)\}_{i=1}^{n_l}$ 上，监督损失定义为：

$$
\mathcal{L}_{\mathrm{sup}}(\theta; B_l)
=
\frac{1}{n_l}
\sum_{i=1}^{n_l}
-\log p_\theta(y_i \mid x_i).
$$

这正对应 `F.cross_entropy(labeled_logits, yb_l)`。

> 注释：这一项就是最普通的“看真标签学分类”。

### 10.19 定义 11：规则使用 batch

在每个 step 里，代码把 labeled 输入与 unlabeled 输入拼接：

$$
X_r = \mathrm{concat}(X_l, X_u).
$$

若对应样本集合记为 $B_r$，则

$$
B_r = B_l^{(x)} \cup B_u,
$$

其中 $B_l^{(x)}$ 表示只取有标签 batch 的输入，不带标签部分。

> 注释：规则系统不关心这里的真标签，它只需要看输入点在哪里。

### 10.20 定义 12：蒸馏损失

在 batch $B_r$ 上，teacher 分布是 $t_\theta(\cdot \mid x)$，student 分布是 $p_\theta(\cdot \mid x)$。

代码调用的是：

- `input = F.log_softmax(student_logits, dim=1)`
- `target = teacher_probs`

因此 PyTorch 中 `F.kl_div(..., reduction="batchmean")` 对应的是：

$$
\mathcal{L}_{\mathrm{distill}}(\theta; B_r)
=
\frac{1}{|B_r|}
\sum_{x \in B_r}
\sum_{y \in \{0,1\}}
t_\theta(y \mid x)
\left(
\log t_\theta(y \mid x)
- \log p_\theta(y \mid x)
\right).
$$

也就是：

$$
\mathcal{L}_{\mathrm{distill}}(\theta; B_r)
=
\frac{1}{|B_r|}
\sum_{x \in B_r}
\mathrm{KL}\!\bigl(t_\theta(\cdot \mid x)\,\|\,p_\theta(\cdot \mid x)\bigr).
$$

这一步非常关键，因为它明确了 KL 的方向是：

$$
\mathrm{KL}(\text{teacher} \,\|\, \text{student}),
$$

而不是相反。

> 注释：代码是在说“把 student 拉向 teacher”，所以 teacher 是 target，student 是被拟合对象。

### 10.21 定义 13：蒸馏权重调度

epoch $t$ 时的蒸馏权重定义为：

$$
\pi_t
=
\texttt{max\_distill\_weight}
\cdot
\min\left(
1,
\frac{t}{\max(1,\texttt{ramp\_up\_epochs})}
\right).
$$

这正对应 `distill_weight_at`。

于是总损失定义为：

$$
\mathcal{L}_t(\theta)
=
(1-\pi_t)\,\mathcal{L}_{\mathrm{sup}}
+ \pi_t\,\mathcal{L}_{\mathrm{distill}}.
$$

> 注释：训练早期先更信标签，后期再逐渐加大 teacher 的影响。

### 10.22 命题 5：无标签样本只通过蒸馏项进入训练

监督损失 $\mathcal{L}_{\mathrm{sup}}$ 只定义在有标签 batch $B_l$ 上。

蒸馏损失 $\mathcal{L}_{\mathrm{distill}}$ 定义在拼接后的 $B_r$ 上。

因此，无标签样本 $u \in B_u$ 满足：

$$
u \notin \mathcal{L}_{\mathrm{sup}},
\qquad
u \in \mathcal{L}_{\mathrm{distill}}.
$$

所以无标签样本参与训练的唯一渠道是：

$$
u
\rightarrow
q_{\mathcal{R}}(\cdot \mid u)
\rightarrow
t_\theta(\cdot \mid u)
\rightarrow
\mathcal{L}_{\mathrm{distill}}.
$$

> 注释：无标签样本没有真标签，但它们仍然可以“模仿规则修正后的 teacher”。

### 10.23 命题 6：`detach` 与 `no_grad` 让 teacher 在当前 step 中被当作常数目标

代码中有两层处理：

- `student_logits.detach()`
- `with torch.no_grad():`

这意味着在当前 step 的反向传播中，teacher 构造路径不参与求导。

实现意义上可以把它理解为：

$$
\nabla_\theta t_\theta(\cdot \mid x) = 0
\quad
\text{（在该 step 的实现图里视作常数 target）}.
$$

因此总梯度是：

$$
\nabla_\theta \mathcal{L}_t
=
(1-\pi_t)\,\nabla_\theta \mathcal{L}_{\mathrm{sup}}
+ \pi_t\,\nabla_\theta \mathcal{L}_{\mathrm{distill}},
$$

其中蒸馏项只通过 student 分布 $p_\theta$ 回传，而不再穿过 teacher 构造图。

> 注释：teacher 在这一小步里更像“临时定下来的答案纸”，而不是和 student 一起被联合优化的可微模块。

### 10.24 `rules.py` 的逐函数解释

下面按照源码顺序回到 `rules.py`。

#### 10.24.1 `RuleSpec`

它定义了一条规则最小需要携带的信息：

- 几何：`coefficients`, `bias`
- 类别语义：`positive_class`
- 规则强度：`weight`, `temperature_scale`
- 元信息：`name`, `description`

它在数学上就是第 10.2 节定义的规则元组。

> 注释：这是“规则的结构体定义”，相当于先把对象类型说清楚。

#### 10.24.2 `RULE_SETS`

这不是推导公式的一部分，而是实验设置的一部分。

它枚举了不同的规则情景：

- 单条正确规则
- 单条错误规则
- 多条大体正确规则
- 正确规则与混杂规则并存
- 多条错误规则

所以 `RULE_SETS` 的作用是提供不同的 $\mathcal{R}$。

> 注释：数学推导里默认有一个规则集合 $\mathcal{R}$，`RULE_SETS` 就是在具体给出它。

#### 10.24.3 `available_rule_sets`

返回所有可选规则集的名字。

它没有新的数学内容，只是配置入口。

#### 10.24.4 `get_rule_specs`

把规则集名字解析成规则列表。

数学上就是从一个字符串标识恢复具体的规则集合 $\mathcal{R}$。

#### 10.24.5 `serialize_rule_specs`

把规则对象转成字典，方便写实验结果。

它不影响理论，只服务于结果记录。

#### 10.24.6 `rule_margin`

这一函数精确实现了第 10.3 节：

$$
m_r(x) = a_r x_1 + b_r x_2 + c_r.
$$

这是所有后续规则概率计算的起点。

#### 10.24.7 `soft_rule_probability_for_rule`

这一函数分两步：

1. 计算有效温度 $\tau_r = T\alpha_r$
2. 把 margin 通过 sigmoid 变成规则支持 class $1$ 的软概率

它精确实现了第 10.5 节到第 10.8 节的推导。

#### 10.24.8 `rule_distribution`

这一函数把标量概率补成完整的二分类分布：

$$
q_r(\cdot \mid x)
=
\bigl(1-q_r(y=1 \mid x), q_r(y=1 \mid x)\bigr).
$$

#### 10.24.9 `hard_rule_prediction_for_rule`

这一函数把单条规则从 soft 版本变成 hard 版本：

$$
\hat y_r(x)
=
\mathbf{1}\!\left[q_r(y=1 \mid x)\ge 0.5\right].
$$

#### 10.24.10 `aggregate_rule_distribution`

这一函数实现第 10.11 节与第 10.12 节：

$$
q_{\mathcal{R}}(y \mid x)
=
\frac{\prod_{r \in \mathcal{R}} q_r(y \mid x)^{w_r}}
{\sum_{k \in \{0,1\}} \prod_{r \in \mathcal{R}} q_r(k \mid x)^{w_r}}.
$$

其中 `clamp_min(1e-6)` 是为了避免出现 $\log 0$。

#### 10.24.11 `aggregated_hard_rule_prediction`

这一函数实现：

$$
\hat y_{\mathcal{R}}(x)
=
\arg\max_{y \in \{0,1\}} q_{\mathcal{R}}(y \mid x).
$$

#### 10.24.12 `build_teacher_probs`

这一函数实现第 10.15 节与第 10.16 节：

$$
t_\theta(y \mid x)
=
\frac{p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda}
{\sum_{k \in \{0,1\}} p_\theta(k \mid x)\, q_{\mathcal{R}}(k \mid x)^\lambda}.
$$

它是整个 `rules.py` 的理论终点，也是整个 Logic-Net toy 的机制中心。

#### 10.24.13 `short_rule_label`

这是展示函数，只负责可视化标签。

它不进入核心推导。

### 10.25 `trainer.py` 的逐函数解释

下面按照源码顺序回到 `trainer.py`。

#### 10.25.1 `ManualAdamW`

这个类是优化器实现。它不属于 Logic-Net 特有思想，但它负责把总损失真正变成参数更新。

其核心形式是：

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t,
$$

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t \odot g_t,
$$

$$
\hat m_t = \frac{m_t}{1-\beta_1^t},
\qquad
\hat v_t = \frac{v_t}{1-\beta_2^t},
$$

$$
\theta
\leftarrow
\theta - \eta\cdot \mathrm{weight\_decay}\cdot \theta
- \eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}.
$$

> 注释：它回答“loss 算完以后参数怎么真的动起来”。

#### 10.25.2 `_to_device`

把 batch 中的张量移动到目标设备。

它不改变任何数学定义。

#### 10.25.3 `distill_weight_at`

实现第 10.21 节的蒸馏权重调度：

$$
\pi_t
=
\texttt{max\_distill\_weight}
\cdot
\min\left(
1,
\frac{t}{\max(1,\texttt{ramp\_up\_epochs})}
\right).
$$

#### 10.25.4 `evaluate`

它同时评估：

1. student 模型自己在数据上的表现；
2. 聚合规则系统自己在数据上的表现；
3. student 与规则系统预测的一致程度；
4. 每一条单独规则的表现。

其中模型预测为：

$$
\hat y_\theta(x)
=
\arg\max_{y \in \{0,1\}} p_\theta(y \mid x).
$$

聚合规则预测为：

$$
\hat y_{\mathcal{R}}(x)
=
\arg\max_{y \in \{0,1\}} q_{\mathcal{R}}(y \mid x).
$$

规则准确率为：

$$
\mathrm{Acc}_{\mathrm{rule}}
=
\frac{1}{N}
\sum_{i=1}^N
\mathbf{1}\!\left[\hat y_{\mathcal{R}}(x_i)=y_i\right].
$$

模型与规则一致率为：

$$
\mathrm{Agree}_{\mathrm{model,rule}}
=
\frac{1}{N}
\sum_{i=1}^N
\mathbf{1}\!\left[\hat y_\theta(x_i)=\hat y_{\mathcal{R}}(x_i)\right].
$$

> 注释：这一步不仅在看“模型准不准”，还在看“模型到底有没有朝规则那边靠过去”。

#### 10.25.5 `_make_optimizer`

只是把配置参数打包成优化器，不引入新的理论。

#### 10.25.6 `train_baseline`

这个函数训练一个没有规则指导的普通监督模型。

它优化的是：

$$
\mathcal{L}_{\mathrm{baseline}}
=
\frac{1}{|B_l|}
\sum_{(x,y)\in B_l}
-\log p_\theta(y \mid x).
$$

它存在的意义是提供比较基线。

#### 10.25.7 `train_logic_guided`

这是整个 `trainer.py` 的核心。

每个训练 step 的逻辑可以完全写成下面这条链：

$$
(X_l, Y_l), X_u
\rightarrow
\mathcal{L}_{\mathrm{sup}}
\rightarrow
X_r
\rightarrow
t_\theta
\rightarrow
\mathcal{L}_{\mathrm{distill}}
\rightarrow
\mathcal{L}_t
\rightarrow
\nabla_\theta \mathcal{L}_t
\rightarrow
\theta.
$$

分解来看：

第一步，在 labeled batch 上计算监督损失：

$$
\mathcal{L}_{\mathrm{sup}}
=
\frac{1}{|B_l|}
\sum_{(x,y)\in B_l}
-\log p_\theta(y \mid x).
$$

第二步，拼接出规则使用 batch：

$$
X_r = \mathrm{concat}(X_l, X_u).
$$

第三步，在 $X_r$ 上计算 student 分布，并构造 teacher：

$$
t_\theta(y \mid x)
=
\frac{p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda}
{\sum_{k \in \{0,1\}} p_\theta(k \mid x)\, q_{\mathcal{R}}(k \mid x)^\lambda}.
$$

第四步，在 $X_r$ 上计算蒸馏损失：

$$
\mathcal{L}_{\mathrm{distill}}
=
\frac{1}{|B_r|}
\sum_{x \in B_r}
\mathrm{KL}\!\bigl(t_\theta(\cdot \mid x)\,\|\,p_\theta(\cdot \mid x)\bigr).
$$

第五步，组合总损失：

$$
\mathcal{L}_t
=
(1-\pi_t)\,\mathcal{L}_{\mathrm{sup}}
+ \pi_t\,\mathcal{L}_{\mathrm{distill}}.
$$

第六步，对 $\mathcal{L}_t$ 反向传播并更新参数。

> 注释：这一整段可以浓缩成一句话：有标签样本负责“别偏离真实标签”，规则 teacher 负责“再往规则偏好的方向推一把”。

#### 10.25.8 为什么这里的 `cycle` 与 `max(...)` 是合理的

有标签 loader 和无标签 loader 的长度通常不同。

代码通过：

- `itertools.cycle(...)`
- `steps = max(len(labeled_loader), len(unlabeled_loader))`

达到的效果是：

- 较短的一边会循环复用；
- 较长的一边决定 epoch 内总步数。

这保证了在一个 epoch 中，两类数据都能持续参与训练。

> 注释：这里的目标不是精确配对，而是别让其中一类数据过早缺席。

#### 10.25.9 `save_metrics`

把指标存成 JSON。

它只负责结果落盘。

#### 10.25.10 `plot_training_curves`

画训练曲线，用来观察：

- baseline 与 logic-guided 的优化轨迹差异；
- 总损失、监督损失、蒸馏损失三者之间的关系。

#### 10.25.11 `_plot_rule_boundaries`

这一函数把第 10.3 节定义的边界真正画出来。

边界方程是：

$$
a_r x_1 + b_r x_2 + c_r = 0.
$$

若 $b_r \neq 0$，则改写成：

$$
x_2 = -\frac{a_r x_1 + c_r}{b_r}.
$$

若 $b_r = 0$ 且 $a_r \neq 0$，则得到竖线：

$$
x_1 = -\frac{c_r}{a_r}.
$$

> 注释：这一步就是把抽象规则重新画回二维平面，让你看到“规则到底是哪条线”。

#### 10.25.12 `plot_decision_boundaries`

这一函数画的是模型自己的概率场与决策边界。

它在网格上计算：

$$
p_\theta(y=1 \mid x),
$$

于是模型的 $0.5$ 决策边界就是：

$$
\{x \in \mathbb{R}^2 : p_\theta(y=1 \mid x)=0.5\}.
$$

再叠加规则边界、测试点、有标签点，你就能同时看到：

1. 数据分布；
2. 模型学到的边界；
3. 规则建议的边界。

### 10.26 整个 Logic-Net toy 的端到端原理总结

现在把所有步骤重新压成一条严格链条：

第一步，定义规则的几何结构：

$$
m_r(x) = a_r x_1 + b_r x_2 + c_r.
$$

第二步，用 sigmoid 把几何边界变成软规则概率：

$$
\rho_r(x)=\sigma(\tau_r m_r(x)).
$$

第三步，引入 `positive_class`，得到单条规则的类别分布：

$$
q_r(\cdot \mid x).
$$

第四步，用加权 log 聚合得到整体规则分布：

$$
q_{\mathcal{R}}(\cdot \mid x).
$$

第五步，把 student 分布与规则分布合成为 teacher：

$$
t_\theta(y \mid x)
=
\frac{p_\theta(y \mid x)\, q_{\mathcal{R}}(y \mid x)^\lambda}
{\sum_{k} p_\theta(k \mid x)\, q_{\mathcal{R}}(k \mid x)^\lambda}.
$$

第六步，在 labeled 数据上算监督损失，在 labeled 与 unlabeled 的拼接 batch 上算蒸馏损失：

$$
\mathcal{L}_t
=
(1-\pi_t)\,\mathcal{L}_{\mathrm{sup}}
+ \pi_t\,\mathcal{L}_{\mathrm{distill}}.
$$

第七步，只通过 student 路径回传梯度，更新参数。

所以整个 toy 的理论核心可以最后压成一句：

$$
\text{rule}
\rightarrow
\text{rule distribution}
\rightarrow
\text{rule-aware teacher}
\rightarrow
\text{KL distillation}
\rightarrow
\text{student update}.
$$

> 注释：这就是这份代码真正实现的 Logic-Net 思路。规则不是直接变成最终 loss，而是先变成 teacher，再通过 teacher 去塑造 student。

### 10.27 读到这里你应该能严格回答的 10 个问题

1. `RuleSpec` 为什么必须同时包含几何、语义和强度信息？
2. `rule_margin` 为什么能同时刻画边界、方向和远近？
3. 为什么温度不会改变边界位置？
4. 为什么 `positive_prob` 不是最终的 class $1$ 概率？
5. 为什么同一条边界可以对应两条语义相反的规则？
6. 多条规则聚合为什么是加权乘法型证据融合，而不是简单平均？
7. `rule_strength` 和 `weight` 控制的到底是不是同一件事？
8. `F.kl_div` 在这里对应的 KL 方向为什么是 $\mathrm{KL}(\text{teacher}\,\|\,\text{student})$？
9. 无标签样本是通过哪条严格的数学路径进入训练的？
10. 为什么 `detach` 与 `no_grad` 会让 teacher 在当前 step 中充当常数 target？

如果这 10 个问题你都能顺着推出来，那么你对这两个文件的理解就已经不是“读懂函数”，而是“读懂机制”。
