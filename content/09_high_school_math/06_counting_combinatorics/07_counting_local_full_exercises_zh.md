# 计数原理与排列组合：考点 33-35 全量本地题库

这一页把本地一轮复习资料中考点 33 到考点 35 的练习题按原考点整理出来。题干中的公式、图形和原 Word 图片会一起呈现；解析版内容折叠在“查看解析版原文”里，适合课后抽题、限时训练和查漏补缺。

返回专题首页：[计数原理与排列组合](./README.md)。配套训练：[计数原理与排列组合：分层训练题库](./06_counting_expression_drills_zh.md)。

## 使用说明

1. 这页是本地资料池，不建议第一次学习时直接通刷。
2. 课堂上先用讲义建立分类、分步、有序、无序和二项式通项，再按考点从这里抽题。
3. 学生讲题时必须说出：对象是什么、先分类还是先分步、是否有序、有没有重复或遗漏。

## 考点 33：两个计数原理

本组来自 `考点33 两个计数原理（练习）（原卷版）.docx`；原卷共抽取 14 道题，解析版原始抽取 14 道，可对齐显示 14 道。

### 题 1（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．甲、乙、丙、丁、戊、己六人按一定的顺序依次抽奖，要求甲排在乙前面，丙与丁不相邻且均不排在最后，则抽奖的顺序有（    ）</p>
<p class="local-docx-line">A．72种B．144种C．360种D．720种</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．甲、乙、丙、丁、戊、己六人按一定的顺序依次抽奖，要求甲排在乙前面，丙与丁不相邻且均不排在最后，则抽奖的顺序有（    ）</p>
<p class="local-docx-line">A．72种B．144种C．360种D．720种</p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】第一步先排甲、乙、戊、己，甲排在乙前面，则有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-002-a9081757d3.png" alt="本地解析几何资料图片" width="608" height="1056">种，第二步再将丙与丁插空到第一步排好的序列中，但注意到丙与丁均不排在最后，故有4个空可选，所以有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-003-281d093430.png" alt="本地解析几何资料图片" width="512" height="608">中插空方法，所以根据分步乘法计数原理有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-004-dc20862636.png" alt="本地解析几何资料图片" width="1984" height="1056">种.故选：B.</p>
</div>
:::

:::

### 题 2（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．12名同学合影，站成前排4人后排8人，现摄影师要从后排8人中抽2人调整到前排，若其他人的相对顺序不变，则不同调整方法的总数是( )</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-002-fc036d75b8.png" alt="本地解析几何资料图片" width="928" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-003-0902967d53.png" alt="本地解析几何资料图片" width="896" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-004-818d125006.png" alt="本地解析几何资料图片" width="928" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-005-8ef22b29e3.png" alt="本地解析几何资料图片" width="928" height="608"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．12名同学合影，站成前排4人后排8人，现摄影师要从后排8人中抽2人调整到前排，若其他人的相对顺序不变，则不同调整方法的总数是( )</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-005-fc036d75b8.png" alt="本地解析几何资料图片" width="928" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-006-0902967d53.png" alt="本地解析几何资料图片" width="896" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-007-818d125006.png" alt="本地解析几何资料图片" width="928" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-008-8ef22b29e3.png" alt="本地解析几何资料图片" width="928" height="608"></p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】第一步从后排8人中选2人有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-009-caeb645a87.png" alt="本地解析几何资料图片" width="512" height="608">种方法，第二步6人前排排列，先排列选出的2人有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-010-21b6f5330f.png" alt="本地解析几何资料图片" width="512" height="608">种方法，再排列其余4人只有1种方法，因此所有的方法总数的种数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-011-818d125006.png" alt="本地解析几何资料图片" width="928" height="608"></p>
</div>
:::

:::

### 题 3（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．受新冠肺炎疫情影响，某学校按上级文件指示，要求错峰放学，错峰有序吃饭.高三年级一层楼六个班排队，甲班必须排在前三位，且丙班、丁班必须排在一起，则这六个班排队吃饭的不同安排方案共有（    ）</p>
<p class="local-docx-line">A．240种B．120种C．188种D．156种</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．受新冠肺炎疫情影响，某学校按上级文件指示，要求错峰放学，错峰有序吃饭.高三年级一层楼六个班排队，甲班必须排在前三位，且丙班、丁班必须排在一起，则这六个班排队吃饭的不同安排方案共有（    ）</p>
<p class="local-docx-line">A．240种B．120种C．188种D．156种</p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】根据题意，按甲班位置分3 种情况讨论：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-012-c71ac915a6.png" alt="本地解析几何资料图片" width="3968" height="1088"></p>
<p class="local-docx-line">（1）甲班排在第一位，丙班和丁班排在一起的情况有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-013-9fdc252075.png" alt="本地解析几何资料图片" width="1280" height="608">种，将剩余的三个班全排列，安排到剩下的3个位置，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-014-90153900c0.png" alt="本地解析几何资料图片" width="1088" height="608">种情况，此时有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-015-cae382f14d.png" alt="本地解析几何资料图片" width="1536" height="448">种安排方案；</p>
<p class="local-docx-line">（2）甲班排在第二位，丙班和丁班在一起的情况有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-016-47fd723500.png" alt="本地解析几何资料图片" width="1280" height="608">种，将剩下的三个班全排列，安排到剩下的三个位置，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-017-90153900c0.png" alt="本地解析几何资料图片" width="1088" height="608">种情况，此时有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-018-c950e81112.png" alt="本地解析几何资料图片" width="1536" height="448">种安排方案；</p>
<p class="local-docx-line">（3）甲班排在第三位，丙班和丁班排在一起的情况有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-019-47fd723500.png" alt="本地解析几何资料图片" width="1280" height="608">种，将剩下的三个班全排列，安排到剩下的三个位置，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-020-90153900c0.png" alt="本地解析几何资料图片" width="1088" height="608">种情况，此时有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-021-c950e81112.png" alt="本地解析几何资料图片" width="1536" height="448">种安排方案；</p>
<p class="local-docx-line">由加法计数原理可知共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-022-2c4f59ad97.png" alt="本地解析几何资料图片" width="2496" height="448">种方案，故选：B</p>
</div>
:::

:::

### 题 4（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．用数字1，2，3，4，5组成没有重复数字的数，问</p>
<p class="local-docx-line">（1）能够组成多少个五位奇数？</p>
<p class="local-docx-line">（2）能够组成多少个正整数？</p>
<p class="local-docx-line">（3）能够组成多少个大于40000的正整数？</p>
<p class="local-docx-line">【题组二 分组分配问题】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．用数字1，2，3，4，5组成没有重复数字的数，问</p>
<p class="local-docx-line">（1）能够组成多少个五位奇数？</p>
<p class="local-docx-line">（2）能够组成多少个正整数？</p>
<p class="local-docx-line">（3）能够组成多少个大于40000的正整数？</p>
<p class="local-docx-line">【答案】（1）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-023-d787c290f8.png" alt="本地解析几何资料图片" width="448" height="416">；（2）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-024-6da18ce52b.png" alt="本地解析几何资料图片" width="672" height="448">；（3）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-025-9cf7ccb87f.png" alt="本地解析几何资料图片" width="512" height="448">；</p>
<p class="local-docx-line">【解析】（1）首先排最个位数字，从1、3、5中选1个数排在个位有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-026-84da681afd.png" alt="本地解析几何资料图片" width="1056" height="608">种，其余4个数全排列有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-027-81aaf5564b.png" alt="本地解析几何资料图片" width="1312" height="608">种，按照分步乘法计数原理可得有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-028-d660ff595f.png" alt="本地解析几何资料图片" width="1664" height="608">个五位奇数；</p>
<p class="local-docx-line">（2）根据题意，</p>
<p class="local-docx-line">若组成一位数，有5种情况，即可以有5个一位数；</p>
<p class="local-docx-line">若组成两位数，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-029-e2bb3273f4.png" alt="本地解析几何资料图片" width="1312" height="608">种情况，即可以有20个两位数；</p>
<p class="local-docx-line">若组成三位数，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-030-44a1daf887.png" alt="本地解析几何资料图片" width="1280" height="608">种情况，即可以有60个三位数；</p>
<p class="local-docx-line">若组成四位数，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-031-18f12ce589.png" alt="本地解析几何资料图片" width="1472" height="608">种情况，即可以有120个四位数；</p>
<p class="local-docx-line">若组成五位数，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-032-726fcb168c.png" alt="本地解析几何资料图片" width="1440" height="608">种情况，即可以有120个五位数；</p>
<p class="local-docx-line">则可以有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-033-37c66793df.png" alt="本地解析几何资料图片" width="4000" height="416">个正整数；</p>
<p class="local-docx-line">（3）根据题意，若组成的数字比40000大的正整数，其首位数字为5或4，有2种情况；</p>
<p class="local-docx-line">在剩下的4个数，安排在后面四位，共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-034-c51d0abe76.png" alt="本地解析几何资料图片" width="1696" height="608">种情况，</p>
<p class="local-docx-line">则有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-035-9cf7ccb87f.png" alt="本地解析几何资料图片" width="512" height="448">个比40000大的正整数；</p>
<p class="local-docx-line">【题组二 分组分配问题】</p>
</div>
:::

:::

### 题 5（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1.某学校有5位教师参加某师范大学组织的暑期骨干教师培训，现有5个培训项目，每位教师可任意选择其中一个项目进行培训，则恰有两个培训项目没有被这5位教师中的任何一位教师选择的情况数为          。</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1.某学校有5位教师参加某师范大学组织的暑期骨干教师培训，现有5个培训项目，每位教师可任意选择其中一个项目进行培训，则恰有两个培训项目没有被这5位教师中的任何一位教师选择的情况数为          。</p>
<p class="local-docx-line">【答案】1500</p>
<p class="local-docx-line">【解析】分两步：第一步：从5个培训项目中选取3个，共C种情况；</p>
<p class="local-docx-line">第二步：5位教师分成两类：①选择选出的3个培训项目的教师人数分别为1人，1人，3人，共种情况；②选择选出的3个培训项目的教师人数分别为1人，2人，2人，共种情况.故选择情况数为CA＝1 500(种).</p>
</div>
:::

:::

### 题 6（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．现有4个不同的球，和4个不同的盒子，把球全部放入盒内．</p>
<p class="local-docx-line">（1）共有多少种不同的方法？</p>
<p class="local-docx-line">（2）若每个盒子不空，共有多少种不同的方法？</p>
<p class="local-docx-line">（3）若恰有一个盒子不放球，共有多少种放法？</p>
<p class="local-docx-line">（4）若恰有两个盒子不放球，共有多少种放法？</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．现有4个不同的球，和4个不同的盒子，把球全部放入盒内．</p>
<p class="local-docx-line">（1）共有多少种不同的方法？</p>
<p class="local-docx-line">（2）若每个盒子不空，共有多少种不同的方法？</p>
<p class="local-docx-line">（3）若恰有一个盒子不放球，共有多少种放法？</p>
<p class="local-docx-line">（4）若恰有两个盒子不放球，共有多少种放法？</p>
<p class="local-docx-line">【答案】（1）256  （2）24  （3）144 （4）84</p>
<p class="local-docx-line">【解析】（1）将4个不同的球放入4个不同的盒子，则共有44=256种不同的放法，</p>
<p class="local-docx-line">（2）将4个不同的球放入4个不同的盒子，若没个盒子不空，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-036-3f11812788.png" alt="本地解析几何资料图片" width="512" height="608">=24种不同的放法，</p>
<p class="local-docx-line">（3）将4个不同的球放入4个不同的盒子，恰有一个盒子不放球，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-037-c5357a9ae8.png" alt="本地解析几何资料图片" width="1280" height="608">=144种不同的放法，</p>
<p class="local-docx-line">（4）将4个不同的球放入4个不同的盒子，恰有两个盒子不放球，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-038-bdf23050ee.png" alt="本地解析几何资料图片" width="512" height="608">（<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-039-e35a762988.png" alt="本地解析几何资料图片" width="1664" height="608">）=84种不同的放法，</p>
</div>
:::

:::

### 题 7（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．有6本不同的书，在下列不同的条件下，各有多少种不同的分法？</p>
<p class="local-docx-line">（1）分给甲､乙､丙三人，其中一个人1本，一个人2本，一个人3本；</p>
<p class="local-docx-line">（2）分成三组，一组4本，另外两组各1本；</p>
<p class="local-docx-line">（3）甲得1本，乙得1本，丙得4本.</p>
<p class="local-docx-line">【题组三 染色问题】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．有6本不同的书，在下列不同的条件下，各有多少种不同的分法？</p>
<p class="local-docx-line">（1）分给甲､乙､丙三人，其中一个人1本，一个人2本，一个人3本；</p>
<p class="local-docx-line">（2）分成三组，一组4本，另外两组各1本；</p>
<p class="local-docx-line">（3）甲得1本，乙得1本，丙得4本.</p>
<p class="local-docx-line">【答案】（1）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-040-0631f4f467.png" alt="本地解析几何资料图片" width="672" height="448">种；（2）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-041-b55d0f52c7.png" alt="本地解析几何资料图片" width="448" height="448">种；（3）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-042-5371f9c099.png" alt="本地解析几何资料图片" width="480" height="448">种.</p>
<p class="local-docx-line">【解析】（1）先将6本不同的书分成1本，2本，3本共3组，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-043-5bbb9c3ea2.png" alt="本地解析几何资料图片" width="1280" height="608">种，</p>
<p class="local-docx-line">再将3组分配给3人有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-044-e284781e5c.png" alt="本地解析几何资料图片" width="480" height="608">种，故共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-045-3e0ac6d00f.png" alt="本地解析几何资料图片" width="2656" height="608">种；</p>
<p class="local-docx-line">（2）只需从6本中选4本一组，其余2本为2组，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-046-b15b612f91.png" alt="本地解析几何资料图片" width="1411" height="670">种；</p>
<p class="local-docx-line">（3）分步处理，先从从6本中选4本给丙，其余2本分给甲乙各一本，</p>
<p class="local-docx-line">即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-047-89c5418303.png" alt="本地解析几何资料图片" width="1760" height="608">种.</p>
<p class="local-docx-line">【题组三 染色问题】</p>
</div>
:::

:::

### 题 8（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．现有4种不同颜色要对如图所示的四个部分进行着色，要求有公共边界的两部分不能用同一种颜色，则不同的着色方法共有 （　　）</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-006-8c7f1cdbbb.png" alt="本地解析几何资料图片" width="78" height="78"></p>
<p class="local-docx-line">A．144种B．72种C．64种D．84种</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．现有4种不同颜色要对如图所示的四个部分进行着色，要求有公共边界的两部分不能用同一种颜色，则不同的着色方法共有 （　　）</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-048-8c7f1cdbbb.png" alt="本地解析几何资料图片" width="78" height="78"></p>
<p class="local-docx-line">A．144种B．72种C．64种D．84种</p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】根据题意，分3步进行分析：①先给最上面“金”着色，有4种结果，②再给“榜”着色，有3种结果，③给“题”着色，若其与“榜”同色，则给“名”着色，有3种结果；若其与“榜”不同色，则给“榜”着色有2种结果，然后给“名”着色，有2种结果，</p>
<p class="local-docx-line">根据分步计数原理知共有4×3×（3+2×2）=84种结果，故选D</p>
</div>
:::

:::

### 题 9（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．如图,用6种不同的颜色把图中A,B,C,D四块区域涂色分开,若相邻区域不能涂同一种颜色,则不同涂法的种数为(　　)</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct33-q-007-d90acd6269.png" alt="本地解析几何资料图片" width="277" height="156"></div>
<p class="local-docx-line">A．400B．460C．480D．496</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．如图,用6种不同的颜色把图中A,B,C,D四块区域涂色分开,若相邻区域不能涂同一种颜色,则不同涂法的种数为(　　)</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct33-a-049-d90acd6269.png" alt="本地解析几何资料图片" width="277" height="156"></div>
<p class="local-docx-line">A．400B．460C．480D．496</p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】只用三种颜色涂色时，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-050-e4e547cd0c.png" alt="本地解析几何资料图片" width="2560" height="608">种方法，</p>
<p class="local-docx-line">用四种颜色涂色时，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-051-f489482c28.png" alt="本地解析几何资料图片" width="2656" height="608">种方法，</p>
<p class="local-docx-line">根据分类计数原理得不同涂法的种数为120+360=480.故答案为：C.</p>
</div>
:::

:::

### 题 10（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．如图，用四种不同的颜色给三棱柱<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-008-7242fedcaa.png" alt="本地解析几何资料图片" width="2272" height="448">的六个顶点涂色，要求每个点涂一种颜色．若每个底面的顶点涂色所使用的颜色不相同，则不同的涂色方法共有________种；若每条棱的两个端点涂不同的颜色，则不同的涂色方法共有________种．</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-009-601b4bb299.png" alt="本地解析几何资料图片" width="194" height="104"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．如图，用四种不同的颜色给三棱柱<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-052-7242fedcaa.png" alt="本地解析几何资料图片" width="2272" height="448">的六个顶点涂色，要求每个点涂一种颜色．若每个底面的顶点涂色所使用的颜色不相同，则不同的涂色方法共有________种；若每条棱的两个端点涂不同的颜色，则不同的涂色方法共有________种．</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-053-601b4bb299.png" alt="本地解析几何资料图片" width="194" height="104"></p>
<p class="local-docx-line">【答案】576    264</p>
<p class="local-docx-line">【解析】（1）由题得每个底面的顶点涂色所使用的颜色不相同，则不同的涂色方法共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-054-ca099835ec.png" alt="本地解析几何资料图片" width="1856" height="608">；</p>
<p class="local-docx-line">（2）若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-055-c1e3bc930d.png" alt="本地解析几何资料图片" width="448" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-056-db8428fc53.png" alt="本地解析几何资料图片" width="448" height="384">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-057-5680a3e25f.png" alt="本地解析几何资料图片" width="384" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-058-8c235f27f1.png" alt="本地解析几何资料图片" width="384" height="448">用四种颜色，则有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-059-81aaf5564b.png" alt="本地解析几何资料图片" width="1312" height="608">；</p>
<p class="local-docx-line">若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-060-c1e3bc930d.png" alt="本地解析几何资料图片" width="448" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-061-db8428fc53.png" alt="本地解析几何资料图片" width="448" height="384">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-062-5680a3e25f.png" alt="本地解析几何资料图片" width="384" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-063-8c235f27f1.png" alt="本地解析几何资料图片" width="384" height="448">用三种颜色，则有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-064-2118794e0d.png" alt="本地解析几何资料图片" width="4256" height="608">；</p>
<p class="local-docx-line">若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-065-c1e3bc930d.png" alt="本地解析几何资料图片" width="448" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-066-db8428fc53.png" alt="本地解析几何资料图片" width="448" height="384">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-067-5680a3e25f.png" alt="本地解析几何资料图片" width="384" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-068-8c235f27f1.png" alt="本地解析几何资料图片" width="384" height="448">用两种颜色，则有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-069-82e341a754.png" alt="本地解析几何资料图片" width="2336" height="608">.</p>
<p class="local-docx-line">所以共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-070-50a630aff5.png" alt="本地解析几何资料图片" width="2400" height="448">264种．</p>
<p class="local-docx-line">故答案为：①576；②264.</p>
</div>
:::

:::

### 题 11（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．如图，用四种不同颜色给图中的A,B,C,D,E,F六个点涂色，要求每个点涂一种颜色，且图中每条线段的两个端点涂不同颜色，则不同的涂色方法用</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct33-q-010-fb65c4cd8f.png" alt="本地解析几何资料图片" width="156" height="167"></div>
<p class="local-docx-line">A．288种B．264种C．240种D．168种</p>
<p class="local-docx-line">【题组四 综合运用】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．如图，用四种不同颜色给图中的A,B,C,D,E,F六个点涂色，要求每个点涂一种颜色，且图中每条线段的两个端点涂不同颜色，则不同的涂色方法用</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct33-a-071-fb65c4cd8f.png" alt="本地解析几何资料图片" width="156" height="167"></div>
<p class="local-docx-line">A．288种B．264种C．240种D．168种</p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】</p>
<p class="local-docx-line">先分步再排列</p>
<p class="local-docx-line">先涂点E，有4种涂法，再涂点B，有两种可能：</p>
<p class="local-docx-line">(1)B与E相同时，依次涂点F，C，D，A，涂法分别有3，2，2，2种；</p>
<p class="local-docx-line">(2)B与E不相同时有3种涂法，再依次涂F、C、D、A点，涂F有2种涂法，涂C点时又有两种可能：</p>
<p class="local-docx-line">（2.1）C与E相同，有1种涂法，再涂点D，有两种可能：</p>
<p class="local-docx-line">①D与B相同，有1种涂法，最后涂A有2种涂法；</p>
<p class="local-docx-line">②D与B不相同，有2种涂法，最后涂A有1种涂法．</p>
<p class="local-docx-line">（2.2）C与E不相同，有1种涂法，再涂点D，有两种可能：</p>
<p class="local-docx-line">①D与B相同，有1种涂法，最后涂A有2种涂法；</p>
<p class="local-docx-line">②D与B不相同，有2种涂法，最后涂A有1种涂法．</p>
<p class="local-docx-line">所以不同的涂色方法有</p>
<p class="local-docx-line">4×{3×2×2×2+3×2×[1×(1×2+1×2)+1×(1×2+1×1)]}=4×(24+42)=264．</p>
<p class="local-docx-line">【题组四 综合运用】</p>
</div>
:::

:::

### 题 12（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．若4名学生报名参加数学、物理、化学兴趣小组，每人选报1项，则不同的报名方式有（    ）</p>
<p class="local-docx-line">A．34种B．43种C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-011-34745dccb3.png" alt="本地解析几何资料图片" width="512" height="608">种D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-012-6437008cae.png" alt="本地解析几何资料图片" width="544" height="608">种</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．若4名学生报名参加数学、物理、化学兴趣小组，每人选报1项，则不同的报名方式有（    ）</p>
<p class="local-docx-line">A．34种B．43种C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-072-34745dccb3.png" alt="本地解析几何资料图片" width="512" height="608">种D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-073-6437008cae.png" alt="本地解析几何资料图片" width="544" height="608">种</p>
<p class="local-docx-line">【答案】A</p>
<p class="local-docx-line">【解析】4名学生，每人有三种可选方案，根据分步计数原理，4人共有34种方法.</p>
<p class="local-docx-line">故选：A.</p>
</div>
:::

:::

### 题 13（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．中国古代的四书是指：《大学》、《中庸》、《论语》、《孟子》，甲、乙、丙、丁<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-013-3c34fd73c6.png" alt="本地解析几何资料图片" width="320" height="416">名同学从中各选一书进行研读，已知四人选取的书恰好互不相同，且甲没有选《中庸》，乙和丙都没有选《论语》，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-q-014-3c34fd73c6.png" alt="本地解析几何资料图片" width="320" height="416">名同学所有可能的选择有______种.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．中国古代的四书是指：《大学》、《中庸》、《论语》、《孟子》，甲、乙、丙、丁<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-074-3c34fd73c6.png" alt="本地解析几何资料图片" width="320" height="416">名同学从中各选一书进行研读，已知四人选取的书恰好互不相同，且甲没有选《中庸》，乙和丙都没有选《论语》，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-075-3c34fd73c6.png" alt="本地解析几何资料图片" width="320" height="416">名同学所有可能的选择有______种.</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-076-78e1107976.png" alt="本地解析几何资料图片" width="448" height="448"></p>
<p class="local-docx-line">【解析】分以下两种情况讨论：</p>
<p class="local-docx-line">（1）乙、丙两人中没有一人选《中庸》，则乙、丙两人在《大学》、《孟子》中各选一书，则甲只能选《大学》，丁只能选《论语》，此时选法种数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-077-764290914c.png" alt="本地解析几何资料图片" width="512" height="608">种；</p>
<p class="local-docx-line">（2）乙、丙两人中有一人选《中庸》，则另一人可在《大学》、《孟子》选择一书，甲、丁两人选书时没有限制，此时选法种数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-078-c4fca1a22c.png" alt="本地解析几何资料图片" width="1248" height="608">.</p>
<p class="local-docx-line">综上所述，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-079-3c34fd73c6.png" alt="本地解析几何资料图片" width="320" height="416">名同学所有可能的选择种数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-080-bb51494443.png" alt="本地解析几何资料图片" width="2784" height="608">.</p>
<p class="local-docx-line">故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-081-78e1107976.png" alt="本地解析几何资料图片" width="448" height="448">.</p>
</div>
:::

:::

### 题 14（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．某学校周三要排语文、数学、英语、物理、化学、体育共六节课，有__________种不同的排法，若体育课既不能与语文相邻，也不能与数学相邻，有__________种不同的排法．（用具体数字作答）</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．某学校周三要排语文、数学、英语、物理、化学、体育共六节课，有__________种不同的排法，若体育课既不能与语文相邻，也不能与数学相邻，有__________种不同的排法．（用具体数字作答）</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-082-6934187f88.png" alt="本地解析几何资料图片" width="704" height="448">    <img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-083-eb4c3b54d1.png" alt="本地解析几何资料图片" width="704" height="448"></p>
<p class="local-docx-line">【解析】某学校周三要排语文、数学、英语、物理、化学、体育共六节课，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-084-2d80b317fd.png" alt="本地解析几何资料图片" width="1504" height="608">种不同的排法当体育在第一节时，在第三，四，五，六节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-085-9f9fdb7031.png" alt="本地解析几何资料图片" width="2912" height="608">种不同的排法</p>
<p class="local-docx-line">当体育在第二节时，在第四，五，六节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-086-7dd962c57d.png" alt="本地解析几何资料图片" width="2944" height="608">种不同的排法</p>
<p class="local-docx-line">当体育在第三节时，在第一，五，六节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-087-7dd962c57d.png" alt="本地解析几何资料图片" width="2944" height="608">种不同的排法</p>
<p class="local-docx-line">当体育在第四节时，在第一，二，六节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-088-7dd962c57d.png" alt="本地解析几何资料图片" width="2944" height="608">种不同的排法</p>
<p class="local-docx-line">当体育在第五节时，在第一，二，三节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-089-7dd962c57d.png" alt="本地解析几何资料图片" width="2944" height="608">种不同的排法</p>
<p class="local-docx-line">当体育在第六节时，在第一，二，三，四节中选2节排语文和数学，其余排英语、物理、化学，则共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-090-9f9fdb7031.png" alt="本地解析几何资料图片" width="2912" height="608">种不同的排法</p>
<p class="local-docx-line">则若体育课既不能与语文相邻，也不能与数学相邻，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-091-58841b5fc2.png" alt="本地解析几何资料图片" width="3136" height="448">种不同的排法</p>
<p class="local-docx-line">故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-092-6934187f88.png" alt="本地解析几何资料图片" width="704" height="448">；<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct33-a-093-eb4c3b54d1.png" alt="本地解析几何资料图片" width="704" height="448"></p>
</div>
:::

:::

## 考点 34：排列、组合

本组来自 `考点34 排列、组合（练习） （原卷版）.docx`；原卷共抽取 11 道题，解析版原始抽取 11 道，可对齐显示 11 道。

### 题 15（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-002-fd818c16cf.png" alt="本地解析几何资料图片" width="1376" height="544">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-003-a1cf5aafda.png" alt="本地解析几何资料图片" width="416" height="352">的值为（    ）</p>
<p class="local-docx-line">A．5B．6C．7D．8</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-002-fd818c16cf.png" alt="本地解析几何资料图片" width="1376" height="544">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-003-a1cf5aafda.png" alt="本地解析几何资料图片" width="416" height="352">的值为（    ）</p>
<p class="local-docx-line">A．5B．6C．7D．8</p>
<p class="local-docx-line">【答案】A</p>
<p class="local-docx-line">【解析】由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-004-fd818c16cf.png" alt="本地解析几何资料图片" width="1376" height="544">，得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-005-f80540992a.png" alt="本地解析几何资料图片" width="7552" height="512">，且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-006-c69ed0facd.png" alt="本地解析几何资料图片" width="960" height="448"></p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-007-579eb1af6c.png" alt="本地解析几何资料图片" width="2880" height="512">即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-008-1d35f7e222.png" alt="本地解析几何资料图片" width="3968" height="544">或<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-009-8fa7400019.png" alt="本地解析几何资料图片" width="1984" height="512">舍去）.故选：A</p>
</div>
:::

:::

### 题 16（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-004-68f7d6868e.png" alt="本地解析几何资料图片" width="2176" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-005-1b662190ae.png" alt="本地解析几何资料图片" width="670" height="388">（    ）</p>
<p class="local-docx-line">A．5B．7C．10D．14</p>
<p class="local-docx-line">.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-010-68f7d6868e.png" alt="本地解析几何资料图片" width="2176" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-011-1b662190ae.png" alt="本地解析几何资料图片" width="670" height="388">（    ）</p>
<p class="local-docx-line">A．5B．7C．10D．14</p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-012-68f7d6868e.png" alt="本地解析几何资料图片" width="2176" height="608">，</p>
<p class="local-docx-line">可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-013-43ebf439f9.png" alt="本地解析几何资料图片" width="8096" height="512">，</p>
<p class="local-docx-line">即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-014-9a29fd913e.png" alt="本地解析几何资料图片" width="3296" height="512">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-015-077353b3d8.png" alt="本地解析几何资料图片" width="896" height="448">.故选：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-016-d7a172d974.png" alt="本地解析几何资料图片" width="352" height="384">.</p>
</div>
:::

:::

### 题 17（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-006-02078e93c4.png" alt="本地解析几何资料图片" width="1344" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-007-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">的值为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-008-2dd012a8b8.png" alt="本地解析几何资料图片" width="320" height="416">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-009-7bc6f46cef.png" alt="本地解析几何资料图片" width="288" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-010-0563812418.png" alt="本地解析几何资料图片" width="320" height="416">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-011-d92f88f1eb.png" alt="本地解析几何资料图片" width="288" height="448"></p>
<p class="local-docx-line">【题组二 组合数计算】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-017-02078e93c4.png" alt="本地解析几何资料图片" width="1344" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-018-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">的值为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-019-2dd012a8b8.png" alt="本地解析几何资料图片" width="320" height="416">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-020-7bc6f46cef.png" alt="本地解析几何资料图片" width="288" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-021-0563812418.png" alt="本地解析几何资料图片" width="320" height="416">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-022-d92f88f1eb.png" alt="本地解析几何资料图片" width="288" height="448"></p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】由排列数公式可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-023-11926735a8.png" alt="本地解析几何资料图片" width="2880" height="640">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-024-44c6ef639a.png" alt="本地解析几何资料图片" width="2304" height="512">，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-025-c9936d28ea.png" alt="本地解析几何资料图片" width="1408" height="512">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-026-eceeaf7acb.png" alt="本地解析几何资料图片" width="864" height="448">.故选：D.</p>
<p class="local-docx-line">【题组二 组合数计算】</p>
</div>
:::

:::

### 题 18（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-012-0c703d0ae7.png" alt="本地解析几何资料图片" width="4064" height="608"> （    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-013-5fb8b45da0.png" alt="本地解析几何资料图片" width="576" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-014-976eff94ae.png" alt="本地解析几何资料图片" width="576" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-015-431fed80f7.png" alt="本地解析几何资料图片" width="1088" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-016-710501bbdc.png" alt="本地解析几何资料图片" width="1088" height="608"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-027-0c703d0ae7.png" alt="本地解析几何资料图片" width="4064" height="608"> （    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-028-5fb8b45da0.png" alt="本地解析几何资料图片" width="576" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-029-976eff94ae.png" alt="本地解析几何资料图片" width="576" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-030-431fed80f7.png" alt="本地解析几何资料图片" width="1088" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-031-710501bbdc.png" alt="本地解析几何资料图片" width="1088" height="608"></p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-032-05489796bc.png" alt="本地解析几何资料图片" width="10496" height="608"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-033-4b552a316c.png" alt="本地解析几何资料图片" width="4640" height="608">．故选：B．</p>
</div>
:::

:::

### 题 19（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-017-8bba01e513.png" alt="本地解析几何资料图片" width="4544" height="608">的值为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-018-d00a562efb.png" alt="本地解析几何资料图片" width="800" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-019-c53ed66a14.png" alt="本地解析几何资料图片" width="832" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-020-3879983499.png" alt="本地解析几何资料图片" width="832" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-021-1f6d1bb38c.png" alt="本地解析几何资料图片" width="800" height="608"></p>
<p class="local-docx-line">【题组三 综合运用】1．下列等式中，正确的是（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-022-dcec213b23.png" alt="本地解析几何资料图片" width="2816" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-023-dabd0ba083.png" alt="本地解析几何资料图片" width="1888" height="608"></p>
<p class="local-docx-line">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-024-081aa3d819.png" alt="本地解析几何资料图片" width="3872" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-025-bfb7a5cc0a.png" alt="本地解析几何资料图片" width="2592" height="992"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-034-8bba01e513.png" alt="本地解析几何资料图片" width="4544" height="608">的值为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-035-d00a562efb.png" alt="本地解析几何资料图片" width="800" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-036-c53ed66a14.png" alt="本地解析几何资料图片" width="832" height="608">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-037-3879983499.png" alt="本地解析几何资料图片" width="832" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-038-1f6d1bb38c.png" alt="本地解析几何资料图片" width="800" height="608"></p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-039-fb46b4dc01.png" alt="本地解析几何资料图片" width="3776" height="608">,<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-040-74881fdcfa.png" alt="本地解析几何资料图片" width="2624" height="608"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-041-8bba01e513.png" alt="本地解析几何资料图片" width="4544" height="608"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-042-fa7a56e0dd.png" alt="本地解析几何资料图片" width="4064" height="1664"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-043-acda1f9c8b.png" alt="本地解析几何资料图片" width="1120" height="608"></p>
<p class="local-docx-line">故选：C</p>
<p class="local-docx-line">【题组三 综合运用】1．下列等式中，正确的是（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-044-dcec213b23.png" alt="本地解析几何资料图片" width="2816" height="608">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-045-dabd0ba083.png" alt="本地解析几何资料图片" width="1888" height="608"></p>
<p class="local-docx-line">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-046-081aa3d819.png" alt="本地解析几何资料图片" width="3872" height="608">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-047-bfb7a5cc0a.png" alt="本地解析几何资料图片" width="2592" height="992"></p>
<p class="local-docx-line">【答案】ABD</p>
<p class="local-docx-line">【解析】选项A，左边=<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-048-5012338bb3.png" alt="本地解析几何资料图片" width="11104" height="1184"> <img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-049-be74ef4a82.png" alt="本地解析几何资料图片" width="2144" height="1184">=右边，正确；</p>
<p class="local-docx-line">选项B，右边<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-050-8fe9f12635.png" alt="本地解析几何资料图片" width="9792" height="1184">左边，正确；</p>
<p class="local-docx-line">选项C，右边<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-051-4545e3bfb3.png" alt="本地解析几何资料图片" width="3264" height="608">左边，错误；</p>
<p class="local-docx-line">选项D，右边<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-052-cf0bc9dee5.png" alt="本地解析几何资料图片" width="12096" height="1184">左边，正确.故选：ABD</p>
</div>
:::

:::

### 题 20（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．计算：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-026-06c8d318f0.png" alt="本地解析几何资料图片" width="2272" height="992"> __________</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．计算：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-053-06c8d318f0.png" alt="本地解析几何资料图片" width="2272" height="992"> __________</p>
<p class="local-docx-line">【答案】36</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-054-623b0bb331.png" alt="本地解析几何资料图片" width="7424" height="992"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-055-fe29c740a3.png" alt="本地解析几何资料图片" width="2784" height="448">.故答案为：36.</p>
</div>
:::

:::

### 题 21（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-027-55b12ff9ca.png" alt="本地解析几何资料图片" width="2048" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-028-967b6ea795.png" alt="本地解析几何资料图片" width="832" height="608">______．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-056-55b12ff9ca.png" alt="本地解析几何资料图片" width="2048" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-057-967b6ea795.png" alt="本地解析几何资料图片" width="832" height="608">______．</p>
<p class="local-docx-line">【答案】12</p>
<p class="local-docx-line">【解析】由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-058-55b12ff9ca.png" alt="本地解析几何资料图片" width="2048" height="608">得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-059-21cac17d9a.png" alt="本地解析几何资料图片" width="4544" height="992">，化简可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-060-765a3e25ba.png" alt="本地解析几何资料图片" width="2912" height="512">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-061-f695d36130.png" alt="本地解析几何资料图片" width="896" height="448">，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-062-f84075d745.png" alt="本地解析几何资料图片" width="2304" height="608">.故答案为：12.</p>
</div>
:::

:::

### 题 22（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-029-c9706b75c3.png" alt="本地解析几何资料图片" width="1696" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-030-1b662190ae.png" alt="本地解析几何资料图片" width="670" height="388">__________．</p>
<p class="local-docx-line">5（1）解不等式：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-031-12f71ce47c.png" alt="本地解析几何资料图片" width="3232" height="608">；</p>
<p class="local-docx-line">（2）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-032-e70f363206.png" alt="本地解析几何资料图片" width="2848" height="1088">，求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-033-4dcd674813.png" alt="本地解析几何资料图片" width="800" height="608">．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-063-c9706b75c3.png" alt="本地解析几何资料图片" width="1696" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-064-1b662190ae.png" alt="本地解析几何资料图片" width="670" height="388">__________．</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-065-b426f92e5d.png" alt="本地解析几何资料图片" width="288" height="448"></p>
<p class="local-docx-line">【解析】由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-066-c9706b75c3.png" alt="本地解析几何资料图片" width="1696" height="608">得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-067-bf6c1bcd2e.png" alt="本地解析几何资料图片" width="4448" height="1728">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-068-fff84f1452.png" alt="本地解析几何资料图片" width="896" height="448"></p>
<p class="local-docx-line">故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-069-b426f92e5d.png" alt="本地解析几何资料图片" width="288" height="448"></p>
<p class="local-docx-line">5（1）解不等式：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-070-12f71ce47c.png" alt="本地解析几何资料图片" width="3232" height="608">；</p>
<p class="local-docx-line">（2）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-071-e70f363206.png" alt="本地解析几何资料图片" width="2848" height="1088">，求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-072-4dcd674813.png" alt="本地解析几何资料图片" width="800" height="608">．</p>
<p class="local-docx-line">【答案】（1）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-073-e766248fb7.png" alt="本地解析几何资料图片" width="1248" height="640">（2）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-074-e242affa7c.png" alt="本地解析几何资料图片" width="1568" height="608"></p>
<p class="local-docx-line">【解析】（1）因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-075-50b7c39f07.png" alt="本地解析几何资料图片" width="3392" height="640">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-076-82fa2fef9f.png" alt="本地解析几何资料图片" width="3232" height="640">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-077-e3f1cc817d.png" alt="本地解析几何资料图片" width="2368" height="640">，</p>
<p class="local-docx-line">所以不等式可化为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-078-7341183ef4.png" alt="本地解析几何资料图片" width="3968" height="640">，</p>
<p class="local-docx-line">解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-079-8d57d0f3be.png" alt="本地解析几何资料图片" width="1792" height="992">，</p>
<p class="local-docx-line">又<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-080-95a82684e8.png" alt="本地解析几何资料图片" width="896" height="448">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-081-249b4b6583.png" alt="本地解析几何资料图片" width="952" height="458">，</p>
<p class="local-docx-line">所以不等式的解集为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-082-e766248fb7.png" alt="本地解析几何资料图片" width="1248" height="640">．</p>
<p class="local-docx-line">（2）因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-083-ae76c51976.png" alt="本地解析几何资料图片" width="2720" height="1120">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-084-d8659c04bf.png" alt="本地解析几何资料图片" width="2720" height="1120">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-085-193a3c312c.png" alt="本地解析几何资料图片" width="2720" height="1120">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-086-e70f363206.png" alt="本地解析几何资料图片" width="2848" height="1088">，</p>
<p class="local-docx-line">可化为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-087-9b7f834446.png" alt="本地解析几何资料图片" width="4128" height="1056">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-088-b1acf80bfb.png" alt="本地解析几何资料图片" width="2848" height="512">，</p>
<p class="local-docx-line">解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-089-12d8b9b8aa.png" alt="本地解析几何资料图片" width="1152" height="448">（舍去）或2，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-090-e242affa7c.png" alt="本地解析几何资料图片" width="1568" height="608">．</p>
</div>
:::

:::

### 题 23（原题 6）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">6．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-034-1d900879a6.png" alt="本地解析几何资料图片" width="2176" height="608">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-035-9789e27eae.png" alt="本地解析几何资料图片" width="1120" height="576">.</p>
<p class="local-docx-line">（1）求x的值；</p>
<p class="local-docx-line">（2）求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-036-1cc785776a.png" alt="本地解析几何资料图片" width="1984" height="608">的值.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">6．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-091-1d900879a6.png" alt="本地解析几何资料图片" width="2176" height="608">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-092-9789e27eae.png" alt="本地解析几何资料图片" width="1120" height="576">.</p>
<p class="local-docx-line">（1）求x的值；</p>
<p class="local-docx-line">（2）求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-093-1cc785776a.png" alt="本地解析几何资料图片" width="1984" height="608">的值.</p>
<p class="local-docx-line">【答案】（1）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-094-41eefc7f0e.png" alt="本地解析几何资料图片" width="864" height="448">；（2）1330</p>
<p class="local-docx-line">【解析】（1）由已知得：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-095-23d321d58c.png" alt="本地解析几何资料图片" width="3968" height="1056">，化简得：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-096-026cf2a2ab.png" alt="本地解析几何资料图片" width="2656" height="512">，</p>
<p class="local-docx-line">解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-097-41eefc7f0e.png" alt="本地解析几何资料图片" width="864" height="448">或<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-098-da8cdde759.png" alt="本地解析几何资料图片" width="1056" height="448">，</p>
<p class="local-docx-line">又因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-099-5cae9ee041.png" alt="本地解析几何资料图片" width="1440" height="1152">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-100-41eefc7f0e.png" alt="本地解析几何资料图片" width="864" height="448">.</p>
<p class="local-docx-line">（2）将<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-101-41eefc7f0e.png" alt="本地解析几何资料图片" width="864" height="448">代入得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-102-c4bdcb44bb.png" alt="本地解析几何资料图片" width="5280" height="608">.</p>
</div>
:::

:::

### 题 24（原题 7）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">7．（1）证明：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-037-6206094c64.png" alt="本地解析几何资料图片" width="2892" height="670">（<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-038-a0079c9c8e.png" alt="本地解析几何资料图片" width="1440" height="448">且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-039-32d0ce7624.png" alt="本地解析几何资料图片" width="992" height="416">）；</p>
<p class="local-docx-line">（2）证明：对一切正整数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-040-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">和一切实数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-041-84d623d1df.png" alt="本地解析几何资料图片" width="1216" height="512">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-042-8c5b7c31c3.png" alt="本地解析几何资料图片" width="480" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-043-383cfdb306.png" alt="本地解析几何资料图片" width="416" height="192">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-044-ac28f498fc.png" alt="本地解析几何资料图片" width="608" height="480">，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-045-7ff783a89c.png" alt="本地解析几何资料图片" width="6624" height="1088">．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">7．（1）证明：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-103-6206094c64.png" alt="本地解析几何资料图片" width="2892" height="670">（<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-104-a0079c9c8e.png" alt="本地解析几何资料图片" width="1440" height="448">且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-105-32d0ce7624.png" alt="本地解析几何资料图片" width="992" height="416">）；</p>
<p class="local-docx-line">（2）证明：对一切正整数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-106-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">和一切实数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-107-84d623d1df.png" alt="本地解析几何资料图片" width="1216" height="512">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-108-8c5b7c31c3.png" alt="本地解析几何资料图片" width="480" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-109-383cfdb306.png" alt="本地解析几何资料图片" width="416" height="192">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-110-ac28f498fc.png" alt="本地解析几何资料图片" width="608" height="480">，有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-111-7ff783a89c.png" alt="本地解析几何资料图片" width="6624" height="1088">．</p>
<p class="local-docx-line">【答案】（1）证明见解析；（2）证明见解析．</p>
<p class="local-docx-line">【解析】证明：（1）右边<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-112-b320ac4fc3.png" alt="本地解析几何资料图片" width="12032" height="1056">左边，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-113-5aecb5cd60.png" alt="本地解析几何资料图片" width="352" height="320"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-114-2a935c13aa.png" alt="本地解析几何资料图片" width="5568" height="640">．</p>
<p class="local-docx-line">（2）①当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-115-4ec88dc56e.png" alt="本地解析几何资料图片" width="832" height="448">时，左边<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-116-8e52a58432.png" alt="本地解析几何资料图片" width="3008" height="992">右边．</p>
<p class="local-docx-line">②假设<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-117-2f94922151.png" alt="本地解析几何资料图片" width="896" height="448">时，对一切实数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-118-84d623d1df.png" alt="本地解析几何资料图片" width="1216" height="512">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-119-8c5b7c31c3.png" alt="本地解析几何资料图片" width="480" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-120-383cfdb306.png" alt="本地解析几何资料图片" width="416" height="192">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-121-94e3d89d13.png" alt="本地解析几何资料图片" width="672" height="512">，都有</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-122-34416d9fec.png" alt="本地解析几何资料图片" width="6624" height="1088">成立，</p>
<p class="local-docx-line">那么，当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-123-c44774ab03.png" alt="本地解析几何资料图片" width="2688" height="512">时，对一切实数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-124-84d623d1df.png" alt="本地解析几何资料图片" width="1216" height="512">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-125-8c5b7c31c3.png" alt="本地解析几何资料图片" width="480" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-126-b6f89bb70c.png" alt="本地解析几何资料图片" width="1824" height="512">，有</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-127-6dcf961eeb.png" alt="本地解析几何资料图片" width="10624" height="1088">，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-128-f2dc63f7cb.png" alt="本地解析几何资料图片" width="11616" height="1088"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-129-0217cb00c4.png" alt="本地解析几何资料图片" width="6432" height="1088"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-130-46adfb944b.png" alt="本地解析几何资料图片" width="7584" height="1088"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-131-fd400a22f2.png" alt="本地解析几何资料图片" width="8864" height="1056"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-132-5baabfe06a.png" alt="本地解析几何资料图片" width="8544" height="1056">，</p>
<p class="local-docx-line">所以当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-133-9869ba1829.png" alt="本地解析几何资料图片" width="1376" height="448">时，等式成立，</p>
<p class="local-docx-line">故对一切正整数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-134-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">和一切实数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-135-84d623d1df.png" alt="本地解析几何资料图片" width="1216" height="512">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-136-8c5b7c31c3.png" alt="本地解析几何资料图片" width="480" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-137-383cfdb306.png" alt="本地解析几何资料图片" width="416" height="192">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-138-ac28f498fc.png" alt="本地解析几何资料图片" width="608" height="480">，</p>
<p class="local-docx-line">有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-139-7ff783a89c.png" alt="本地解析几何资料图片" width="6624" height="1088">．</p>
</div>
:::

:::

### 题 25（原题 8）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">8．（1）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-046-659c3f94e2.png" alt="本地解析几何资料图片" width="2656" height="1152">，求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-047-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">的值.</p>
<p class="local-docx-line">（2）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-048-12ea6eb638.png" alt="本地解析几何资料图片" width="2528" height="1664">求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-q-049-bc3408ab23.png" alt="本地解析几何资料图片" width="640" height="416">的值.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">8．（1）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-140-659c3f94e2.png" alt="本地解析几何资料图片" width="2656" height="1152">，求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-141-64795d2af5.png" alt="本地解析几何资料图片" width="320" height="352">的值.</p>
<p class="local-docx-line">（2）已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-142-12ea6eb638.png" alt="本地解析几何资料图片" width="2528" height="1664">求<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-143-bc3408ab23.png" alt="本地解析几何资料图片" width="640" height="416">的值.</p>
<p class="local-docx-line">【答案】（1）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-144-d2fd8d58ea.png" alt="本地解析几何资料图片" width="928" height="448">（2）<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-145-ffea47cfe5.png" alt="本地解析几何资料图片" width="864" height="448">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-146-88e7fdc732.png" alt="本地解析几何资料图片" width="1024" height="448"></p>
<p class="local-docx-line">【解析】（1）原方程化为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-147-066a573dca.png" alt="本地解析几何资料图片" width="2144" height="1152">，变形得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-148-c580d4a931.png" alt="本地解析几何资料图片" width="2272" height="608">，展开可得：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-149-bad2e7c38e.png" alt="本地解析几何资料图片" width="8896" height="1056"> 解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-150-2a17454c85.png" alt="本地解析几何资料图片" width="2880" height="640"> 即n2-3n-54=0， 解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-151-80ec5423fc.png" alt="本地解析几何资料图片" width="896" height="448">或<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-152-44e655e87f.png" alt="本地解析几何资料图片" width="1088" height="448">（舍去）.</p>
<p class="local-docx-line">（2）∵<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-153-e38df28093.png" alt="本地解析几何资料图片" width="3584" height="512">，∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-154-b025b884b0.png" alt="本地解析几何资料图片" width="800" height="448">，由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-155-1063783b63.png" alt="本地解析几何资料图片" width="2560" height="608">，∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-156-7ff6c5fe3d.png" alt="本地解析几何资料图片" width="1632" height="448">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-157-8d7296c16c.png" alt="本地解析几何资料图片" width="1088" height="448">，由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-158-c67dfbcbf5.png" alt="本地解析几何资料图片" width="2208" height="992">，得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-159-149230ded7.png" alt="本地解析几何资料图片" width="4832" height="640">将<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-160-8d7296c16c.png" alt="本地解析几何资料图片" width="1088" height="448">代入得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-161-ab714c6116.png" alt="本地解析几何资料图片" width="864" height="448">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct34-a-162-a70883581b.png" alt="本地解析几何资料图片" width="1024" height="448">.</p>
</div>
:::

:::

## 考点 35：二项式定理

本组来自 `考点35 二项式定理（练习） （原卷版）.docx`；原卷共抽取 29 道题，解析版原始抽取 29 道，可对齐显示 29 道。

### 题 26（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-002-e6d64e819e.png" alt="本地解析几何资料图片" width="1312" height="992">的二项展开式中，常数项的值为________</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-002-e6d64e819e.png" alt="本地解析几何资料图片" width="1312" height="992">的二项展开式中，常数项的值为________</p>
<p class="local-docx-line">【答案】－160</p>
<p class="local-docx-line">【解析】展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-003-8484f9233c.png" alt="本地解析几何资料图片" width="5312" height="992">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-004-bb1acc77ef.png" alt="本地解析几何资料图片" width="1568" height="448">，得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-005-617e2ec8e9.png" alt="本地解析几何资料图片" width="832" height="448"></p>
<p class="local-docx-line">∴在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-006-522e23afec.png" alt="本地解析几何资料图片" width="1408" height="1184">的二项展开式中，常数项的值为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-007-0dbee96a3d.png" alt="本地解析几何资料图片" width="2528" height="608">故答案为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-008-3ec0b95711.png" alt="本地解析几何资料图片" width="896" height="448"></p>
</div>
:::

:::

### 题 27（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-003-d9c0d10d82.png" alt="本地解析几何资料图片" width="1728" height="1152">展开式中，二项式系数最大的项是_________．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-009-d9c0d10d82.png" alt="本地解析几何资料图片" width="1728" height="1152">展开式中，二项式系数最大的项是_________．</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-010-9c0104f584.png" alt="本地解析几何资料图片" width="832" height="992"></p>
<p class="local-docx-line">【解析】在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-011-d9c0d10d82.png" alt="本地解析几何资料图片" width="1728" height="1152">的展开式中，由二次项系数的性质可得：展开式中第4项的二项式系数最大，因此，该项为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-012-f713a36e34.png" alt="本地解析几何资料图片" width="4416" height="1184">.故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-013-9c0104f584.png" alt="本地解析几何资料图片" width="832" height="992">.</p>
</div>
:::

:::

### 题 28（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-004-cac20730b7.png" alt="本地解析几何资料图片" width="1792" height="1184">的展开式中，常数项为__________（用数字作答）.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-014-cac20730b7.png" alt="本地解析几何资料图片" width="1792" height="1184">的展开式中，常数项为__________（用数字作答）.</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-015-2040d8332c.png" alt="本地解析几何资料图片" width="448" height="864"></p>
<p class="local-docx-line">【解析】因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-016-40ac1e0f57.png" alt="本地解析几何资料图片" width="6624" height="1184">，令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-017-3db99ad48f.png" alt="本地解析几何资料图片" width="1568" height="448">，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-018-c185aa0ac0.png" alt="本地解析几何资料图片" width="928" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-019-ac5d761416.png" alt="本地解析几何资料图片" width="1216" height="992">.故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-020-2040d8332c.png" alt="本地解析几何资料图片" width="448" height="864">.</p>
</div>
:::

:::

### 题 29（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-005-bb1b553569.png" alt="本地解析几何资料图片" width="1728" height="1184">的展开式中，含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-006-04a714f8bf.png" alt="本地解析几何资料图片" width="448" height="512">的系数为_______．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-021-bb1b553569.png" alt="本地解析几何资料图片" width="1728" height="1184">的展开式中，含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-022-04a714f8bf.png" alt="本地解析几何资料图片" width="448" height="512">的系数为_______．</p>
<p class="local-docx-line">【答案】6</p>
<p class="local-docx-line">【解析】根据题意，二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-023-7c1c784508.png" alt="本地解析几何资料图片" width="1632" height="992">的展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-024-650bf67a86.png" alt="本地解析几何资料图片" width="4896" height="992">，令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-025-f322767346.png" alt="本地解析几何资料图片" width="1728" height="448">，可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-026-c0d54a4b09.png" alt="本地解析几何资料图片" width="800" height="416">，此时<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-027-ff324164f6.png" alt="本地解析几何资料图片" width="2464" height="608">，即含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-028-3a8e2d52bf.png" alt="本地解析几何资料图片" width="448" height="512">的系数为6，故答案为：6．</p>
</div>
:::

:::

### 题 30（原题 5）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">5．若直线<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-007-13cf4a6534.png" alt="本地解析几何资料图片" width="4640" height="544">垂直，则二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-008-9e8ce86f0c.png" alt="本地解析几何资料图片" width="1728" height="1184">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-009-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数为(  )</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-010-880def8159.png" alt="本地解析几何资料图片" width="480" height="384">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-011-8a42d89b04.png" alt="本地解析几何资料图片" width="704" height="1024">C．2D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-012-f0d0df4269.png" alt="本地解析几何资料图片" width="384" height="992"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">5．若直线<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-029-13cf4a6534.png" alt="本地解析几何资料图片" width="4640" height="544">垂直，则二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-030-9e8ce86f0c.png" alt="本地解析几何资料图片" width="1728" height="1184">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-031-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数为(  )</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-032-880def8159.png" alt="本地解析几何资料图片" width="480" height="384">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-033-8a42d89b04.png" alt="本地解析几何资料图片" width="704" height="1024">C．2D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-034-f0d0df4269.png" alt="本地解析几何资料图片" width="384" height="992"></p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】由直线<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-035-50cd601971.png" alt="本地解析几何资料图片" width="2048" height="512">与<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-036-1690ce177b.png" alt="本地解析几何资料图片" width="2336" height="512">垂直，可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-037-cecdfb098c.png" alt="本地解析几何资料图片" width="2848" height="640">，求得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-038-15fed672d5.png" alt="本地解析几何资料图片" width="960" height="992">，则二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-039-9da02065b6.png" alt="本地解析几何资料图片" width="3936" height="1184">的展开式的通项公式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-040-496d2a8ae3.png" alt="本地解析几何资料图片" width="4800" height="1184">，令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-041-cb1d2e4bf9.png" alt="本地解析几何资料图片" width="1664" height="448">，求得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-042-2b412aebe3.png" alt="本地解析几何资料图片" width="832" height="448">，可得展开式中x的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-043-05b057028c.png" alt="本地解析几何资料图片" width="3392" height="1184">.故答案为B．</p>
</div>
:::

:::

### 题 31（原题 6）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">6．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-013-b419c3bdbb.png" alt="本地解析几何资料图片" width="1472" height="992">的二项展开式中常数项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-014-8a42d89b04.png" alt="本地解析几何资料图片" width="704" height="1024">，则常数a的值是_______.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">6．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-044-b419c3bdbb.png" alt="本地解析几何资料图片" width="1472" height="992">的二项展开式中常数项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-045-8a42d89b04.png" alt="本地解析几何资料图片" width="704" height="1024">，则常数a的值是_______.</p>
<p class="local-docx-line">【答案】2</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-046-b419c3bdbb.png" alt="本地解析几何资料图片" width="1472" height="992">的第r＋1项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-047-79a7d56093.png" alt="本地解析几何资料图片" width="6368" height="992">，</p>
<p class="local-docx-line">常数项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-048-8a42d89b04.png" alt="本地解析几何资料图片" width="704" height="1024">，则r＝3，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-049-0263504023.png" alt="本地解析几何资料图片" width="2560" height="992">，解得a＝2.故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-050-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416"></p>
</div>
:::

:::

### 题 32（原题 7）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">7．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-015-7c3a897a87.png" alt="本地解析几何资料图片" width="1408" height="1056">的二项展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-016-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">项的系数为______.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">7．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-051-7c3a897a87.png" alt="本地解析几何资料图片" width="1408" height="1056">的二项展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-052-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">项的系数为______.</p>
<p class="local-docx-line">【答案】－160</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-053-7c3a897a87.png" alt="本地解析几何资料图片" width="1408" height="1056">的展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-054-a6490cab15.png" alt="本地解析几何资料图片" width="5344" height="896">，</p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-055-58fc420e75.png" alt="本地解析几何资料图片" width="1696" height="448">，得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-056-617e2ec8e9.png" alt="本地解析几何资料图片" width="832" height="448">，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-057-7c3a897a87.png" alt="本地解析几何资料图片" width="1408" height="1056">的二项展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-058-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">项的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-059-d14ccbd599.png" alt="本地解析几何资料图片" width="2432" height="544">，</p>
<p class="local-docx-line">故答案为：－160</p>
</div>
:::

:::

### 题 33（原题 8）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">8．已知在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-017-972939c347.png" alt="本地解析几何资料图片" width="2434" height="1340">的展开式中，第6项为常数项，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-018-5732bbcc03.png" alt="本地解析几何资料图片" width="670" height="388">______.</p>
<p class="local-docx-line">【题组二  因式之积的特定项系数】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">8．已知在<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-060-972939c347.png" alt="本地解析几何资料图片" width="2434" height="1340">的展开式中，第6项为常数项，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-061-5732bbcc03.png" alt="本地解析几何资料图片" width="670" height="388">______.</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-062-215a2c175b.png" alt="本地解析几何资料图片" width="448" height="448"></p>
<p class="local-docx-line">【解析】二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-063-972939c347.png" alt="本地解析几何资料图片" width="2434" height="1340">的展开式的通项公式为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-064-aaf4f21ec2.png" alt="本地解析几何资料图片" width="2976" height="960">，</p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-065-5c679e5be9.png" alt="本地解析几何资料图片" width="896" height="448">，可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-066-6cbe2de260.png" alt="本地解析几何资料图片" width="1664" height="992">，求得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-067-da3dd836ec.png" alt="本地解析几何资料图片" width="1056" height="448">．故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-068-215a2c175b.png" alt="本地解析几何资料图片" width="448" height="448"></p>
<p class="local-docx-line">【题组二  因式之积的特定项系数】</p>
</div>
:::

:::

### 题 34（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-019-14dcd1bb3e.png" alt="本地解析几何资料图片" width="2624" height="704">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-020-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">的系数为（    ）</p>
<p class="local-docx-line">A．40B．80C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-021-4e39b0112a.png" alt="本地解析几何资料图片" width="704" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-022-5b82608850.png" alt="本地解析几何资料图片" width="704" height="448"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-069-14dcd1bb3e.png" alt="本地解析几何资料图片" width="2624" height="704">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-070-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">的系数为（    ）</p>
<p class="local-docx-line">A．40B．80C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-071-4e39b0112a.png" alt="本地解析几何资料图片" width="704" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-072-5b82608850.png" alt="本地解析几何资料图片" width="704" height="448"></p>
<p class="local-docx-line">【答案】A</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-073-5ac1a13d41.png" alt="本地解析几何资料图片" width="1376" height="704">展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-074-a2f8b3eca9.png" alt="本地解析几何资料图片" width="3712" height="704">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-075-c185aa0ac0.png" alt="本地解析几何资料图片" width="928" height="416">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-076-fd7139e901.png" alt="本地解析几何资料图片" width="3328" height="704">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-077-617e2ec8e9.png" alt="本地解析几何资料图片" width="832" height="448">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-078-f7a55e2668.png" alt="本地解析几何资料图片" width="3808" height="704">，</p>
<p class="local-docx-line">则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-079-14dcd1bb3e.png" alt="本地解析几何资料图片" width="2624" height="704">的展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-080-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">的项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-081-5b2a4dd132.png" alt="本地解析几何资料图片" width="4576" height="704">，</p>
<p class="local-docx-line">故<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-082-14dcd1bb3e.png" alt="本地解析几何资料图片" width="2624" height="704">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-083-171d59d1c8.png" alt="本地解析几何资料图片" width="384" height="480">的系数为40．故选：A．</p>
</div>
:::

:::

### 题 35（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-023-76c7bcd551.png" alt="本地解析几何资料图片" width="2944" height="1184">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-024-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数是（    ）</p>
<p class="local-docx-line">A．10B．2C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-025-ec922db0f3.png" alt="本地解析几何资料图片" width="704" height="416">D．34</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-084-76c7bcd551.png" alt="本地解析几何资料图片" width="2944" height="1184">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-085-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数是（    ）</p>
<p class="local-docx-line">A．10B．2C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-086-ec922db0f3.png" alt="本地解析几何资料图片" width="704" height="416">D．34</p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】由题意，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-087-ffd8c26693.png" alt="本地解析几何资料图片" width="9088" height="1280"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-088-b7fa9aa929.png" alt="本地解析几何资料图片" width="3072" height="1152">，</p>
<p class="local-docx-line">又<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-089-e7a72c1da3.png" alt="本地解析几何资料图片" width="1184" height="704">的展开式的通项公式为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-090-84c6b37210.png" alt="本地解析几何资料图片" width="1984" height="608">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-091-542085c465.png" alt="本地解析几何资料图片" width="1280" height="1152">的展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-092-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-093-c43e8ef72f.png" alt="本地解析几何资料图片" width="1888" height="1056">，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-094-0fea0c6aa4.png" alt="本地解析几何资料图片" width="1536" height="1152">的展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-095-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-096-fe4d38bf92.png" alt="本地解析几何资料图片" width="2432" height="1056">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-097-76c7bcd551.png" alt="本地解析几何资料图片" width="2944" height="1184">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-098-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-099-72f8dcb05d.png" alt="本地解析几何资料图片" width="2504" height="670">.</p>
<p class="local-docx-line">故选：C．</p>
</div>
:::

:::

### 题 36（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-026-4cd5e83eb3.png" alt="本地解析几何资料图片" width="2784" height="704">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-027-c230099867.png" alt="本地解析几何资料图片" width="768" height="576">的系数为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-028-fb5a022e71.png" alt="本地解析几何资料图片" width="512" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-029-6d68175250.png" alt="本地解析几何资料图片" width="480" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-030-dfed68719c.png" alt="本地解析几何资料图片" width="640" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-031-84aa7d636c.png" alt="本地解析几何资料图片" width="640" height="448"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-100-4cd5e83eb3.png" alt="本地解析几何资料图片" width="2784" height="704">的展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-101-c230099867.png" alt="本地解析几何资料图片" width="768" height="576">的系数为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-102-fb5a022e71.png" alt="本地解析几何资料图片" width="512" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-103-6d68175250.png" alt="本地解析几何资料图片" width="480" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-104-dfed68719c.png" alt="本地解析几何资料图片" width="640" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-105-84aa7d636c.png" alt="本地解析几何资料图片" width="640" height="448"></p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-106-719bd5f424.png" alt="本地解析几何资料图片" width="1472" height="704">展开式的通项公式为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-107-3d183a8a16.png" alt="本地解析几何资料图片" width="5312" height="704">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-108-617e2ec8e9.png" alt="本地解析几何资料图片" width="832" height="448">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-109-ce78a5bbe6.png" alt="本地解析几何资料图片" width="4224" height="608">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-110-c185aa0ac0.png" alt="本地解析几何资料图片" width="928" height="416">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-111-da34ed7c06.png" alt="本地解析几何资料图片" width="4256" height="608">，</p>
<p class="local-docx-line">据此可得：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-112-c230099867.png" alt="本地解析几何资料图片" width="768" height="576">的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-113-dcfa0ceb5c.png" alt="本地解析几何资料图片" width="2144" height="448">.</p>
<p class="local-docx-line">本题选择C选项.</p>
</div>
:::

:::

### 题 37（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4.已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-032-fbaf1aa9e8.png" alt="本地解析几何资料图片" width="8325" height="776">，其中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-033-2b2f450b11.png" alt="本地解析几何资料图片" width="1184" height="576">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-034-96ce987934.png" alt="本地解析几何资料图片" width="608" height="448">______．</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4.已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-114-fbaf1aa9e8.png" alt="本地解析几何资料图片" width="8325" height="776">，其中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-115-2b2f450b11.png" alt="本地解析几何资料图片" width="1184" height="576">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-116-96ce987934.png" alt="本地解析几何资料图片" width="608" height="448">______．</p>
<p class="local-docx-line">【答案】3</p>
<p class="local-docx-line">【解析】由题意展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-117-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-118-567d97eae0.png" alt="本地解析几何资料图片" width="2080" height="608">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-119-c225afd502.png" alt="本地解析几何资料图片" width="864" height="448">．故答案为：3．</p>
</div>
:::

:::

### 题 38（原题 5）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">5．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-035-5371e0e311.png" alt="本地解析几何资料图片" width="3488" height="1184">的展开式中x2项的系数为__________.</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">5．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-120-5371e0e311.png" alt="本地解析几何资料图片" width="3488" height="1184">的展开式中x2项的系数为__________.</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-121-2b735c964a.png" alt="本地解析几何资料图片" width="480" height="416"></p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-122-68fc0a93f2.png" alt="本地解析几何资料图片" width="1408" height="1184">的通项公式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-123-77cfb94a87.png" alt="本地解析几何资料图片" width="5312" height="992">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-124-f58026d84d.png" alt="本地解析几何资料图片" width="1024" height="448">为偶数</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-125-bb1acc77ef.png" alt="本地解析几何资料图片" width="1568" height="448">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-126-db9e70693c.png" alt="本地解析几何资料图片" width="864" height="448"> ，此时<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-127-68fc0a93f2.png" alt="本地解析几何资料图片" width="1408" height="1184">展开式的常数项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-128-ff4a6be8b4.png" alt="本地解析几何资料图片" width="2304" height="608">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-129-ad2174a091.png" alt="本地解析几何资料图片" width="1792" height="448">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-130-f41288ba11.png" alt="本地解析几何资料图片" width="864" height="416">，此时<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-131-68fc0a93f2.png" alt="本地解析几何资料图片" width="1408" height="1184">展开式的<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-132-4c99ec7263.png" alt="本地解析几何资料图片" width="576" height="512">的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-133-9b214d3d0c.png" alt="本地解析几何资料图片" width="2080" height="608">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-134-5371e0e311.png" alt="本地解析几何资料图片" width="3488" height="1184">的展开式中x2项的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-135-a0467ca544.png" alt="本地解析几何资料图片" width="5344" height="608">，</p>
<p class="local-docx-line">故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-136-2b735c964a.png" alt="本地解析几何资料图片" width="480" height="416"></p>
</div>
:::

:::

### 题 39（原题 6）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">6．若随机变量<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-036-281966cf7a.png" alt="本地解析几何资料图片" width="2144" height="704">，且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-037-3640d60f62.png" alt="本地解析几何资料图片" width="3296" height="640">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-038-a84e7e9399.png" alt="本地解析几何资料图片" width="3264" height="1216">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-039-f2e6609013.png" alt="本地解析几何资料图片" width="416" height="512">项的系数是__________．</p>
<p class="local-docx-line">【题组三 （二项式）系数和】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">6．若随机变量<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-137-281966cf7a.png" alt="本地解析几何资料图片" width="2144" height="704">，且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-138-3640d60f62.png" alt="本地解析几何资料图片" width="3296" height="640">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-139-a84e7e9399.png" alt="本地解析几何资料图片" width="3264" height="1216">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-140-f2e6609013.png" alt="本地解析几何资料图片" width="416" height="512">项的系数是__________．</p>
<p class="local-docx-line">【答案】1620</p>
<p class="local-docx-line">【解析】</p>
<p class="local-docx-line">随机变量<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-141-281966cf7a.png" alt="本地解析几何资料图片" width="2144" height="704">，均值是2，且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-142-b38d1ec47c.png" alt="本地解析几何资料图片" width="3296" height="640">，∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-143-c2199a7adc.png" alt="本地解析几何资料图片" width="864" height="448">；∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-144-b848e23d17.png" alt="本地解析几何资料图片" width="10656" height="1216">；又<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-145-7b66351c6b.png" alt="本地解析几何资料图片" width="1888" height="1216">展开式的通项公式为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-146-5eab5ca6d2.png" alt="本地解析几何资料图片" width="7712" height="1216">，令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-147-bc85fe20b4.png" alt="本地解析几何资料图片" width="1536" height="992">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-148-a030351d5a.png" alt="本地解析几何资料图片" width="800" height="896">，不合题意，舍去；令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-149-02a4497d41.png" alt="本地解析几何资料图片" width="1632" height="992">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-150-c185aa0ac0.png" alt="本地解析几何资料图片" width="928" height="416">，对应<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-151-3d16811d9f.png" alt="本地解析几何资料图片" width="448" height="512">的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-152-7cea1983dd.png" alt="本地解析几何资料图片" width="3040" height="704">；令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-153-31fcaa0aba.png" alt="本地解析几何资料图片" width="1600" height="992">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-154-406b38461a.png" alt="本地解析几何资料图片" width="928" height="992">，不合题意，舍去；∴展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-155-f2e6609013.png" alt="本地解析几何资料图片" width="416" height="512">项的系数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-156-d3a5e5a6bb.png" alt="本地解析几何资料图片" width="2304" height="448">，故答案为1620.</p>
<p class="local-docx-line">【题组三 （二项式）系数和】</p>
</div>
:::

:::

### 题 40（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．已知二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-040-18ae543567.png" alt="本地解析几何资料图片" width="1312" height="576">的展开式的二项式项的系数和为64，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-041-3f75f9d356.png" alt="本地解析几何资料图片" width="6496" height="608"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-042-d938a58355.png" alt="本地解析几何资料图片" width="1536" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-043-61e48634e9.png" alt="本地解析几何资料图片" width="768" height="576">（    ）</p>
<p class="local-docx-line">A．20B．30C．60D．80</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．已知二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-157-18ae543567.png" alt="本地解析几何资料图片" width="1312" height="576">的展开式的二项式项的系数和为64，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-158-3f75f9d356.png" alt="本地解析几何资料图片" width="6496" height="608"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-159-d938a58355.png" alt="本地解析几何资料图片" width="1536" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-160-61e48634e9.png" alt="本地解析几何资料图片" width="768" height="576">（    ）</p>
<p class="local-docx-line">A．20B．30C．60D．80</p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】根据题意，令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-161-5e2b15f3af.png" alt="本地解析几何资料图片" width="1696" height="512">可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-162-2be65d0355.png" alt="本地解析几何资料图片" width="1248" height="512">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-163-264c22b116.png" alt="本地解析几何资料图片" width="4032" height="576"></p>
<p class="local-docx-line">设<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-164-06f7c0de74.png" alt="本地解析几何资料图片" width="1248" height="448">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-165-c62dede408.png" alt="本地解析几何资料图片" width="2176" height="448"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-166-3b2e296894.png" alt="本地解析几何资料图片" width="8896" height="608">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-167-d6efb620eb.png" alt="本地解析几何资料图片" width="3328" height="704">，</p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-168-94697cfdca.png" alt="本地解析几何资料图片" width="1376" height="448">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-169-eb9f70c0aa.png" alt="本地解析几何资料图片" width="864" height="416">．∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-170-e807f54006.png" alt="本地解析几何资料图片" width="6432" height="608">，可知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-171-6b9b1b0783.png" alt="本地解析几何资料图片" width="1216" height="576">.</p>
<p class="local-docx-line">故选：C.</p>
</div>
:::

:::

### 题 41（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-044-3af90705b6.png" alt="本地解析几何资料图片" width="10688" height="1088">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-045-e78006a95e.png" alt="本地解析几何资料图片" width="736" height="512">（    ）</p>
<p class="local-docx-line">A．21B．42C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-046-756cabb942.png" alt="本地解析几何资料图片" width="704" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-047-7902cc8360.png" alt="本地解析几何资料图片" width="896" height="448"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-172-3af90705b6.png" alt="本地解析几何资料图片" width="10688" height="1088">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-173-e78006a95e.png" alt="本地解析几何资料图片" width="736" height="512">（    ）</p>
<p class="local-docx-line">A．21B．42C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-174-756cabb942.png" alt="本地解析几何资料图片" width="704" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-175-7902cc8360.png" alt="本地解析几何资料图片" width="896" height="448"></p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-176-455e662918.png" alt="本地解析几何资料图片" width="4544" height="1216">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-177-fcc7e743da.png" alt="本地解析几何资料图片" width="416" height="576">即为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-178-827b36844d.png" alt="本地解析几何资料图片" width="1184" height="704">展开式中<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-179-486c4639c3.png" alt="本地解析几何资料图片" width="448" height="512">的系数<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-180-c64b615ee9.png" alt="本地解析几何资料图片" width="1728" height="608">，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-181-14d2f4b36e.png" alt="本地解析几何资料图片" width="1440" height="576">，故选：C.</p>
</div>
:::

:::

### 题 42（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-048-928a8c7edb.png" alt="本地解析几何资料图片" width="5600" height="704">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-049-02db6deeb0.png" alt="本地解析几何资料图片" width="4736" height="640">（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-050-0b62913c08.png" alt="本地解析几何资料图片" width="928" height="480">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-051-bc0fdeb9c3.png" alt="本地解析几何资料图片" width="416" height="480">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-052-14247d8b15.png" alt="本地解析几何资料图片" width="896" height="512">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-053-3b6d4721c6.png" alt="本地解析几何资料图片" width="416" height="512"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-182-928a8c7edb.png" alt="本地解析几何资料图片" width="5600" height="704">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-183-02db6deeb0.png" alt="本地解析几何资料图片" width="4736" height="640">（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-184-0b62913c08.png" alt="本地解析几何资料图片" width="928" height="480">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-185-bc0fdeb9c3.png" alt="本地解析几何资料图片" width="416" height="480">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-186-14247d8b15.png" alt="本地解析几何资料图片" width="896" height="512">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-187-3b6d4721c6.png" alt="本地解析几何资料图片" width="416" height="512"></p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】由题可知：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-188-83258a3308.png" alt="本地解析几何资料图片" width="320" height="352">的奇数次幂的系数均为负数</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-189-0ef72c5313.png" alt="本地解析几何资料图片" width="8448" height="640"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-190-112bc05745.png" alt="本地解析几何资料图片" width="5920" height="704"></p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-191-59f5a6655d.png" alt="本地解析几何资料图片" width="1088" height="448">得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-192-3766969a7c.png" alt="本地解析几何资料图片" width="4448" height="608"></p>
<p class="local-docx-line">则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-193-abb58eccf2.png" alt="本地解析几何资料图片" width="5088" height="640"></p>
<p class="local-docx-line">故选：D</p>
</div>
:::

:::

### 题 43（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-054-9eb517cc7f.png" alt="本地解析几何资料图片" width="7936" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-055-1caf7ef7db.png" alt="本地解析几何资料图片" width="704" height="512">（ ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-056-3e1378a028.png" alt="本地解析几何资料图片" width="896" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-057-e5bbac204f.png" alt="本地解析几何资料图片" width="640" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-058-47add332e6.png" alt="本地解析几何资料图片" width="512" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-059-8c05be05f1.png" alt="本地解析几何资料图片" width="704" height="448"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-194-9eb517cc7f.png" alt="本地解析几何资料图片" width="7936" height="608">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-195-1caf7ef7db.png" alt="本地解析几何资料图片" width="704" height="512">（ ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-196-3e1378a028.png" alt="本地解析几何资料图片" width="896" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-197-e5bbac204f.png" alt="本地解析几何资料图片" width="640" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-198-47add332e6.png" alt="本地解析几何资料图片" width="512" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-199-8c05be05f1.png" alt="本地解析几何资料图片" width="704" height="448"></p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】∵<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-200-6180f8b7e7.png" alt="本地解析几何资料图片" width="3552" height="576">，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-201-6f0bd17c8d.png" alt="本地解析几何资料图片" width="14432" height="704">∴<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-202-51a5eeb16c.png" alt="本地解析几何资料图片" width="3744" height="608">故选B.</p>
</div>
:::

:::

### 题 44（原题 5）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">5．二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-060-41662c31b6.png" alt="本地解析几何资料图片" width="1920" height="1216">中，前三项的系数成等差数列，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-061-5732bbcc03.png" alt="本地解析几何资料图片" width="670" height="388">__________，二项式系数最大的项是__________.</p>
<p class="local-docx-line">【题组四 二项式性质及运用】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">5．二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-203-41662c31b6.png" alt="本地解析几何资料图片" width="1920" height="1216">中，前三项的系数成等差数列，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-204-5732bbcc03.png" alt="本地解析几何资料图片" width="670" height="388">__________，二项式系数最大的项是__________.</p>
<p class="local-docx-line">【答案】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-205-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">    <img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-206-3982217188.png" alt="本地解析几何资料图片" width="928" height="1056"></p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-207-41662c31b6.png" alt="本地解析几何资料图片" width="1920" height="1216">展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-208-f299662c6d.png" alt="本地解析几何资料图片" width="6400" height="1216">，</p>
<p class="local-docx-line">由题意可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-209-c3c17d9664.png" alt="本地解析几何资料图片" width="3008" height="992">，整理得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-210-e6d3b6ce78.png" alt="本地解析几何资料图片" width="2272" height="512">，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-211-0e665cbc66.png" alt="本地解析几何资料图片" width="1216" height="448">且<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-212-66d1297b71.png" alt="本地解析几何资料图片" width="1088" height="512">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-213-32ecaf7de0.png" alt="本地解析几何资料图片" width="768" height="416">，</p>
<p class="local-docx-line">因此，二项式系数最大的项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-214-a5d8f040a2.png" alt="本地解析几何资料图片" width="4320" height="1184">.故答案为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-215-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">；<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-216-3982217188.png" alt="本地解析几何资料图片" width="928" height="1056">.</p>
<p class="local-docx-line">【题组四 二项式性质及运用】</p>
</div>
:::

:::

### 题 45（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-062-f966703d49.png" alt="本地解析几何资料图片" width="1856" height="1184">展开式中只有第六项的二项式系数最大，则展开式中的常数项是（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-063-e5bbac204f.png" alt="本地解析几何资料图片" width="640" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-064-d3b7ab1e86.png" alt="本地解析几何资料图片" width="480" height="448">C．-180D．-90</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-217-f966703d49.png" alt="本地解析几何资料图片" width="1856" height="1184">展开式中只有第六项的二项式系数最大，则展开式中的常数项是（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-218-e5bbac204f.png" alt="本地解析几何资料图片" width="640" height="448">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-219-d3b7ab1e86.png" alt="本地解析几何资料图片" width="480" height="448">C．-180D．-90</p>
<p class="local-docx-line">【答案】A</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-220-f12bf44d55.png" alt="本地解析几何资料图片" width="352" height="320"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-221-f966703d49.png" alt="本地解析几何资料图片" width="1856" height="1184">展开式中只有第六项的二项式系数最大，</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-222-0ea1dedf81.png" alt="本地解析几何资料图片" width="1344" height="448">，</p>
<p class="local-docx-line">故<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-223-f966703d49.png" alt="本地解析几何资料图片" width="1856" height="1184">展开式的通项公式为</p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-224-7ee60b2330.png" alt="本地解析几何资料图片" width="6912" height="1184">，</p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-225-62ebfdc296.png" alt="本地解析几何资料图片" width="1696" height="992">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-226-c185aa0ac0.png" alt="本地解析几何资料图片" width="928" height="416">，</p>
<p class="local-docx-line">所以展开式中的常数项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-227-e097ada754.png" alt="本地解析几何资料图片" width="2176" height="608">.</p>
<p class="local-docx-line">故选：A</p>
</div>
:::

:::

### 题 46（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-065-8b5f29ed9f.png" alt="本地解析几何资料图片" width="1440" height="1152">的展开式中只有第7项的二项式系数最大，则展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-066-5e7a78d8da.png" alt="本地解析几何资料图片" width="416" height="480">项的系数是（    ）.</p>
<p class="local-docx-line">A．132B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-067-e3be9bc42c.png" alt="本地解析几何资料图片" width="896" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-068-1b95a72f3b.png" alt="本地解析几何资料图片" width="704" height="448">D．66</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-228-8b5f29ed9f.png" alt="本地解析几何资料图片" width="1440" height="1152">的展开式中只有第7项的二项式系数最大，则展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-229-5e7a78d8da.png" alt="本地解析几何资料图片" width="416" height="480">项的系数是（    ）.</p>
<p class="local-docx-line">A．132B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-230-e3be9bc42c.png" alt="本地解析几何资料图片" width="896" height="448">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-231-1b95a72f3b.png" alt="本地解析几何资料图片" width="704" height="448">D．66</p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-232-8b5f29ed9f.png" alt="本地解析几何资料图片" width="1440" height="1152">展开式中只有第7项的二项式系数最大，</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-233-b01ad241b7.png" alt="本地解析几何资料图片" width="320" height="352">为偶数，展开式有13项，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-234-079273786c.png" alt="本地解析几何资料图片" width="1056" height="448">，</p>
<p class="local-docx-line">所以二项式展开式的通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-235-7af9eee5d9.png" alt="本地解析几何资料图片" width="5760" height="1184"></p>
<p class="local-docx-line">由<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-236-d9e3fd5db7.png" alt="本地解析几何资料图片" width="1760" height="448">得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-237-05f3195aef.png" alt="本地解析几何资料图片" width="864" height="416">，</p>
<p class="local-docx-line">所以展开式中含<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-238-5e7a78d8da.png" alt="本地解析几何资料图片" width="416" height="480">项的系数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-239-d7c0f0cbdc.png" alt="本地解析几何资料图片" width="1376" height="608">.</p>
<p class="local-docx-line">故选：D</p>
</div>
:::

:::

### 题 47（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-069-7ca4ed774f.png" alt="本地解析几何资料图片" width="1184" height="576">的展开式中第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-070-1c19950b7f.png" alt="本地解析几何资料图片" width="320" height="416">项与第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-071-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">项的二项式系数相等，则奇数项的二项式系数和为（    ）．</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-072-ceb0aad405.png" alt="本地解析几何资料图片" width="512" height="480">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-073-c72d366009.png" alt="本地解析几何资料图片" width="512" height="480">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-074-70725c1dff.png" alt="本地解析几何资料图片" width="512" height="480">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-075-89d3ea74f4.png" alt="本地解析几何资料图片" width="448" height="480"></p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．已知<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-240-7ca4ed774f.png" alt="本地解析几何资料图片" width="1184" height="576">的展开式中第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-241-1c19950b7f.png" alt="本地解析几何资料图片" width="320" height="416">项与第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-242-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">项的二项式系数相等，则奇数项的二项式系数和为（    ）．</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-243-ceb0aad405.png" alt="本地解析几何资料图片" width="512" height="480">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-244-c72d366009.png" alt="本地解析几何资料图片" width="512" height="480">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-245-70725c1dff.png" alt="本地解析几何资料图片" width="512" height="480">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-246-89d3ea74f4.png" alt="本地解析几何资料图片" width="448" height="480"></p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-247-7ca4ed774f.png" alt="本地解析几何资料图片" width="1184" height="576">的展开式中第4项与第8项的二项式系数相等，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-248-06cc01cdd1.png" alt="本地解析几何资料图片" width="56" height="25">，解得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-249-962c4aab4d.png" alt="本地解析几何资料图片" width="44" height="19">，</p>
<p class="local-docx-line">所以二项式<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-250-6914c83e61.png" alt="本地解析几何资料图片" width="1248" height="576">中奇数项的二项式系数和为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-251-31377b04b6.png" alt="本地解析几何资料图片" width="76" height="41">．</p>
</div>
:::

:::

### 题 48（原题 4）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">4．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-076-cbe81aa1f4.png" alt="本地解析几何资料图片" width="1760" height="992">展开式中只有第四项的系数最大，则展开式中有理项的项数为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-077-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-078-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-079-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-080-1c19950b7f.png" alt="本地解析几何资料图片" width="320" height="416"></p>
<p class="local-docx-line">【题组五  整除问题】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">4．若<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-252-cbe81aa1f4.png" alt="本地解析几何资料图片" width="1760" height="992">展开式中只有第四项的系数最大，则展开式中有理项的项数为（    ）</p>
<p class="local-docx-line">A．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-253-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">B．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-254-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">C．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-255-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">D．<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-256-1c19950b7f.png" alt="本地解析几何资料图片" width="320" height="416"></p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-257-f43a0f5cb4.png" alt="本地解析几何资料图片" width="1888" height="1184">展开式中只有第四项的系数最大，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-258-3abcbefc15.png" alt="本地解析几何资料图片" width="896" height="448">，</p>
<p class="local-docx-line">则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-259-698242e2fe.png" alt="本地解析几何资料图片" width="1856" height="1184">展开式通项为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-260-0c850e5e20.png" alt="本地解析几何资料图片" width="5312" height="1184">，</p>
<p class="local-docx-line">因为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-261-a087e2d190.png" alt="本地解析几何资料图片" width="1408" height="448">，所以当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-262-fcbfcf3835.png" alt="本地解析几何资料图片" width="1856" height="512">时为有理项，所以有理项共有4项，故选：D.</p>
<p class="local-docx-line">【题组五  整除问题】</p>
</div>
:::

:::

### 题 49（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1.<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-081-cf8d7313ec.png" alt="本地解析几何资料图片" width="4832" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-082-5f1cbb1004.png" alt="本地解析几何资料图片" width="1536" height="608">除以88的余数是（ ）</p>
<p class="local-docx-line">A．－1B．1C．－87D．87</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1.<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-263-cf8d7313ec.png" alt="本地解析几何资料图片" width="4832" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-264-5f1cbb1004.png" alt="本地解析几何资料图片" width="1536" height="608">除以88的余数是（ ）</p>
<p class="local-docx-line">A．－1B．1C．－87D．87</p>
<p class="local-docx-line">【答案】B</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-265-cf8d7313ec.png" alt="本地解析几何资料图片" width="4832" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-266-5f1cbb1004.png" alt="本地解析几何资料图片" width="1536" height="608"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-267-22f9fc2bd7.png" alt="本地解析几何资料图片" width="3520" height="704"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-268-c1ee637713.png" alt="本地解析几何资料图片" width="4736" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-269-0ff06e1112.png" alt="本地解析几何资料图片" width="1536" height="608"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-270-5e97d1ac27.png" alt="本地解析几何资料图片" width="4704" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-271-c3bc4c7e9c.png" alt="本地解析几何资料图片" width="1600" height="608">,</p>
<p class="local-docx-line">所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-272-cf8d7313ec.png" alt="本地解析几何资料图片" width="4832" height="608">…<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-273-5f1cbb1004.png" alt="本地解析几何资料图片" width="1536" height="608">除以88的余数是1，</p>
<p class="local-docx-line">故选:B.</p>
</div>
:::

:::

### 题 50（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2.<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-083-786663ef9d.png" alt="本地解析几何资料图片" width="6688" height="608">除以5的余数是</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2.<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-274-786663ef9d.png" alt="本地解析几何资料图片" width="6688" height="608">除以5的余数是</p>
<p class="local-docx-line">【答案】3</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-275-786663ef9d.png" alt="本地解析几何资料图片" width="6688" height="608"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-276-96d1b630d3.png" alt="本地解析几何资料图片" width="5408" height="576">，它除以5余数为3．</p>
</div>
:::

:::

### 题 51（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3.5051﹣1被7除后的余数为_____．</p>
<p class="local-docx-line">【题组六 杨辉三角】</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3.5051﹣1被7除后的余数为_____．</p>
<p class="local-docx-line">【答案】0</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-277-d424c4643d.png" alt="本地解析几何资料图片" width="9632" height="608"></p>
<p class="local-docx-line"><img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-278-69b35ff7ff.png" alt="本地解析几何资料图片" width="4960" height="608"></p>
<p class="local-docx-line">因为49是7的倍数，所以5051﹣1被7除后的余数为0.</p>
<p class="local-docx-line">故答案为：0</p>
<p class="local-docx-line">【题组六 杨辉三角】</p>
</div>
:::

:::

### 题 52（原题 1）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">1．将杨辉三角中的奇数换成1，偶数换成0，便可以得到如图的“0-1三角”.在“<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-084-eaa6f8ea5e.png" alt="本地解析几何资料图片" width="768" height="448">三角”中，从第1行起，设第n<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-085-d9a2234c3a.png" alt="本地解析几何资料图片" width="1440" height="576">次出现全行为1时，1的个数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-086-77783fb3a1.png" alt="本地解析几何资料图片" width="448" height="576">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-q-087-fcc7e743da.png" alt="本地解析几何资料图片" width="416" height="576">等于（　　）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-q-088-e55ee062a6.png" alt="本地解析几何资料图片" width="312" height="209"></div>
<p class="local-docx-line">A．13B．14C．15D．16</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">1．将杨辉三角中的奇数换成1，偶数换成0，便可以得到如图的“0-1三角”.在“<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-279-eaa6f8ea5e.png" alt="本地解析几何资料图片" width="768" height="448">三角”中，从第1行起，设第n<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-280-d9a2234c3a.png" alt="本地解析几何资料图片" width="1440" height="576">次出现全行为1时，1的个数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-281-77783fb3a1.png" alt="本地解析几何资料图片" width="448" height="576">，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-282-fcc7e743da.png" alt="本地解析几何资料图片" width="416" height="576">等于（　　）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-a-283-e55ee062a6.png" alt="本地解析几何资料图片" width="312" height="209"></div>
<p class="local-docx-line">A．13B．14C．15D．16</p>
<p class="local-docx-line">【答案】D</p>
<p class="local-docx-line">【解析】第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-284-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">行和第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-285-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">行全是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-286-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-287-39242318da.png" alt="本地解析几何资料图片" width="2048" height="576"></p>
<p class="local-docx-line">依题意，第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-288-7e53298fa7.png" alt="本地解析几何资料图片" width="288" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-289-e2650bd1a7.png" alt="本地解析几何资料图片" width="2848" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-290-894ec935b7.png" alt="本地解析几何资料图片" width="1088" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-291-745334cd75.png" alt="本地解析几何资料图片" width="288" height="416">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-292-c6d73d6e2b.png" alt="本地解析几何资料图片" width="2848" height="608">，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-293-a8a7760640.png" alt="本地解析几何资料图片" width="3136" height="512">全为奇数，一共有<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-294-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">个，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-295-90541afc19.png" alt="本地解析几何资料图片" width="992" height="576"></p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-296-674c1f29f5.png" alt="本地解析几何资料图片" width="288" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-297-eb2407f8b7.png" alt="本地解析几何资料图片" width="2816" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-298-97ff50fe79.png" alt="本地解析几何资料图片" width="1056" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-299-9ff754a456.png" alt="本地解析几何资料图片" width="288" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-300-8f839e1b89.png" alt="本地解析几何资料图片" width="2848" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-301-e3a6bd0a56.png" alt="本地解析几何资料图片" width="1312" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-302-215a2c175b.png" alt="本地解析几何资料图片" width="448" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-303-e2b19a40ef.png" alt="本地解析几何资料图片" width="3072" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-304-eb1c81d863.png" alt="本地解析几何资料图片" width="1344" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-305-60ac703595.png" alt="本地解析几何资料图片" width="458" height="458">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-306-5db8ecf71c.png" alt="本地解析几何资料图片" width="3008" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-307-d26402ab1a.png" alt="本地解析几何资料图片" width="1536" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-308-37ac56a233.png" alt="本地解析几何资料图片" width="448" height="416">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-309-c76007f71b.png" alt="本地解析几何资料图片" width="3072" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-310-9a36499df0.png" alt="本地解析几何资料图片" width="1344" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-311-11562c24ff.png" alt="本地解析几何资料图片" width="448" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-312-44953f7b69.png" alt="本地解析几何资料图片" width="3040" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-313-c0d8b90a45.png" alt="本地解析几何资料图片" width="1344" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-314-6928a88984.png" alt="本地解析几何资料图片" width="448" height="416">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-315-67221cd988.png" alt="本地解析几何资料图片" width="3072" height="608">，而<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-316-6d68f46932.png" alt="本地解析几何资料图片" width="1344" height="608">为偶数，不合题意；</p>
<p class="local-docx-line">第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-317-c22b54e1b3.png" alt="本地解析几何资料图片" width="448" height="448">行原来的数是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-318-21a8c666e5.png" alt="本地解析几何资料图片" width="3040" height="608"></p>
<p class="local-docx-line">即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-319-5dbeca4e38.png" alt="本地解析几何资料图片" width="11232" height="512">，全为奇数，即<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-320-1e06ecad8f.png" alt="本地解析几何资料图片" width="1184" height="576">故选：D</p>
</div>
:::

:::

### 题 53（原题 2）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">2．如图所示的三角形数组是我国古代数学家杨辉发现的，称为杨辉三角形，根据数组中的数构成的规律，其中的a所表示的数是（    ）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-q-089-9c0ab45400.png" alt="本地解析几何资料图片" width="227" height="176"></div>
<p class="local-docx-line">A．2B．4C．6D．8</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">2．如图所示的三角形数组是我国古代数学家杨辉发现的，称为杨辉三角形，根据数组中的数构成的规律，其中的a所表示的数是（    ）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-a-321-9c0ab45400.png" alt="本地解析几何资料图片" width="227" height="176"></div>
<p class="local-docx-line">A．2B．4C．6D．8</p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】从第三行起头尾两个数均为1，中间数等于上一行肩上两数之和，所以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-322-398a25a8e6.png" alt="本地解析几何资料图片" width="1760" height="416">.</p>
<p class="local-docx-line">故选：C.</p>
</div>
:::

:::

### 题 54（原题 3）

:::diagram
<div class="local-docx-card local-docx-question">
<p class="local-docx-line">3．我国南宋数学家杨辉1261年所著的《详解九章算法》一书里出现了如图所示的表，即杨辉三角，这是数学史上的一个伟大成就.在“杨辉三角”中，若去除所有为1的项，依次构成数列2，3，3，4，6，4，5，10，10，5，…，则此数列的前56项和为（    ）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-q-090-2c031894b2.png" alt="本地解析几何资料图片" width="154" height="152"></div>
<p class="local-docx-line">A．2060B．2038C．4084D．4108</p>
</div>
:::

:::solution 查看解析版原文

:::diagram
<div class="local-docx-card local-docx-answer">
<p class="local-docx-line">3．我国南宋数学家杨辉1261年所著的《详解九章算法》一书里出现了如图所示的表，即杨辉三角，这是数学史上的一个伟大成就.在“杨辉三角”中，若去除所有为1的项，依次构成数列2，3，3，4，6，4，5，10，10，5，…，则此数列的前56项和为（    ）</p>
<div class="local-docx-figure"><img class="local-docx-image local-docx-block-image" src="../../../assets/counting-local/ct35-a-323-2c031894b2.png" alt="本地解析几何资料图片" width="154" height="152"></div>
<p class="local-docx-line">A．2060B．2038C．4084D．4108</p>
<p class="local-docx-line">【答案】C</p>
<p class="local-docx-line">【解析】<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-324-b01ad241b7.png" alt="本地解析几何资料图片" width="320" height="352">次二项式系数对应杨辉三角形的第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-325-dc2f4f88f0.png" alt="本地解析几何资料图片" width="768" height="448">行，例如<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-326-cfaebdaa74.png" alt="本地解析几何资料图片" width="3168" height="704">，系数分别为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-327-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-328-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-329-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">，对应杨辉三角形的第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-330-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">行，</p>
<p class="local-docx-line">令<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-331-a512a403ab.png" alt="本地解析几何资料图片" width="832" height="448">，就可以求出该行的系数之和；第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-332-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">行为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-333-6c2a946d81.png" alt="本地解析几何资料图片" width="448" height="480">，第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-334-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">行为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-335-8da074f986.png" alt="本地解析几何资料图片" width="384" height="480">，第<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-336-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">行为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-337-6a00fea443.png" alt="本地解析几何资料图片" width="448" height="480">，以此类推，即每一行数字之和构成首项是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-338-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">，公比是<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-339-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">的等比数列，</p>
<p class="local-docx-line">则杨辉三角形的前<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-340-b01ad241b7.png" alt="本地解析几何资料图片" width="320" height="352">行的和为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-341-94f90251a5.png" alt="本地解析几何资料图片" width="2944" height="1056">，</p>
<p class="local-docx-line">若去除所有为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-342-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">的项，则剩下的每一行的个数为<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-343-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-344-8ddef9d0e2.png" alt="本地解析几何资料图片" width="320" height="416">，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-345-6da24262de.png" alt="本地解析几何资料图片" width="288" height="448">，...，可看成以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-346-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">为首项，以<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-347-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">为公差的等差数列，则<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-348-1e0b7401ea.png" alt="本地解析几何资料图片" width="2016" height="992">，</p>
<p class="local-docx-line">当<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-349-079273786c.png" alt="本地解析几何资料图片" width="1056" height="448">时，<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-350-1088536d05.png" alt="本地解析几何资料图片" width="2688" height="992">，去除两端的<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-351-8215aa87bc.png" alt="本地解析几何资料图片" width="224" height="416">可得<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-352-b47ab302cc.png" alt="本地解析几何资料图片" width="1952" height="448">，</p>
<p class="local-docx-line">则此数列的前<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-353-110d81a533.png" alt="本地解析几何资料图片" width="480" height="448">项的和为：<img class="local-docx-image local-docx-inline-image" src="../../../assets/counting-local/ct35-a-354-e5c5a7e081.png" alt="本地解析几何资料图片" width="5792" height="608">.故选：C.</p>
</div>
:::

:::

## 抽取统计

- 全量原卷题目：54 道。
- 可折叠解析版题块：54 道。

- 考点 33 两个计数原理：原卷 14 道，解析版原始抽取 14 道，可对齐显示 14 道。
- 考点 34 排列、组合：原卷 11 道，解析版原始抽取 11 道，可对齐显示 11 道。
- 考点 35 二项式定理：原卷 29 道，解析版原始抽取 29 道，可对齐显示 29 道。
