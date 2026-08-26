# -*- coding: utf-8 -*-
LEC = 6
TITLE = "Light Scattering and Dynamic Light Scattering"
CN = "光散射与动态光散射"
SRC = "讲义 Lectures_5-7"
L = [
dict(kind="理解", topic="光散射的微观机理", ans=2,
 stem="What physically happens when light is scattered by a molecule?",
 opts=["The photon is absorbed and re-emitted at a longer wavelength",
       "The molecule is ionized", 
       "The electric field <b>polarizes the electron cloud</b>, creating an oscillating dipole that re-radiates in all directions",
       "The molecule rotates and emits heat"],
 exp="""<p>讲义描述的链条：<br>
① 光是电磁波，电场垂直于传播方向振荡<br>
② 电场与分子作用，<b>极化电子云</b>，产生一个<b>同频率振荡的偶极矩 μ</b><br>
③ 这个偶极<b>向各个方向再辐射</b>电场<br>
④ 这就是光散射</p>
<p class="trap"><b>散射不是吸收</b>：散射光与入射光<b>频率相同</b>（弹性），没有能量损失。
这与紫外吸收（电子跃迁到激发态）是完全不同的过程。</p>""",
 kp="散射 = 电子云被极化产生振荡偶极再辐射；弹性、不改变频率",
 src="p.20「Light Scattering」"),

dict(kind="计算", topic="Rayleigh 方程", ans=1,
 stem="In Rayleigh's equation I<sub>θ</sub>/I₀ = 8π⁴α²(1+cos²θ)/(λ⁴r²), the scattered intensity depends on wavelength as:",
 opts=["λ⁻¹", "<b>λ⁻⁴</b>", "λ⁻²", "λ⁺⁴"],
 exp="""<div class="fb">I<sub>θ</sub>/I₀ = 8π⁴α²(1 + cos²θ) / (λ⁴ r²)</div>
<p>各符号：α 极化率，θ 散射角，λ 波长，r 检测器距离。</p>
<p><b>λ⁻⁴</b> 是最重要的依赖关系——<b>短波长被散射得强烈得多</b>。</p>
<p class="trap"><b>四次方的威力</b>：紫光（400 nm）与红光（700 nm）之比是
(700/400)⁴ = <b>9.4 倍</b>。这就是天空呈蓝色的原因。</p>""",
 kp="Rayleigh: I ∝ α²(1+cos²θ)/(λ⁴r²)；λ⁻⁴ 是核心",
 src="p.20「Using Rayleigh's Equation」"),

dict(kind="计算", topic="λ⁻⁴ 的定量应用", ans=2,
 stem="What is the ratio of scattered intensity for 400 nm light to that for 700 nm light from the same small particle?",
 opts=["1.75", "3.06", "9.38", "5.35"],
 exp="""<div class="fb">I<sub>400</sub>/I<sub>700</sub> = (700/400)⁴ = (1.75)⁴</div>
<p>(1.75)² = 3.0625；(3.0625)² = <b>9.38</b></p>
<p class="trap"><b>三个错误选项对应三种失误</b>：<br>
· 1.75 = 只算了一次方<br>
· 3.06 = 只算了二次方<br>
· 5.35 = 三次方</p>
<p><b>注意方向</b>：<b>短波长在分子上</b>——400 nm 被散射得更强，所以比值 &gt; 1。</p>""",
 kp="比值要取四次方；短波长散射强，比值分子放短波长",
 src="p.20–21「Rayleigh Scattering」"),

dict(kind="理解", topic="天空为什么是蓝的", ans=3,
 stem="Why is the sky blue?",
 opts=["Non-blue light gets absorbed by water vapour, leaving blue in the sky",
       "Blue light is reflected off the ocean water",
       "Non-blue light is scattered strongly by air molecules, leaving blue light in the sky",
       "<b>Blue light is scattered strongly by air molecules, causing the sky to appear blue</b>"],
 exp="""<p>讲义给的解释：<i>“<b>Blue light</b> from the sun, due to a <b>shorter wavelength</b>, is
<b>scattered more strongly</b> by air molecules than light of other colours. Since we view the sky
<b>away from the sun</b>, we see the blue scattered light and the sky appears blue.”</i></p>
<p class="trap"><b>选项 C 是最刁钻的干扰项</b>——它把散射方向搞反了。
"非蓝光被强散射掉、剩下蓝光"描述的是<b>直视太阳</b>的情形
（那正是<b>日落发红</b>的原因：蓝光沿途被散射走了，直射光剩下红）。</p>
<p><b>看天空 = 看侧向散射光 → 蓝；看落日 = 看透射光 → 红。</b>同一个 λ⁻⁴，两种现象。</p>""",
 kp="蓝光被强散射；看天空是侧向散射光（蓝），看落日是透射光（红）",
 src="官方 Question 22（对应 p.20–21）"),

dict(kind="理解", topic="散射的角度对称性", ans=1,
 stem="For a <b>small</b> particle, the factor (1 + cos²θ) means the scattering pattern is:",
 opts=["Strongest at 90°", "<b>Symmetric</b> between forward and backward directions",
       "Only in the forward direction", "Independent of angle"],
 exp="""<p>cos²θ 对 θ 和 180°−θ 取值相同，所以 (1+cos²θ) 在<b>前向（θ=0°）和后向（θ=180°）相等</b>，
都等于 2；在 90° 处最小，等于 1。<b>整体前后对称。</b></p>
<p class="trap"><b>这个对称性只对小粒子成立</b>。当粒子 <b>&gt; λ/20</b> 时，
同一粒子不同部位的散射光发生<b>相消干涉</b>，散射变得<b>不对称</b>——
正是这个不对称性让我们能测出 <b>R<sub>g</sub></b>。</p>""",
 kp="小粒子散射前后对称；大粒子因干涉而不对称，由此可测 Rg",
 src="p.20「(1 + cos²θ)」；p.24「asymmetrical」"),

dict(kind="理解", topic="极化率与折射率", ans=0,
 stem="The polarizability α is related to refractive index through the Lorentz–Lorenz equation. After substituting n = n₀ + (dn/dc)c and neglecting second-order terms, α becomes proportional to:",
 opts=["n₀ (dn/dc) c", "n₀² c", "(dn/dc)² ", "1/λ⁴"],
 exp="""<p>Lorentz–Lorenz：α ≈ (n² − n₀²)/(4π) · (V/N)</p>
<p>代入 n = n₀ + (dn/dc)c 并展开：n² ≈ n₀² + 2n₀(dn/dc)c（丢掉二次项），故</p>
<div class="fb">α = [n₀ c / (2π)] · (dn/dc) · (V/N)</div>
<p>因为 <b>I ∝ α²</b>，所以散射强度 <b>∝ (dn/dc)²</b> ——这就是为什么 dn/dc 在光散射中如此关键。</p>""",
 kp="α ∝ n₀(dn/dc)c；因 I ∝ α²，故散射强度 ∝ (dn/dc)²",
 src="p.21「Lorentz–Lorenz equation」"),

dict(kind="理解", topic="如何提高 dn/dc", ans=2,
 stem="How can dn/dc be made large, to maximize light scattering intensity?",
 opts=["Increase the refractive index of the solvent", "Decrease the refractive index of the solvent",
       "Choose a solvent whose refractive index <b>differs strongly</b> from that of the polymer",
       "Increase the concentration of the polymer solution"],
 exp="""<p>讲义给的答案：<i>“The greater the <b>difference in refractive index between the polymer and
the solvent</b>, the more the overall refractive index will vary with polymer concentration,
i.e. higher dn/dc.”</i></p>
<p class="trap"><b>为什么 A、B 都不对</b>：单纯升高或降低溶剂折射率没有意义——
关键是与<b>高分子</b>的<b>差值</b>。若溶剂折射率正好等于高分子，dn/dc = 0，<b>完全看不到散射</b>
（这正是"折射率匹配法"让物体隐形的原理）。</p>
<p><b>D 也不对</b>：dn/dc 是<b>斜率</b>，是材料对的固有性质，与实际浓度无关。
提高浓度确实增大 I（因为 I ∝ c），但没有改变 dn/dc。</p>""",
 kp="dn/dc 取决于高分子与溶剂的折射率之差；差越大信号越强",
 src="官方 Question 23（对应 p.21、p.26）"),

dict(kind="理解", topic="光学常数 K", ans=1,
 stem="The optical constant K = 2π²n₀²(dn/dc)²/(λ⁴N<sub>Av</sub>) is introduced in order to:",
 opts=["Account for the polymer's molecular weight",
       "Collect all the <b>instrument and material constants</b> into one symbol, simplifying the working equation",
       "Convert mole fraction to volume fraction", "Correct for temperature"],
 exp="""<div class="fb">K = 2π² n₀² (dn/dc)² / (λ⁴ N<sub>Av</sub>)</div>
<p>K 里装的全是<b>与样品分子量无关</b>的量：溶剂折射率 n₀、折射率增量 dn/dc、
激光波长 λ。定义了 K 之后，Rayleigh 方程简化成：</p>
<div class="fb">I<sub>θ</sub>/I₀ = K c M<sub>w</sub> (1 + cos²θ)/r²</div>
<p>剩下的<b>只有 c 和 M<sub>w</sub></b>——实验上测 I、已知 c，就能解出 M<sub>w</sub>。</p>""",
 kp="K 打包所有仪器与材料常数，使工作方程只剩 c 与 Mw", src="p.22「optical constant K」"),

dict(kind="理解", topic="高分子溶液的散射式", ans=1,
 stem="For polymer solutions (small M<sub>w</sub>), M<sub>w</sub> in the scattering equation is replaced by:",
 opts=["M<sub>w</sub> + 2Bc", "1/(1/M<sub>w</sub> + 2Bc + ⋯)", "M<sub>w</sub>·(1 + 2Bc)", "M<sub>w</sub>/2Bc"],
 exp="""<div class="fb">I<sub>θ</sub>/I₀ = Kc (1+cos²θ)/r² × <b>1/(1/M<sub>w</sub> + 2Bc + ⋯)</b></div>
<p>其中 <b>B 正是渗透压方程里的第二维里系数</b>——讲义明确写着
<i>“containing the virial coefficient in osmotic pressure equation”</i>。</p>
<p class="trap"><b>这不是巧合</b>：两种方法测的都是溶液的<b>浓度涨落</b>。
渗透压直接测化学势对浓度的响应；光散射测浓度涨落的均方大小
（基于 Smoluchowski 和 Einstein 的涨落理论）。<b>同一个 B 出现在两处。</b></p>
<p><b>实验做法</b>：取倒数得 Kc/R<sub>θ</sub> = 1/M<sub>w</sub> + 2Bc，
作图对 c 外推到 <b>c → 0</b>，截距给 1/M<sub>w</sub>、斜率给 2B。</p>""",
 kp="光散射与渗透压共用同一个第二维里系数 B；作图外推 c→0 取截距",
 src="p.23「Rayleigh Scattering for Small Mw Polymer Solutions」"),

dict(kind="理解", topic="大粒子的干涉效应", ans=2,
 stem="When a particle is larger than about λ/20, what happens to the scattered light?",
 opts=["It is absorbed", "It shifts to longer wavelength",
       "Waves scattered from different parts of the <b>same</b> particle interfere <b>destructively</b>, reducing the net intensity",
       "It becomes completely polarized"],
 exp="""<p>讲义原文：<i>“When a light wave scatter off different parts of the <b>same particle</b>,
the scattered waves are mostly <b>out of phase</b> and <b>destructive interference</b> occurs.
This causes a <b>net reduction</b> of scattered intensity, depending on angle.”</i></p>
<p><b>后果</b>：<br>
· 散射曲线变得<b>不对称</b>：<b>前向散射 &gt; 后向散射</b><br>
· <b>唯一不受影响的角度是 θ = 0°</b>（此时各部分的光程差为零，无相位差）</p>
<p class="trap"><b>这个"缺陷"恰恰是信息来源</b>：干涉的强弱取决于粒子尺寸与波长之比，
所以从<b>角度依赖</b>可以反推出 <b>R<sub>g</sub></b>。</p>""",
 kp="大粒子内部相消干涉 → 前向>后向、θ=0 不受影响 → 由角度依赖测 Rg",
 src="p.24「Light Scattering for Larger Particles」"),

dict(kind="计算", topic="散射矢量 q", ans=1,
 stem="The scattering vector is q = (4πn/λ)sin(θ/2). At what angle does q vanish?",
 opts=["θ = 90°", "<b>θ = 0°</b>", "θ = 180°", "q never vanishes"],
 exp="""<p>sin(θ/2) = 0 当且仅当 θ = 0°。</p>
<p><b>物理意义</b>：在大粒子的散射式中</p>
<div class="fb">1/M<sub>w</sub> · (1 + q²R<sub>g</sub>²/3 + ⋯)</div>
<p>q → 0 时修正项消失，回到<b>不受干涉影响</b>的理想结果——
这与讲义说的"唯一不受影响的角度是 θ = 0°"<b>完全吻合</b>。</p>
<p class="trap"><b>实验做法</b>：θ = 0° 处无法测量（会被入射光淹没），
所以要在<b>多个角度</b>测量后<b>外推到 θ → 0</b>。
这就是 <b>Zimm 图</b>的由来——同时对 c → 0 和 θ → 0 双重外推。</p>""",
 kp="q = (4πn/λ)sin(θ/2)；θ→0 时 q→0，修正项消失，需外推",
 src="p.25「scattering vector」"),

dict(kind="计算", topic="q 的数值计算", ans=1,
 stem="For λ = 633 nm, solvent n = 1.33, and θ = 90°, what is q?",
 opts=["1.32×10⁷ m⁻¹", "1.87×10⁷ m⁻¹", "2.64×10⁷ m⁻¹", "9.35×10⁶ m⁻¹"],
 exp="""<div class="fb">q = (4πn/λ) sin(θ/2)</div>
<p>4πn/λ = 4 × 3.1416 × 1.33 / (633×10⁻⁹) = 16.713 / 6.33×10⁻⁷ = 2.640×10⁷ m⁻¹</p>
<p>sin(90°/2) = sin45° = 0.7071</p>
<p>q = 2.640×10⁷ × 0.7071 = <b>1.87×10⁷ m⁻¹</b></p>
<p class="trap"><b>陷阱</b>：选项 C 是忘了乘 sin(θ/2)。注意公式里是 <b>θ/2</b> 不是 θ
——与 Bragg 定律"题目给 2θ、公式用 θ"是同一类陷阱。</p>
<p><b>量级感</b>：1/q ≈ 53 nm，这正是光散射能分辨的尺寸尺度。</p>""",
 kp="q 计算注意 sin(θ/2)；1/q 给出可分辨的尺寸尺度", src="p.25「q = (4πn/λ)sin(θ/2)」"),

dict(kind="理解", topic="光散射测 Mw 的原因", ans=1,
 stem="Static light scattering measures M<sub>w</sub> rather than M<sub>n</sub> because:",
 opts=["Large molecules are easier to see",
       "The scattering by each particle is <b>weighted relative to its mass</b>",
       "Small molecules do not scatter at all", "The detector saturates for small molecules"],
 exp="""<p>讲义原文：<i>“light scattering measures <b>weight average</b> molecular weight (M<sub>w</sub>)
and not M<sub>n</sub> — because the scattering by each particle is <b>weighted relative to its mass</b>.”</i></p>
<p><b>数学根源</b>：散射强度 I ∝ c·M。总散射 = Σ c<sub>i</sub>M<sub>i</sub> ∝ Σ n<sub>i</sub>M<sub>i</sub>²，
再除以总浓度 Σ n<sub>i</sub>M<sub>i</sub>，正好是 <b>M<sub>w</sub> 的定义</b>。</p>
<p class="trap"><b>与渗透压对照记忆</b>：<br>
· 渗透压——每个分子贡献<b>相同</b>（数个数）→ <b>M<sub>n</sub></b><br>
· 光散射——每个分子按<b>质量</b>贡献 → <b>M<sub>w</sub></b></p>""",
 kp="散射按质量加权 → Mw；与渗透压按个数 → Mn 形成对照",
 src="p.26「Light Scattering Experiments」"),

dict(kind="理解", topic="光散射实验的三个要求", ans=3,
 stem="Which is <b>NOT</b> a stated requirement for a reliable light scattering experiment?",
 opts=["Samples should be dust-free", "Concentration should be low so particles scatter independently",
       "dn/dc should be as large as possible", "The solution must be at its theta temperature"],
 exp="""<p>讲义列出的三条要求：<br>
① <i>“Solution samples should be <b>dust-free</b>!”</i>——灰尘颗粒比高分子大得多，散射强度以尺寸的高次方增长，一粒灰就能淹没信号<br>
② <i>“Concentration should be <b>low</b> such that particles behave as <b>independent scatterers</b>”</i><br>
③ <i>“<b>dn/dc</b> should be as large as possible to get highest signal strength”</i></p>
<p><b>D 不是要求</b>——θ 条件是溶液热力学的一个特殊状态，光散射在任何溶剂中都能做。
实际上人们常<b>刻意避开</b> θ 条件，因为 θ 溶剂中 B = 0 反而损失了溶剂品质的信息。</p>""",
 kp="三条要求：无尘、低浓度、大 dn/dc", src="p.26「Light Scattering Experiments」"),

dict(kind="理解", topic="静态与动态光散射的区别", ans=1,
 stem="The essential difference between static and dynamic light scattering is that DLS measures:",
 opts=["The time-averaged intensity", "The <b>temporal fluctuations</b> of the scattered intensity",
       "The wavelength shift", "The polarization state"],
 exp="""<p>讲义原文：<br>
· <b>静态</b>：<i>“we obtain a <b>time-average intensity</b> of scattered light to determine M<sub>w</sub> and R<sub>g</sub>”</i><br>
· <b>动态</b>：<i>“we detect the <b>temporal fluctuations</b> in the scattered light intensity, and use this
information to determine the <b>hydrodynamic radius (R<sub>h</sub>)</b>”</i></p>
<table class="mini"><thead><tr><th></th><th>测什么</th><th>给出</th></tr></thead><tbody>
<tr><td><b>静态 SLS</b></td><td>强度的<b>平均值</b>（及角度依赖）</td><td><b>M<sub>w</sub></b>、<b>R<sub>g</sub></b></td></tr>
<tr><td><b>动态 DLS</b></td><td>强度的<b>涨落快慢</b></td><td><b>R<sub>h</sub></b></td></tr>
</tbody></table>
<p class="trap"><b>DLS 不给分子量</b>——这是极高频的考点。</p>""",
 kp="SLS 测平均强度 → Mw、Rg；DLS 测涨落快慢 → Rh（不给分子量）",
 src="p.28「Dynamic Light Scattering (DLS) Principles」"),

dict(kind="理解", topic="涨落的来源", ans=2,
 stem="Why does the scattered intensity fluctuate in time in a DLS experiment?",
 opts=["The laser power fluctuates", "The temperature oscillates",
       "Scattered waves from randomly moving particles <b>interfere</b>, and as the particles move the bright and dark regions move",
       "The detector is noisy"],
 exp="""<p>讲义原文：<i>“Scattered light waves from random particles <b>interfere</b> to give brighter and darker regions.
As the particles <b>move about</b>, the bright and dark regions <b>also move</b>.
The <b>rate</b> that the brightness fluctuates is related to the <b>speed of particle movement</b>,
which is in turn related to the <b>'size'</b> of the particle.”</i></p>
<p><b>完整逻辑链</b>：布朗运动 → 干涉图样移动 → 强度涨落 → 涨落速率 ∝ 粒子运动速度 ∝ 1/尺寸</p>""",
 kp="涨落源于运动粒子的干涉图样移动；涨落速率反映粒子运动快慢",
 src="p.28「DLS Principles」"),

dict(kind="理解", topic="小粒子涨落更快", ans=0,
 stem="Will the scattered light intensity fluctuate <b>faster</b> or <b>slower</b> for small dissolved polymer particles compared with large ones?",
 opts=["<b>Faster</b> for small particles", "Slower for small particles",
       "The same for both", "It depends on the solvent"],
 exp="""<p>讲义给的答案：<i>“Because small particles <b>diffuse faster</b> in solution and causes
<b>faster changes</b> in scattered light intensity.”</i></p>
<p><b>定量依据</b>是 Stokes-Einstein：</p>
<div class="fb">D<sub>t</sub> = kT / (6πη<sub>s</sub>R<sub>h</sub>)　→　<b>D ∝ 1/R<sub>h</sub></b></div>
<p>粒子越小 → D 越大 → 扩散越快 → 干涉图样变化越快 → <b>自相关函数衰减越快</b>。</p>
<p class="trap"><b>DLS 的全部信息就在"衰减有多快"里</b>——衰减快 = 小粒子，衰减慢 = 大粒子。</p>""",
 kp="小粒子 D 大、扩散快、涨落快、自相关衰减快", src="官方 Question 24（对应 p.28、p.31）"),

dict(kind="理解", topic="自相关函数的定义", ans=0,
 stem="The time autocorrelation function is C(t′) = (1/T)∫₀ᵀ I<sub>s</sub>(t)·I<sub>s</sub>(t+t′)dt. What does the operation do?",
 opts=["Multiplies the intensity trace by a copy of <b>itself shifted by t′</b>, then averages over time",
       "Differentiates the intensity with respect to time",
       "Takes the Fourier transform of the intensity", "Computes the total scattered energy"],
 exp="""<p>讲义的操作步骤：<br>
① 把 I<sub>s</sub> 的曲线与<b>它自己平移 t′ 后</b>的曲线相乘<br>
② 在选定的时间范围 T 上<b>积分</b><br>
③ 除以 T（使结果不依赖 T 的选取）<br>
④ 对不同的 t′ 重复</p>
<p><b>为什么这样做有用</b>：把 I<sub>s</sub> 写成 ⟨I<sub>s</sub>⟩ + δI<sub>s</sub> 展开后，
交叉项 ⟨I<sub>s</sub>⟩δI<sub>s</sub> <b>平均为零</b>，只剩</p>
<div class="fb">C(t′) = ⟨I<sub>s</sub>⟩² + (1/T)∫ δI<sub>s</sub>(t) δI<sub>s</sub>(t+t′) dt</div>
<p>第二项正是我们要的<b>涨落的记忆</b>。</p>""",
 kp="自相关 = 曲线与自身平移版相乘再平均；交叉项平均为零，只剩涨落项",
 src="p.29–30「Tracking Time Decay of Intensity Fluctuation」"),

dict(kind="理解", topic="自相关函数的两个极限", ans=1,
 stem="What are the limiting values of C(t′) at t′ = 0 and t′ → ∞?",
 opts=["Zero at t′ = 0; large at t′ → ∞",
       "<b>Large at t′ = 0</b> (curve multiplied by itself); decays to <b>⟨I<sub>s</sub>⟩²</b> at t′ → ∞",
       "Both are zero", "Both equal ⟨I<sub>s</sub>⟩²"],
 exp="""<p>讲义的两个极端情形：<br>
· <b>t′ = 0</b>：δI<sub>s</sub>(t) 与 δI<sub>s</sub>(t+t′) <b>完全相同</b>，乘积恒为正（平方），平均值<b>大</b><br>
· <b>t′ → ∞</b>：两者<b>毫不相关</b>，乘积正负各半，平均<b>为 0</b>，只剩基线 ⟨I<sub>s</sub>⟩²</p>
<div class="fb">C(t′) = (⟨I<sub>s</sub>²⟩ − ⟨I<sub>s</sub>⟩²) exp(−2q²D<sub>m</sub>t′) + ⟨I<sub>s</sub>⟩²</div>
<p>即从高处<b>指数衰减</b>到基线。<b>衰减速率 = 2q²D<sub>m</sub></b>。</p>""",
 kp="C(t′) 由高值指数衰减到基线 ⟨I⟩²，速率 2q²D_m",
 src="p.30–31「Imagine 2 extreme scenarios」"),

dict(kind="理解", topic="扩散系数与衰减速率", ans=0,
 stem="In C(t′) ∝ exp(−2q²D<sub>m</sub>t′), a <b>higher</b> diffusion coefficient gives:",
 opts=["<b>Faster</b> decay of the correlation function", "Slower decay",
       "No change in decay rate", "An oscillating correlation function"],
 exp="""<p>讲义原文：<i>“The <b>higher</b> the diffusion coefficient, the <b>faster the decay</b>.”</i></p>
<p>指数中 D<sub>m</sub> 越大 → 指数下降越陡 → 相关性"忘得"越快。</p>
<p><b>整条推理链（必须能背下来）</b>：</p>
<div class="fb">小粒子 → D 大 → 衰减快 ⟷ 大粒子 → D 小 → 衰减慢</div>
<p><b>实验流程</b>：作 C(t′) vs t′ 图 → 拟合指数得 D<sub>m</sub> → 外推 c→0 得 D<sub>t</sub>
→ Stokes-Einstein 得 R<sub>h</sub>。</p>""",
 kp="D 越大衰减越快；实验流程 C(t′) → D_m → D_t → R_h",
 src="p.31「The higher the diffusion coefficient, the faster the decay」"),

dict(kind="理解", topic="Dm 与 Dt 的区别", ans=1,
 stem="What is the difference between the mutual diffusion coefficient D<sub>m</sub> and the tracer diffusion coefficient D<sub>t</sub>?",
 opts=["D<sub>m</sub> is for a single particle; D<sub>t</sub> is for a collection",
       "D<sub>m</sub> is for a <b>collection</b> of particles; D<sub>t</sub> is for a <b>single</b> particle, obtained by extrapolating D<sub>m</sub> to zero concentration",
       "They are identical", "D<sub>t</sub> depends on the scattering angle"],
 exp="""<p>讲义定义：<br>
· <b>D<sub>m</sub></b>：mutual diffusion coefficient，<i>“diffusion of a <b>collection</b> of particles”</i><br>
· <b>D<sub>t</sub></b>：tracer diffusion coefficient，<i>“diffusion of a <b>single</b> particle”</i></p>
<div class="fb">lim<sub>c→0</sub> D<sub>m</sub> = D<sub>t</sub> = kT/(6πη<sub>s</sub>R<sub>h</sub>)</div>
<p><b>为什么必须外推</b>：有限浓度下粒子之间有流体力学相互作用和热力学耦合，
D<sub>m</sub> 依赖浓度。只有<b>无限稀释</b>时粒子才真正独立，Stokes-Einstein 才严格成立。</p>
<p class="trap">讲义还建议<i>“Measurements could be taken at several angles to improve results reliability”</i>
——多角度测量交叉验证。</p>""",
 kp="D_m（集体）外推到 c→0 得 D_t（单粒子），才能用 Stokes-Einstein",
 src="p.31「Dm values should be taken at low concentrations」"),

dict(kind="计算", topic="Stokes-Einstein 求 Rh", ans=1,
 stem="A particle in water (η<sub>s</sub> = 1.00×10⁻³ Pa·s) at 293 K has D<sub>t</sub> = 5.0×10⁻¹² m²/s. What is R<sub>h</sub>?",
 opts=["4.3 nm", "43 nm", "430 nm", "4.3 μm"],
 exp="""<div class="fb">R<sub>h</sub> = kT / (6π η<sub>s</sub> D<sub>t</sub>)</div>
<p>分子：kT = 1.381×10⁻²³ × 293 = <b>4.046×10⁻²¹ J</b></p>
<p>分母：6π × 1.00×10⁻³ × 5.0×10⁻¹² = 18.85 × 5.0×10⁻¹⁵ = <b>9.425×10⁻¹⁴</b></p>
<p>R<sub>h</sub> = 4.046×10⁻²¹ / 9.425×10⁻¹⁴ = 4.29×10⁻⁸ m = <b>43 nm</b></p>
<p class="trap"><b>量级自查</b>：高分子的 R<sub>h</sub> 通常在<b>几 nm 到几百 nm</b>。
算出 4.3 μm 说明差了 100 倍，多半是单位错了。</p>""",
 kp="R_h = kT/(6πη D)；高分子 R_h 典型量级为 nm–百 nm",
 src="p.31「Stokes-Einstein Relation」"),

dict(kind="计算", topic="布朗运动与扩散系数", ans=1,
 stem="A particle undergoes Brownian motion, taking N steps of length l in time t. If D<sub>t</sub> is defined as the mean-square distance from the origin divided by 6×time, then D<sub>t</sub> =",
 opts=["N l / (6t)", "<b>N l² / (6t)</b>", "N² l / (6t)", "N² l² / (6t)"],
 exp="""<p><b>关键在于均方位移</b>。这与 Lecture 1 的末端距<b>是同一个数学问题</b>：
N 步随机行走，每步长 l，均方位移</p>
<div class="fb">⟨r²⟩ = N l²</div>
<p>（交叉项因方向随机而平均为零——与 ⟨h²⟩ = nl² 的推导<b>一模一样</b>）</p>
<p>按定义 D<sub>t</sub> = ⟨r²⟩/(6t) = <b>N l²/(6t)</b></p>
<p class="trap"><b>陷阱</b>：选项 A 用了 l 的一次方。<b>必须是 l²</b>——因为求的是<b>均方</b>位移。
讲义明确提示：<i>“Derivation can be found in lecture on polymer <b>end-to-end distance</b>”</i>。</p>
<p><b>这题是全课最漂亮的呼应</b>：高分子链在<b>空间</b>中的随机行走，
与粒子在<b>时间</b>中的随机行走，是同一个 √N 定律。</p>""",
 kp="⟨r²⟩ = Nl²（与 ⟨h²⟩ = nl² 同源）；D_t = Nl²/6t",
 src="官方 Question 25（对应 p.31 与 L1 p.10）"),

dict(kind="理解", topic="Rg 与 Rh 的区别", ans=2,
 stem="For the same polymer sample, R<sub>g</sub> and R<sub>h</sub> are:",
 opts=["Always exactly equal", "R<sub>h</sub> is always much larger than R<sub>g</sub>",
       "<b>Different quantities</b>: R<sub>g</sub> is a mass distribution measure (from SLS), R<sub>h</sub> is an equivalent hard-sphere radius for diffusion (from DLS)",
       "R<sub>g</sub> can only be measured by DLS"],
 exp="""<table class="mini"><thead><tr><th></th><th>R<sub>g</sub></th><th>R<sub>h</sub></th></tr></thead><tbody>
<tr><td>定义</td><td>单体到质心的 RMS 距离</td><td>扩散上等效硬球的半径</td></tr>
<tr><td>测法</td><td><b>静态</b>光散射（角度依赖）</td><td><b>动态</b>光散射（涨落）</td></tr>
<tr><td>物理</td><td>质量<b>如何分布</b></td><td>拖着溶剂<b>怎么动</b></td></tr>
</tbody></table>
<p><b>比值 R<sub>g</sub>/R<sub>h</sub> 本身就是形状指纹</b>：<br>
· 理想线团 ≈ 1.5　· 致密硬球 ≈ 0.775　· 刚性棒 &gt; 2</p>
<p class="trap"><b>DLS 给的是 R<sub>h</sub>，不是 R<sub>g</sub>，也不是分子量。</b>
这三点是最容易被考的混淆处。</p>""",
 kp="Rg（SLS，质量分布）与 Rh（DLS，扩散等效球）是不同的量；比值反映形状",
 src="p.13（L1）、p.25 与 p.28、p.31 综合"),

dict(kind="理解", topic="散射与折射率不均", ans=1,
 stem="A polymer solution scatters light strongly. If a second solvent is chosen whose refractive index exactly matches the polymer's, the scattering will:",
 opts=["Increase", "Essentially <b>vanish</b>, since dn/dc → 0", "Be unchanged", "Become wavelength-independent"],
 exp="""<p>散射强度 <b>I ∝ (dn/dc)²</b>。若溶剂与高分子折射率完全匹配，
溶液的折射率<b>不随浓度变化</b> → dn/dc = 0 → <b>I → 0</b>，样品在光学上"消失"。</p>
<p class="trap"><b>这条原理在本课出现了三次</b>：<br>
· <b>L6</b>：折射率差越大，dn/dc 越大，散射越强<br>
· <b>L8</b>：玻璃态高分子折射率均一 → <b>透明</b>；半结晶体晶区/非晶区折射率不同 → <b>发白</b><br>
· <b>L9</b>：银纹产生 10–20 nm 微孔洞，与高分子折射率差极大 → <b>应力发白</b></p>
<p><b>一句话</b>：<b>光散射的根源永远是折射率的不均匀。</b></p>""",
 kp="I ∝ (dn/dc)²；折射率匹配则不散射。这条贯穿 L6/L8/L9",
 src="p.21、p.26；p.4（L8）；p.22（L9）"),

dict(kind="计算", topic="散射强度的浓度依赖", ans=0,
 stem="In the dilute limit (neglecting the 2Bc term), how does the scattered intensity depend on concentration c and molecular weight M<sub>w</sub>?",
 opts=["I ∝ c·M<sub>w</sub>", "I ∝ c²·M<sub>w</sub>", "I ∝ c/M<sub>w</sub>", "I ∝ M<sub>w</sub> only"],
 exp="""<div class="fb">I<sub>θ</sub>/I₀ = K c M<sub>w</sub> (1+cos²θ)/r²</div>
<p><b>I ∝ c·M<sub>w</sub></b>——浓度和分子量都是一次方。</p>
<p><b>实用推论</b>：同样质量浓度下，<b>分子量越大信号越强</b>。
所以光散射对<b>高分子量组分特别敏感</b>——这既是它测 M<sub>w</sub> 的原因，
也是它对<b>微量聚集体或灰尘极其敏感</b>的原因（一粒灰的"分子量"是天文数字）。</p>
<p class="trap">这正好解释了讲义那条要求：<b>"Solution samples should be dust-free!"</b>——
不是洁癖，是物理必然。</p>""",
 kp="I ∝ c·Mw；对高分子量组分极敏感，故必须除尘",
 src="p.22「= K c Mw (1+cos²θ)/r²」；p.26"),

dict(kind="理解", topic="Rayleigh 散射用于气体", ans=1,
 stem="When Rayleigh's equation is applied to a <b>gas</b>, the background refractive index n₀ is taken as:",
 opts=["1.33", "<b>1</b> (vacuum)", "The gas's own refractive index", "Zero"],
 exp="""<p>讲义原文：<i>“For a sample of gas molecules, <b>n₀ (background refractive index) is simply 1</b>,
and M<sub>w</sub> is the molar mass of the molecule.”</i></p>
<p><b>为什么</b>：气体分子稀疏地分布在<b>真空</b>背景里，真空折射率 = 1。</p>
<p class="trap"><b>与溶液的关键差别</b>：高分子溶液中，散射是<b>相对于溶剂背景</b>发生的，
所以要用<b>溶剂的折射率 n<sub>s</sub></b>。讲义在溶液公式里明确写着
<i>“where n<sub>s</sub> is <b>solvent</b> refractive index”</i>。</p>
<p><b>物理含义</b>：只有<b>折射率的差异</b>才产生散射——溶液里"看得见"高分子，
是因为它与溶剂折射率不同，而不是因为它本身有折射率。</p>""",
 kp="气体背景 n₀ = 1（真空）；溶液背景用溶剂折射率 n_s",
 src="p.22「n₀ is simply 1」；p.23「n_s is solvent refractive index」"),

dict(kind="理解", topic="Smoluchowski-Einstein 涨落理论", ans=2,
 stem="The polymer-solution scattering expression is derived based on theories of Smoluchowski and Einstein concerning:",
 opts=["Chemical reaction rates", "Crystal lattice vibrations",
       "<b>Particle (concentration) fluctuations</b>", "Quantum electrodynamics"],
 exp="""<p>讲义原文：<i>“Based on theories of Smoluchowski and Einstein on <b>particle fluctuations</b>,
the following expression could be derived.”</i></p>
<p><b>核心思想的转变</b>：在溶液中，散射<b>不是</b>来自单个分子的独立贡献，
而是来自<b>局部浓度涨落</b>造成的折射率不均匀。</p>
<p class="trap"><b>这解释了两件事</b>：<br>
① 为什么<b>渗透压的第二维里系数 B</b> 会出现在散射公式里——
B 描述溶液抵抗浓度涨落的能力，涨落越难发生（B 越大），散射越弱<br>
② 为什么<b>完全均匀的介质不散射</b>——没有涨落就没有折射率不均</p>""",
 kp="溶液散射源于浓度涨落（Smoluchowski-Einstein），故与渗透压的 B 相连",
 src="p.23「theories of Smoluchowski and Einstein on particle fluctuations」"),

dict(kind="理解", topic="选择合适的表征方法", ans=1,
 stem="A researcher has a polymer sample and needs M<sub>w</sub>, R<sub>g</sub> <b>and</b> R<sub>h</sub>. The minimum set of techniques is:",
 opts=["Osmometry alone", "<b>Static light scattering (multi-angle) plus dynamic light scattering</b>",
       "Viscometry alone", "MALDI-TOF alone"],
 exp="""<p><b>多角度静态光散射</b>一次给两个量：<br>
· 外推 c→0、θ→0 得<b>截距</b> → <b>M<sub>w</sub></b><br>
· 角度依赖的<b>斜率</b> → <b>R<sub>g</sub></b></p>
<p><b>动态光散射</b>给 <b>R<sub>h</sub></b>。</p>
<p class="trap"><b>为什么其他选项不行</b>：<br>
· 渗透压只给 M<sub>n</sub>，<b>无任何尺寸信息</b>（依数性）<br>
· 粘度给 [η]（间接反映 V<sub>h</sub>），但<b>需要标定</b>，且不直接给 R<sub>g</sub><br>
· MALDI 给分子量分布，但<b>不给溶液中的尺寸</b></p>
<p><b>现代仪器通常把 SLS + DLS 集成在一台机器上</b>，一次进样同时得到三个量。</p>""",
 kp="多角度 SLS 给 Mw + Rg；DLS 补 Rh。渗透压与 MALDI 不给溶液尺寸",
 src="p.25–26、p.28、p.31 综合"),
]

L.append(dict(kind="理解", topic="为什么必须低浓度", ans=1,
 stem="Why must light scattering measurements be made at <b>low</b> concentration?",
 opts=["To avoid heating the sample",
       "So that particles behave as <b>independent scatterers</b>, and so the 2Bc correction term stays small",
       "To prevent the polymer from crystallizing", "To keep the laser from saturating"],
 exp="""<p>讲义要求：<i>“Concentration should be low such that particles behave as
<b>independent scatterers</b>.”</i></p>
<p><b>两层原因</b>：</p>
<p>① <b>物理上</b>：浓度高时链彼此重叠、相互干涉，散射不再是各分子贡献的简单加和，
Rayleigh 的推导前提失效。</p>
<p>② <b>数学上</b>：工作方程里的 <b>2Bc</b> 修正项随浓度增大，
使 Kc/R<sub>θ</sub> 对 c 的关系偏离线性：</p>
<div class="fb">Kc/R<sub>θ</sub> = 1/M<sub>w</sub> + 2Bc + ⋯</div>
<p>只有在低浓度线性区，才能可靠地<b>外推到 c → 0</b> 取截距求 M<sub>w</sub>。</p>
<p class="trap"><b>光散射需要"双重外推"</b>：既要 <b>c → 0</b>（消除浓度效应），
又要 <b>θ → 0</b>（消除粒子内干涉）。把两者画在同一张图上就是 <b>Zimm 图</b>。</p>""",
 kp="低浓度保证独立散射且 2Bc 项可控；需 c→0 与 θ→0 双重外推",
 src="p.23、p.26「Concentration should be low」"))
