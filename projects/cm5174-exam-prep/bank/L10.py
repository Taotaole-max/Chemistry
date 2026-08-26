# -*- coding: utf-8 -*-
LEC = 10
TITLE = "Solid State Properties – Elastomeric and Crystalline State"
CN = "弹性态与结晶态"
SRC = "讲义 Lectures_8-10"
L = [
dict(kind="理解", topic="弹性体的必要条件", ans=3,
 stem="Which set lists the conditions a polymer must satisfy to behave as an elastomer?",
 opts=["Below T<sub>g</sub>, highly crystalline, uncrosslinked",
       "Above T<sub>g</sub>, highly crystalline, uncrosslinked",
       "Below T<sub>g</sub>, amorphous, crosslinked",
       "<b>Above T<sub>g</sub>, negligible crystalline content, crosslinked</b>"],
 exp="""<p>讲义列出的弹性体特征：<br>
· The polymer is <b>above its glass transition temperature (T<sub>g</sub>)</b><br>
· The polymer has <b>zero or negligible crystalline content</b><br>
· The polymer <b>should be crosslinked</b><br>
· Deformation is <b>completely recoverable</b><br>
· Modulus is much lower than brittle or ductile polymer<br>
· <b>Higher modulus when highly-stretched</b></p>
<p><b>三个条件各自的作用</b>：<br>
· <b>高于 T<sub>g</sub></b> → 链段能自由运动（否则是玻璃，硬而脆）<br>
· <b>无结晶</b> → 没有刚性晶区限制形变<br>
· <b>交联</b> → 防止链永久滑移，保证<b>完全可恢复</b></p>""",
 kp="弹性体三条件：高于 T_g、无结晶、已交联；缺一不可",
 src="p.34「Characteristics of Elastomers」"),

dict(kind="理解", topic="高度拉伸时模量升高", ans=1,
 stem="An elastomer shows a <b>higher</b> modulus when highly stretched because:",
 opts=["It crosslinks further during stretching",
       "<b>The chains approach their fully extended conformation, so further extension requires stretching bonds rather than unravelling coils</b>",
       "It crystallizes into a glass", "The temperature drops"],
 exp="""<p>讲义在应力-应变图上标注 <b>“Modulus is higher before fracture”</b>。</p>
<p><b>物理图像</b>：弹性体的低模量来自<b>构象舒展</b>（熵弹性）——把卷曲的链拉直几乎不费力。
但当链接近<b>完全伸直</b>时，再拉就要<b>拉伸化学键和键角</b>了，这需要大得多的力
→ 曲线急剧上翘。</p>
<p class="trap"><b>与韧性高分子的"应变硬化"要区分</b>：<br>
· 韧性塑料的应变硬化是<b>链取向</b>造成的（不可恢复）<br>
· 弹性体的上翘是<b>构象耗尽</b>（仍然可恢复）<br>
天然橡胶还会有<b>应变诱导结晶</b>进一步强化，但那超出本讲范围。</p>""",
 kp="高度拉伸时构象自由度耗尽，转为拉伸键长键角 → 模量升高",
 src="p.34「Modulus is higher before fracture」"),

dict(kind="理解", topic="常见弹性体", ans=0,
 stem="Which list contains only polymers named in the lecture as popular elastomers?",
 opts=["<b>cis-1,4-polyisoprene, polysiloxanes, poly(acrylonitrile-butadiene)</b>",
       "Polystyrene, PMMA, polycarbonate", "Polyethylene, polypropylene, PET",
       "Epoxy, phenol-formaldehyde, PEEK"],
 exp="""<p>讲义列出：<i>“Popular elastomers include <b>cis-1,4-polyisoprene (rubber)</b>,
<b>polysiloxanes (silicone)</b>, <b>poly-acrylonitrile-butadiene (nitrile rubber)</b>.”</i></p>
<p class="trap"><b>其余选项分别是</b>：<br>
· B：<b>脆性玻璃态</b>高分子（T<sub>g</sub> 高于室温）<br>
· C：<b>半结晶</b>高分子<br>
· D：<b>热固性</b>树脂（高度交联）+ 工程塑料</p>
<p><b>注意"cis-"很关键</b>：<b>cis</b>-1,4-聚异戊二烯是天然橡胶（弹性体）；
而 <b>trans</b>-1,4-聚异戊二烯是杜仲胶，<b>能结晶</b>、硬而不弹。
<b>同样的化学式，立构不同则性质完全不同</b>——这与本讲后半的"立构规整性决定能否结晶"是同一主题。</p>""",
 kp="三种常见弹性体；cis vs trans 聚异戊二烯说明立构决定性质",
 src="p.34「Popular elastomers」"),

dict(kind="理解", topic="硫化", ans=1,
 stem="Vulcanization refers to:",
 opts=["Melting rubber at high temperature",
       "<b>Crosslinking cis-1,4-polyisoprene with sulfur by heating</b>",
       "Dissolving rubber in a solvent", "Adding carbon black filler"],
 exp="""<p>讲义：<i>“Traditionally known as <b>vulcanization</b>. <b>Sulfur</b> is used to crosslink
<b>cis-1,4-polyisoprene (rubber)</b> by <b>heating</b>. The mechanism of vulcanization is
<b>not well understood</b>, but evidence points to <b>ionic-type reaction</b>.”</i></p>
<p><b>交联点的作用</b>：<i>“Each crosslink forms a <b>permanent anchor</b> between 2 chains.
Crosslinking creates a network and <b>preserves shape</b> of elastomer – allows chains to
<b>return to original positions</b> after deformation.”</i></p>
<p class="trap"><b>两个容易被考的细节</b>：<br>
① 硫化的机理<b>至今未完全清楚</b>，证据指向<b>离子型</b>反应（不是自由基）<br>
② 交联是<b>永久的化学键</b>——这是弹性体形变完全可恢复的根本保证</p>""",
 kp="硫化 = 硫加热交联 cis-1,4-聚异戊二烯；机理未明，证据指向离子型反应",
 src="p.35「Crosslinking of Rubber」"),

dict(kind="理解", topic="弹性功的热力学处理", ans=2,
 stem="For an elastomer, the additional work term dw<sub>add</sub> in dG = Vdp − SdT + dw<sub>add</sub> is written as:",
 opts=["−p dV", "T dS", "<b>f dL</b>（elastic work）", "μ dn"],
 exp="""<p>讲义把额外功取为<b>弹性功</b>：<b>dw<sub>add</sub> = f dL</b>（力 × 长度变化），于是</p>
<div class="fb">dG = V dp − S dT + f dL</div>
<p>写成全微分并对比系数：</p>
<div class="fb">(∂G/∂p)<sub>T,L</sub> = V　　(∂G/∂T)<sub>p,L</sub> = −S　　<b>(∂G/∂L)<sub>p,T</sub> = f</b></div>
<p class="trap"><b>这是"额外功"这个抽象概念的第三次具体化</b>：<br>
· <b>L2</b>：dw<sub>add</sub> = 组成变化 → 引出<b>化学势 μ</b><br>
· <b>L2</b>：dw<sub>add</sub> = 电功 → "自由"能的含义<br>
· <b>L10</b>：dw<sub>add</sub> = <b>弹性功 f dL</b> → 引出<b>力 f 是 G 对长度的偏导</b></p>""",
 kp="dw_add = f dL → f = (∂G/∂L)_{p,T}；与化学势同源的处理手法",
 src="p.36「Thermodynamic Behaviour of Elastomers」"),

dict(kind="理解", topic="Maxwell 关系", ans=1,
 stem="Because the order of partial differentiation is unimportant, one obtains:",
 opts=["(∂f/∂T)<sub>p,L</sub> = +(∂S/∂L)<sub>p,T</sub>", "<b>(∂f/∂T)<sub>p,L</sub> = −(∂S/∂L)<sub>p,T</sub></b>",
       "(∂f/∂L)<sub>p,T</sub> = −(∂S/∂T)<sub>p,L</sub>", "(∂f/∂T)<sub>p,L</sub> = (∂V/∂L)<sub>p,T</sub>"],
 exp="""<p>对 G 的混合二阶偏导，先对 T 后对 L 与先对 L 后对 T 结果相同：</p>
<div class="fb">∂/∂L[(∂G/∂T)<sub>p,L</sub>]<sub>p,T</sub> = ∂/∂T[(∂G/∂L)<sub>p,T</sub>]<sub>p,L</sub></div>
<p>左边 = ∂(−S)/∂L，右边 = ∂f/∂T，故</p>
<div class="fb">(∂f/∂T)<sub>p,L</sub> = −(∂S/∂L)<sub>p,T</sub></div>
<p><b>这个关系的威力</b>：左边是<b>可以直接测量</b>的（固定伸长率，测应力随温度的变化）；
右边是<b>无法直接测量</b>的（拉伸对熵的影响）。<b>Maxwell 关系把不可测的量变成了可测的量。</b></p>""",
 kp="Maxwell 关系 (∂f/∂T)_{p,L} = −(∂S/∂L)_{p,T}；把不可测的熵变化换成可测的应力-温度斜率",
 src="p.36「Because the order of differentiation is unimportant」"),

dict(kind="理解", topic="应力随温度上升的含义", ans=1,
 stem="At a fixed extension of 350%, the stress in an elastomer <b>increases</b> with temperature. This means:",
 opts=["Entropy increases with length", "<b>Entropy decreases with length</b>",
       "Enthalpy decreases with length", "The polymer is below T<sub>g</sub>"],
 exp="""<p>由 (∂f/∂T)<sub>p,L</sub> = −(∂S/∂L)<sub>p,T</sub>：</p>
<p>实验观察 <b>斜率为正</b>（f 随 T 增大）→ 右边为正 → <b>(∂S/∂L) 为负</b> → <b>拉伸使熵下降</b>。</p>
<p>讲义解释：<i>“The decrease in entropy is due to <b>loss of conformational possibilities</b> in an
<b>extended (stretched) ordered form</b>.”</i></p>
<p class="trap"><b>直观理解</b>：无规线团有<b>天文数字</b>种构象；完全伸直的链<b>只有一种</b>。
拉伸就是把体系从"构象很多"逼到"构象很少"——熵必然下降。</p>""",
 kp="f–T 斜率为正 ⇒ ∂S/∂L < 0 ⇒ 拉伸降低构象熵",
 src="p.37「Stress in Elastomer vs. Temperature at fixed Strain」"),

dict(kind="理解", topic="曲线的反转点", ans=2,
 stem="At low temperature the stress–temperature curve of an elastomer shows an <b>inversion point</b>. This is due to:",
 opts=["Crystallization", "Chemical degradation",
       "<b>The glass transition — the polymer is no longer elastomeric</b>", "Melting"],
 exp="""<p>讲义：<i>“The <b>inversion point</b> (at low temp) is due to <b>glass transition</b> –
the polymer is <b>no longer elastomeric</b>.”</i></p>
<p><b>为什么会反转</b>：低于 T<sub>g</sub> 后链段被冻结，形变不再靠构象舒展（熵弹性），
而是靠<b>拉伸键长键角</b>（能量弹性，像普通固体一样）。此时升温会使材料<b>软化</b>，
应力<b>下降</b>而非上升——斜率变号。</p>
<p class="trap"><b>这个反转点是"熵弹性"与"能量弹性"的分界</b>，
也再次印证弹性体<b>必须高于 T<sub>g</sub></b> 这个条件。</p>""",
 kp="低温反转点 = 玻璃化；其下是能量弹性而非熵弹性",
 src="p.37「The inversion point (at low temp) is due to glass transition」"),

dict(kind="理解", topic="y 轴截距的意义", ans=2,
 stem="In f = (∂H/∂L)<sub>p,T</sub> − T(∂S/∂L)<sub>p,T</sub>, the <b>y-intercept</b> of the f-vs-T plot corresponds to (∂H/∂L). Experimentally this value is:",
 opts=["Very large and positive", "Very large and negative",
       "<b>Near zero</b>, meaning stretching stores almost no energy as enthalpy",
       "Equal to the modulus"],
 exp="""<p>讲义：<i>“The <b>y-intercept</b> of the stress vs temp curve is therefore the change in enthalpy
with change in length. Since the (∂H/∂L) value is <b>near to zero</b>, the stress and extension
<b>does not cause heat energy to be stored</b> within the elastomer (isothermal condition).
<b>The stress is mainly used for decreasing entropy in the elastomer.</b>”</i></p>
<div class="fb">橡胶弹性是<b>熵弹性</b>，不是键的拉伸</div>
<p class="trap"><b>与金属的根本区别</b>：<br>
· <b>金属/陶瓷</b>：<b>能量弹性</b>——拉伸原子间键，储存<b>焓</b>；升温软化（模量下降）<br>
· <b>橡胶</b>：<b>熵弹性</b>——舒展构象，几乎不储存焓；<b>升温反而变硬</b>（f 随 T 上升）</p>
<p><b>"升温变硬"是熵弹性最反直觉也最标志性的证据。</b></p>""",
 kp="截距 (∂H/∂L) ≈ 0 → 应力几乎全部用于降熵；橡胶升温变硬，金属升温变软",
 src="p.38「Entropic Nature of Stress」"),

dict(kind="计算", topic="绝热拉伸", ans=0,
 stem="During <b>adiabatic</b> extension of an elastomer, C<sub>V,p</sub>ΔT = AEL²/(2L₀). This means:",
 opts=["<b>The rubber heats up when stretched</b>", "The rubber cools when stretched",
       "The temperature is unchanged", "The rubber melts"],
 exp="""<p>讲义推导：绝热时无热交换，弹性功全部变成内能：</p>
<div class="fb">f = (∂U/∂L)<sub>V,p</sub> = C<sub>V,p</sub>(∂T/∂L)<sub>V,p</sub>　⇒　∫f dL = ∫C<sub>V,p</sub> dT</div>
<p>代入 f/A = E·L/L₀ 积分得 <b>C<sub>V,p</sub>ΔT = AEL²/(2L₀)</b>。</p>
<p>右边<b>恒为正</b>（都是正量）→ <b>ΔT &gt; 0</b> → 讲义原话：
<i>“<b>rubber heats up when stretched under adiabatic condition</b>”</i>。</p>
<p class="trap"><b>可以亲手验证</b>：把橡皮筋<b>迅速</b>拉长，立刻贴到嘴唇上——能明显感到<b>变热</b>；
保持拉伸等它冷却后<b>迅速松开</b>，再贴嘴唇——会感到<b>变凉</b>。
这是熵弹性最直接的宏观证据（也是橡胶热机的原理）。</p>""",
 kp="绝热拉伸橡胶升温（C_V,p ΔT = AEL²/2L₀）；松弛则降温",
 src="p.39「Adiabatic Extension of Elastomers」"),

dict(kind="理解", topic="立构规整性与结晶", ans=1,
 stem="Which polymers can crystallize?",
 opts=["Atactic polymers only", "<b>Stereo-regular (isotactic, syndiotactic) polymers</b>",
       "All polymers regardless of tacticity", "Only crosslinked polymers"],
 exp="""<p>讲义：<i>“<b>Stereo-regular (isotactic, syndiotactic)</b> polymers crystallizes –
<b>necessary for packing into regular unit cell</b>. <b>Stereo-irregular (atactic)</b> polymers
<b>do not crystallize</b>.”</i></p>
<p><b>三种立构</b>：<br>
· <b>Isotactic 全同</b>：所有取代基 R 在同一侧 → <b>能结晶</b><br>
· <b>Syndiotactic 间同</b>：R 交替排列 → <b>能结晶</b><br>
· <b>Atactic 无规</b>：R 随机排列 → <b>不能结晶</b></p>
<p class="trap"><b>讲义给的例外</b>：<i>“polymers with <b>small polar side groups</b> may sometimes
crystallize (e.g. <b>poly(vinyl alcohol)</b>, <b>poly(vinyl fluoride)</b>)”</i>——
侧基<b>又小又极性</b>时，即使无规也可能结晶（侧基小到不妨碍堆砌，极性又提供额外作用力）。</p>""",
 kp="全同/间同能结晶，无规不能；例外是小极性侧基（PVA、聚氟乙烯）",
 src="p.40「Factors that Affect Polymer Crystallization」"),

dict(kind="理解", topic="结晶的好处", ans=3,
 stem="Which are stated benefits of polymer crystallization?",
 opts=["Improved transparency only", "Lower melting point",
       "Easier melt processing", "<b>Enhanced mechanical strength, greater resistance to degradation, better barrier properties</b>"],
 exp="""<p>讲义列出三条 <b>Benefits of Polymer Crystallization</b>：<br>
· <b>Enhances mechanical strength</b>（力学强度提高）<br>
· <b>Greater resistance to degradation</b>（抗降解性更好）<br>
· <b>Better barrier properties</b>（阻隔性更好）</p>
<p><b>共同原因</b>：晶区中链<b>紧密有序堆砌</b>，小分子（氧气、水、溶剂、化学试剂）
<b>难以渗入</b>，链也难以移动。</p>
<p class="trap"><b>但代价是</b>：<br>
· <b>不透明</b>（晶区/非晶区折射率差 → 散射，Lecture 8）<br>
· <b>加工更难</b>（需精细控制结晶动力学，Lecture 8）</p>
<p><b>阻隔性的实际应用</b>：PET 饮料瓶靠结晶度阻隔 CO₂，这就是碳酸饮料瓶用 PET 的原因。</p>""",
 kp="结晶三大好处：强度、抗降解、阻隔；代价是不透明与加工难",
 src="p.40「Benefits of Polymer Crystallization」"),

dict(kind="理解", topic="晶体的三个层级", ans=1,
 stem="The three structural levels of a polymer crystal, from smallest to largest, are:",
 opts=["Spherulite → lamellae → unit cell", "<b>Unit cell → lamellae → spherulite</b>",
       "Lamellae → unit cell → spherulite", "Unit cell → spherulite → lamellae"],
 exp="""<table class="mini"><thead><tr><th>层级</th><th>结构</th><th>尺度</th></tr></thead><tbody>
<tr><td><b>Unit Cell 晶胞</b></td><td>相邻链堆砌形成的重复单元</td><td><b>2–20 Å</b>（每边）</td></tr>
<tr><td><b>Lamellae 片晶</b></td><td>晶胞堆成的薄二维片</td><td><b>厚 100–500 Å</b>，宽数微米</td></tr>
<tr><td><b>Spherulite 球晶</b></td><td>片晶堆成的三维球</td><td><b>数十至数百微米</b></td></tr>
</tbody></table>
<p><b>跨越四个数量级</b>：从 Å 到几百 μm。这三级结构是理解高分子结晶形貌的框架。</p>
<p class="trap"><b>球晶大到可以用光学显微镜看到</b>（几十微米），
讲义给的图例就是<b>聚 L-乳酸的球晶</b>偏光显微照片。</p>""",
 kp="晶胞（2–20 Å）→ 片晶（100–500 Å 厚）→ 球晶（数十至数百 μm）",
 src="p.41「Structure of Polymer Crystal – Three Levels」"),

dict(kind="理解", topic="c 轴的约定", ans=1,
 stem="By convention, which crystallographic axis corresponds to the polymer backbone (fiber axis)?",
 opts=["The a-axis", "<b>The c-axis, except for monoclinic crystals where it is b</b>",
       "The b-axis always", "It varies randomly"],
 exp="""<p>讲义：<i>“By convention, <b>c-axis corresponds to the polymer backbone</b> (also termed
<b>fiber axis</b>) <b>except for monoclinic crystals where it is b</b>.”</i></p>
<p><b>为什么需要这个约定</b>：高分子晶体高度<b>各向异性</b>——沿主链方向是<b>共价键</b>（很强），
垂直方向是<b>次级作用力</b>（很弱）。指明哪个轴是链方向，才能理解力学和热学的各向异性。</p>
<p class="trap"><b>单斜晶系是例外</b>，这个细节讲义特意点出，容易成为考点。</p>
<p><b>链的堆砌顺序</b>（讲义）：<i>“Chain first adopts <b>lowest energy conformation</b>
(<b>trans</b> for polyethylene), then packs as closely as possible to neighbouring chains.”</i>
——先定构象，再谈堆砌。</p>""",
 kp="c 轴 = 主链方向（单斜例外为 b）；链先取最低能量构象（PE 是全反式）再堆砌",
 src="p.42–43「Polymer Unit Cells」"),

dict(kind="计算", topic="Bragg 定律", ans=1,
 stem="XRD of polyethylene with Cu Kα (λ = 1.54 Å) shows a first-order (n = 1) reflection at <b>2θ = 21.5°</b>. What is the interplanar spacing D?",
 opts=["2.06 Å", "<b>4.13 Å</b>", "8.26 Å", "0.41 Å"],
 exp="""<div class="fb">2 D sin θ = n λ　⇒　D = nλ / (2 sin θ)</div>
<p><b>① 先把 2θ 除以 2</b>：θ = 21.5°/2 = <b>10.75°</b>，sin(10.75°) = 0.1865</p>
<p><b>②</b> D = 1.54 / (2 × 0.1865) = 1.54 / 0.373 = <b>4.13 Å</b></p>
<p class="trap">⚠️ <b>最容易错的一步</b>：题目给的是 <b>2θ（衍射角）</b>，公式里用的是 <b>θ</b>。
直接代 21.5° 会得到 2.10 Å（选项 A）。</p>
<p><b>约定的由来</b>：入射光与晶面成 θ，反射光也成 θ，所以反射光相对<b>入射方向</b>偏折了 <b>2θ</b>
——实验上量的就是这个偏折角，故谱图横轴永远是 2θ。</p>
<p><b>λ = 1.54 Å 是 Cu Kα 的波长</b>，讲义给出，考试可能不提供，要记住。</p>""",
 kp="Bragg 2D sinθ = nλ；题目给 2θ 必须先除以 2；Cu Kα λ = 1.54 Å",
 src="p.44「Bragg's Law」"),

dict(kind="计算", topic="Bragg 定律反算", ans=2,
 stem="A polymer crystal has interplanar spacing D = 5.0 Å. Using Cu Kα (λ = 1.54 Å), at what <b>2θ</b> does the first-order reflection appear?",
 opts=["8.9°", "12.6°", "<b>17.7°</b>", "35.4°"],
 exp="""<div class="fb">sin θ = nλ/(2D) = 1.54 / (2 × 5.0) = 0.154</div>
<p>θ = arcsin(0.154) = <b>8.86°</b></p>
<p><b>但题目问的是 2θ</b>：2θ = 2 × 8.86 = <b>17.7°</b></p>
<p class="trap"><b>选项 A（8.9°）就是忘了乘 2 的陷阱</b>——那是 θ 不是 2θ。
<b>正算要除以 2，反算要乘以 2</b>，方向别弄反。</p>
<p><b>规律</b>：D 越大 → sinθ 越小 → 2θ 越小。<b>大晶面间距对应小角度衍射</b>，
这就是研究大周期结构要用<b>小角散射（SAXS）</b>的原因。</p>""",
 kp="反算 Bragg 要记得最后乘 2 得到 2θ；D 越大衍射角越小",
 src="p.44「Bragg's Law」"),

dict(kind="理解", topic="单晶与粉末衍射", ans=2,
 stem="A <b>powder</b> XRD pattern appears as concentric rings because:",
 opts=["The X-ray beam is circular", "The detector is round",
       "<b>Tiny crystals in all orientations are present, so every allowed reflection appears at its 2θ in all azimuthal directions</b>",
       "The sample is amorphous"],
 exp="""<p>讲义：<i>“<b>Powder</b>: Tiny crystals in <b>all orientations</b> present in a powder sample –
diffraction pattern appears like <b>concentric rings</b>.”</i></p>
<p>对比 <b>单晶</b>：<i>“Diffraction pattern depends on <b>crystal orientation</b> and measurements at
different orientations reveal <b>unique crystal structure and space group</b>.”</i></p>
<table class="mini"><thead><tr><th></th><th>单晶</th><th>粉末</th></tr></thead><tbody>
<tr><td>花样</td><td>离散<b>斑点</b></td><td><b>同心圆环</b></td></tr>
<tr><td>信息量</td><td>高（可定空间群）</td><td>较低（只有 d 值）</td></tr>
<tr><td>制样</td><td>难（要长单晶）</td><td><b>容易</b></td></tr>
</tbody></table>
<p class="trap"><b>高分子几乎只能做粉末衍射</b>——讲义明说 <i>“Powder polymer samples easier to obtain”</i>。
高分子极难长出足够大的单晶。</p>""",
 kp="粉末各取向都有 → 同心圆环；高分子基本只能做粉末衍射",
 src="p.45「XRD Diffraction Patterns」"),

dict(kind="理解", topic="高分子衍射峰的归属", ans=1,
 stem="In a polymer powder XRD pattern, each peak could be attributed to:",
 opts=["Only one specific crystal plane",
       "<b>Either a different crystal plane or a higher order diffraction (n &gt; 1)</b>",
       "The amorphous halo only", "Instrumental noise"],
 exp="""<p>讲义：<i>“Each peak could be attributed to <b>either a different crystal plane or a higher order
diffraction (n &gt; 1)</b>.”</i></p>
<p><b>为什么会有歧义</b>：Bragg 定律 2D sinθ = nλ 中，<b>n = 2 时的 D</b> 与
<b>n = 1 时的 D/2</b> 给出<b>相同</b>的衍射角——单凭一个峰无法区分是"某晶面的二级衍射"
还是"另一个间距减半的晶面的一级衍射"。</p>
<p><b>怎么解决</b>：需要测<b>多个峰</b>并结合已知的晶胞参数做<b>指标化（indexing）</b>。</p>
<p class="trap"><b>2θ 的读取</b>：讲义说明 <i>“Diffraction angle 2θ can be obtained from
<b>distance of ring from centre</b>”</i>——从圆环到中心的距离换算。</p>""",
 kp="每个峰可能是不同晶面或高级衍射（n>1）；需多峰指标化才能确定",
 src="p.46「Polymer X-Ray Diffraction Patterns」"),

dict(kind="计算", topic="Tm 对片晶尺寸的依赖", ans=2,
 stem="From T<sub>m</sub>/T<sub>m</sub><sup>∞</sup> = 1 − (2γ/ΔH<sub>V</sub><sup>b</sup>)(1/l + 1/r), decreasing the lamellar thickness l will:",
 opts=["Raise T<sub>m</sub>", "Leave T<sub>m</sub> unchanged", "<b>Lower T<sub>m</sub></b>", "Make T<sub>m</sub> infinite"],
 exp="""<p>l 减小 → 1/l 增大 → 括号内增大 → 减去的量增大 → <b>T<sub>m</sub>/T<sub>m</sub><sup>∞</sup> 减小</b>
→ <b>T<sub>m</sub> 降低</b>。</p>
<p><b>物理原因</b>：熔融过程包含两部分——<b>熔化本体晶体</b>（ΔG<sub>b</sub>，与体积成正比）
和<b>消除表面能</b>（ΔG<sub>s</sub>，与表面积成正比）。晶体越小，<b>表面积/体积比越大</b>，
表面能占的比重越大，熔化就越容易。</p>
<p class="trap"><b>推导中的关键代换</b>：对无限大晶体（无表面能）ΔG<sub>V</sub><sup>∞</sup> = 0，
由此得 ΔS<sub>V</sub><sup>b</sup> = ΔH<sub>V</sub><sup>b</sup>/T<sub>m</sub><sup>∞</sup>，
代回后消掉了熵项——这是能得到简洁结果的诀窍。</p>""",
 kp="片晶越薄越小 → 表面能占比越大 → T_m 越低",
 src="p.47–49「Dependence of Tm on Crystal (Lamellar) Size」"),

dict(kind="理解", topic="Tm 对分子量的依赖", ans=1,
 stem="Chain ends lower the melting point of a polymer because they:",
 opts=["Increase the crystal size", "<b>Act like impurities, causing freezing (melting) point depression</b>",
       "Increase the enthalpy of fusion", "Crosslink the chains"],
 exp="""<p>讲义：<i>“<b>Chain ends act like impurities</b> and causes <b>freezing (melting) point depression</b>.”</i></p>
<p><b>推导思路</b>（与 Lecture 2 的 Raoult 定律同源）：<br>
· 不纯液体化学势 μ<sub>A,l</sub> = μ*<sub>A,l</sub> + RT ln x<sub>A</sub><br>
· 链端摩尔分数 <b>x<sub>B</sub> = 2M₀/M<sub>n</sub></b>（每条链<b>两个</b>链端，M₀ 是重复单元分子量）<br>
· 用 ln x<sub>A</sub> ≈ −x<sub>B</sub> 得</p>
<div class="fb">2M₀/M<sub>n</sub> = (ΔH<sub>m</sub>/nR)(1/T<sub>m</sub> − 1/T<sub>m</sub><sup>∞</sup>)</div>
<p><b>M<sub>n</sub> 越低 → 链端分数越高 → T<sub>m</sub> 越低。</b></p>
<p class="trap"><b>注意 x<sub>B</sub> 里的因子 2</b>——每条链有两个端。
另外这里用的是 <b>M<sub>n</sub></b>（数均），因为链端数正比于链的条数。</p>""",
 kp="链端 = 杂质 → 熔点降低；x_B = 2M₀/M_n（每链两端），用 Mn",
 src="p.50–51「Dependence of Tm on Molecular Weight」"),

dict(kind="理解", topic="结晶机理", ans=2,
 stem="Polymers crystallize by which mechanism?",
 opts=["Spinodal decomposition", "Instantaneous ordering throughout the melt",
       "<b>Nucleation and growth</b> — stable nuclei appear first, then grow by incorporating chains from the amorphous phase",
       "Evaporation and condensation"],
 exp="""<p>讲义：<i>“Polymers crystallize by a <b>nucleation and growth</b> mechanism.
<b>Stable nuclei</b> first appears, followed by <b>growth of the nuclei</b> through incorporation of
<b>more chains from amorphous phase</b>.”</i></p>
<p class="trap"><b>与 Lecture 4 的相分离机理呼应</b>：<br>
· 相分离有<b>两种</b>机理：spinodal decomposition（无势垒）和 nucleation and growth（有势垒）<br>
· <b>结晶只有一种</b>：nucleation and growth</p>
<p><b>为什么结晶必须成核</b>：形成一个小晶核会<b>增加表面能</b>（不利），
只有当晶核长到足够大、体积项（有利）压过表面项时才能稳定存在——
这正是<b>活化势垒</b>的来源，与 Lecture 4 的成核完全同理。</p>""",
 kp="结晶只走成核-生长机理；表面能造成成核势垒，与 L4 的 N&G 同理",
 src="p.52「Mechanism of Crystallization」"),

dict(kind="理解", topic="片晶厚度的双重决定", ans=3,
 stem="Lamellar thickness is determined by both thermodynamics and kinetics. At <b>low</b> temperature:",
 opts=["Thick lamellae dominate because they are more stable",
       "Thick lamellae dominate because they grow faster",
       "Thin lamellae are thermodynamically forbidden",
       "<b>Thin lamellae dominate — they are thermodynamically allowed at low T and also grow more rapidly</b>"],
 exp="""<p>讲义的两条并列理由：<br>
· <b>热力学上</b>：<i>“thinner lamellar has <b>lower T<sub>m</sub></b>, hence <b>lower temp allows growth of
thinner crystals</b>”</i>——薄片晶熔点低，只有低温才不会立刻熔掉<br>
· <b>动力学上</b>：<i>“thinner lamellar generally <b>grow more rapidly</b>, hence <b>thinner crystals
dominate at low temp</b>”</i>——薄片晶长得快</p>
<p><b>两条理由指向同一个结论</b>：<b>低温 → 薄片晶</b>。</p>
<p class="trap"><b>讲义还指出一个有趣现象</b>：<i>“<b>Abrupt transitions</b> happen when thinner lamellar
becomes thermodynamically allowed”</i>——生长速率随温度变化时会出现<b>突变</b>，
因为每当温度降到某个值、更薄的片晶变得热力学允许时，生长模式就跳一档。
讲义给的实例是<b>聚环氧乙烷（PEO）</b>。</p>""",
 kp="低温 → 薄片晶（热力学允许 + 动力学更快）；生长速率随温度出现突变",
 src="p.52「Mechanism of Crystallization」"),

dict(kind="理解", topic="球晶", ans=1,
 stem="Spherulites are formed by:",
 opts=["Crystallization during flow", "<b>Nucleation and growth</b> (the normal mechanism)",
       "Deep undercooling causing disorganised growth", "Lamellae splaying out from a centre"],
 exp="""<p>讲义的形貌图注：<i>“<b>Spherulites</b> of poly(L-lactide) (<b>by nucleation and growth</b>)”</i>
——球晶是常规成核-生长的产物。</p>
<p><b>四种形貌的完整对照（讲义 p.53）</b>：</p>
<table class="mini"><thead><tr><th>形貌</th><th>形成条件</th></tr></thead><tbody>
<tr><td><b>Spherulite 球晶</b></td><td>常规<b>成核-生长</b></td></tr>
<tr><td><b>Hedrite</b></td><td>片晶从中心<b>张开（splay out）</b>时</td></tr>
<tr><td><b>Dendrite 枝晶</b></td><td><b>更深过冷</b>下的无序生长</td></tr>
<tr><td><b>Shish kebab 串晶</b></td><td><b>在流动条件下</b>结晶</td></tr>
</tbody></table>""",
 kp="球晶 = 常规成核生长；hedrite、枝晶、串晶各有特定形成条件",
 src="p.53「Morphology of Crystalline Polymers」"),

dict(kind="理解", topic="串晶 shish kebab", ans=3,
 stem="The 'shish kebab' morphology of polyethylene forms when the polymer is crystallized:",
 opts=["At very high pressure", "From dilute solution", "Under deep undercooling",
       "<b>During flow</b>"],
 exp="""<p>讲义图注：<i>“<b>Shish kebab</b> of polyethylene (<b>when crystallized during flow</b>)”</i>。</p>
<p><b>结构</b>：流动使部分链沿流动方向<b>伸展并结晶</b>成中心的"<b>串（shish）</b>"，
其他链再垂直于它生长出片晶"<b>肉块（kebab）</b>"，形似烤肉串。</p>
<p class="trap"><b>工业意义极大</b>：<b>所有的加工工艺都涉及流动</b>
（挤出、注塑、纺丝——Lecture 9）。所以实际制品中的结晶形貌<b>不是</b>教科书里
静置生长的球晶，而往往是流动诱导的取向结构。</p>
<p><b>这也解释了纤维为什么强</b>：纺丝时的拉伸使链高度取向并形成串晶结构，
沿纤维轴方向全是<b>共价键</b>承力。</p>""",
 kp="串晶在流动下结晶形成；实际加工制品的结晶形貌多是流动诱导的",
 src="p.53「Shish kebab of polyethylene」"),

dict(kind="理解", topic="枝晶", ans=2,
 stem="Dendrites of polyethylene form under:",
 opts=["Slow cooling near T<sub>m</sub>", "Flow conditions",
       "<b>Deeper undercooling</b>, giving disorganised growth", "High pressure"],
 exp="""<p>讲义图注：<i>“<b>Dendrite</b> of polyethylene (<b>disorganised growth by deeper undercooling</b>)”</i>。</p>
<p><b>为什么过冷度大会长成枝晶</b>：过冷度大 → 结晶<b>驱动力</b>很强 → 生长极快 →
但链<b>来不及</b>有序排列到晶体表面 → 生长在<b>尖端优先</b>（尖端更容易接触到新的链），
形成分叉的树枝状结构。</p>
<p class="trap"><b>与"低温 → 薄片晶"是同一件事的两个侧面</b>：
过冷度越大，热力学驱动越强但动力学越受限，结构就越不完善——
<b>薄、快、乱</b>。</p>""",
 kp="深过冷 → 生长快但来不及有序 → 枝晶；与「低温薄片晶」同源",
 src="p.53「Dendrite of polyethylene」"),

dict(kind="计算", topic="链端摩尔分数", ans=1,
 stem="A polymer has repeat unit M₀ = 100 g/mol and M<sub>n</sub> = 10,000 g/mol. What is the mole fraction of chain ends x<sub>B</sub>?",
 opts=["0.010", "<b>0.020</b>", "0.050", "0.100"],
 exp="""<div class="fb">x<sub>B</sub> = 2M₀ / M<sub>n</sub> = 2 × 100 / 10,000 = <b>0.020</b></div>
<p class="trap"><b>关键是因子 2</b>——<b>每条链有两个链端</b>。忘掉它会得到 0.010（选项 A）。</p>
<p><b>物理意义</b>：这条链平均有 100 个重复单元，其中"端"占了 2 个，
即 <b>2%</b> 的单元是链端。这 2% 就相当于 2% 的杂质，造成熔点降低。</p>
<p><b>量级感</b>：M<sub>n</sub> 越大 x<sub>B</sub> 越小。若 M<sub>n</sub> = 10⁶，
x<sub>B</sub> = 0.0002，链端效应基本可忽略——这就是<b>高分子量高分子的 T<sub>m</sub> 接近 T<sub>m</sub><sup>∞</sup></b> 的原因。</p>""",
 kp="x_B = 2M₀/M_n，因子 2 来自每链两端；高分子量时链端效应可忽略",
 src="p.51「x_B = 2M₀/M_n」"),

dict(kind="理解", topic="Tm 与 Tg 的影响因素对比", ans=2,
 stem="Increasing M<sub>n</sub> affects T<sub>g</sub> and T<sub>m</sub> how?",
 opts=["Raises T<sub>g</sub>, lowers T<sub>m</sub>", "Lowers both",
       "<b>Raises both</b> — both effects trace back to chain ends", "Lowers T<sub>g</sub>, raises T<sub>m</sub>"],
 exp="""<p><b>两者都升高，而且原因同源——都是链端在作怪</b>：</p>
<table class="mini"><thead><tr><th></th><th>关系式</th><th>链端的作用</th></tr></thead><tbody>
<tr><td><b>T<sub>g</sub></b>（L8）</td><td>T<sub>g</sub> = T<sub>g</sub>(∞) − K/M<sub>n</sub></td><td>链端<b>自由体积大</b> → 易运动 → T<sub>g</sub> 低</td></tr>
<tr><td><b>T<sub>m</sub></b>（L10）</td><td>2M₀/M<sub>n</sub> = (ΔH<sub>m</sub>/nR)(1/T<sub>m</sub> − 1/T<sub>m</sub><sup>∞</sup>)</td><td>链端<b>相当于杂质</b> → 熔点降低</td></tr>
</tbody></table>
<p><b>两者都是 1/M<sub>n</sub> 的形式</b>，都在高分子量时趋于平台值。</p>
<p class="trap"><b>这是很好的跨讲综合题素材</b>：同一个"链端"概念，
在 L8 用<b>自由体积</b>解释 T<sub>g</sub>，在 L10 用<b>依数性</b>解释 T<sub>m</sub>。</p>""",
 kp="M_n 升高使 T_g 和 T_m 都升高；都源于链端，都是 1/M_n 形式",
 src="p.13（L8）与 p.50–51（L10）"),

dict(kind="理解", topic="弹性体与结晶的互斥", ans=1,
 stem="Why must an elastomer have negligible crystalline content?",
 opts=["Crystals would make it transparent",
       "<b>Rigid crystalline regions would restrict the conformational freedom needed for entropic elasticity</b>",
       "Crystals would lower T<sub>g</sub>", "Crystals would prevent crosslinking"],
 exp="""<p>橡胶弹性的本质是<b>熵弹性</b>——靠链<b>舒展与回缩构象</b>产生回复力，
这要求链段有<b>充分的构象自由度</b>。</p>
<p><b>晶区是刚性的、有序的、链被锁定的</b>——它既不能舒展也不能回缩，
只会像刚性填料一样<b>提高模量、降低伸长率</b>，破坏弹性体的特征行为。</p>
<p class="trap"><b>回到弹性体的三个条件看</b>，它们其实是<b>同一个要求的三个方面</b>：<br>
· 高于 T<sub>g</sub> → 链段<b>能动</b><br>
· 无结晶 → 链段<b>没被锁住</b><br>
· 交联 → 链<b>不会跑掉</b>（形变可恢复）<br>
前两条保证"能变形"，第三条保证"能回来"。</p>""",
 kp="晶区锁住构象自由度，与熵弹性冲突；三个条件是「能变形 + 能回来」",
 src="p.34「Characteristics of Elastomers」；p.38「Entropic Nature of Stress」"),

dict(kind="理解", topic="全课综合：为什么 PE 不透明而 PS 透明", ans=2,
 stem="Polystyrene (atactic) is transparent while high-density polyethylene is opaque. The two key reasons are:",
 opts=["PS absorbs light; PE reflects it",
       "PS has higher molecular weight",
       "<b>Atactic PS cannot crystallize (uniform refractive index → no scattering); HDPE is semi-crystalline (crystallite/amorphous refractive index difference → scattering)</b>",
       "PE has a higher T<sub>g</sub>"],
 exp="""<p><b>这道题串起三讲</b>：</p>
<p><b>① 立构规整性（L10 p.40）</b>：商业聚苯乙烯是 <b>atactic 无规</b> → <b>不能结晶</b> →
全部是无定形玻璃态。而 PE 结构规整（无侧基）→ <b>易结晶</b> → 半结晶。</p>
<p><b>② 光学性质（L8 p.4）</b>：<br>
· 玻璃态 PS：链无规堆砌但<b>折射率处处均一</b> → <b>无散射 → 透明</b><br>
· 半结晶 PE：<b>晶区与非晶区折射率不同</b> → <b>散射 → 不透明</b></p>
<p><b>③ 散射的根源（L6）</b>：折射率不均匀才产生散射。</p>
<p class="trap"><b>推论</b>：如果把 HDPE 的晶粒做得<b>远小于可见光波长</b>，
它就会变透明——这正是<b>茂金属催化的低结晶度 PE 薄膜</b>比较透明的原因。
<b>不是"有没有晶"，而是"晶粒有多大"。</b></p>""",
 kp="无规立构 PS 不结晶故透明；半结晶 PE 因折射率不均而散射。串联 L6/L8/L10",
 src="p.40（L10）、p.4（L8）、p.21（L6）综合"),
]

L.append(dict(kind="理解", topic="全课综合：三个「半径」与三种「平均」", ans=1,
 stem="A single polymer sample is characterised by osmometry, static light scattering, DLS and viscometry. Which set of quantities is obtained?",
 opts=["M<sub>w</sub> from osmometry, M<sub>n</sub> from light scattering, R<sub>g</sub> from DLS",
       "<b>M<sub>n</sub> from osmometry; M<sub>w</sub> and R<sub>g</sub> from static light scattering; R<sub>h</sub> from DLS; M<sub>v</sub> ≈ M<sub>w</sub> from viscometry</b>",
       "All four give M<sub>n</sub>", "Only viscometry gives a molecular weight"],
 exp="""<p><b>全课表征方法的总对照表——这是最容易出综合题的一页</b>：</p>
<table class="mini"><thead><tr><th>方法</th><th>给出</th><th>原理</th></tr></thead><tbody>
<tr><td>膜渗透压 / VPO / 端基分析</td><td><b>M<sub>n</sub></b></td><td>依数性，<b>数个数</b></td></tr>
<tr><td><b>静态</b>光散射（多角度）</td><td><b>M<sub>w</sub> + R<sub>g</sub></b></td><td>按<b>质量</b>加权；角度依赖给尺寸</td></tr>
<tr><td><b>动态</b>光散射 DLS</td><td><b>R<sub>h</sub></b>（<b>不给分子量</b>）</td><td>涨落快慢 → 扩散系数 → Stokes-Einstein</td></tr>
<tr><td>粘度法</td><td><b>M<sub>v</sub> ≈ M<sub>w</sub></b></td><td>[η] = kM<sup>a</sup>，需标定</td></tr>
<tr><td>SEC / GPC</td><td>整个分布 → M<sub>n</sub>、M<sub>w</sub>、PDI</td><td>尺寸排阻，需校准</td></tr>
<tr><td>MALDI-TOF-MS</td><td>整个分布 → M<sub>n</sub>、M<sub>w</sub></td><td>t ∝ √m；仅限极性高分子</td></tr>
</tbody></table>
<p><b>三个「半径」也要分清</b>：<br>
· <b>R<sub>g</sub></b> 回转半径 ← 静态光散射（L1 定义、L6 测量）<br>
· <b>R<sub>h</sub></b> 流体力学半径 ← DLS（L5 的 Stokes 定律 + L6）<br>
· <b>R₀</b> 密堆积球半径 ← 概念比较，恒有 R<sub>g</sub> &lt; R₀（L1）</p>
<p class="trap"><b>两个最高频的错误</b>：以为 DLS 能给分子量（<b>不能</b>）；
把 R<sub>g</sub> 和 R<sub>h</sub> 当成同一个量（<b>不是</b>）。</p>""",
 kp="方法-平均值-半径的总对照；DLS 只给 Rh 不给分子量，Rg ≠ Rh",
 src="p.7（L5）、p.26、p.31（L6）、p.34–40（L7）、p.13、p.17（L1）综合"))
