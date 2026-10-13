"""Build the public English practice plan; never embed personal learner records."""
from pathlib import Path
import json
from html import escape
ROOT=Path(__file__).resolve().parents[1]
weeks=json.loads((ROOT/'content/english_daily_plan.json').read_text())
source=(ROOT/'docs/english.html').read_text()
nav=source[source.index('    <div class="topbar">'):source.index('    <div class="page-head">')]
parts=[]
for week in weeks:
 cards=[]
 for d in week['days']:
  cards.append(f'''<details class="day" id="day-{d['day']}"><summary><span class="day-number">DAY {d['day']:02}</span> {escape(d['title'])}</summary><div class="day-body"><p><strong>听力 · 20 分钟</strong>：<a href="{week['audio']}">打开本周 {week['level']} 音频与逐字稿</a>。取 2—3 分钟或完整短音频，按下方听力流程练习。复盘日换用同级新材料。</p><p><strong>口头表达 · 15 分钟</strong>：{escape(d['speak'])} 先录一遍，只修三处，再录一遍。</p><p><strong>读写 · 15 分钟</strong>：{escape(d['write'])} 较长材料只读一段；写不满不补时，记录实际完成量。</p><p><strong>回忆 · 10 分钟</strong>：选三个实用表达，不看笔记各造一句新句子；复习昨天的三个表达。</p><label class="done"><input type="checkbox" data-day="{d['day']}"> 我已完成今天的练习与复盘</label></div></details>''')
 parts.append(f'''<section id="week-{week['week']}" class="week"><p class="eyebrow">WEEK {week['week']:02}</p><h2>{week['title']}</h2><p>{week['description']}</p>{''.join(cards)}</section>''')
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>每天一小时英语 · 四周行动计划 | math.bozhanli.com</title><meta name="description" content="面向工作沟通、研究讨论与博士学习的四周英语计划：每天60分钟，28天任务，听力材料、表达模板与复盘标准。"><link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/english-plan.css"><script defer src="assets/english-plan.js"></script></head><body><div class="shell page">'''+nav+'''
<main id="main"><header class="plan-hero"><p class="eyebrow">ENGLISH IN PRACTICE · 28 DAYS</p><h1>让英语用得起来。<br>从每天一小时开始。</h1><p class="lead">围绕工作沟通、研究讨论与博士生活，把听懂的内容变成自己能说、能写的话。</p><p>以 C1 为长期方向，这四周用来建立练习方式与观察进步，不承诺四周达到 C1，也不代替正式等级测评。</p><div class="plan-actions"><a class="primary" href="#day-1">开始第 1 天</a><a href="#routine">先看 60 分钟怎么用</a><a href="english.html">返回英语知识库</a></div></header>
<section class="progress-panel" aria-label="学习进度"><strong id="progress-label" aria-live="polite">完成记录：0 / 28 天</strong><progress id="progress" max="28" value="0">0/28</progress><p id="storage-note">只在当前浏览器保存完成记录；不上传，不跨设备同步。清除浏览器数据会丢失记录。</p><noscript><p>未启用 JavaScript：所有任务仍可阅读，完成记录不会保存。</p></noscript></section>
<nav class="week-nav" aria-label="四周导航"><a href="#week-1">01 工作与经历</a><a href="#week-2">02 解释研究</a><a href="#week-3">03 互动澄清</a><a href="#week-4">04 新材料讨论</a></nav>
<section class="page-section" id="routine"><h2>每天 60 分钟，只围绕一个主题</h2><div class="routine-grid"><div><b>20′</b><h3>精听</h3><p>关原文听 → 对照找漏听 → 再关原文听。</p></div><div><b>15′</b><h3>开口</h3><p>先自己说 → 只改三处 → 重新表达。</p></div><div><b>15′</b><h3>读写</h3><p>读一个段落 → 写自己的解释或回复。</p></div><div><b>10′</b><h3>回忆</h3><p>每天三个表达，放进新的真实情境。</p></div></div><p>第 1 天保存一段未经润色的录音和初稿作为起点。用手机或电脑自己的录音工具；本页不录音、不收集个人练习内容。录音和笔记留在自己的设备。</p></section>
<section class="page-section"><h2>听不懂时，先找原因</h2><ol><li>前 5 分钟：不看原文听两遍，记录主题与两条细节。</li><li>接着 7 分钟：对照逐字稿，标出“词不认识”“认识但没听出”“听见了但没跟上逻辑”。</li><li>接着 5 分钟：只反复听最难的两三句，暂停模仿重音和停顿。</li><li>最后 3 分钟：关闭原文重听，用三句话总结，不要求逐词翻译。</li></ol><p>初听连主题都抓不到，就换 <a href="https://learnenglish.britishcouncil.org/free-resources/listening/b1">B1 材料</a>或更短片段；听两遍能概括主题和关键细节，再试 <a href="https://learnenglish.britishcouncil.org/free-resources/listening/b2">B2 材料</a>。周次不强制升级。链接材料来自 British Council，含音频、逐字稿与练习；请在来源网站使用，不在本站复制音频或整篇文本。</p></section>
'''+''.join(parts)+'''
<section class="page-section" id="phrases"><h2>先把这八个表达用熟</h2><div class="phrase-grid"><p><strong>The main problem is that…</strong><br>说明研究或工作问题。</p><p><strong>The idea behind this method is…</strong><br>先讲直觉，再讲细节。</p><p><strong>Compared with the baseline, …</strong><br>比较时说明指标与条件。</p><p><strong>One limitation is that…</strong><br>准确说明适用边界。</p><p><strong>Could you rephrase the last part?</strong><br>请对方换一种说法。</p><p><strong>Do you mean that…?</strong><br>主动核对理解。</p><p><strong>Let me check that I understood you correctly.</strong><br>总结后让对方确认。</p><p><strong>I would need to check the exact formula.</strong><br>不确定时先说明，再查证。</p></div><p>每天选三个与你当日任务相关的表达，用自己的内容填充。能自然使用简单表达，比记住一长串生词更适合当前任务。</p></section>
<section class="page-section"><h2>让 AI 做反馈，不替你完成第一遍</h2><p>先说或写，再把原稿交给 AI。建议复制下面的要求：</p><blockquote>保留我的意思和语气，只指出最影响理解的三处，并解释原因。给我自然、适合口头表达的修改，不要升级成论文腔，不要添加我没有提供的事实。然后每次问一个追问，让我用新内容再次使用这些表达。只有文字时，不要判断我的发音或真实听力等级。</blockquote><p>如果只是把一段文稿润色得漂亮，还不能说明你已经会表达。第二天换个问题再说一次。</p></section>
<section class="page-section" id="review"><h2>每周复盘：看能力，不只看打卡</h2><p>第 7、14、21、28 天替换当天练习内容，总时间仍为 60 分钟。记录以下四项，不折算为 CEFR 等级：</p><ul><li><strong>听懂：</strong>新材料不看原文时，能否说出主题和两条准确细节？</li><li><strong>讲清：</strong>两分钟表达是否有主题、例子和结尾？是否因为找词多次放弃句子？</li><li><strong>互动：</strong>能否澄清问题并继续回应？独白练习不能代替真实互动测评。</li><li><strong>迁移：</strong>昨天纠正的表达，今天换情境后还能否正确使用？</li></ul><details><summary>展开可复制的复盘模板</summary><pre>日期 / 任务：
材料与片段：
不看原文听到的主题与细节：
三处卡点及原因：
今天能独立使用的三个表达：
重录后改善了什么：
下一次只调整哪一项：</pre></details><p>下轮调整：听力仍常丢主题，就缩短片段；能听懂但说不出，保留主题、增加重述；只会熟稿，就增加陌生追问。每次只调整一个难度维度。</p></section>
<section class="page-section"><h2>知识库：遇到问题再查</h2><ul><li><a href="notes/10-english/01-grammar-reading/01-clause-skeletons-zh.html">句子主干</a> · 说不清谁做什么时。</li><li><a href="notes/10-english/01-grammar-reading/02-tense-aspect-zh.html">时态与体</a> · 叙述经历与当前状态时。</li><li><a href="notes/10-english/01-grammar-reading/03-modality-counterfactuals-zh.html">情态与反事实</a> · 区分事实、可能与假设时。</li><li><a href="notes/10-english/01-grammar-reading/13-stance-evidentiality-zh.html">立场与证据</a> · 解释研究结论时。</li><li><a href="notes/10-english/01-grammar-reading/09-comparison-parallelism-ellipsis-zh.html">比较、平行与省略</a> · 比较方法时。</li><li><a href="notes/10-english/01-grammar-reading/14-academic-argument-zh.html">学术论证</a> · 提出问题、整理证据时。</li></ul><p>不必先完成全部语法模块。每次查一个当前真正用得上的知识点，再回到自己的句子。</p></section>
<footer class="page-section"><p>课程定位：向 C1 逐步前进的起步计划。<a href="https://www.coe.int/en/web/common-european-framework-reference-languages/table-1-cefr-3.3-common-reference-levels-global-scale">CEFR 官方等级说明</a>。听力外链核对日期：2026-09-20；若材料变动，可回同级目录选择有逐字稿的短材料。</p><a href="english.html">返回英语首页</a></footer></main></div></body></html>'''
(ROOT/'docs/english-plan.html').write_text(html)
print('Built english-plan.html: 4 weeks, 28 daily tasks')
