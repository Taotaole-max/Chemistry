# Part B5 配图：镀层防腐、PBR、智能材料、压电/热释电/热电、绿光激光笔、ZT、LiC6、硫化物电解质、液/固电解质
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, Ellipse
from common import *


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def b5_1():
    fig = plt.figure(figsize=(15, 6.4))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 0.42])
    for k, (coat, ccol, title, anode_is_coat) in enumerate([
            ("Zn", "#b0bec5", "(a) 镀锌铁（白铁皮）：划伤后 Zn 牺牲", True),
            ("Sn", "#e0e0e0", "(b) 镀锡铁（马口铁）：划伤后 Fe 加速腐蚀", False)]):
        ax = fig.add_subplot(gs[k]); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8.6)
        ax.set_title(title, fontsize=11.5)
        ax.add_patch(Rectangle((0.5, 0.8), 9, 2.6, fc="#8d6e63", ec="k"))
        ax.text(5, 1.6, "Fe 基体", ha="center", color="white", fontsize=11)
        ax.add_patch(Rectangle((0.5, 3.4), 3.8, 0.8, fc=ccol, ec="k")); ax.add_patch(Rectangle((5.7, 3.4), 3.8, 0.8, fc=ccol, ec="k"))
        ax.add_patch(Rectangle((4.3, 3.4), 1.4, 0.8, fc="#e3f2fd", ec="none", alpha=0.8))
        ax.text(2.4, 3.8, f"{coat} 镀层", ha="center", fontsize=10); ax.text(7.6, 3.8, f"{coat} 镀层", ha="center", fontsize=10)
        ax.add_patch(Rectangle((0.5, 4.2), 9, 2.1, fc="#e3f2fd", ec="none", alpha=0.8))
        ax.text(9.3, 6.0, "水膜 + O₂", ha="right", fontsize=9.5, color="#1565c0")
        ax.text(5, 3.0, "划痕", ha="center", fontsize=9.5, color="white")
        if anode_is_coat:
            ax.text(2.2, 5.1, "阳极（Zn 表面）：\nZn → Zn²⁺ + 2e⁻", ha="center", fontsize=9.3, color=C_RED)
            ax.text(5.6, 5.1, "阴极（裸露 Fe）：\nO₂ + 2H₂O + 4e⁻ → 4OH⁻", ha="left", fontsize=9.3, color=C_BLUE)
            ax.annotate("", xy=(4.9, 3.2), xytext=(2.6, 3.2), arrowprops=dict(arrowstyle="-|>", color="#ffeb3b", lw=2.2))
            ax.text(3.6, 2.75, "e⁻", color="#ffeb3b", fontsize=11)
            ax.text(5, 7.4, "Zn（−0.76 V）比 Fe 活泼 → Zn 作阳极被消耗\nFe 作阴极受保护（阴极保护 / 牺牲阳极）", ha="center", fontsize=10)
        else:
            ax.add_patch(Polygon([(4.3, 3.4), (5.7, 3.4), (5.3, 2.5), (4.7, 2.5)], fc="#4e342e", ec="k"))
            ax.text(4.4, 5.1, "阳极（划痕 Fe）：\nFe → Fe²⁺ + 2e⁻", ha="right", fontsize=9.3, color=C_RED)
            ax.text(7.6, 5.1, "阴极（Sn 表面）：\nO₂ + 2H₂O\n+ 4e⁻ → 4OH⁻", ha="center", fontsize=9.3, color=C_BLUE)
            ax.annotate("", xy=(7.5, 3.2), xytext=(5.4, 3.0), arrowprops=dict(arrowstyle="-|>", color="#ffeb3b", lw=2.2))
            ax.text(6.3, 2.6, "e⁻", color="#ffeb3b", fontsize=11)
            ax.text(5, 7.4, "Sn（−0.14 V）比 Fe 惰性 → 小面积 Fe 作阳极\n大面积 Sn 作阴极 → 划痕处点蚀反而更快", ha="center", fontsize=10)
    ax = fig.add_subplot(gs[2])
    pots = [("Zn²⁺/Zn", -0.76, C_GRAY), ("Fe²⁺/Fe", -0.44, "#8d6e63"), ("Sn²⁺/Sn", -0.14, "#9e9e9e")]
    ax.axvline(0.5, color="k", lw=1.2)
    for lab, E, c in pots:
        ax.plot([0.35, 0.65], [E, E], color=c, lw=4)
        ax.text(0.7, E, f"{lab}  {E} V", va="center", fontsize=10)
    ax.set_ylim(-0.9, 0.0); ax.set_xlim(0, 2.2); ax.set_xticks([])
    ax.set_ylabel("E° / V（vs SHE）"); ax.set_title("标准电极电势", fontsize=11)
    ax.text(0.05, -0.86, "↓ 更活泼（易被氧化）", fontsize=9)
    clean(ax)
    save(fig, "B5_01_zinc_vs_tin_coating.png")


def b5_2():
    data = {"Na": (61.98, 2.27, 22.99, 0.968, 2), "Ca": (56.08, 3.34, 40.08, 1.55, 1), "Mg": (40.30, 3.58, 24.305, 1.738, 1),
            "Al": (101.96, 3.95, 26.98, 2.70, 2), "Sn": (150.7, 7.0, 118.7, 7.3, 1), "Zn": (81.38, 5.61, 65.38, 7.14, 1),
            "Cu": (143.09, 6.0, 63.55, 8.96, 2), "Ni": (74.69, 6.67, 58.69, 8.91, 1), "Fe": (159.69, 5.24, 55.85, 7.87, 2),
            "W": (231.84, 7.16, 183.84, 19.25, 1)}
    oxide = {"Na": "Na₂O", "Ca": "CaO", "Mg": "MgO", "Al": "Al₂O₃", "Sn": "SnO₂", "Zn": "ZnO", "Cu": "Cu₂O", "Ni": "NiO",
             "Fe": "Fe₂O₃", "W": "WO₃"}
    names = list(data)
    pbr = [d[0] * d[3] / (d[4] * d[2] * d[1]) for d in data.values()]
    fig, ax = plt.subplots(figsize=(13, 5.4))
    ax.axhspan(0, 1, color=C_RED, alpha=0.08); ax.axhspan(1, 2, color=C_GREEN, alpha=0.1); ax.axhspan(2, 3.8, color=C_ORANGE, alpha=0.1)
    cols = [C_RED if p < 1 else (C_GREEN if p < 2 else C_ORANGE) for p in pbr]
    b = ax.bar(range(len(names)), pbr, color=cols, width=0.6, edgecolor=["k" if n == "Sn" else "none" for n in names], lw=2)
    for i, (n, p) in enumerate(zip(names, pbr)):
        ax.text(i, p + 0.06, f"{p:.2f}", ha="center", fontsize=10, fontweight="bold" if n == "Sn" else None)
    ax.set_xticks(range(len(names))); ax.set_xticklabels([f"{n}\n{oxide[n]}" for n in names], fontsize=9.5)
    ax.set_ylabel("PBR = V(氧化物) / V(消耗的金属)")
    ax.text(9.8, 0.5, "PBR < 1：膜不连续、多孔\n→ 不保护（Na、Ca、Mg）", fontsize=9.5, ha="left", va="center", color=C_RED)
    ax.text(9.8, 1.5, "1 < PBR < 2：致密、轻微压应力\n→ 钝化保护（Al、Sn、Ni…）", fontsize=9.5, ha="left", va="center", color=C_GREEN)
    ax.text(9.8, 2.9, "PBR > 2：压应力过大\n→ 起皱、剥落（Fe₂O₃、WO₃）", fontsize=9.5, ha="left", va="center", color="#b06000")
    ax.set_xlim(-0.6, 12.6); ax.set_ylim(0, 3.8); ax.set_title("Pilling–Bedworth 比（由密度计算，Sn 为本题）", fontsize=12)
    clean(ax)
    save(fig, "B5_02_pilling_bedworth_ratio.png")


def b5_3():
    fig, ax = plt.subplots(figsize=(14, 7.2)); ax.axis("off"); ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    rows = [("机械应力 / 压力", "压电材料\nPZT、石英 SiO₂", "电压（电荷）\n（逆效应：电压 → 形变）", "燃气灶点火器、石英表振子、\n超声探头、喷墨打印头"),
            ("温度变化", "形状记忆合金\nNiTi（Nitinol）", "形状恢复（相变：\n马氏体 ⇌ 奥氏体）", "血管支架、眼镜框、\n温控驱动器"),
            ("光照（UV）/ 温度", "光致变色 / 热致变色\nAgCl 掺杂玻璃、VO₂", "颜色 / 透光率改变\n（VO₂：68 °C 金属–绝缘体转变）", "变色眼镜片、\n智能窗（调光玻璃）"),
            ("电压", "电致变色\nWO₃", "颜色 / 透光率改变\n（Li⁺/H⁺ 嵌入 → 蓝色 MₓWO₃）", "Boeing 787 舷窗、\n防眩后视镜"),
            ("磁场", "磁致伸缩\nTerfenol-D（Tb₀.₃Dy₀.₇Fe₂）", "形变（应变）", "声呐、精密执行器")]
    ax.text(1.5, 9.6, "输入", ha="center", fontsize=12, fontweight="bold")
    ax.text(5.0, 9.6, "智能材料", ha="center", fontsize=12, fontweight="bold")
    ax.text(8.6, 9.6, "输出", ha="center", fontsize=12, fontweight="bold")
    ax.text(12.0, 9.6, "典型应用", ha="center", fontsize=12, fontweight="bold")
    for k, (i, m, o, a) in enumerate(rows):
        y = 8.4 - k * 1.85
        hl = k < 3
        fbox(ax, 1.5, y, 2.6, 1.2, i, fc="#fff3e0", ec=C_ORANGE, fs=10)
        fbox(ax, 5.0, y, 3.4, 1.4, m, fc="#eef3fb" if hl else "#f5f5f5", ec=C_BLUE if hl else "#999", fs=10)
        fbox(ax, 8.6, y, 3.2, 1.4, o, fc="#e8f5e9", ec=C_GREEN, fs=9.5)
        ax.text(10.5, y, a, va="center", fontsize=9.6)
        farrow(ax, (2.85, y), (3.25, y)); farrow(ax, (6.75, y), (6.95, y))
    ax.text(0.1, 0.1, "前三行即题目要求的“三种智能材料”，后两行供补充", fontsize=9.5, color=C_GRAY)
    save(fig, "B5_03_smart_materials_input_output.png")


def b5_4a():
    fig, axs = plt.subplots(1, 4, figsize=(16, 5.2), gridspec_kw=dict(width_ratios=[1, 1, 1.15, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.set_title("(a1) 压电效应", fontsize=11.5)
    ax.add_patch(Rectangle((1.5, 2.5), 3, 2.6, fc="#e1bee7", ec="k"))
    for x in np.linspace(1.8, 4.2, 5):
        ax.text(x, 5.3, "+", ha="center", fontsize=13, color=C_RED); ax.text(x, 2.05, "−", ha="center", fontsize=15, color=C_BLUE)
    ax.annotate("", xy=(3, 5.8), xytext=(3, 7.0), arrowprops=dict(arrowstyle="-|>", lw=2.5))
    ax.annotate("", xy=(3, 1.8), xytext=(3, 0.6), arrowprops=dict(arrowstyle="-|>", lw=2.5))
    ax.text(3.3, 6.6, "F", fontsize=12); ax.text(3.3, 0.8, "F", fontsize=12)
    ax.text(3, 3.8, "非中心对称\n晶体", ha="center", fontsize=10)
    ax.text(3, -0.4, "应力 → 正负电荷中心相对位移\n→ 表面出现电荷/电压（可逆）", ha="center", fontsize=9.5, va="top")
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.set_title("(a2) 热释电效应", fontsize=11.5)
    ax.add_patch(Rectangle((1.5, 2.5), 3, 2.6, fc="#ffe0b2", ec="k"))
    for x in np.linspace(1.9, 4.1, 4):
        ax.annotate("", xy=(x, 4.8), xytext=(x, 2.8), arrowprops=dict(arrowstyle="-|>", color=C_PURPLE, lw=1.8))
    ax.text(3, 5.4, "+ + + +", ha="center", fontsize=12, color=C_RED); ax.text(3, 1.9, "− − − −", ha="center", fontsize=12, color=C_BLUE)
    ax.text(3, 6.6, "ΔT（如人体红外辐射）", ha="center", fontsize=10, color=C_RED)
    ax.text(0.6, 3.8, "P$_s$", fontsize=12, color=C_PURPLE)
    ax.text(3, -0.4, "极性晶体有自发极化 Ps\n温度变 → Ps 变 → 表面电荷变化", ha="center", fontsize=9.5, va="top")
    ax = axs[2]; ax.axis("off"); ax.set_xlim(0, 7); ax.set_ylim(0, 8); ax.set_title("(a3) 热电（Seebeck / Peltier）效应", fontsize=11.5)
    ax.add_patch(Rectangle((0.8, 6.0), 5.4, 0.6, fc=C_RED, alpha=0.7)); ax.text(3.5, 6.85, "热端 T_h", ha="center", fontsize=10, color=C_RED)
    ax.add_patch(Rectangle((0.8, 1.6), 2.0, 0.5, fc="#90caf9")); ax.add_patch(Rectangle((4.2, 1.6), 2.0, 0.5, fc="#90caf9"))
    ax.text(3.5, 1.15, "冷端 T_c", ha="center", fontsize=10, color=C_BLUE)
    ax.add_patch(Rectangle((1.2, 2.1), 1.2, 3.9, fc="#bbdefb", ec="k")); ax.text(1.8, 4.0, "n", ha="center", fontsize=14)
    ax.add_patch(Rectangle((4.6, 2.1), 1.2, 3.9, fc="#ffcdd2", ec="k")); ax.text(5.2, 4.0, "p", ha="center", fontsize=14)
    ax.annotate("", xy=(1.8, 2.5), xytext=(1.8, 5.6), arrowprops=dict(arrowstyle="-|>", color=C_BLUE))
    ax.annotate("", xy=(5.2, 2.5), xytext=(5.2, 5.6), arrowprops=dict(arrowstyle="-|>", color=C_RED))
    ax.text(2.5, 3.4, "e⁻", color=C_BLUE); ax.text(4.0, 3.4, "h⁺", color=C_RED)
    ax.plot([1.8, 1.8, 2.8], [1.6, 0.6, 0.6], color="k"); ax.plot([5.2, 5.2, 4.2], [1.6, 0.6, 0.6], color="k")
    ax.add_patch(Circle((3.5, 0.6), 0.35, fc="white", ec="k")); ax.text(3.5, 0.6, "V", ha="center", va="center")
    ax.text(3.5, -0.4, "温差 → 载流子从热端扩散到冷端 → 电压\nΔV = −S·ΔT（逆：通电 → 一端吸热 Peltier 制冷）", ha="center", fontsize=9.5, va="top")
    ax = axs[3]; ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.set_title("对称性层级", fontsize=11.5)
    for r, (lab, c) in enumerate([("21 个非中心对称点群\n（其中 20 个压电）", "#e1bee7"), ("10 个极性点群\n（热释电）", "#ffe0b2"), ("铁电体\n（Ps 可被电场翻转）", "#c8e6c9")]):
        ax.add_patch(Ellipse((3, 3.6 - r * 0.85), 5.6 - r * 1.5, 6.0 - r * 1.7, fc=c, ec="k"))
        ax.text(3, [5.75, 4.05, 1.9][r], lab, ha="center", va="center", fontsize=9.3)
    ax.text(3, -0.4, "铁电 ⊂ 热释电 ⊂ 压电：\nBaTiO₃、PZT 三者都是；\n石英只压电，不热释电", ha="center", fontsize=9.5, va="top")
    plt.subplots_adjust(bottom=0.2)
    save(fig, "B5_04a_piezo_pyro_thermoelectric.png")


def b5_4d():
    fig, ax = plt.subplots(figsize=(15, 5.6)); ax.axis("off"); ax.set_xlim(0, 30); ax.set_ylim(0, 10)
    ax.set_title("(d) 绿光激光笔（DPSS：二极管泵浦固体激光 + 倍频）", fontsize=12)
    ax.add_patch(FancyBboxPatch((0.3, 3.4), 28.5, 3.0, boxstyle="round,pad=0,rounding_size=1.0", fc="#f5f5f5", ec="#999"))
    ax.add_patch(Rectangle((0.8, 3.9), 3.2, 2.0, fc="#ffe082", ec="k")); ax.text(2.4, 4.9, "电池", ha="center")
    comps = [(5.0, 2.3, "#ef9a9a", "① 激光二极管\nGaAlAs\n→ 808 nm（红外）"),
             (9.5, 1.0, "#e0e0e0", "聚焦\n透镜"),
             (12.0, 2.2, "#ce93d8", "② Nd:YVO₄\n（或 Nd:YAG）\n808 nm 泵浦\n→ 1064 nm 激光"),
             (16.4, 2.2, "#a5d6a7", "③ KTP 晶体\nKTiOPO₄\n倍频（SHG）\n1064 → 532 nm"),
             (20.6, 1.1, "#80cbc4", "④ 红外\n滤光片"),
             (23.0, 1.0, "#e0e0e0", "准直\n透镜")]
    for x, w, c, lab in comps:
        ax.add_patch(Rectangle((x, 3.8), w, 2.2, fc=c, ec="k"))
        ax.text(x + w / 2, 3.4, lab, ha="center", va="top", fontsize=9.5)
    beams = [(7.3, 9.5, "#b71c1c", "808"), (10.5, 12.0, "#b71c1c", "808"), (14.2, 16.4, "#6a1b9a", "1064"),
             (18.6, 20.6, C_GREEN, "532+1064"), (21.7, 23.0, C_GREEN, "532"), (24.0, 29.6, "#00c853", "532 nm 绿光")]
    for a, b, c, t in beams:
        ax.plot([a, b], [4.9, 4.9], color=c, lw=3)
        ax.text((a + b) / 2, 5.2, t, ha="center", fontsize=8.5, color=c)
    ax.text(15, 9.0, "Nd³⁺：⁴F₃/₂ → ⁴I₁₁/₂ 跃迁发 1064 nm；KTP 非中心对称 → 二阶非线性：2 个 1064 nm 光子 → 1 个 532 nm 光子（ω → 2ω）",
            ha="center", fontsize=10)
    ax.text(15, 8.2, "光学部分至少 3 种功能材料：GaAlAs 二极管、Nd:YVO₄ 增益晶体、KTP 倍频晶体（另有 IR 滤光片和透镜）",
            ha="center", fontsize=10.5, fontweight="bold")
    save(fig, "B5_04d_green_laser_pointer.png")


def b5_5():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.4))
    n = np.logspace(17, 23, 300)       # cm^-3
    e = 1.602e-19
    S = 86.17e-6 * np.log(1 + 3e20 / n)  # V/K
    mu = 100e-4                           # m^2/Vs
    sig = n * 1e6 * e * mu
    T = 300; L = 2.44e-8; kL = 1.0
    kap = kL + L * sig * T
    PF = S ** 2 * sig
    ZT = PF * T / kap
    ax = axs[0]
    ax.loglog(n, S * 1e6, color=C_RED, lw=2.5, label="S（µV/K）")
    ax.loglog(n, sig / 100, color=C_BLUE, lw=2.5, label="σ（S/cm）")
    ax.loglog(n, kap, color=C_ORANGE, lw=2.5, label="κ = κ_L + κ_e（W/m·K）")
    ax.axvspan(1e17, 1e18, color="#eeeeee"); ax.axvspan(1e19, 1e21, color=C_GREEN, alpha=0.1); ax.axvspan(1e22, 1e23, color=C_BLUE, alpha=0.08)
    ax.text(3e17, 2e6, "绝缘体/\n轻掺杂", ha="center", fontsize=9.5)
    ax.text(1e20, 2e6, "重掺杂半导体", ha="center", fontsize=9.5, color=C_GREEN)
    ax.text(3e22, 2e6, "金属", ha="center", fontsize=9.5, color=C_BLUE)
    ax.set_xlabel("载流子浓度 n / cm⁻³"); ax.set_ylim(0.1, 1e7)
    ax.set_title("(a) S 与 σ 此消彼长；κ_e 随 σ 增大（Wiedemann–Franz）", fontsize=11)
    ax.legend(fontsize=9.5, loc="lower left"); clean(ax)
    ax = axs[1]
    ax.semilogx(n, ZT / ZT.max(), color=C_PURPLE, lw=2.5, label="ZT（归一化）")
    ax.semilogx(n, PF / PF.max(), color=C_GREEN, lw=2, ls="--", label="功率因子 S²σ（归一化）")
    ax.axvspan(1e19, 1e21, color=C_GREEN, alpha=0.1)
    ax.set_xlabel("载流子浓度 n / cm⁻³"); ax.set_ylabel("相对值")
    ax.set_title("(b) ZT = S²σT/κ 在 10¹⁹–10²⁰ cm⁻³ 附近最大", fontsize=11)
    ax.text(1.5e21, 0.6, "金属：S 极小\n→ S² 更小 → ZT ≈ 0", fontsize=10)
    ax.text(1.5e17, 0.6, "绝缘体：σ 太小\n→ ZT ≈ 0", fontsize=10)
    ax.legend(fontsize=9.5, loc="upper right"); clean(ax)
    save(fig, "B5_05_thermoelectric_ZT.png")


def b5_6():
    fig = plt.figure(figsize=(15, 6.0))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 0.8, 0.9])
    ax = fig.add_subplot(gs[0]); setup_ax(ax, "(a) 俯视：Li 占每第三个六元环中心（√3×√3 R30°）", fs=11)
    a1 = np.array([2.46, 0.0]); a2 = np.array([1.23, 2.1304])
    Cs = []
    for i in range(-3, 6):
        for j in range(-3, 6):
            o = i * a1 + j * a2
            for b in ((a1 + a2) / 3, 2 * (a1 + a2) / 3):
                Cs.append(o + b)
    Cs = [c for c in Cs if -1 < c[0] < 11 and -1 < c[1] < 9.5]
    for i, p in enumerate(Cs):
        for q in Cs[i + 1:]:
            if np.linalg.norm(p - q) < 1.5:
                ax.plot([p[0], q[0]], [p[1], q[1]], color="#555", lw=1.2, zorder=1)
    for p in Cs:
        ax.add_patch(Circle(p, 0.16, fc=C_DARK, zorder=2))
    for i in range(-3, 6):
        for j in range(-3, 6):
            o = i * a1 + j * a2
            if (i - j) % 3 == 0 and -0.5 < o[0] < 10.5 and -0.5 < o[1] < 9:
                ax.add_patch(Circle(o, 0.45, fc=C_PURPLE, ec="k", zorder=3, alpha=0.9))
                ax.text(o[0], o[1], "Li", ha="center", va="center", color="white", fontsize=8, zorder=4)
    O = 1 * a1 + 1 * a2
    A1 = a1 + a2; A2 = -a1 + 2 * a2
    cell = [O, O + A1, O + A1 + A2, O + A2]
    ax.add_patch(Polygon(cell, fc=C_ORANGE, alpha=0.18, ec=C_RED, lw=2.2, zorder=5))
    ax.text(*(O + A1 / 2 + np.array([0.5, -0.9])), "a = √3 × 2.46 = 4.26 Å", color=C_RED, fontsize=9.5, zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.85))
    ax.set_xlim(-0.8, 10.8); ax.set_ylim(-0.8, 9.6)
    foot(ax, "红框 = LiC₆ 的二维晶胞（菱形，60°/120°）：4 个顶点 Li = 2×1/6 + 2×1/3 = 1 个 Li\n面积 = 3 个石墨烯原胞 × 2 C = 6 个 C → LiC₆", fontsize=9.8)
    ax = fig.add_subplot(gs[1]); ax.axis("off"); ax.set_xlim(-2.0, 6); ax.set_ylim(-0.5, 9)
    ax.set_title("(b) 侧视：AA 堆叠，Li 夹在层间", fontsize=11)
    for L in range(3):
        y = 1.0 + L * 3.0
        ax.plot([0.3, 5.7], [y, y], color=C_DARK, lw=2)
        for x in np.arange(0.4, 5.8, 0.71):
            ax.add_patch(Circle((x, y), 0.12, fc=C_DARK))
        if L < 2:
            for x in (0.75, 2.88, 5.01):
                ax.add_patch(Circle((x, y + 1.5), 0.33, fc=C_PURPLE, ec="k"))
    ax.annotate("", xy=(0.0, 4.0), xytext=(0.0, 1.0), arrowprops=dict(arrowstyle="<->", color=C_RED))
    ax.text(-0.15, 2.5, "3.70 Å\n（石墨\n3.35 Å）", fontsize=9, color=C_RED, ha="right", va="center")
    ax.text(3, -0.4, "嵌 Li 后层间距增大约 10 %；\n石墨的 ABAB 变为 AA（Li 上下\n都正对六元环中心）", ha="center", fontsize=9.5, va="top")
    ax = fig.add_subplot(gs[2])
    labs = ["LiC₆\n（石墨/Li）", "NaC₆₄\n（石墨/Na）", "硬碳\n（Na，实测）"]
    vals = [96400 / (6 * 12.01) / 3.6, 96400 / (64 * 12.01) / 3.6, 300]
    cols = [C_PURPLE, C_ORANGE, C_GRAY]
    ax.bar(range(3), vals, color=cols, width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + 8, f"{v:.0f}" if i != 1 else f"{v:.1f}", ha="center", fontsize=11, fontweight="bold" if i == 1 else None)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=10)
    ax.set_ylabel("理论比容量 / mAh·g⁻¹（以碳计）"); ax.set_ylim(0, 430)
    ax.set_title("(c) Na 在石墨中只能到 NaC₆₄", fontsize=11)
    ax.text(1, 150, "Q = F / (64 × 12.01 g/mol)\n= 125 C/g ÷ 3.6\n≈ 34.8 mAh/g", ha="center", fontsize=9.6,
            bbox=dict(fc="white", ec=C_ORANGE))
    clean(ax)
    save(fig, "B5_06_LiC6_structure_NaC64_capacity.png")


def b5_7():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.2), gridspec_kw=dict(width_ratios=[1, 1, 1.3]))
    tet = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]) / np.sqrt(3)
    for ax, M, cM, title, note in [(axs[0], "P", C_ORANGE, "[PS₄]³⁻ 正四面体", "来自 Li₃PS₄（P⁵⁺）\n每个单元配 3 个 Li⁺"),
                                   (axs[1], "Si", C_GRAY, "[SiS₄]⁴⁻ 正四面体", "来自 Li₄SiS₄（Si⁴⁺）\n每个单元配 4 个 Li⁺")]:
        setup_ax(ax, title, fs=11.5)
        sc = Scene(ax, azim=-35, elev=20)
        sc.ball((0, 0, 0), 0.38, cM, label=M, fs=10)
        for v in tet * 2.05:
            sc.ball(v, 0.55, C_YELLOW, label="S", fs=9, lc="k")
            sc.line((0, 0, 0), v, color="#555", lw=3)
        sc.render()
        foot(ax, note, fontsize=10)
    ax = axs[2]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 9)
    ax.set_title("固溶体：x Li₄SiS₄ + (1 − x) Li₃PS₄", fontsize=11.5)
    ax.plot([0.8, 9.2], [6.8, 6.8], color="k", lw=2)
    ax.text(0.8, 7.2, "Li₃PS₄", ha="center"); ax.text(9.2, 7.2, "Li₄SiS₄", ha="center")
    x = 0.8 + 0.4 * 8.4
    ax.plot(x, 6.8, "o", color=C_RED, ms=11); ax.text(x, 7.25, "x = 0.4", color=C_RED, ha="center")
    lines = ["Li：0.4×4 + 0.6×3 = 1.6 + 1.8 = 3.4 ✓",
             "Si：0.4    P：0.6    S：0.4×4 + 0.6×4 = 4 ✓",
             "电荷：阴离子平均 −(0.4×4 + 0.6×3) = −3.4",
             "          由 3.4 个 Li⁺ 平衡 ✓",
             "",
             "本质：用 Si⁴⁺ 异价取代部分 P⁵⁺",
             "→ 每取代 1 个 P，需多 1 个 Li⁺ 补偿电荷",
             "→ 额外 Li⁺ 占据间隙位、Li 亚晶格无序",
             "→ 载流子更多、迁移通道更通畅 → 离子电导率↑",
             "（thio-LISICON 系；同理 Li₁₀GeP₂S₁₂）"]
    for k, t in enumerate(lines):
        ax.text(0.3, 5.9 - k * 0.6, t, fontsize=9.8, fontweight="bold" if k in (5,) else None)
    save(fig, "B5_07_thio_LISICON_building_units.png")


def b5_8():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.8), gridspec_kw=dict(width_ratios=[1.2, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(a) 液态电解质电池的问题", fontsize=11.5)
    ax.add_patch(Rectangle((0.5, 1.2), 1.6, 5.0, fc="#616161", ec="k")); ax.text(1.3, 3.7, "负极\nLi / 石墨", ha="center", color="white", fontsize=9.5)
    ax.add_patch(Rectangle((7.9, 1.2), 1.6, 5.0, fc="#455a64", ec="k")); ax.text(8.7, 3.7, "正极\nLiCoO₂\nNMC", ha="center", color="white", fontsize=9.5)
    ax.add_patch(Rectangle((2.1, 1.2), 5.8, 5.0, fc="#e3f2fd", ec="k"))
    ax.plot([5.0, 5.0], [1.2, 6.2], color=C_GRAY, lw=3, ls=(0, (3, 2))); ax.text(5.1, 0.85, "隔膜", fontsize=9)
    ax.text(3.6, 5.6, "LiPF₆ / EC + DMC", ha="center", fontsize=9.5)
    xs = [2.1, 2.6, 2.4, 3.0, 2.8, 3.5, 3.3, 4.0, 3.8, 4.6]
    ys = [3.4, 3.6, 3.2, 3.5, 3.0, 3.3, 3.8, 3.4, 3.1, 3.3]
    ax.plot(xs[:2] + [2.9, 3.4, 4.1, 4.8], [3.4, 3.6, 3.35, 3.55, 3.3, 3.4], color="#9e9e9e", lw=3)
    ax.text(3.1, 2.4, "① 枝晶穿透\n隔膜 → 短路", fontsize=9.5, color=C_RED, ha="center")
    ax.text(6.4, 4.6, "② 有机溶剂易燃\n热失控起火", fontsize=9.5, color=C_RED, ha="center")
    ax.text(6.4, 2.6, "③ 高压下氧化分解\n（窗口 ≈ 4.3–4.5 V）", fontsize=9.5, color=C_RED, ha="center")
    ax.text(5, 7.3, "④ 挥发、漏液；LiPF₆ 遇水 → HF；t₊ 仅 0.2–0.4", ha="center", fontsize=9.8, color=C_RED)
    ax = axs[1]
    ax.set_title("(b) 电化学稳定窗口 vs 电极电位", fontsize=11.5)
    ax.axhspan(1.0, 4.4, xmin=0.05, xmax=0.35, color=C_BLUE, alpha=0.25)
    ax.text(0.2, 2.7, "碳酸酯\n电解液\n稳定区", ha="center", fontsize=10, transform=ax.get_yaxis_transform())
    items = [("Li 金属", 0.0), ("石墨（LiC₆）≈", 0.1), ("LiFePO₄", 3.45), ("LiCoO₂ / NMC", 4.0), ("LiNi₀.₅Mn₁.₅O₄", 4.7)]
    for lab, E in items:
        ax.plot([0.45, 0.6], [E, E], color=C_RED, lw=3, transform=ax.get_yaxis_transform())
        ax.text(0.63, E + (0.22 if E == 0.1 else (-0.1 if E == 0.0 else 0)), f"{lab}  {E} V", va="center", fontsize=9.8, transform=ax.get_yaxis_transform())
    ax.set_ylim(-0.3, 5.3); ax.set_xticks([]); ax.set_ylabel("电位 / V vs Li⁺/Li")
    ax.text(0.2, 0.35, "负极电位低于下限\n→ 靠 SEI 膜动力学保护", ha="center", fontsize=8.8, transform=ax.get_yaxis_transform())
    clean(ax)
    save(fig, "B5_08_liquid_electrolyte_problems.png")


def b5_9():
    fig = plt.figure(figsize=(15, 6))
    ax = fig.add_subplot(1, 2, 1, projection="polar")
    cats = ["室温离子电导率", "安全性\n（不燃）", "电化学窗口", "Li⁺ 迁移数 t₊", "电极界面接触", "工艺 / 成本", "抑制枝晶 /\n可用 Li 金属"]
    liq = [5, 1, 2.5, 1.5, 5, 5, 1]
    sol = [3, 5, 4, 5, 1.5, 1.5, 3.5]
    ang = np.linspace(0, 2 * np.pi, len(cats), endpoint=False).tolist()
    for v, c, lab in [(liq, C_BLUE, "液态电解质"), (sol, C_RED, "固态电解质")]:
        vv = v + v[:1]; aa = ang + ang[:1]
        ax.plot(aa, vv, color=c, lw=2, label=lab); ax.fill(aa, vv, color=c, alpha=0.15)
    ax.set_xticks(ang); ax.set_xticklabels(cats, fontsize=9.5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels([])
    ax.set_ylim(0, 5.2); ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.12), fontsize=9.5)
    ax.set_title("(a) 定性对比（越外越好）", fontsize=11.5, pad=22)
    ax = fig.add_subplot(1, 2, 2)
    mats = [("液态 LiPF₆/EC-DMC", 10, C_BLUE), ("Li₁₀GeP₂S₁₂（LGPS，硫化物）", 12, C_ORANGE), ("Li₆PS₅Cl（硫银锗矿型）", 2, C_ORANGE),
            ("Li₇La₃Zr₂O₁₂（LLZO，石榴石氧化物）", 0.5, C_GRAY), ("Li₁.₃Al₀.₃Ti₁.₇(PO₄)₃（NASICON）", 0.7, C_GRAY),
            ("PEO–LiTFSI（聚合物，25 °C）", 0.005, C_GREEN), ("LiPON（薄膜）", 0.002, C_PURPLE)]
    for k, (n, v, c) in enumerate(mats):
        ax.barh(len(mats) - k, v, color=c, height=0.6)
        ax.text(v * 1.3, len(mats) - k, f"{v} mS/cm", va="center", fontsize=9.5)
    ax.set_xscale("log"); ax.set_xlim(1e-3, 200)
    ax.set_yticks(range(len(mats), 0, -1)); ax.set_yticklabels([m[0] for m in mats], fontsize=9.5)
    ax.set_xlabel("室温离子电导率 / mS·cm⁻¹（数量级）")
    ax.set_title("(b) 固态电解质的电导率跨 4 个数量级", fontsize=11.5); clean(ax)
    plt.tight_layout()
    save(fig, "B5_09_solid_vs_liquid_electrolytes.png")


if __name__ == "__main__":
    for f in [b5_1, b5_2, b5_3, b5_4a, b5_4d, b5_5, b5_6, b5_7, b5_8, b5_9]:
        f()
