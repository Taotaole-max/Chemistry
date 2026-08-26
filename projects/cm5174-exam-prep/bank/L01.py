# -*- coding: utf-8 -*-
LEC = 1
TITLE = "Polymer Size and Conformations"
CN = "高分子尺寸与构象"
SRC = "讲义 Lectures_1-4"
L = [
dict(kind="理解", topic="高分子的定义",
 stem="Which statement best matches the definition of a polymer given in the lecture?",
 opts=["A substance whose molecules contain long sequences of atoms linked mainly by <b>covalent (primary) bonds</b>",
       "Any substance with a molecular weight above 1,000 g/mol",
       "A substance whose molecules are held together mainly by van der Waals forces",
       "A crystalline solid built from repeating unit cells"], ans=0,
 exp="""<p>讲义原文：<i>“a substance composed of molecules which have long sequences of atoms or groups of atoms
linked to each other by <b>primary (usually covalent) bonds</b>”</i>，也叫 <b>macromolecule</b>。</p>
<p>关键在<b>共价主键</b>连成的<b>长序列</b>——不是靠分子量数值卡线（排除 B），也不是靠次级作用力聚集（排除 C）。
正是这个"大尺寸"赋予高分子独特的力学、化学和热性质。</p>""",
 kp="高分子 = 共价主键连成长序列的大分子；大尺寸决定性质", src="p.4「Introduction to Polymers – Definition」"),

dict(kind="理解", topic="热固性 vs 热塑性",
 stem="Which class of polymer <b>cannot</b> be processed by the application of heat?",
 opts=["Thermoplastics", "Thermosets", "Elastomers", "All polymers can be heat-processed"], ans=1,
 exp="""<p><b>Thermosets 热固性</b>：高度交联，链运动被限制，因此<b>抗热软化、抗机械变形、抗溶剂侵蚀</b>，
但代价是<b>不能热加工</b>（cannot be heat-processed）。例：环氧树脂、酚醛树脂。</p>
<p>对比 <b>Thermoplastics 热塑性</b>（PS、PP）：受热可软化或熔融，能用热和压力加工（模压、挤出）。</p>""",
 kp="三大分类：热塑性可熔融加工 / 热固性高度交联不可热加工 / 弹性体轻度交联",
 src="p.5「Classification of Polymers – by Thermal & Mechanical Properties」"),

dict(kind="理解", topic="弹性体的交联程度",
 stem="According to the lecture's classification, elastomers differ from thermosets mainly in that elastomers have:",
 opts=["A higher degree of crosslinking", "A <b>low</b> degree of crosslinking",
       "No crosslinking at all", "Crystalline rather than amorphous domains"], ans=1,
 exp="""<p>讲义：弹性体是 <i>“soft rubbery polymers with a <b>low degree of crosslinking</b>”</i>，
能在应力下产生很大形变，并<b>恢复原尺寸</b>。热固性则是 <b>high degree of crosslinking</b>。</p>
<p>注意"完全不交联"是错的——弹性体<b>必须</b>交联，否则链会永久滑移，形变不可恢复（这点在 Lecture 10 会再强调）。</p>""",
 kp="弹性体 = 轻度交联 + 大形变可恢复；交联度是它与热固性的分水岭",
 src="p.5「Classification」；另见 p.34（L10）「Characteristics of Elastomers」"),

dict(kind="计算", topic="数均分子量 Mn",
 stem="A sample contains 4.0 mol of chains of M = 5 kg/mol and 1.0 mol of chains of M = 30 kg/mol. What is M<sub>n</sub>?",
 opts=["10 kg/mol", "12.5 kg/mol", "17.5 kg/mol", "22 kg/mol"], ans=0,
 exp="""<div class="fb">M<sub>n</sub> = Σn<sub>i</sub>M<sub>i</sub> / Σn<sub>i</sub> = [4(5) + 1(30)] / (4+1) = 50 / 5 = <b>10 kg/mol</b></div>
<p>M<sub>n</sub> 按<b>分子个数</b>平均，每条链权重相同——所以数量占优的短链把平均值拉低。
选项 C（17.5）是不加权的算术平均 (5+30)/2，选项 D 是 M<sub>w</sub>。</p>""",
 kp="Mn 按分子个数平均，是依数性方法（渗透压、VPO、端基分析）测到的量",
 src="p.6「Molecular Weight of Polymers」"),

dict(kind="计算", topic="重均分子量 Mw",
 stem="For the same sample (4.0 mol at 5 kg/mol, 1.0 mol at 30 kg/mol), what is M<sub>w</sub>?",
 opts=["10 kg/mol", "12.5 kg/mol", "20 kg/mol", "22 kg/mol"], ans=3,
 exp="""<div class="fb">M<sub>w</sub> = Σn<sub>i</sub>M<sub>i</sub><sup>2</sup> / Σn<sub>i</sub>M<sub>i</sub>
= [4(25) + 1(900)] / [4(5) + 1(30)] = 1000 / 50 = <b>22 kg/mol</b></div>
<p class="trap"><b>陷阱</b>：分母是 <b>Σn<sub>i</sub>M<sub>i</sub>（总质量 = 50）</b>，不是 Σn<sub>i</sub>（= 5）。
用错分母会得到 200。</p>
<p>注意 22 &gt; 10：那 1 mol 长链只占 20% 的分子数，却占 60% 的质量，所以在 M<sub>w</sub> 里权重大得多。</p>""",
 kp="Mw 按质量加权，大分子贡献更大；分母是总质量 Σn_iM_i", src="p.6「Molecular Weight of Polymers」"),

dict(kind="计算", topic="PDI 与分布宽度",
 stem="Continuing the same sample (M<sub>n</sub> = 10, M<sub>w</sub> = 22 kg/mol), what is the PDI and how would the lecture classify this distribution?",
 opts=["2.2 — broad dispersity", "2.2 — narrow dispersity",
       "0.45 — monodisperse", "1.2 — narrow dispersity"], ans=0,
 exp="""<p>PDI = M<sub>w</sub>/M<sub>n</sub> = 22/10 = <b>2.2</b></p>
<p>讲义给的分档：</p>
<table class="mini"><thead><tr><th>PDI</th><th>分类</th></tr></thead><tbody>
<tr><td>= 1</td><td><b>Monodisperse</b> 单分散</td></tr>
<tr><td>1 &lt; PDI &lt; 1.5</td><td><b>Narrow dispersity</b> 窄分布</td></tr>
<tr><td>&gt; 2</td><td><b>Broad dispersity</b> 宽分布</td></tr>
</tbody></table>
<p>2.2 &gt; 2，属于<b>宽分布</b>。</p>""",
 kp="PDI 分档：=1 单分散、1–1.5 窄、>2 宽", src="p.6「Polydispersity Index (PDI)」"),

dict(kind="理解", topic="Mw ≥ Mn 恒成立",
 stem="For any real polymer sample, which relationship must hold?",
 opts=["M<sub>n</sub> &gt; M<sub>w</sub> always", "M<sub>w</sub> ≥ M<sub>n</sub>, with equality only for a monodisperse sample",
       "M<sub>w</sub> = M<sub>n</sub> always", "The relationship depends on the shape of the distribution"], ans=1,
 exp="""<p>M<sub>w</sub> 在求平均时给<b>大分子额外的权重</b>（多乘了一个 M），M<sub>n</sub> 不给。
只要样品里存在<b>不止一种分子量</b>，M<sub>w</sub> 就一定被拉得更高。</p>
<p>只有所有链完全一样长（单分散）时两者相等，此时 PDI = 1。</p>
<p class="trap"><b>用途</b>：这是最快的自查手段——考试中算出 PDI &lt; 1，一定是把 M<sub>w</sub> 的分母写错了。</p>""",
 kp="Mw ≥ Mn 恒成立，等号仅在单分散时取到；可用来自查计算", src="p.6「Molecular Weight of Polymers」"),

dict(kind="理解", topic="平均值对长链的敏感度",
 stem="A tiny amount of very long chains is accidentally introduced into a monodisperse sample. What happens?",
 opts=["M<sub>n</sub> rises sharply, M<sub>w</sub> barely changes",
       "M<sub>w</sub> rises much more than M<sub>n</sub>, so PDI increases",
       "Both rise by the same factor, PDI unchanged",
       "Neither changes because the amount is tiny"], ans=1,
 exp="""<p>加入的链<b>数目</b>很少 → 对 M<sub>n</sub>（按个数平均）几乎没影响。</p>
<p>但这些链<b>很长</b>，在 M<sub>w</sub> 里以 M<sub>i</sub><sup>2</sup> 的形式出现 → 权重被平方放大 →
M<sub>w</sub> 明显上升 → <b>PDI 增大</b>。</p>
<p>这也解释了为什么两种平均值都要报：单看 M<sub>n</sub> 会漏掉少量超长链，而超长链对熔体粘度、力学性能影响很大。</p>""",
 kp="Mw 对高分子量尾部极敏感（M² 加权），Mn 对低分子量端敏感",
 src="p.6「Weighted by the molecular weight – greater contributions by large weight species」"),

dict(kind="理解", topic="平均末端矢量为零",
 stem="Why is the <b>average end-to-end vector</b> ⟨<b>h</b>⟩ of a model chain equal to zero?",
 opts=["Because the chain is always fully coiled",
       "Because the sample is isotropic — no direction is preferred, so vectors cancel",
       "Because the bond vectors all have the same length",
       "Because the chain has no volume"], ans=1,
 exp="""<p>讲义原文：<i>“since there is no reason for each vector to point in one direction more than any other
(i.e. sample is <b>isotropic</b>), the average <b>h</b> = 0”</i>。</p>
<p>矢量相加时正负方向互相抵消，平均为零。<b>但我们要的是平均末端"距离"（标量），不是平均矢量</b>
——所以必须改求<b>均方根</b>：先平方（消掉符号）、再平均、再开方。</p>""",
 kp="⟨h⟩ = 0 源于各向同性；因此改用 RMS ⟨h²⟩^½ 描述尺寸",
 src="p.8「Average End-to-End Distance for Model Chain」"),

dict(kind="理解", topic="交叉项为何消失",
 stem="In the derivation of ⟨h²⟩ for a <b>freely-jointed</b> chain, why do all the cross terms ⟨<b>l</b><sub>i</sub>·<b>l</b><sub>j</sub>⟩ (i ≠ j) vanish?",
 opts=["Because the bond vectors are all perpendicular to each other",
       "Because θ can range over 0°–180°, so cos θ averages to zero",
       "Because l<sub>i</sub> and l<sub>j</sub> have different lengths",
       "Because the sum contains equal numbers of positive and negative bond lengths"], ans=1,
 exp="""<p>点积 <b>l</b><sub>i</sub>·<b>l</b><sub>j</sub> = l² cos θ。在自由连接链里相邻链段取向<b>完全不受约束</b>，
θ 可以是 0° 到 180° 的任意值，<b>cos θ 从 −1 到 +1 均匀取值，平均为 0</b>。</p>
<div class="fb">⟨h²⟩ = nl² + Σ<sub>i</sub>Σ<sub>j≠i</sub>⟨l<sub>i</sub>·l<sub>j</sub>⟩ = nl² + 0 = <b>nl²</b></div>
<p>剩下的 n 项是 i = j 的自点积，每项 = l²，共 n 项。</p>""",
 kp="自由连接链：交叉项因 ⟨cos θ⟩ = 0 而消失，得 ⟨h²⟩ = nl²",
 src="p.9–10「Find the root-mean-square of the h distance」"),

dict(kind="计算", topic="自由连接链 RMS",
 stem="A freely-jointed chain has n = 2,500 bonds of length l = 2.0 Å. What is its RMS end-to-end distance?",
 opts=["50 Å", "100 Å", "2,500 Å", "5,000 Å"], ans=1,
 exp="""<div class="fb">⟨h²⟩<sup>1/2</sup> = √n · l = √2500 × 2.0 = 50 × 2.0 = <b>100 Å</b></div>
<p class="trap"><b>陷阱</b>：选项 A 是只开了 √n 忘了乘 l；选项 D 是伸直长度 n·l = 5,000 Å。</p>
<p><b>记住这个标度</b>：RMS ∝ <b>√n</b>，而伸直长度 ∝ <b>n</b>。链越长，无规线团相对伸直链就越"紧缩"。</p>""",
 kp="⟨h²⟩^½ = √n · l；RMS ∝ √n，伸直长度 ∝ n", src="p.10「⟨h²⟩ = nl²」"),

dict(kind="计算", topic="固定键角的修正因子",
 stem="For a chain with fixed <b>tetrahedral</b> bond angles but free rotation, ⟨h²⟩ is how many times that of a freely-jointed chain with the same n and l?",
 opts=["0.5", "1.0", "2.0", "4.0"], ans=2,
 exp="""<div class="fb">⟨h²⟩ = n l² · (1 + cos θ)/(1 − cos θ)</div>
<p><b>θ = 180° − 109.5° = 70.5°</b>，cos 70.5° = 0.334</p>
<p>因子 = (1 + 0.334)/(1 − 0.334) = 1.334 / 0.666 = <b>2.00</b></p>
<p class="trap">⚠️⚠️ <b>本课最大的陷阱</b>：公式里的 <b>θ 是键角的补角，不是键角本身</b>。
若直接代 cos 109.5° = −0.334，因子变成 0.5（正好是选项 A），答案差 4 倍。
课程官方 Question 4 专门设了这个坑，题干还加了 hint："Is θ the bond angle?"</p>""",
 kp="θ = 180° − 键角；sp³ 时因子恰好 ≈ 2，即固定键角使 ⟨h²⟩ 翻倍",
 src="p.11–12「Fixed bond angle, free rotation」；官方 Question 4"),

dict(kind="理解", topic="三种链模型的共性",
 stem="What do the freely-jointed, fixed-bond-angle, and fixed-rotation-angle chain models have in common?",
 opts=["They all give exactly the same ⟨h²⟩",
       "⟨h²⟩ is proportional to n l² in all three; only the prefactor differs",
       "They all require the chain to have finite volume",
       "They all give ⟨h²⟩ proportional to n² l²"], ans=1,
 exp="""<p>三个模型的结果分别是 nl²、nl²·f(θ)、nl²·f(θ)·f(φ)——<b>全部正比于 nl²</b>，
局部化学约束只改变一个<b>前置因子</b>。讲义原话：<i>"Size is changed only by a prefactor that depends on the local constraint"</i>。</p>
<p>这就是为什么可以把所有约束打包成一个常数：</p>
<div class="fb">⟨h²⟩ = C<sub>∞</sub> n l² = N b²</div>
<p>C<sub>∞</sub> 叫<b>特征比</b>（∞ 表示适用于大 n），b 叫<b>统计链段长度</b>，N 是聚合度。</p>""",
 kp="所有链模型 ⟨h²⟩ ∝ nl²，差别只在前置因子 → 归并为 C∞ 和 b",
 src="p.12「All proportional to nl²」"),

dict(kind="计算", topic="统计链段长度 b",
 stem="A polymer has C<sub>∞</sub> = 6.0, backbone bond length l = 1.5 Å, and each repeat unit contains 2 backbone bonds (so n = 2N). What is the statistical segment length b?",
 opts=["1.5 Å", "3.0 Å", "5.2 Å", "9.0 Å"], ans=2,
 exp="""<p>由定义 <b>C<sub>∞</sub> n l² = N b²</b>，代入 n = 2N：</p>
<div class="fb">b² = C<sub>∞</sub> n l² / N = C<sub>∞</sub> (2N) l² / N = 2 C<sub>∞</sub> l²</div>
<p>b² = 2 × 6.0 × (1.5)² = 27.0 → b = √27 = <b>5.2 Å</b></p>
<p><b>物理含义</b>：b 是"有效"链段长度，比真实键长大得多（5.2 Å vs 1.5 Å），
因为真实链的局部刚性使得要走好几个键才"忘掉"原来的方向。</p>""",
 kp="b 是把局部约束吸收进去的等效链段长度，恒大于真实键长；注意 n 与 N 的换算",
 src="p.12「C∞: Characteristic Ratio / b: Statistical segment length」"),

dict(kind="计算", topic="伸直（contour）长度",
 stem="What is the fully stretched-out length of a polyethylene chain of M = 140,000 g/mol? (C–C bond length 1.5 Å)",
 opts=["7,500 Å", "10,000 Å", "12,500 Å", "15,000 Å"], ans=3,
 exp="""<p>每个 CH<sub>2</sub> 重复单元 <b>14 g/mol</b>，所以主链上有</p>
<div class="fb">140,000 / 14 = 10,000 个 C–C 单元</div>
<p>伸直长度 = 10,000 × 1.5 Å = <b>15,000 Å</b></p>
<p class="trap"><b>关键一步是"数键数"</b>：先用分子量除以重复单元质量得到单元数，再乘键长。
PE 的重复单元是 CH<sub>2</sub>（14），不是 C<sub>2</sub>H<sub>4</sub>（28）——用 28 会得到 7,500（选项 A）。</p>""",
 kp="contour length = n × l；PE 每个 CH₂ 单元 14 g/mol 对应一个 C–C 键",
 src="官方 Question 2（配合 p.7 的图示）"),

dict(kind="计算", topic="密堆积立方体尺寸",
 stem="If that same 140,000 g/mol polyethylene molecule were packed into a tiny cube, what would the cube edge be? (ρ = 0.9 g/cm³, 6.02×10²³ chains per mole)",
 opts=["5,900 Å", "6,400 Å", "64 Å", "59 Å"], ans=2,
 exp="""<p><b>① 单链质量</b>：140,000 g/mol ÷ 6.02×10²³ chain/mol = 2.33×10⁻¹⁹ g/chain</p>
<p><b>② 单链体积</b>：2.33×10⁻¹⁹ g ÷ 0.9 g/cm³ = 2.58×10⁻¹⁹ cm³</p>
<p><b>③ 立方体边长</b>：(2.58×10⁻¹⁹)<sup>1/3</sup> = 6.4×10⁻⁷ cm = <b>64 Å</b></p>
<p><b>把三个尺度放在一起看</b>（同一条链）：</p>
<table class="mini"><thead><tr><th>状态</th><th>尺寸</th></tr></thead><tbody>
<tr><td>完全伸直</td><td>15,000 Å</td></tr>
<tr><td>无规线团（RMS）</td><td>212 Å</td></tr>
<tr><td>密堆积立方体</td><td>64 Å</td></tr>
</tbody></table>
<p>真实的溶液构象是<b>中间那个</b>——既不是棍，也不是实心块。</p>""",
 kp="密度法求单链体积；三种尺度 15,000 / 212 / 64 Å 的量级对比",
 src="官方 Question 3"),

dict(kind="计算", topic="RMS 末端距（含键角）",
 stem="What is the RMS end-to-end distance of that 140,000 g/mol polyethylene chain, given a tetrahedral bond angle of 109.5° and free rotation? (l = 1.5 Å)",
 opts=["212 Å", "11,238 Å", "45,048 Å", "106 Å"], ans=0,
 exp="""<p>n = 10,000 个 C–C 键（同上题）。<b>θ = 180 − 109.5 = 70.5°</b>，因子 ≈ 2：</p>
<div class="fb">⟨h²⟩ = n l² (1+cos θ)/(1−cos θ) = 10,000 × 2.25 × 2 = 45,048 Å²</div>
<p>⟨h²⟩<sup>1/2</sup> = √45,048 = <b>212 Å</b></p>
<p class="trap"><b>三个错误选项分别对应三种典型失误</b>：<br>
· <b>45,048</b>（选项 C）= 忘了开方，那是 ⟨h²⟩ 本身<br>
· <b>106</b>（选项 D）= 用了 cos 109.5° 导致因子取 0.5<br>
· <b>11,238</b>（选项 B）= 中间量算错</p>""",
 kp="完整流程：数键数 → 代因子 → 别忘开方。这是官方原题",
 src="官方 Question 4"),

dict(kind="理解", topic="回转半径的定义",
 stem="The radius of gyration R<sub>g</sub> is defined as:",
 opts=["The distance between the two chain ends",
       "The RMS distance of <b>all monomers</b> from the chain's centre of mass",
       "Half the contour length", "The radius of the smallest sphere enclosing the chain"], ans=1,
 exp="""<p>末端距只强调<b>首尾两个</b>单体，但讲义指出 <i>“all monomers are important”</i>。
R<sub>g</sub> 取<b>所有</b>单体到<b>质心</b>距离的均方根：</p>
<div class="fb">R<sub>g</sub> = ⟨s²⟩<sup>1/2</sup> = [ (1/N) Σ<sub>i</sub> s<sub>i</sub>² ]<sup>1/2</sup></div>
<p>（假设各单体质量相等）。质心的定义保证 <b>Σ m<sub>i</sub> s<sub>i</sub> = 0</b>。</p>
<p><b>为什么重要</b>：R<sub>g</sub> <b>可以被光散射直接测量</b>，而末端距不能——这是它在实验上更有用的原因。</p>""",
 kp="Rg = 所有单体到质心的 RMS 距离；可由光散射直接测量",
 src="p.13「Radius of Gyration (Rg)」"),

dict(kind="计算", topic="由 N、b 求 Rg",
 stem="An ideal chain has N = 4,900 and b = 7.0 Å. What is R<sub>g</sub>?",
 opts=["100 Å", "200 Å", "245 Å", "490 Å"], ans=1,
 exp="""<div class="fb">R<sub>g</sub>² = N b² / 6 = 4,900 × 49 / 6 = 240,100 / 6 = 40,017 Å²</div>
<p>R<sub>g</sub> = √40,017 = <b>200 Å</b></p>
<p class="trap"><b>两个常见失误</b>：忘记除以 6（得 490 Å，选项 D）、忘记开方。</p>""",
 kp="Rg² = Nb²/6（理想链，假设链无体积可自穿）", src="p.16–17「Rg² = Nb²/6」"),

dict(kind="计算", topic="Rg 与末端距的换算",
 stem="For an ideal chain, the RMS end-to-end distance ⟨h²⟩<sup>1/2</sup> equals R<sub>g</sub> multiplied by:",
 opts=["√2 ≈ 1.41", "√6 ≈ 2.45", "6", "1/√6 ≈ 0.41"], ans=1,
 exp="""<p>由 ⟨h²⟩ = Nb² 和 R<sub>g</sub>² = Nb²/6：</p>
<div class="fb">R<sub>g</sub>² = ⟨h²⟩ / 6　⇒　⟨h²⟩<sup>1/2</sup> = √6 · R<sub>g</sub> ≈ <b>2.45 R<sub>g</sub></b></div>
<p>用上一题的数：R<sub>g</sub> = 200 Å，则 ⟨h²⟩<sup>1/2</sup> = 2.45 × 200 = 490 Å。
（直接算 √(4900×49) = 70×7 = 490 Å，一致。）</p>
<p class="trap">注意方向别搞反：<b>末端距比 R<sub>g</sub> 大</b>（因为末端距量的是两端之间，R<sub>g</sub> 量的是到中心）。</p>""",
 kp="⟨h²⟩^½ = √6 · Rg ≈ 2.45 Rg；末端距大于回转半径",
 src="p.16「Rg² = Nb²/6」与 p.12「⟨h²⟩ = Nb²」联立"),

dict(kind="理解", topic="Rg 与密堆积球半径 R₀",
 stem="A polymer is densely packed into a sphere of radius R₀. What is the relationship between R<sub>g</sub> and R₀?",
 opts=["R<sub>g</sub> = R₀", "R<sub>g</sub> &lt; R₀", "R<sub>g</sub> &gt; R₀", "Not possible to determine"], ans=1,
 exp="""<p>R<sub>g</sub> 是所有单体到质心的<b>均方根</b>距离——是个"平均"量。
既然是平均，就<b>总有一部分单体比 R<sub>g</sub> 更远</b>（最远的那些正好在 R₀ 处）。</p>
<p>讲义原话：<i>“R<sub>g</sub> does not represent the maximum spatial extent of the polymer.
There are always some monomers further away than R<sub>g</sub> from the center of mass.”</i></p>
<p>所以恒有 <b>R<sub>g</sub> &lt; R₀</b>。（对均匀实心球，精确值是 R<sub>g</sub> = √(3/5) R₀ ≈ 0.775 R₀。）</p>""",
 kp="Rg 是均方根平均，不是最大空间尺度，故恒小于外接/密堆球半径",
 src="官方 Question 5"),

dict(kind="理解", topic="标度指数：理想链",
 stem="For an ideal chain (no excluded volume, chains may intersect), R<sub>g</sub> ∝ N<sup>ν</sup> with ν equal to:",
 opts=["1/3", "1/2", "3/5", "1"], ans=1,
 exp="""<p>由 R<sub>g</sub>² = Nb²/6 直接得 R<sub>g</sub> ∝ <b>N<sup>1/2</sup></b>。</p>
<p>讲义特别注明这是<b>在"链没有体积、可以自相交"的假设下</b>推出的——
所以 ν = 1/2 描述的是<b>理想链</b>，实验上对应 <b>θ 溶剂</b>中的行为。</p>""",
 kp="理想链 ν = 1/2，成立前提是忽略排除体积", src="p.17「Rg ∝ N^(1/2)」"),

dict(kind="理解", topic="标度指数：良溶剂",
 stem="In a <b>good solvent</b>, R<sub>g</sub> ∝ N<sup>3/5</sup> rather than N<sup>1/2</sup>. The physical reason is:",
 opts=["The solvent chemically reacts with the chain",
       "The chain has <b>finite volume</b> and cannot intersect itself, so it swells",
       "The chain becomes fully rigid", "The chain collapses into a dense sphere"], ans=1,
 exp="""<p>讲义：ν = 3/5 适用于 <i>“a polymer chain which has <b>finite volume</b> and hence could not
intersect in space”</i>，并注明 <i>“Observed for polymer in a <b>good solvent</b>”</i>。</p>
<p>这就是<b>排除体积效应</b>：真实链段占据空间，不能自我穿越，链因此比理想链<b>更伸展</b>
（3/5 &gt; 1/2）。</p>
<p><b>四个标度值一起记</b>：</p>
<table class="mini"><thead><tr><th>情形</th><th>ν</th></tr></thead><tbody>
<tr><td>致密球（密堆积）</td><td>1/3</td></tr>
<tr><td>理想链 / θ 溶剂</td><td>1/2</td></tr>
<tr><td><b>良溶剂</b></td><td><b>3/5</b></td></tr>
<tr><td>刚性棒</td><td>1</td></tr>
</tbody></table>""",
 kp="良溶剂 ν = 3/5 源于排除体积；四个标度指数 1/3 < 1/2 < 3/5 < 1",
 src="p.17「Radius of Gyration – scaling」"),

dict(kind="理解", topic="标度指数：致密球",
 stem="Why does a polymer packed into a dense sphere give R<sub>g</sub> ∝ N<sup>1/3</sup>?",
 opts=["Because N ∝ V = (4/3)πR³, so R ∝ N<sup>1/3</sup>",
       "Because the surface area scales as R²", "Because the chain is fully extended",
       "Because the density decreases with N"], ans=0,
 exp="""<p>密堆积意味着<b>体积正比于单体数</b>：N ∝ V = (4/3)πR³。</p>
<div class="fb">R ∝ N<sup>1/3</sup></div>
<p>这是四个标度里<b>最紧缩</b>的一个（指数最小）——单体数增加时尺寸增长最慢。
另一端是刚性棒 ν = 1：完全伸直，尺寸与 N 成正比，增长最快。</p>""",
 kp="致密球 ν = 1/3 来自体积正比于 N；是四种标度中最紧缩的",
 src="p.17「For a polymer that packs into a dense sphere」"),

dict(kind="计算", topic="标度关系的应用",
 stem="A polymer in a <b>good solvent</b> has its degree of polymerization increased 32-fold. By what factor does R<sub>g</sub> increase?",
 opts=["4", "5.7", "8", "32"], ans=2,
 exp="""<p>良溶剂 R<sub>g</sub> ∝ N<sup>3/5</sup>：</p>
<div class="fb">R<sub>g</sub> 倍数 = 32<sup>3/5</sup> = 32<sup>0.6</sup></div>
<p>32 = 2⁵，所以 32<sup>0.6</sup> = 2<sup>5×0.6</sup> = 2³ = <b>8</b></p>
<p class="trap"><b>对比</b>：同样 32 倍的 N，若是理想链（ν = 1/2）只增大 32<sup>0.5</sup> = 5.7 倍（选项 B）。
排除体积让链在良溶剂中膨胀得更快。</p>""",
 kp="标度换算技巧：把倍数写成 2 的幂，指数运算就变简单",
 src="p.17「Rg ∝ N^(3/5)」"),

dict(kind="理解", topic="n 与 N 的区别",
 stem="In ⟨h²⟩ = C<sub>∞</sub> n l² = N b², the symbols n and N refer respectively to:",
 opts=["Number of <b>backbone bonds</b> and <b>degree of polymerization</b> (repeat units)",
       "Degree of polymerization and number of chains",
       "Number of chains and number of monomers", "Both mean the same thing"], ans=0,
 exp="""<p>讲义定义：<b>n</b> 是模型里的<b>链段（键）数目</b>，<b>N</b> 是<b>聚合度</b>（number of repeat units）。</p>
<p>两者<b>一般不相等</b>：例如聚乙烯每个重复单元 CH<sub>2</sub> 贡献 1 个 C–C 键（n ≈ N），
但很多高分子每个重复单元含 2 个或更多主链键（n = 2N 等）。</p>
<p class="trap">做题时如果题目同时给了 C<sub>∞</sub>、l 和"每单元几个主链键"，
就是在考这个换算——见本讲第 14 题。</p>""",
 kp="n = 主链键数，N = 聚合度；两者靠「每重复单元含几个主链键」换算",
 src="p.12「N: Degree of polymerization (number of repeat units)」"),

dict(kind="理解", topic="固定旋转角模型",
 stem="Adding a <b>fixed rotation angle φ</b> constraint (on top of a fixed bond angle θ) changes ⟨h²⟩ by introducing which extra factor?",
 opts=["(1 + cos φ)/(1 − cos φ)", "(1 − cos φ)/(1 + cos φ)", "cos²φ", "1/(1 + cos φ)"], ans=0,
 exp="""<div class="fb">⟨h²⟩ = n l² · (1 + cos θ)/(1 − cos θ) · <b>(1 + cos φ)/(1 − cos φ)</b></div>
<p>形式与键角那一项<b>完全相同</b>，只是把 θ 换成 φ——这是三个模型里约束最强的一个。</p>
<p>但结论不变：仍然 ∝ nl²，只是前置因子更大。所有这些都被吸收进 <b>C<sub>∞</sub></b>。</p>""",
 kp="固定旋转角引入同形式的第二个因子；模型再复杂也只改前置因子",
 src="p.12「Fixed bond angle, fixed rotation angle φ」"),

dict(kind="理解", topic="C∞ 的含义",
 stem="A polymer with a <b>stiffer</b> backbone would be expected to have:",
 opts=["A smaller C<sub>∞</sub>", "A larger C<sub>∞</sub>",
       "C<sub>∞</sub> = 1 regardless", "C<sub>∞</sub> &lt; 1"], ans=1,
 exp="""<p>C<sub>∞</sub> 衡量真实链比理想自由连接链"伸展"多少：</p>
<div class="fb">C<sub>∞</sub> = ⟨h²⟩<sub>real</sub> / (n l²)</div>
<p>链越<b>刚硬</b>（键角、旋转受限越强）→ 越难卷曲 → ⟨h²⟩ 越大 → <b>C<sub>∞</sub> 越大</b>。</p>
<p>自由连接链是下限，C<sub>∞</sub> = 1；固定 sp³ 键角已使 C<sub>∞</sub> ≈ 2；真实高分子常在 4–10。</p>
<p class="trap">C<sub>∞</sub> <b>不可能小于 1</b>——那意味着比完全自由的链还要卷曲，物理上不成立（排除 D）。</p>""",
 kp="C∞ 是链刚性的度量，自由连接链为 1，越刚硬越大", src="p.12「C∞: Characteristic Ratio」"),

dict(kind="理解", topic="为何 ∞ 下标",
 stem="Why is the characteristic ratio written as C<sub>∞</sub> (with an infinity subscript)?",
 opts=["Because it applies to chains of infinite molecular weight only",
       "Because it is the limiting value that applies for <b>large n</b>",
       "Because it can take infinitely large values", "Because it is measured at infinite dilution"], ans=1,
 exp="""<p>讲义注解：<i>“∞ because applies to large n”</i>。</p>
<p>对<b>短链</b>，端效应显著，⟨h²⟩/(nl²) 还随 n 变化；<b>n 足够大</b>后这个比值趋于一个常数——
那个极限值就是 C<sub>∞</sub>。</p>
<p>同样的"大 N 极限"思想也出现在 R<sub>g</sub>² 的推导里：
精确结果是 R<sub>g</sub>² = Nb²/6 − b²/(6N)，<b>大 N 时</b>第二项才可以丢掉。</p>""",
 kp="C∞ 是 n → 大 时的极限值；Rg² = Nb²/6 同样是大 N 近似",
 src="p.12「(∞ because applies to large n)」；p.16「For large values of N」"),

dict(kind="理解", topic="Rg 的实验可测性",
 stem="Which experimental technique gives direct access to the radius of gyration R<sub>g</sub>?",
 opts=["Membrane osmometry", "Light scattering", "End-group analysis", "Differential scanning calorimetry"], ans=1,
 exp="""<p>讲义在定义 R<sub>g</sub> 时就点明：<i>“Radius of gyration (R<sub>g</sub>) can be measured by
<b>light scattering</b> techniques”</i>。</p>
<p>具体机理在 Lecture 6：当粒子尺寸 &gt; λ/20 时，同一粒子不同部位的散射光发生<b>相消干涉</b>，
使散射强度出现<b>角度依赖</b>，从这个角度依赖里可以提取 R<sub>g</sub>：</p>
<div class="fb">1/M<sub>w</sub> · (1 + q²R<sub>g</sub>²/3 + …)，其中 q = (4πn/λ)·sin(θ/2)</div>
<p class="trap"><b>别混</b>：静态光散射给 <b>M<sub>w</sub> 和 R<sub>g</sub></b>；动态光散射（DLS）给的是
<b>R<sub>h</sub></b>（流体力学半径），是另一个量。</p>""",
 kp="Rg ← 静态光散射（角度依赖）；Rh ← 动态光散射。两者不同",
 src="p.13「can be measured by light scattering techniques」；p.25（L6）"),
]
