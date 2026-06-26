from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "10_english" / "01_grammar_reading"
ANCHOR = "\n## 迁移与反思"
MARKER = "<!-- advanced-reading-block -->"


BLOCKS = {
    "01_clause_skeletons_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> In debates about automated diagnosis, the most consequential disagreement is not whether an algorithm can identify patterns that escape a clinician's immediate attention. It is whether the institution that deploys the algorithm can explain which kinds of uncertainty the system has been trained to ignore. A model that performs well on historical data may still fail when the clinical population changes, because the relationships it has learned are often relationships among recorded variables rather than among the underlying biological processes. For that reason, a responsible evaluation asks not only how accurate the model is, but also what has to remain true for that accuracy to mean what its advocates claim.

本段是原创论文语域仿真材料，不复制论文正文；训练目标是让你读真实论文时能主动恢复主干、论元和附加信息。

### 结构地图

1. 第一句先否定一个表层争点：核心分歧不是算法能否识别模式。
2. 第二句给出真正争点：部署机构能否解释系统忽略了哪些不确定性。
3. 第三句说明原因：历史数据表现好，不等于临床环境变化后仍可靠。
4. 第四句提出读者应追问的评价标准。

### 句群拆解

- `the most consequential disagreement is not whether...` 的主干是 `disagreement is not whether...`，`about automated diagnosis` 只是议题范围。
- 第二句的主干是 `It is whether...`，`It` 回指上一句的 `the most consequential disagreement`。
- 第三句主干是 `A model may fail`；`that performs well...` 是定语从句，`because...` 给出失败原因。
- 第四句主干是 `a responsible evaluation asks...`，后面两个 `what/how` 从句是 `asks` 的内容论元。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

请写出第三句的最小主干，并说明哪些成分不能删、哪些成分只是解释条件。

:::solution 查看解析
第三句最小主干是 `A model may fail`。但若为了理解论文论证，不能只停在这三个词上，还要保留 `when the clinical population changes`，因为它限制失败发生的情形；`because...` 是原因从句，用来解释为什么历史数据表现好仍可能失败。`that performs well on historical data` 修饰 `model`，不是主句谓语。
:::

### 高阶训练 2
**高阶语境：学术科研**

第二句中的 `which kinds of uncertainty the system has been trained to ignore` 在句法上充当什么成分？为什么这不是一个独立问句？

:::solution 查看解析
它是 `explain` 的宾语内容，是嵌入式疑问分句。独立问句会使用疑问语序，如 `which kinds ... has the system...`；这里保持陈述语序 `the system has been trained`，说明它被嵌入到 `can explain` 后面，作为“解释的内容”。
:::

### 高阶训练 3
**高阶语境：真实生活**

把最后一句改写成生活场景：比如评价一个导航软件。要求保留 `not only..., but also...` 的双重追问结构。

:::solution 查看解析
可以写成：`A careful user asks not only how fast the navigation app finds a route, but also what has to remain true for that route to be reliable.` 这里 `not only` 后问速度，`but also` 后问可靠性的前提，结构与原句一致。
:::
""",
    "02_tense_aspect_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> Researchers have long assumed that remote collaboration reduces informal learning, but the evidence has become less straightforward as teams have adopted persistent chat, shared documents, and recorded meetings. In one longitudinal study, junior employees reported that they had received fewer spontaneous explanations during their first months online, while managers argued that written exchanges had made some forms of feedback more visible than they had been in the office. The important question, therefore, is not simply whether remote work lowered learning, but which kinds of learning had already depended on physical proximity and which kinds were being redistributed across digital records.

### 结构地图

1. 第一句用现在完成时 `have long assumed / has become` 把过去延续到现在。
2. 第二句用过去完成时 `had received / had made / had been` 表示相对于研究报告时间更早的经验。
3. 第三句把问题从“是否降低学习”推进到“不同学习类型如何迁移”。

### 句群拆解

- `have long assumed` 表示这种假设不是一次性发生，而是长期存在到现在。
- `has become less straightforward` 暗示证据状态发生了变化，并且这个变化影响当前判断。
- `had received fewer...` 是员工回忆研究期早段经历；`had made... more visible` 是经理对已经发生变化的解释。
- `were being redistributed` 用过去进行被动，强调研究观察期内正在发生的重组。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

解释为什么第一句不用简单过去时 `assumed`，而用 `have long assumed`。

:::solution 查看解析
`have long assumed` 把假设的起点放在过去，同时强调它一直影响到现在的研究讨论。若用 `assumed`，读者可能理解为过去某个阶段的观点；现在完成时则说明这个观点仍是当前争论的背景。
:::

### 高阶训练 2
**高阶语境：学术科研**

第二句中两个过去完成时 `had received` 和 `had made` 分别服务于什么时间关系？

:::solution 查看解析
`had received` 表示员工在报告时回顾“刚上线前几个月已经经历过的事情”；`had made` 表示经理认为书面交流在评价时点之前已经产生了影响。两者都把事件放到“研究报告/访谈陈述”之前。
:::

### 高阶训练 3
**高阶语境：真实生活**

用一句英语描述：你原来一直以为线上课效率低，但最近发现录屏和共享文档让复习更容易。要求使用现在完成时。

:::solution 查看解析
可以写：`I have long thought that online classes were less efficient, but recorded lessons and shared documents have made review easier recently.` 第一个现在完成时表示长期看法，第二个现在完成时表示最近变化对现在的影响。
:::
""",
    "03_modality_counterfactuals_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The policy might appear successful if success is defined only as a short-term increase in enrollment. Yet a different conclusion would follow if the analysis asked whether the students who enrolled under the policy could have achieved the same outcomes without the subsidy. The counterfactual is difficult to observe directly, so the paper treats matched districts as a proxy rather than as proof. This distinction matters because a policy can be associated with an outcome without having caused it.

### 结构地图

1. 第一句用 `might` 降低断言强度，并把成功限定在一个定义里。
2. 第二句用 `would follow if...` 建立反事实推理路径。
3. 第三句说明反事实不可直接观察，所以只能用代理对象。
4. 第四句区分相关和因果。

### 句群拆解

- `might appear successful` 不是说政策一定成功，而是“在某定义下看起来成功”。
- `would follow if...` 表示结论依赖一个未实际采取的分析问题。
- `could have achieved` 指向过去可能性：没有补贴时是否也能达到同样结果。
- `rather than as proof` 把证据地位压低：matched districts 是 proxy，不是 proof。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

找出本段中最关键的反事实问题，并说明它为什么比“入学率是否提高”更深。

:::solution 查看解析
关键问题是 `whether the students who enrolled under the policy could have achieved the same outcomes without the subsidy`。它问的是没有补贴时结果是否仍会发生，直接对应因果判断；“入学率是否提高”只描述政策后发生了什么，不能排除其他原因。
:::

### 高阶训练 2
**高阶语境：学术科研**

解释 `might appear`, `would follow`, `could have achieved` 三个情态结构的功能差异。

:::solution 查看解析
`might appear` 表示谨慎判断；`would follow` 表示在某条件成立时会推出某结论；`could have achieved` 表示过去未观测情形中的可能性。三者分别承担“弱断言、条件推论、反事实可能性”。
:::

### 高阶训练 3
**高阶语境：真实生活**

朋友说“我喝了咖啡所以考试考好了”。请用英文写一句反事实追问。

:::solution 查看解析
可以写：`Would you have performed just as well if you had not drunk the coffee?` 这句话不是否定咖啡可能有用，而是要求比较“实际发生”和“没有咖啡时可能发生”的结果。
:::
""",
    "04_noun_phrases_reference_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The rapid expansion of platform-based labor has intensified a long-standing dispute over the classification of workers whose income depends on algorithmically mediated tasks. This dispute is not merely terminological. The category assigned to such workers determines which protections they can claim, which risks firms can externalize, and which forms of bargaining remain legally imaginable. For that reason, the seemingly technical phrase independent contractor often carries a theory of responsibility inside it.

### 结构地图

1. 第一句由一个超长名词短语作主语，核心名词是 `expansion`。
2. 第二句用 `This dispute` 回指上一句的分类争议。
3. 第三句展开 `classification/category` 的后果。
4. 第四句说明术语背后的责任理论。

### 句群拆解

- `The rapid expansion of platform-based labor` 的中心是 `expansion`，不是 `labor`。
- `workers whose income depends...` 是 `workers` 的关系从句，说明被分类对象。
- 第三句主干是 `The category determines...`，后面三个 `which` 从句是并列宾语。
- `the seemingly technical phrase independent contractor` 是名词短语，核心是 `phrase`，`independent contractor` 是短语内容。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

拆开第一句主语，写出它的中心词、前置修饰和后置修饰。

:::solution 查看解析
主语是 `The rapid expansion of platform-based labor`。中心词是 `expansion`；前置修饰是 `rapid`；后置修饰是 `of platform-based labor`。后面的 `whose income depends...` 不修饰 `expansion`，而是修饰 `workers`。
:::

### 高阶训练 2
**高阶语境：学术科研**

第三句中三个 `which` 从句为什么可以并列？它们共同受哪个动词支配？

:::solution 查看解析
三个 `which` 从句都回答“这个类别决定什么”，共同受 `determines` 支配：决定劳动者可主张哪些保护、企业可外部化哪些风险、哪些谈判形式在法律上仍可想象。
:::

### 高阶训练 3
**高阶语境：真实生活**

把 `the seemingly technical phrase independent contractor often carries a theory of responsibility inside it` 改写成中文解释。

:::solution 查看解析
可以解释为：“independent contractor 这个看起来只是技术分类的词，实际上暗含了谁该承担责任的判断。”重点不是翻译词面，而是看出名词短语背后的制度含义。
:::
""",
    "05_complement_subordinate_clauses_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The authors argue that the apparent stability of the measure should not be mistaken for conceptual clarity. They show that respondents who select the same option may be answering different questions, because some treat the scale as a measure of satisfaction while others treat it as a measure of obligation. What the study demonstrates, then, is that a survey item can be statistically reliable without being semantically stable.

### 结构地图

1. 第一句 `argue that...` 给出作者论点。
2. 第二句 `show that...` 给出证据和解释。
3. 第三句用 `What... is that...` 总结研究证明的内容。

### 句群拆解

- `that the apparent stability...` 是 `argue` 的宾语从句。
- `respondents who select the same option` 中 `who...` 限定受访者。
- `because...` 从句解释为什么同选项不等于同理解。
- `What the study demonstrates` 是主语从句；`that a survey item...` 是表语从句。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

第三句的主句谓语是什么？两个从句分别占据什么句法位置？

:::solution 查看解析
主句谓语是 `is`。`What the study demonstrates` 是主语从句，整体充当主语；`that a survey item can be statistically reliable without being semantically stable` 是表语从句，说明被证明的内容。
:::

### 高阶训练 2
**高阶语境：学术科研**

解释 `statistically reliable` 与 `semantically stable` 的对比在论证中起什么作用。

:::solution 查看解析
前者说数据在统计上可能重复一致，后者说受访者是否在理解同一个意义。作者要说明：数字稳定不必然等于概念清楚，因此测量质量不能只看统计指标。
:::

### 高阶训练 3
**高阶语境：真实生活**

请用 `without being...` 写一句生活例句，表达“一个评价可能很一致，但意思并不一致”。

:::solution 查看解析
可以写：`A restaurant may receive consistently high ratings without being praised for the same reason by every customer.` 一致的是评分，不一致的是评分背后的含义。
:::
""",
    "06_relatives_apposition_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The archive, which contains letters written over four decades, has often been treated as evidence of a single political conversion. That interpretation, however, overlooks a simpler possibility: that the writer used different vocabularies for different audiences. The letters that were sent to party officials emphasize loyalty, whereas those addressed to family members describe uncertainty and fatigue. The contrast suggests not hypocrisy, but audience-sensitive self-presentation.

### 结构地图

1. 第一句非限制性关系从句介绍 archive 的内容。
2. 第二句冒号后用同位语内容说明 `a simpler possibility`。
3. 第三句限制性关系从句区分不同信件。
4. 第四句给出解释：不是虚伪，而是面向受众的自我呈现。

### 句群拆解

- `which contains...` 只是补充说明 archive，不限定是哪一个 archive。
- `that the writer used...` 是 `possibility` 的同位内容。
- `letters that were sent...` 中的 `that` 是限制性定语从句，区分写给官员的信。
- `those addressed to family members` 中 `those` 代替 `letters`，后面的过去分词短语作后置修饰。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

比较第一句 `which contains...` 与第三句 `that were sent...` 的功能差别。

:::solution 查看解析
`which contains...` 是非限制性补充信息，删去后仍指同一个 archive；`that were sent...` 是限制性信息，用来从所有 letters 中筛出写给 party officials 的那一类。前者补充，后者分类。
:::

### 高阶训练 2
**高阶语境：学术科研**

第二句冒号后的 `that` 从句为什么不是普通定语从句？

:::solution 查看解析
它解释 `a simpler possibility` 的具体内容，即“这个可能性是什么”。它不是修饰一个名词的属性，而是填充该名词的命题内容，因此是同位内容从句。
:::

### 高阶训练 3
**高阶语境：真实生活**

用 `those addressed to...` 模仿写一句，比较两类消息。

:::solution 查看解析
可以写：`The messages sent to colleagues sound formal, whereas those addressed to close friends are brief and playful.` `those` 代替 `messages`，`addressed to close friends` 后置修饰。
:::
""",
    "07_nonfinite_clauses_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> Seeking to reduce the noise in the dataset, the researchers excluded observations recorded during the first week of implementation. The decision, while defensible, makes the estimated effect harder to interpret, because the excluded cases may have captured the period in which users were still learning to navigate the interface. To treat the remaining data as fully representative is therefore to assume that adaptation itself is not part of the intervention's effect.

### 结构地图

1. 第一句用现在分词短语说明研究者排除数据的目的。
2. 第二句用过去分词短语限定被排除的 observations，并解释后果。
3. 第三句用两个不定式结构形成判断：把剩余数据当代表性样本，就是作出一个假设。

### 句群拆解

- `Seeking to reduce...` 的逻辑主语是 `the researchers`。
- `recorded during...` 修饰 `observations`，表示这些观察值是在第一周记录的。
- `while defensible` 是压缩让步结构，完整意思近似 `although the decision is defensible`。
- `To treat... is therefore to assume...` 中两个不定式分别占据主语和表语位置。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

判断 `Seeking to reduce the noise in the dataset` 的逻辑主语，并说明如果主语不一致会产生什么问题。

:::solution 查看解析
逻辑主语是 `the researchers`，因为是研究者试图降低噪声。如果后面主句主语换成 `observations`，就会变成“观察值试图降低噪声”，造成悬垂修饰。
:::

### 高阶训练 2
**高阶语境：学术科研**

第三句中 `To treat... is therefore to assume...` 为什么适合学术写作？

:::solution 查看解析
它把一个方法选择转化为一个可审查的前提：把剩余数据视为代表性样本，就等于假设适应过程不属于干预效果。这个结构能暴露推理条件，而不是只陈述操作。
:::

### 高阶训练 3
**高阶语境：真实生活**

用 `while defensible` 写一句：某个决定可以理解，但会带来解释困难。

:::solution 查看解析
可以写：`The decision to skip the meeting, while defensible, made the later misunderstanding harder to resolve.` `while defensible` 压缩了让步关系，主干仍是 `The decision made... harder...`。
:::
""",
    "08_negation_scope_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The study does not show that the treatment has no effect. It shows that the available evidence is not strong enough to distinguish a small effect from random variation. Nor does the failure to reach statistical significance imply that the theory is false; it may instead indicate that the study was not designed to detect the kind of effect the theory predicts. A careful reader therefore separates absence of evidence from evidence of absence.

### 结构地图

1. 第一句先限定否定范围：研究没有证明“无效”。
2. 第二句说明真正结论：证据不足以区分小效应和随机波动。
3. 第三句用倒装否定 `Nor does...` 阻止读者过度推论。
4. 第四句提出经典区分：没有证据不等于证据表明没有。

### 句群拆解

- `does not show that... has no effect` 中外层否定落在 `show` 上，不是直接断言 treatment 无效。
- `not strong enough to distinguish...` 的否定范围是证据强度。
- `Nor does... imply...` 等于 `The failure... does not imply... either`。
- `not designed to detect...` 否定的是研究设计能力，不是否定理论预测本身。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

说明第一句和“the treatment has no effect”在逻辑上有什么不同。

:::solution 查看解析
第一句是否定“研究证明了无效”这个说法，即证据没有达到证明无效的程度；`the treatment has no effect` 是直接断言治疗没有效果。前者是证据状态判断，后者是世界状态判断。
:::

### 高阶训练 2
**高阶语境：学术科研**

解释 `absence of evidence` 与 `evidence of absence` 的差别。

:::solution 查看解析
`absence of evidence` 是没有足够证据支持某结论；`evidence of absence` 是有证据支持某对象或效应不存在。前者通常要求继续谨慎，后者才允许更强的否定结论。
:::

### 高阶训练 3
**高阶语境：真实生活**

有人说“我没看到消息，所以你一定没发”。请用英文回应，体现否定范围。

:::solution 查看解析
可以写：`The fact that I did not see the message does not prove that you did not send it.` 这句话否定的是“没看到能证明没发”，而不是直接判断对方是否发送。
:::
""",
    "09_comparison_parallelism_ellipsis_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The new curriculum improved students' performance more in tasks requiring explanation than in tasks requiring memorization. This pattern is less surprising than it first appears, because the intervention gave students more opportunities to compare strategies, revise claims, and justify conclusions. The gains were therefore not simply larger than those in the control group; they were larger in precisely the domain the curriculum was designed to affect.

### 结构地图

1. 第一句比较两个任务领域的提升幅度。
2. 第二句用 `less... than...` 修正读者直觉。
3. 第三句不是简单比较实验组与控制组，而是指出比较发生在预设目标领域。

### 句群拆解

- `more in A than in B` 比较的是同一课程对两类任务的影响。
- `less surprising than it first appears` 中省略了比较基准：“比最初看起来的那样更不意外”。
- `compare strategies, revise claims, and justify conclusions` 三个动词结构平行。
- `those in the control group` 中 `those` 代替 `gains`。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

第一句比较的对象是什么？不要把它误读成哪一种比较？

:::solution 查看解析
它比较的是“同一新课程在解释型任务与记忆型任务中的提升幅度”。不要误读成“新课程和旧课程的总体比较”，因为句中比较结构是 `more in tasks... than in tasks...`。
:::

### 高阶训练 2
**高阶语境：学术科研**

分析 `compare strategies, revise claims, and justify conclusions` 的平行性。

:::solution 查看解析
三个成分都是原形动词 + 名词宾语，且共同受 `gave students more opportunities to` 支配。平行结构让读者看出干预提供的是一组同类认知活动。
:::

### 高阶训练 3
**高阶语境：真实生活**

写一句比较：某个 app 在“规划复杂行程”上比在“查附近餐厅”上更有用。

:::solution 查看解析
可以写：`The app is more useful for planning complex trips than for finding nearby restaurants.` 比较对象是两个用途，结构保持 `more useful for A than for B` 的平行。
:::
""",
    "10_information_structure_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> Many studies report that students benefit from feedback. Less often discussed is the order in which that feedback becomes useful. In the first stage, students may need comments that identify errors; only later do they benefit from comments that challenge the assumptions behind their solutions. What matters, then, is not feedback in the abstract but the fit between a learner's current representation of the problem and the kind of response the teacher provides.

### 结构地图

1. 第一句给出读者熟悉的旧信息：反馈有用。
2. 第二句倒装，把“较少讨论的点”放到句首突出。
3. 第三句用时间推进展示反馈需求变化。
4. 第四句用 `not... but...` 把主题从抽象反馈转向匹配关系。

### 句群拆解

- `Less often discussed is...` 是信息结构调整，正常语序可还原为 `The order... is less often discussed`。
- `In the first stage` 与 `only later` 构成时间对比。
- `comments that identify errors` 与 `comments that challenge...` 是两类反馈。
- `What matters` 是主语从句，把真正重要的内容推迟到 `is` 后展开。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

第二句为什么采用倒装，而不写成 `The order... is less often discussed`？

:::solution 查看解析
倒装把 `Less often discussed` 放到句首，形成“从已有共识转向被忽视问题”的信息推进。它不仅改变语序，也改变读者注意力：重点不再是反馈有用，而是反馈何时有用。
:::

### 高阶训练 2
**高阶语境：学术科研**

最后一句中 `not feedback in the abstract but the fit...` 的论证功能是什么？

:::solution 查看解析
它排除一个过宽的概念“抽象的反馈”，改为强调具体匹配关系。作者不是问反馈有没有用，而是问学生当前理解状态和教师回应类型是否匹配。
:::

### 高阶训练 3
**高阶语境：真实生活**

用 `What matters is not... but...` 写一句关于学习方法的表达。

:::solution 查看解析
可以写：`What matters is not the number of hours you study but the quality of attention you bring to each problem.` 结构把表面指标排除，突出真正变量。
:::
""",
    "11_nominalization_compression_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The privatization of risk in contemporary labor markets has made insecurity appear to be a feature of individual planning rather than a consequence of institutional design. This reframing matters because the conversion of collective problems into personal responsibilities changes the kinds of remedies that seem available. If unemployment is described as a failure of adaptability, then training appears natural; if it is described as a failure of demand, then public investment becomes easier to justify.

### 结构地图

1. 第一句由名词化 `privatization` 承载复杂过程。
2. 第二句继续用名词化 `conversion` 描述责任转移。
3. 第三句通过两个 if 分支展示不同命名如何导向不同政策。

### 句群拆解

- `The privatization of risk` 可还原为 “institutions/firms shift risk onto individuals”。
- `insecurity appear to be...` 是 `make + object + complement`。
- `the conversion of collective problems into personal responsibilities` 把“把集体问题变成个人责任”压缩成名词短语。
- 两个 `if it is described as...` 平行，比较两种解释框架。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

把 `the conversion of collective problems into personal responsibilities` 还原成带动词的句子。

:::solution 查看解析
可以还原为：`Institutions or public discourse convert collective problems into personal responsibilities.` 名词化隐藏了施动者；还原后可以追问“谁在转换、为什么转换、转换后谁受益”。
:::

### 高阶训练 2
**高阶语境：学术科研**

解释第三句为什么要并列两个 `if` 分支。

:::solution 查看解析
两个分支展示同一现象被不同方式命名后，会让不同解决方案显得自然。`failure of adaptability` 导向 training；`failure of demand` 导向 public investment。并列结构服务于“语言框架影响政策想象”的论点。
:::

### 高阶训练 3
**高阶语境：真实生活**

把“把拖延描述成性格问题，会让休息和任务设计的问题被忽视”写成英文，尽量使用名词化。

:::solution 查看解析
可以写：`The description of procrastination as a character problem can obscure questions of rest and task design.` `description` 和 `questions` 都是名词化，让句子更接近学术压缩风格。
:::
""",
    "12_cohesion_reference_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> Early experiments suggested that the intervention increased trust, but later replications complicated that conclusion. They found smaller effects in communities where local institutions were already viewed as legitimate. This pattern does not necessarily contradict the original finding; rather, it suggests that the intervention may matter most where baseline trust is low. Such a possibility shifts the question from whether the program works to for whom and under what conditions it works.

### 结构地图

1. 第一句建立旧结论和新复制研究之间的关系。
2. 第二句 `They` 回指 later replications。
3. 第三句 `This pattern` 总结前面的结果，并给出重新解释。
4. 第四句 `Such a possibility` 回指这种条件性解释，推进研究问题。

### 句群拆解

- `that conclusion` 指“干预提高信任”的早期结论。
- `They found...` 中 `They` 不是 early experiments，而是 later replications。
- `This pattern` 指“基线合法性高的社区效果较小”这一整体模式。
- `Such a possibility` 指“干预在基线信任低处更重要”的可能性。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

说明第二句 `They` 的先行词，并给出判断理由。

:::solution 查看解析
`They` 指 `later replications`。理由是第二句说“发现较小效果”，这通常是复制研究的结果；若指 early experiments，就会与第一句中 early experiments 已经 suggested 的内容混淆。
:::

### 高阶训练 2
**高阶语境：学术科研**

`This pattern` 和 `Such a possibility` 分别压缩了前文哪一层信息？

:::solution 查看解析
`This pattern` 压缩的是“合法性已高的社区效果较小”这一经验模式；`Such a possibility` 压缩的是作者对该模式的解释，即干预可能主要在基线信任低时起作用。
:::

### 高阶训练 3
**高阶语境：真实生活**

读句子：`The new schedule helped beginners more than advanced students. This pattern suggests that the problem was not motivation but initial confusion.` 解释 `This pattern` 指什么。

:::solution 查看解析
`This pattern` 指“新时间表对初学者比对高阶学生帮助更大”这一结果模式。它不是指 schedule 本身，而是指前一句呈现出的差异。
:::
""",
    "13_stance_evidentiality_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> The results appear to support the hypothesis that deliberation reduces polarization, although the evidence is not decisive. The strongest effect is observed among participants who entered the discussion with moderate views, which suggests that the treatment may have helped those who were already open to revision. It would therefore be premature to claim that deliberation depolarizes groups in general. A more cautious interpretation is that structured discussion can create opportunities for movement under favorable initial conditions.

### 结构地图

1. 第一句用 `appear to` 和让步从句控制断言强度。
2. 第二句从最强效应出现的位置推断机制。
3. 第三句明确拒绝过度推广。
4. 第四句给出更谨慎的解释。

### 句群拆解

- `appear to support` 表示证据倾向，不是最终证明。
- `although the evidence is not decisive` 明确限制结论强度。
- `which suggests...` 回指前面整个观察结果，而非单个名词。
- `It would therefore be premature to claim...` 是评价性立场：现在下普遍结论还太早。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

列出本段至少三个降低断言强度的表达，并说明它们如何保护论证。

:::solution 查看解析
可以列出 `appear to`, `not decisive`, `may have helped`, `premature to claim`, `more cautious interpretation`, `can create opportunities`。这些表达防止把有限证据说成普遍定律，使结论与证据强度匹配。
:::

### 高阶训练 2
**高阶语境：学术科研**

第二句的 `which suggests` 指向什么？为什么重要？

:::solution 查看解析
它指向“最强效应出现在原本观点较温和的参与者中”这一观察，而不是单独指 `moderate views`。这很重要，因为作者据此推断机制：讨论可能帮助的是本来就愿意修正观点的人。
:::

### 高阶训练 3
**高阶语境：真实生活**

把“这个方法可能有帮助，但现在说它适合所有人还太早”写成英文，使用谨慎立场表达。

:::solution 查看解析
可以写：`The method may be helpful, but it would be premature to claim that it works for everyone.` `may` 和 `premature to claim` 都限制了断言范围。
:::
""",
    "14_academic_argument_zh.md": """
<!-- advanced-reading-block -->
## 长段精读：论文级句群

> A common objection to universal basic income is that it would weaken incentives to work. The objection is serious, but it does not settle the question, because labor supply is only one dimension of economic participation. If a basic income allowed people to leave abusive jobs, invest in training, or care for family members without immediate destitution, then a narrow measure of hours worked might understate the policy's social value. The argument for the policy therefore depends not on denying incentive effects, but on asking which effects a society chooses to count.

### 结构地图

1. 第一句提出反方观点。
2. 第二句承认其严肃性，但限制其结论力。
3. 第三句构造条件推理，说明单一指标可能低估社会价值。
4. 第四句给出作者的核心论证位置：不是否认激励效应，而是追问社会计量什么。

### 句群拆解

- `A common objection... is that...` 建立“反对意见的内容”。
- `serious, but...` 是让步转折：承认对方问题，但不同意它终结争论。
- `If... then...` 中三个动词 `leave, invest, care` 平行，列出可能收益。
- `depends not on..., but on...` 明确论证依赖的不是否认，而是评价框架。

### GRE/PhD 级训练

### 高阶训练 1
**高阶语境：学术科研**

本段如何处理反方观点？请说明它不是简单反驳，而是重新界定问题。

:::solution 查看解析
作者先承认反方观点严肃，然后指出它不能终结问题，因为工作时长只是经济参与的一个维度。随后作者把问题从“是否削弱工作激励”改成“社会选择计入哪些影响”。这是一种重构评价框架的论证。
:::

### 高阶训练 2
**高阶语境：学术科研**

第三句为什么说 `a narrow measure of hours worked might understate the policy's social value`？

:::solution 查看解析
因为基本收入可能带来的价值不只体现在工作小时数上，还可能体现在离开有害工作、投资培训、照顾家人等方面。如果只计算工作小时，就会漏掉这些社会价值。
:::

### 高阶训练 3
**高阶语境：真实生活**

模仿 `depends not on..., but on...` 写一句：评价一次休息不是看有没有少做事，而是看是否恢复了长期注意力。

:::solution 查看解析
可以写：`The value of a break depends not on whether it reduces the number of tasks completed that day, but on whether it restores attention over the longer term.` 结构明确排除短期数量指标，转向长期注意力。
:::
""",
}


def main() -> int:
    changed = 0
    for filename, block in BLOCKS.items():
        path = CONTENT_DIR / filename
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        if ANCHOR not in text:
            raise RuntimeError(f"{filename}: anchor not found")
        text = text.replace(ANCHOR, "\n\n" + block.strip() + "\n" + ANCHOR, 1)
        path.write_text(text, encoding="utf-8", newline="\n")
        changed += 1
    print(f"Inserted advanced reading blocks into {changed} modules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
