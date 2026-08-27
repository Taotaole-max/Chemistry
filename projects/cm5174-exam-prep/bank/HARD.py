# -*- coding: utf-8 -*-
LEC = 99
TITLE = "Advanced / Application-Oriented Problems"
CN = "进阶应用题"
SRC = "讲义 Lectures_1-10 综合"
L = [
# ============ A · 多步链式计算 ============
dict(kind="链式", topic="等摩尔 vs 等质量混合", ans=2, tag="L1",
 stem="Two blends are made from the same two fractions (10 kg/mol and 100 kg/mol). Blend <b>A</b> mixes them in <b>equal molar</b> amounts; blend <b>B</b> mixes them in <b>equal mass</b>. Which statement is correct?",
 opts=["Both blends have the same PDI, since they contain the same two species",
       "A has the larger PDI (1.67 vs 1.21)",
       "B has the larger PDI (3.02 vs 1.67)",
       "B has the smaller PDI because its M<sub>n</sub> is smaller"],
 exp="""<p><b>A（等摩尔）</b>：n₁ = n₂ = 1<br>
M<sub>n</sub> = (10+100)/2 = <b>55</b>；M<sub>w</sub> = (10²+100²)/(10+100) = 10100/110 = <b>91.8</b><br>
PDI = 91.8/55 = <b>1.67</b></p>
<p><b>B（等质量）</b>：设各取质量 m，则 n₁ = m/10，n₂ = m/100<br>
M<sub>n</sub> = 2m/(m/10 + m/100) = 2/0.11 = <b>18.2</b><br>
M<sub>w</sub> = (n₁·10² + n₂·100²)/(2m) = (10m + 100m)/2m = <b>55</b><br>
PDI = 55/18.2 = <b>3.02</b></p>
<p class="trap"><b>为什么等质量的分布反而"更宽"</b>：等质量意味着短链的<b>条数</b>是长链的 10 倍，
M<sub>n</sub> 被大量短链狠狠拉低（18.2），而 M<sub>w</sub> 仍被长链的质量撑住（55）。
两个平均被拉开，PDI 就大。</p>
<p><b>可迁移的直觉</b>：<b>M<sub>n</sub> 对低分子量端敏感，M<sub>w</sub> 对高分子量端敏感。</b>
任何让"短链条数多、长链质量重"的配方，PDI 都会大。</p>""",
 kp="等质量混合比等摩尔混合给出更宽的分布；Mn 敏感于低端、Mw 敏感于高端",
 src="p.6（L1）"),

dict(kind="链式", topic="从 C∞ 一路算到 [η]", ans=1, tag="L1→L5",
 stem="A polymer has C<sub>∞</sub> = 7.0, n = 5,000 backbone bonds of l = 1.54 Å, and M = 70,000 g/mol. Treating the coil as a hydrodynamically equivalent sphere with V<sub>h</sub> = (4/3)πR<sub>g</sub>³, estimate the intrinsic viscosity [η].",
 opts=["0.15 dL/g", "1.47 dL/g", "14.7 dL/g", "147 dL/g"],
 exp="""<p><b>四步链条，每一步都不能跳</b>：</p>
<p><b>① ⟨h²⟩ = C<sub>∞</sub>nl²</b> = 7.0 × 5,000 × 1.54² = <b>83,006 Å²</b></p>
<p><b>② R<sub>g</sub>² = ⟨h²⟩/6</b> = 13,834 Å² → R<sub>g</sub> = <b>117.6 Å</b></p>
<p><b>③ V<sub>h</sub> = (4/3)πR<sub>g</sub>³</b> = 4.19 × 1.63×10⁶ = <b>6.82×10⁶ Å³ = 6.82×10⁻¹⁸ cm³</b></p>
<p><b>④ [η] = (5/2)N<sub>Av</sub>V<sub>h</sub>/M</b> = 2.5 × 6.022×10²³ × 6.82×10⁻¹⁸ / 70,000
= <b>147 cm³/g = 1.47 dL/g</b></p>
<p class="trap"><b>两个单位陷阱</b>：<br>
· <b>Å³ → cm³ 要乘 10⁻²⁴</b>（1 Å = 10⁻⁸ cm，立方后是 10⁻²⁴）<br>
· <b>1 dL/g = 100 cm³/g</b>——选项 D（147 dL/g）就是忘了这一步</p>
<p><b>合理性检验</b>：柔性高分子的 [η] 典型值就是 <b>0.1–10 dL/g</b> 量级，1.47 落在正中。</p>""",
 kp="C∞ → ⟨h²⟩ → Rg → Vh → [η] 的完整链条；Å³→cm³ 乘 10⁻²⁴，1 dL/g = 100 cm³/g",
 src="p.12、p.16（L1）；p.13–14（L5）"),

dict(kind="链式", topic="两点法同时求 M 和 B", ans=0, tag="L5",
 stem="Osmotic data (Π/RT in mol/L, c in g/L): at c = 1.0, Π/RT = 6.0×10⁻⁵; at c = 5.0, Π/RT = 4.0×10⁻⁴. Determine M and the solvent quality.",
 opts=["M ≈ 18,000 g/mol; B &gt; 0, a good solvent",
       "M ≈ 18,000 g/mol; B &lt; 0, a poor solvent",
       "M ≈ 16,700 g/mol; B = 0, a theta solvent",
       "M ≈ 12,500 g/mol; B &gt; 0, a good solvent"],
 exp="""<p><b>关键第一步：先线性化。</b>把 Π/RT = c/M + Bc² <b>两边除以 c</b>：</p>
<div class="fb">(Π/RT)/c = 1/M + B·c</div>
<p>这样就变成一条<b>直线</b>，截距 1/M、斜率 B。</p>
<p><b>两点</b>：<br>
c = 1.0：(6.0×10⁻⁵)/1.0 = <b>6.0×10⁻⁵</b><br>
c = 5.0：(4.0×10⁻⁴)/5.0 = <b>8.0×10⁻⁵</b></p>
<p><b>斜率</b>：B = (8.0−6.0)×10⁻⁵ / (5.0−1.0) = <b>5.0×10⁻⁶</b>（<b>正</b> → 良溶剂）</p>
<p><b>截距</b>：1/M = 6.0×10⁻⁵ − 5.0×10⁻⁶×1.0 = 5.5×10⁻⁵ → <b>M = 18,200 g/mol</b></p>
<p class="trap"><b>最常见的错法</b>：直接拿 c = 1.0 那一点算 M = 1/(6×10⁻⁵) = 16,700（选项 C）。
<b>那一点还含有 Bc² 的贡献</b>，不是纯的 c/M。必须<b>外推到 c → 0</b>，
而两点法正是在做这件事。</p>
<p><b>顺带</b>：B &gt; 0 ⟺ χ &lt; 0.5 ⟺ ν = 3/5 ⟺ a ≈ 0.8，这四条同时成立。</p>""",
 kp="Π/RT 除以 c 线性化 → 截距 1/M、斜率 B；单点算 M 会因 Bc² 而偏小",
 src="p.6–7（L5）"),

dict(kind="链式", topic="临界温度：小分子与高分子相差多少", ans=3, tag="L2→L4",
 stem="Two systems have the same exchange energy, characterised by zΔw/k = 600 K. System X is a small-molecule mixture (χ<sub>c</sub> = 2); system Y is a solution of a polymer with N = 100. Estimate their critical temperatures.",
 opts=["X: 300 K, Y: 300 K", "X: 1200 K, Y: 300 K", "X: 300 K, Y: 496 K", "X: 300 K, Y: 992 K"],
 exp="""<p>由 χ = zΔw/(kT) = 600/T，令 χ = χ<sub>c</sub> 求 T<sub>c</sub>：</p>
<p><b>X（小分子）</b>：χ<sub>c</sub> = 2 → T<sub>c</sub> = 600/2 = <b>300 K</b></p>
<p><b>Y（高分子）</b>：χ<sub>c</sub> = ½(1 + 1/√N)² = ½(1 + 1/10)² = ½(1.21) = <b>0.605</b><br>
T<sub>c</sub> = 600/0.605 = <b>992 K</b></p>
<p class="trap"><b>这个 3 倍多的差距是本课最有冲击力的定量结论之一</b>：
<b>完全相同的分子间作用</b>，小分子在 300 K 以上就完全互溶，
而 N = 100 的高分子要到近 1000 K 才行——实际上早就分解了。</p>
<p><b>物理根源</b>：χ<sub>c</sub> 从 2 掉到 0.6，是因为高分子的<b>混合熵只有小分子的约一半</b>
（Flory-Huggins 里高分子项被 N 削弱），能"抵抗"的焓不利就少得多。</p>
<p><b>实际含义</b>：这就是为什么<b>高分子极难找到好溶剂</b>，而<b>两种高分子几乎必然不相容</b>
（共混时两项都被削弱，χ<sub>c</sub> 更小）。</p>""",
 kp="同样 Δw 下高分子 T_c 远高于小分子；根源是 χ_c 从 2 降到约 0.5",
 src="p.36（L2）；p.45（L3）；p.60（L4）"),

dict(kind="链式", topic="XRD 反推晶胞参数", ans=1, tag="L10",
 stem="Polyethylene has an orthorhombic unit cell with a = 7.42 Å and b = 4.95 Å. For an orthorhombic lattice, 1/d²<sub>hkl</sub> = h²/a² + k²/b² + l²/c². At what 2θ should the (110) reflection appear with Cu Kα (λ = 1.54 Å)?",
 opts=["10.8°", "21.6°", "24.0°", "36.3°"],
 exp="""<p><b>① 求面间距</b>（h=1, k=1, l=0）：</p>
<div class="fb">1/d² = 1/7.42² + 1/4.95² = 0.01816 + 0.04081 = 0.05897</div>
<p>d = 1/√0.05897 = <b>4.118 Å</b></p>
<p><b>② Bragg 定律</b>：sin θ = λ/(2d) = 1.54/(2×4.118) = 0.1870 → θ = 10.78°</p>
<p><b>③ 题目问 2θ</b>：2θ = <b>21.6°</b></p>
<p class="trap"><b>选项 A（10.8°）是忘了乘 2 的陷阱</b>——那是 θ 不是 2θ。</p>
<p><b>这题的价值在于交叉验证</b>：讲义在 XRD 那页给出的聚乙烯实测强峰正是
<b>2θ ≈ 21.5°</b>。我们从<b>晶胞参数</b>独立算出 21.6°，两者吻合
——这说明那个峰确实归属于 <b>(110) 晶面</b>。</p>
<p>这正是 XRD <b>指标化（indexing）</b>的实际做法：由候选晶胞算出各晶面的理论 2θ，
与实测峰位比对来确认归属。</p>""",
 kp="由晶胞参数算 d 再用 Bragg 求 2θ；这是 XRD 指标化的基本操作",
 src="p.42–46（L10）"),

dict(kind="链式", topic="片晶厚度造成的熔点压低", ans=2, tag="L10",
 stem="For polyethylene, T<sub>m</sub><sup>∞</sup> = 418 K, surface energy γ = 0.09 J/m², and ΔH<sub>V</sub><sup>b</sup> = 2.8×10⁸ J/m³. For a lamella of thickness l = 10 nm with r ≫ l (so 1/r is negligible), what is T<sub>m</sub>?",
 opts=["418 K (no change)", "405 K", "391 K", "352 K"],
 exp="""<div class="fb">T<sub>m</sub>/T<sub>m</sub><sup>∞</sup> = 1 − (2γ/ΔH<sub>V</sub><sup>b</sup>)(1/l + 1/r) ≈ 1 − (2γ/ΔH<sub>V</sub><sup>b</sup>)(1/l)</div>
<p><b>① 括号外的系数</b>：2γ/ΔH<sub>V</sub><sup>b</sup> = 0.18 / 2.8×10⁸ = <b>6.43×10⁻¹⁰ m</b>
（<b>注意它是一个长度</b>——量纲上必须如此才能和 1/l 相乘变成无量纲）</p>
<p><b>②</b> 6.43×10⁻¹⁰ / 10×10⁻⁹ = <b>0.0643</b></p>
<p><b>③</b> T<sub>m</sub> = 418 × (1 − 0.0643) = <b>391 K</b>，即熔点被压低了 <b>27 K</b></p>
<p class="trap"><b>量纲自查是这题的关键</b>：2γ/ΔH<sub>V</sub> 的单位是
(J/m²)/(J/m³) = <b>m</b>。它有个名字叫<b>特征长度</b>——当片晶厚度降到这个量级时，
表面能就会主导，晶体根本无法稳定存在。这里它约 0.64 nm，
所以 10 nm 的片晶已经"够厚"，只损失 6% 的熔点。</p>
<p><b>推论</b>：若 l 降到 2 nm，压低量变成 32%，T<sub>m</sub> 只剩 284 K——
这就是<b>低温结晶得到薄片晶、薄片晶熔点低</b>的定量版本。</p>""",
 kp="2γ/ΔH_V 是一个特征长度；片晶厚度接近它时熔点急剧下降",
 src="p.47–49（L10）"),

dict(kind="链式", topic="通用校准（k 与 a 都不同）", ans=2, tag="L7",
 stem="A polystyrene standard (k<sub>s</sub> = 1.2×10⁻⁴, a<sub>s</sub> = 0.72) of M<sub>s</sub> = 100,000 elutes at a given V<sub>R</sub>. An unknown polymer (k<sub>x</sub> = 4.9×10⁻⁴, a<sub>x</sub> = 0.68) elutes at the same V<sub>R</sub>. What is M<sub>x</sub>?",
 opts=["24,500 g/mol", "41,000 g/mol", "57,000 g/mol", "100,000 g/mol"],
 exp="""<div class="fb">k<sub>s</sub>M<sub>s</sub><sup>a<sub>s</sub>+1</sup> = k<sub>x</sub>M<sub>x</sub><sup>a<sub>x</sub>+1</sup></div>
<p><b>① 左边</b>：1.2×10⁻⁴ × (10⁵)<sup>1.72</sup><br>
(10⁵)<sup>1.72</sup> = 10<sup>8.6</sup> = 3.98×10⁸<br>
左边 = 1.2×10⁻⁴ × 3.98×10⁸ = <b>4.78×10⁴</b></p>
<p><b>②</b> M<sub>x</sub><sup>1.68</sup> = 4.78×10⁴ / 4.9×10⁻⁴ = <b>9.75×10⁷</b></p>
<p><b>③</b> M<sub>x</sub> = (9.75×10⁷)<sup>1/1.68</sup>：
log₁₀ = 7.989/1.68 = 4.755 → M<sub>x</sub> = 10<sup>4.755</sup> = <b>5.7×10⁴</b></p>
<p class="trap"><b>三处容易错</b>：<br>
① 指数是 <b>a+1</b> 不是 a<br>
② 两边的指数<b>不同</b>（1.72 vs 1.68），不能约掉<br>
③ 最后要开 <b>1/(a<sub>x</sub>+1)</b> 次方，不是 1/a<sub>x</sub></p>
<p><b>结果的意义</b>：如果直接用 PS 校准曲线读，会报 100,000；
通用校准修正后只有 57,000——<b>误差高达 75%</b>。
这就是为什么标样结构不同时必须做通用校准。</p>""",
 kp="通用校准三处易错：指数 a+1、两边指数不同、最后开 1/(a_x+1) 次方",
 src="p.36（L7）"),

dict(kind="链式", topic="Flory-Fox 两点定参数再外推", ans=1, tag="L8",
 stem="A polymer has T<sub>g</sub> = 358 K at M<sub>n</sub> = 10,000 and T<sub>g</sub> = 368 K at M<sub>n</sub> = 25,000. Predict T<sub>g</sub> at M<sub>n</sub> = 50,000.",
 opts=["369.7 K", "371.3 K", "374.7 K", "378.0 K"],
 exp="""<p><b>① 两式相减消掉 T<sub>g</sub>(∞)</b>：</p>
<div class="fb">368 − 358 = K(1/10⁴ − 1/2.5×10⁴) = K(1.0×10⁻⁴ − 4.0×10⁻⁵) = K × 6.0×10⁻⁵</div>
<p>K = 10 / 6.0×10⁻⁵ = <b>1.67×10⁵</b></p>
<p><b>② 回代求 T<sub>g</sub>(∞)</b>：358 = T<sub>g</sub>(∞) − 1.67×10⁵/10⁴ = T<sub>g</sub>(∞) − 16.7
→ T<sub>g</sub>(∞) = <b>374.7 K</b></p>
<p><b>③ 外推</b>：T<sub>g</sub>(5×10⁴) = 374.7 − 1.67×10⁵/5×10⁴ = 374.7 − 3.3 = <b>371.3 K</b></p>
<p class="trap"><b>选项 C（374.7 K）是把 T<sub>g</sub>(∞) 直接当成答案</b>——
那是 M<sub>n</sub> → ∞ 的极限值，50,000 还没到那里。</p>
<p><b>值得注意的收敛速度</b>：M<sub>n</sub> 从 10,000 → 25,000 → 50,000，
T<sub>g</sub> 是 358 → 368 → 371.3，离极限 374.7 越来越近但<b>越来越慢</b>（1/M<sub>n</sub> 的形状）。
所以<b>高分子量样品的 T<sub>g</sub> 几乎不随分子量变化</b>——这是工业上乐见的性质。</p>""",
 kp="两点相减消 T_g(∞) 求 K，再回代；T_g 随 M_n 按 1/M_n 收敛，高分子量时趋于平台",
 src="p.13（L8）"),

dict(kind="链式", topic="泊松比与体积变化", ans=1, tag="L9",
 stem="A polymer bar is stretched to 1.0% tensile strain. Its Poisson's ratio is ν = 0.35. To first order, by what percentage does its <b>volume</b> change?",
 opts=["0% (volume is conserved)", "+0.30%", "+1.0%", "−0.70%"],
 exp="""<p>拉伸方向伸长 ε，两个横向各收缩 νε。体积的相对变化（一阶近似）：</p>
<div class="fb">ΔV/V ≈ ε − 2νε = ε(1 − 2ν)</div>
<p>= 0.010 × (1 − 0.70) = 0.0030 = <b>+0.30%</b></p>
<p class="trap"><b>ν = 0.5 是体积不变的临界值</b>：<br>
· ν = 0.5 → ΔV/V = 0，<b>体积严格守恒</b>——<b>橡胶</b>接近这个值<br>
· ν &lt; 0.5 → 拉伸时体积<b>增大</b>——玻璃态高分子（ν ≈ 0.3–0.4）属于此类<br>
· ν 的理论上限就是 0.5（超过就意味着拉伸使体积减小，违反稳定性）</p>
<p><b>与熵弹性的呼应</b>：橡胶 ν ≈ 0.5 说明拉伸时<b>几乎不改变体积</b>，
只是把线团<b>舒展</b>——正对应 Lecture 10 的结论"应力几乎全部用于降熵，
不储存焓"。<b>体积不变 = 分子间距不变 = 没有拉伸化学键。</b></p>""",
 kp="ΔV/V ≈ ε(1−2ν)；ν=0.5 体积守恒（橡胶），玻璃态 ν≈0.35 拉伸增体积",
 src="p.18（L9）；p.38（L10）"),

dict(kind="链式", topic="绝热拉伸的温升", ans=1, tag="L10",
 stem="A rubber strip (A = 1.0 mm², E = 1.0 MPa, L₀ = 50 mm) is stretched adiabatically by L = 100 mm. Its heat capacity is C<sub>V,p</sub> = 0.50 J/K. Using C<sub>V,p</sub>ΔT = AEL²/(2L₀), what is ΔT?",
 opts=["−0.20 K (it cools)", "+0.20 K (it warms)", "+2.0 K", "+20 K"],
 exp="""<div class="fb">C<sub>V,p</sub>ΔT = AEL² / (2L₀)</div>
<p><b>单位统一到 SI</b>：A = 1.0×10⁻⁶ m²，E = 1.0×10⁶ Pa，L = 0.10 m，L₀ = 0.050 m</p>
<p>分子 = 1.0×10⁻⁶ × 1.0×10⁶ × (0.10)² = 1.0 × 0.010 = <b>0.010 J·m/m</b><br>
分母 = 2 × 0.050 = <b>0.10</b><br>
弹性功 = 0.010/0.10 = <b>0.10 J</b></p>
<p>ΔT = 0.10 / 0.50 = <b>+0.20 K</b>（<b>升温</b>）</p>
<p class="trap"><b>符号必须是正的</b>：式子右边全是正量（A、E、L²、L₀ 都为正），
所以 ΔT &gt; 0 是<b>数学上的必然</b>。选项 A 犯的是方向错误。</p>
<p><b>可以亲手验证</b>：迅速拉长橡皮筋贴到嘴唇上——<b>变热</b>；
保持拉伸等它散完热，再迅速松开贴嘴唇——<b>变凉</b>。
这是熵弹性最直接的宏观证据（也是橡胶热机的原理）。</p>
<p><b>0.2 K 虽小但可测</b>：用热电偶或红外测温都能看到。</p>""",
 kp="绝热拉伸必然升温（右边恒正）；松弛则降温，是熵弹性的直接证据",
 src="p.39（L10）"),

# ============ B · 逆向求解 ============
dict(kind="逆向", topic="Rg 翻倍需要多少 N", ans=0, tag="L1",
 stem="By what factor must the degree of polymerization increase to <b>double</b> R<sub>g</sub>, (i) in a good solvent and (ii) in a theta solvent?",
 opts=["(i) 3.2×　(ii) 4.0×", "(i) 4.0×　(ii) 3.2×", "(i) 2.0×　(ii) 2.0×", "(i) 8.0×　(ii) 4.0×"],
 exp="""<p>由 R<sub>g</sub> ∝ N<sup>ν</sup>，要求 R<sub>g</sub> 变 2 倍：<b>2 = f<sup>ν</sup> → f = 2<sup>1/ν</sup></b></p>
<p><b>(i) 良溶剂</b> ν = 3/5：f = 2<sup>1/0.6</sup> = 2<sup>1.667</sup> = <b>3.17 ≈ 3.2</b></p>
<p><b>(ii) θ 溶剂</b> ν = 1/2：f = 2<sup>1/0.5</sup> = 2² = <b>4.0</b></p>
<p class="trap"><b>方向别搞反</b>：<b>ν 越大，链越"会长"</b>，达到同样尺寸<b>需要的 N 越少</b>。
良溶剂 ν = 0.6 &gt; θ 溶剂 ν = 0.5，所以良溶剂只需 3.2 倍而 θ 溶剂需 4 倍。</p>
<p><b>换个角度看同一件事</b>：固定 N 把溶剂从 θ 换成良溶剂，链会<b>膨胀</b>；
所以在良溶剂里"用更少的单体就能撑到同样大"。</p>
<p><b>注意指数是 1/ν 不是 ν</b>——这是逆向题的核心。若算成 2<sup>0.6</sup> = 1.52 就完全错了。</p>""",
 kp="逆向标度：f = 2^(1/ν)；ν 越大所需 N 倍数越小",
 src="p.17（L1）"),

dict(kind="逆向", topic="混合熵降到 60% 对应的 N", ans=1, tag="L3",
 stem="At φ<sub>A</sub> = φ<sub>B</sub> = 0.5, what degree of polymerization N reduces ΔS<sub>mix</sub> to exactly <b>60%</b> of the small-molecule value?",
 opts=["N = 2", "N = 5", "N = 50", "N = 500"],
 exp="""<p><b>小分子（N=1）</b>：−2(0.5 ln0.5) = <b>0.6931</b>（×nR）<br>
<b>目标</b>：0.60 × 0.6931 = <b>0.4159</b></p>
<p><b>高分子</b>：−[0.5 ln0.5 + (0.5/N) ln0.5] = 0.34657 + <b>0.34657/N</b></p>
<p>令其等于 0.4159：0.34657/N = 0.0693 → <b>N = 5.0</b></p>
<p class="trap">⚠️ <b>这个答案会让很多人吃惊</b>：<b>N 只要 5</b>，混合熵就掉到只剩 60%。
不需要 N = 500 那么夸张。</p>
<p><b>为什么衰减这么快</b>：溶剂项 0.34657 是<b>固定</b>的下限，高分子项从 0.34657 起
按 1/N 衰减。N=2 时已掉到 75%，N=5 时 60%，N=10 时 55%，
<b>N→∞ 的极限是 50%</b>。</p>
<p><b>可迁移的结论</b>：<b>「高分子难溶」这个效应在很低的聚合度就已经基本饱和</b>。
从 N=10 到 N=10,000，混合熵只再降 5 个百分点。
所以真正让高分子量样品更难溶的，是<b>相图向稀溶液移动</b>那个效应，
而不是熵还在继续大幅下降。</p>""",
 kp="N=5 时混合熵已降到 60%；该效应在低 N 就饱和，极限是 50%",
 src="p.45（L3）"),

dict(kind="逆向", topic="从 Rg/Rh 判断构象", ans=2, tag="L1→L6",
 stem="Static light scattering gives R<sub>g</sub> = 50 nm and DLS gives R<sub>h</sub> = 33 nm for the same sample. What does the ratio tell you?",
 opts=["R<sub>g</sub>/R<sub>h</sub> ≈ 0.66 — the chain is a compact sphere",
       "R<sub>g</sub>/R<sub>h</sub> ≈ 1.5 — the chain is a rigid rod",
       "R<sub>g</sub>/R<sub>h</sub> ≈ 1.5 — the chain behaves as a random coil",
       "The two radii should be equal; the data must be wrong"],
 exp="""<p>R<sub>g</sub>/R<sub>h</sub> = 50/33 = <b>1.52</b></p>
<table class="mini"><thead><tr><th>构象</th><th>R<sub>g</sub>/R<sub>h</sub></th></tr></thead><tbody>
<tr><td>致密硬球</td><td>≈ <b>0.775</b></td></tr>
<tr><td><b>无规线团（理想链）</b></td><td>≈ <b>1.5</b></td></tr>
<tr><td>刚性棒</td><td><b>&gt; 2</b></td></tr>
</tbody></table>
<p>1.52 明确指向<b>无规线团</b>。</p>
<p class="trap"><b>为什么这个比值有意义</b>：两个半径量的是<b>不同的东西</b>——<br>
· <b>R<sub>g</sub></b>：质量<b>如何分布</b>（几何量）<br>
· <b>R<sub>h</sub></b>：拖着溶剂<b>怎么扩散</b>（流体力学量）<br>
线团内部有大量溶剂随之运动，使它在扩散上"显得"比几何尺寸小，故 R<sub>g</sub> &gt; R<sub>h</sub>。
致密球没有这种内部溶剂，比值就小于 1。</p>
<p><b>实用价值</b>：<b>单独一个半径说明不了构象，比值才行。</b>
所以现代仪器把 SLS 和 DLS 集成在一起，一次进样同时给出两者。
比值突然从 1.5 掉到 0.8，就说明链<b>塌缩</b>了（溶剂变差或蛋白质折叠）。</p>""",
 kp="Rg/Rh 是构象指纹：0.775 球 / 1.5 线团 / >2 棒；单个半径无法判断构象",
 src="p.13（L1）；p.25、p.31（L6）"),

dict(kind="逆向", topic="从 a 值反推整套溶液性质", ans=3, tag="L5 综合",
 stem="Viscometry on a polymer–solvent pair gives Mark-Houwink exponent a = 0.50. Which set of statements is <b>all correct</b> for this system?",
 opts=["ν = 0.5, B &gt; 0, χ &lt; 0.5, chain expanded",
       "ν = 0.6, B = 0, χ = 0.5, chain ideal",
       "ν = 0.5, B &lt; 0, χ &gt; 0.5, chain collapsed",
       "ν = 0.5, B = 0, χ = 0.5, chain behaves ideally — a theta solvent"],
 exp="""<p><b>由 a = 3ν − 1 反推</b>：0.50 = 3ν − 1 → <b>ν = 0.50</b></p>
<p>ν = 1/2 是<b>理想链</b>的标度 → 这是 <b>θ 溶剂</b>。整套等价说法随之全部确定：</p>
<table class="mini"><thead><tr><th>量</th><th>值</th><th>出自</th></tr></thead><tbody>
<tr><td>Mark-Houwink a</td><td><b>0.50</b></td><td>L5</td></tr>
<tr><td>标度指数 ν</td><td><b>1/2</b></td><td>L1</td></tr>
<tr><td>第二维里系数 B</td><td><b>0</b></td><td>L5</td></tr>
<tr><td>Flory-Huggins χ</td><td><b>0.5</b></td><td>L3</td></tr>
<tr><td>链构象</td><td><b>理想链</b>（排除体积与链-链吸引恰好抵消）</td><td>—</td></tr>
</tbody></table>
<p class="trap"><b>这是本课最高频的综合考点</b>：<b>看到任何一个，其余四个都成立</b>。
出题人很喜欢给你其中一个、问另外几个。</p>
<p><b>对照记住良溶剂那一套</b>：a ≈ 0.8、ν = 3/5、B &gt; 0、χ &lt; 0.5、链<b>膨胀</b>。</p>""",
 kp="θ 溶剂五种等价说法：a=0.5 / ν=1/2 / B=0 / χ=0.5 / 理想链",
 src="p.17（L1）；p.45（L3）；p.7、p.14（L5）"),

dict(kind="逆向", topic="从 MALDI 峰间距识别重复单元", ans=1, tag="L7",
 stem="A MALDI-TOF spectrum of an unknown polymer shows a regular series of peaks separated by exactly <b>44 Da</b>. What can you conclude?",
 opts=["The polymer has M<sub>n</sub> = 44 g/mol",
       "The <b>repeat unit</b> has a mass of 44 Da — consistent with poly(ethylene oxide), –CH₂CH₂O–",
       "The polymer is doubly charged", "The matrix contributes 44 Da to every peak"],
 exp="""<p>MALDI 几乎只产生<b>单电荷</b>离子，所以谱图横轴的 m/z <b>就是质量</b>。
相邻峰的差 = <b>相差一个重复单元</b>：</p>
<div class="fb">峰间距 = 重复单元质量 = <b>44 Da</b></div>
<p>44 对应 <b>–CH₂CH₂O–</b>（C₂H₄O = 24+4+16 = 44）→ <b>聚环氧乙烷 PEO</b>。</p>
<p class="trap"><b>这正是 MALDI 相对 SEC 的独特能力</b>：SEC 只能给出"分子量分布"这条曲线，
而 MALDI <b>把每一个聚合度都分开显示</b>，因此能读出：<br>
· <b>重复单元质量</b>（峰间距）<br>
· <b>端基质量</b>（某个峰的质量减去 n×44，再减去阳离子 Na⁺ 的 23）<br>
· <b>是否有副产物系列</b>（另一组间距相同但整体偏移的峰）</p>
<p><b>为什么选项 A 错</b>：44 是<b>间距</b>不是<b>绝对位置</b>。
M<sub>n</sub> 要由整个峰系列的丰度加权算出，通常是几千到几万。</p>
<p><b>顺带</b>：PEO 有极性醚氧，能配位 Na⁺，<b>正是 MALDI 适用的类型</b>；
换成聚乙烯就完全测不了。</p>""",
 kp="MALDI 峰间距 = 重复单元质量；扣掉 n×单元与阳离子质量可得端基",
 src="p.39–40（L7）"),

# ============ C · 判别与证伪 ============
dict(kind="判别", topic="哪条与 θ 溶剂矛盾", ans=3, tag="综合",
 stem="A polymer solution is claimed to be at its theta condition. Which observation would be <b>INCONSISTENT</b> with that claim?",
 opts=["The second virial coefficient B is zero",
       "The Mark-Houwink exponent is a = 0.5",
       "R<sub>g</sub> scales as N<sup>0.5</sup>",
       "The ratio R<sub>g</sub>/R<sub>h</sub> is measured to be 0.78"],
 exp="""<p>前三条都是 θ 条件的<b>标准表现</b>（B = 0、a = 0.5、ν = 1/2，三者等价）。</p>
<p><b>D 与之矛盾</b>：R<sub>g</sub>/R<sub>h</sub> ≈ <b>0.78 是致密硬球</b>的特征值。
θ 溶剂中链是<b>理想线团</b>，比值应该在 <b>1.5</b> 附近。</p>
<p class="trap"><b>0.78 意味着什么</b>：链已经<b>塌缩成致密球</b>——
这是<b>不良溶剂</b>（χ &gt; 0.5、B &lt; 0）的表现，比 θ 条件更差。</p>
<p><b>这类"找矛盾"题的解法</b>：把已知条件展开成一整套等价说法，
再逐条比对哪个对不上。θ 条件的完整清单：</p>
<div class="fb">a = 0.5　·　ν = 1/2　·　B = 0　·　χ = 0.5　·　R<sub>g</sub>/R<sub>h</sub> ≈ 1.5</div>""",
 kp="找矛盾题：把条件展开成等价清单再逐条比对；Rg/Rh=0.78 是塌缩球不是理想链",
 src="p.7、p.14（L5）；p.31（L6）"),

dict(kind="判别", topic="两个平均分子量能否推出分布", ans=2, tag="L5→L7",
 stem="Osmometry gives M<sub>n</sub> = 40,000 and light scattering gives M<sub>w</sub> = 120,000 for a sample. What can you legitimately conclude?",
 opts=["The sample contains exactly two species, of 40,000 and 120,000",
       "Half the chains are 40,000 and half are 120,000",
       "PDI = 3.0, so the distribution is broad — but the <b>shape</b> of the distribution cannot be determined",
       "The sample is monodisperse because both values were measurable"],
 exp="""<p>PDI = 120,000/40,000 = <b>3.0</b> → 按讲义分档属于<b>宽分布</b>（PDI &gt; 2）。</p>
<p class="trap"><b>但两个平均值绝不足以确定分布的形状。</b>
无穷多种不同形状的分布都可以给出同一对 (M<sub>n</sub>, M<sub>w</sub>)：<br>
· 一个宽而连续的单峰<br>
· 一个窄峰 + 一条高分子量长尾<br>
· 真正的双峰分布</p>
<p><b>要知道形状，必须用能给出整个分布的方法</b>：<b>SEC</b> 或 <b>MALDI-TOF</b>。
这正是这两种方法不可替代的价值。</p>
<p><b>为什么 A、B 错</b>：它们都在<b>假设</b>一个具体的分布形状，而数据不支持这种断言。
（顺带验算 B：等摩尔的 40k 和 120k 给 M<sub>n</sub> = 80,000，与题给的 40,000 不符，直接排除。）</p>
<p><b>可迁移的思维</b>：<b>平均值是分布的"矩"，有限个矩不能唯一确定分布。</b>
这在统计上是普适的。</p>""",
 kp="两个平均只给 PDI，不能定分布形状；要形状必须用 SEC 或 MALDI",
 src="p.6（L1）；p.7（L5）；p.26（L6）；p.34–40（L7）"),

dict(kind="判别", topic="ΔG<0 却分相", ans=1, tag="L4",
 stem="A mixture has ΔG<sub>mix</sub> &lt; 0 at its overall composition, yet it separates into two phases. Which statement correctly explains this?",
 opts=["The measurement of ΔG<sub>mix</sub> must be wrong — a negative ΔG<sub>mix</sub> forbids phase separation",
       "ΔG<sub>mix</sub> &lt; 0 only means mixing beats <b>complete</b> demixing; splitting into two binodal compositions can reach an <b>even lower</b> G",
       "Phase separation is driven by kinetics, not thermodynamics",
       "The two phases must have positive ΔG<sub>mix</sub> individually"],
 exp="""<p><b>要分清两个完全不同的比较</b>：</p>
<table class="mini"><thead><tr><th>比较对象</th><th>回答的问题</th><th>判据</th></tr></thead><tbody>
<tr><td>ΔG<sub>mix</sub> vs <b>0</b></td><td>"混合" 比 "完全不混" 好吗？</td><td>符号</td></tr>
<tr><td>曲线 vs <b>公切线</b></td><td>"单相" 比 "分成两相" 好吗？</td><td><b>曲率</b></td></tr>
</tbody></table>
<p>ΔG<sub>mix</sub> &lt; 0 只回答了<b>第一个</b>问题。分相与否取决于<b>第二个</b>——
即 ΔG 曲线在该组成处是否<b>凹向下</b>、能否画出一条更低的公切线。</p>
<p class="trap"><b>选项 C 是个很有迷惑性的错误</b>：分相在这里<b>恰恰是热力学驱动的</b>
（能量更低）。动力学只决定分相走<b>哪条路</b>（SD 还是 N&amp;G）和<b>多快</b>，
不决定<b>要不要</b>分。</p>
<p><b>官方 Question 13 就是这个考点</b>，讲义答案原文：
<i>"Phase separate (even when Gibbs energy of mixing is negative).
Even lower Gibbs energy can be achieved through phase separation."</i></p>""",
 kp="ΔG_mix 的符号与分相判据是两件事；分相由曲率/公切线决定，且是热力学驱动",
 src="p.52–55（L4）；官方 Question 13"),

dict(kind="判别", topic="哪种情况 MALDI 会误导", ans=0, tag="L7",
 stem="A broad-distribution polyester is measured by both SEC and MALDI-TOF. MALDI reports a <b>lower M<sub>w</sub> and a narrower PDI</b> than SEC. What is the most likely explanation?",
 opts=["MALDI systematically under-represents the <b>high-M tail</b> (harder to vaporize, may fragment, detector saturated by early-arriving small ions)",
       "SEC always overestimates molecular weight",
       "The polyester is too polar for MALDI",
       "MALDI measures M<sub>n</sub> while SEC measures M<sub>w</sub>"],
 exp="""<p>讲义列出 MALDI 测值偏低的<b>三条</b>原因（官方 Question 28 答案为"以上皆是"）：<br>
① 高分子量物种<b>更难汽化</b><br>
② 高分子量物种在解吸电离时<b>可能碎裂</b><br>
③ 检测器被<b>先到的小分子离子饱和</b>，对后到的大分子响应下降</p>
<p><b>三条都作用在高分子量端</b> → 高 M 尾巴被系统性削弱。</p>
<p class="trap"><b>为什么 PDI 也会变窄</b>：M<sub>w</sub> 对高分子量端的敏感度<b>远高于</b> M<sub>n</sub>
（M<sub>w</sub> 里有 M² 加权）。削掉高 M 尾巴，<b>M<sub>w</sub> 下降得比 M<sub>n</sub> 多</b>
→ 比值 M<sub>w</sub>/M<sub>n</sub> 变小 → <b>PDI 偏窄</b>。</p>
<p><b>选项 C 说反了</b>：聚酯<b>正是</b>含极性基团、适合 MALDI 的类型
（讲义点名 poly-esters, acrylates, amides）。<b>不适合的是 PE、PP。</b></p>
<p><b>实践结论</b>：<b>宽分布样品不要只信 MALDI</b>，
它在窄分布样品上准确，宽分布时应与 SEC 交叉验证。</p>""",
 kp="MALDI 三条偏低原因都在高 M 端 → Mw 降得比 Mn 多 → PDI 偏窄；宽分布须与 SEC 互验",
 src="p.39–40（L7）；官方 Question 28"),

dict(kind="判别", topic="快冷样品的哪个性质会漂移", ans=2, tag="L8",
 stem="A rapidly-quenched glassy sample is stored at room temperature (well below T<sub>g</sub>) for six months. Which change is expected?",
 opts=["It crystallizes into a semi-crystalline solid",
       "Its molecular weight decreases",
       "It slowly <b>contracts</b> toward the volume of a slowly-cooled sample — physical aging",
       "Nothing changes, because it is below T<sub>g</sub> and therefore frozen"],
 exp="""<p>讲义：<i>"If given sufficient time, a rapidly-cooled sample at rest will <b>contract</b> to give
volume of slowly-cooled sample – known as <b>aging</b> (<b>not desirable</b>)."</i></p>
<p><b>根本原因</b>：玻璃是<b>亚稳</b>的。快冷冻结下来的结构比平衡态<b>疏松</b>
（自由体积过剩），系统会自发地、缓慢地向更紧密的堆砌弛豫。</p>
<p class="trap"><b>选项 D 的想法很自然但不对</b>：低于 T<sub>g</sub> <b>不等于</b>完全冻结。
链段的大尺度运动确实被冻住了，但<b>局部的、微小的重排仍在以极慢的速率进行</b>
——正是这些微弱运动累积成老化。</p>
<p><b>工程后果</b>：老化过程中材料<b>密度上升、模量上升、韧性下降（变脆）</b>，
产品性能随存放时间<b>漂移</b>。这就是塑料件放久了容易脆裂的原因之一。</p>
<p><b>为什么测 T<sub>g</sub> 要取第二次扫描</b>：第一次升温正是为了<b>抹掉</b>
样品累积的这段热历史，否则测到的 T<sub>g</sub> 取决于样品放了多久。</p>""",
 kp="低于 T_g 不等于完全冻结；老化使密度与模量上升、变脆，故测 T_g 取第二次扫描",
 src="p.8（L8）"),

dict(kind="判别", topic="透明性能推出什么", ans=1, tag="L8→L10",
 stem="A polymer sample is completely <b>transparent</b>. Which conclusion is best supported?",
 opts=["It must have a very low molecular weight",
       "It has no crystalline domains large enough to scatter visible light — it is either fully amorphous, or its crystallites are far smaller than λ",
       "It must be crosslinked",
       "Its refractive index must be close to 1"],
 exp="""<p>散射的<b>唯一</b>根源是<b>折射率不均匀</b>。透明 → 光学上均一 → <b>没有足够大的折射率不均区域</b>。</p>
<p><b>两条路径都能给出透明</b>：<br>
① <b>完全无定形</b>（如无规立构 PS）——链无规堆砌但折射率处处相同<br>
② <b>有晶但晶粒远小于波长</b>——尺度不够，散射可忽略</p>
<p class="trap"><b>为什么不能直接断言"完全无定形"</b>：这正是本题的思考点。
讲义只讲了"半结晶发白"，但那默认晶粒尺度与可见光可比。
<b>把晶粒做到纳米级，半结晶高分子照样透明</b>——茂金属催化的低结晶度 PE 薄膜就是例子。</p>
<p><b>三个错误选项各错在哪</b>：<br>
· A：分子量与光学均一性<b>无关</b><br>
· C：交联与散射<b>无关</b>（交联的橡胶可以是透明的）<br>
· D：<b>绝对</b>折射率是多少不重要，重要的是<b>内部有没有差异</b>——
玻璃态 PMMA 的 n ≈ 1.49，一样透明</p>""",
 kp="透明 ⟸ 折射率均一；有晶但晶粒远小于 λ 也能透明，不能直接断言完全无定形",
 src="p.4（L8）；p.40（L10）；p.21（L6）"),

# ============ D · 数量级与标度推理 ============
dict(kind="标度", topic="溶剂品质对 [η] 的放大", ans=2, tag="L5",
 stem="For M = 10⁵ and assuming the same k, how many times larger is [η] in a good solvent (a = 0.80) than in a theta solvent (a = 0.50)?",
 opts=["1.6×", "5.0×", "32×", "300×"],
 exp="""<div class="fb">[η]<sub>good</sub>/[η]<sub>θ</sub> = M<sup>0.80</sup>/M<sup>0.50</sup> = M<sup>0.30</sup></div>
<p>= (10⁵)<sup>0.30</sup> = 10<sup>1.5</sup> = <b>31.6 ≈ 32</b></p>
<p class="trap"><b>0.3 的指数差看着不大，放到 10⁵ 上就是 32 倍</b>——
这是幂律最反直觉的地方。指数的<b>微小</b>差异，在<b>大自变量</b>下会被放大成数量级差异。</p>
<p><b>为什么这在实验上有用</b>：正因为放大效应这么强，
<b>粘度法对溶剂品质极其敏感</b>——测同一个样品在不同溶剂中的 [η]，
就能明确区分溶剂好坏。</p>
<p><b>但也是陷阱</b>：<b>k 和 a 必须成对使用</b>。
用查来的良溶剂 a 配上另一个溶剂测的 [η]，分子量能错出一个数量级。
讲义强调"k、a 需标定或查文献"正是这个意思。</p>
<p><b>物理图像</b>：良溶剂中链膨胀 → V<sub>h</sub> 大 → 同样质量占据更大的流体力学体积 → 更粘。</p>""",
 kp="指数差 0.3 在 M=10⁵ 时放大成 32 倍；k 与 a 必须成对使用",
 src="p.14–15（L5）"),

dict(kind="标度", topic="N 从 100 到 10000 熵变多少", ans=0, tag="L3",
 stem="At φ = 0.5, by what percentage does ΔS<sub>mix</sub> change when N increases from 100 to 10,000?",
 opts=["It drops by only about 1%", "It drops by about 50%",
       "It drops by about 99%", "It increases by about 1%"],
 exp="""<p>ΔS/(nR) = −[0.5 ln0.5 + (0.5/N) ln0.5] = 0.34657 + 0.34657/N</p>
<p><b>N = 100</b>：0.34657 + 0.003466 = <b>0.35004</b><br>
<b>N = 10,000</b>：0.34657 + 0.0000347 = <b>0.34661</b></p>
<p>比值 = 0.34661/0.35004 = <b>0.990</b> → 只降了约 <b>1%</b></p>
<p class="trap">⚠️ <b>这个结果对"分子量越高越难溶"的通常说法是个重要修正</b>。
N 增大 100 倍，混合熵<b>几乎没变</b>——因为固定的溶剂项 0.34657 已经占了绝对主导。</p>
<p><b>那为什么高分子量确实更难溶？</b>真正起作用的是<b>相图的形状</b>：</p>
<p>· χ<sub>c</sub> = ½(1+1/√N)²：N=100 时 0.605，N=10,000 时 <b>0.51</b>——<b>容忍度进一步收紧</b><br>
· 相图<b>向更小的 φ<sub>B</sub> 移动</b> → 只能配<b>更稀</b>的溶液</p>
<p><b>结论</b>：高 N 的困难不在"熵还在大幅下降"，
而在<b>临界 χ 逼近 0.5 这个硬下限</b>，以及<b>可溶浓度范围被压缩</b>。
理解这一层，就比只会背"N 大难溶"深了一个层次。</p>""",
 kp="N 从 100→10000 熵仅降 1%；高分子量的真正困难在 χ_c 逼近 0.5 与相图移向稀溶液",
 src="p.45（L3）；p.60（L4）"),

dict(kind="标度", topic="Rayleigh 与 λ 的四次方", ans=2, tag="L6",
 stem="A light scattering instrument is upgraded from a 633 nm (red) laser to a 442 nm (blue) laser. Ignoring changes in dn/dc, by what factor does the scattered intensity increase?",
 opts=["1.4×", "2.1×", "4.2×", "8.4×"],
 exp="""<div class="fb">I ∝ λ⁻⁴　⇒　I<sub>442</sub>/I<sub>633</sub> = (633/442)⁴</div>
<p>633/442 = 1.432；1.432² = 2.051；2.051² = <b>4.21</b></p>
<p class="trap"><b>三个错误选项正是三种"次方数错误"</b>：<br>
1.43 = 一次方　·　2.05 = 二次方　·　8.4 ≈ 三次方多</p>
<p><b>实验上的意义</b>：换成短波长激光，信号强度<b>翻两番</b>，
这对<b>低分子量样品</b>或<b>低浓度样品</b>意义重大（因为 I ∝ c·M<sub>w</sub>，本来就弱）。</p>
<p><b>但短波长有代价</b>：<br>
① <b>吸收</b>——很多高分子和溶剂在蓝紫区开始吸收，会引入荧光和加热<br>
② <b>q 变大</b>——q = (4πn/λ)sin(θ/2)，λ 变小则 q 变大，
意味着<b>粒子内干涉的修正项 q²R<sub>g</sub>²/3 更显著</b>，
对大粒子反而更难外推到 θ → 0</p>
<p>这就是为什么 633 nm 的 He-Ne 激光仍是光散射的常用光源——<b>是一个权衡而非单纯的优劣</b>。</p>""",
 kp="I ∝ λ⁻⁴，换短波长信号大增；但吸收与更大的 q 是代价",
 src="p.20–21、p.25（L6）"),

dict(kind="标度", topic="飞行时间与质量的平方根", ans=1, tag="L7",
 stem="In a MALDI-TOF instrument, two singly-charged ions differ in flight time by a factor of 1.5. What is their mass ratio?",
 opts=["1.5", "2.25", "3.0", "1.22"],
 exp="""<p>由 t ∝ √m，反过来 <b>m ∝ t²</b>：</p>
<div class="fb">m₂/m₁ = (t₂/t₁)² = 1.5² = <b>2.25</b></div>
<p class="trap"><b>正反两个方向都要会</b>：<br>
· 已知<b>质量</b>求<b>时间</b>：t ∝ <b>√m</b>（开方）<br>
· 已知<b>时间</b>求<b>质量</b>：m ∝ <b>t²</b>（平方）<br>
用反了就会选 1.22（= √1.5）或 1.5。</p>
<p><b>为什么是这个关系</b>：加速阶段 qV = ½mv²，同样电场同样电荷（单电荷）
→ v = √(2qV/m) ∝ 1/√m；飞行管长度 L 固定 → t = L/v ∝ √m。</p>
<p><b>分辨率的含义</b>：t ∝ √m 意味着<b>质量越大，相邻质量的时间差越小</b>——
所以 TOF 的<b>分辨率随质量增大而下降</b>。这也是 MALDI 在高分子量端表现变差的原因之一
（除了汽化难、碎裂、检测器饱和之外）。</p>""",
 kp="t ∝ √m 与 m ∝ t² 两个方向都要会；分辨率随质量增大而下降",
 src="p.40（L7）"),
]

L += [
# ============ E · 实验设计与方法选择 ============
dict(kind="设计", topic="给定目标选方法", ans=1, tag="L5→L7",
 stem="You must determine the <b>PDI</b> of an unknown <b>polypropylene</b> sample. Which approach works?",
 opts=["Membrane osmometry plus static light scattering, at room temperature in THF",
       "<b>High-temperature SEC</b> (e.g. trichlorobenzene at ~140 °C) with proper calibration",
       "MALDI-TOF-MS with a Na⁺ salt and an aromatic matrix",
       "Dynamic light scattering, which gives both M<sub>n</sub> and M<sub>w</sub>"],
 exp="""<p><b>要 PDI 就要同时知道 M<sub>n</sub> 和 M<sub>w</sub></b>。逐项排查两个约束——
<b>需要什么量</b>和<b>样品有什么限制</b>：</p>
<p><b>C 错</b>：聚丙烯<b>非极性</b>，没有能配位 Na⁺ 的位点，<b>无法有效电离</b>。
讲义明确把 poly-ethylene、propylene 排除在 MALDI 之外。</p>
<p><b>D 错</b>：<b>DLS 根本不给分子量</b>，它给的是 R<sub>h</sub>。这是最高频的混淆点。</p>
<p><b>A 部分对但不可行</b>：原理上渗透压给 M<sub>n</sub>、光散射给 M<sub>w</sub>，确实能算 PDI。
但 <b>PP 在室温下不溶于 THF</b>——半结晶的聚烯烃室温下几乎不溶于任何溶剂。</p>
<p><b>B 正确</b>：必须<b>高温</b>把晶区熔掉才能溶解，这就是<b>高温 GPC</b>存在的理由。</p>
<p class="trap"><b>这类题的思路</b>：先问"要什么量"（→ 缩到 SEC/MALDI），
再问"样品允许吗"（→ 排除 MALDI，且必须高温）。<b>两个筛子都要过。</b></p>""",
 kp="选方法要过两道筛：需要什么量 + 样品有什么限制；聚烯烃必须高温 GPC",
 src="p.7（L5）；p.34–40（L7）；p.3（L8）"),

dict(kind="设计", topic="如何提高光散射信噪比", ans=2, tag="L6",
 stem="A light scattering measurement on a low-M<sub>w</sub> polymer gives a very weak signal. Which change would give the largest improvement <b>without</b> invalidating the measurement?",
 opts=["Raise the concentration well above the dilute regime",
       "Use a solvent whose refractive index closely matches the polymer",
       "<b>Choose a solvent whose refractive index differs strongly from the polymer</b>, maximizing dn/dc",
       "Measure only at θ = 180°"],
 exp="""<p>散射强度 <b>I ∝ (dn/dc)² · c · M<sub>w</sub></b>。逐项分析：</p>
<p><b>C 正确</b>：dn/dc 以<b>平方</b>进入，是最有效的杠杆，且讲义明确要求
<i>"dn/dc should be as large as possible to get highest signal strength"</i>。
折射率差越大，dn/dc 越大。</p>
<p><b>B 恰恰相反</b>：折射率匹配 → dn/dc → 0 → <b>信号消失</b>（样品"隐形"）。</p>
<p class="trap"><b>A 是最有迷惑性的错误</b>：提高浓度确实增大 I（I ∝ c），
但会<b>让测量失效</b>——讲义要求"浓度要低使粒子作为<b>独立散射体</b>"。
浓度高时 2Bc 修正项变大、粒子间相互干涉，<b>外推到 c→0 就不可靠了</b>。
题干特意写了 "without invalidating the measurement"。</p>
<p><b>D 无意义</b>：(1+cos²θ) 在 0° 和 180° 都等于 2，180° 并不比其他角度强；
而且大粒子在<b>后向</b>散射反而<b>更弱</b>（干涉），还必须多角度外推到 θ→0。</p>""",
 kp="dn/dc 以平方进入，是最有效杠杆；提高浓度会破坏「独立散射体」前提",
 src="p.21、p.26（L6）；官方 Question 23"),

dict(kind="设计", topic="区分可混溶与不互溶共混", ans=0, tag="L8",
 stem="You blend two polymers and need to know whether they are miscible. The quickest reliable experiment is:",
 opts=["Run DSC and count the number of glass transitions",
       "Measure the molecular weight by SEC",
       "Measure the intrinsic viscosity in a good solvent",
       "Record an XRD pattern"],
 exp="""<table class="mini"><thead><tr><th>DSC 观察</th><th>结论</th></tr></thead><tbody>
<tr><td><b>一个</b> T<sub>g</sub>，介于两组分之间（符合 Fox 方程）</td><td><b>可混溶</b>（单相）</td></tr>
<tr><td><b>两个</b> T<sub>g</sub>，各自接近纯组分</td><td><b>不互溶</b>（相分离）</td></tr>
</tbody></table>
<p>讲义给的 PS/PPO 图正是<b>可混溶</b>体系的例子——只有一个 T<sub>g</sub>，随组成连续移动。</p>
<p class="trap"><b>为什么其他三个不行</b>：<br>
· <b>SEC</b>：测的是<b>各组分自己的</b>分子量，与它们混不混<b>无关</b><br>
· <b>粘度</b>：在<b>溶液</b>中测，共混物一旦溶解就分开了，<b>丢失了固态的相信息</b><br>
· <b>XRD</b>：只看<b>结晶</b>；两个都是无定形的共混物在 XRD 上看不出区别</p>
<p><b>为什么"数 T<sub>g</sub> 个数"这么有效</b>：T<sub>g</sub> 是<b>相</b>的性质。
有几个相，就有几个 T<sub>g</sub>。这把"相容性"这个抽象问题变成了<b>数峰</b>的操作。</p>
<p><b>联系 L3</b>：由于共混时<b>两项</b>混合熵都被 N 削弱，
<b>绝大多数高分子对不相容</b>——看到两个 T<sub>g</sub> 才是常态。</p>""",
 kp="DSC 数 T_g 个数判相容性；T_g 是相的性质，有几相就有几个 T_g",
 src="p.14（L8）；p.45（L3）"),

dict(kind="设计", topic="UCST 还是 LCST 与对策", ans=2, tag="L4",
 stem="A polymer solution is clear at 20 °C, turns cloudy at 55 °C, and clears again on cooling. To <b>redissolve</b> it at 55 °C you should:",
 opts=["Heat it further, since this is UCST behaviour",
       "Add more polymer to raise the concentration",
       "<b>Dilute it</b> — the one-phase region extends to lower φ<sub>B</sub>; heating would make it worse since this is LCST behaviour",
       "Nothing can be done; the polymer has degraded"],
 exp="""<p><b>① 判断类型</b>：<b>升温变浑、降温变清</b> → 单相区在<b>低温</b>一侧 → <b>LCST</b>。</p>
<p><b>② 排除"继续加热"</b>：LCST 体系升温使 χ <b>更正</b>（χ = α/T + β，α&lt;0、β&gt;0），
分相<b>更严重</b>。选项 A 把它当成 UCST 了。</p>
<p><b>③ 为什么稀释有效</b>：不论 UCST 还是 LCST，<b>相图都是有限宽度的两相区</b>，
两侧仍是单相。把组成移到 binodal <b>之外</b>就回到单相。
而高分子相图<b>本来就偏向小 φ<sub>B</sub></b>（N 越大越明显），
所以<b>往稀的方向走</b>是可靠的出路。</p>
<p class="trap"><b>选项 B 恰好走反方向</b>——提高浓度是往两相区中心走。</p>
<p><b>典型体系</b>：讲义点名 <b>PEO/水</b>。机理是靠<b>氢键</b>溶解，
氢键<b>随温度升高而变弱</b> → 高温时溶剂-高分子作用变差 → 分相。
（这也是很多水溶性高分子加热会析出的原因。）</p>""",
 kp="升温变浑 = LCST；对策是稀释而非加热；PEO/水靠氢键，氢键随温度减弱",
 src="p.61（L4）"),

dict(kind="设计", topic="为什么必须双重外推", ans=3, tag="L6",
 stem="In a rigorous static light scattering experiment on a <b>large</b> polymer, why must one extrapolate to <b>both</b> c → 0 and θ → 0?",
 opts=["To reduce random noise in the detector",
       "Because the laser power drifts with time",
       "Only c → 0 is needed; the θ dependence carries no information",
       "<b>c → 0 removes the 2Bc interparticle term; θ → 0 removes the intraparticle interference term q²R<sub>g</sub>²/3</b>"],
 exp="""<p>完整的工作方程里有<b>两个</b>需要消除的修正项，来源完全不同：</p>
<div class="fb">Kc/R<sub>θ</sub> = (1/M<sub>w</sub>)(1 + q²R<sub>g</sub>²/3 + ⋯) + 2Bc + ⋯</div>
<table class="mini"><thead><tr><th>修正项</th><th>来源</th><th>如何消除</th></tr></thead><tbody>
<tr><td><b>2Bc</b></td><td><b>粒子之间</b>的相互作用</td><td><b>c → 0</b>（无限稀释）</td></tr>
<tr><td><b>q²R<sub>g</sub>²/3</b></td><td><b>同一粒子内部</b>不同部位的相消干涉</td><td><b>θ → 0</b>（q → 0）</td></tr>
</tbody></table>
<p>两者<b>互不替代</b>：稀释再多也消不掉粒子内干涉；测到 0° 也消不掉浓度效应。
只有双重外推后的<b>截距</b>才是真正的 <b>1/M<sub>w</sub></b>。</p>
<p class="trap"><b>选项 C 正好丢掉了最有价值的信息</b>：θ 依赖的<b>斜率</b>给出的正是 <b>R<sub>g</sub></b>。
如果只做 c → 0 而不测角度依赖，就<b>得不到 R<sub>g</sub></b>，
静态光散射的一半价值就没了。</p>
<p><b>Zimm 图</b>就是把 c 和 θ 两个外推画在<b>同一张图</b>上的经典做法——
两族直线交汇于一点，那个交点就是 1/M<sub>w</sub>。</p>""",
 kp="2Bc 靠 c→0 消除（粒子间）、q²Rg²/3 靠 θ→0 消除（粒子内）；后者的斜率给 Rg",
 src="p.23、p.25–26（L6）"),

# ============ F · 跨讲综合 ============
dict(kind="综合", topic="一条链的四种尺度", ans=1, tag="L1",
 stem="For a polyethylene chain of M = 140,000 g/mol, the contour length is 15,000 Å, the RMS end-to-end distance is 212 Å, and the densely-packed cube edge is 64 Å. Which statement about R<sub>g</sub> is correct?",
 opts=["R<sub>g</sub> ≈ 212 Å, equal to the RMS end-to-end distance",
       "R<sub>g</sub> ≈ 87 Å, i.e. the RMS end-to-end distance divided by √6",
       "R<sub>g</sub> ≈ 64 Å, equal to the cube edge",
       "R<sub>g</sub> ≈ 15,000 Å, since R<sub>g</sub> measures the full extent of the chain"],
 exp="""<div class="fb">R<sub>g</sub> = ⟨h²⟩<sup>1/2</sup> / √6 = 212 / 2.449 = <b>86.6 ≈ 87 Å</b></div>
<p><b>把四个尺度排成序列，物理图像就清楚了</b>：</p>
<table class="mini"><thead><tr><th>尺度</th><th>数值</th><th>含义</th></tr></thead><tbody>
<tr><td>伸直长度</td><td><b>15,000 Å</b></td><td>完全拉直的理论上限</td></tr>
<tr><td>RMS 末端距</td><td><b>212 Å</b></td><td>线团的首尾距离</td></tr>
<tr><td><b>R<sub>g</sub></b></td><td><b>87 Å</b></td><td>单体到质心的均方根距离</td></tr>
<tr><td>密堆积立方体</td><td><b>64 Å</b></td><td>完全压实的下限</td></tr>
</tbody></table>
<p class="trap"><b>R<sub>g</sub> 落在 212 和 64 之间，这很关键</b>：<br>
· 比末端距<b>小</b>——因为量的是"到中心"而非"两端之间"<br>
· 比密堆积立方体<b>大</b>——线团内部有大量溶剂，并非实心</p>
<p><b>选项 D 的错误值得强调</b>：R<sub>g</sub> 是<b>均方根平均</b>，
<b>不代表最大空间尺度</b>——总有单体比 R<sub>g</sub> 更远（官方 Question 5 就考这个）。</p>
<p><b>一句话</b>：真实的溶液构象是个<b>蓬松的球</b>，既不是棍（15,000 Å），
也不是实心块（64 Å）。</p>""",
 kp="四种尺度的排序：伸直 ≫ 末端距 > Rg > 密堆积；Rg 不是最大空间尺度",
 src="p.13、p.16–17（L1）；官方 Question 2–5"),

dict(kind="综合", topic="橡胶为什么升温变硬", ans=2, tag="L10",
 stem="A steel wire under constant load <b>expands</b> when heated, but a stretched rubber band under constant load <b>contracts</b> when heated. The fundamental reason is:",
 opts=["Rubber has a negative thermal expansion coefficient in all directions",
       "The rubber crystallizes on heating",
       "<b>Steel elasticity is enthalpic (bond stretching); rubber elasticity is entropic — heating strengthens the entropic restoring force</b>",
       "The rubber band is below its T<sub>g</sub>"],
 exp="""<p><b>两种弹性的根本区别</b>：</p>
<table class="mini"><thead><tr><th></th><th>钢丝</th><th>橡胶</th></tr></thead><tbody>
<tr><td>弹性来源</td><td><b>焓弹性</b>——拉伸原子间<b>键</b></td><td><b>熵弹性</b>——舒展<b>构象</b></td></tr>
<tr><td>储存的是</td><td>焓（键能）</td><td>几乎不储存焓，(∂H/∂L) ≈ 0</td></tr>
<tr><td>升温</td><td>热振动削弱键 → <b>变软、伸长</b></td><td>回复力 ∝ T → <b>变硬、收缩</b></td></tr>
</tbody></table>
<p><b>定量依据</b>：由 f = (∂H/∂L) − T(∂S/∂L)，橡胶的截距 (∂H/∂L) ≈ 0，故</p>
<div class="fb">f ≈ −T(∂S/∂L)<sub>p,T</sub>　——<b>回复力正比于绝对温度 T</b></div>
<p>拉伸使熵下降（(∂S/∂L) &lt; 0），所以 f &gt; 0；<b>T 越高这个力越大</b>
→ 恒定负载下橡胶必须<b>收缩</b>才能重新平衡。</p>
<p class="trap"><b>选项 D 恰好说反</b>：橡胶<b>必须高于 T<sub>g</sub></b> 才有熵弹性。
低于 T<sub>g</sub> 它就变成玻璃，行为反而<b>像钢</b>（能量弹性）——
这正是 f–T 曲线在低温处出现<b>反转点</b>的原因。</p>""",
 kp="焓弹性升温变软、熵弹性升温变硬；f ∝ T 是熵弹性的标志",
 src="p.36–38（L10）"),

dict(kind="综合", topic="同一个 B 为何出现在两处", ans=1, tag="L5→L6",
 stem="The second virial coefficient B appears in <b>both</b> the osmotic pressure equation and the light scattering equation. Why?",
 opts=["It is a coincidence of notation; they are different quantities",
       "<b>Both techniques probe concentration fluctuations</b>; B measures how strongly the solution resists them",
       "Both use the same laser wavelength",
       "B is a universal constant equal to 1/M"],
 exp="""<p>讲义在光散射一节明确写着 <i>"containing the virial coefficient <b>in osmotic pressure equation</b>"</i>
——<b>是同一个 B</b>。</p>
<p><b>共同的物理内核</b>：溶液散射的推导基于 <b>Smoluchowski 和 Einstein 的粒子涨落理论</b>
（讲义原话）——散射<b>不是</b>各分子独立贡献的加和，而是来自<b>局部浓度涨落</b>造成的折射率不均。</p>
<table class="mini"><thead><tr><th>方法</th><th>直接测</th><th>B 的角色</th></tr></thead><tbody>
<tr><td><b>渗透压</b></td><td>化学势对浓度的响应</td><td>非理想性的一阶修正</td></tr>
<tr><td><b>光散射</b></td><td>浓度涨落的均方大小</td><td>抵抗涨落的能力</td></tr>
</tbody></table>
<p><b>直观理解</b>：<b>B 大（良溶剂）→ 溶液"不愿意"出现浓度不均 → 涨落被压制 → 散射弱</b>；
这正是散射式中 B 出现在<b>分母</b>（1/M<sub>w</sub> + 2Bc）的原因。</p>
<p class="trap"><b>推论</b>：<b>良溶剂中散射反而更弱</b>。
所以做光散射时，溶剂选择要在"dn/dc 要大"和"B 不要太大"之间权衡
——这是选项 A 那种"只是记号巧合"的想法完全看不到的层次。</p>""",
 kp="B 在两处是同一个量，因为两者都探测浓度涨落；良溶剂 B 大则散射弱",
 src="p.6–7（L5）；p.23（L6）"),

dict(kind="综合", topic="链端的两次出场", ans=3, tag="L8→L10",
 stem="Chain ends lower <b>both</b> T<sub>g</sub> and T<sub>m</sub>, but through different mechanisms. Which pairing is correct?",
 opts=["Both through excess free volume",
       "Both through colligative (impurity) effects",
       "T<sub>g</sub> through impurity effect; T<sub>m</sub> through free volume",
       "<b>T<sub>g</sub> through excess free volume; T<sub>m</sub> through the colligative (impurity) effect</b>"],
 exp="""<table class="mini"><thead><tr><th></th><th>机理</th><th>关系式</th></tr></thead><tbody>
<tr><td><b>T<sub>g</sub></b>（L8）</td><td>链端处<b>自由体积过剩</b>，链段更易运动</td><td>T<sub>g</sub> = T<sub>g</sub>(∞) − K/M<sub>n</sub></td></tr>
<tr><td><b>T<sub>m</sub></b>（L10）</td><td>链端<b>相当于杂质</b>，凝固点降低（依数性）</td><td>2M₀/M<sub>n</sub> = (ΔH<sub>m</sub>/nR)(1/T<sub>m</sub> − 1/T<sub>m</sub><sup>∞</sup>)</td></tr>
</tbody></table>
<p><b>两条推导路径完全不同</b>：<br>
· T<sub>g</sub> 走的是<b>自由体积/动力学</b>论证——链端周围松散，链段活动性高<br>
· T<sub>m</sub> 走的是<b>热力学依数性</b>论证——从 μ = μ* + RT ln x<sub>A</sub> 出发，
与凝固点降低<b>完全同源</b>（回到 L2 的 Raoult 定律）</p>
<p class="trap"><b>但两者的数学形式都是 1/M<sub>n</sub></b>，都用 <b>M<sub>n</sub></b>
（因为链端数正比于<b>链的条数</b>），也都在高分子量时趋于平台。
<b>形式相同、机理不同</b>——这正是这道题想区分的。</p>
<p><b>注意 T<sub>m</sub> 式中的因子 2</b>：每条链有<b>两个</b>端，故 x<sub>B</sub> = 2M₀/M<sub>n</sub>。</p>""",
 kp="T_g 靠自由体积、T_m 靠依数性；形式都是 1/M_n 且都用 Mn，但机理不同",
 src="p.13（L8）；p.50–51（L10）"),

dict(kind="综合", topic="随机行走的两个化身", ans=2, tag="L1→L6",
 stem="The DLS lecture defines D<sub>t</sub> = Nl²/(6t) for a particle taking N steps of length l, and refers back to the derivation of the polymer end-to-end distance. What is the shared mathematical core?",
 opts=["Both use Stirling's approximation",
       "Both rely on Bragg's law",
       "<b>Both are random walks: squaring the sum makes the cross terms vanish because ⟨cos θ⟩ = 0, leaving ⟨R²⟩ = Nl²</b>",
       "Both assume the steps are all in the same direction"],
 exp="""<p><b>同一个数学问题的两个物理化身</b>：</p>
<table class="mini"><thead><tr><th></th><th>随机行走发生在</th><th>结果</th></tr></thead><tbody>
<tr><td><b>L1 末端距</b></td><td><b>空间</b>——链段一步步接下去</td><td>⟨h²⟩ = nl²</td></tr>
<tr><td><b>L6 布朗运动</b></td><td><b>时间</b>——粒子一步步走</td><td>⟨r²⟩ = Nl²，D<sub>t</sub> = Nl²/6t</td></tr>
</tbody></table>
<p><b>共同的推导</b>：把矢量和平方展开，得 N 个自点积（每个 = l²）加上所有交叉项；
交叉项 = l²⟨cos θ⟩，因方向<b>完全随机</b>而<b>平均为零</b>。剩下 <b>Nl²</b>。</p>
<p class="trap"><b>关键是 l 的平方</b>：因为求的是<b>均方</b>位移。
写成 Nl（一次方）就错了——那是<b>伸直长度</b>／<b>总路程</b>，完全不同的量。</p>
<p><b>由此得到的普适结论</b>：随机行走的<b>净位移 ∝ √N</b>，而<b>总路程 ∝ N</b>。
两者的比值 √N/N = 1/√N 随 N 增大而减小——这就是为什么长链的线团
比伸直链<b>小两个数量级</b>（本讲第一题算过：15,000 Å vs 212 Å，比值约 √n = √10⁴ = 100）。</p>""",
 kp="随机行走 ⟨R²⟩ = Nl² 出现在空间（链）与时间（扩散）两处；净位移 ∝ √N",
 src="p.9–10（L1）；p.31（L6）；官方 Question 25"),

dict(kind="综合", topic="加工方式决定结晶形貌", ans=0, tag="L9→L10",
 stem="Textbook pictures of polymer crystals usually show <b>spherulites</b>, yet the crystalline morphology inside an extruded or spun product is often quite different. Why?",
 opts=["<b>Processing involves flow, and crystallization under flow gives oriented shish kebab structures rather than spherulites</b>",
       "Processed polymers do not crystallize at all",
       "Spherulites only form above T<sub>m</sub>",
       "Extrusion destroys the unit cell"],
 exp="""<p>讲义在形貌一页明确标注：<b>Shish kebab</b> of polyethylene —
<i>"when crystallized <b>during flow</b>"</i>；而 <b>Spherulite</b> —
<i>"by nucleation and growth"</i>（即<b>静置</b>条件下的常规产物）。</p>
<p><b>关键在于：所有的加工工艺都涉及流动</b>——挤出、注塑、纺丝、吹塑（Lecture 9 全篇）。
流动使部分链沿流向<b>伸展并结晶</b>成中心的"串"，其余链再垂直于它长出片晶"肉块"。</p>
<p class="trap"><b>这解释了教科书与实物的落差</b>：球晶是<b>实验室静置结晶</b>的产物，
<b>工业制品几乎从不是</b>。</p>
<p><b>为什么这很重要——纤维强度的来源</b>：<br>
熔融纺丝中 <b>godets 拉伸</b>使链高度取向（L9），形成串晶结构（L10），
沿纤维轴方向全是<b>共价键</b>承力 → 强度和模量大幅提高。
<b>未拉伸的纤维强度很低。</b></p>
<p><b>四种形貌的条件</b>：球晶（常规成核生长）· hedrite（片晶从中心张开）·
枝晶（<b>深过冷</b>）· <b>串晶（流动下）</b>。</p>""",
 kp="加工必涉流动 → 串晶而非球晶；纺丝的拉伸取向是纤维强度的来源",
 src="p.29（L9）；p.52–53（L10）"),

# ============ G · 陷阱换皮（同一个坑，新场景） ============
dict(kind="陷阱", topic="非四面体键角", ans=2, tag="L1",
 stem="A conjugated polymer has a backbone bond angle of <b>120°</b> (sp²). For a fixed-bond-angle, freely-rotating chain, ⟨h²⟩ equals how many times nl²?",
 opts=["0.33", "1.0", "3.0", "2.0"],
 exp="""<div class="fb">⟨h²⟩ = nl² · (1 + cos θ)/(1 − cos θ)</div>
<p><b>θ 是键角的补角</b>：θ = 180° − 120° = <b>60°</b>，cos 60° = <b>0.500</b></p>
<p>因子 = (1 + 0.5)/(1 − 0.5) = 1.5/0.5 = <b>3.0</b></p>
<p class="trap">⚠️ <b>换了角度，同一个坑还在</b>：<br>
· 若直接代 cos 120° = <b>−0.5</b>，得 (0.5)/(1.5) = <b>0.33</b>（选项 A）——差 9 倍<br>
· 选项 D（2.0）是把 sp³ 的结果直接搬过来</p>
<p><b>物理意义值得体会</b>：键角从 109.5° 张到 120°，因子从 2.0 升到 3.0
——<b>键角越"平"（越接近 180°），链越伸展</b>。极限情形键角 = 180°（完全伸直）时
cos θ = cos 0° = 1，因子 → <b>∞</b>，正对应刚性棒。</p>
<p><b>反向检验</b>：键角 = 90° 时 θ = 90°，cos = 0，因子 = 1
——退化回<b>自由连接链</b>。这个自洽性检查可以帮你确认公式没记反。</p>""",
 kp="θ = 180° − 键角；键角越接近 180° 链越伸展，90° 时退化为自由连接链",
 src="p.11–12（L1）；官方 Question 4"),

dict(kind="陷阱", topic="Fox 方程用摄氏度的后果", ans=3, tag="L8",
 stem="A student applies the Fox equation to a 50:50 blend of A (T<sub>g</sub> = 100 °C) and B (T<sub>g</sub> = −40 °C) using <b>Celsius</b> values directly. What happens?",
 opts=["The answer is correct, since Fox is a ratio equation",
       "The answer is 30 °C, the correct value",
       "The answer is too high by about 10 °C",
       "<b>The calculation breaks down</b> — 1/T<sub>g</sub> = 0.5/100 + 0.5/(−40) gives a <b>negative</b> value and a meaningless T<sub>g</sub>"],
 exp="""<p><b>用摄氏度硬算</b>：1/T<sub>g</sub> = 0.5/100 + 0.5/(−40) = 0.005 − 0.0125 = <b>−0.0075</b><br>
→ T<sub>g</sub> = <b>−133</b>，一个毫无物理意义的数。</p>
<p><b>正确做法（绝对温度）</b>：T<sub>g(A)</sub> = 373 K，T<sub>g(B)</sub> = 233 K<br>
1/T<sub>g</sub> = 0.5/373 + 0.5/233 = 0.001340 + 0.002146 = 0.003486<br>
T<sub>g</sub> = <b>286.8 K = 13.7 °C</b></p>
<p class="trap"><b>选项 B（30 °C）是"线性加权"的结果</b>：0.5(100) + 0.5(−40) = 30。
<b>Fox 不是线性加权</b>，是<b>倒数的加权平均</b>，结果<b>总是低于</b>线性值
（13.7 （13.8 &lt; 30，低了 16 度）lt; 30，低了 16 度）。</p>
<p><b>为什么负温度这么危险</b>：摄氏度的<b>零点是人为选的</b>，
而 Fox 方程里 T 出现在<b>分母</b>，只有<b>绝对</b>温标才有物理意义。
<b>凡是把温度放进分母或做乘除的公式，一律先换 K。</b></p>
<p><b>同类的公式</b>：χ = zΔw/kT、Π = RTc/M、Flory-Fox、Arrhenius……全都如此。</p>""",
 kp="温度进分母的公式一律用 K；Fox 是倒数加权，结果恒低于线性加权",
 src="p.14（L8）"),

dict(kind="陷阱", topic="渗透压的单位陷阱", ans=1, tag="L5",
 stem="A student computes Π = RTc/M with c = 8.0 g/L, M = 40,000 g/mol, T = 300 K and reports Π = 0.50 Pa. What went wrong, and what is the correct answer?",
 opts=["Nothing is wrong; 0.50 Pa is correct",
       "<b>c must be in g/m³ (8.0 g/L = 8,000 g/m³); Π = 499 Pa</b>",
       "T should be in Celsius; Π = 45 Pa",
       "M must be in kg/mol; Π = 0.50 kPa"],
 exp="""<p><b>正确计算</b>：c = 8.0 g/L = <b>8,000 g/m³</b></p>
<div class="fb">Π = 8.314 × 300 × (8,000 / 40,000) = 2,494 × 0.20 = <b>499 Pa</b></div>
<p>学生用 8.0 g/L 直接代入，<b>差了 1000 倍</b>。</p>
<p class="trap"><b>为什么必须是 g/m³</b>：<br>
R 的单位是 <b>J·K⁻¹·mol⁻¹ = Pa·m³·K⁻¹·mol⁻¹</b>。<br>
要让 RT·(c/M) 得到 <b>Pa</b>，c/M 必须是 <b>mol/m³</b>，故 c 必须是 <b>g/m³</b>。<br>
<b>SI 制里体积单位是 m³ 不是 L。</b></p>
<p><b>一个快速的合理性检查</b>：499 Pa 对应液柱高度<br>
h = Π/(ρg) = 499/9810 = <b>5.1 cm</b>——正是渗透计上肉眼可读的高度。<br>
而 0.50 Pa 只对应 <b>0.05 mm</b>，根本没法测量。
<b>算出的结果如果在实验上不可测，多半是单位错了。</b></p>
<p><b>选项 C 的错误更严重</b>：热力学公式中的 T <b>永远</b>是绝对温度。</p>""",
 kp="Π 公式中 c 用 g/m³（1 g/L = 1000 g/m³）；用液柱高度做合理性检查",
 src="p.6（L5）"),

dict(kind="陷阱", topic="Mw 分母写错的后果", ans=2, tag="L1",
 stem="For a sample of 3 mol at 20 kg/mol and 1 mol at 60 kg/mol, a student computes M<sub>w</sub> = [3(20²) + 1(60²)]/(3+1) = 1,200 kg/mol. What is the correct M<sub>w</sub>, and how could the error have been caught instantly?",
 opts=["1,200 kg/mol; there is no error",
       "30 kg/mol; the error is using M<sub>i</sub> instead of M<sub>i</sub>²",
       "<b>40 kg/mol; M<sub>w</sub> can never exceed the largest species present (60 kg/mol)</b>",
       "24 kg/mol; the error is that M<sub>n</sub> and M<sub>w</sub> were swapped"],
 exp="""<p><b>正确计算</b>：分母必须是 <b>Σn<sub>i</sub>M<sub>i</sub></b>（总质量），不是 Σn<sub>i</sub>：</p>
<div class="fb">M<sub>w</sub> = [3(400) + 1(3600)] / [3(20) + 1(60)] = 4800 / 120 = <b>40 kg/mol</b></div>
<p>（顺带 M<sub>n</sub> = 120/4 = 30 kg/mol，PDI = 40/30 = 1.33，合理。）</p>
<p class="trap"><b>最快的自查：任何平均分子量都必须落在最小值与最大值之间。</b><br>
样品里只有 20 和 60，所以 <b>20 ≤ M<sub>n</sub>, M<sub>w</sub> ≤ 60</b>。
算出 1,200 <b>远超最大组分</b>，<b>一眼就知道错了</b>，根本不用检查过程。</p>
<p><b>第二道自查</b>：<b>M<sub>w</sub> ≥ M<sub>n</sub> 且 PDI ≥ 1</b> 恒成立。
若算出 PDI &lt; 1，一定是分母写错了。</p>
<p><b>把这两条自查记住</b>：考试时算完扫一眼，能挡掉绝大多数分子量计算的粗心错误。
比重算一遍快得多。</p>""",
 kp="两条自查：平均值必在最小与最大组分之间；Mw ≥ Mn 即 PDI ≥ 1",
 src="p.6（L1）"),

dict(kind="陷阱", topic="2θ 与 θ 在两处出现", ans=3, tag="L6→L10",
 stem="Both the DLS scattering vector q = (4πn/λ)sin(θ/2) and Bragg's law 2D sinθ = nλ involve an angle. Which statement is correct?",
 opts=["Both formulas take the full experimentally-measured scattering angle directly",
       "Both formulas require the measured angle to be halved first",
       "q takes the full angle; Bragg takes half the measured angle",
       "<b>q uses half the scattering angle (θ/2); Bragg uses θ, but XRD data are reported as 2θ, so that measured value must be halved</b>"],
 exp="""<table class="mini"><thead><tr><th></th><th>实验测到的角</th><th>公式里用的</th><th>操作</th></tr></thead><tbody>
<tr><td><b>DLS / SLS</b></td><td>散射角 θ</td><td><b>sin(θ/2)</b></td><td>代入时<b>除以 2</b></td></tr>
<tr><td><b>XRD</b></td><td>衍射角 <b>2θ</b></td><td>sin <b>θ</b></td><td>先<b>除以 2</b> 再取 sin</td></tr>
</tbody></table>
<p><b>两处都要"除以 2"，但来源不同</b>：<br>
· 光散射里 <b>θ/2 是公式本身的形式</b>（来自散射矢量的几何推导）<br>
· XRD 里是因为<b>数据的记录习惯</b>是 2θ（入射与反射各成 θ，故偏折 2θ）</p>
<p class="trap"><b>这是本课唯一两处涉及角度的计算，都设了同一个坑。</b>
考试时看到角度，第一反应应该是："这是测量角还是公式角？"</p>
<p><b>验算示例</b>：λ = 633 nm、n = 1.33、θ = 90° →
q = (4π×1.33/633 nm)×sin45° = 2.64×10⁷ × 0.707 = <b>1.87×10⁷ m⁻¹</b>。
若漏掉 /2 用 sin90° = 1，会得 2.64×10⁷，偏大 41%。</p>""",
 kp="DLS 用 sin(θ/2)（公式本身）、XRD 给 2θ 需先除 2（记录习惯）；两处都要除以 2",
 src="p.25（L6）；p.44（L10）"),
]
