# -*- coding: utf-8 -*-
LEC = 5
TITLE = "Characterization: Osmotic Pressure & Viscometry"
CN = "渗透压与粘度法"
SRC = "讲义 Lectures_5-7"
L = [
dict(kind="理解", topic="渗透压的起因", ans=1,
 stem="What makes solvent flow across the semipermeable membrane into the solution?",
 opts=["The solution is denser than the pure solvent",
       "The solvent's chemical potential is <b>lower</b> in the solution (μ<sub>A</sub> = μ<sub>A</sub>* + RT ln x<sub>A</sub> &lt; μ<sub>A</sub>*)",
       "The solute is attracted to the membrane", "Gravity pulls solvent through"],
 exp="""<p>由 <b>μ<sub>A</sub> = μ<sub>A</sub>* + RT ln x<sub>A</sub></b>，因 0 &lt; x<sub>A</sub> &lt; 1 故 ln x<sub>A</sub> &lt; 0，
所以<b>溶液侧溶剂的化学势更低</b>，体系不在平衡态。</p>
<p>讲义描述：纯溶剂侧的化学势"想降低"，溶液侧"想升高"，于是
<i>“solvent molecules move across membrane to <b>try to</b> dilute solution and increase its chemical potential”</i>。</p>
<p class="trap"><b>与溶质无关</b>——溶质根本过不了膜，它的作用只是<b>稀释溶剂</b>、降低溶剂的化学势。
这就是渗透压是<b>依数性</b>的根本原因。</p>""",
 kp="渗透压源于溶剂化学势在溶液侧被稀释而降低；与溶质种类无关",
 src="p.3「Osmotic Pressure」"),

dict(kind="理解", topic="压力如何抬高化学势", ans=0,
 stem="As solvent flows in, the liquid level rises and raises the pressure on the solution side. The chemical potential responds according to:",
 opts=["dμ = V<sub>m</sub> dp", "dμ = −S<sub>m</sub> dp", "dμ = RT dp", "dμ = −V<sub>m</sub> dp"],
 exp="""<p>由 dG = V dp − S dT，恒温下取摩尔量即 <b>dμ = V<sub>m</sub> dp</b>。积分：</p>
<div class="fb">μ<sub>A</sub>(p° + Π) = μ<sub>A</sub>(p°) + V<sub>m</sub>Π</div>
<p><b>压力升高使化学势升高</b>（V<sub>m</sub> &gt; 0），这正好<b>抵消</b>稀释造成的降低。
当两者恰好相等时体系达到平衡，此时的压差就是<b>渗透压 Π</b>。</p>
<p class="trap">这里再次用到 Lecture 2 的 <b>(∂G/∂p)<sub>T</sub> = V</b>——
这个偏导在本课至少出现三次（气体 G = G° + nRT ln p、渗透压、以及 Lecture 8 判断转变阶数）。</p>""",
 kp="dμ = V_m dp；压力升高抵消稀释降低，平衡时给出 Π",
 src="p.4「Osmotic Pressure」"),

dict(kind="计算", topic="渗透压的基本关系", ans=1,
 stem="Setting the two chemical potentials equal at equilibrium gives which relation?",
 opts=["V<sub>m</sub>Π = +RT ln x<sub>A</sub>", "V<sub>m</sub>Π = −RT ln x<sub>A</sub>",
       "Π = RT ln x<sub>A</sub>", "V<sub>m</sub>Π = RT x<sub>A</sub>"],
 exp="""<p>平衡条件：μ<sub>A</sub>*(p°) = μ<sub>A</sub>(p° + Π)</p>
<p>左边 = μ<sub>A</sub>(p°) − RT ln x<sub>A</sub>；右边 = μ<sub>A</sub>(p°) + V<sub>m</sub>Π</p>
<div class="fb">V<sub>m</sub>Π = −RT ln x<sub>A</sub></div>
<p><b>符号检查</b>：ln x<sub>A</sub> &lt; 0，所以 −RT ln x<sub>A</sub> &gt; 0 → <b>Π &gt; 0</b>，
渗透压为正，物理上合理。</p>""",
 kp="V_mΠ = −RT ln x_A 是渗透压的严格出发点", src="p.5「Osmotic Pressure」"),

dict(kind="理解", topic="Taylor 展开的作用", ans=2,
 stem="The expansion ln x<sub>A</sub> = ln(1 − x<sub>B</sub>) = −x<sub>B</sub> − ½x<sub>B</sub>² − ⅓x<sub>B</sub>³ … is used to:",
 opts=["Prove that Π is always negative", "Eliminate the temperature dependence",
       "Turn the exact relation into a <b>power series in concentration</b> (the virial expansion)",
       "Convert mole fraction to volume fraction"],
 exp="""<p>把 Taylor 展开代入 V<sub>m</sub>Π = −RT ln x<sub>A</sub>，得到按浓度幂次排列的级数：</p>
<div class="fb">Π = RT [ c/M + Bc² + B₃c³ + ⋯ ]</div>
<p>讲义称之为 <b>virial expansion（维里展开）</b>。</p>
<p><b>为什么这么做</b>：第一项 c/M <b>只与分子数目有关</b>，可以直接给出分子量；
高次项则装进了<b>溶质-溶质相互作用</b>的信息。把两类效应分离开，实验上才能低浓度外推取斜率。</p>
<p class="trap"><b>稀溶液近似</b>：x<sub>B</sub> 很小时 ln(1−x<sub>B</sub>) ≈ −x<sub>B</sub>，
只保留第一项 → Π = RT c/M。这是所有渗透压计算题的基础。</p>""",
 kp="Taylor 展开把精确式变成 virial 级数，分离「数分子」与「相互作用」两部分",
 src="p.5「Taylor series / Virial expansion」"),

dict(kind="计算", topic="渗透压计算", ans=1,
 stem="A polymer solution of 2.0 g/L has M = 25,000 g/mol. What is Π at 298 K (dilute limit)?",
 opts=["66 Pa", "198 Pa", "496 Pa", "1,983 Pa"],
 exp="""<p><b>单位换算（关键）</b>：c = 2.0 g/L = <b>2,000 g/m³</b></p>
<div class="fb">Π = RT · c/M = 8.314 × 298 × (2,000 / 25,000)</div>
<p>= 2,477.6 × 0.08 = <b>198 Pa</b></p>
<p class="trap"><b>最大的坑是单位</b>：SI 制下 c 必须是 <b>g/m³</b>，M 是 g/mol，Π 才是 Pa。
直接代 2.0 g/L 会得到 0.198 Pa，差 1000 倍。</p>
<p><b>换成液柱</b>：h = Π/(ρg) = 198/9810 ≈ <b>2.0 cm</b>——这就是渗透压法好用的原因，
几百 Pa 的微小压力被放大成厘米级的可读高度。</p>""",
 kp="Π = RTc/M；c 用 g/m³（1 g/L = 1000 g/m³）", src="p.6「Osmotic Pressure」"),

dict(kind="计算", topic="由渗透压反求分子量", ans=2,
 stem="A 4.0 g/L solution shows Π = 330 Pa at 300 K. What is M (dilute limit)?",
 opts=["7,560 g/mol", "15,100 g/mol", "30,200 g/mol", "60,500 g/mol"],
 exp="""<div class="fb">M = RT · c / Π = 8.314 × 300 × 4,000 / 330</div>
<p>= 2,494.2 × 4,000 / 330 = 9,976,800 / 330 = <b>30,200 g/mol</b></p>
<p class="trap"><b>陷阱</b>：忘记把 4.0 g/L 换成 4,000 g/m³ 会得到 30.2 g/mol，
一个荒谬的高分子量——<b>结果荒谬时先查单位</b>。</p>""",
 kp="M = RTc/Π；结果量级不合理时优先检查单位换算", src="p.6"),

dict(kind="计算", topic="液柱高度", ans=2,
 stem="An osmotic pressure of 500 Pa is measured. What height of aqueous solution column does this correspond to? (ρ = 1000 kg/m³, g = 9.81 m/s²)",
 opts=["0.51 mm", "5.1 mm", "5.1 cm", "51 cm"],
 exp="""<div class="fb">h = Π / (ρg) = 500 / (1000 × 9.81) = 0.0510 m = <b>5.1 cm</b></div>
<p><b>好记的换算</b>：<b>约 100 Pa ≈ 1 cm 水柱</b>。
所以几百帕的渗透压对应几厘米——用尺子就能读得很准。</p>
<p>这就是<b>膜渗透压法</b>能测高分子量的原因：直接测压力困难，但测液面高度容易。</p>""",
 kp="h = Π/(ρg)；约 100 Pa ≈ 1 cm 水柱", src="p.4「creates an increase in pressure… proportional to height of fluid」"),

dict(kind="理解", topic="依数性", ans=2,
 stem="Two separate setups contain 0.01 mol/L glucose and 0.01 mol/L sucrose respectively. Which shows the higher osmotic pressure?",
 opts=["Glucose (smaller molecule)", "Sucrose (larger molecule)",
       "Approximately the same", "Cannot be determined without the molar masses"],
 exp="""<p><b>基本相同。</b>讲义原文：<i>“In dilute solutions, osmotic pressure depends on the
<b>number of solute particles and not their identity</b>. This is known as a <b>colligative property</b>
(same as boiling point elevation and freezing point depression).”</i></p>
<p><b>数学来源</b>：virial 展开的第一项是 RT·n<sub>B</sub>/V——<b>只含摩尔浓度</b>，不含任何与溶质
种类有关的量。葡萄糖和蔗糖虽然分子量差近一倍，但<b>摩尔浓度相同</b>，故 Π 相同。</p>
<p class="trap"><b>正因如此，渗透压法测的是 M<sub>n</sub>（数均）</b>——它数的是"个数"。
这与光散射（按质量加权，给 M<sub>w</sub>）形成鲜明对照。</p>""",
 kp="渗透压是依数性，只数分子个数 → 测 Mn；同族还有沸点升高、凝固点降低",
 src="官方 Question 18（对应 p.7）"),

dict(kind="理解", topic="良溶剂中的 B", ans=0,
 stem="In a <b>good</b> solvent, the second virial coefficient B is:",
 opts=["B &gt; 0, because favourable polymer-solvent interaction gives a greater drive for solvent to cross the membrane",
       "B &lt; 0", "B = 0", "B is undefined"],
 exp="""<p>讲义原文：<i>“In good solvents, polymer-solvent interaction is favourable.
There is <b>greater drive for solvent to cross the membrane</b>, hence <b>B &gt; 0</b>.”</i></p>
<p><b>物理图像</b>：良溶剂里高分子"喜欢"被溶剂包围，因此更"渴望"稀释
→ 渗透压<b>高于</b>仅由分子数目预测的理想值 → 正的偏离 → B &gt; 0。</p>
<p><b>三讲串联</b>：良溶剂 ⟺ <b>B &gt; 0</b>（L5）⟺ <b>χ &lt; 0.5</b>（L3）⟺
<b>R<sub>g</sub> ∝ N<sup>3/5</sup></b>（L1）⟺ <b>a ≈ 0.8</b>（L5 粘度）。<b>四种说法描述同一件事。</b></p>""",
 kp="良溶剂 B>0；与 χ<0.5、ν=3/5、a≈0.8 完全等价",
 src="p.7「Some Conclusions on Osmotic Pressure」"),

dict(kind="理解", topic="不良溶剂中的 B", ans=1,
 stem="In a <b>poor</b> solvent, B is negative because:",
 opts=["The polymer precipitates immediately",
       "Solute-solute interaction is favourable, so solvent crossing the membrane to dilute the solution is <b>not</b> favoured",
       "The membrane leaks", "The molar mass becomes negative"],
 exp="""<p>讲义原文：<i>“In poor solvents, <b>solute-solute interaction is favourable</b>.
Solvents crossing membrane to dilute solution is <b>not favoured</b>. B &lt; 0.”</i></p>
<p>链段之间宁愿彼此接触也不愿接触溶剂 → 链<b>塌缩</b>，稀释的驱动力减弱 →
渗透压<b>低于</b>理想值 → B &lt; 0。</p>""",
 kp="不良溶剂 B<0，链倾向自身聚集而非被溶剂化", src="p.7「In poor solvents」"),

dict(kind="理解", topic="θ 溶剂", ans=2,
 stem="A solvent for which B = 0 is called:",
 opts=["An ideal solvent", "A good solvent", "A <b>theta (θ)</b> solvent", "A non-solvent"],
 exp="""<p>讲义原文：<i>“In intermediate case where <b>B = 0</b>, the solvent is called a <b>theta (θ) solvent</b>.”</i></p>
<p><b>θ 溶剂的特殊地位</b>：链-链吸引与排除体积排斥<b>恰好抵消</b>，链表现为<b>理想链</b>：</p>
<table class="mini"><thead><tr><th>量</th><th>θ 溶剂中的值</th></tr></thead><tbody>
<tr><td>第二维里系数 B</td><td><b>0</b></td></tr>
<tr><td>Flory-Huggins χ</td><td><b>0.5</b></td></tr>
<tr><td>标度指数 ν</td><td><b>1/2</b></td></tr>
<tr><td>Mark-Houwink a</td><td><b>0.5</b></td></tr>
</tbody></table>
<p class="trap">这张表是<b>跨讲综合题的高发区</b>——四个数字描述的是同一个物理状态。</p>""",
 kp="θ 溶剂：B=0、χ=0.5、ν=1/2、a=0.5，链呈理想链行为", src="p.7「theta (θ) solvent」"),

dict(kind="计算", topic="从图求分子量", ans=0,
 stem="A plot of Π/RT versus c is linear at low c with slope 1.0×10⁻⁴ mol/g. What is M?",
 opts=["10,000 g/mol", "7,500 g/mol", "5,800 g/mol", "5,000 g/mol"],
 exp="""<p>低浓度时高次项可忽略：</p>
<div class="fb">Π/RT ≈ c/M　→　斜率 = <b>1/M</b></div>
<p>M = 1 / (1.0×10⁻⁴) = <b>10,000 g/mol</b></p>
<p class="trap"><b>两个要点</b>：<br>
① 必须取<b>低浓度处</b>的斜率——高浓度处 Bc² 项使曲线弯曲<br>
② 斜率是 1/M，要<b>取倒数</b></p>
<p><b>B 的正负从曲线弯曲方向也能读出</b>：向上弯 → B &gt; 0（良溶剂）；向下弯 → B &lt; 0（不良溶剂）。</p>""",
 kp="Π/RT vs c 的低浓度斜率 = 1/M；曲线弯曲方向给出 B 的符号",
 src="官方 Question 19（对应 p.6–7）"),

dict(kind="理解", topic="渗透压测哪种平均", ans=0,
 stem="For a polydisperse polymer, the M obtained from osmotic pressure is:",
 opts=["The <b>number-average</b> M<sub>n</sub>", "The weight-average M<sub>w</sub>",
       "The viscosity-average M<sub>v</sub>", "The z-average M<sub>z</sub>"],
 exp="""<p>讲义原文：<i>“In polydisperse polymers with a range of molecular weight,
M represents <b>number-average molecular weight M<sub>n</sub></b>.”</i></p>
<p><b>为什么</b>：Π 的第一项正比于<b>溶质的摩尔浓度</b>（分子个数/体积）。
测总质量除以总摩尔数，得到的正是 M<sub>n</sub> 的定义。</p>
<p class="trap"><b>方法-平均值对照（高频综合题）</b>：<br>
· <b>M<sub>n</sub></b> ← 膜渗透压、VPO、端基分析（依数性，数个数）<br>
· <b>M<sub>w</sub></b> ← 静态光散射（按质量加权）<br>
· <b>M<sub>v</sub> ≈ M<sub>w</sub></b> ← 粘度法<br>
· <b>R<sub>h</sub></b> ← DLS（不给分子量）</p>""",
 kp="渗透压给 Mn；这是依数性方法的共同特征", src="p.7 第 6 条结论"),

dict(kind="理解", topic="蒸气压渗透法 VPO", ans=1,
 stem="In vapour-phase osmometry, why does the temperature of the <b>solution</b> droplet rise?",
 opts=["Because the solution has a higher heat capacity",
       "Because the solution has a <b>lower chemical potential</b>, so solvent vapour <b>condenses</b> onto it, releasing latent heat",
       "Because the thermistor heats it electrically", "Because the solute reacts exothermically"],
 exp="""<p>讲义原文：<i>“Since solution has a <b>lower chemical potential</b>, solvent vapour <b>condenses at the solution</b>.
This typically <b>raises the solution temperature</b>.”</i>（冷凝放出潜热）</p>
<p><b>装置</b>：密闭腔内被溶剂蒸气饱和，两个热敏电阻上分别放一滴溶液和一滴纯溶剂，测温差 ΔT。</p>
<div class="fb">ΔT = K [ c/M + Bc² + B₃c³ + ⋯ ]</div>
<p>形式与渗透压<b>完全相同</b>，只是把 RT 换成了<b>标定常数 K</b>。</p>
<p class="trap"><b>VPO 必须用已知分子量的标样标定 K</b>——这是它与膜渗透压法的关键差别，
后者的 RT 是已知的，不需要标定。</p>""",
 kp="VPO：溶剂蒸气在溶液上冷凝放热 → ΔT；需标样标定 K；同样测 Mn",
 src="p.8「Vapour-Phase Osmometry」"),

dict(kind="理解", topic="Newton 粘度定律", ans=0,
 stem="Newton's law of viscosity states that the shear stress σ is related to the velocity gradient by:",
 opts=["σ = η (dv/dy)", "σ = η / (dv/dy)", "σ = η (dy/dv)", "σ = η²(dv/dy)"],
 exp="""<div class="fb">σ = η (dv/dy)</div>
<p>· <b>σ 剪切应力</b>（Pa）= F/A，作用力<b>平行</b>于表面<br>
· <b>dv/dy 速度梯度</b>（s⁻¹），也记作 γ<br>
· <b>η 粘度</b>（Pa·s），是两者的比例常数</p>
<p class="trap"><b>讲义特别提醒：剪切应力 σ 与压强不同</b>（"Note: this is different from pressure"）。
虽然量纲都是 Pa，但压强<b>垂直</b>于表面，剪切应力<b>平行</b>于表面。</p>""",
 kp="σ = η dv/dy；剪切应力平行于表面，与压强（垂直）不同",
 src="p.9「Newton's Law of Viscosity」"),

dict(kind="理解", topic="剪切变稀", ans=2,
 stem="Some fluids appear <b>less viscous</b> at high flow rates. This effect is called:",
 opts=["Shear thickening", "Newtonian flow", "<b>Shear thinning</b>", "Creep"],
 exp="""<p>讲义原文：<i>“At high flow rates, some fluids behave <b>less viscous</b> due to an effect called
<b>shear thinning</b>”</i>，并声明本课<b>只处理 Newtonian 流动</b>。</p>
<p><b>高分子为什么会剪切变稀</b>：高剪切下无规线团被拉伸<b>沿流动方向取向</b>、
链间缠结被解开，流动阻力下降。</p>
<p class="trap"><b>工业意义极大</b>：注塑、挤出（Lecture 9）都在高剪切下进行，
正是靠剪切变稀，熔体才能顺利填满模腔。<b>但粘度法测分子量必须在低剪切下做</b>，
否则测到的不是零剪切粘度，分子量会算错。</p>""",
 kp="剪切变稀 = 高剪切下粘度下降；本课只处理 Newtonian 流",
 src="p.10「Newton's Law of Viscosity」"),

dict(kind="理解", topic="溶解高分子对粘度的影响", ans=0,
 stem="How does the viscosity of a solution change when a polymer is dissolved in it?",
 opts=["Viscosity <b>always increases</b>", "Viscosity always decreases",
       "Viscosity stays the same", "It depends on the polymer and solvent"],
 exp="""<p>讲义给的答案：<i>“Viscosity <b>always increases</b> because the polymer particles in the liquid
<b>obstructs and hinders the flow</b> of the liquid. Hence, higher shear stress is required to maintain
the same velocity gradient.”</i></p>
<p class="trap"><b>注意"always"</b>——选项 D（"看高分子和溶剂"）看起来很稳妥，
但在这个层面上是<b>错</b>的。溶剂品质会影响<b>增加多少</b>（通过 R<sub>g</sub> 和 V<sub>h</sub>），
但<b>方向永远是增加</b>：任何占体积的粒子都阻碍流动。</p>
<p>Einstein 定律 η = η<sub>s</sub>(1 + 2.5φ + …) 从数学上保证了这一点——括号里恒大于 1。</p>""",
 kp="溶解高分子必然增大粘度（占体积阻碍流动）；溶剂品质只影响增幅",
 src="官方 Question 20（对应 p.12–13）"),

dict(kind="理解", topic="Stokes 定律", ans=1,
 stem="Stokes' law for the viscous force on a sphere is F<sub>vis</sub> = 6πη<sub>s</sub>Rv₀. The quantity 6πη<sub>s</sub>R is called:",
 opts=["The Reynolds number", "The <b>friction factor</b> f", "The intrinsic viscosity", "The virial coefficient"],
 exp="""<div class="fb">F<sub>vis</sub> = 6π η<sub>s</sub> R v₀，其中 <b>f = 6π η<sub>s</sub> R</b> 为摩擦因子</div>
<p>· η<sub>s</sub>：流体粘度　· R：球半径　· v₀：球相对流体的速度</p>
<p class="trap"><b>这个 6πηR 会在 Lecture 6 再次出现</b>——Stokes-Einstein 关系
<b>D<sub>t</sub> = kT/(6πη<sub>s</sub>R<sub>h</sub>)</b> 就是由它推导的。
讲义明确写着 "derived from Stokes' Law"。<b>DLS 测 R<sub>h</sub> 的理论根基在这一页。</b></p>""",
 kp="Stokes 定律 F = 6πηRv；摩擦因子 f = 6πηR 是 Stokes-Einstein 的来源",
 src="p.11「Viscous Forces on Rigid Spheres – Stokes' Law」"),

dict(kind="计算", topic="Einstein 粘度定律", ans=2,
 stem="Rigid spheres occupy 4.0 vol% of a suspension. By Einstein's law (to first order), by what percentage does the viscosity increase?",
 opts=["4.0%", "6.4%", "10.0%", "25.0%"],
 exp="""<div class="fb">η = η<sub>s</sub>(1 + (5/2)φ + 4φ² + ⋯) ≈ η<sub>s</sub>(1 + 2.5φ)</div>
<p>2.5 × 0.040 = 0.100 → <b>增加 10.0%</b></p>
<p class="trap"><b>讲义强调的关键性质</b>：<i>“The overall viscosity <b>does not depend on sphere size</b>,
but only on their <b>volume fraction (φ)</b>.”</i></p>
<p>一个大球和一千个小球，只要总体积分数相同，对粘度的贡献就相同。
这正是把它用到高分子上的<b>理由</b>——链的形状千变万化，但只要能定义一个
<b>流体力学体积 V<sub>h</sub></b>，就能套用。</p>""",
 kp="Einstein: η = η_s(1+2.5φ)；只依赖体积分数，与球大小无关",
 src="p.12「Viscosity for a Suspension of Spheres – Einstein's Law」"),

dict(kind="理解", topic="特性粘度的定义", ans=1,
 stem="In η = η<sub>s</sub>(1 + c[η] + k<sub>h</sub>c²[η]² + …), the intrinsic viscosity [η] represents:",
 opts=["The viscosity of the pure polymer melt",
       "The <b>rate at which viscosity increases with added concentration</b>",
       "The viscosity of the pure solvent", "The shear stress at unit velocity gradient"],
 exp="""<p>讲义原文：<i>“[η] is defined as <b>intrinsic viscosity</b> and represents
<b>rate at which viscosity increases with added concentration</b>”</i>。</p>
<p>把 Einstein 定律里的 φ 换成高分子的表达式 φ = cN<sub>Av</sub>V<sub>h</sub>/M，对比系数得：</p>
<div class="fb">[η] = (5/2) · N<sub>Av</sub>V<sub>h</sub> / M</div>
<p><b>物理含义</b>：[η] ∝ V<sub>h</sub>/M，即"<b>每单位质量占多大流体力学体积</b>"
——它衡量的是链在溶液里<b>有多蓬松</b>。良溶剂中链膨胀 → V<sub>h</sub> 大 → [η] 大。</p>""",
 kp="[η] = (5/2)N_Av V_h/M，衡量单位质量占据的流体力学体积（链的蓬松程度）",
 src="p.13「Applying Einstein's Law to a Polymer Solution」"),

dict(kind="理解", topic="流体力学体积", ans=1,
 stem="When applying Einstein's law to a polymer chain, assuming the chain behaves 'hydrodynamically like a sphere' means:",
 opts=["The chain is literally shaped like a sphere",
       "The chain <b>drags solvent as though</b> it were a sphere of volume V<sub>h</sub> — it does not mean it is shaped like one",
       "The chain must be crosslinked", "The chain has zero volume"],
 exp="""<p>讲义特意加了括号说明：<i>“if we assumed that a polymer chain behaved <b>hydrodynamically</b>
like a sphere (<b>does not mean it is shaped like a sphere</b>)”</i>。</p>
<p><b>真实的链是蓬松的无规线团</b>，但它<b>裹挟</b>着内部的溶剂一起运动，
在流体动力学上等效于一个实心球——这个等效球的体积就是 <b>V<sub>h</sub></b>，且 V<sub>h</sub> ∝ (4/3)πR<sub>g</sub>³。</p>
<p class="trap"><b>同样的"等效球"思想</b>在 DLS 里给出 <b>R<sub>h</sub></b>
（"as if it is a hard sphere with radius R<sub>h</sub>"）。<b>R<sub>g</sub>、R<sub>h</sub>、V<sub>h</sub>
描述的是同一个线团的不同侧面</b>，数值上不相等。</p>""",
 kp="流体力学等效球：链裹挟溶剂一起运动，等效体积 V_h ∝ R_g³",
 src="p.14「behaved hydrodynamically like a sphere」"),

dict(kind="计算", topic="Mark-Houwink 指数的推导", ans=1,
 stem="Combining [η] ∝ R<sub>g</sub>³/M with R<sub>g</sub> ∝ N<sup>ν</sup> ∝ M<sup>ν</sup> gives [η] = kM<sup>a</sup> with a equal to:",
 opts=["3ν", "<b>3ν − 1</b>", "ν − 1", "ν/3"],
 exp="""<div class="fb">[η] ∝ R<sub>g</sub>³/M ∝ M<sup>3ν</sup>/M = M<sup>3ν−1</sup>　⇒　<b>a = 3ν − 1</b></div>
<p>讲义的推导路径：Einstein → [η] = (5/2)N<sub>Av</sub>V<sub>h</sub>/M → V<sub>h</sub> ∝ R<sub>g</sub>³
→ 代入标度关系 → <b>Mark-Houwink 方程</b>。</p>
<p class="trap"><b>会推比会背重要</b>——这样任给一个 ν 都能立刻算出 a，
不需要死记那张表。</p>""",
 kp="a = 3ν − 1，由 [η] ∝ R_g³/M 与 R_g ∝ M^ν 联立得到",
 src="p.14「Mark-Houwink Equation」"),

dict(kind="计算", topic="a 值与溶剂品质", ans=2,
 stem="Given [η] = kM<sup>a</sup>, what value of a is expected for a polymer dissolved in a <b>good solvent</b>?",
 opts=["0.3", "0.5", "0.8", "2.0"],
 exp="""<p>良溶剂 ν = 3/5：</p>
<div class="fb">a = 3(3/5) − 1 = 9/5 − 1 = 4/5 = <b>0.8</b></div>
<p><b>完整对照表</b>：</p>
<table class="mini"><thead><tr><th>链形态</th><th>ν</th><th>a = 3ν−1</th></tr></thead><tbody>
<tr><td>致密球</td><td>1/3</td><td><b>0</b></td></tr>
<tr><td>θ 溶剂 / 理想链</td><td>1/2</td><td><b>0.5</b></td></tr>
<tr><td><b>良溶剂</b></td><td>3/5</td><td><b>0.8</b></td></tr>
<tr><td>刚性棒</td><td>1</td><td><b>2</b></td></tr>
</tbody></table>
<p>讲义补充：<i>“Most values of a lie between <b>0.5 and 1</b>, which represents flexible chain with
finite chain volume.”</i></p>""",
 kp="良溶剂 a = 0.8；实际柔性链的 a 多在 0.5–1 之间",
 src="官方 Question 21（对应 p.14–15）"),

dict(kind="计算", topic="刚性棒的 a 值", ans=3,
 stem="What is a for a polymer that behaves as a <b>rigid rod</b>?",
 opts=["0", "0.5", "1.0", "2.0"],
 exp="""<p>刚性棒完全伸直，R<sub>g</sub> ∝ N¹，即 ν = 1：</p>
<div class="fb">a = 3(1) − 1 = <b>2</b></div>
<p>这是四种形态中 a 的<b>最大值</b>——刚性棒的 [η] 对分子量最敏感。</p>
<p class="trap"><b>另一端</b>：致密球 ν = 1/3 给 a = 0，意味着 [η] <b>与分子量无关</b>。
这很好理解——致密球的 V<sub>h</sub>/M 就是比容，与球多大无关。</p>""",
 kp="刚性棒 a = 2（上限）；致密球 a = 0，[η] 与 M 无关",
 src="p.14–15「Mark-Houwink」"),

dict(kind="计算", topic="Mark-Houwink 实际计算", ans=1,
 stem="For a polymer with k = 2.0×10⁻⁴ and a = 0.75, what is [η] for M = 100,000 g/mol? (units: dL/g)",
 opts=["0.20 dL/g", "1.12 dL/g", "2.00 dL/g", "20.0 dL/g"],
 exp="""<div class="fb">[η] = k M<sup>a</sup> = 2.0×10⁻⁴ × (100,000)<sup>0.75</sup></div>
<p>(10⁵)<sup>0.75</sup> = 10<sup>3.75</sup> = <b>5,623</b></p>
<p>[η] = 2.0×10⁻⁴ × 5,623 = <b>1.12 dL/g</b></p>
<p class="trap"><b>算 10 的分数次幂的技巧</b>：把底数写成 10 的幂，指数直接相乘。
(10⁵)<sup>0.75</sup> = 10<sup>3.75</sup>，而 10<sup>3.75</sup> = 10³ × 10<sup>0.75</sup> ≈ 1000 × 5.62 = 5,620。</p>""",
 kp="[η] = kM^a 的直接计算；把底数化为 10 的幂便于心算", src="p.14–15"),

dict(kind="理解", topic="粘度法测哪种平均", ans=2,
 stem="The molecular weight obtained from viscometry is:",
 opts=["Exactly M<sub>n</sub>", "Exactly M<sub>w</sub>",
       "M<sub>v</sub>, which is usually <b>closer to M<sub>w</sub></b>", "The z-average"],
 exp="""<p>讲义原文：<i>“this is usually <b>closer to weight-average molecular weight (M<sub>w</sub>)</b>”</i>。</p>
<p><b>为什么</b>：[η] ∝ M<sup>a</sup>，a 通常在 0.5–1 之间。<br>
· 若 a = 1，M<sub>v</sub> <b>严格等于</b> M<sub>w</sub><br>
· a &lt; 1 时 M<sub>v</sub> 略低于 M<sub>w</sub>，但仍远高于 M<sub>n</sub></p>
<p class="trap"><b>粘度法的两个前提</b>（讲义明确指出）：<br>
① 必须用已知分子量的标样<b>标定 k 和 a</b>，或从文献查<br>
② k、a 依赖<b>高分子-溶剂-温度</b>三者的组合，换体系就要重新标定</p>""",
 kp="粘度法给 M_v ≈ M_w；k 和 a 需标定，且依赖高分子/溶剂/温度",
 src="p.15「Viscometry Experimental Techniques」"),

dict(kind="理解", topic="旋转粘度计", ans=1,
 stem="In a rotational viscometer, viscosity is obtained from:",
 opts=["The time for a fixed volume to flow through a capillary",
       "The ratio of <b>torque</b> to <b>angular velocity</b>, times a calibration constant",
       "The height of a liquid column", "The rate of sphere sedimentation"],
 exp="""<div class="fb">η = C × (Torque / Angular velocity)</div>
<p>讲义的对应关系：<br>
· <b>转动圆盘所需扭矩</b> ∝ 剪切应力 σ<br>
· <b>角速度（转速）</b> ∝ 速度梯度 dv/dy</p>
<p>两者相除正是 η = σ/(dv/dy)，再乘一个<b>标定常数 C</b> 修正几何因素。</p>
<p class="trap"><b>旋转粘度计的独特优势</b>：可以<b>连续改变转速</b>，
从而测出粘度随剪切速率的变化——这是检测<b>剪切变稀</b>的标准手段。
毛细管粘度计只能给出单一剪切条件下的值。</p>""",
 kp="旋转粘度计：η = C × 扭矩/角速度；可变转速，适合研究剪切变稀",
 src="p.16「Rotational Viscometer」"),

dict(kind="理解", topic="毛细管粘度计与 Poiseuille 方程", ans=3,
 stem="In the Poiseuille equation ΔV/Δt = (ρgL + Δp)πR⁴/(8ηL), the flow rate is most sensitive to which quantity?",
 opts=["The solution density ρ", "The capillary length L", "The viscosity η",
       "The capillary <b>radius R</b>, since it enters as R⁴"],
 exp="""<div class="fb">ΔV/Δt = (ρgL + Δp) π R⁴ / (8ηL)</div>
<p><b>R 的四次方</b>意味着半径变化 10% 会使流量变化约 46%——远比其他变量敏感。</p>
<p class="trap"><b>实验含义</b>：<br>
① 毛细管必须<b>极其洁净</b>——一点点污物就显著改变有效半径<br>
② 同一支粘度计的<b>相对</b>测量（溶液 vs 纯溶剂流出时间之比）可以<b>消去</b> R⁴、L 等几何量，
这正是 Ubbelohde 粘度计的实际用法</p>
<p><b>Ubbelohde 的设计要点</b>（讲义）：底部的<b>开口管 D</b> 保证液柱上下气压相等，
使 Δp 项可控。</p>""",
 kp="Poiseuille 中 R⁴ 使流量对半径极敏感 → 实际用相对测量消去几何量",
 src="p.17「Capillary Viscometer / Ubbelohde Viscometer」"),

dict(kind="计算", topic="相对粘度法", ans=1,
 stem="In an Ubbelohde viscometer, pure solvent takes 100 s to flow between the marks and the polymer solution takes 125 s. Assuming equal densities, what is η/η<sub>s</sub>?",
 opts=["0.80", "1.25", "1.56", "25"],
 exp="""<p>由 Poiseuille 方程，同一支粘度计、同样的驱动压力下，<b>流出时间正比于粘度</b>
（几何量 R⁴、L 和驱动项全部相同，相除即消去）：</p>
<div class="fb">η / η<sub>s</sub> = t / t<sub>s</sub> = 125 / 100 = <b>1.25</b></div>
<p>即溶液粘度比纯溶剂高 25%，这个比值叫<b>相对粘度</b> η<sub>rel</sub>。</p>
<p><b>接下来怎么用</b>：由 η = η<sub>s</sub>(1 + c[η] + …) 得
(η<sub>rel</sub> − 1)/c ≈ [η]（低浓度），再由 [η] = kM<sup>a</sup> 求分子量。
实际操作要测<b>多个浓度</b>并<b>外推到 c → 0</b>。</p>""",
 kp="相对粘度 = 流出时间之比；几何量相除消去，故只需测时间",
 src="p.17「Time measurement (Δt)」"),

dict(kind="理解", topic="渗透压与粘度法的分工", ans=2,
 stem="A researcher needs both M<sub>n</sub> and an estimate of chain <b>size in solution</b>. The best pairing is:",
 opts=["Viscometry for M<sub>n</sub>, osmometry for size",
       "Both from osmometry alone",
       "<b>Osmometry for M<sub>n</sub>, viscometry for [η] (which reflects V<sub>h</sub> ∝ R<sub>g</sub>³)</b>",
       "Neither technique gives size information"],
 exp="""<p><b>渗透压</b>：第一项只数分子个数 → <b>M<sub>n</sub></b>，但<b>完全不含尺寸信息</b>
（依数性——葡萄糖和蔗糖给同样的 Π）。</p>
<p><b>粘度</b>：[η] = (5/2)N<sub>Av</sub>V<sub>h</sub>/M，而 V<sub>h</sub> ∝ R<sub>g</sub>³
→ <b>直接反映链在溶液中的尺寸</b>。</p>
<p class="trap"><b>额外收获</b>：由 Mark-Houwink 指数 a 还能反推<b>溶剂品质</b>
（a ≈ 0.5 → θ 溶剂；a ≈ 0.8 → 良溶剂）。所以粘度法一次给出"多大 + 溶得好不好"两条信息，
这是它虽然需要标定却仍被广泛使用的原因。</p>""",
 kp="渗透压给 Mn 但无尺寸信息；粘度给尺寸（V_h）与溶剂品质（a）",
 src="p.7 与 p.13–15 综合"),
]
