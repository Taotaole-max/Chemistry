# -*- coding: utf-8 -*-
LEC = 9
TITLE = "Mechanical Properties & Processing of Polymers"
CN = "力学性质与加工"
SRC = "讲义 Lectures_8-10"
L = [
dict(kind="计算", topic="拉伸应力与应变的定义", ans=1,
 stem="Tensile stress σ<sub>t</sub> and strain ε are defined as:",
 opts=["σ<sub>t</sub> = f·A and ε = ΔL·L₀", "<b>σ<sub>t</sub> = f/A and ε = ΔL/L₀</b>",
       "σ<sub>t</sub> = A/f and ε = L₀/ΔL", "σ<sub>t</sub> = f/L₀ and ε = ΔL/A"],
 exp="""<div class="fb">σ<sub>t</sub> = f / A　　ε = ΔL / L₀</div>
<p>f 是沿形变轴的力，A 是受力面积；ΔL 是长度变化，L₀ 是<b>原始</b>长度。</p>
<p><b>单位</b>：σ 是 Pa（N/m²），<b>ε 无量纲</b>（常写成百分比）。</p>
<p class="trap"><b>与剪切应力的区别</b>（Lecture 5）：拉伸应力 f <b>垂直</b>于受力面，
剪切应力 f <b>平行</b>于受力面。两者量纲相同但物理意义不同。</p>""",
 kp="σ = f/A（垂直）、ε = ΔL/L₀（无量纲）；区别于剪切应力（平行）",
 src="p.17「Tensile Stress / Strain」"),

dict(kind="理解", topic="杨氏模量", ans=0,
 stem="In σ<sub>t</sub> = Eε, the constant E is called the modulus. It corresponds to:",
 opts=["The <b>slope</b> of the stress–strain curve in the initial linear region",
       "The area under the stress-strain curve", "The stress at fracture", "The maximum strain"],
 exp="""<div class="fb">σ<sub>t</sub> = E ε　⇒　E = σ/ε = 曲线斜率</div>
<p>讲义：<i>“The proportionality constant between stress and strain is called the <b>Modulus</b> or
<b>Young's Modulus (E)</b>. This linear correlation is usually true for <b>small strains</b>.”</i></p>
<p class="trap"><b>"小应变"是前提</b>——超过线性区后曲线弯曲，斜率不再是 E。
所以 E 必须取<b>初始</b>斜率。</p>
<p><b>其他两个量别混</b>：<b>曲线下面积</b>是断裂功（韧性），<b>断裂点应力</b>是抗拉强度。</p>""",
 kp="E = 应力-应变曲线的初始斜率；只在小应变线性区成立",
 src="p.17「Modulus or Young's Modulus (E)」"),

dict(kind="计算", topic="模量计算", ans=2,
 stem="A polymer bar of cross-section 2.0 mm² and original length 50 mm elongates 1.0 mm under a 100 N load in the linear region. E = ?",
 opts=["0.5 GPa", "1.0 GPa", "<b>2.5 GPa</b>", "5.0 GPa"],
 exp="""<p><b>应力</b>：σ = 100 N / (2.0×10⁻⁶ m²) = 5.0×10⁷ Pa = <b>50 MPa</b></p>
<p><b>应变</b>：ε = 1.0/50 = <b>0.020</b></p>
<p><b>模量</b>：E = 50 MPa / 0.020 = 2500 MPa = <b>2.5 GPa</b></p>
<p class="trap"><b>单位换算是最大失分点</b>：<b>1 mm² = 10⁻⁶ m²</b>（不是 10⁻³）。
应变本身无量纲，mm/mm 直接约掉，不需要换算。</p>
<p><b>量级感</b>：玻璃态高分子 E ≈ 1–3 GPa，弹性体 E ≈ 1 MPa（低三个数量级），
金属 E ≈ 70–200 GPa。<b>2.5 GPa 正是典型的玻璃态高分子。</b></p>""",
 kp="E = σ/ε；1 mm² = 10⁻⁶ m²；玻璃态高分子 E 约 1–3 GPa",
 src="p.17「σ_t = Eε」"),

dict(kind="计算", topic="泊松比", ans=1,
 stem="Poisson's ratio ν is defined by −Δd/d = −Δh/h = ν·ΔL/L₀. A bar with d = 10 mm and ν = 0.40 is stretched by 5%. What is Δd?",
 opts=["−0.10 mm", "<b>−0.20 mm</b>", "−0.40 mm", "−0.50 mm"],
 exp="""<div class="fb">−Δd/d = ν · (ΔL/L₀)　⇒　Δd = −ν · d · (ΔL/L₀)</div>
<p>Δd = −0.40 × 10 mm × 0.05 = <b>−0.20 mm</b>（负号表示横向<b>收缩</b>）</p>
<p><b>物理含义</b>：拉伸时材料在<b>两个横向</b>都收缩，收缩量正比于伸长量，
比例常数就是泊松比 ν。</p>
<p class="trap"><b>ν 的取值范围</b>：理论上 0 &lt; ν &lt; 0.5。
<b>ν = 0.5 意味着体积不变</b>——橡胶接近这个值（拉伸时几乎不改变体积）；
玻璃态高分子约 0.3–0.4（拉伸时体积略增）。</p>""",
 kp="Δd = −ν·d·(ΔL/L₀)；ν→0.5 表示体积不变（橡胶），玻璃态约 0.3–0.4",
 src="p.18「Poisson's Ratio (ν)」"),

dict(kind="理解", topic="抗拉强度与屈服强度", ans=2,
 stem="Which pair of definitions is correct?",
 opts=["Tensile strength = stress at yield point; Yield strength = stress at fracture",
       "Both refer to the stress at fracture",
       "<b>Tensile strength = maximum stress at the point of fracture; Yield strength = stress at the onset of non-recoverable deformation</b>",
       "Tensile strength = the slope; Yield strength = the area"],
 exp="""<p>讲义定义：<br>
· <b>Tensile strength</b> is the <b>max stress at point of fracture</b>（断裂点的最大应力）<br>
· <b>Yield strength</b> is stress at <b>onset of non-recoverable deformation</b>（开始出现不可恢复形变时的应力）</p>
<p class="trap"><b>屈服 = 弹性与塑性的分界</b>。屈服点<b>之前</b>卸载能完全回弹；
屈服点<b>之后</b>会留下永久形变。</p>
<p><b>不是所有材料都有屈服点</b>：<b>脆性</b>高分子（PS、PMMA）线性升到断裂，<b>无屈服点</b>；
<b>弹性体</b>形变完全可恢复，也<b>无屈服点</b>。只有<b>韧性</b>高分子（PP、PE）有明显屈服。</p>""",
 kp="抗拉强度 = 断裂应力；屈服强度 = 不可恢复形变的起点。脆性与弹性体无屈服点",
 src="p.17「Tensile strength / Yield strength」"),

dict(kind="理解", topic="脆性行为（曲线 A）", ans=0,
 stem="Curve A in the stress–strain analysis (high modulus, approximately linear right up to fracture, no yield point) describes which polymers?",
 opts=["<b>Brittle — e.g. polystyrene, PMMA</b>", "Ductile — e.g. polypropylene, polyethylene",
       "Elastomeric — e.g. cis-1,4-polyisoprene", "Semi-crystalline only"],
 exp="""<p>讲义：<i>“<b>A: Brittle</b> – Modulus (E), given by the slope, is <b>high</b> and approx.
<b>linear up to point of fracture</b> (e.g. <b>Polystyrene, PMMA</b>).”</i></p>
<p><b>脆性的特征</b>：模量高、应变小、无屈服、断裂突然。断裂前几乎不吸收能量
（曲线下面积小 = 韧性差）。</p>
<p class="trap"><b>PS 和 PMMA 都是 T<sub>g</sub> 约 100 °C 的玻璃态高分子</b>——
室温远低于 T<sub>g</sub>，链段被冻结，所以表现脆性。<b>升温到接近 T<sub>g</sub> 就会转为韧性</b>
（脆-韧转变，见下题）。</p>""",
 kp="脆性（A）：E 高、线性至断裂、无屈服；PS、PMMA，因室温远低于 T_g",
 src="p.19「Stress-Strain Analysis」"),

dict(kind="理解", topic="韧性行为（曲线 B）", ans=1,
 stem="Curve B (ductile) shows, in order:",
 opts=["Linear rise then immediate fracture",
       "<b>Rise to yield point → plastic deformation with strain softening → large deformation → modulus rises again before fracture (strain hardening)</b>",
       "Very low modulus with no yield point", "Constant stress throughout"],
 exp="""<p>讲义：<i>“<b>B: Ductile</b> – Stress rises to the max at <b>yield point</b>, where the material begins
to undergo <b>plastic deformation (non-recoverable)</b>. <b>Strain softening</b> occurs and material
deforms to a large extent. Modulus (E) <b>increases again</b> before fracture (<b>strain hardening</b>).
(e.g. <b>polypropylene, polyethylene</b>)”</i></p>
<p><b>四个阶段</b>：弹性 → <b>屈服</b> → 应变软化（应力下降但继续大幅形变，对应<b>细颈扩展</b>）
→ <b>应变硬化</b>（链沿拉伸方向取向，模量回升）→ 断裂。</p>
<p class="trap"><b>应变软化对应"成颈"，应变硬化对应"颈部扩展完毕后链取向"</b>——
把力学曲线与微观机理对应起来是本讲的关键。</p>""",
 kp="韧性（B）：屈服 → 应变软化（成颈）→ 应变硬化（链取向）→ 断裂；PP、PE",
 src="p.19「B: Ductile」"),

dict(kind="理解", topic="弹性体行为（曲线 C）", ans=2,
 stem="Curve C (elastomeric) is characterised by:",
 opts=["Very high modulus and small strain at fracture",
       "A sharp yield point followed by necking",
       "<b>Very low modulus, no yield point (recoverable deformation), strain at fracture typically 500–1000%</b>",
       "Linear behaviour up to 10% strain then fracture"],
 exp="""<p>讲义：<i>“<b>C: Elastomeric</b> – Modulus (E) is <b>very low</b>; there is <b>no yield point</b>
(<b>recoverable</b> deformation); the strain at fracture is <b>high (generally 500%–1000%)</b>
(e.g. <b>cis-1,4-polyisoprene – rubber</b>).”</i></p>
<p><b>三个数量级的对比</b>：脆性/韧性高分子断裂应变通常 &lt; 10%，弹性体是 <b>500–1000%</b>
（即拉长 6–11 倍）。</p>
<p class="trap"><b>"无屈服点"的原因</b>：弹性体的形变是<b>构象的舒展</b>（熵弹性，Lecture 10），
不涉及链的永久滑移，所以完全可恢复，不存在"塑性起点"。</p>""",
 kp="弹性体（C）：E 极低、无屈服、断裂应变 500–1000%、完全可恢复",
 src="p.19「C: Elastomeric」"),

dict(kind="理解", topic="脆-韧转变", ans=1,
 stem="Raising the temperature of a polymer causes a brittle-to-ductile transition because:",
 opts=["The polymer melts", "<b>Ductility requires substantial molecular mobility and rearrangement, which is favoured at higher temperature</b>",
       "The modulus increases", "Crosslinks break"],
 exp="""<p>讲义：<i>“<b>Brittle-to-ductile transition</b> occurs when the polymer temperature is raised.
Ductility requires <b>substantial molecular mobility and rearrangement</b>, which is favoured at
higher temperatures.”</i></p>
<p><b>韧性 = 能够大幅塑性形变</b>，而塑性形变需要链段能够重排（成颈、取向）。
温度越高，链段活动性越强 → 越容易发生这些重排。</p>
<p><b>讲义给的例证</b>：<i>“Stress–strain response for <b>PMMA</b> at various temperatures”</i>——
同一材料在不同温度下从脆性变为韧性。</p>""",
 kp="升温 → 链段活动性增强 → 脆-韧转变；同一材料可表现两种行为",
 src="p.20「Variation of Stress-Strain Behaviour with Temperature」"),

dict(kind="理解", topic="形变速率的影响", ans=2,
 stem="Faster deformation rate causes a polymer to behave:",
 opts=["More ductile", "Unchanged", "<b>More brittle</b>, because there is less time for molecular rearrangement",
       "Like a liquid"],
 exp="""<p>讲义：<i>“Brittle-to-ductile transition <b>depends on rate of deformation</b>.
<b>Faster deformation causes more brittle behaviour</b> in polymer – <b>less time for molecular
rearrangement</b>.”</i></p>
<p class="trap"><b>时间与温度是等效的</b>：<br>
· <b>升温</b> = 给分子更强的活动能力<br>
· <b>放慢速率</b> = 给分子更多的活动时间<br>
两者效果相同——这就是高分子力学中的<b>时温等效原理</b>。</p>
<p><b>工程含义</b>：同一个塑料件，慢慢弯可以弯很大，<b>猛地一敲就碎</b>。
所以抗冲击性能必须用<b>高速冲击试验</b>测，不能用慢速拉伸推断。</p>""",
 kp="快速形变 → 更脆（来不及重排）；时间与温度等效",
 src="p.20「Faster deformation causes more brittle behaviour」"),

dict(kind="理解", topic="粘弹性：玻璃态区", ans=0,
 stem="In region A-B of the modulus–temperature curve for atactic polystyrene (below T<sub>g</sub>), the deformation is:",
 opts=["<b>Recoverable (elastic)</b>", "Purely viscous flow", "Partially recoverable", "Not measurable"],
 exp="""<p>讲义：<i>“<b>A-B: Glassy state (below T<sub>g</sub>)</b> – deformation <b>recoverable (elastic)</b>”</i>。</p>
<p><b>五个区间的完整对照</b>：</p>
<table class="mini"><thead><tr><th>区间</th><th>状态</th><th>行为</th></tr></thead><tbody>
<tr><td><b>A-B</b></td><td>玻璃态（&lt; T<sub>g</sub>）</td><td>形变<b>可恢复</b>（弹性）</td></tr>
<tr><td>B-C</td><td>推迟弹性态（T<sub>g</sub> 在此区）</td><td>应变<b>缓慢</b>增加、缓慢恢复</td></tr>
<tr><td>C-D</td><td>橡胶态</td><td>模量<b>平台</b>；瞬时弹性 + 粘性流动 + 不完全恢复</td></tr>
<tr><td>D-E</td><td>橡胶流动态</td><td>模量<b>进一步下降</b></td></tr>
<tr><td>E-F</td><td>粘流态</td><td><b>无弹性响应、无恢复</b>，纯粘性流动</td></tr>
</tbody></table>""",
 kp="五个粘弹性区间：玻璃态 → 推迟弹性 → 橡胶平台 → 橡胶流动 → 粘流",
 src="p.21「Viscoelasticity」"),

dict(kind="理解", topic="粘弹性：橡胶平台", ans=1,
 stem="Region C-D (rubbery state) is characterised by:",
 opts=["Modulus continuing to fall steeply", "<b>The modulus flattening into a plateau</b>, with immediate elastic response followed by viscous flow and incomplete recovery",
       "No deformation at all", "Complete and instantaneous recovery"],
 exp="""<p>讲义：<i>“<b>C-D: Rubbery state</b> – <b>Modulus flattens</b>; shows <b>immediate elastic response</b>,
followed by <b>viscous flow</b> and <b>incomplete recovery</b>.”</i></p>
<p><b>橡胶平台的来源</b>：链段已经可以自由运动（&gt; T<sub>g</sub>），但整条链的移动被
<b>缠结</b>限制住了——缠结起到"临时交联"的作用，撑起一个模量平台。</p>
<p class="trap"><b>"不完全恢复"是关键</b>：与真正的交联弹性体不同，
未交联高分子的缠结<b>会随时间滑脱</b>，所以有永久形变。
<b>要得到完全可恢复的弹性，必须化学交联</b>（Lecture 10）。</p>""",
 kp="橡胶平台源于链缠结（临时交联）；未交联者缠结会滑脱，故恢复不完全",
 src="p.21「C-D: Rubbery state」"),

dict(kind="理解", topic="银纹 crazing", ans=1,
 stem="Crazing is best described as:",
 opts=["The alignment of crystalline lamellae",
       "<b>The mechanism of crack propagation, creating micro-voids between stretched fibrils, propagating perpendicular to the stress</b>",
       "Deformation bands at 45° to the stress", "The formation of a neck after yielding"],
 exp="""<p>讲义要点：<br>
· 银纹是高分子中<b>裂纹扩展</b>的机理，导致<b>脆性断裂</b><br>
· 在被拉伸的<b>原纤（fibrils）</b>之间形成<b>微孔洞</b>，原纤直径约 <b>10–20 nm</b><br>
· 银纹<b>沿垂直于应力的方向</b>扩展<br>
· 原纤最终断裂 → 断裂<br>
· 银纹<b>散射光</b>，所以看起来发白/发雾</p>
<p class="trap"><b>反直觉的结论</b>：<i>“<b>Ability for polymer to craze makes them mechanically strong</b> –
energy is dissipated in process of drawing polymer into fibrils.”</i>
<b>能起银纹反而使材料强韧</b>——因为把高分子拉成原纤的过程<b>耗散了大量能量</b>。</p>""",
 kp="银纹：原纤间 10–20 nm 微孔洞、垂直应力扩展、散射光发白；能起银纹反而强韧",
 src="p.22「Crazing」"),

dict(kind="理解", topic="银纹为何发白", ans=2,
 stem="Why do crazes appear white or hazy?",
 opts=["They absorb visible light", "They fluoresce",
       "<b>The micro-voids scatter light</b> because of the large refractive index difference between void and polymer",
       "They crystallize"],
 exp="""<p>讲义直接写着 <i>“<b>Light scattering by craze</b> cause them to look white/hazy”</i>。</p>
<p><b>光学原理</b>：银纹内部是 10–20 nm 的<b>微孔洞</b>（n ≈ 1，空气）与高分子原纤（n ≈ 1.5）
交替排列，<b>折射率差极大</b> → 强烈散射 → 发白。</p>
<p class="trap"><b>这是本课"折射率不均 → 散射"原理的第三次出现</b>：<br>
· <b>L6</b>：dn/dc 越大散射越强<br>
· <b>L8</b>：半结晶高分子晶区/非晶区折射率差 → 发白<br>
· <b>L9</b>：银纹微孔洞 → <b>应力发白（stress whitening）</b></p>
<p><b>日常观察</b>：把塑料尺或塑料袋用力弯折，折痕处发白——那就是银纹。</p>""",
 kp="银纹发白源于微孔洞与高分子的折射率差；与 L6/L8 同一散射原理",
 src="p.22「Light scattering by craze」"),

dict(kind="理解", topic="剪切带 shear banding", ans=1,
 stem="Shear deformation bands develop at approximately what angle to the stress direction?",
 opts=["0°（parallel）", "<b>~45°</b>", "90°（perpendicular）", "Random angles"],
 exp="""<p>讲义：<i>“Shear deformation bands can develop at angles <b>~45°</b> to stress direction.
Once a small region experiences shear displacement, the shear <b>propagates since it is weaker than
surrounding un-deformed regions</b>.”</i></p>
<p><b>为什么是 45°</b>：单轴拉伸时，<b>最大剪应力出现在与拉伸轴成 45° 的平面上</b>
（材料力学的基本结果）。</p>
<p class="trap"><b>与银纹的方向对比（高频考点）</b>：</p>
<table class="mini"><thead><tr><th>机理</th><th>方向</th></tr></thead><tbody>
<tr><td><b>Crazing 银纹</b></td><td><b>垂直</b>于应力（90°）</td></tr>
<tr><td><b>Shear banding 剪切带</b></td><td>与应力成 <b>~45°</b></td></tr>
</tbody></table>
<p>讲义给的图例是<b>聚苯乙烯在垂直压缩下</b>的偏光显微照片。</p>""",
 kp="剪切带与应力成 ~45°（最大剪应力面）；银纹垂直于应力",
 src="p.23「Shear Banding」"),

dict(kind="理解", topic="细颈 necking", ans=0,
 stem="Necking occurs at which point in the stress–strain curve, and how does the neck extend?",
 opts=["<b>Right after the yield point; the neck extends by stretching the un-necked region, which is less strained and requires less stress</b>",
       "Before the yield point; by fracturing the necked region",
       "At fracture; by crystallizing", "Only in elastomers; by crosslinking"],
 exp="""<p>讲义：<i>“Necking occurs <b>right after yield point</b> in ductile polymer.
Neck extends by <b>stretching of un-necked region</b> – un-necked region <b>less strained</b>,
hence <b>requires less stress</b> to stretch. After entire sample is necked, <b>modulus increases</b>
before fracture (<b>strain hardening</b>).”</i></p>
<p><b>为什么颈部不会越拉越细直到断裂</b>：颈部内的链已经<b>高度取向</b>，反而变得更强
（应变硬化）；相比之下未成颈区更"软"，所以后续形变都发生在那里——
<b>颈部向两端"传播"</b>而不是继续变细。</p>
<p class="trap"><b>这正是拉伸取向纤维的工业原理</b>（Lecture 9 的 melt spinning：
"godets 拉伸纤维"），通过成颈使链沿轴向取向，大幅提高纤维强度。</p>""",
 kp="细颈在屈服点后出现；颈部因链取向而变强，故向两端扩展而非继续变细",
 src="p.23「Necking」"),

dict(kind="理解", topic="挤出成型", ans=1,
 stem="In extrusion, what is the function of the <b>breaker plate</b>?",
 opts=["To heat the polymer", "<b>To help with melt compression and to block contaminants</b>",
       "To cool the extrudate", "To cut the product to length"],
 exp="""<p>讲义：<i>“<b>Breaker plate</b> helps with <b>melt compression</b> and <b>blocks contaminants</b>.”</i></p>
<p><b>挤出的完整流程</b>：<br>
① 料斗装树脂（颗粒或粉末）<br>
② <b>旋转螺杆</b>把固体树脂送入<b>加热料筒</b><br>
③ 树脂开始熔融并被<b>压实</b><br>
④ 全部熔融后被压过 <b>breaker plate</b><br>
⑤ 通过<b>口模（die）</b>挤出成所需形状</p>
<p><b>产品</b>：棒、管、各种形状和尺寸的片材。</p>
<p class="trap"><b>挤出是最基础的加工工艺</b>——注塑（injection molding）用的也是
"往复螺杆"，讲义明确说 <i>“similar to extrusion”</i>。吹塑的管坯也是先挤出的。</p>""",
 kp="Breaker plate 压实熔体并挡杂质；挤出是注塑、吹塑的共同基础",
 src="p.24「Extrusion」"),

dict(kind="理解", topic="模压 vs 传递模塑", ans=2,
 stem="What distinguishes <b>transfer molding</b> from <b>compression molding</b>?",
 opts=["Transfer molding uses no heat",
       "Compression molding uses a plunger",
       "<b>In transfer molding the resin is first loaded into a separate transfer cavity, then a plunger pushes the melt into the mold cavity</b>",
       "Transfer molding requires a vacuum"],
 exp="""<table class="mini"><thead><tr><th>工艺</th><th>做法</th></tr></thead><tbody>
<tr><td><b>Compression 模压</b></td><td>树脂直接放进<b>开启的加热模具下半部</b>，上半部压下，压力使熔体填满型腔，<b>多余料被挤出</b></td></tr>
<tr><td><b>Transfer 传递模塑</b></td><td>树脂先装入<b>单独的传递腔</b>，<b>柱塞</b>把熔化的高分子<b>推入</b>模腔</td></tr>
</tbody></table>
<p><b>传递模塑的优势</b>：熔体在进入模腔前已经熔好、流动性一致，
所以能做<b>更复杂、更精细</b>的零件，且不产生模压那样的溢料。</p>
<p class="trap"><b>三种"用柱塞/螺杆推熔体进模腔"的工艺容易混</b>：
传递模塑（柱塞）、<b>注塑</b>（往复螺杆 + 液压合模 + 顶针脱模）、
<b>反应注塑</b>（推入的是<b>单体</b>，在模腔内才聚合）。</p>""",
 kp="传递模塑用单独传递腔 + 柱塞；模压直接压、有溢料",
 src="p.25「Compression Molding / Transfer Molding」"),

dict(kind="理解", topic="反应注塑 RIM", ans=2,
 stem="In Reaction Injection Molding (RIM), what is injected into the mold?",
 opts=["Molten polymer", "Polymer solution",
       "<b>Monomers and other reactants (via a mixing unit); polymerization occurs inside the mold</b>",
       "Polymer powder"],
 exp="""<p>讲义：<i>“<b>Monomers and other reactants</b> are first injected into <b>mixing unit</b>,
followed by injection into the mold where <b>polymerization reaction occurs</b>.”</i></p>
<p><b>RIM 与普通注塑的根本区别</b>：注塑注入的是<b>已经聚合好的熔体</b>，
RIM 注入的是<b>还没反应的单体</b>，聚合在模腔里完成。</p>
<p class="trap"><b>RIM 的优势</b>：单体粘度<b>远低于</b>熔体，所以<br>
① 所需注射压力和合模力小得多<br>
② 能做<b>非常大</b>的零件（如汽车保险杠）<br>
③ 可以直接做<b>热固性</b>制品（交联在模内完成）</p>""",
 kp="RIM 注入单体、模内聚合；单体粘度低故可做大件与热固性制品",
 src="p.26「Reaction Injection Molding」"),

dict(kind="理解", topic="热成型", ans=1,
 stem="In thermoforming, the softened plastic sheet takes the shape of the mold because:",
 opts=["A plunger presses it down", "<b>A vacuum is applied to the space below the sheet</b>",
       "Air is blown into it", "Two rollers compress it"],
 exp="""<p>讲义：<i>“Plastic sheet is <b>heated till it softens</b>. A <b>vacuum is applied to the space below
the sheet</b> and the softened sheet is <b>forced to take the shape of the mold</b>.”</i></p>
<p class="trap"><b>与吹塑（Blow Molding）正好相反，很容易混</b>：</p>
<table class="mini"><thead><tr><th>工艺</th><th>起始形态</th><th>成型驱动</th></tr></thead><tbody>
<tr><td><b>Thermoforming 热成型</b></td><td><b>片材</b></td><td><b>下方抽真空</b>（向下吸）</td></tr>
<tr><td><b>Blow Molding 吹塑</b></td><td><b>中空管坯 parison</b></td><td><b>内部吹气</b>（向外胀）</td></tr>
</tbody></table>
<p><b>典型产品</b>：热成型 → 一次性餐盒、泡壳包装；吹塑 → 瓶子、中空容器。</p>""",
 kp="热成型：片材 + 抽真空；吹塑：管坯 + 吹气。两者驱动方向相反",
 src="p.27「Thermoforming / Blow Molding」"),

dict(kind="理解", topic="吹塑的管坯", ans=0,
 stem="In blow molding, the polymer is first extruded as:",
 opts=["<b>A hollow tube called a parison</b>", "A flat sheet", "A solid rod", "A fine fibre"],
 exp="""<p>讲义：<i>“Polymer is first <b>extruded as a hollow tube (parison)</b> into an open mold.
Mold closes and <b>air is forced in to inflate the parison</b>, which takes the shape of the mold.”</i></p>
<p><b>三步</b>：① 挤出管坯 → ② 合模 → ③ 吹气膨胀贴壁</p>
<p class="trap"><b>为什么必须是中空管坯</b>：要吹气就必须先有一个封闭的中空腔体。
这也是吹塑<b>只能做中空制品</b>（瓶、罐、油箱）的原因——实心件做不了。</p>
<p><b>注意"parison"这个词</b>——讲义特意给出了这个术语。</p>""",
 kp="吹塑先挤出中空管坯 parison，再合模吹气；只能做中空制品",
 src="p.27「Blow Molding」"),

dict(kind="理解", topic="压延成型", ans=1,
 stem="Calendering produces a thin plastic sheet by:",
 opts=["Extruding through a slit die", "<b>Compressing molten polymer in a small gap between two heated rotating cylinders</b>",
       "Casting from solution", "Blowing a bubble of melt"],
 exp="""<p>讲义：<i>“Molten polymer is <b>compressed in a small gap between two heated rotating cylinders</b>
to give a <b>thin plastic sheet</b>.”</i></p>
<p><b>与挤出片材的区别</b>：挤出是让熔体<b>通过口模</b>成型；
压延是让熔体<b>在两辊之间被辗压</b>成型。压延能做出更薄、更均匀、表面更好的膜。</p>
<p class="trap"><b>典型应用</b>：PVC 薄膜、人造革、地板革——都是压延产品。
压延特别适合<b>热敏性</b>材料（如 PVC），因为受热时间比挤出短。</p>""",
 kp="压延 = 两加热转辊间隙辗压成薄片；适合 PVC 等热敏材料",
 src="p.28「Calendering」"),

dict(kind="理解", topic="三种涂布方式", ans=2,
 stem="Which description of coating methods is <b>correct</b>?",
 opts=["Roll coating uses a blade to control thickness",
       "Blade coating extrudes melt directly onto the web",
       "<b>Roll coating: lower roll picks up liquid and delivers it to the sheet; Blade coating: a blade controls coating thickness; Slot-die: melt or solution is extruded directly onto the moving web</b>",
       "All three require a vacuum"],
 exp="""<p>讲义列出的三种涂布方式：</p>
<table class="mini"><thead><tr><th>方式</th><th>机理</th></tr></thead><tbody>
<tr><td><b>Roll coating</b></td><td><b>下辊</b>蘸取液体并<b>传递</b>到基材上</td></tr>
<tr><td><b>Blade coating</b></td><td>用<b>刮刀</b>控制涂层厚度</td></tr>
<tr><td><b>Slot-die coating</b></td><td>熔体或溶液<b>直接挤到</b>移动的基材（web）上</td></tr>
</tbody></table>
<p>共同点：都把高分子熔体或溶液涂到<b>移动的基材（web）</b>上。</p>
<p><b>后处理</b>：讲义注明 <i>“Coated film may be <b>crosslinked/cured</b> by heat or UV”</i>——
涂完可用<b>热或紫外</b>交联固化。</p>""",
 kp="三种涂布：roll（辊传递）、blade（刮刀控厚）、slot-die（直接挤出）；可热/UV 固化",
 src="p.28「Coating」"),

dict(kind="理解", topic="熔融纺丝", ans=1,
 stem="In melt spinning, the components in order are:",
 opts=["Spinneret → non-solvent bath → roller",
       "<b>Spinneret (die with tiny holes) → air cooling → godets (stretching rollers) → spin bobbin</b>",
       "Mixing unit → mold → ejector pins", "Heated cylinders → blade → web"],
 exp="""<p>讲义描述的熔融纺丝流程：<br>
① 高分子<b>熔融</b>并从带有一个或多个细孔的口模——称为 <b>spinneret（喷丝板）</b>——挤出<br>
② 挤出的纤维被<b>空气冷却</b><br>
③ <b>godets（导辊）拉伸</b>纤维<br>
④ 纤维卷绕到 <b>spin bobbin</b> 上</p>
<p class="trap"><b>godets 拉伸这一步至关重要</b>——它使链沿纤维轴<b>取向</b>
（正是前面讲的 necking / 应变硬化机理），大幅提高纤维的强度和模量。
<b>未拉伸的纤维强度很低。</b></p>""",
 kp="熔融纺丝：喷丝板 → 空气冷却 → godets 拉伸取向 → 卷绕；拉伸是强度的来源",
 src="p.29「Melt Spinning」"),

dict(kind="理解", topic="干法与湿法纺丝", ans=2,
 stem="What is the key difference between <b>dry</b> spinning and <b>wet</b> spinning?",
 opts=["Dry spinning uses a melt; wet spinning uses a solution",
       "Dry spinning uses water; wet spinning uses air",
       "<b>Dry spinning evaporates solvent with heated gas; wet spinning passes the solution through a spinneret immersed in a non-solvent bath where the fibre coagulates</b>",
       "They are the same process"],
 exp="""<p><b>两者都用 20–40 wt% 的高分子溶液</b>（不是熔体），区别在于<b>如何固化</b>：</p>
<table class="mini"><thead><tr><th>工艺</th><th>固化方式</th></tr></thead><tbody>
<tr><td><b>Dry 干法</b></td><td><b>加热气体</b>快速<b>蒸发</b>纤维中的溶剂</td></tr>
<tr><td><b>Wet 湿法</b></td><td>喷丝板<b>浸在非溶剂浴</b>中，纤维在其中<b>凝固</b>，由辊收集</td></tr>
</tbody></table>
<p class="trap"><b>为什么需要溶液纺丝</b>：有些高分子<b>熔点高于分解温度</b>
（如聚丙烯腈、纤维素），根本无法熔融纺丝，只能先溶解再纺。</p>
<p><b>三种纺丝的选择逻辑</b>：能熔就熔融纺（最经济）→ 不能熔就溶液纺 →
溶剂易挥发用干法、不易挥发用湿法。</p>""",
 kp="干法用热气蒸发溶剂、湿法用非溶剂浴凝固；两者都用溶液，适用于不能熔融的高分子",
 src="p.30「Dry Spinning / Wet Spinning」"),

dict(kind="理解", topic="静电纺丝", ans=1,
 stem="Electrospinning can draw polymer fibres down to thicknesses as small as:",
 opts=["100 μm", "<b>100 nm</b>", "1 mm", "1 Å"],
 exp="""<p>讲义：<i>“Electrospinning can draw polymer fibers to thicknesses as small as <b>100 nm</b>.”</i></p>
<p><b>原理</b>：<i>“A <b>highly-charged</b> polymer melt or solution is passed through a small aperture,
and is <b>accelerated by high voltage</b> towards a target plate.”</i>
静电斥力把射流不断拉细，得到纳米级纤维。</p>
<p><b>讲义补充</b>：<i>“Residual charges on the fiber <b>dissipate with time</b>”</i>——
纤维上的残余电荷会随时间耗散。给的图例是<b>静电纺 PET 的 SEM 照片</b>。</p>
<p class="trap"><b>量级对比</b>：常规熔融纺丝纤维直径约 10–50 μm，
静电纺是 <b>100 nm</b>——细了<b>两个数量级</b>。
巨大的比表面积使其适合<b>过滤、组织工程支架、传感器</b>等应用。</p>""",
 kp="静电纺丝靠高压静电拉细，可达 100 nm，比常规纺丝细两个数量级",
 src="p.31「Electrospinning」"),

dict(kind="计算", topic="应变的百分数表示", ans=2,
 stem="A rubber band of original length 8.0 cm is stretched to 56 cm. What is the strain?",
 opts=["7.0 (700%)", "<b>6.0 (600%)</b>", "0.86 (86%)", "48 (4800%)"],
 exp="""<div class="fb">ε = ΔL/L₀ = (56 − 8.0)/8.0 = 48/8.0 = <b>6.0</b>，即 <b>600%</b></div>
<p class="trap"><b>最常见的错误</b>：用 <b>L/L₀ = 56/8 = 7.0</b>（选项 A）。
应变的定义是 <b>ΔL</b>/L₀，分子是<b>长度的变化量</b>，不是最终长度。<br>
（伸长比 λ = L/L₀ = 7.0 是另一个量，在橡胶弹性理论中常用，但不是应变。）</p>
<p><b>合理性检查</b>：600% 的断裂应变正好落在讲义给弹性体的
<b>500%–1000%</b> 范围内 ✓</p>""",
 kp="ε = ΔL/L₀ 用长度变化量；区别于伸长比 λ = L/L₀",
 src="p.17「ε = ΔL/L₀」；p.19「500%-1000%」"),

dict(kind="计算", topic="由模量反推受力", ans=1,
 stem="A polymer rod (E = 3.0 GPa, cross-section 4.0 mm²) is to be stretched by 0.5% strain. What force is required?",
 opts=["30 N", "<b>60 N</b>", "120 N", "600 N"],
 exp="""<p><b>① 应力</b>：σ = Eε = 3.0×10⁹ × 0.005 = 1.5×10⁷ Pa = <b>15 MPa</b></p>
<p><b>② 力</b>：f = σA = 1.5×10⁷ × 4.0×10⁻⁶ = <b>60 N</b></p>
<p class="trap"><b>两处单位</b>：<br>
· 0.5% 要写成 <b>0.005</b>（不是 0.5）<br>
· 4.0 mm² = <b>4.0×10⁻⁶ m²</b></p>
<p><b>合理性</b>：60 N 约等于提起 6 kg 物体的力，对 4 mm² 的塑料杆产生 0.5% 形变——量级合理。</p>""",
 kp="f = EεA；百分比应变要化成小数，mm² 要化成 m²", src="p.17「σ_t = Eε」"),

dict(kind="理解", topic="加工工艺的选择", ans=1,
 stem="Which processing method would you choose to make a hollow plastic bottle?",
 opts=["Calendering", "<b>Blow molding</b>", "Melt spinning", "Compression molding"],
 exp="""<p><b>吹塑</b>是做中空容器的标准工艺：挤出管坯 → 合模 → 吹气贴壁。</p>
<p><b>其余选项各自的产品</b>：<br>
· <b>压延</b> → 薄膜、片材（<b>平面</b>制品）<br>
· <b>熔融纺丝</b> → 纤维<br>
· <b>模压</b> → 实心的、形状相对简单的件，且难做中空</p>
<p class="trap"><b>"工艺-产品"对应关系是本讲最实际的考点</b>：</p>
<table class="mini"><thead><tr><th>产品</th><th>工艺</th></tr></thead><tbody>
<tr><td>管材、棒材、片材（连续截面）</td><td><b>挤出</b></td></tr>
<tr><td>复杂形状的实心件</td><td><b>注塑</b></td></tr>
<tr><td>中空容器</td><td><b>吹塑</b></td></tr>
<tr><td>一次性餐盒、泡壳</td><td><b>热成型</b></td></tr>
<tr><td>薄膜、人造革</td><td><b>压延</b></td></tr>
<tr><td>纤维</td><td><b>纺丝</b></td></tr>
<tr><td>大型件、热固性件</td><td><b>RIM</b></td></tr>
</tbody></table>""",
 kp="工艺-产品对应表：挤出/注塑/吹塑/热成型/压延/纺丝/RIM 各有其典型制品",
 src="p.24–31「Polymer Processing」综合"),

dict(kind="理解", topic="力学与结构的贯通", ans=2,
 stem="Polystyrene is brittle at room temperature but the same polymer becomes ductile at 80 °C. The underlying reason connects to which property from Lecture 8?",
 opts=["Its molecular weight distribution", "Its degree of crystallinity",
       "<b>Its glass transition temperature (T<sub>g</sub> ≈ 100 °C) — approaching T<sub>g</sub> restores chain mobility</b>",
       "Its refractive index"],
 exp="""<p>PS 的 <b>T<sub>g</sub> ≈ 100 °C</b>。室温（25 °C）远低于 T<sub>g</sub>，链段被<b>冻结</b>
→ 无法进行塑性形变所需的重排 → <b>脆性</b>（讲义曲线 A）。</p>
<p>升到 80 °C 时已<b>接近</b> T<sub>g</sub>，链段活动性大幅提高
→ 能够成颈、取向 → <b>韧性</b>。</p>
<p class="trap"><b>这就是讲义那张"PMMA 在不同温度下的应力-应变曲线"想说明的事</b>：
<b>脆性/韧性不是材料的固有标签，而是"测试温度相对于 T<sub>g</sub> 的位置"。</b></p>
<p><b>由此可以推断</b>：<br>
· 室温下的<b>脆性</b>塑料 → T<sub>g</sub> <b>远高于</b>室温（PS、PMMA）<br>
· 室温下的<b>韧性</b>塑料 → T<sub>g</sub> <b>低于</b>室温（PE T<sub>g</sub> ≈ −120 °C、PP ≈ −10 °C）<br>
· 室温下的<b>弹性体</b> → T<sub>g</sub> 远低于室温 <b>且已交联</b></p>""",
 kp="脆性/韧性取决于测试温度相对 T_g 的位置；PE/PP 室温韧是因 T_g 极低",
 src="p.19–20（L9）与 p.11–12（L8）贯通"),
]
