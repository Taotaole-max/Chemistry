# -*- coding: utf-8 -*-
LEC = 2
TITLE = "Thermodynamics of Mixtures"
CN = "混合热力学"
SRC = "讲义 Lectures_1-4"
L = [
dict(kind="理解", topic="内能的两个来源",
 stem="In dU = dq + dw, for a system that only does expansion work, the work term equals:",
 opts=["+p dV", "−p dV", "−V dp", "T dS"], ans=1,
 exp="""<p>讲义推导：dw<sub>rev</sub> = −F dx = −(F/A)×A dx = <b>−p dV</b>。</p>
<p>负号的物理含义：系统<b>膨胀</b>（dV &gt; 0）时对外做功，内能<b>下降</b>。
反过来压缩（dV &lt; 0）时外界对系统做功，内能上升。</p>
<p class="trap">注意 −V dp 是焓变里出现的项（dH = dU + p dV + V dp），别与做功混淆。</p>""",
 kp="dw_rev = −p dV；负号表示膨胀消耗内能", src="p.20「Internal Energy (U)」"),

dict(kind="理解", topic="熵的定义式",
 stem="The thermodynamic definition of entropy used in the lecture is:",
 opts=["dS = dq<sub>rev</sub> / T", "dS = k lnΩ", "dS = dU / T", "dS = −(∂G/∂p)<sub>T</sub>"], ans=0,
 exp="""<div class="fb">dS = dq<sub>rev</sub> / T　即　dq<sub>rev</sub> = T dS</div>
<p>讲义的注解是 <i>“heat stimulates disorderly motion”</i>——热量输入激发无序运动，因此增加熵。</p>
<p class="trap"><b>别混</b>：S = k lnΩ 是<b>统计</b>定义（Boltzmann 公式，p.32 才出现），
本页给的是<b>热力学</b>定义。这门课的漂亮之处在于两条路径最后给出<b>完全相同</b>的 ΔS<sub>mix</sub>。</p>""",
 kp="热力学定义 dS = dq_rev/T；统计定义 S = k lnΩ；两者殊途同归",
 src="p.20「Definition of entropy」；p.32「Boltzmann Formula」"),

dict(kind="理解", topic="热力学基本方程",
 stem="The 'Fundamental Equation' given in the lecture is:",
 opts=["dU = T dS − p dV + dw<sub>add</sub>", "dU = T dS + p dV",
       "dG = V dp − S dT", "dH = dU + p dV"], ans=0,
 exp="""<p>把 dq<sub>rev</sub> = T dS 和 dw = −p dV 代回 dU = dq + dw + dw<sub>add</sub>：</p>
<div class="fb">dU = T dS − p dV + dw<sub>add</sub></div>
<p><b>dw<sub>add</sub></b> 是"额外的非膨胀功"——包括电功，以及<b>组成变化</b>。
这一项非常关键：后面正是靠它引出<b>化学势</b>，进而推出混合的热力学。</p>""",
 kp="基本方程 dU = TdS − pdV + dw_add；dw_add 承载组成变化，是通往化学势的入口",
 src="p.20「The Fundamental Equation」"),

dict(kind="理解", topic="自发性判据的来源",
 stem="The Clausius inequality dU − T dS ≤ 0 is derived from the requirement that:",
 opts=["The system's entropy alone must increase",
       "The <b>total</b> entropy of system plus surroundings must increase",
       "The enthalpy must decrease", "The internal energy must decrease"], ans=1,
 exp="""<p>第二定律要求 <b>dS + dS<sub>sur</sub> ≥ 0</b>。若自发变化由热量 q 流入系统引起，
则环境失去 q，即 dS<sub>sur</sub> = −dq/T：</p>
<div class="fb">dS − dq/T ≥ 0　⇒　T dS ≥ dq = dU　⇒　<b>dU − T dS ≤ 0</b></div>
<p class="trap"><b>常见误解</b>：以为自发过程系统熵必须增加。<b>错</b>——
系统熵可以减少（比如结晶、橡胶被拉伸），只要环境熵增加得更多即可。</p>""",
 kp="自发性的根本判据是总熵增；Clausius 不等式是它在系统变量上的表达",
 src="p.21「Second Law of Thermodynamics – Criteria for Spontaneity」"),

dict(kind="理解", topic="焓的定义动机",
 stem="Enthalpy H = U + pV is defined so that:",
 opts=["The contributions of <b>expansion work</b> are taken out of the internal energy",
       "The contributions of entropy are removed", "It equals the heat at constant volume",
       "It is always negative"], ans=0,
 exp="""<p>讲义给的动机原话：<i>“Defined so that contributions of <b>expansion work</b> taken out of internal energy”</i>。</p>
<p>推导得 dH = dU + V dp，因此在<b>恒压</b>下 <b>dH = dq<sub>p</sub></b>——焓变就是恒压下的热量，实验上直接可测。</p>
<p><b>对照记忆</b>：Gibbs 能 G = H − TS 的动机是 <i>“contributions of <b>entropy</b> taken out of enthalpy”</i>。
两个函数都是为了"剥掉"某一部分，方便在特定条件下判断方向。</p>""",
 kp="H 剥掉膨胀功 → 恒压热；G 剥掉熵项 → 恒温恒压自发性判据",
 src="p.22「Enthalpy (H) / Gibbs Energy (G)」"),

dict(kind="理解", topic="Gibbs 能的自发性判据",
 stem="At constant temperature <b>and</b> pressure, a process is spontaneous when:",
 opts=["dU ≤ 0", "dH ≤ 0", "dG = dH − T dS ≤ 0", "dS ≤ 0"], ans=2,
 exp="""<div class="fb">dG<sub>T,p</sub> = dH − T dS ≤ 0</div>
<p>推导：由 dG = dH − T dS − S dT，恒温去掉 S dT；再由 dH = dU + p dV + V dp，恒压去掉 V dp；
代入 Clausius 不等式 dU − T dS ≤ 0 即得。</p>
<p>讲义强调：<b>恒温恒压正是化学中最常见的条件</b>，所以 ΔG 成为最常用的判据。</p>
<p class="trap"><b>两个条件缺一不可</b>：dG ≤ 0 只在<b>同时</b>恒温恒压下才是自发性判据。</p>""",
 kp="ΔG ≤ 0 是恒温恒压下的自发性判据；这正是混合热力学全篇的基础",
 src="p.23「At constant temperature / defined at constant pressure」"),

dict(kind="理解", topic="为什么叫「自由」能",
 stem="Why is G called the Gibbs '<b>free</b>' energy?",
 opts=["Because it costs nothing to compute",
       "Because at constant T and p, dG equals the <b>maximum non-expansion work</b> the system can do",
       "Because it is independent of temperature", "Because it is always released as heat"], ans=1,
 exp="""<p>把基本方程代入 dG = dH − T dS − S dT，整理得</p>
<div class="fb">dG = V dp − S dT + dw<sub>add</sub></div>
<p>恒温恒压下 dp = dT = 0，于是 <b>dG = dw<sub>add</sub></b>——即系统能做的<b>最大非膨胀功</b>
（例如电功）。讲义原话：<i>“hence termed Gibbs 'free' energy”</i>。</p>""",
 kp="恒温恒压下 dG = dw_add，是可提取的最大有用功", src="p.24「Combining Gibbs Energy and Enthalpy」"),

dict(kind="理解", topic="G 的两个偏导",
 stem="Which pair of partial derivatives of G is correct?",
 opts=["(∂G/∂p)<sub>T</sub> = V and (∂G/∂T)<sub>p</sub> = −S",
       "(∂G/∂p)<sub>T</sub> = −V and (∂G/∂T)<sub>p</sub> = S",
       "(∂G/∂p)<sub>T</sub> = S and (∂G/∂T)<sub>p</sub> = V",
       "(∂G/∂p)<sub>T</sub> = −S and (∂G/∂T)<sub>p</sub> = −V"], ans=0,
 exp="""<p>直接从 dG = V dp − S dT 读系数：</p>
<div class="fb">(∂G/∂p)<sub>T</sub> = <b>V</b>　　(∂G/∂T)<sub>p</sub> = <b>−S</b></div>
<p><b>后面反复用到这两个式子</b>：<br>
· 由 ΔG<sub>mix</sub> 对 T 求导得 <b>ΔS<sub>mix</sub></b>（p.31）<br>
· 由 (∂G/∂T)<sub>p</sub> = −S 推 C<sub>p</sub> 与 G 的二阶导关系，判断 T<sub>g</sub> 是几阶转变（Lecture 8）<br>
· 由 dG = V dp 推渗透压（Lecture 5）</p>""",
 kp="(∂G/∂p)_T = V、(∂G/∂T)_p = −S 是贯穿全课的两个工具",
 src="p.26「Partial Derivatives」"),

dict(kind="计算", topic="气体 Gibbs 能随压力变化",
 stem="One mole of ideal gas is compressed isothermally at 298 K from 1 bar to 10 bar. What is ΔG?",
 opts=["−5.7 kJ", "+2.5 kJ", "+5.7 kJ", "+24.8 kJ"], ans=2,
 exp="""<div class="fb">ΔG = nRT ln(p<sub>f</sub>/p<sub>i</sub>) = 1 × 8.314 × 298 × ln(10)</div>
<p>= 2477.6 × 2.303 = <b>+5.71 kJ</b></p>
<p>推导来源：恒温下 dG = V dp，代入 V = nRT/p 积分即得。</p>
<p><b>符号意义</b>：压缩使 G <b>升高</b>——气体被压缩不是自发的，需要外界做功。
若取标准态（1 bar）为初态，就得到 <b>G = G° + nRT ln p</b>，除以 n 即 <b>μ = μ° + RT ln p</b>，
这是后面所有混合推导的起点。</p>""",
 kp="G = G° + nRT ln p；μ = μ° + RT ln p 是混合热力学的出发点",
 src="p.25「Variation of Gibbs Energy with Pressure」"),

dict(kind="理解", topic="化学势的定义",
 stem="The chemical potential μ is defined as:",
 opts=["(∂G/∂T)<sub>p,n</sub>", "(∂G/∂n)<sub>T,p</sub>, i.e. the <b>partial molar Gibbs energy</b>",
       "(∂G/∂p)<sub>T,n</sub>", "G divided by the total mass"], ans=1,
 exp="""<p>在 G 的全微分中加入组成变化项：</p>
<div class="fb">dG = (∂G/∂p)<sub>T,n</sub> dp + (∂G/∂T)<sub>p,n</sub> dT + <b>(∂G/∂n)<sub>T,p</sub></b> dn</div>
<p>第三项的系数就是<b>化学势 μ</b>，也叫<b>偏摩尔 Gibbs 能</b>。二元体系的完整式子：</p>
<div class="fb">dG = V dp − S dT + μ<sub>A</sub> dn<sub>A</sub> + μ<sub>B</sub> dn<sub>B</sub> + ⋯</div>
<p>讲义称之为 <b>“Fundamental equation of chemical thermodynamics”</b>，
且对二元混合物 <b>G = μ<sub>A</sub>n<sub>A</sub> + μ<sub>B</sub>n<sub>B</sub></b>。</p>""",
 kp="μ = 偏摩尔 Gibbs 能；G = Σμᵢnᵢ", src="p.26「Chemical potential (μ)」"),

dict(kind="理解", topic="Dalton 定律在推导中的作用",
 stem="In deriving ΔG<sub>mix</sub> for gases, Dalton's law is used to replace p<sub>A</sub>/p by:",
 opts=["x<sub>A</sub> (the mole fraction)", "n<sub>A</sub>", "V<sub>A</sub>/V", "1 − χ"], ans=0,
 exp="""<p>Dalton 定律：<b>分压与总压之比等于摩尔分数</b></p>
<div class="fb">p<sub>A</sub>/p = n<sub>A</sub>/n = x<sub>A</sub></div>
<p>把它代入 ΔG<sub>mix</sub> = RT ln(p<sub>A</sub>/p)·n<sub>A</sub> + RT ln(p<sub>B</sub>/p)·n<sub>B</sub>，
就得到只含摩尔分数的漂亮结果：</p>
<div class="fb">ΔG<sub>mix</sub> = nRT (x<sub>A</sub> ln x<sub>A</sub> + x<sub>B</sub> ln x<sub>B</sub>)</div>""",
 kp="气体用 Dalton 定律、液体用 Raoult 定律，各自把压力比换成摩尔分数",
 src="p.28「From Dalton's Law」"),

dict(kind="理解", topic="混合总是自发的三条推论",
 stem="From ΔG<sub>mix</sub> = nRT(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>), which statement is <b>WRONG</b>?",
 opts=["ΔG<sub>mix</sub> is always negative, so mixing of ideal gases is always spontaneous",
       "ΔG<sub>mix</sub> is proportional to temperature",
       "ΔG<sub>mix</sub> becomes positive when x<sub>A</sub> &gt; 0.5",
       "The magnitude of ΔG<sub>mix</sub> is largest at x<sub>A</sub> = 0.5"], ans=2,
 exp="""<p>选 C，因为它是<b>错的</b>。摩尔分数<b>永远</b>在 0 和 1 之间，所以 ln x <b>永远为负</b>，
ΔG<sub>mix</sub> <b>恒为负</b>，与组成无关。</p>
<p>讲义列出的三条结论：<br>
① 摩尔分数在 0–1 之间 → <b>ΔG<sub>mix</sub> 恒负</b><br>
② <b>气体混合总是自发</b><br>
③ ΔG<sub>mix</sub> <b>正比于温度</b>（式中显含 T）</p>
<p>D 也对：x ln x 之和在 x = 0.5 处绝对值最大。</p>""",
 kp="理想混合 ΔG 恒负、正比于 T、在 x=0.5 处最负", src="p.28「Gibbs Energy of Mixing – Gases」"),

dict(kind="理解", topic="Raoult 定律",
 stem="Raoult's law states that, for an ideal solution:",
 opts=["p<sub>A</sub>/p<sub>A</sub>* = x<sub>A</sub>", "p<sub>A</sub>/p = x<sub>A</sub>",
       "p<sub>A</sub>* / p<sub>A</sub> = x<sub>A</sub>", "p<sub>A</sub> = x<sub>A</sub> χ"], ans=0,
 exp="""<div class="fb">p<sub>A</sub> / p<sub>A</sub>* = x<sub>A</sub></div>
<p>即<b>混合物中 A 的蒸气分压</b>与<b>纯 A 的蒸气压</b>之比，约等于 A 在混合物中的<b>摩尔分数</b>。
讲义注明：<b>只适用于理想溶液</b>。</p>
<p class="trap"><b>别与 Dalton 混</b>：Dalton 是 p<sub>A</sub>/p<sub>总</sub> = x<sub>A</sub>（选项 B），
分母是<b>总压</b>；Raoult 的分母是<b>纯液体的蒸气压</b>。两者用在不同地方。</p>""",
 kp="Raoult：p_A/p_A* = x_A（分母是纯液体蒸气压），仅适用理想溶液",
 src="p.29「Raoult's Law」"),

dict(kind="理解", topic="不纯液体的化学势",
 stem="Is the chemical potential of an impure liquid higher than, lower than, or the same as that of the pure liquid?",
 opts=["Higher", "Lower", "The same", "Depends on the identity of the impurity"], ans=1,
 exp="""<div class="fb">μ<sub>A</sub> = μ<sub>A</sub>* + RT ln x<sub>A</sub></div>
<p>因为 <b>0 &lt; x<sub>A</sub> &lt; 1</b>，所以 <b>ln x<sub>A</sub> &lt; 0</b>，因此 μ<sub>A</sub> &lt; μ<sub>A</sub>*
——<b>不纯液体的化学势总是更低</b>。</p>
<p><b>这条结论是三个后续现象的共同源头</b>：<br>
· <b>渗透压</b>（Lecture 5）：溶液侧 μ 低 → 溶剂想过膜<br>
· <b>沸点升高 / 凝固点降低</b>（依数性）<br>
· <b>链端使 T<sub>m</sub> 降低</b>（Lecture 10）：链端相当于杂质</p>""",
 kp="μ_A = μ_A* + RT ln x_A < μ_A*；渗透压与所有依数性的共同起点",
 src="p.29「μ_A = μ_A* + RT ln x_A」；官方 Question 7"),

dict(kind="理解", topic="气体与液体结果的一致性",
 stem="Comparing ΔG<sub>mix</sub> for ideal gases and for ideal liquid solutions, the lecture finds that:",
 opts=["The liquid result has an extra χ term", "The two expressions are <b>exactly the same</b>",
       "The liquid result is twice as large", "The liquid result has the opposite sign"], ans=1,
 exp="""<p>讲义在推完液体后特别标注：<i>“<b>Exactly the same</b> as Gibbs energy of mixing for gases!”</i></p>
<div class="fb">ΔG<sub>mix</sub> = nRT (x<sub>A</sub> ln x<sub>A</sub> + x<sub>B</sub> ln x<sub>B</sub>)</div>
<p><b>为什么会一样</b>：两条推导都归结为"混合前后化学势之差 = RT ln(压力比)"，
而 Dalton 和 Raoult 分别把各自的压力比换成了同一个 x<sub>A</sub>。</p>
<p class="trap">注意这只对<b>理想</b>体系成立。非理想（regular solution）要加 <b>x<sub>A</sub>x<sub>B</sub>χ</b> 项。</p>""",
 kp="理想气体与理想溶液的 ΔG_mix 表达式完全相同", src="p.30「Gibbs Energy of Mixing – Liquids」"),

dict(kind="计算", topic="由 ΔG 求 ΔS",
 stem="Using ΔS<sub>mix</sub> = −(∂ΔG<sub>mix</sub>/∂T)<sub>p,n</sub>, what is ΔS<sub>mix</sub> for an ideal mixture?",
 opts=["−nR(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)",
       "+nR(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)",
       "−nRT(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)", "0"], ans=0,
 exp="""<p>ΔG<sub>mix</sub> = <b>nRT</b>(x ln x + x ln x)，对 T 求偏导时 T 是唯一含 T 的因子：</p>
<div class="fb">∂ΔG<sub>mix</sub>/∂T = nR(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)</div>
<p>加负号：<b>ΔS<sub>mix</sub> = −nR(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)</b></p>
<p>因 ln x &lt; 0，整体<b>恒为正</b>——混合熵永远增加。</p>
<p class="trap"><b>陷阱</b>：选项 C 保留了 T。求导后 T 就消失了，ΔS 里<b>不含 T</b>。</p>""",
 kp="ΔS_mix = −nR Σx ln x，恒正，且不含温度", src="p.31「Entropy of Mixing」"),

dict(kind="计算", topic="理想混合熵计算",
 stem="2.0 mol of A is mixed with 6.0 mol of B to form an ideal solution. What is ΔS<sub>mix</sub>?",
 opts=["+11.5 J/K", "+18.7 J/K", "+37.4 J/K", "+46.7 J/K"], ans=2,
 exp="""<p>x<sub>A</sub> = 2/8 = 0.25，x<sub>B</sub> = 6/8 = 0.75，<b>n = 8.0 mol</b></p>
<div class="fb">ΔS = −8.0 × 8.314 × [0.25 ln0.25 + 0.75 ln0.75]</div>
<p>0.25 × (−1.386) = −0.3466；0.75 × (−0.2877) = −0.2158；和 = −0.5623</p>
<p>ΔS = −66.51 × (−0.5623) = <b>+37.4 J/K</b></p>
<p class="trap"><b>陷阱</b>：n 必须是<b>总</b>摩尔数 8.0。另外注意组成不对称（0.25/0.75）时
ΔS 比等摩尔时（0.5/0.5 给 46.1 J/K）<b>小</b>——熵在等摩尔处最大。</p>""",
 kp="n 取总摩尔数；混合熵在 x = 0.5 时最大", src="p.31「Entropy of Mixing」"),

dict(kind="理解", topic="理想体系混合焓为零",
 stem="Why is ΔH<sub>mix</sub> = 0 for ideal gases and ideal solutions?",
 opts=["Because the temperature does not change",
       "Ideal gases have <b>no</b> intermolecular interaction; ideal solutions have A-A, B-B and A-B interactions that are <b>identical</b>",
       "Because ΔG = 0", "Because the volume does not change"], ans=1,
 exp="""<p>由 ΔH = ΔG + TΔS，把两式代入正好抵消，得 <b>ΔH<sub>mix</sub> = 0</b>。讲义给的物理解释：</p>
<p>· <b>理想气体</b>：分子间<b>没有</b>相互作用，换不换邻居都一样<br>
· <b>理想溶液</b>：A-A、B-B、A-B 三种相互作用<b>完全相同</b>，换邻居不改变能量</p>
<p>结论：<b>“Mixing is largely driven by entropy!”</b>——理想混合完全靠熵驱动。</p>
<p class="trap">这正是<b>非理想</b>体系的切入点：只要 A-B 与 A-A/B-B 不同，就产生非零的<b>交换能</b>，
于是有了 χ。</p>""",
 kp="理想混合 ΔH = 0，混合纯由熵驱动；非理想的偏离由交换能 Δw 度量",
 src="p.31「In ideal gases and ideal solutions, enthalpy of mixing is zero」"),

dict(kind="计算", topic="Boltzmann 组合数",
 stem="A lattice of 12 sites holds 5 molecules of A and 7 of B. What is Ω?",
 opts=["60", "792", "5,040", "95,040"], ans=1,
 exp="""<div class="fb">Ω = m! / (m<sub>A</sub>! m<sub>B</sub>!) = 12! / (5! · 7!) = 479,001,600 / (120 × 5040) = <b>792</b></div>
<p>这就是组合数 C(12,5)。</p>
<p><b>为什么这样数</b>：12 个格点全排列有 12! 种，但同种分子彼此<b>无法区分</b>，
所以要除掉 A 内部的 5! 种和 B 内部的 7! 种重复。</p>""",
 kp="Ω = m!/(m_A! m_B!)；除阶乘是因为同种分子不可区分",
 src="p.32「Entropy of Mixing by Statistical Thermodynamics」"),

dict(kind="理解", topic="混合前的熵",
 stem="In the statistical derivation, what is the entropy of the <b>unmixed</b> (pure) components?",
 opts=["S = k ln 2", "S = 0, because Ω = 1", "S = −k Σ m ln x", "S = k ln m!"], ans=1,
 exp="""<p>纯物质的所有分子都相同，把它们排进格子<b>只有一种可分辨的方式</b>，即 <b>Ω = 1</b>：</p>
<div class="fb">S = k lnΩ = k ln 1 = <b>0</b></div>
<p>因此 <b>ΔS<sub>mix</sub> = S<sub>混合后</sub> − 0 = S<sub>混合后</sub></b>，直接就是混合后的熵。</p>
<p>再把分子数换成摩尔数（n = m/N<sub>Av</sub>，且 N<sub>Av</sub>k = R），
就回到 <b>ΔS<sub>mix</sub> = −nR(x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>)</b>
——与热力学路线<b>完全一致</b>。</p>""",
 kp="纯态 Ω = 1 → S = 0，故 ΔS_mix 等于混合后的 S；两条推导路径结果相同",
 src="p.33「Before Mixing: S = k lnΩ = k ln 1 = 0」"),

dict(kind="理解", topic="Stirling 近似",
 stem="Stirling's approximation, used to simplify k ln[m!/(m<sub>A</sub>!m<sub>B</sub>!)], states that:",
 opts=["ln m! ≈ m ln m − m", "ln m! ≈ m ln m", "ln m! ≈ m − ln m", "ln m! ≈ m²/2"], ans=0,
 exp="""<div class="fb">ln m! ≈ m ln m − m</div>
<p>它把难处理的阶乘变成可微的初等函数，是从 Ω 推到 ΔS<sub>mix</sub> 的关键一步。</p>
<p><b>适用条件</b>：m 很大。对格子模型（分子数 ~10²³）这个近似极其精确。</p>
<p class="trap">Stirling 近似在本课出现<b>两次</b>：这里（p.32）和 <b>Flory-Huggins 推导</b>（Lecture 3, p.43），
是必须记住的工具。</p>""",
 kp="Stirling: ln m! ≈ m ln m − m；L2 和 L3（Flory-Huggins）各用一次",
 src="p.32「Using Stirling's approximation」"),

dict(kind="理解", topic="交换能 Δw",
 stem="The exchange energy Δw is defined as:",
 opts=["w<sub>AB</sub> − w<sub>AA</sub> − w<sub>BB</sub>", "w<sub>AB</sub> − w<sub>AA</sub>/2 − w<sub>BB</sub>/2",
       "(w<sub>AA</sub> + w<sub>BB</sub>)/2 − w<sub>AB</sub>", "w<sub>AA</sub> + w<sub>BB</sub> + w<sub>AB</sub>"], ans=1,
 exp="""<div class="fb">Δw = w<sub>AB</sub> − w<sub>AA</sub>/2 − w<sub>BB</sub>/2</div>
<p><b>物理含义</b>：拆掉<b>半对</b> A-A 和<b>半对</b> B-B，换成<b>一对</b> A-B，所付出的能量代价。</p>
<p>"半对"的来源：讲义在算纯组分焓时用了 H<sub>A</sub> = ½ z m<sub>A</sub> w<sub>AA</sub>，
<b>½ 是因为每两个分子之间只有一次相互作用</b>（避免重复计数）。</p>
<p>由此得 ΔH<sub>mix</sub> = (m<sub>A</sub>m<sub>B</sub>/m) · z Δw。</p>""",
 kp="Δw 是交换能；½ 因子来自每两分子只算一次相互作用",
 src="p.34–36「Enthalpy of Mixing / exchange energy」"),

dict(kind="理解", topic="χ 的物理意义",
 stem="The interaction parameter χ = zΔw/kT is best described as:",
 opts=["The exchange energy per molecule, normalized by the thermal energy kT",
       "The number of nearest neighbours", "The total enthalpy of mixing",
       "The ratio of A to B molecules"], ans=0,
 exp="""<div class="fb">χ = z Δw / kT</div>
<p>讲义原话：<i>“the exchange energy <b>per molecule</b>, normalized by its <b>thermal energy kT</b>”</i>。
z 是近邻数，把"每对"的代价乘成"每分子"的代价，再除 kT 变成无量纲数。</p>
<p><b>为什么要除 kT</b>：热运动能量 kT 是"对抗"焓不利影响的尺度。χ 直接告诉你
"能量代价相对于热扰动有多大"——<b>χ 大 → 焓占上风 → 倾向分相</b>。</p>
<p class="trap"><b>关键推论</b>：χ ∝ 1/T，所以<b>升温 χ 减小</b> → 高温更易互溶 → 这就是常见的 <b>UCST</b>。</p>""",
 kp="χ = zΔw/kT 无量纲；χ ∝ 1/T 是 UCST 行为的根源",
 src="p.36「This is defined as interaction parameter」"),

dict(kind="计算", topic="混合焓计算",
 stem="A regular solution has χ = 0.8. For 5.0 mol total at x<sub>A</sub> = 0.4 and T = 350 K, what is ΔH<sub>mix</sub>?",
 opts=["1.40 kJ", "2.79 kJ", "3.49 kJ", "5.59 kJ"], ans=1,
 exp="""<div class="fb">ΔH<sub>mix</sub> = x<sub>A</sub> x<sub>B</sub> χ n R T</div>
<p>x<sub>A</sub>x<sub>B</sub> = 0.4 × 0.6 = 0.24</p>
<p>nRT = 5.0 × 8.314 × 350 = 14,550 J</p>
<p>ΔH = 0.24 × 0.8 × 14,550 = <b>2,794 J ≈ 2.79 kJ</b></p>
<p class="trap"><b>陷阱</b>：x<sub>B</sub> = 1 − x<sub>A</sub> = 0.6，别忘了算。用 0.4² 会得到别的数。
另外 ΔH<sub>mix</sub> &gt; 0 说明混合<b>吸热</b>，焓上不利。</p>""",
 kp="ΔH_mix = x_A x_B χ nRT；χ > 0 时混合吸热、焓上不利",
 src="p.36「ΔH_mix = x_A x_B χ nRT」"),

dict(kind="理解", topic="regular solution 的 ΔG",
 stem="For a regular (non-ideal) solution, ΔG<sub>mix</sub> is:",
 opts=["nRT[x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>]",
       "nRT[x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub> + x<sub>A</sub>x<sub>B</sub>χ]",
       "nRT·x<sub>A</sub>x<sub>B</sub>χ", "nRT[x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>] − x<sub>A</sub>x<sub>B</sub>χ"], ans=1,
 exp="""<div class="fb">ΔG<sub>mix</sub> = nRT [ x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub> + x<sub>A</sub>x<sub>B</sub>χ ]</div>
<p>三项的角色：</p>
<table class="mini"><thead><tr><th>项</th><th>来源</th><th>符号</th><th>作用</th></tr></thead><tbody>
<tr><td>x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub></td><td>−TΔS</td><td><b>恒负</b></td><td>永远有利于混合</td></tr>
<tr><td>x<sub>A</sub>x<sub>B</sub>χ</td><td>ΔH</td><td>χ&gt;0 时为正</td><td>不利于混合</td></tr>
</tbody></table>
<p>两者的<b>竞争</b>决定是否分相——这正是 Lecture 4 全篇的主题。</p>""",
 kp="regular solution ΔG = 熵项（恒负）+ 焓项 x_A x_B χ；两者竞争决定相行为",
 src="p.36「In regular (non-ideal) solutions」"),

dict(kind="理解", topic="油水不互溶的原因",
 stem="A 1:1 mixture of oil and water does not mix at room temperature. Which term in ΔG<sub>mix</sub> = nRT[x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub> + x<sub>A</sub>x<sub>B</sub>χ] is responsible?",
 opts=["x<sub>A</sub>ln x<sub>A</sub>", "x<sub>B</sub>ln x<sub>B</sub>",
       "x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub>", "x<sub>A</sub>x<sub>B</sub>χ"], ans=3,
 exp="""<p><b>x<sub>A</sub>x<sub>B</sub>χ 是焓项，且为正</b>，这使混合在能量上不利。</p>
<p>两个熵项 x ln x <b>恒为负</b>，永远<b>有利于</b>混合——它们不可能是"不互溶"的原因。
油水不互溶正是因为 χ 足够大，焓项压过了熵项。</p>
<p class="trap"><b>物理来源</b>：水-水之间有强氢键（w<sub>AA</sub> 很负），油-水之间没有，
所以 Δw = w<sub>AB</sub> − w<sub>AA</sub>/2 − w<sub>BB</sub>/2 <b>为正且很大</b> → χ 大。</p>""",
 kp="不互溶永远归因于正的焓项 x_A x_B χ，熵项永远促进混合",
 src="官方 Question 9（对应 p.36）"),

dict(kind="计算", topic="判断混合是否自发",
 stem="For an equimolar regular solution at 300 K with χ = 2.5, is mixing spontaneous? (evaluate ΔG<sub>mix</sub>/nRT)",
 opts=["Yes, ΔG/nRT = −0.693", "Yes, ΔG/nRT = −0.068",
       "No, ΔG/nRT = +0.068", "No, ΔG/nRT = +0.625"], ans=1,
 exp="""<div class="fb">ΔG/nRT = x<sub>A</sub>ln x<sub>A</sub> + x<sub>B</sub>ln x<sub>B</sub> + x<sub>A</sub>x<sub>B</sub>χ</div>
<p>熵项：2 × 0.5 × ln0.5 = <b>−0.693</b><br>
焓项：0.5 × 0.5 × 2.5 = <b>+0.625</b></p>
<p>合计 = −0.693 + 0.625 = <b>−0.068</b> → 为负，<b>混合自发</b>。</p>
<p class="trap">⚠️ <b>但这不代表不分相！</b>ΔG &lt; 0 只说明"混合比完全不混合好"。
χ = 2.5 &gt; 2 时 ΔG 曲线中间会出现<b>局部极大</b>，通过<b>分相</b>可以达到更低的能量。
这是 Lecture 4 的核心，也是官方 Question 13 的考点。</p>""",
 kp="ΔG_mix < 0 ≠ 不分相；χ = 2 是对称 regular solution 的临界值",
 src="p.36 与 p.51「Local maximum」联读"),

dict(kind="理解", topic="χ 与温度的关系",
 stem="Based on χ = zΔw/kT alone, raising the temperature of a mixture with Δw &gt; 0 will:",
 opts=["Increase χ, making mixing less favourable", "Decrease χ, making mixing more favourable",
       "Leave χ unchanged", "Make Δw negative"], ans=1,
 exp="""<p>χ = zΔw/<b>kT</b>，T 在分母 → <b>升温使 χ 减小</b> → 焓的不利影响相对减弱 → 更易互溶。</p>
<p>这就是<b>常见的 UCST 行为</b>：温度高于临界温度后完全互溶。</p>
<p class="trap"><b>但要注意</b>（Lecture 4 会讲）：经验上 χ 还可写成 <b>χ = α/T + β</b>。
当 α 为负、β 为正时，升温反而使 χ 变大 → <b>LCST</b>（升温分相），
例如 <b>PEO/水</b>（氢键随温度升高变弱）。理论式只给出 UCST。</p>""",
 kp="理论 χ ∝ 1/T 只能给 UCST；经验式 χ = α/T + β 才能描述 LCST",
 src="p.36「χ = zΔw/kT」；p.61（L4）「LCST」"),

dict(kind="理解", topic="近邻数 z 的角色",
 stem="In the lattice model, the coordination number z appears in Δw's prefactor. What happens to z in the final expression for ΔG<sub>mix</sub>?",
 opts=["It must be measured experimentally for each system",
       "It is absorbed into the single parameter χ",
       "It cancels out exactly", "It equals 6 for all polymers"], ans=1,
 exp="""<p>z 被<b>吸收进 χ</b>：χ = <b>z</b>Δw/kT。最终的 ΔG<sub>mix</sub> 表达式里<b>只出现 χ</b>，
不再单独出现 z 或 Δw。</p>
<p><b>这是格子模型的聪明之处</b>：z 和 Δw 都难以独立测量，但组合成的 χ 是<b>可以由实验拟合</b>的
单一参数（例如从相图或渗透压的第二维里系数得到）。</p>
<p class="trap">同样的"参数打包"手法在本课出现多次：Lecture 1 把局部约束打包成 <b>C<sub>∞</sub></b>，
Lecture 3 的 Flory-Huggins 推导中 <b>z 也在最后消失</b>（讲义原话："the actual number does not matter"）。</p>""",
 kp="z 和 Δw 打包成可测的单一参数 χ；同类手法见 C∞",
 src="p.36「χ = zΔw/kT」；p.40（L3）「the actual number does not matter」"),

dict(kind="计算", topic="化学势下降量",
 stem="At 298 K, by how much is the chemical potential of solvent A lowered when its mole fraction is reduced to x<sub>A</sub> = 0.80?",
 opts=["−553 J/mol", "−1,240 J/mol", "−2,478 J/mol", "−4,340 J/mol"], ans=0,
 exp="""<div class="fb">μ<sub>A</sub> − μ<sub>A</sub>* = RT ln x<sub>A</sub> = 8.314 × 298 × ln(0.80)</div>
<p>ln 0.80 = −0.2231</p>
<p>= 2,477.6 × (−0.2231) = <b>−553 J/mol</b></p>
<p><b>这个数的用处</b>：正是这 553 J/mol 的化学势落差驱动溶剂穿过半透膜，产生渗透压
（Lecture 5：V<sub>m</sub>Π = −RT ln x<sub>A</sub>）。</p>
<p class="trap"><b>陷阱</b>：选项 C 是 RT 本身（忘了乘 ln x）。</p>""",
 kp="RT ln x_A 给出化学势降低量；它就是渗透压的驱动力",
 src="p.29「μ_A = μ_A* + RT ln x_A」；p.5（L5）"),
]
