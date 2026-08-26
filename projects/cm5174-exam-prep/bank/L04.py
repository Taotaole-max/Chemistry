# -*- coding: utf-8 -*-
LEC = 4
TITLE = "Phase Behavior of Polymer Solutions"
CN = "高分子溶液的相行为"
SRC = "讲义 Lectures_1-4"
L = [
dict(kind="理解", topic="相的定义", ans=1,
 stem="According to the lecture, a 'phase' signifies a state of matter that is uniform throughout in:",
 opts=["Chemical composition only", "Both <b>chemical composition</b> and <b>physical state</b>",
       "Physical state only", "Temperature and pressure only"],
 exp="""<p>讲义原文：<i>“Phase signifies a state of matter that is uniform throughout,
<b>not only in chemical composition but also in physical state</b>”</i>。</p>
<p><b>两个条件缺一不可</b>：<br>
· 冰水混合物——化学组成相同（都是 H₂O），但<b>物理状态不同</b> → <b>2 相</b><br>
· 油水混合物——物理状态相同（都是液体），但<b>化学组成不同</b> → <b>2 相</b></p>""",
 kp="相 = 化学组成与物理状态都均一的部分；两个条件都要满足",
 src="p.48「Definition of Phase」"),

dict(kind="理解", topic="数相", ans=2,
 stem="How many phases are present in each? (i) Ice-blended café latte　(ii) Nitrogen and argon in a cylinder　(iii) Clear bar soap with essential oil fragrance　(iv) A teaspoon of NaCl in 1 L of water",
 opts=["1, 1, 2, 1", "2, 1, 1, 2", "2, 1, 1, 1", "2, 2, 1, 2"],
 exp="""<table class="mini"><thead><tr><th>体系</th><th>相数</th><th>理由</th></tr></thead><tbody>
<tr><td>(i) 冰沙拿铁</td><td><b>2</b></td><td>固态冰 + 液体，<b>物理状态</b>不同</td></tr>
<tr><td>(ii) 氮气 + 氩气</td><td><b>1</b></td><td>气体<b>永远互溶</b>（ΔG<sub>mix</sub> 恒负）</td></tr>
<tr><td>(iii) 透明香皂 + 精油</td><td><b>1</b></td><td><b>"clear"（透明）是关键词</b>——不散射光说明均一</td></tr>
<tr><td>(iv) 一勺 NaCl 溶于 1 L 水</td><td><b>1</b></td><td>量很少，完全溶解成均一溶液</td></tr>
</tbody></table>
<p class="trap"><b>(iii) 的判断技巧</b>：<b>透明 = 单相</b>。若分成两相，两相折射率不同就会散射光而<b>发浑</b>
——这与 Lecture 8「半结晶高分子发白」是同一个光学原理。</p>""",
 kp="数相看组成与状态是否均一；「透明」是单相的实验判据",
 src="官方 Question 12（对应 p.48）"),

dict(kind="理解", topic="临界点", ans=0,
 stem="On a temperature–composition phase diagram, the critical point T<sub>c</sub> marks the temperature above which:",
 opts=["<b>All</b> compositions of the mixture exist as one phase",
       "All compositions phase separate", "Only the 50:50 composition is stable",
       "The solvent boils"],
 exp="""<p>讲义原文：<i>“Critical point (T<sub>c</sub>) – above this temperature,
<b>all compositions</b> of mixture exist as 1 phase”</i>。</p>
<p><b>物理含义</b>：温度足够高时，−TΔS 这个有利项压过焓项 x<sub>A</sub>x<sub>B</sub>χ
（而且 χ ∝ 1/T 本身也随升温减小），ΔG 曲线全程<b>凹向上</b>，"鼓包"消失 → 任何组成都不分相。</p>
<p class="trap">这里说的是 <b>UCST</b> 型（上临界共溶温度）。<b>LCST</b> 型正相反——
<b>低于</b>某温度才全部互溶。</p>""",
 kp="UCST 的 T_c 之上任何组成都单相；LCST 则相反",
 src="p.49「Critical point (T_c)」"),

dict(kind="理解", topic="binodal 的定义", ans=1,
 stem="The <b>binodal</b> (coexistence curve) is the boundary under which:",
 opts=["Phase separation is always spontaneous and barrier-free",
       "Phase separation is <b>thermodynamically favoured</b>, though the solution may still persist as a metastable single phase",
       "The solution is always stable", "The polymer crystallizes"],
 exp="""<p>讲义原文：<i>“Binodal (coexistence curve) – Boundary, under which, phase separation
(into 2 phases) is <b>thermodynamically favoured</b>. However, solution <b>may still exist in
metastable state</b>.”</i></p>
<p class="trap"><b>关键区分</b>：</p>
<table class="mini"><thead><tr><th></th><th>binodal 之下</th><th>spinodal 之下</th></tr></thead><tbody>
<tr><td>热力学上分相有利？</td><td><b>是</b></td><td><b>是</b></td></tr>
<tr><td>会自发立即发生？</td><td><b>不一定</b>（可亚稳）</td><td><b>是</b>（无势垒）</td></tr>
</tbody></table>
<p>binodal 与 spinodal 之间就是<b>亚稳区</b>，需要成核才能启动分相。</p>""",
 kp="binodal 之下分相有利但可亚稳；spinodal 之下才无势垒自发",
 src="p.49「Binodal (coexistence curve)」"),

dict(kind="理解", topic="spinodal 的定义", ans=2,
 stem="The <b>spinodal</b> (stability limit) is the boundary below which:",
 opts=["The solution becomes more stable", "Nucleation is required for phase separation",
       "Phase separation is <b>spontaneous</b> (no activation barrier)", "The mixture becomes a single phase"],
 exp="""<p>讲义原文：<i>“Spinodal (stability limit) – Boundary to solution stability.
Phase separation is <b>spontaneous</b> for compositions under this boundary.”</i></p>
<p><b>数学上</b>它是 ΔG 曲线的<b>拐点</b>连线（d²ΔG/dx² = 0）。
拐点以内曲线<b>凹向下</b>，任何微小的组成涨落都<b>降低</b> Gibbs 能，因此<b>没有势垒</b>，
分相在整个体积内立刻同时开始——这就是 <b>spinodal decomposition</b>。</p>""",
 kp="spinodal 内无活化势垒，分相自发且遍及全体积",
 src="p.49「Spinodal (stability limit)」"),

dict(kind="理解", topic="ΔH 与 ΔS 的组成依赖", ans=3,
 stem="Both ΔH<sub>mix</sub> = x<sub>A</sub>x<sub>B</sub>χnRT and ΔS<sub>mix</sub> = −nR(x<sub>A</sub>lnx<sub>A</sub> + x<sub>B</sub>lnx<sub>B</sub>) share which feature?",
 opts=["Both are always negative", "Both are independent of composition",
       "Both are largest at x<sub>A</sub> → 0", "Both are largest in magnitude when the two components contribute roughly <b>equally</b>"],
 exp="""<p>讲义原文：<i>“Entropy of mixing and enthalpy of mixing <b>highest</b> when each component
contributes approximately <b>equal amounts</b> to mixture”</i>——即两条曲线都在 x ≈ 0.5 处取极值。</p>
<p>· x<sub>A</sub>x<sub>B</sub> 在 x = 0.5 时最大（= 0.25）<br>
· −(x lnx + x lnx) 在 x = 0.5 时最大（= ln2 = 0.693）</p>
<p class="trap"><b>但符号相反</b>：ΔS 恒正（有利），χ &gt; 0 时 ΔH 恒正（不利）。
正因为两者<b>形状相似、方向相反</b>，它们的竞争才可能在中间产生"鼓包"。</p>
<p>讲义还提醒：<b>真实高分子溶液的曲线并不对称</b>（因为 φ<sub>B</sub>/N 那一项）。</p>""",
 kp="ΔH 与 ΔS 都在等量组成处最大，但符号相反；高分子体系不对称",
 src="p.50「Recall that, in regular solutions」"),

dict(kind="理解", topic="高温与低温的差异", ans=1,
 stem="Why does a 'local maximum' bump appear in the ΔG<sub>mix</sub> curve at <b>low</b> temperature but not at high temperature?",
 opts=["Because ΔS becomes negative at low T",
       "Because χ ∝ 1/T grows at low T, so the <b>enthalpy contribution becomes relatively larger</b> than the entropy contribution",
       "Because the solvent freezes", "Because ΔH becomes zero at low T"],
 exp="""<p>把方程除以 RT 来看清竞争：</p>
<div class="fb">ΔG<sub>mix</sub>/(RT) = ΔH<sub>mix</sub>/(RT) − ΔS<sub>mix</sub>/R</div>
<p>讲义原话：<br>
· <b>高温</b>：χ 小（χ = zΔw/kT），<b>混合主要由熵支配</b> → 曲线全程凹向上<br>
· <b>低温</b>：<b>焓的贡献相对高于熵的贡献</b> → 在 ΔG 曲线中间造成一个 <b>local maximum</b></p>
<p>正是这个"鼓包"让分相成为可能——没有它，曲线处处凹向上，永远单相。</p>""",
 kp="低温时焓项相对增强 → ΔG 曲线出现局部极大 → 才可能分相",
 src="p.51「At high temperature… At low temperature…」"),

dict(kind="理解", topic="凹凸性判据", ans=0,
 stem="A mixture will <b>not</b> phase separate as long as the ΔG<sub>mix</sub> curve is:",
 opts=["Concave <b>upwards</b> in that region", "Concave downwards", "Negative", "Positive"],
 exp="""<p>讲义原文：<i>“This happens as long as the ΔG curve is <b>concave upwards</b>”</i>
（不分相），以及 <i>“Phase separation happens as long as the ΔG curve is <b>concave downwards</b>”</i>。</p>
<p><b>几何论证</b>：把组成为 x<sub>A</sub> 的单相拆成 x<sub>A</sub>′ 和 x<sub>A</sub>″ 两相，
两相体系的 ΔG 等于<b>连接曲线上两点的直线</b>在 x<sub>A</sub> 处的高度（按杠杆规则加权平均）。</p>
<p>· 曲线<b>凹向上</b> → 弦<b>高于</b>曲线 → 分相<b>升高</b>能量 → <b>不分相</b><br>
· 曲线<b>凹向下</b> → 弦<b>低于</b>曲线 → 分相<b>降低</b>能量 → <b>分相</b></p>
<p>讲义强调：<b>无论怎么选 x<sub>A</sub>′ 和 x<sub>A</sub>″，结论都一样。</b></p>""",
 kp="凹向上不分相、凹向下分相；判据是曲率不是 ΔG 的符号",
 src="p.52–54「Analysing if phase separation is thermodynamically favourable」"),

dict(kind="理解", topic="ΔG<0 与分相的关系", ans=0,
 stem="Assuming x<sub>A</sub> = 0.5 and the ΔG<sub>mix</sub> curve has a local maximum there, will the mixture phase separate — even though ΔG<sub>mix</sub> is negative?",
 opts=["Yes — an even lower Gibbs energy can be achieved through phase separation",
       "No — a negative ΔG<sub>mix</sub> guarantees a single phase",
       "No — phase separation requires ΔG<sub>mix</sub> &gt; 0",
       "Cannot be determined from ΔG<sub>mix</sub>"],
 exp="""<p>讲义给的答案：<i>“<b>Phase separate</b> (even when Gibbs energy of mixing is negative).
<b>Even lower Gibbs energy can be achieved through phase separation.</b>”</i></p>
<p class="trap">⚠️ <b>这是本讲最容易错的概念</b>。要分清两个不同的比较：</p>
<table class="mini"><thead><tr><th>比较</th><th>回答的问题</th></tr></thead><tbody>
<tr><td>ΔG<sub>mix</sub> vs 0</td><td>"混合"比"完全不混"好吗？</td></tr>
<tr><td><b>曲线 vs 公切线</b></td><td>"单相"比"分成两相"好吗？<b>← 这才是分相判据</b></td></tr>
</tbody></table>
<p>ΔG<sub>mix</sub> &lt; 0 只回答了第一个问题。<b>第二个问题要看曲率。</b></p>""",
 kp="ΔG_mix<0 只说明混合优于完全不混；分相与否要比较曲线与公切线",
 src="官方 Question 13（对应 p.52–55）"),

dict(kind="理解", topic="binodal 点的作图求法", ans=2,
 stem="Graphically, the two binodal compositions at a given temperature are found by:",
 opts=["Locating the minimum of the ΔG curve", "Locating the inflection points",
       "Drawing the <b>common tangent</b> that touches the ΔG curve at two points",
       "Drawing a horizontal line through ΔG = 0"],
 exp="""<p>讲义原文：<i>“We draw a <b>tangent line that touches the ΔG curve at the two concave points</b>.
Any compositions within the two points prefers to phase separate to achieve lower energy.
These two points define the <b>binodal points</b> at each temperature.”</i></p>
<p><b>公切线的意义</b>：切点处两相的<b>化学势相等</b>（这正是相平衡条件），
所以公切线给出的是<b>平衡共存的两个组成</b>。</p>
<p>讲义也坦白：<i>“We can find the points mathematically, but this is <b>algebraically tedious</b>”</i>
——所以考试更可能考<b>作图理解</b>而不是解析求解。</p>""",
 kp="binodal = 公切线的两个切点，对应两相化学势相等",
 src="p.55「Finding the Binodal points」"),

dict(kind="计算", topic="spinodal 的数学条件", ans=1,
 stem="Mathematically, the spinodal points are located by solving:",
 opts=["dΔG<sub>m</sub>/dx<sub>A</sub> = 0", "d²ΔG<sub>m</sub>/dx<sub>A</sub>² = 0",
       "d³ΔG<sub>m</sub>/dx<sub>A</sub>³ = 0", "ΔG<sub>m</sub> = 0"],
 exp="""<p>spinodal 点 a 和 b 是曲线<b>由凹向上转为凹向下</b>的位置，即<b>拐点</b>：</p>
<div class="fb">d²ΔG<sub>m</sub> / dx<sub>A</sub>² = 0</div>
<p>讲义原文：<i>“Points a and b occur where the ΔG curve switches from concave up to concave down.
These are known as <b>inflection points</b>.”</i></p>
<p><b>三个判据一起记</b>：</p>
<table class="mini"><thead><tr><th>目标</th><th>条件</th></tr></thead><tbody>
<tr><td>Binodal</td><td>公切线（作图）</td></tr>
<tr><td><b>Spinodal</b></td><td><b>二阶导 = 0</b></td></tr>
<tr><td>临界点</td><td>三阶导 = 0</td></tr>
</tbody></table>""",
 kp="spinodal ⟺ 拐点 ⟺ d²ΔG/dx² = 0", src="p.58「Finding the Spinodal」"),

dict(kind="计算", topic="临界点的数学条件", ans=2,
 stem="The critical point is located by solving:",
 opts=["dΔG<sub>m</sub>/dx<sub>A</sub> = 0", "d²ΔG<sub>m</sub>/dx<sub>A</sub>² = 0",
       "d³ΔG<sub>m</sub>/dx<sub>A</sub>³ = 0", "ΔH<sub>mix</sub> = 0"],
 exp="""<div class="fb">d³ΔG<sub>m</sub> / dx<sub>A</sub>³ = 0</div>
<p>讲义原文：<i>“The critical point is the temperature and x<sub>A</sub> composition where the
'local maximum' bump <b>first appears</b> on the ΔG curve. The <b>inflection points merge</b> at this point.”</i></p>
<p><b>为什么是三阶导</b>：两个拐点（二阶导的两个根）在临界点<b>重合成一个二重根</b>，
这要求二阶导的导数也为零，即三阶导 = 0。</p>
<p class="trap">临界点<b>同时</b>满足 d²ΔG/dx² = 0 和 d³ΔG/dx³ = 0
——它是 binodal 与 spinodal 两条曲线的<b>交汇顶点</b>。</p>""",
 kp="临界点 = 两拐点合并 ⟺ 二阶导与三阶导同时为零",
 src="p.59「Finding the Critical point (T_c)」"),

dict(kind="理解", topic="亚稳区的微观论证", ans=1,
 stem="Why is a composition lying between x<sub>A</sub>′ (binodal) and a (spinodal) <b>metastable</b>?",
 opts=["Because ΔG<sub>mix</sub> is positive there",
       "Because that part of the curve is concave <b>upwards</b>, so any <b>small</b> local fluctuation raises G and is rejected",
       "Because the temperature is above T<sub>c</sub>", "Because the composition is exactly 0.5"],
 exp="""<p>讲义的论证很精妙：分相<b>必须先经历小幅的局部组成涨落</b>（这种涨落时刻在发生）。</p>
<p>在 x<sub>A</sub>′ 与 a 之间，曲线<b>凹向上</b> → <b>任何小尺度的分相都不利</b>
（即便大尺度分相到 x<sub>A</sub>′ 和 x<sub>A</sub>″ 是有利的）→ 涨落自动退回 → <b>亚稳</b>。</p>
<p>而在 a 与 b 之间，曲线<b>凹向下</b> → 任何涨落都有利 → 体系<b>无能垒</b>地走向分相。</p>
<p class="trap"><b>核心矛盾</b>：大尺度分相有利，但<b>通往它的小尺度路径不利</b>——
这就是活化势垒的来源，也是"亚稳"与"不稳"的分界。</p>""",
 kp="亚稳的本质：大尺度分相有利但小尺度路径不利 → 存在活化势垒",
 src="p.56–57「Finding the Spinodal – Why?」"),

dict(kind="理解", topic="N 增大对相图的影响", ans=1,
 stem="According to the general conclusions for polymer solution phase diagrams, increasing N:",
 opts=["Lowers T<sub>c</sub> and shifts the diagram to higher φ<sub>B</sub>",
       "<b>Raises</b> T<sub>c</sub> and shifts the diagram to <b>lower</b> φ<sub>B</sub>",
       "Raises T<sub>c</sub> and shifts to higher φ<sub>B</sub>", "Has no effect"],
 exp="""<p>讲义 General conclusions 原文：<br>
① <i>“Critical point <b>increases</b> as polymer degree of polymerization (N) increases”</i><br>
② <i>“Phase diagram shifts towards <b>smaller</b> polymer volume fraction φ<sub>B</sub> as N increases
(means <b>only dilute samples can dissolve</b>)”</i></p>
<p><b>根源</b>：ΔS<sub>mix</sub> 中高分子项被 N 削弱，而焓项不被削弱
→ 需要更高温度才能压过焓 → T<sub>c</sub> 升高、单相区缩小。</p>
<p class="trap"><b>实验含义</b>：同一种高分子，分子量越高<b>越难溶</b>，而且<b>只能配稀溶液</b>——
想配浓一点就分相。这在实际配溶液时是天天遇到的现象。</p>""",
 kp="N↑ → T_c↑、相图移向小 φ_B；高分子量只能配稀溶液",
 src="p.60「Phase Diagram of Polymer Solutions – General conclusions」"),

dict(kind="理解", topic="LCST 的经验式", ans=1,
 stem="LCST behaviour (phase separation on <b>heating</b>) is described empirically by χ = α/T + β with:",
 opts=["α positive, β negative", "α <b>negative</b>, β <b>positive</b>", "α = β = 0", "α positive, β = 0"],
 exp="""<p>讲义原文：<i>“When <b>α is negative and β is positive</b>, higher temp. causes χ to be more positive.
This causes mixing to be less spontaneous at higher temperature, and phase separation occurs.”</i></p>
<p><b>为什么需要经验式</b>：理论式 χ = zΔw/kT <b>只能给出 UCST</b>（χ 随 T 单调下降）。
要描述 LCST，必须允许 χ 随 T <b>上升</b>，这就需要一个正的常数项 β。</p>
<p><b>讲义给的例子</b>：<b>聚环氧乙烷（PEO）/ 水</b>，机理是靠<b>氢键</b>溶解，
而<b>氢键在高温下变弱</b> → 高温时溶剂-高分子作用变差 → 分相。</p>
<p class="trap">讲义标题写的是 <b>“Less Usual Case of LCST”</b>——LCST 是<b>少见</b>情形，
UCST 才是常态。</p>""",
 kp="LCST 需 α<0、β>0；典型例子 PEO/水（氢键随温度减弱）",
 src="p.61「Less Usual Case of Lower Critical Solution Temperature (LCST)」"),

dict(kind="理解", topic="spinodal decomposition 的触发", ans=2,
 stem="Spinodal decomposition occurs when a mixture is quenched from above T<sub>c</sub> to a temperature:",
 opts=["Above the binodal", "Between the binodal and the spinodal",
       "<b>Inside</b> the spinodal region", "Above T<sub>c</sub>"],
 exp="""<p>讲义原文：<i>“Assuming we quench the temperature of a mixture quickly from T₂ (high temp. above T<sub>c</sub>)
to T₁ <b>inside the spinodal region</b>, phase separation occurs. Mechanism is known as
<b>spinodal decomposition</b>.”</i></p>
<p><b>"快速淬冷"很关键</b>：如果慢慢降温，体系会在经过亚稳区时就通过成核完成分相，
到不了 spinodal 区。只有<b>快速</b>穿过亚稳区，才能把体系"困"在不稳区里，触发 SD。</p>""",
 kp="SD 需快速淬冷进入 spinodal 区；慢降温会先在亚稳区成核",
 src="p.62「Mechanism of Phase Separation – Spinodal Decomposition」"),

dict(kind="理解", topic="SD 的空间特征", ans=0,
 stem="During spinodal decomposition, composition fluctuations:",
 opts=["Occur throughout the <b>entire volume</b> of the mixture, and every fluctuation lowers G",
       "Occur only at container walls", "Occur only at a few nucleation sites",
       "Must exceed a critical size to grow"],
 exp="""<p>讲义原文：<i>“Composition fluctuates about x<sub>A</sub> <b>throughout entire volume</b> of the mixture.
Inside the spinodal region, <b>any fluctuation lowers the Gibbs energy</b>.
Separation into regions of different compositions is favoured <b>across entire mixture volume</b>.”</i></p>
<p><b>形貌后果</b>：在固体混合物中（高分子共混、金属合金），SD 给出特征性的
<b>互穿网络（interpenetrating network）</b>微结构——两相都是连续的，互相缠绕。</p>
<p class="trap">对比 N&amp;G 得到的是<b>分散的孤立液滴/颗粒</b>。
<b>看形貌就能反推机理</b>，这是材料表征中的常用手段。</p>""",
 kp="SD 遍及全体积、任何涨落都降 G → 互穿网络形貌",
 src="p.63–64「Spinodal Decomposition」"),

dict(kind="理解", topic="nucleation and growth 的触发", ans=1,
 stem="Nucleation and growth occurs when a mixture is quenched to a temperature that is:",
 opts=["Inside the spinodal", "<b>Outside</b> the spinodal but <b>inside</b> the binodal",
       "Above the binodal", "Above T<sub>c</sub>"],
 exp="""<p>讲义原文：<i>“Assuming we quench… to T₁ <b>outside the spinodal region (but inside binodal)</b>,
solution mixture remains <b>meta-stable</b>. Phase separation can occur, but goes through a
<b>nucleation and growth</b> mechanism.”</i></p>
<p>这就是<b>亚稳区</b>：热力学上分相有利，但小涨落被"顶回去"，必须等一次<b>足够大的偶然涨落</b>
才能越过势垒成核。</p>""",
 kp="N&G 发生在 binodal 内、spinodal 外的亚稳区", src="p.65「Nucleation and Growth」"),

dict(kind="理解", topic="N&G 的涨落行为", ans=1,
 stem="Outside the spinodal region, what happens to a <b>small</b> composition fluctuation?",
 opts=["It grows immediately", "It <b>raises</b> the Gibbs energy, so the composition normally returns to x<sub>A</sub>",
       "It lowers G and spreads", "It has no effect on G"],
 exp="""<p>讲义原文：<i>“Outside the spinodal region, any fluctuation <b>raises</b> the Gibbs energy.
Normally, the composition <b>returns to x<sub>A</sub></b>. However, <b>occasional large fluctuation</b>
can trigger nucleation and growth.”</i></p>
<p><b>触发条件的作图求法</b>：在 x<sub>A</sub> 处作<b>切线</b>，切线与曲线的另一个交点给出
<i>“first point where Gibbs energy of separated components ≤ Gibbs energy of mixture”</i>
——涨落必须达到<b>这个组成</b>才能成核。</p>
<p>越过之后，Gibbs 能开始下降，组成被<b>驱动</b>向 x<sub>A</sub>″，成核完成。</p>""",
 kp="亚稳区小涨落被退回，需大涨落越过切线交点才成核",
 src="p.66–67「Nucleation and Growth」"),

dict(kind="理解", topic="N&G 的生长阶段", ans=2,
 stem="After a nucleus forms, what drives its <b>growth</b>?",
 opts=["Only temperature gradients", "Only surface tension",
       "Growth is driven by the <b>lowering of Gibbs energy</b>, while diffusion is driven by the <b>composition gradient</b>",
       "Mechanical stirring"],
 exp="""<p>讲义原文：<i>“The A-enriched nucleus is surrounded by area <b>depleted of A</b>.
<b>Diffusion of A</b> occurs towards depleted regions, which in turn, feeds the growth of A-enriched nucleus.
<b>Growth is driven by the lowering of Gibbs energy, while diffusion is driven by composition gradient.</b>”</i></p>
<p><b>两个驱动力分工明确</b>：<br>
· <b>热力学驱动力</b>（ΔG 下降）决定"要不要长"<br>
· <b>动力学过程</b>（扩散）决定"长多快"</p>
<p>最终当达到最低 Gibbs 能时，扩散和生长<b>同时停止</b>——终态组成正是 binodal 组成。</p>""",
 kp="N&G：ΔG 下降驱动生长，组成梯度驱动扩散；两者共同决定动力学",
 src="p.68「Nucleation and Growth」"),

dict(kind="理解", topic="两种机理的终态", ans=2,
 stem="What are the <b>final</b> phase compositions after spinodal decomposition, compared with those after nucleation and growth?",
 opts=["SD gives spinodal compositions, N&amp;G gives binodal compositions",
       "SD gives binodal, N&amp;G gives spinodal", "<b>Both</b> give the binodal compositions",
       "Both give pure A and pure B"],
 exp="""<p>讲义对比表明确写着两者 <i>“Final compositions defined by <b>binodal</b> points”</i>。</p>
<p><b>为什么必然如此</b>：binodal 是<b>公切线的切点</b>，代表两相化学势相等的<b>真正平衡态</b>。
不论走哪条路径（无势垒的 SD，还是要成核的 N&amp;G），只要给足时间，
体系最终都落到<b>同一个平衡终点</b>。</p>
<p class="trap"><b>机理决定路径和形貌，热力学决定终点。</b>
官方 Question 15（SD）和 Question 16（N&amp;G）分别问终态，答案<b>相同</b>——就是考这个。</p>""",
 kp="两种机理终态相同（binodal 组成）；机理只影响路径与形貌",
 src="p.69「Spinodal Decomposition vs. Nucleation and Growth」；官方 Q15、Q16"),

dict(kind="理解", topic="两种机理的完整对比", ans=3,
 stem="Which row of the SD-vs-N&amp;G comparison is <b>INCORRECT</b>?",
 opts=["SD: occurs uniformly across entire mixture　|　N&amp;G: occurs sporadically",
       "SD: inside spinodal region　|　N&amp;G: outside spinodal region",
       "SD: no activation barrier　|　N&amp;G: has activation barrier",
       "SD: final compositions at spinodal　|　N&amp;G: final compositions at binodal"],
 exp="""<p>选 D，它是<b>错的</b>——<b>两者的终态组成都由 binodal 决定</b>。</p>
<p>讲义 p.69 的完整对比表：</p>
<table class="mini"><thead><tr><th></th><th>Spinodal Decomposition</th><th>Nucleation &amp; Growth</th></tr></thead><tbody>
<tr><td>空间分布</td><td>整个混合物<b>均匀</b>发生</td><td><b>零星散发</b>发生</td></tr>
<tr><td>区域</td><td>spinodal <b>内</b></td><td>spinodal <b>外</b></td></tr>
<tr><td>活化势垒</td><td><b>无</b></td><td><b>有</b></td></tr>
<tr><td>最终组成</td><td><b>binodal</b></td><td><b>binodal</b></td></tr>
</tbody></table>""",
 kp="四行对比表：分布、区域、势垒不同，终态相同",
 src="p.69「Spinodal Decomposition vs. Nucleation and Growth」"),

dict(kind="理解", topic="读 Gibbs 图：binodal 之外", ans=0,
 stem="Compounds A and B are mixed at a composition lying <b>outside</b> the two binodal points x<sub>A</sub>′ and x<sub>A</sub>″. What is the result?",
 opts=["1 phase with composition x<sub>A</sub>", "2 phases with compositions a and b",
       "2 phases with compositions x<sub>A</sub>′ and x<sub>A</sub>″", "2 phases of pure A and pure B"],
 exp="""<p>讲义给的答案：<i>“Compositions <b>outside</b> binodal points <b>do not phase separate</b>”</i>。</p>
<p>在 binodal 之外，ΔG 曲线<b>凹向上</b>，任何分相尝试都会升高能量 → <b>保持单相</b>。</p>
<p><b>三种情形的完整对照（必背）</b>：</p>
<table class="mini"><thead><tr><th>x<sub>A</sub> 的位置</th><th>结果</th><th>机理</th></tr></thead><tbody>
<tr><td>binodal <b>之外</b></td><td><b>单相</b></td><td>—</td></tr>
<tr><td>binodal 与 spinodal 之间</td><td>2 相 @ binodal</td><td><b>N&amp;G</b></td></tr>
<tr><td>spinodal <b>之内</b></td><td>2 相 @ binodal</td><td><b>SD</b></td></tr>
</tbody></table>""",
 kp="binodal 之外单相；三种位置对应三种结果，终态组成都是 binodal",
 src="官方 Question 17（对应 p.55）"),

dict(kind="理解", topic="读 Gibbs 图：spinodal 之内", ans=1,
 stem="A mixture at composition x<sub>A</sub> lying <b>inside</b> the spinodal (between a and b) undergoes spinodal decomposition. The resulting composition is:",
 opts=["1 phase with x<sub>A</sub>", "2 phases with compositions x<sub>A</sub>′ and x<sub>A</sub>″ (the binodal points)",
       "2 phases with compositions a and b (the spinodal points)", "2 phases of pure A and pure B"],
 exp="""<p>讲义给的答案：<i>“<b>Spinodal decomposition stops at binodal compositions</b>”</i>。</p>
<p><b>过程</b>：涨落在整个体积内被放大 → 组成不断向两端演化 →
一直演化到 <b>x<sub>A</sub>′ 和 x<sub>A</sub>″</b> 才停下（这时 Gibbs 能达到公切线给出的最低值）。</p>
<p class="trap"><b>易错点</b>：以为分相"停在" spinodal 点 a 和 b（选项 C）。<b>不对</b>——
a 和 b 只是<b>不稳区的边界</b>，标志"何时无势垒"，不是平衡组成。<b>平衡组成永远是 binodal。</b></p>""",
 kp="SD 停在 binodal 组成，不是 spinodal 组成；a、b 只是稳定性边界",
 src="官方 Question 15（对应 p.63–64）"),

dict(kind="理解", topic="读 Gibbs 图：亚稳区", ans=1,
 stem="A mixture at composition x<sub>A</sub> lying between x<sub>A</sub>′ and a (the metastable region) eventually phase separates by nucleation and growth. The final composition is:",
 opts=["1 phase with x<sub>A</sub>", "2 phases with compositions x<sub>A</sub>′ and x<sub>A</sub>″",
       "2 phases with compositions a and b", "2 phases of pure A and pure B"],
 exp="""<p>讲义给的答案：<i>“<b>Nucleation and growth stops at binodal compositions</b>”</i>。</p>
<p>与 SD 完全一样的终点——因为 binodal 是<b>热力学平衡</b>的定义，与到达路径无关。</p>
<p><b>两条路径的差别只在过程</b>：</p>
<table class="mini"><thead><tr><th></th><th>起步</th><th>过程</th></tr></thead><tbody>
<tr><td>SD</td><td>立即，全体积</td><td>组成连续演化</td></tr>
<tr><td>N&amp;G</td><td>要等大涨落</td><td>成核 + 扩散喂养生长</td></tr>
</tbody></table>
<p>但两条路径的<b>终点相同</b>。</p>""",
 kp="N&G 同样停在 binodal 组成；路径不同、终点相同",
 src="官方 Question 16（对应 p.66–68）"),

dict(kind="理解", topic="相图与 ΔG 曲线的对应", ans=2,
 stem="Moving <b>down</b> in temperature on a UCST phase diagram, the ΔG<sub>mix</sub> curve changes how?",
 opts=["It becomes a straight line", "It flattens and loses its minimum",
       "A local maximum ('bump') appears and deepens, and the two inflection points <b>move apart</b>",
       "It shifts upward but keeps the same shape"],
 exp="""<p><b>降温过程中</b>：χ ∝ 1/T 增大 → 焓项 x<sub>A</sub>x<sub>B</sub>χ 相对增强 →
中间的"鼓包"从无到有、越来越明显。</p>
<p>· 恰在 <b>T<sub>c</sub></b>：鼓包<b>刚刚出现</b>，两个拐点<b>重合</b>（d³ΔG/dx³ = 0）<br>
· <b>T &lt; T<sub>c</sub></b>：鼓包加深，两个拐点<b>分开</b>并向两侧移动 → spinodal 曲线张开<br>
· 同时两个公切点也分开 → binodal 曲线张开</p>
<p class="trap"><b>相图上的每一条水平线，对应一条 ΔG 曲线。</b>
把这个对应关系想清楚，读相图题就不会错。</p>""",
 kp="降温 → 鼓包出现加深 → 拐点与切点分开 → 相图上 spinodal/binodal 张开",
 src="p.55–59「Finding the Binodal / Spinodal / Critical point」"),

dict(kind="理解", topic="淬冷路径决定形貌", ans=1,
 stem="Two identical polymer blends are quenched from the same T₂: one lands inside the spinodal, the other in the metastable region. Their <b>equilibrium</b> compositions and <b>microstructures</b> will be:",
 opts=["Different compositions, same microstructure", "Same compositions, <b>different</b> microstructures",
       "Different compositions, different microstructures", "Identical in every respect"],
 exp="""<p><b>组成相同</b>：两者终态都是同一温度下的 binodal 组成（热力学决定）。</p>
<p><b>形貌不同</b>：<br>
· 落入 spinodal → <b>SD</b> → <b>互穿网络</b>（两相连续、互相缠绕）<br>
· 落入亚稳区 → <b>N&amp;G</b> → <b>分散的孤立颗粒/液滴</b></p>
<p class="trap"><b>这在材料上极重要</b>：同样的组成，互穿网络的力学性能（尤其韧性）
通常远好于分散颗粒结构。<b>控制淬冷路径 = 控制材料性能</b>，
而组成分析看不出这个差别，必须靠显微形貌。</p>""",
 kp="热力学定组成、动力学路径定形貌；形貌差异直接影响材料性能",
 src="p.64「distinctive microstructure of interpenetrating network」；p.69"),

dict(kind="计算", topic="杠杆规则", ans=1,
 stem="A mixture of overall composition x<sub>A</sub> = 0.40 separates into two phases with x<sub>A</sub>′ = 0.10 and x<sub>A</sub>″ = 0.70. What fraction of the material ends up in the x<sub>A</sub>″ phase?",
 opts=["0.30", "0.50", "0.57", "0.70"],
 exp="""<p><b>杠杆规则</b>（物料衡算）：设 x<sub>A</sub>″ 相占分数 f，则</p>
<div class="fb">0.10(1 − f) + 0.70 f = 0.40</div>
<p>0.10 + 0.60 f = 0.40 → f = 0.30/0.60 = <b>0.50</b></p>
<p><b>更快的算法</b>：f = (x<sub>A</sub> − x<sub>A</sub>′)/(x<sub>A</sub>″ − x<sub>A</sub>′)
= (0.40 − 0.10)/(0.70 − 0.10) = 0.30/0.60 = 0.50。
整体组成正好在两个 binodal 点<b>正中间</b>，所以两相各占一半。</p>
<p><b>与 ΔG 图的联系</b>：正是这个加权平均，使两相体系的 ΔG 等于<b>公切线在 x<sub>A</sub> 处的高度</b>
——公切线判据的数学基础就是杠杆规则。</p>""",
 kp="杠杆规则 f = (x−x′)/(x″−x′)；它是「两相 ΔG = 弦的高度」的来源",
 src="p.52「ΔG of 2 phases, half contributed by…」"),

dict(kind="理解", topic="UCST 与 LCST 的判别", ans=0,
 stem="A polymer solution is clear at 20 °C but turns cloudy when heated to 60 °C. This system exhibits:",
 opts=["LCST behaviour", "UCST behaviour", "Neither", "Both simultaneously"],
 exp="""<p><b>升温反而分相</b>（变浑浊）→ 这是 <b>LCST</b>（Lower Critical Solution Temperature）。</p>
<p>"下临界"指的是：<b>单相区在下方</b>，临界点是单相区的<b>上</b>边界温度。
名字容易反直觉——记住<b>看单相区在哪一侧</b>就不会错。</p>
<table class="mini"><thead><tr><th></th><th>单相区</th><th>行为</th><th>常见度</th></tr></thead><tbody>
<tr><td><b>UCST</b></td><td>高温侧</td><td>升温溶解</td><td>常见</td></tr>
<tr><td><b>LCST</b></td><td><b>低温侧</b></td><td><b>升温分相</b></td><td>少见</td></tr>
</tbody></table>
<p class="trap"><b>"变浑浊"就是分相的信号</b>——两相折射率不同产生光散射，与 Lecture 8
半结晶高分子发白、Lecture 9 银纹应力发白是同一光学机理。</p>""",
 kp="LCST：单相区在低温侧，升温分相；浑浊 = 分相的光学信号",
 src="p.61「LCST」"),

dict(kind="理解", topic="相图的三个区域", ans=3,
 stem="On a UCST phase diagram below T<sub>c</sub>, moving from the edge toward the middle at fixed T, you pass through regions in the order:",
 opts=["Unstable → metastable → stable", "Metastable → stable → unstable",
       "Stable → unstable → metastable", "<b>Stable → metastable → unstable</b>"],
 exp="""<p>从相图边缘（纯组分一侧）向中间移动：</p>
<table class="mini"><thead><tr><th>区域</th><th>边界</th><th>曲率</th><th>行为</th></tr></thead><tbody>
<tr><td><b>稳定</b></td><td>binodal 之外</td><td>凹向上</td><td>单相</td></tr>
<tr><td><b>亚稳</b></td><td>binodal 与 spinodal 之间</td><td>凹向上</td><td>需成核 → N&amp;G</td></tr>
<tr><td><b>不稳</b></td><td>spinodal 之内</td><td><b>凹向下</b></td><td>无势垒 → SD</td></tr>
</tbody></table>
<p>注意<b>稳定区和亚稳区的曲率相同</b>（都凹向上）——它们的差别不在局部曲率，
而在于<b>是否存在一条更低的公切线</b>。</p>""",
 kp="由外向内：稳定 → 亚稳 → 不稳；亚稳与稳定的曲率相同，差别在公切线",
 src="p.49、p.55–58 综合"),

dict(kind="理解", topic="相图的实验测定", ans=1,
 stem="Experimentally, the <b>binodal</b> of a polymer solution is most directly located by:",
 opts=["Measuring the glass transition temperature",
       "Finding the temperature at which the solution first becomes <b>cloudy</b> on cooling (cloud point)",
       "Measuring the intrinsic viscosity", "X-ray diffraction"],
 exp="""<p><b>浊点法（cloud point）</b>：缓慢降温，记录溶液<b>刚开始变浑</b>的温度。
变浑意味着出现了第二相（折射率不同 → 散射光）。</p>
<p><b>为什么测到的是 binodal 而不是 spinodal</b>：缓慢降温时，体系一进入亚稳区
就有足够时间通过<b>成核</b>完成分相，所以肉眼看到的第一个浑浊点对应
<b>binodal</b>（分相刚变得热力学有利的边界）。</p>
<p class="trap"><b>spinodal 难以直接测量</b>——必须快速淬冷"跳过"亚稳区，
通常靠散射实验（观察特征波长的涨落放大）间接确定。这也是讲义只教作图求 spinodal
而不谈实验的原因。</p>""",
 kp="浊点法测 binodal；spinodal 需快速淬冷 + 散射，难直接测",
 src="p.49「Binodal」与 p.62 淬冷讨论的延伸"),
]
