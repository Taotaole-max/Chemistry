# -*- coding: utf-8 -*-
LEC = 8
TITLE = "Solid State Properties – Glassy State"
CN = "固态性质：玻璃态"
SRC = "讲义 Lectures_8-10"
L = [
dict(kind="理解", topic="玻璃的定义", ans=1,
 stem="Which set of statements correctly describes a glass, according to the lecture?",
 opts=["Crystalline solid with long-range order; flows slowly; thermodynamically stable",
       "<b>Amorphous solid; no long-range order; does not flow; metastable</b>",
       "Amorphous liquid that flows very slowly; thermodynamically stable",
       "Crystalline solid; no long-range order; metastable"],
 exp="""<p>讲义列出的四条：<br>
① Glass is an <b>amorphous solid</b>（无定形固体）<br>
② There is <b>no long-range order</b> or packing in the molecules<br>
③ However, it <b>does not flow</b>（unlike liquid）<br>
④ Glass is typically <b>not in its most thermodynamically stable state — metastable</b></p>
<p>并且讲义强调：这是<b>高分子中最普遍的状态</b>（"the most prevalent state in polymers"）。</p>
<p class="trap"><b>"玻璃会缓慢流动"是流传很广的谣言</b>（教堂彩窗下厚上薄其实是古代制造工艺所致）。
讲义明确写着 <b>does not flow</b>。</p>""",
 kp="玻璃 = 无定形、无长程有序、不流动、亚稳；高分子中最常见的状态",
 src="p.3「Definitions of a Glass」"),

dict(kind="理解", topic="玻璃态的形成", ans=2,
 stem="How does the glassy state form on cooling a polymer melt?",
 opts=["The molecules suddenly align into a crystal",
       "The polymer chemically crosslinks",
       "Molecular motion slows until, below a certain temperature, the disordered molecules <b>cannot rearrange into optimal packing</b>",
       "The polymer evaporates and re-condenses"],
 exp="""<p>讲义描述：<i>“When a molten material is cooled, molecular motion <b>slows down</b> and the
molecules <b>try to pack</b>. Below a temperature, the disordered molecules slows to the extent that
they <b>cannot rearrange themselves into their optimal packing</b>. This temperature is the
<b>glass transition temperature (T<sub>g</sub>)</b>.”</i></p>
<p><b>关键词是"来不及"</b>——玻璃化不是热力学相变，而是<b>动力学被冻结</b>。
分子并非"不想"堆砌得更好，而是<b>没时间</b>了。</p>
<p class="trap"><b>这直接推出两个结论</b>：<br>
① T<sub>g</sub> <b>依赖冷却速率</b>（时间尺度问题）<br>
② 玻璃是<b>亚稳</b>的（存在更低能量的堆砌方式，只是达不到）</p>""",
 kp="玻璃化是动力学冻结而非热力学相变；由此推出依赖冷却速率与亚稳性",
 src="p.3「Formation of Glassy State」"),

dict(kind="理解", topic="与结晶的竞争", ans=1,
 stem="The glass-forming process is in competition with:",
 opts=["Evaporation", "<b>Crystallization</b>, where ordered packing is achieved",
       "Degradation", "Crosslinking"],
 exp="""<p>讲义：<i>“This process is in <b>competition with crystallization</b> – where ordered packing is achieved.
In cases where only a fraction of the polymer successfully crystallizes, the remaining portion remains
amorphous – <b>semi-crystalline state</b>.”</i></p>
<p><b>冷却时的两条路</b>：<br>
· <b>来得及排列</b> → 结晶（有序）<br>
· <b>来不及排列</b> → 玻璃（无序）<br>
· <b>部分排列</b> → <b>半结晶态</b>（高分子最常见的实际状态）</p>
<p class="trap"><b>高分子几乎不可能 100% 结晶</b>——链太长，总有缠结的部分排不进晶格。
所以"结晶性高分子"实际都是<b>半结晶</b>的。</p>""",
 kp="玻璃化与结晶竞争；部分结晶给出半结晶态，高分子无法 100% 结晶",
 src="p.3「Formation of Glassy State」"),

dict(kind="理解", topic="玻璃态为何透明", ans=0,
 stem="Why is a glassy polymer such as PMMA optically transparent?",
 opts=["Chains are randomly packed (like a liquid), making the refractive index <b>homogeneous</b>, so there is no scattering",
       "It absorbs all visible light", "It has a very low refractive index",
       "The chains are perfectly aligned"],
 exp="""<p>讲义：<i>“Glassy polymer is optically transparent – polymer chains are <b>randomly packed</b>
(like liquid), which makes <b>refractive index homogenous</b>, hence <b>no scattering</b>.”</i></p>
<p>反过来：<i>“In semi-crystalline polymer, <b>refractive index difference</b> between crystallites and
amorphous regions cause <b>light scattering</b> – appears <b>hazy or opaque</b>.”</i></p>
<p class="trap"><b>无序反而透明，有序反而浑浊</b>——这很反直觉。
关键不在"有没有序"，而在<b>折射率是否处处相同</b>。
玻璃态虽然无序，但<b>均匀地</b>无序，光走过去感觉不到变化。</p>
<p><b>这是 L6「散射源于折射率不均」的直接应用</b>，同一原理还解释 L9 的银纹应力发白。</p>""",
 kp="透明源于折射率均一（不是有序）；半结晶因晶区/非晶区折射率差而发白",
 src="p.4「Properties of a Glassy Polymer」"),

dict(kind="理解", topic="玻璃态与结晶态的加工性", ans=2,
 stem="Which comparison between glassy and crystalline polymers is <b>correct</b>?",
 opts=["Crystalline polymers are easier to process from the melt",
       "Glassy polymers are always mechanically stronger",
       "<b>Glassy polymers are easier to process from melt; crystalline polymers require careful control of crystallization kinetics; crystalline polymers are usually mechanically stronger</b>",
       "Both require identical processing conditions"],
 exp="""<p>讲义的三条对比：<br>
① <i>“<b>Glassy polymers are easier to process</b> from melt – can be obtained quickly on cooling”</i><br>
② <i>“<b>Crystalline polymer processing requires careful control of crystallization kinetics</b>”</i><br>
③ <i>“<b>Crystalline polymers are usually mechanically stronger</b>, though glassy polymers with
high T<sub>g</sub> are adequate for applications”</i></p>
<p><b>本质的权衡</b>：结晶给强度，但结晶<b>要花时间</b>，且冷却条件直接决定最终形貌
（Lecture 10 会讲：低温 → 薄片晶）。玻璃态"冷了就成型"，工艺简单但强度稍逊。</p>""",
 kp="玻璃态易加工、结晶态强度高但需控制动力学",
 src="p.4「Properties of a Glassy Polymer」"),

dict(kind="理解", topic="体积-温度曲线", ans=1,
 stem="On a volume–temperature cooling curve, the path <b>ABHI</b> (liquid → glassy solid) is characterised by:",
 opts=["A jump in volume at T<sub>m</sub>", "A <b>continuous</b> volume change, with T<sub>g</sub> obtained by <b>extrapolation</b>",
       "A jump in volume at T<sub>g</sub>", "No change in volume at all"],
 exp="""<p>讲义对四条路径的说明：</p>
<table class="mini"><thead><tr><th>路径</th><th>终态</th><th>特征</th></tr></thead><tbody>
<tr><td>ABDG</td><td>结晶固体</td><td>T<sub>m</sub> 处<b>体积跳变</b>，dV/dT 斜率改变</td></tr>
<tr><td><b>ABHI</b></td><td><b>玻璃态</b></td><td><b>体积连续</b>，T<sub>g</sub> 由<b>外推</b>得到</td></tr>
<tr><td>ABCEFG</td><td>半结晶</td><td>T<sub>m</sub> 起结晶，剩余部分再玻璃化</td></tr>
<tr><td>ABJK</td><td>玻璃态（快冷）</td><td>体积更大，<b>T<sub>g</sub>′ 更高</b></td></tr>
</tbody></table>
<p class="trap"><b>"外推"是关键词</b>——玻璃化处曲线只是<b>拐折</b>（斜率变），没有跳变，
所以 T<sub>g</sub> 必须由两条直线段延长线的<b>交点</b>确定，而不能直接读。</p>""",
 kp="ABHI：体积连续、只有斜率变，T_g 靠两直线外推交点确定",
 src="p.5「Characteristics of Glass and Melting Transition」"),

dict(kind="理解", topic="冷却速率对 Tg 的影响", ans=1,
 stem="Path ABJK represents cooling at a <b>faster</b> rate. Compared with slow cooling, fast cooling gives:",
 opts=["A smaller final volume and a lower T<sub>g</sub>",
       "A <b>larger</b> final volume and a <b>higher</b> T<sub>g</sub>",
       "The same volume and T<sub>g</sub>", "A larger volume but a lower T<sub>g</sub>"],
 exp="""<p>讲义：<i>“ABJK – Transition from liquid to glassy solid at <b>faster cooling rate</b>
(<b>insufficient time</b> for molecules to pack, giving overall <b>larger volume</b>;
<b>T<sub>g</sub>′ is higher</b>).”</i></p>
<p><b>为什么</b>：快冷 → 分子来不及堆砌 → 在<b>更高的温度</b>就已经"跟不上"了 → T<sub>g</sub> 偏高，
且冻结下来的结构更疏松（体积大、自由体积多）。</p>
<p class="trap">⚠️ <b>方向极易记反</b>。记住因果：<b>快冷 = 更早冻结 = T<sub>g</sub> 更高 + 体积更大</b>。
慢冷则相反——有时间压实，体积小、T<sub>g</sub> 低。</p>""",
 kp="快冷 → 体积大、T_g 高；慢冷 → 体积小、T_g 低",
 src="p.5「ABJK – faster cooling rate」；p.8「TMA Data Analysis」"),

dict(kind="理解", topic="老化 aging", ans=2,
 stem="A rapidly-cooled glassy sample left at rest will slowly contract toward the volume of a slowly-cooled sample. This is called:",
 opts=["Crystallization", "Crazing", "<b>Aging</b>", "Annealing to the melt"],
 exp="""<p>讲义：<i>“If given sufficient time, a rapidly-cooled sample at rest will contract to give volume
of slowly-cooled sample – known as <b>aging</b> (<b>not desirable</b>)”</i>。</p>
<p><b>本质</b>：玻璃是<b>亚稳</b>的，快冷冻结的疏松结构会自发向更紧密的堆砌缓慢演化——
这是玻璃态"未完成的弛豫"。</p>
<p class="trap"><b>为什么工程上不希望</b>：材料的尺寸、模量、脆性都会<b>随存放时间漂移</b>，
产品性能不稳定。这也是<b>塑料件放久了变脆</b>的原因之一。</p>""",
 kp="aging = 亚稳玻璃向更紧密堆砌的自发弛豫；导致性能随时间漂移",
 src="p.8「Aging (not desirable)」"),

dict(kind="理解", topic="为何取第二次扫描", ans=1,
 stem="Why are TMA and DSC data taken on the <b>second</b> heating scan (heat–cool–heat)?",
 opts=["To warm up the instrument", "To <b>erase the thermal history</b> and get reproducible data",
       "To crystallize the sample", "To remove the solvent"],
 exp="""<p>讲义：<i>“For reproducible data, both TMA and DSC data are obtained at their <b>2nd thermal
scanning cycle</b> (i.e. heat-cool-heat-cool) – <b>to erase thermal history</b>.”</i></p>
<p><b>为什么必须这样做</b>：既然 T<sub>g</sub> 依赖冷却速率和存放历史（aging），
样品"过去经历了什么"就会影响测量结果。第一次升温把这些历史<b>抹掉</b>，
然后在<b>仪器控制的已知速率</b>下降温，第二次升温测到的才是可比较的值。</p>
<p class="trap"><b>报告 T<sub>g</sub> 时必须注明速率</b>——不注明的 T<sub>g</sub> 值严格来说是不完整的。</p>""",
 kp="第二次扫描抹掉热历史；报告 T_g 应注明升降温速率",
 src="p.8「For reproducible data… 2nd thermal scanning cycle」"),

dict(kind="理解", topic="一阶转变的判据", ans=1,
 stem="Melting is a <b>first-order</b> transition because there is a discontinuity in:",
 opts=["The second derivative of G", "The <b>first</b> derivative of G (V and H)",
       "G itself", "The third derivative of G"],
 exp="""<p>由 <b>(∂G/∂p)<sub>T</sub> = V</b> 和 <b>(∂G/∂T)<sub>p</sub> = −S</b>，
V 和 S（以及 H）都是 G 的<b>一阶导数</b>。</p>
<p>熔融时 <b>V 发生跳变</b>（讲义 V–T 图上的台阶）→ G 的一阶导不连续 → <b>一阶转变</b>。</p>
<p class="trap"><b>玻璃化则不同</b>：V <b>连续</b>，跳变发生在 <b>dV/dT</b>（即热膨胀系数 α）
和 <b>C<sub>p</sub></b> 上，这些是 G 的<b>二阶</b>导数 → <b>二阶转变</b>。</p>""",
 kp="熔融：G 的一阶导（V、H）跳变 → 一阶转变", src="p.6「Discontinuity (jump) in 1st derivative of G」"),

dict(kind="理解", topic="二阶转变的判据", ans=2,
 stem="The glass transition is a <b>second-order</b> transition because the jump occurs in:",
 opts=["V and H", "G itself", "<b>α and C<sub>p</sub></b> (second derivatives of G)", "Nothing jumps"],
 exp="""<p>两个二阶导数量：</p>
<div class="fb">α = (1/V)(∂V/∂T)<sub>p</sub> = (1/V)·∂/∂T[(∂G/∂p)<sub>T</sub>]</div>
<div class="fb">C<sub>p</sub> = (∂H/∂T)<sub>p</sub> = T(∂S/∂T)<sub>p</sub> = T·∂/∂T[−(∂G/∂T)<sub>p</sub>]</div>
<p>两者都是 G 的二阶偏导，在 T<sub>g</sub> 处呈<b>台阶式跳变</b>。</p>
<p><b>实验对应</b>：<br>
· <b>TMA</b> 测 V vs T → 拐折 → 由 α 的台阶定 T<sub>g</sub><br>
· <b>DSC</b> 测 (∂q/∂T)<sub>p</sub> vs T → <b>C<sub>p</sub> 的台阶</b> → 定 T<sub>g</sub></p>
<p class="trap"><b>形状对比</b>：熔融在 C<sub>p</sub> 曲线上是<b>尖峰</b>（吸收潜热），
玻璃化是<b>台阶</b>（无潜热）。看曲线形状就能区分。</p>""",
 kp="T_g：α 和 C_p（G 的二阶导）跳变 → 二阶转变；C_p 上是台阶不是尖峰",
 src="p.6「2nd order transition」；p.9「Heat Capacity」"),

dict(kind="理解", topic="TMA 的测量对象", ans=0,
 stem="Thermomechanical Analyser (TMA) / dilatometry data is:",
 opts=["<b>V versus T</b>", "(∂q/∂T)<sub>p</sub> versus T", "Stress versus strain", "Intensity versus 2θ"],
 exp="""<p>讲义明确标注：<b>“TMA data is V vs. T”</b>。</p>
<p><b>原理</b>：测量样品受热时的<b>体积膨胀</b>——通过精确测量高度变化推算体积
（要求样品<b>各向同性</b>膨胀）。</p>
<p><b>不规则形状样品</b>可用<b>填充介质</b>，讲义指明高分子用 <b>Hg（汞）</b>。
填充液必须满足三条：已知热膨胀系数、<b>不与高分子发生化学反应</b>、<b>不溶胀/不溶解</b>高分子。</p>
<p class="trap"><b>TMA 的独特价值</b>：<i>“especially when T<sub>g</sub> not obtainable from DSC”</i>——
某些高分子的 C<sub>p</sub> 台阶很微弱，DSC 测不出来，但体积变化仍然可测。
TMA 还是测<b>热膨胀系数 α</b> 的常规手段。</p>""",
 kp="TMA 数据是 V vs T；高分子用 Hg 作填充介质；DSC 失效时的补充手段",
 src="p.7「Thermomechanical Analyser (TMA) - Dilatometry」"),

dict(kind="理解", topic="DSC 的测量对象", ans=1,
 stem="Differential Scanning Calorimetry (DSC) data is:",
 opts=["V versus T", "<b>(∂q/∂T)<sub>p</sub> versus T</b>", "Torque versus angular velocity", "V<sub>R</sub> versus log M"],
 exp="""<p>讲义标注：<b>“DSC data is (∂q/∂T)<sub>p</sub> vs. T”</b>，即<b>热容</b>随温度的变化。</p>
<p><b>工作原理</b>：<br>
① 样品盘和<b>空参比盘</b>分置两个腔室<br>
② 仪器维持两腔<b>温度相同</b>，并以<b>相同速率</b>升降温<br>
③ 记录每升高 1 K 各自所需的热量<br>
④ <b>用样品盘的减去空盘的</b>，得到样品本身（不含盘）所需的热量</p>
<p class="trap"><b>"差示"（Differential）就体现在第 ④ 步</b>——扣除空盘的贡献。
这是"differential"一词的由来，不是指微分。</p>""",
 kp="DSC 数据是 C_p vs T；「差示」指扣除空参比盘的贡献",
 src="p.10「Differential Scanning Calorimetry (DSC)」"),

dict(kind="理解", topic="按 Tg 分类的应用", ans=1,
 stem="Polymers with T<sub>g</sub> <b>below room temperature</b> are typically used as:",
 opts=["Engineering thermoplastics", "<b>Elastomers</b> (when crosslinked into a permanent network)",
       "Adhesives", "Fibres"],
 exp="""<p>讲义的应用分类表：</p>
<table class="mini"><thead><tr><th>T<sub>g</sub></th><th>用途</th></tr></thead><tbody>
<tr><td><b>低于室温</b></td><td><b>弹性体</b>（交联成永久网络后有极大弹性）</td></tr>
<tr><td>室温 ~ 100°C 且不结晶</td><td>不适合做块体材料，但适合做<b>胶粘剂</b></td></tr>
<tr><td>接近或高于 100°C</td><td><b>热塑性塑料</b>（T<sub>g</sub> 以上加工、冷却成型）</td></tr>
<tr><td>~200°C</td><td><b>工程热塑性塑料</b>（用于更严苛的场合，需求量大）</td></tr>
</tbody></table>
<p class="trap"><b>"低于室温"是弹性体的必要条件之一</b>——Lecture 10 会强调
弹性体必须<b>高于 T<sub>g</sub></b> 才有橡胶弹性。室温使用就要求 T<sub>g</sub> &lt; 室温。</p>""",
 kp="T_g 分档决定用途：<室温弹性体 / 室温–100°C 胶粘剂 / >100°C 塑料 / ~200°C 工程塑料",
 src="p.11「Polymer Applications based on Glass Transition Temperature」"),

dict(kind="理解", topic="主链柔性对 Tg 的影响", ans=1,
 stem="A polymer with a <b>highly flexible</b> backbone will have:",
 opts=["A high T<sub>g</sub>", "A <b>low</b> T<sub>g</sub>", "T<sub>g</sub> = 0 K", "T<sub>g</sub> independent of backbone"],
 exp="""<p>讲义：<i>“<b>High backbone flexibility gives low T<sub>g</sub></b> while <b>rigid backbone gives
high T<sub>g</sub></b> – a more flexible backbone allows for <b>higher chain mobility and rearrangement</b>
at any given temperature.”</i></p>
<p><b>逻辑</b>：T<sub>g</sub> 是链段"动得起来"的温度。主链越柔顺 → 越容易转动 →
在<b>更低的温度</b>就能重排 → T<sub>g</sub> 低。</p>
<p><b>讲义给的反例</b>：<b>PEEK</b>（聚醚醚酮）主链有刚性芳环，
T<sub>g</sub> = <b>143 °C（416 K）</b>——典型的工程热塑性塑料。</p>""",
 kp="主链柔性↑ → T_g↓；刚性芳环主链 → T_g↑（PEEK 143°C）",
 src="p.12「Factors that Affect Tg – Chemical Structure」"),

dict(kind="理解", topic="侧基对 Tg 的影响", ans=2,
 stem="Bulky, rigid side groups (e.g. phenyl, ester) affect T<sub>g</sub> by:",
 opts=["Lowering it, by pushing chains apart", "Having no effect",
       "<b>Raising</b> it, because they impede polymer movement and rearrangement", "Making the polymer crystallize"],
 exp="""<p>讲义：<i>“T<sub>g</sub> <b>increases</b> with larger (and rigid) sidegroup – <b>bulky sidegroups</b>
(eg. phenyl, ester group) <b>impede polymer movement and rearrangement</b>.”</i></p>
<p><b>直观例子</b>：聚乙烯（侧基是 H，T<sub>g</sub> ≈ −120 °C）→
聚丙烯（甲基）→ <b>聚苯乙烯（苯基，T<sub>g</sub> ≈ 100 °C）</b>。
侧基越大越刚，链段转动越困难。</p>
<p class="trap"><b>但要小心</b>：<b>长而柔顺</b>的侧链（如长烷基链）反而<b>降低</b> T<sub>g</sub>——
它们起"内增塑"作用，把主链撑开。讲义强调的是"<b>大而刚性</b>"的侧基。</p>""",
 kp="大而刚性的侧基升高 T_g；长柔性侧链反而起内增塑作用降低 T_g",
 src="p.12「Tg increases with larger (and rigid) sidegroup」"),

dict(kind="理解", topic="分子间作用力对 Tg 的影响", ans=0,
 stem="Polymers containing polar groups such as chloride, nitrile or ester tend to have:",
 opts=["<b>Higher</b> T<sub>g</sub>, due to stronger intermolecular interactions", "Lower T<sub>g</sub>",
       "T<sub>g</sub> unaffected by polarity", "No glass transition at all"],
 exp="""<p>讲义：<i>“Polymers with <b>weak intermolecular interaction have lower T<sub>g</sub></b>,
<b>polar interactions give higher T<sub>g</sub></b> (eg. chloride, nitrile, ester).”</i></p>
<p><b>为什么</b>：极性基团之间的偶极-偶极作用（乃至氢键）像"分子间的胶水"，
链要滑动就必须先克服这些作用 → 需要更高温度 → T<sub>g</sub> 升高。</p>
<p><b>典型对比</b>：聚乙烯（−120 °C，只有色散力）vs <b>PVC</b>（约 80 °C，C–Cl 极性）
vs <b>聚丙烯腈</b>（约 105 °C，强极性腈基）。</p>""",
 kp="极性基团（Cl、CN、酯）增强分子间作用 → T_g 升高",
 src="p.12「polar interactions give higher Tg」"),

dict(kind="计算", topic="Flory-Fox 方程", ans=1,
 stem="The Flory-Fox equation relating T<sub>g</sub> to molecular weight is:",
 opts=["T<sub>g</sub>(M<sub>n</sub>) = T<sub>g</sub>(M<sub>∞</sub>) + K/M<sub>n</sub>",
       "<b>T<sub>g</sub>(M<sub>n</sub>) = T<sub>g</sub>(M<sub>∞</sub>) − K/M<sub>n</sub></b>",
       "1/T<sub>g</sub> = 1/T<sub>g</sub>(M<sub>∞</sub>) − K/M<sub>n</sub>",
       "T<sub>g</sub> = K·M<sub>n</sub>"],
 exp="""<div class="fb">T<sub>g</sub>(M<sub>n</sub>) = T<sub>g</sub>(M<sub>∞</sub>) − K/M<sub>n</sub></div>
<p>K 是经验常数。<b>负号</b>表示：分子量越低，T<sub>g</sub> 比无限大分子量的极限值低得越多。</p>
<p><b>物理原因</b>：<b>链端的自由体积比链中间大</b>。分子量低 → 链端占比高 →
自由体积多 → 链段更易运动 → T<sub>g</sub> 低。</p>
<p class="trap"><b>注意用的是 M<sub>n</sub>（数均）</b>，不是 M<sub>w</sub>——
因为链端数目正比于<b>链的条数</b>，而 M<sub>n</sub> 正是数条数的那个平均。</p>""",
 kp="Flory-Fox：T_g = T_g(∞) − K/M_n；链端自由体积是物理根源，用 Mn",
 src="p.13「Flory-Fox Equation」"),

dict(kind="计算", topic="Flory-Fox 计算", ans=2,
 stem="A polymer has T<sub>g</sub>(M<sub>∞</sub>) = 378 K and K = 1.5×10⁵ K·g/mol. What is T<sub>g</sub> for M<sub>n</sub> = 5,000 g/mol?",
 opts=["318 K", "333 K", "<b>348 K</b>", "363 K"],
 exp="""<div class="fb">T<sub>g</sub> = 378 − 1.5×10⁵/5,000 = 378 − 30 = <b>348 K</b></div>
<p>即 75 °C，比高分子量极限（378 K = 105 °C）<b>低了 30 K</b>。</p>
<p class="trap"><b>量级检验</b>：M<sub>n</sub> = 5,000 对高分子来说是<b>很低</b>的分子量（约 50 个单体），
链端占比高，T<sub>g</sub> 降低 30 K 是合理的。若 M<sub>n</sub> = 10⁵，降低量只有 1.5 K，
基本达到极限值——这解释了为什么<b>高分子量高分子的 T<sub>g</sub> 几乎不随 M 变化</b>。</p>""",
 kp="Flory-Fox 直接代入；高分子量时 K/M_n 很小，T_g 趋于平台",
 src="p.13「Flory-Fox Equation」"),

dict(kind="计算", topic="由两点求 Flory-Fox 常数", ans=1,
 stem="For polystyrene, T<sub>g</sub> = 90 °C at M<sub>n</sub> = 20,000 and T<sub>g</sub>(M<sub>∞</sub>) = 100 °C. What is T<sub>g</sub> at M<sub>n</sub> = 10,000?",
 opts=["45 °C", "<b>80 °C</b>", "85 °C", "95 °C"],
 exp="""<p><b>① 求 K</b>：90 = 100 − K/20,000 → K/20,000 = 10 → <b>K = 2×10⁵</b></p>
<p><b>② 代入</b>：T<sub>g</sub> = 100 − 2×10⁵/10,000 = 100 − 20 = <b>80 °C</b></p>
<p><b>快捷法</b>：M<sub>n</sub> <b>减半</b> → K/M<sub>n</sub> <b>加倍</b> →
偏离量从 10 °C 变成 20 °C → 100 − 20 = 80 °C。</p>
<p class="trap"><b>选项 D（95 °C）</b>是把关系当成正比例了；
<b>选项 A（45 °C）</b>是把 T<sub>g</sub> 本身减半。</p>""",
 kp="两点定 K 再外推；M_n 减半则偏离量加倍", src="p.13「Flory-Fox」"),

dict(kind="理解", topic="增塑剂", ans=1,
 stem="Low molecular weight plasticizer is added to a polymer in order to:",
 opts=["Raise T<sub>g</sub>", "<b>Lower</b> T<sub>g</sub>", "Increase crystallinity", "Crosslink the chains"],
 exp="""<p>讲义：<i>“Low molecular weight <b>plasticizer</b> can be used to <b>lower T<sub>g</sub></b>.”</i></p>
<p><b>原理</b>：小分子增塑剂挤进链之间，把链<b>撑开</b>，增加自由体积、削弱链间作用力
→ 链段在更低温度就能运动 → T<sub>g</sub> 下降。</p>
<p><b>最著名的例子</b>：<b>PVC</b>。纯 PVC 的 T<sub>g</sub> ≈ 80 °C，室温下又硬又脆（用作下水管道）；
加入邻苯二甲酸酯类增塑剂后 T<sub>g</sub> 降到室温以下，变成柔软的<b>软管、人造革、保鲜膜</b>。
<b>同一种高分子，靠增塑剂做出完全不同的产品。</b></p>
<p class="trap"><b>定量计算用 Fox 方程</b>（把增塑剂当作一个低 T<sub>g</sub> 组分），见下题。</p>""",
 kp="增塑剂增加自由体积、降低 T_g；PVC 硬管 vs 软管是同一材料的两种状态",
 src="p.13「Low molecular weight plasticizer」"),

dict(kind="理解", topic="交联对 Tg 的影响", ans=0,
 stem="Crosslinking a polymer affects T<sub>g</sub> by:",
 opts=["<b>Raising</b> it, because chain movement is restricted", "Lowering it",
       "Eliminating the glass transition", "Having no effect"],
 exp="""<p>讲义：<i>“<b>Crosslinking restricts chain movements and increases T<sub>g</sub></b>.”</i></p>
<p>交联点是<b>永久的化学锚点</b>，链段能活动的范围被限制在交联点之间，
需要更高温度才能达到同样的活动能力。</p>
<p class="trap"><b>交联度极高时</b>（热固性树脂）T<sub>g</sub> 可以高到<b>超过分解温度</b>——
材料在玻璃化之前就已经烧掉了。这正是<b>热固性材料不能热加工</b>（Lecture 1）的微观原因。</p>
<p><b>但弹性体也是交联的</b>——区别在于<b>交联度低</b>，T<sub>g</sub> 仍在室温以下，
交联只是防止链永久滑移，不阻碍局部链段运动。</p>""",
 kp="交联限制链运动 → T_g 升高；高度交联可使 T_g 超过分解温度",
 src="p.13「Crosslinking」；p.5（L1）热固性"),

dict(kind="计算", topic="Fox 方程", ans=0,
 stem="The Fox equation for the T<sub>g</sub> of a miscible blend of A and B is:",
 opts=["<b>1/T<sub>g</sub> = w<sub>A</sub>/T<sub>g(A)</sub> + w<sub>B</sub>/T<sub>g(B)</sub></b>",
       "T<sub>g</sub> = w<sub>A</sub>T<sub>g(A)</sub> + w<sub>B</sub>T<sub>g(B)</sub>",
       "T<sub>g</sub> = √(T<sub>g(A)</sub>T<sub>g(B)</sub>)",
       "ln T<sub>g</sub> = w<sub>A</sub>ln T<sub>g(A)</sub> + w<sub>B</sub>ln T<sub>g(B)</sub>"],
 exp="""<div class="fb">1/T<sub>g</sub> = w<sub>A</sub>/T<sub>g(A)</sub> + w<sub>B</sub>/T<sub>g(B)</sub></div>
<p>w<sub>A</sub>、w<sub>B</sub> 是<b>质量分数</b>（weight fractions）。</p>
<p class="trap">⚠️ <b>两个必须注意的点</b>：<br>
① <b>是倒数的加权平均</b>，不是线性加权（选项 B 是最常见的错误）<br>
② <b>必须用绝对温度 K</b>——用摄氏度算完全错，遇到负的 T<sub>g</sub> 分母还会出问题</p>
<p><b>讲义还给了更精确的版本</b>（基于熵的考虑）：</p>
<div class="fb">ln T<sub>g</sub> = [w<sub>A</sub>ΔC<sub>p(A)</sub>ln T<sub>g(A)</sub> + w<sub>B</sub>ΔC<sub>p(B)</sub>ln T<sub>g(B)</sub>] / [w<sub>A</sub>ΔC<sub>p(A)</sub> + w<sub>B</sub>ΔC<sub>p(B)</sub>]</div>
<p>其中 ΔC<sub>p</sub> 是各组分玻璃化时的热容变化。图上 Fox 方程是<b>虚线</b>，这个是<b>实线</b>。</p>""",
 kp="Fox：1/T_g 的质量分数加权；必须用 K；更精确版本含 ΔC_p 权重",
 src="p.14「Fox Equation」"),

dict(kind="计算", topic="Fox 方程计算", ans=1,
 stem="A miscible blend is 80 wt% polymer A (T<sub>g</sub> = 100 °C) and 20 wt% plasticizer B (T<sub>g</sub> = −50 °C). Estimate the blend T<sub>g</sub>.",
 opts=["70 °C", "<b>56 °C</b>", "40 °C", "20 °C"],
 exp="""<p><b>① 换成绝对温度</b>：T<sub>g(A)</sub> = 373 K，T<sub>g(B)</sub> = 223 K</p>
<p><b>②</b> 1/T<sub>g</sub> = 0.8/373 + 0.2/223 = 0.002145 + 0.000897 = <b>0.003042</b></p>
<p><b>③</b> T<sub>g</sub> = 1/0.003042 = 328.8 K = <b>55.6 °C ≈ 56 °C</b></p>
<p class="trap">⚠️ <b>选项 A（70 °C）同时踩两个坑</b>：它是<b>线性加权</b>的结果
0.8(100) + 0.2(−50) = 70。Fox 是<b>倒数加权</b>，结果总是<b>低于</b>线性值。</p>
<p><b>物理意义</b>：只加 20% 增塑剂就把 T<sub>g</sub> 从 100 °C 拉到 56 °C——
增塑剂的效果<b>非线性地强</b>，这正是它实用的原因。</p>""",
 kp="Fox 计算必须用 K；结果总低于线性加权值", src="p.14「Fox Equation」"),

dict(kind="理解", topic="共混物 Tg 的诊断价值", ans=2,
 stem="A blend of two polymers shows <b>two separate</b> glass transitions. This indicates that the blend is:",
 opts=["Miscible", "Crystalline", "<b>Immiscible</b> (phase separated)", "Crosslinked"],
 exp="""<p>Fox 方程的前提是 <b>miscible</b>（可混溶）——讲义标题写的就是
<i>“T<sub>g</sub> vs. composition for <b>miscible</b> polystyrene/PPO blends”</i>。</p>
<table class="mini"><thead><tr><th>观察</th><th>结论</th></tr></thead><tbody>
<tr><td><b>一个</b> T<sub>g</sub>，介于两组分之间</td><td><b>可混溶</b>（单相），符合 Fox 方程</td></tr>
<tr><td><b>两个</b> T<sub>g</sub>，各自接近纯组分</td><td><b>不互溶</b>（相分离）</td></tr>
</tbody></table>
<p class="trap"><b>这是 DSC 最重要的应用之一</b>：数 T<sub>g</sub> 的个数就能判断相容性，
比显微镜快得多。</p>
<p><b>与 Lecture 3 呼应</b>：高分子共混时<b>两项</b>混合熵都被 N 削弱，
所以<b>绝大多数高分子对不相容</b>——看到两个 T<sub>g</sub> 才是常态，
PS/PPO 这样的可混溶体系反而<b>稀有</b>。</p>""",
 kp="一个 T_g = 可混溶；两个 T_g = 相分离。DSC 数 T_g 是判断相容性的快捷手段",
 src="p.14「miscible polystyrene/PPO blends」；p.45（L3）"),

dict(kind="理解", topic="自由体积的统一解释", ans=1,
 stem="Which set of factors <b>all</b> lower T<sub>g</sub> through the same underlying mechanism (increased free volume / easier chain motion)?",
 opts=["Crosslinking, bulky side groups, polar groups",
       "<b>Low molecular weight, plasticizer addition, flexible backbone</b>",
       "Aromatic backbone, high molecular weight, crystallinity",
       "Fast cooling, crosslinking, polar groups"],
 exp="""<p>三者的共同机理都是<b>让链段更容易运动</b>：<br>
· <b>低分子量</b> → 链端多 → 链端处自由体积大<br>
· <b>加增塑剂</b> → 小分子撑开链间距 → 自由体积增加<br>
· <b>柔性主链</b> → 转动能垒低 → 同样温度下活动性更高</p>
<p><b>反方向的因素（升高 T<sub>g</sub>）</b>：刚性芳环主链、大而刚性的侧基、
极性相互作用、交联、高分子量。</p>
<p class="trap"><b>快冷升高 T<sub>g</sub> 是另一回事</b>——它不改变材料本身，
只是改变了<b>测量时的时间尺度</b>（动力学效应），所以不能与上述结构因素混为一谈。</p>""",
 kp="降 T_g：低分子量、增塑剂、柔性主链（都增大自由体积）；快冷是动力学效应不同源",
 src="p.12–13「Factors that Affect Glass Transition Temperature」"),

dict(kind="理解", topic="Tg 与 Tm 的关系", ans=2,
 stem="For a <b>semi-crystalline</b> polymer cooled from the melt (path ABCEFG), the sequence of events is:",
 opts=["Glass transition first, then crystallization",
       "Only crystallization occurs",
       "<b>Crystallization begins at T<sub>m</sub>, followed by glass transition of the remaining amorphous portion</b>",
       "Both happen at the same temperature"],
 exp="""<p>讲义对 ABCEFG 的说明：<i>“Transition from liquid to semi-crystalline solid
(<b>crystallization begins at T<sub>m</sub></b>, followed by <b>glass transition for remaining polymer</b>).”</i></p>
<p><b>降温顺序</b>：T<sub>m</sub> &gt; T<sub>g</sub>，所以先到 T<sub>m</sub>（部分结晶），
剩下没结晶的非晶部分继续降温，到 T<sub>g</sub> 时玻璃化。</p>
<p class="trap"><b>半结晶高分子同时有 T<sub>m</sub> 和 T<sub>g</sub></b>——
DSC 曲线上会看到<b>两个特征</b>：T<sub>g</sub> 处的<b>台阶</b>和 T<sub>m</sub> 处的<b>吸热尖峰</b>。
纯玻璃态高分子只有台阶，没有尖峰。</p>""",
 kp="半结晶体：T_m 先结晶、剩余非晶在 T_g 玻璃化；DSC 上台阶 + 尖峰并存",
 src="p.5「ABCEFG」；p.9"),

dict(kind="计算", topic="热膨胀系数", ans=1,
 stem="The coefficient of thermal expansion is defined as:",
 opts=["α = (∂V/∂T)<sub>p</sub>", "<b>α = (1/V)(∂V/∂T)<sub>p</sub></b>", "α = V(∂T/∂V)<sub>p</sub>", "α = (∂p/∂T)<sub>V</sub>"],
 exp="""<div class="fb">α = (1/V) (∂V/∂T)<sub>p</sub></div>
<p><b>为什么要除以 V</b>：这样得到的是<b>相对</b>（分数）膨胀率，单位是 K⁻¹，
与样品大小无关——是<b>材料的本征性质</b>。</p>
<p class="trap"><b>玻璃化时 α 发生跳变</b>：玻璃态的 α 比橡胶态<b>小</b>
（链段冻结，只剩键长键角的振动贡献）。TMA 上表现为 V–T 曲线<b>斜率变小</b>，
两段直线的交点就是 T<sub>g</sub>。</p>
<p><b>工程意义</b>：α 的跳变意味着材料跨越 T<sub>g</sub> 时尺寸稳定性突变，
这是电子封装等精密应用必须考虑的。</p>""",
 kp="α = (1/V)(∂V/∂T)_p，除以 V 使其成为材料本征量；T_g 处 α 跳变",
 src="p.6「Coefficient of Thermal Expansion (α)」；p.7"),

dict(kind="理解", topic="填充介质的要求", ans=3,
 stem="When a filling medium (e.g. Hg) is used in TMA for irregularly-shaped samples, the liquid must satisfy all EXCEPT:",
 opts=["Have a known thermal expansion coefficient", "Not react chemically with the polymer",
       "Not swell or dissolve the polymer", "<b>Have the same density as the polymer</b>"],
 exp="""<p>讲义列出的三条要求：<i>“liquid must have a <b>known thermal expansion coefficient</b> and must
<b>not interact chemically / swell / dissolve</b> the polymer”</i>。</p>
<p><b>密度相同不是要求</b>——事实上汞的密度（13.5 g/cm³）远大于任何高分子（约 1 g/cm³）。</p>
<p><b>为什么这三条重要</b>：<br>
① 已知 α：测到的是"高分子 + 液体"的总膨胀，必须能<b>扣除</b>液体的贡献<br>
② 不反应、③ 不溶胀/溶解：否则测的就不是高分子本身的体积变化了</p>
<p class="trap"><b>汞为什么合适</b>：α 精确已知、化学惰性、不润湿也不溶解有机高分子。
（现代实验室因毒性已改用其他介质，但讲义给的是经典方案。）</p>""",
 kp="填充介质三要求：已知 α、不反应、不溶胀溶解；密度无需匹配",
 src="p.7「Filling medium: Hg for polymers」"),
]

L.append(dict(kind="计算", topic="Fox 方程反解组成", ans=2,
 stem="Polymer A (T<sub>g</sub> = 105 °C) is to be plasticized with B (T<sub>g</sub> = −73 °C) to give a blend T<sub>g</sub> of 25 °C. What weight fraction of plasticizer is needed?",
 opts=["0.15", "0.20", "<b>0.30</b>", "0.45"],
 exp="""<p><b>① 全部换成 K</b>：T<sub>g(A)</sub> = 378 K，T<sub>g(B)</sub> = 200 K，目标 T<sub>g</sub> = 298 K</p>
<p><b>② 代入 Fox</b>（令 w<sub>B</sub> = w，则 w<sub>A</sub> = 1 − w）：</p>
<div class="fb">1/298 = (1−w)/378 + w/200</div>
<p>0.003356 = 0.002646 − 0.002646w + 0.005w</p>
<p>0.003356 − 0.002646 = 0.002354 w　→　w = 0.000710 / 0.002354 = <b>0.302 ≈ 0.30</b></p>
<p>即需要 <b>30 wt% 的增塑剂</b>。</p>
<p class="trap"><b>本题真正要考的是流程</b>：<br>
① <b>先换 K</b>（三个温度都要换）<br>
② 设未知数代入 Fox<br>
③ 解一元一次方程<br>
用摄氏度做这道题会得到完全不同且无意义的结果。</p>""",
 kp="Fox 方程可反解所需增塑剂用量；三个温度都必须换成 K",
 src="p.14「Fox Equation」"))
