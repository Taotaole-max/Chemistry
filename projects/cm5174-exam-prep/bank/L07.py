# -*- coding: utf-8 -*-
LEC = 7
TITLE = "Size Exclusion Chromatography and Mass Spectrometry"
CN = "SEC 与质谱"
SRC = "讲义 Lectures_5-7"
L = [
dict(kind="理解", topic="SEC 的另一个名字", ans=1,
 stem="Size Exclusion Chromatography (SEC) is also known as:",
 opts=["High Performance Liquid Chromatography", "<b>Gel Permeation Chromatography (GPC)</b>",
       "Ion Exchange Chromatography", "Thin Layer Chromatography"],
 exp="""<p>讲义标题即写明：<i>“Size Exclusion Chromatography (also known as <b>Gel Permeation
Chromatography (GPC)</b>)”</i>。</p>
<p>两个名字强调的角度不同：<br>
· <b>SEC</b>（尺寸排阻）强调<b>分离机理</b>——大分子被"排除"在孔外<br>
· <b>GPC</b>（凝胶渗透）强调<b>固定相</b>——多孔凝胶</p>
<p>文献里两者<b>完全通用</b>，看到 GPC 就是 SEC。</p>""",
 kp="SEC = GPC；同一技术的两个名字", src="p.34「Principles of Size Exclusion Chromatography」"),

dict(kind="理解", topic="SEC 的分离机理", ans=1,
 stem="In SEC, molecules are separated according to:",
 opts=["Their charge", "Their <b>size</b>", "Their polarity", "Their boiling point"],
 exp="""<p>讲义：<i>“Used to separate molecules according to their <b>sizes</b>”</i>。
溶液（流动相）流过装填<b>多孔凝胶</b>（固定相）的色谱柱。</p>
<p class="trap"><b>SEC 不依赖化学相互作用</b>——这是它与其他色谱（离子交换、反相等）
的根本区别。理想的 SEC 柱应当与样品<b>没有任何吸附作用</b>，纯粹靠空间排阻。</p>
<p><b>后果</b>：这既是优点（对化学结构不挑剔），也是它最大的<b>局限</b>——
分离依据是尺寸<b>而非分子量</b>，两者的换算需要校准。</p>""",
 kp="SEC 靠空间排阻分离尺寸，不依赖化学作用；这既是优势也是局限来源",
 src="p.34「separate molecules according to their sizes」"),

dict(kind="理解", topic="洗脱顺序", ans=0,
 stem="In SEC, which molecules are eluted <b>first</b>?",
 opts=["The <b>largest</b>, because they are excluded from the pores",
       "The smallest, because they diffuse faster",
       "The most polar", "The least dense"],
 exp="""<p>讲义原文：<i>“<b>Largest</b> molecules are <b>excluded from the pores</b> and are eluted <b>first</b>.
<b>Smallest</b> molecules are <b>retained by the pores</b> and are eluted <b>last</b>.”</i></p>
<p><b>为什么</b>：大分子进不了孔，只能走<b>孔与孔之间</b>的空隙（volume outside pores），
路径短 → <b>保留体积 V<sub>R</sub> 小</b> → 先出。<br>
小分子能钻进孔内，多走了很多"弯路" → V<sub>R</sub> 大 → 后出。</p>
<p class="trap"><b>这与直觉相反</b>——很多人以为小分子跑得快。
在 SEC 里恰恰相反：<b>大分子先出</b>。</p>""",
 kp="大分子被孔排阻、路径短、先洗脱；小分子进孔、后洗脱",
 src="p.34「Largest molecules are excluded from the pores」"),

dict(kind="理解", topic="SEC 校准曲线", ans=2,
 stem="For SEC calibration, what is typically <b>linear</b> against the retention volume V<sub>R</sub>?",
 opts=["M", "M²", "<b>log M</b>", "1/M"],
 exp="""<p>讲义：<i>“Typically, the plot of <b>log M</b> is linear vs. V<sub>R</sub>”</i>，即</p>
<div class="fb">ln M = k V<sub>R</sub> + c</div>
<p><b>做法</b>：用一系列已知分子量的<b>标样</b>跑柱，记录各自的 V<sub>R</sub>，作 log M–V<sub>R</sub> 图；
未知样品由其 V<sub>R</sub> 从曲线读出 M。</p>
<p class="trap"><b>对数关系的含义</b>：V<sub>R</sub> 的<b>线性</b>变化对应 M 的<b>数量级</b>变化。
所以 SEC 能在一次运行中覆盖很宽的分子量范围，但对<b>相近分子量</b>的分辨率有限。</p>""",
 kp="log M 对 V_R 线性；SEC 覆盖范围宽但对相近 M 分辨有限",
 src="p.35「Calibration of SEC」"),

dict(kind="理解", topic="SEC 的第一个问题", ans=1,
 stem="A key limitation of conventional SEC calibration is that:",
 opts=["It cannot detect polymers at all",
       "SEC works on the basis of <b>size, not M</b> — so unless the standard has the <b>same chemical composition and structure</b> as the unknown, the result is inaccurate",
       "It requires the polymer to be crystalline", "It only works above 200 °C"],
 exp="""<p>讲义原文：<i>“SEC works on basis of <b>size, not M</b>. Unless the calibration standard has
<b>same chemical composition and structure</b> as unknown, otherwise results will <b>not be accurate</b>.”</i></p>
<p><b>问题的实质</b>：同样分子量的<b>刚性链</b>和<b>柔性链</b>在溶液中尺寸完全不同，
洗脱体积也就不同。用聚苯乙烯标样去读一个支化聚合物，会得到系统性偏差。</p>
<p class="trap"><b>解决办法就是通用校准</b>（下一题）——用 Mark-Houwink 常数把"尺寸"换算回"分子量"。</p>""",
 kp="SEC 按尺寸分离，标样必须与未知样化学结构相同，否则需通用校准",
 src="p.35「Potential Problems」"),

dict(kind="理解", topic="SEC 的第二个问题", ans=2,
 stem="What happens to polymer molecules that are <b>larger than the pores</b>?",
 opts=["They are permanently trapped in the column", "They are chemically degraded",
       "They have <b>no access to internal pore volume</b> and elute together with <b>no differentiation</b> in V<sub>R</sub>",
       "They elute last"],
 exp="""<p>讲义原文：<i>“Any polymer larger than the pores will have <b>no access to internal pore volume</b>,
and will be eluted with <b>no differentiation in V<sub>R</sub></b>.”</i></p>
<p><b>后果</b>：所有超大分子<b>挤在同一个洗脱体积</b>出来（即"排阻极限"），
彼此无法区分——这是 SEC 分子量上限的来源。</p>
<p class="trap"><b>实验对策</b>：根据样品的分子量范围<b>选择合适孔径</b>的柱子，
或把不同孔径的柱<b>串联</b>使用，扩展有效分离范围。</p>""",
 kp="超过孔径的分子一起洗脱、无分辨（排阻极限）；需选合适孔径或串联柱",
 src="p.35「Potential Problems」"),

dict(kind="理解", topic="通用校准的核心思想", ans=1,
 stem="Universal calibration is based on the principle that polymers with the same ____ elute at the same V<sub>R</sub>.",
 opts=["Molecular weight", "<b>Hydrodynamic volume V<sub>h</sub></b>", "Chemical composition", "Density"],
 exp="""<p>讲义原文：<i>“Polymers with the <b>same size (hydrodynamic volume V<sub>h</sub>)</b> will elute
with the same V<sub>R</sub>.”</i></p>
<p>这句话把 SEC 的"缺陷"变成了可利用的规律：既然柱子只认<b>尺寸</b>，
那就用尺寸作为通用标尺，再靠 Mark-Houwink 把尺寸换算成各自的分子量。</p>
<div class="fb">[η] = (5/2)N<sub>Av</sub>V<sub>h</sub>/M　且　[η] = kM<sup>a</sup>　⇒　V<sub>h</sub> ∝ k M<sup>a+1</sup></div>""",
 kp="通用校准：相同 V_h 相同 V_R；由 [η] 两个表达式得 V_h ∝ kM^(a+1)",
 src="p.36「Universal Calibration of SEC」"),

dict(kind="计算", topic="通用校准公式", ans=2,
 stem="The universal calibration relation between a standard (s) and an unknown (x) eluting at the same V<sub>R</sub> is:",
 opts=["k<sub>s</sub>M<sub>s</sub> = k<sub>x</sub>M<sub>x</sub>", "k<sub>s</sub>M<sub>s</sub><sup>a<sub>s</sub></sup> = k<sub>x</sub>M<sub>x</sub><sup>a<sub>x</sub></sup>",
       "<b>k<sub>s</sub>M<sub>s</sub><sup>a<sub>s</sub>+1</sup> = k<sub>x</sub>M<sub>x</sub><sup>a<sub>x</sub>+1</sup></b>",
       "k<sub>s</sub>/M<sub>s</sub> = k<sub>x</sub>/M<sub>x</sub>"],
 exp="""<div class="fb">k<sub>s</sub> M<sub>s</sub><sup>a<sub>s</sub>+1</sup> = k<sub>x</sub> M<sub>x</sub><sup>a<sub>x</sub>+1</sup></div>
<p>解出未知样分子量：</p>
<div class="fb">M<sub>x</sub> = [ k<sub>s</sub>M<sub>s</sub><sup>a<sub>s</sub>+1</sup> / k<sub>x</sub> ]<sup>1/(a<sub>x</sub>+1)</sup></div>
<p class="trap"><b>指数是 a+1 不是 a</b>——因为 V<sub>h</sub> ∝ kM<sup>a+1</sup>（[η]·M ∝ V<sub>h</sub>）。
选项 B 漏掉了那个 +1，是最常见的错误。</p>
<p><b>前提</b>：<b>两种高分子的 k 和 a 都必须已知</b>（查文献或标定）。</p>""",
 kp="通用校准 k_s M_s^(a_s+1) = k_x M_x^(a_x+1)；注意指数是 a+1",
 src="p.36「Universal Calibration」"),

dict(kind="计算", topic="通用校准数值题", ans=1,
 stem="A PS standard (k<sub>s</sub> = 1.0×10⁻⁴, a<sub>s</sub> = 0.7) of M<sub>s</sub> = 100,000 elutes at a given V<sub>R</sub>. An unknown polymer has k<sub>x</sub> = 1.0×10⁻⁴ and a<sub>x</sub> = 0.7. What is M<sub>x</sub>?",
 opts=["50,000", "<b>100,000</b>", "170,000", "200,000"],
 exp="""<p>两者的 k 和 a <b>完全相同</b>，方程两边形式一致：</p>
<div class="fb">1.0×10⁻⁴ · M<sub>s</sub><sup>1.7</sup> = 1.0×10⁻⁴ · M<sub>x</sub><sup>1.7</sup>　⇒　M<sub>x</sub> = M<sub>s</sub> = <b>100,000</b></div>
<p><b>这题在考概念不是算术</b>：当未知样与标样的 Mark-Houwink 常数相同时
（即化学结构相同），<b>通用校准退化成普通校准</b>，不需要任何修正。</p>
<p class="trap"><b>反过来说</b>：只有当 k 或 a 不同时，通用校准才真正起作用。
这也解释了为什么用 PS 标样测 PS 样品从来不需要通用校准。</p>""",
 kp="k、a 相同时通用校准退化为普通校准；只有结构不同才需要修正",
 src="p.36「Universal Calibration」"),

dict(kind="计算", topic="通用校准（不同常数）", ans=2,
 stem="Standard: k<sub>s</sub> = 8×10⁻⁵, a<sub>s</sub> = 0.5, M<sub>s</sub> = 50,000. Unknown: k<sub>x</sub> = 1×10⁻⁵, a<sub>x</sub> = 0.5. Find M<sub>x</sub>.",
 opts=["50,000", "100,000", "<b>200,000</b>", "400,000"],
 exp="""<p>a<sub>s</sub> = a<sub>x</sub> = 0.5，故两边指数都是 <b>1.5</b>：</p>
<div class="fb">8×10⁻⁵ × (50,000)<sup>1.5</sup> = 1×10⁻⁵ × M<sub>x</sub><sup>1.5</sup></div>
<p>M<sub>x</sub><sup>1.5</sup> = 8 × (50,000)<sup>1.5</sup></p>
<p>M<sub>x</sub> = 8<sup>1/1.5</sup> × 50,000 = 8<sup>2/3</sup> × 50,000</p>
<p>8<sup>2/3</sup> = (∛8)² = 2² = <b>4</b>　→　M<sub>x</sub> = <b>200,000</b></p>
<p class="trap"><b>陷阱</b>：不能直接按 k 的比值 8 倍去乘（那给 400,000，选项 D）。
必须开 <b>1/(a+1) = 2/3</b> 次方。</p>""",
 kp="8^(2/3) = 4；指数 1/(a+1) 必须用上", src="p.36"),

dict(kind="理解", topic="SEC 检测器：示差折光", ans=0,
 stem="A refractometer detector in SEC produces a signal proportional to:",
 opts=["<b>Concentration</b>", "Molecular weight", "Concentration × molecular weight", "Retention volume"],
 exp="""<p>讲义：<i>“<b>Refractometer</b> – Light is refracted by an amount <b>proportional to concentration</b>.”</i></p>
<p><b>示差折光是最通用的 SEC 检测器</b>：<br>
· 优点：<b>对任何高分子都有响应</b>（只要与溶剂折射率不同），不需要发色团<br>
· 缺点：灵敏度不如 UV，且对温度波动敏感</p>
<p class="trap"><b>与 UV 检测器的关键差别</b>：RI 信号 ∝ <b>浓度</b>（即 n<sub>i</sub>M<sub>i</sub>，质量浓度）；
而 UV 信号也 ∝ n<sub>i</sub>M<sub>i</sub>——两者其实<b>都</b>正比于质量浓度，
只是 UV 多一层"发色团数目随 M 增长"的道理（见后面的题）。</p>""",
 kp="RI 检测器信号 ∝ 浓度；通用性强，不需发色团", src="p.37「Detectors in SEC Experiments」"),

dict(kind="理解", topic="SEC 检测器：UV-Vis", ans=1,
 stem="A UV-Vis detector can be used in SEC provided that:",
 opts=["The polymer is crystalline", "The polymer <b>absorbs</b> in the UV or visible range",
       "The solvent is water", "The molecular weight is below 10,000"],
 exp="""<p>讲义：<i>“Absorbance is proportional to concentration (Beer-Lambert law).
<b>Polymer must be absorbing in UV or visible range.</b>”</i></p>
<p><b>这是 UV 检测器的硬限制</b>：聚乙烯、聚丙烯等<b>没有发色团</b>的高分子
在 UV-Vis 区不吸收，用不了 UV 检测器，必须改用示差折光。</p>
<p class="trap"><b>反过来是优点</b>：如果样品是<b>共聚物</b>且只有一种单体吸收 UV，
把 UV 和 RI 两个检测器<b>串联</b>，就能算出<b>共聚组成随分子量的分布</b>
——这是单一检测器做不到的。</p>""",
 kp="UV 检测器要求高分子有发色团；PE/PP 不适用，需用 RI",
 src="p.37「UV-Visible spectrometer」"),

dict(kind="理解", topic="UV 信号高度正比于什么", ans=1,
 stem="If a polymer is detected by UV absorption, the signal <b>height</b> in the chromatogram is proportional to:",
 opts=["n<sub>i</sub>", "<b>n<sub>i</sub>M<sub>i</sub></b>", "n<sub>i</sub>/V<sub>total</sub>", "M<sub>i</sub>"],
 exp="""<p>讲义给的推理：<i>“By Beer-Lambert law, absorbance is proportional to <b>molar concentration</b>,
which is proportional to <b>number of moles of i-mer</b>. <b>However</b>, the number of <b>chromophores</b>
in each polymer molecule also increases <b>proportionately with molecular weight</b>.
Hence, absorbance is proportional to n<sub>i</sub> <b>AND</b> M<sub>i</sub>.”</i></p>
<div class="fb">信号高度 h ∝ n<sub>i</sub> × M<sub>i</sub></div>
<p class="trap"><b>这是本讲最容易错的一题</b>。直觉上"吸光度 ∝ 摩尔浓度"就该是 n<sub>i</sub>，
但<b>每条链上的发色团数目本身正比于链长</b>，两个 M 的因子相乘。</p>
<p><b>为什么重要</b>：正因为 h ∝ n<sub>i</sub>M<sub>i</sub>（即质量浓度），
后面从谱图算 M<sub>n</sub> 时才要用 <b>∫h dM / ∫(h/M) dM</b> 这个形式。</p>""",
 kp="UV 信号 h ∝ n_i M_i（发色团数目随 M 增长）；决定后续积分公式的形式",
 src="官方 Question 26（对应 p.37–38）"),

dict(kind="理解", topic="光散射与粘度检测器的优势", ans=2,
 stem="Coupling a <b>light scattering</b> or <b>viscometer</b> detector to SEC has which advantage?",
 opts=["It makes the run faster", "It removes the need for a solvent",
       "Calibration with molecular weight standards <b>may not be required</b>",
       "It allows detection of non-polar polymers only"],
 exp="""<p>讲义对光散射和粘度检测器都写着：<i>“Can be used together with (1) or (2) to determine M<sub>w</sub>.
<b>Calibration with molecular weight standards may not be required.</b>”</i></p>
<p><b>为什么能免标定</b>：<br>
· <b>光散射</b>直接测<b>绝对分子量</b>（I ∝ cM<sub>w</sub>），不依赖柱子的校准曲线<br>
· <b>粘度计</b>测 [η]，配合通用校准原理也能给绝对值</p>
<p class="trap"><b>这解决了 SEC 最大的软肋</b>——不再需要"结构相同的标样"。
现代的 <b>SEC-MALS</b>（多角度光散射联用）正是基于此，是测未知高分子绝对分子量的标准方法。</p>
<p><b>注意</b>：这两种检测器<b>必须与浓度检测器（RI 或 UV）联用</b>——
因为要算 M 就需要同时知道 c。</p>""",
 kp="LS/粘度检测器给绝对分子量，免标样；但需与浓度检测器联用",
 src="p.37「Light scattering / Viscometer」"),

dict(kind="理解", topic="从谱图计算 Mn 和 Mw", ans=1,
 stem="Given a chromatogram of signal height h vs V<sub>R</sub>, M<sub>n</sub> is computed as:",
 opts=["∫hM dM / ∫h dM", "<b>∫h dM / ∫(h/M) dM</b>", "∫h dV<sub>R</sub> / ∫M dV<sub>R</sub>", "∫h² dM / ∫h dM"],
 exp="""<p>讲义给的两个公式：</p>
<div class="fb">M<sub>n</sub> = ∫h dM / ∫(h/M) dM　　M<sub>w</sub> = ∫hM dM / ∫h dM</div>
<p><b>为什么是这个形式</b>：信号高度 <b>h ∝ n·M</b>（质量），所以<br>
· h/M ∝ n（<b>个数</b>）→ 分母 ∫(h/M)dM 相当于 Σn<sub>i</sub><br>
· ∫h dM 相当于 Σn<sub>i</sub>M<sub>i</sub>（<b>总质量</b>）<br>
两者相除正是 M<sub>n</sub> = Σn<sub>i</sub>M<sub>i</sub>/Σn<sub>i</sub> ✓</p>
<p class="trap"><b>还有一步换元</b>：数据是 h vs V<sub>R</sub>，不是 h vs M。
由 ln M = kV<sub>R</sub> + c 得 <b>dM = k·exp(kV<sub>R</sub>+c) dV<sub>R</sub></b>，代入后才能对 V<sub>R</sub> 积分。</p>""",
 kp="h ∝ nM，故 h/M ∝ n；M_n = ∫h dM/∫(h/M)dM，且需用 dM = k·e^(kV+c)dV 换元",
 src="p.38「Analysis of SEC Data」"),

dict(kind="理解", topic="SEC 能给出什么", ans=3,
 stem="Properly calibrated SEC can provide:",
 opts=["Only M<sub>n</sub>", "Only M<sub>w</sub>", "Only the PDI",
       "<b>The entire molecular weight distribution</b>, hence M<sub>n</sub>, M<sub>w</sub> and PDI"],
 exp="""<p>SEC 的独特价值在于它<b>把整个分布画了出来</b>——不像渗透压或光散射只给一个平均值。</p>
<p>有了 h vs M 的完整曲线，就能积分算出<b>任何</b>平均值：M<sub>n</sub>、M<sub>w</sub>，
以及它们的比值 <b>PDI</b>。</p>
<p class="trap"><b>"给出分布"的方法只有两类</b>：<br>
· <b>SEC/GPC</b>——需要校准<br>
· <b>MALDI-TOF-MS</b>——直接给各分子量物种的丰度<br>
其余方法（渗透压、光散射、粘度）都只给<b>单个平均值</b>，无法反映分布宽窄。</p>""",
 kp="SEC 与 MALDI 是仅有的两类能给出完整分布（因而能算 PDI）的方法",
 src="p.34「Polymer molecular weights and their distribution」；p.38"),

dict(kind="理解", topic="MALDI 的全称与定位", ans=0,
 stem="MALDI-TOF-MS stands for:",
 opts=["<b>Matrix-Assisted Laser Desorption Ionization – Time-of-Flight – Mass Spectrometry</b>",
       "Molecular Analysis by Laser Diffraction", "Multi-Angle Light Detection Instrument",
       "Mass Analysis of Long-chain Dispersed Ions"],
 exp="""<p>三个部分各司其职：<br>
· <b>MALDI</b>（基质辅助激光解吸电离）——把高分子<b>完好地</b>送进气相并带上电荷<br>
· <b>TOF</b>（飞行时间）——按 m/z <b>分离</b><br>
· <b>MS</b>（质谱）——<b>检测</b>各物种丰度</p>
<p>最终数据是<b>各分子量物种的丰度分布</b>，由此可同时算出 <b>M<sub>n</sub> 和 M<sub>w</sub></b>。</p>""",
 kp="MALDI（电离）+ TOF（分离）+ MS（检测）；给出完整分子量分布",
 src="p.39「MALDI-TOF-MS」"),

dict(kind="理解", topic="为什么叫「软」电离", ans=2,
 stem="MALDI uses a laser pulse as a '<b>soft</b>' ionization technique in order to:",
 opts=["Speed up the analysis", "Increase the charge state",
       "<b>Prevent the breaking up or degradation</b> of the polymer", "Heat the sample uniformly"],
 exp="""<p>讲义原文：<i>“Uses laser pulse as a '<b>soft</b>' ionization technique to <b>prevent the breaking up
or the degrading of polymers</b>.”</i></p>
<p><b>为什么高分子需要软电离</b>：传统的电子轰击电离（EI）能量太高，会把长链打成碎片，
测到的就不是原始分子量分布了。</p>
<p><b>MALDI 的巧妙之处</b>：激光并<b>不直接照射高分子</b>，而是被<b>基质</b>吸收。
基质迅速受热汽化，把高分子"<b>带</b>"进气相——高分子本身几乎没有直接吸收能量。</p>""",
 kp="软电离防止链断裂；激光被基质吸收，高分子被「带」进气相",
 src="p.39「MALDI」"),

dict(kind="理解", topic="基质的作用", ans=1,
 stem="In MALDI, the polymer is dispersed in an aromatic organic matrix. The matrix must:",
 opts=["React chemically with the polymer", "<b>Absorb at the laser wavelength</b> (usually 337 nm)",
       "Be a strong acid", "Have the same molecular weight as the polymer"],
 exp="""<p>讲义原文：<i>“Polymer and cationic salt (Na⁺, K⁺) are dispersed in <b>aromatic organic compound
matrix that absorbs at laser wavelength (usually <b>337 nm</b>)</b>. Laser pulse absorption by aromatic
compounds <b>rapidly heats and vaporizes</b> the compounds and polymer molecules into the gas phase.”</i></p>
<p><b>三个组分各自的角色</b>：</p>
<table class="mini"><thead><tr><th>组分</th><th>作用</th></tr></thead><tbody>
<tr><td><b>基质</b>（芳香族）</td><td>吸收 337 nm 激光，汽化并携带高分子</td></tr>
<tr><td><b>阳离子盐</b>（Na⁺/K⁺）</td><td>与高分子结合使其<b>带电</b></td></tr>
<tr><td>高分子</td><td>被动地被带进气相</td></tr>
</tbody></table>
<p><b>337 nm</b> 是氮气激光器的波长，这就是它成为 MALDI 标准光源的原因。</p>""",
 kp="基质吸收 337 nm 激光并携带高分子汽化；Na⁺/K⁺ 提供电荷",
 src="p.39「MALDI」"),

dict(kind="理解", topic="MALDI 的适用范围", ans=2,
 stem="MALDI is suitable for which polymers?",
 opts=["All polymers equally", "Only non-polar polymers such as polyethylene",
       "Only polymers with <b>polar groups</b> (polyesters, acrylates, amides) — <b>not</b> polyethylene or polypropylene",
       "Only crosslinked polymers"],
 exp="""<p>讲义原文：<i>“This technique is <b>only suitable for polymers with polar groups</b>
(poly-esters, acrylates, amides), <b>not for non-polar polymers</b> (poly-ethylene, propylene).”</i></p>
<p><b>为什么</b>：MALDI 靠高分子与 <b>Na⁺/K⁺ 阳离子或质子结合</b>而带电。
非极性链（PE、PP）<b>没有能配位阳离子的位点</b>，无法有效带电，也就飞不到检测器。</p>
<p class="trap"><b>这是 MALDI 最重要的局限</b>。恰恰是产量最大的两种通用塑料（PE、PP）
用不了 MALDI，只能靠 SEC 或高温 GPC。</p>""",
 kp="MALDI 只适用含极性基团的高分子；PE、PP 无法电离",
 src="p.39「only suitable for polymers with polar groups」"),

dict(kind="理解", topic="单电荷的优势", ans=1,
 stem="Why is it advantageous that MALDI 'invariably produces singly-charged species'?",
 opts=["It increases sensitivity",
       "Since z = 1, the measured <b>m/z ratio is directly the mass</b> — no ambiguity from multiple charge states",
       "It reduces the flight time", "It prevents fragmentation"],
 exp="""<p>讲义特别注明这是 <i>“(very advantageous)”</i>。</p>
<p><b>原因</b>：质谱测的永远是 <b>m/z</b>。若同一分子可能带 1、2、3 个电荷，
一个分子量就会在谱图上出现多个峰，解谱极其复杂。</p>
<p><b>MALDI 只产生单电荷</b>（z = 1）→ <b>m/z 就是 m</b> → 谱图可以直接读成分子量分布。</p>
<p class="trap"><b>对比电喷雾电离（ESI）</b>：ESI 产生<b>多电荷</b>物种，对小分子蛋白很有用
（可把大质量压进小 m/z 范围），但对分子量本就分散的合成高分子，多电荷会让谱图完全无法解析。
<b>这就是合成高分子用 MALDI 而非 ESI 的原因。</b></p>""",
 kp="单电荷使 m/z = m，谱图可直接读成分子量分布",
 src="p.40「MALDI invariably produces singly-charged species (very advantageous)」"),

dict(kind="理解", topic="TOF 的加速原理", ans=0,
 stem="In the TOF analyser, ions are accelerated by a high electric field. The acceleration is given by:",
 opts=["<b>Newton's second law F = ma</b>", "Bragg's law", "Stokes' law", "The Boltzmann distribution"],
 exp="""<p>讲义明确写着 <b>F = ma （Newton's Second Law）</b>。</p>
<p><b>推理链</b>：同样的电场、同样的电荷（单电荷）→ <b>同样的力 F</b><br>
→ 由 a = F/m，<b>质量小的加速度大</b><br>
→ 获得<b>更高的速度</b><br>
→ <b>先到达检测器</b></p>
<p class="trap"><b>定量关系不是线性的</b>：由 qV = ½mv² 得 v ∝ 1/√m，
所以 <b>飞行时间 t ∝ √m</b>，不是 ∝ m。这是计算题的必考点。</p>""",
 kp="F = ma；小质量加速度大、速度快、先到；但 t ∝ √m 非线性",
 src="p.40「Newton's Second Law」"),

dict(kind="理解", topic="哪个先到检测器", ans=0,
 stem="Do smaller or larger polymer molecules arrive at the detector first?",
 opts=["<b>Smaller</b>", "Larger", "They arrive simultaneously", "It depends on the matrix"],
 exp="""<p>讲义给的答案：<i>“For the same electrical force (singly-charged particles), a <b>smaller mass</b>
polymer will have a <b>higher acceleration</b>, and will therefore fly towards detector at
<b>higher velocity</b> and <b>arrive first</b>.”</i></p>
<p class="trap"><b>与 SEC 正好相反，很容易混</b>：</p>
<table class="mini"><thead><tr><th>技术</th><th>谁先出</th><th>原因</th></tr></thead><tbody>
<tr><td><b>SEC</b></td><td><b>大分子</b></td><td>被孔排阻，路径短</td></tr>
<tr><td><b>MALDI-TOF</b></td><td><b>小分子</b></td><td>质量小、加速度大、速度快</td></tr>
</tbody></table>
<p><b>记忆法</b>：SEC 是"大的走捷径"，TOF 是"轻的跑得快"。</p>""",
 kp="TOF 小分子先到；与 SEC 大分子先出正好相反", src="官方 Question 27（对应 p.40）"),

dict(kind="计算", topic="飞行时间的定量关系", ans=1,
 stem="A singly-charged ion of m = 2,000 Da arrives in 30 μs. When does an ion of m = 8,000 Da arrive?",
 opts=["45 μs", "<b>60 μs</b>", "90 μs", "120 μs"],
 exp="""<p>由 qV = ½mv² 得 v = √(2qV/m) ∝ 1/√m；飞行距离 L 固定，故</p>
<div class="fb">t = L/v ∝ √m</div>
<p>t₂/t₁ = √(8,000/2,000) = √4 = <b>2</b></p>
<p>t₂ = 30 × 2 = <b>60 μs</b></p>
<p class="trap"><b>陷阱</b>：质量变成 4 倍，时间只变 <b>2</b> 倍（不是 4 倍 = 120 μs，选项 D）。
<b>t ∝ √m，不是 ∝ m。</b></p>""",
 kp="t ∝ √m；质量 4 倍则时间 2 倍", src="p.40「Time-of-flight (TOF)」"),

dict(kind="计算", topic="由飞行时间反推质量", ans=2,
 stem="Under identical conditions, ion A (m = 1,000 Da) arrives at 25 μs and ion B arrives at 75 μs. What is B's mass?",
 opts=["3,000 Da", "5,000 Da", "<b>9,000 Da</b>", "15,000 Da"],
 exp="""<p>t ∝ √m，故 m ∝ t²：</p>
<div class="fb">m<sub>B</sub>/m<sub>A</sub> = (t<sub>B</sub>/t<sub>A</sub>)² = (75/25)² = 3² = <b>9</b></div>
<p>m<sub>B</sub> = 9 × 1,000 = <b>9,000 Da</b></p>
<p class="trap"><b>反过来用要平方</b>：时间 3 倍 → 质量 <b>9</b> 倍（不是 3 倍，选项 A）。
正向 t ∝ √m，反向 m ∝ t²，别用反了。</p>""",
 kp="反推时 m ∝ t²；时间 3 倍对应质量 9 倍", src="p.40"),

dict(kind="理解", topic="MALDI 测值偏低的原因", ans=3,
 stem="MALDI-TOF-MS may give molecular weight values <b>smaller</b> than the actual value. The likely reason is:",
 opts=["The higher molecular weight species are harder to vaporize",
       "The higher molecular weight species may degrade into smaller fragments during desorption and ionization",
       "The detector is saturated by lower molecular weight species that arrived earlier and becomes less responsive",
       "<b>All of the above</b>"],
 exp="""<p>官方答案是 <b>D（以上皆是）</b>。三条原因：</p>
<p>① <b>高分子量物种更难汽化</b>——质量大，需要更多能量才能进入气相，
在同样激光能量下"起飞"效率低</p>
<p>② <b>解吸电离过程中可能碎裂</b>——即便是软电离，超长链仍可能断裂，
碎片被计入较低分子量</p>
<p>③ <b>检测器饱和</b>——小分子<b>先到</b>（t ∝ √m），大量小分子离子先轰击检测器，
使其响应下降，后到的大分子信号被低估</p>
<p class="trap"><b>三条原因都指向同一个方向：低估高分子量端</b>，
所以 M<sub>n</sub> 和 M<sub>w</sub> 都偏低，而且 <b>M<sub>w</sub> 受影响更大</b>（它对高分子量端更敏感）
→ 测出的 <b>PDI 偏窄</b>。</p>""",
 kp="MALDI 偏低的三条原因都在高分子量端；导致 PDI 测得偏窄",
 src="官方 Question 28（对应 p.39–40）"),

dict(kind="理解", topic="MALDI 与 SEC 的互补", ans=1,
 stem="Compared with SEC, a key advantage of MALDI-TOF-MS is that it:",
 opts=["Works for all polymers including polyethylene",
       "Gives <b>absolute</b> masses without needing molecular weight standards for calibration",
       "Is much cheaper", "Can measure crosslinked polymers"],
 exp="""<p><b>MALDI 直接测质量</b>（通过飞行时间），不需要"结构相同的标样"——
这正好补上了 SEC 最大的软肋。</p>
<table class="mini"><thead><tr><th></th><th>SEC</th><th>MALDI-TOF</th></tr></thead><tbody>
<tr><td>依据</td><td>尺寸（需校准）</td><td><b>质量（绝对）</b></td></tr>
<tr><td>适用范围</td><td><b>几乎所有可溶高分子</b></td><td>仅极性高分子</td></tr>
<tr><td>分子量上限</td><td>受孔径限制</td><td>受汽化/碎裂限制</td></tr>
<tr><td>给出分布</td><td>是</td><td>是</td></tr>
</tbody></table>
<p class="trap"><b>选项 A 恰恰是 MALDI 的弱点</b>——PE、PP 正是它<b>不能</b>测的。
两种方法是<b>互补</b>而非替代关系。</p>""",
 kp="MALDI 给绝对质量免标定，但只限极性高分子；与 SEC 互补",
 src="p.35「Potential Problems」与 p.39–40 对照"),

dict(kind="理解", topic="孔外体积与孔内体积", ans=1,
 stem="On an SEC calibration curve, the <b>volume outside the pores</b> corresponds to:",
 opts=["The retention volume of the smallest molecules",
       "The <b>minimum</b> retention volume — where fully excluded (largest) molecules elute",
       "The total column volume", "The dead volume of the detector"],
 exp="""<p>讲义在校准曲线图上标出了三个关键体积：<br>
· <b>Volume outside pores</b>——完全被排阻的大分子走的路径，对应<b>最小</b> V<sub>R</sub><br>
· <b>Max internal pore volume accessed by polymer</b>——完全渗透的小分子，对应<b>最大</b> V<sub>R</sub><br>
· <b>Fraction of internal pore volume accessible</b>——中间尺寸分子部分进入孔</p>
<p><b>所有的分离都发生在这两个极限之间</b>。超出这个范围的分子
（太大或太小）都<b>挤在端点</b>，无法区分。</p>
<p class="trap">这解释了为什么<b>选柱子要匹配样品的分子量范围</b>——
样品必须落在这个"工作窗口"内才有分辨率。</p>""",
 kp="孔外体积 = 最小 V_R（全排阻）；全孔体积 = 最大 V_R；分离只在两者之间",
 src="p.35「Volume outside pores / Max internal pore volume」"),

dict(kind="理解", topic="表征方法的综合选择", ans=2,
 stem="A lab needs the <b>PDI</b> of a polyethylene sample. Which technique is appropriate?",
 opts=["Membrane osmometry alone", "MALDI-TOF-MS",
       "<b>SEC (high-temperature GPC)</b>", "Static light scattering alone"],
 exp="""<p><b>要 PDI 就必须知道 M<sub>n</sub> 和 M<sub>w</sub> 两者</b>，
也就是需要<b>完整的分子量分布</b>。只有 SEC 和 MALDI 能给出分布。</p>
<p><b>但样品是聚乙烯</b>：<br>
· <b>MALDI 不行</b>——PE 非极性，无法电离（讲义明确排除）<br>
· <b>渗透压只给 M<sub>n</sub></b>，光散射只给 M<sub>w</sub>，单用任何一个都<b>算不出 PDI</b></p>
<p>所以只能用 <b>SEC</b>。（PE 室温下不溶，实际要用<b>高温 GPC</b>，
通常在 140–160 °C 的三氯苯中进行。）</p>
<p class="trap"><b>这类"给定样品选方法"的题</b>是综合考点：
要同时考虑<b>需要什么量</b>和<b>样品有什么限制</b>。</p>""",
 kp="求 PDI 需完整分布 → 只能 SEC 或 MALDI；PE 非极性排除 MALDI",
 src="p.34–38 与 p.39 综合"),
]

L.append(dict(kind="计算", topic="SEC 校准曲线的应用", ans=1,
 stem="An SEC column is calibrated as log₁₀M = 9.0 − 0.25·V<sub>R</sub> (V<sub>R</sub> in mL). An unknown sample elutes at V<sub>R</sub> = 20.0 mL. What is its M?",
 opts=["1.0×10³", "<b>1.0×10⁴</b>", "1.0×10⁵", "1.0×10⁶"],
 exp="""<div class="fb">log₁₀M = 9.0 − 0.25 × 20.0 = 9.0 − 5.0 = <b>4.0</b></div>
<p>M = 10⁴ = <b>10,000 g/mol</b></p>
<p class="trap"><b>负斜率的物理含义</b>：V<sub>R</sub> 越大 M 越小——
正是"大分子被排阻、先出（小 V<sub>R</sub>）"的数学表达。
如果你算出的关系是正斜率，一定是把洗脱顺序搞反了。</p>
<p><b>灵敏度感受</b>：斜率 −0.25 /mL 意味着 V<sub>R</sub> 每增加 4 mL，
分子量就<b>降一个数量级</b>。这既说明 SEC 覆盖范围宽，
也说明<b>V<sub>R</sub> 的微小误差会被放大</b>——所以流速必须极其稳定。</p>""",
 kp="log M 对 V_R 线性且斜率为负；V_R 的小误差被指数放大，流速需稳定",
 src="p.35「the plot of log M is linear vs. V_R」"))
