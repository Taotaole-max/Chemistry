# -*- coding: utf-8 -*-
LEC = 3
TITLE = "Thermodynamics of Polymer Solutions (Flory-Huggins)"
CN = "高分子溶液热力学"
SRC = "讲义 Lectures_1-4"
L = [
dict(kind="理解", topic="Flory-Huggins 要解决什么",
 stem="Flory-Huggins theory extends the regular-solution treatment in order to calculate:",
 opts=["The entropy and enthalpy of mixing for <b>polymer solutions</b>",
       "The crystallization rate of polymers", "The glass transition temperature",
       "The molecular weight distribution"], ans=0,
 exp="""<p>讲义 Key Concepts：<i>“To extend the thermodynamics of mixing to polymer solution systems”</i>、
<i>“To apply Flory-Huggins Theory to determine entropy of polymer dissolution”</i>。</p>
<p>它沿用<b>与 regular solution 相同的格子模型</b>，但必须处理一个新事实：
<b>一条高分子链要占 N 个连续格点</b>，而不是 1 个。这个约束大幅减少可排布方式，
从而降低混合熵。</p>""",
 kp="Flory-Huggins = 格子模型 + 「链占 N 个连续格点」这一约束",
 src="p.38–39「Key Concepts / Flory-Huggins Theory」"),

dict(kind="计算", topic="总格点数",
 stem="A Flory-Huggins lattice holds 600 solvent molecules and 8 polymer chains of N = 50. How many lattice sites are there in total?",
 opts=["608", "650", "1,000", "1,200"], ans=2,
 exp="""<div class="fb">m = m<sub>A</sub> + N m<sub>B</sub> = 600 + 50 × 8 = 600 + 400 = <b>1,000</b></div>
<p class="trap"><b>陷阱</b>：选项 A（608）把每条链当成占<b>一个</b>格点了。
Flory-Huggins 的核心前提正是<b>一条链占 N 个格点</b>——链的体积必须显式计入。</p>""",
 kp="m = m_A + N·m_B；链占 N 个格点是全部推导的起点", src="p.39「Total number of lattice sites」"),

dict(kind="计算", topic="体积分数",
 stem="For that same lattice (600 solvent, 8 chains of N = 50), what are φ<sub>A</sub> and φ<sub>B</sub>?",
 opts=["φ<sub>A</sub> = 0.987, φ<sub>B</sub> = 0.013", "φ<sub>A</sub> = 0.60, φ<sub>B</sub> = 0.40",
       "φ<sub>A</sub> = 0.40, φ<sub>B</sub> = 0.60", "φ<sub>A</sub> = 0.75, φ<sub>B</sub> = 0.25"], ans=1,
 exp="""<div class="fb">φ<sub>A</sub> = m<sub>A</sub>/m = 600/1000 = <b>0.60</b>　　φ<sub>B</sub> = Nm<sub>B</sub>/m = 400/1000 = <b>0.40</b></div>
<p class="trap"><b>陷阱</b>：选项 A 是按<b>摩尔分数</b>算的 8/608 ≈ 0.013。
<b>Flory-Huggins 一律用体积分数 φ，不用摩尔分数 x</b>——因为高分子和溶剂的"分子"大小差 N 倍，
用摩尔分数会严重低估高分子占据的空间。</p>""",
 kp="φ_B = Nm_B/(m_A + Nm_B)；高分子体系用体积分数而非摩尔分数",
 src="p.39「Volume fractions of A and B」"),

dict(kind="理解", topic="放第一个单体的可选格点",
 stem="If i chains have already been placed, how many sites are available for the <b>first</b> monomer of the (i+1)th chain?",
 opts=["m − i", "m − iN", "z(m − iN)/m", "(z−1)(m − iN)/m"], ans=1,
 exp="""<p>已放 i 条链，每条占 N 个格点 → 已占 <b>iN</b> 个格点 → 剩下 <b>m − iN</b> 个空位。
第一个单体<b>可以自由选择任何一个空位</b>：</p>
<div class="fb">第 1 个单体的可选数 = m − iN</div>
<p>从第 2 个单体开始就不自由了——必须放在<b>前一个单体的近邻</b>，这才引出 z 和 (z−1)。</p>""",
 kp="第一个单体自由放（m − iN 种），后续单体受「必须相邻」约束",
 src="p.40「To insert the 1st monomer unit」"),

dict(kind="理解", topic="第二个单体的有效格点数",
 stem="For the <b>second</b> monomer of a chain, the effective number of available sites is z(m−iN)/m. What does the factor (m−iN)/m represent?",
 opts=["The number of chains already placed", "The <b>probability</b> that a given neighbouring site is empty",
       "The coordination number", "The volume fraction of polymer"], ans=1,
 exp="""<p>第 2 个单体必须放在 z 个近邻中的一个，但<b>这些近邻不一定是空的</b>。
空位占全部格点的比例是 <b>(m − iN)/m</b>，这就是<b>某个近邻恰好为空的概率</b>。</p>
<div class="fb">有效可选数 = z × (m − iN)/m</div>
<p>这是一个<b>平均场近似</b>：假定空位在格子中<b>均匀随机分布</b>，
所以任一近邻为空的概率就等于整体空位分数。</p>""",
 kp="(m−iN)/m 是近邻为空的概率；这是平均场近似的体现",
 src="p.40「The probability that each neighbouring site is empty」"),

dict(kind="理解", topic="为什么第三个单体用 z−1",
 stem="From the <b>third</b> monomer onwards, the coordination factor becomes (z−1) rather than z. Why?",
 opts=["Because one neighbouring site is already occupied by the <b>previous</b> monomer of the same chain",
       "Because the lattice loses one site each time", "Because z decreases with temperature",
       "Because two monomers cannot be adjacent"], ans=0,
 exp="""<p>第 3 个单体要接在第 2 个单体旁边，但第 2 个单体的 z 个近邻中<b>已经有一个被第 1 个单体占了</b>，
所以只剩 <b>z − 1</b> 个方向可选。</p>
<div class="fb">第 3 个及以后：(z − 1) × (m − iN)/m</div>
<p>讲义同时声明了两条<b>近似假设</b>：<br>
① 链<b>不折回</b>已占据的格点（no back-folding）<br>
② 每加一个单体<b>不改变</b>空位比例</p>
<p>这两条都是为了让连乘式可解，也是 Flory-Huggins 精度的主要来源限制。</p>""",
 kp="(z−1) 来自前一个单体占掉一个方向；模型假设不折回、空位比例不变",
 src="p.41「the number of sites available for the 3rd monomer becomes z−1」"),

dict(kind="理解", topic="单条链的放置方式数",
 stem="The total number of ways of placing the (i+1)th chain is approximated as:",
 opts=["(m − iN)<sup>N</sup>", "[(z−1)/m]<sup>N−1</sup> (m − iN)<sup>N</sup>",
       "z<sup>N</sup> (m − iN)", "m!/(m−iN)!"], ans=1,
 exp="""<p>把各单体的可选数连乘：</p>
<div class="fb">(m−iN) · z(m−iN)/m · [(z−1)(m−iN)/m]<sup>N−2</sup> ≈ [(z−1)/m]<sup>N−1</sup> (m−iN)<sup>N</sup></div>
<p>讲义把第 2 个单体的 z <b>近似成 (z−1)</b>（"Approximate to (z−1)"），
这样 N−1 个因子形式统一，指数才写得出来。</p>
<p><b>数一数</b>：共 N 个单体贡献 N 个 (m−iN) 因子；除第 1 个外的 N−1 个单体各贡献一个 (z−1)/m。</p>""",
 kp="单链放置数 ≈ [(z−1)/m]^(N−1)(m−iN)^N；把 z 近似为 z−1 是为了统一指数",
 src="p.41「total number of ways of putting the (i+1)th polymer chain」"),

dict(kind="理解", topic="为什么除以 m_B!",
 stem="In Ω = (1/m<sub>B</sub>!) Π …, why is the product divided by m<sub>B</sub>!?",
 opts=["To convert to molar quantities", "Because all polymer chains are <b>identical to each other</b>",
       "Because of Stirling's approximation", "To remove the temperature dependence"], ans=1,
 exp="""<p>讲义注解：<i>“Division by m<sub>B</sub>! accounts for the fact that <b>all chains are same as each other</b>”</i>。</p>
<p>连乘时我们是"第 1 条、第 2 条、…"依次放的，隐含把链<b>编了号</b>。
但真实的链<b>彼此不可区分</b>，交换任意两条链得到的是<b>同一个</b>构型，
所以要除掉 m<sub>B</sub>! 种重复计数。</p>
<p class="trap">这与 Lecture 2 里 Ω = m!/(m<sub>A</sub>!m<sub>B</sub>!) 除阶乘是<b>完全相同的道理</b>
——同种粒子不可区分。</p>""",
 kp="除 m_B! 是因为链彼此不可区分；与 L2 的 Ω 除阶乘同理",
 src="p.42「Division by m_B! accounts for…」"),

dict(kind="理解", topic="推导中的关键代换",
 stem="In converting the product term into factorials, the derivation uses the identity:",
 opts=["m − Nm<sub>B</sub> = m<sub>A</sub>", "m + Nm<sub>B</sub> = m<sub>A</sub>",
       "m<sub>A</sub> = N m<sub>B</sub>", "m = N m<sub>B</sub>"], ans=0,
 exp="""<p>讲义原话：<i>“Trick is to realize that <b>m − Nm<sub>B</sub> = m<sub>A</sub></b>”</i>，因此
<b>m/N − m<sub>B</sub> = m<sub>A</sub>/N</b>。</p>
<p>这一步把连乘 Π(m − iN)<sup>N</sup> 转成阶乘形式：</p>
<div class="fb">N<sup>Nm<sub>B</sub></sup> · [ (m/N)! / (m<sub>A</sub>/N)! ]<sup>N</sup></div>
<p>转成阶乘之后才能用 <b>Stirling 近似</b>处理，这是能走到最终解析式的关键。</p>""",
 kp="m − Nm_B = m_A 是把连乘转成阶乘的关键代换", src="p.42「Trick is to realize that…」"),

dict(kind="理解", topic="纯组分的熵",
 stem="Substituting m<sub>A</sub> = 0 into the general entropy expression gives S<sub>B</sub> (pure polymer). Substituting m<sub>B</sub> = 0 gives S<sub>A</sub> (pure solvent), which equals:",
 opts=["k m<sub>A</sub> ln m<sub>A</sub>", "0", "−k m<sub>A</sub> ln φ<sub>A</sub>", "k ln m<sub>A</sub>!"], ans=1,
 exp="""<div class="fb">S<sub>A</sub> = k[m<sub>A</sub> ln m<sub>A</sub> − m<sub>A</sub> ln m<sub>A</sub>] = <b>0</b></div>
<p>纯溶剂的所有分子都相同、都占一个格点，只有一种可分辨排法 → Ω = 1 → S = 0。
与 Lecture 2 的结论一致。</p>
<p class="trap"><b>但纯高分子的 S<sub>B</sub> 不为零！</b>因为链<b>本身</b>在格子里还有构象自由度：</p>
<div class="fb">S<sub>B</sub> = k[m<sub>B</sub>ln(Nm<sub>B</sub>) − m<sub>B</sub>ln m<sub>B</sub> − m<sub>B</sub>(N−1) + m<sub>B</sub>(N−1)ln(z−1)]</div>
<p>正因如此，ΔS<sub>mix</sub> = S − S<sub>A</sub> − S<sub>B</sub> 时那些含 (z−1) 的项<b>正好相消</b>
——这就是 <b>z 最终消失</b>的原因。</p>""",
 kp="S_A = 0 但 S_B ≠ 0（链有构象熵）；相减时含 z 的项抵消",
 src="p.44「The entropy for the pure (unmixed) polymer and solvent」"),

dict(kind="理解", topic="Flory-Huggins 混合熵",
 stem="The Flory-Huggins entropy of mixing (molar form) is:",
 opts=["−nR[φ<sub>A</sub>lnφ<sub>A</sub> + φ<sub>B</sub>lnφ<sub>B</sub>]",
       "−nR[φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub>]",
       "−nR[(φ<sub>A</sub>/N)lnφ<sub>A</sub> + φ<sub>B</sub>lnφ<sub>B</sub>]",
       "−(nR/N)[φ<sub>A</sub>lnφ<sub>A</sub> + φ<sub>B</sub>lnφ<sub>B</sub>]"], ans=1,
 exp="""<div class="fb">ΔS<sub>mix</sub> = −nR [ φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N) lnφ<sub>B</sub> ]</div>
<p class="trap"><b>三个错误选项都很像，必须看清 1/N 落在哪一项</b>：<br>
· <b>只有高分子那一项（B）</b>除以 N<br>
· <b>溶剂项（A）原封不动</b><br>
· <b>不是整体</b>除以 N（选项 D 的错法）</p>
<p><b>1/N 的来源</b>：从分子数换算到摩尔数时，m<sub>B</sub>/m = (1/N)(Nm<sub>B</sub>/m) = φ<sub>B</sub>/N
——高分子的<b>摩尔数</b>只有其体积分数的 1/N。</p>""",
 kp="只有高分子项除以 N，溶剂项不变；1/N 来自「链的摩尔数远少于其体积分数」",
 src="p.45「ΔS_mix = −nR[φ_A lnφ_A + (φ_B/N) lnφ_B]」"),

dict(kind="计算", topic="高分子 vs 小分子混合熵",
 stem="At φ<sub>A</sub> = φ<sub>B</sub> = 0.5, what fraction of the small-molecule mixing entropy does a polymer with N = 100 retain?",
 opts=["about 1%", "about 25%", "about 50%", "about 99%"], ans=2,
 exp="""<p><b>小分子（N=1）</b>：−[0.5 ln0.5 + 0.5 ln0.5] = <b>0.6931</b> (×nR)</p>
<p><b>高分子（N=100）</b>：−[0.5 ln0.5 + (0.5/100) ln0.5] = −[−0.3466 − 0.00347] = <b>0.3500</b></p>
<p>比值 = 0.3500 / 0.6931 = <b>0.505 ≈ 50%</b></p>
<p class="trap">⚠️ <b>最普遍的误解</b>：以为除以 N 会让熵掉到 1/N（1%，选项 A）。
<b>错</b>——溶剂那一项完全没被除，它独自就贡献了 0.3466。
N → ∞ 时极限是 <b>0.5</b>，不是 0。</p>""",
 kp="φ=0.5 时熵只减到约一半（极限 0.5），绝不是 1/N",
 src="p.45；官方 Question 11"),

dict(kind="计算", topic="不同 N 下的混合熵",
 stem="Compute ΔS<sub>mix</sub>/(nR) for a polymer solution with φ<sub>A</sub> = 0.9, φ<sub>B</sub> = 0.1, N = 1000.",
 opts=["0.0949", "0.3250", "0.6931", "0.9485"], ans=0,
 exp="""<div class="fb">ΔS/(nR) = −[φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub>]</div>
<p>溶剂项：−0.9 × ln(0.9) = −0.9 × (−0.10536) = <b>+0.09482</b><br>
高分子项：−(0.1/1000) × ln(0.1) = −0.0001 × (−2.3026) = <b>+0.00023</b></p>
<p>合计 = <b>0.0949</b></p>
<p><b>注意</b>：高分子项只占 0.24%——N 很大时 ΔS<sub>mix</sub> <b>几乎完全由溶剂贡献</b>。
这解释了为什么高分子溶解在熵上如此吃亏。</p>""",
 kp="N 很大时混合熵几乎全部来自溶剂项", src="p.45「ΔS_mix」"),

dict(kind="理解", topic="链连接如何减少排布数",
 stem="Eight lattice sites contain 2 black circles. The number of arrangements is 28 if they are free, but only 10 if they are <b>linked together</b>. This illustrates that:",
 opts=["Linking increases the number of configurations",
       "Linking sharply <b>reduces</b> the number of configurations, hence lowering the entropy of mixing",
       "The lattice size must be increased", "Entropy is independent of connectivity"], ans=1,
 exp="""<p>不相连：C(8,2) = 8!/(6!2!) = <b>28</b> 种<br>
相连（必须占相邻格点）：只有 <b>10</b> 种</p>
<p>这个小例子直观展示了 Flory-Huggins 的<b>全部物理内容</b>：
共价键把单体<b>绑</b>在一起，大幅削减了可分辨的排布方式 → <b>ΔS<sub>mix</sub> 变小</b>。</p>
<p><b>推论</b>：ΔS 变小 → −TΔS 这个有利项变弱 → <b>高分子溶解不如小分子自发</b>。</p>""",
 kp="连接性削减排布数 → 混合熵下降 → 溶解性变差。这是 FH 的物理内核",
 src="官方 Question 10 与 11"),

dict(kind="理解", topic="混合焓为何不除 N",
 stem="In Flory-Huggins theory, ΔH<sub>mix</sub> = φ<sub>A</sub>φ<sub>B</sub>χnRT — it is <b>not</b> divided by N. Why?",
 opts=["Because enthalpy is always zero for polymers",
       "Because enthalpy depends only on <b>local contacts</b> between solvent and monomer units, which are unaffected by whether the monomers are linked",
       "Because χ already contains 1/N", "Because the derivation neglects enthalpy"], ans=1,
 exp="""<p>讲义原话：<i>“Enthalpy of mixing depends only on <b>local interactions</b> between solvent and monomer units,
and remains approximately equal even when monomers are <b>linked in a chain</b>”</i>。</p>
<p><b>关键对比</b>：</p>
<table class="mini"><thead><tr><th></th><th>受连接性影响？</th><th>结果</th></tr></thead><tbody>
<tr><td><b>熵</b></td><td><b>是</b>——排布方式大减</td><td>高分子项除以 N</td></tr>
<tr><td><b>焓</b></td><td><b>否</b>——只看谁挨着谁</td><td>形式不变，不除 N</td></tr>
</tbody></table>
<p>把一串单体连成链，并<b>不改变</b>每个单体周围有多少个溶剂邻居，所以接触能几乎不变。</p>""",
 kp="熵受连接性影响（除 N），焓只看局部接触（不除 N）——这是 FH 最核心的不对称",
 src="p.45「Enthalpy of mixing depends only on local interactions」"),

dict(kind="理解", topic="Flory-Huggins 的 ΔG",
 stem="The complete Flory-Huggins Gibbs energy of mixing is:",
 opts=["nRT[φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub> + φ<sub>A</sub>φ<sub>B</sub>χ]",
       "nRT[φ<sub>A</sub>lnφ<sub>A</sub> + φ<sub>B</sub>lnφ<sub>B</sub> + φ<sub>A</sub>φ<sub>B</sub>χ]",
       "nRT[(φ<sub>A</sub>lnφ<sub>A</sub> + φ<sub>B</sub>lnφ<sub>B</sub>)/N + φ<sub>A</sub>φ<sub>B</sub>χ]",
       "nRT[φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub> + φ<sub>A</sub>φ<sub>B</sub>χ/N]"], ans=0,
 exp="""<div class="fb">ΔG<sub>mix</sub> = nRT [ φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub> + φ<sub>A</sub>φ<sub>B</sub>χ ]</div>
<p>其中 χ = zΔw/kT。三项的角色：</p>
<p>· 前两项 = −TΔS，<b>恒负</b>，有利混合，但<b>高分子项被 N 削弱</b><br>
· 第三项 = ΔH，χ &gt; 0 时为正，<b>不利混合</b>，<b>且不被 N 削弱</b></p>
<p class="trap"><b>这个不对称是全部结论的来源</b>：N 增大只削弱有利项、不削弱不利项，
所以<b>分子量越高越难溶</b>，临界温度越高，相图越向稀溶液一侧移动。</p>""",
 kp="FH 的 ΔG：熵项被 N 削弱、焓项不被削弱 → 高分子难溶",
 src="p.45「ΔG_mix = nRT[…]」"),

dict(kind="计算", topic="临界 χ 与分相", ans=0,
 stem="For φ<sub>A</sub> = φ<sub>B</sub> = 0.5, N = 1000 and χ = 0.55, evaluate ΔG<sub>mix</sub>/(nRT), and decide whether the solution stays as one phase.",
 opts=["−0.209 — negative, yet the solution still phase separates",
       "−0.209 — negative, so it stays as one phase",
       "+0.209 — positive, so it phase separates",
       "+0.138 — positive, so it stays as one phase"],
 exp="""<p><b>熵项</b>：φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub>
= −0.3466 − 0.00035 = <b>−0.3469</b></p>
<p><b>焓项</b>：φ<sub>A</sub>φ<sub>B</sub>χ = 0.25 × 0.55 = <b>+0.1375</b></p>
<div class="fb">ΔG<sub>mix</sub>/(nRT) = −0.3469 + 0.1375 = <b>−0.209</b></div>
<p class="trap">⚠️ <b>ΔG &lt; 0 却仍然分相</b>——这正是本题的考点。<br>
对 N = 1000 的高分子，临界值 χ<sub>c</sub> = ½(1 + 1/√N)² ≈ <b>0.53</b>。
题给 χ = 0.55 已<b>超过</b>临界值，ΔG 曲线中间出现局部极大，
通过分相成两个 binodal 组成可以达到<b>更低</b>的能量。</p>
<p>ΔG<sub>mix</sub> &lt; 0 只说明"混合比完全不混合好"，<b>不等于"不分相"</b>。
判据永远是 ΔG 曲线的<b>凹凸性</b>，不是它的符号。（官方 Question 13 同一考点）</p>""",
 kp="高分子 χ_c = ½(1+1/√N)² ≈ 0.5；ΔG<0 不等于不分相，判据是曲线凹凸性",
 src="p.45；与 p.52–55（L4）联读"),

dict(kind="理解", topic="N 对溶解性的影响",
 stem="As N increases at fixed φ and χ, the entropic (favourable) term:",
 opts=["Increases without limit", "Approaches a finite limit determined by the <b>solvent</b> term alone",
       "Goes to zero", "Becomes positive"], ans=1,
 exp="""<p>ΔS<sub>mix</sub>/(nR) = −[φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/N)lnφ<sub>B</sub>]</p>
<p>N → ∞ 时第二项 → 0，剩下 <b>−φ<sub>A</sub>lnφ<sub>A</sub></b>——一个<b>有限的非零值</b>，
完全由溶剂贡献。</p>
<p class="trap"><b>不是趋于零</b>（选项 C）。哪怕链无限长，溶剂分子仍然可以在格子里到处跑，
这部分熵永远存在。这也是为什么再高分子量的高分子<b>仍然能溶</b>——只是需要更好的溶剂（更小的 χ）。</p>""",
 kp="N → ∞ 时混合熵趋于溶剂项的有限值，不是零", src="p.45"),

dict(kind="计算", topic="从体积分数反推链数",
 stem="A lattice of 2,000 sites has φ<sub>B</sub> = 0.30 with chains of N = 60. How many polymer chains are present?",
 opts=["6", "10", "60", "600"], ans=1,
 exp="""<p>高分子占据的格点数 = φ<sub>B</sub> × m = 0.30 × 2,000 = <b>600 个格点</b></p>
<div class="fb">m<sub>B</sub> = 600 / N = 600 / 60 = <b>10 条链</b></div>
<p class="trap"><b>陷阱</b>：选项 D（600）是<b>格点数</b>不是<b>链数</b>。
体积分数给的是"占多少格子"，要再除以 N 才是链的条数。</p>
<p>顺带：m<sub>A</sub> = 2000 − 600 = 1,400 个溶剂分子。</p>""",
 kp="φ_B·m 给出高分子占据的格点数，除以 N 才是链数", src="p.39「Volume fractions」"),

dict(kind="理解", topic="平均场近似的局限",
 stem="Which assumption is <b>NOT</b> made in the Flory-Huggins derivation as presented?",
 opts=["The polymer does not fold back onto previously occupied sites",
       "Each added monomer does not change the proportion of empty sites",
       "Empty sites are randomly distributed throughout the lattice",
       "The polymer chains are perfectly rigid rods"], ans=3,
 exp="""<p>讲义明确声明了前三条：<i>“assuming polymer does not turn back to previously occupied sites,
and that each added monomer does not affect the proportion of empty sites”</i>，
以及用 (m−iN)/m 作为空位概率所隐含的<b>均匀随机分布</b>假设。</p>
<p><b>D 是错的</b>——Flory-Huggins <b>不</b>假设链是刚性棒。恰恰相反，
它假设链是<b>柔性</b>的，可以在格子里任意走出蜿蜒路径。</p>
<p class="trap"><b>这些近似的代价</b>：在<b>稀溶液</b>中链周围其实是"空旷"的，
空位分布并不均匀，所以 Flory-Huggins 在稀溶液区的定量精度有限。</p>""",
 kp="FH 三条假设：不折回、空位比例不变、空位随机分布；链是柔性而非刚性",
 src="p.41「assuming polymer does not turn back…」"),

dict(kind="理解", topic="z 在最终结果中消失",
 stem="The coordination number z appears throughout the derivation but is absent from the final ΔS<sub>mix</sub>. This is because:",
 opts=["z was set to 1", "The (z−1) terms in S and in S<sub>B</sub> cancel when ΔS<sub>mix</sub> = S − S<sub>A</sub> − S<sub>B</sub> is formed",
       "z was approximated as infinite", "z only affects the enthalpy"], ans=1,
 exp="""<p>含 (z−1) 的项在总熵 S 和纯高分子熵 S<sub>B</sub> 中<b>形式完全相同</b>
（都是 <b>k m<sub>B</sub>(N−1) ln(z−1)</b>），相减时<b>精确抵消</b>。</p>
<p>讲义在推导之初就预告了这一点：<i>“Let the number of neighbouring site be z
(<b>the actual number does not matter</b>)”</i>。</p>
<p class="trap"><b>但 z 并没有真正消失</b>——它躲进了 <b>χ = zΔw/kT</b> 里，
在<b>焓</b>项中继续起作用。所以：<b>熵里 z 消失，焓里 z 藏在 χ 中</b>。</p>""",
 kp="z 在熵项中相消，但通过 χ = zΔw/kT 保留在焓项里",
 src="p.40「the actual number does not matter」；p.44 相减"),

dict(kind="计算", topic="混合焓（体积分数形式）", ans=0,
 stem="A polymer solution has φ<sub>B</sub> = 0.2, χ = 0.6, n = 3.0 mol of lattice sites, T = 300 K. What is ΔH<sub>mix</sub>?",
 opts=["0.72 kJ", "1.20 kJ", "2.39 kJ", "3.59 kJ"],
 exp="""<div class="fb">ΔH<sub>mix</sub> = φ<sub>A</sub>φ<sub>B</sub> χ n R T</div>
<p>φ<sub>A</sub> = 1 − 0.2 = 0.8，故 φ<sub>A</sub>φ<sub>B</sub> = 0.8 × 0.2 = <b>0.16</b></p>
<p>nRT = 3.0 × 8.314 × 300 = <b>7,483 J</b></p>
<p>ΔH = 0.16 × 0.6 × 7,483 = <b>718 J ≈ 0.72 kJ</b></p>
<p class="trap"><b>陷阱</b>：忘了算 φ<sub>A</sub> = 1 − φ<sub>B</sub>，直接用 0.2 会得到 0.9 kJ；
选项 D 是漏掉 φ<sub>A</sub>φ<sub>B</sub> 只乘 χ 的结果。</p>
<p><b>与 regular solution 的唯一差别</b>：把 x 换成 φ，其余形式完全一样——
因为<b>焓不受连接性影响</b>，只看局部接触。</p>""",
 kp="ΔH_mix = φ_A φ_B χ nRT，与 regular solution 同形式（x → φ）",
 src="p.45「ΔH_mix = φ_A φ_B χ nRT」"),

dict(kind="理解", topic="临界 χ 值的差异",
 stem="For a symmetric small-molecule regular solution the critical value is χ<sub>c</sub> = 2. For a polymer solution with large N, χ<sub>c</sub> is approximately:",
 opts=["2", "1", "0.5", "0"], ans=2,
 exp="""<p>对 Flory-Huggins，临界条件给出</p>
<div class="fb">χ<sub>c</sub> = ½ (1 + 1/√N)²　→　N → ∞ 时 χ<sub>c</sub> → <b>0.5</b></div>
<p><b>这个对比极具冲击力</b>：小分子要 χ 大于 <b>2</b> 才分相，
而高分子只要 χ 超过 <b>0.5</b> 就分相——<b>容忍度只有小分子的四分之一</b>。</p>
<p><b>原因</b>：高分子的混合熵只有小分子的一半左右，能"抵抗"的焓不利就少得多。</p>
<p class="trap"><b>实用推论</b>：χ = 0.5 正是<b>θ 溶剂</b>的条件（Lecture 5 的 B = 0）。
所以 <b>θ 溶剂恰好处在高分子溶解性的临界点上</b>——这不是巧合。</p>""",
 kp="高分子 χ_c → 0.5（小分子是 2）；χ = 0.5 恰是 θ 溶剂条件",
 src="p.45 与 p.60（L4）；对照 p.7（L5）θ solvent"),

dict(kind="理解", topic="为什么相图不对称",
 stem="Polymer solution phase diagrams are strongly <b>asymmetric</b> (skewed toward low φ<sub>B</sub>), unlike small-molecule ones. The mathematical origin is:",
 opts=["The χ term", "The φ<sub>B</sub>/N factor in the entropy term",
       "The temperature dependence of χ", "The volume fraction definition"], ans=1,
 exp="""<p>小分子的 ΔG<sub>mix</sub> 里 x<sub>A</sub>lnx<sub>A</sub> 和 x<sub>B</sub>lnx<sub>B</sub> <b>形式对称</b>，
所以曲线关于 x = 0.5 对称。</p>
<p>高分子里两项<b>不对称</b>：φ<sub>A</sub>lnφ<sub>A</sub> 对 <b>(φ<sub>B</sub>/N)lnφ<sub>B</sub></b>
——高分子项被 N 压扁了，所以 ΔG 曲线的极小值<b>偏向高 φ<sub>A</sub>（稀溶液）一侧</b>。</p>
<p>讲义在 Lecture 4 明确指出：<i>“real solutions (e.g. polymer solutions) are typically <b>non-symmetrical</b>”</i>，
并且 <i>“Phase diagram shifts towards <b>smaller φ<sub>B</sub></b> as N increases”</i>。</p>""",
 kp="φ_B/N 这一项破坏对称性 → 相图偏向稀溶液一侧",
 src="p.45；p.50 与 p.60（L4）"),

dict(kind="计算", topic="每摩尔格点的混合自由能",
 stem="Compare ΔG<sub>mix</sub>/(nRT) at φ<sub>B</sub> = 0.5, χ = 0, for (i) N = 1 and (ii) N = 10.",
 opts=["(i) −0.693, (ii) −0.381", "(i) −0.693, (ii) −0.069",
       "(i) −0.347, (ii) −0.381", "(i) −0.693, (ii) −0.693"], ans=0,
 exp="""<p>χ = 0，只剩熵项。</p>
<p><b>(i) N = 1</b>：−[0.5 ln0.5 + 0.5 ln0.5] → ΔG/(nRT) = <b>−0.693</b></p>
<p><b>(ii) N = 10</b>：φ<sub>A</sub>lnφ<sub>A</sub> + (φ<sub>B</sub>/10)lnφ<sub>B</sub>
= −0.3466 + (0.05)(−0.6931) = −0.3466 − 0.03466 = <b>−0.381</b></p>
<p>即便 N 只有 10，混合驱动力已经从 0.693 掉到 0.381（约 55%）。
<b>N 的削弱效应在很小的 N 就已经显著</b>。</p>""",
 kp="N 的削弱效应在 N ~ 10 就已明显；χ=0 时 ΔG 全部来自熵",
 src="p.45"),

dict(kind="理解", topic="Flory-Huggins 与 regular solution 的对应",
 stem="Setting N = 1 in the Flory-Huggins expression recovers:",
 opts=["The ideal gas law", "The regular solution expression from Lecture 2",
       "The Mark-Houwink equation", "Raoult's law"], ans=1,
 exp="""<p>令 N = 1，则 φ 就等于 x（每个"链"只占一个格点，体积分数 = 摩尔分数）：</p>
<div class="fb">ΔG<sub>mix</sub> = nRT[x<sub>A</sub>lnx<sub>A</sub> + x<sub>B</sub>lnx<sub>B</sub> + x<sub>A</sub>x<sub>B</sub>χ]</div>
<p>这正是 Lecture 2 的 <b>regular solution</b> 结果。</p>
<p><b>意义</b>：Flory-Huggins 是 regular solution 的<b>推广</b>，而不是另起炉灶。
N = 1 是它的特例，这也是检验记忆是否正确的好方法——
如果你记的公式在 N = 1 时回不到 regular solution，那一定记错了。</p>""",
 kp="N = 1 时 FH 退化为 regular solution；可用作公式自查",
 src="p.45 与 p.36 对照"),

dict(kind="理解", topic="高分子-高分子共混",
 stem="For a blend of <b>two polymers</b> A and B with degrees of polymerization N<sub>A</sub> and N<sub>B</sub>, the entropy term becomes −nR[(φ<sub>A</sub>/N<sub>A</sub>)lnφ<sub>A</sub> + (φ<sub>B</sub>/N<sub>B</sub>)lnφ<sub>B</sub>]. What does this imply?",
 opts=["Polymer blends mix more easily than polymer solutions",
       "Polymer blends are <b>much harder</b> to mix, since <b>both</b> terms are now suppressed",
       "The enthalpy term also gets divided", "Blends always form a single phase"], ans=1,
 exp="""<p>高分子溶液里只有<b>一</b>项被除以 N；高分子共混里<b>两</b>项都被除
→ 混合熵被削弱得更彻底。</p>
<p><b>后果</b>：绝大多数高分子对<b>互不相容</b>。这就是为什么：<br>
· 塑料回收中不同高分子必须<b>分开</b>，混在一起力学性能很差<br>
· 可混溶共混物（如讲义 Lecture 8 提到的 <b>PS/PPO</b>）非常<b>稀有</b>，往往需要特殊相互作用（χ &lt; 0）</p>
<p class="trap">Lecture 8 的 <b>Fox 方程</b>（共混物只有一个 T<sub>g</sub>）只对<b>可混溶</b>共混物成立；
不互溶的共混物会显示<b>两个</b> T<sub>g</sub>——这正是判断相容性的实验手段。</p>""",
 kp="两种高分子共混时两项都被 N 削弱 → 绝大多数高分子对不相容",
 src="p.45 的推广；p.14（L8）PS/PPO 可混溶共混"),

dict(kind="计算", topic="溶剂与高分子的摩尔比",
 stem="In a lattice with φ<sub>A</sub> = 0.5, φ<sub>B</sub> = 0.5 and N = 500, what is the ratio of the <b>number of solvent molecules</b> to the <b>number of polymer chains</b>?",
 opts=["1 : 1", "250 : 1", "500 : 1", "1 : 500"], ans=2,
 exp="""<p>设总格点 m = 1000。则 m<sub>A</sub> = 500 个溶剂分子，高分子占 500 个格点。</p>
<div class="fb">m<sub>B</sub> = 500 / N = 500 / 500 = <b>1 条链</b></div>
<p>比值 = 500 : 1</p>
<p><b>这个数字很说明问题</b>：体积上各占一半，但<b>分子个数</b>上溶剂是链的 500 倍。
熵是数"个数"的，所以溶剂在混合熵中占绝对主导——正好解释了前面几题的结论。</p>""",
 kp="等体积分数下溶剂分子数是链数的 N 倍；熵数个数，故溶剂主导",
 src="p.39「Volume fractions / Total number of lattice sites」"),

dict(kind="理解", topic="良溶剂 / 不良溶剂的 χ",
 stem="Which χ value corresponds to a <b>good</b> solvent for a high-N polymer?",
 opts=["χ = 0.1", "χ = 0.5", "χ = 1.0", "χ = 2.0"], ans=0,
 exp="""<p>高分子的临界值 <b>χ<sub>c</sub> ≈ 0.5</b>：</p>
<table class="mini"><thead><tr><th>χ</th><th>溶剂品质</th><th>链构象</th></tr></thead><tbody>
<tr><td><b>χ &lt; 0.5</b></td><td><b>良溶剂</b></td><td>膨胀，R<sub>g</sub> ∝ N<sup>3/5</sup></td></tr>
<tr><td>χ = 0.5</td><td><b>θ 溶剂</b></td><td>理想链，R<sub>g</sub> ∝ N<sup>1/2</sup></td></tr>
<tr><td>χ &gt; 0.5</td><td>不良溶剂</td><td>塌缩 / 分相</td></tr>
</tbody></table>
<p>χ = 0.1 明显小于 0.5 → <b>良溶剂</b>。</p>
<p class="trap"><b>把三讲串起来</b>：χ &lt; 0.5（L3）⟺ 第二维里系数 B &gt; 0（L5）⟺
Mark-Houwink a ≈ 0.8（L5）⟺ R<sub>g</sub> ∝ N<sup>3/5</sup>（L1）。<b>说的是同一件事。</b></p>""",
 kp="χ<0.5 良溶剂 / =0.5 θ 溶剂 / >0.5 不良；与 B、a、ν 一一对应",
 src="p.45；p.7（L5）θ solvent；p.17（L1）scaling"),

dict(kind="理解", topic="Flory-Huggins 的最终用途",
 stem="Within this course, the main use of the Flory-Huggins ΔG<sub>mix</sub> expression is to:",
 opts=["Predict the glass transition temperature",
       "Construct the <b>phase diagram</b> (binodal, spinodal, critical point) of polymer solutions",
       "Calculate the molecular weight from viscosity", "Determine crystal unit cell dimensions"], ans=1,
 exp="""<p>Lecture 4 全篇就是拿这个 ΔG<sub>mix</sub> 表达式去做三件事：</p>
<table class="mini"><thead><tr><th>目标</th><th>数学操作</th></tr></thead><tbody>
<tr><td><b>Binodal</b></td><td>对 ΔG 曲线作<b>公切线</b>，取两个切点</td></tr>
<tr><td><b>Spinodal</b></td><td>d²ΔG/dφ² = 0（拐点）</td></tr>
<tr><td><b>临界点</b></td><td>d³ΔG/dφ³ = 0（拐点合并）</td></tr>
</tbody></table>
<p>并由此得到两条 general conclusions：<b>N 增大 → T<sub>c</sub> 升高</b>、
<b>相图向更小的 φ<sub>B</sub> 移动</b>。</p>""",
 kp="FH 的 ΔG 是 L4 全部相图分析的输入", src="p.45 → p.55–60（L4）"),
]
