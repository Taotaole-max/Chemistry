# Part A3 配图：制氢、氢化物、锂/钠/NaOH/铝/硅/钢/钛的工业流程
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyBboxPatch
from common import *


def a3_1():
    fig, axs = plt.subplots(1, 2, figsize=(15, 6.0), gridspec_kw=dict(width_ratios=[1.35, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 13.5); ax.set_ylim(0, 8)
    ax.set_title("(a) 甲烷水蒸气重整（SMR）+ 水煤气变换（WGS）", fontsize=12)
    fbox(ax, 1.3, 6.3, 2.5, 1.0, "CH₄ + H₂O(g)\n天然气 + 水蒸气", fc="#fff3e0", ec=C_ORANGE, fs=9.5)
    fbox(ax, 5.1, 6.3, 4.1, 1.6, "重整炉（Ni 催化）\n700–900 °C，20–30 bar\nCH₄ + H₂O → CO + 3H₂\nΔH = +206 kJ/mol（强吸热）", fs=9.5)
    fbox(ax, 10.6, 6.3, 4.6, 1.6, "变换反应器（Fe–Cr 或 Cu–Zn 催化）\n200–450 °C\nCO + H₂O → CO₂ + H₂\nΔH = −41 kJ/mol（放热）", fs=9.5)
    fbox(ax, 10.6, 3.7, 3.4, 1.1, "变压吸附（PSA）\n分离 CO₂ 等杂质", fs=9.5)
    fbox(ax, 8.9, 1.3, 2.6, 0.9, "H₂（≥ 99.9 %）", fc="#e8f5e9", ec=C_GREEN, fs=11)
    fbox(ax, 12.3, 1.3, 2.0, 0.9, "CO₂ 排放", fc="#fdecea", ec=C_RED, fs=10)
    farrow(ax, (2.55, 6.3), (3.05, 6.3)); farrow(ax, (7.15, 6.3), (8.3, 6.3))
    farrow(ax, (10.6, 5.5), (10.6, 4.25)); farrow(ax, (10.0, 3.15), (9.1, 1.75)); farrow(ax, (11.2, 3.15), (12.1, 1.75))
    ax.text(0.1, 4.4, "总反应：CH₄ + 2H₂O → CO₂ + 4H₂", fontsize=10.5, color=C_DARK)
    ax.text(0.1, 3.3, "✓ 成本最低、技术成熟、规模大\n   （全球大部分 H₂ 由此而来）", fontsize=10, color=C_GREEN, va="center")
    ax.text(0.1, 1.7, "✗ 依赖化石原料，CO₂ 排放大\n   （≈ 9–10 kg CO₂ / kg H₂）\n   强吸热、需高温；需提纯",
            fontsize=10, color=C_RED, va="center")
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-1.2, 8)
    ax.set_title("(b) 电解水（碱性电解槽示意）", fontsize=12)
    ax.add_patch(Rectangle((1, 1.6), 8, 4.2, fc="#e3f2fd", ec="k", lw=1.5))
    ax.add_patch(Rectangle((2.0, 2.0), 0.35, 3.3, fc="#555", ec="k"))
    ax.add_patch(Rectangle((7.65, 2.0), 0.35, 3.3, fc="#555", ec="k"))
    ax.plot([5, 5], [1.6, 5.8], color=C_PURPLE, lw=3, ls=(0, (4, 2)))
    ax.text(5, 1.2, "隔膜（PEM 电解则为质子交换膜）", ha="center", fontsize=9.5, color=C_PURPLE)
    ax.plot([2.17, 2.17, 7.83, 7.83], [5.3, 7.2, 7.2, 5.3], color="k", lw=1.2)
    fbox(ax, 5, 7.2, 3.6, 0.7, "直流电源（可再生电力）", fc="white", ec="k", fs=9.5)
    ax.text(1.95, 6.1, "阴极 (−)", ha="right", fontsize=10); ax.text(8.05, 6.1, "阳极 (+)", ha="left", fontsize=10)
    for k in range(5):
        ax.add_patch(Circle((2.7 + 0.25 * (k % 2), 2.4 + 0.65 * k), 0.12, fc="white", ec=C_BLUE))
        ax.add_patch(Circle((7.3 - 0.25 * (k % 2), 2.6 + 0.7 * k), 0.16, fc="white", ec=C_RED))
    ax.text(3.7, 4.4, "H₂↑", fontsize=14, color=C_BLUE); ax.text(5.6, 4.4, "O₂↑", fontsize=14, color=C_RED)
    ax.text(3.1, 2.6, "OH⁻ ⟶", fontsize=10, color=C_DARK)
    ax.text(0.2, 0.5, "阴极：4H₂O + 4e⁻ → 2H₂ + 4OH⁻      阳极：4OH⁻ → O₂ + 2H₂O + 4e⁻", fontsize=9.6)
    ax.text(0.2, -0.2, "总：2H₂O → 2H₂ + O₂（E° = 1.23 V，实际需 1.8–2.0 V）", fontsize=9.8, fontweight="bold")
    ax.text(0.2, -0.95, "✓ 高纯 H₂；用绿电时零 CO₂     ✗ 耗电大（≈ 50 kWh/kg H₂），成本高", fontsize=9.8)
    save(fig, "A3_01_hydrogen_production.png")


def a3_2():
    layout = {
        "H": (1, 1), "He": (18, 1),
        "Li": (1, 2), "Be": (2, 2), "B": (13, 2), "C": (14, 2), "N": (15, 2), "O": (16, 2), "F": (17, 2), "Ne": (18, 2),
        "Na": (1, 3), "Mg": (2, 3), "Al": (13, 3), "Si": (14, 3), "P": (15, 3), "S": (16, 3), "Cl": (17, 3), "Ar": (18, 3),
    }
    p4 = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"]
    p5 = ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"]
    p6 = ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"]
    for per, row in [(4, p4), (5, p5), (6, p6)]:
        for g, el in enumerate(row):
            layout[el] = (g + 1, per)
    ionic = {"Li", "Na", "K", "Rb", "Cs", "Ca", "Sr", "Ba"}
    border = {"Be", "Mg", "Al"}
    metallic = {"Sc", "Y", "La", "Ti", "Zr", "Hf", "V", "Nb", "Ta", "Cr", "Ni", "Pd"}
    gap = {"Mn", "Fe", "Co", "Mo", "Tc", "Ru", "Rh", "W", "Re", "Os", "Ir", "Pt", "Cu", "Ag", "Au"}
    noble = {"He", "Ne", "Ar", "Kr", "Xe", "Rn"}
    col = {}
    for el in layout:
        if el in ionic: col[el] = "#7fb2e5"
        elif el in border: col[el] = "#c7b4e8"
        elif el in metallic: col[el] = "#f2b36b"
        elif el in gap: col[el] = "#d9d9d9"
        elif el in noble: col[el] = "white"
        elif el == "H": col[el] = "white"
        else: col[el] = "#9ed39f"
    fig, ax = plt.subplots(figsize=(13, 5.6))
    ax.axis("off")
    for el, (g, p) in layout.items():
        ax.add_patch(Rectangle((g, -p), 0.95, 0.95, fc=col[el], ec="#555", lw=0.8))
        ax.text(g + 0.475, -p + 0.47, el, ha="center", va="center", fontsize=11,
                fontweight="bold" if el in {"Li", "Na", "Pd", "Ti", "C", "Si", "B"} else None)
    legend = [("#7fb2e5", "离子型（盐型）：LiH、NaH、CaH₂ —— 含 H⁻"), ("#c7b4e8", "过渡/聚合型：(BeH₂)ₙ、MgH₂、(AlH₃)ₙ"),
              ("#f2b36b", "金属型（间隙型）：PdHₓ(x≈0.6)、TiH₂、LaH₂ —— 非整比"),
              ("#9ed39f", "共价型（分子型）：B₂H₆、CH₄、SiH₄、NH₃、H₂O、HF"), ("#d9d9d9", "“氢化物空缺区”：无稳定二元氢化物")]
    for k, (c, t) in enumerate(legend):
        ax.add_patch(Rectangle((3.2, -1.05 - 0.5 * k), 0.4, 0.35, fc=c, ec="#555"))
        ax.text(3.75, -0.88 - 0.5 * k, t, va="center", fontsize=10)
    ax.set_xlim(0.8, 19.2); ax.set_ylim(-6.3, -0.4)
    ax.set_title("氢化物的三大类按周期表分布（电负性：左→右增大）", fontsize=12)
    save(fig, "A3_02_hydride_types_periodic_table.png")


def a3_3():
    fig, ax = plt.subplots(figsize=(12, 4.6))
    ax.axis("off"); ax.set_xlim(1.4, 4.2); ax.set_ylim(-2.3, 2.0)
    ax.annotate("", xy=(4.15, 0), xytext=(1.45, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(4.15, -0.25, "Pauling 电负性 χ", ha="right", fontsize=10)
    els = [("Al", 1.61), ("Si", 1.90), ("Ge", 2.01), ("B", 2.04), ("P", 2.19), ("C", 2.55), ("S", 2.58), ("N", 3.04),
           ("Cl", 3.16), ("O", 3.44), ("F", 3.98)]
    for k, (e, x) in enumerate(els):
        c = C_BLUE if x < 2.2 else (C_GRAY if x < 2.6 else C_RED)
        y = 0.3 + 0.38 * (k % 3)
        ax.plot([x, x], [0, y - 0.1], color=c, lw=1)
        ax.text(x, y, f"{e}\n{x}", ha="center", fontsize=9.5, color=c)
    ax.plot([2.2, 2.2], [-0.3, 1.5], color="k", ls="--")
    ax.text(2.20, 1.6, "H  χ = 2.20", ha="center", fontsize=11, fontweight="bold")
    ax.text(1.75, 1.35, "E 比 H 电负性小\nE(δ+)–H(δ−)：“氢负性”（hydridic）", ha="center", fontsize=10, color=C_BLUE)
    ax.text(3.45, 1.35, "E 比 H 电负性大\nE(δ−)–H(δ+)：“质子性”（protic）", ha="center", fontsize=10, color=C_RED)
    ax.text(1.55, -0.75, "典型反应：H⁻ 转移 / 还原 / 与质子性试剂放 H₂\n"
                         "SiH₄ + 2H₂O → SiO₂ + 4H₂（碱催化）\n"
                         "SiH₄ + 2O₂ → SiO₂ + 2H₂O（空气中自燃）\n"
                         "B₂H₆ + 6H₂O → 2B(OH)₃ + 6H₂；B₂H₆ 还是 Lewis 酸（缺电子）",
            fontsize=9.8, va="top", color=C_BLUE)
    ax.text(2.95, -0.75, "典型反应：给出 H⁺（Brønsted 酸）\n"
                         "HCl + H₂O → H₃O⁺ + Cl⁻\n"
                         "NH₃ / H₂O / HF：氢键、孤对作 Lewis 碱\n"
                         "CH₄（χ 差极小）：几乎不极化，化学惰性",
            fontsize=9.8, va="top", color=C_RED)
    save(fig, "A3_03_covalent_hydride_reactivity.png")


def a3_4():
    fig, ax = plt.subplots(figsize=(14, 7.4)); ax.axis("off"); ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    fbox(ax, 3.3, 9.3, 5.6, 0.8, "① 盐湖卤水（南美“锂三角”：Atacama 等）\nLi⁺ ≈ 0.1–0.2 %，伴有 Na⁺、K⁺、Mg²⁺、硼", fc="#e3f2fd", fs=9.8)
    fbox(ax, 3.3, 7.7, 5.6, 0.9, "日晒蒸发池（12–24 个月）\nNaCl、KCl 先析出 → 浓缩到 ≈6 % Li", fs=9.8)
    fbox(ax, 3.3, 6.2, 5.6, 0.8, "除 Mg²⁺（石灰沉淀 Mg(OH)₂）、除硼（萃取）", fs=9.8)
    fbox(ax, 10.7, 9.3, 5.6, 0.8, "② 锂辉石矿 LiAlSi₂O₆（澳大利亚，硬岩开采）\n浮选精矿 ≈6 % Li₂O", fc="#fff3e0", ec=C_ORANGE, fs=9.8)
    fbox(ax, 10.7, 7.7, 5.6, 0.9, "煅烧 ≈1050 °C：α → β 型（体积 +30 %，结构疏松易反应）", fc="#fff3e0", ec=C_ORANGE, fs=9.8)
    fbox(ax, 10.7, 6.2, 5.6, 0.8, "酸焙烧 250 °C：2LiAlSi₂O₆ + H₂SO₄ → Li₂SO₄ + H₂O·Al₂O₃·4SiO₂\n水浸出 Li₂SO₄", fc="#fff3e0", ec=C_ORANGE, fs=9.3)
    for x in (3.3, 10.7):
        farrow(ax, (x, 8.9), (x, 8.15)); farrow(ax, (x, 7.25), (x, 6.6))
    fbox(ax, 7.0, 4.5, 7.4, 0.9, "沉淀：2Li⁺ + Na₂CO₃ → Li₂CO₃↓ + 2Na⁺（80–90 °C；Li₂CO₃ 溶解度随温度升高而降低）", fc="#e8f5e9",
         ec=C_GREEN, fs=9.8)
    farrow(ax, (3.3, 5.8), (5.0, 4.95)); farrow(ax, (10.7, 5.8), (9.0, 4.95))
    fbox(ax, 7.0, 3.1, 7.4, 0.8, "Li₂CO₃ + 2HCl → 2LiCl + H₂O + CO₂", fs=10)
    farrow(ax, (7.0, 4.05), (7.0, 3.5))
    fbox(ax, 7.0, 1.6, 7.4, 1.0, "熔盐电解 LiCl–KCl 共晶（≈420 °C，KCl 降低熔点）\n阴极(钢)：Li⁺ + e⁻ → Li(l)    阳极(石墨)：2Cl⁻ → Cl₂ + 2e⁻",
         fc="#ede7f6", ec=C_PURPLE, fs=9.8)
    farrow(ax, (7.0, 2.7), (7.0, 2.1))
    ax.text(0.1, 4.2, "✓ 能耗低、成本低\n   （太阳能蒸发）\n✗ 慢（1–2 年）、\n   干旱区耗水、\n   受气候/地域限制、\n   Mg/Li 比高时难提纯",
            fontsize=9.6, va="top", color=C_DARK)
    ax.text(11.0, 3.95, "✓ 快、不受气候限制，\n   矿石品位高、易扩产\n✗ 高温煅烧耗能大、CO₂ 多，\n   大量酸/碱试剂与尾矿，\n   采矿成本高",
            fontsize=9.6, va="top", color=C_DARK)
    save(fig, "A3_04_lithium_production_routes.png")


def a3_5():
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.8), gridspec_kw=dict(width_ratios=[1, 1, 1.05]))
    ax = axs[0]; setup_ax(ax, "Li 金属：bcc，a = 3.51 Å", fs=11)
    a = 3.51
    sc = Scene(ax, azim=-62, elev=18, scale=0.5)
    sc.box((a,0,0),(0,a,0),(0,0,a))
    for p in [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]:
        sc.ball(np.array(p) * a, 0.5, C_PURPLE)
    sc.ball(np.array([0.5,0.5,0.5]) * a, 0.5, C_PURPLE)
    sc.render()
    foot(ax, "2 Li / 43.2 Å³ → 46 Li/nm³\nρ = 0.534 g/cm³\n金属半径 152 pm（2s 电子云很“松”）", fontsize=9.8)
    ax = axs[1]; setup_ax(ax, "LiH：NaCl 型，a = 4.08 Å", fs=11)
    a = 4.08
    sc = Scene(ax, azim=-62, elev=18, scale=0.5)
    sc.box((a,0,0),(0,a,0),(0,0,a))
    corn = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]
    face = [(0.5,0.5,0),(0.5,0.5,1),(0.5,0,0.5),(0.5,1,0.5),(0,0.5,0.5),(1,0.5,0.5)]
    import itertools
    edge = [p for p in itertools.product([0,0.5,1], repeat=3) if sorted(p).count(0.5) == 1]
    for p in corn + face:
        sc.ball(np.array(p) * a, 0.62, "#9ec7ea")
    for p in [(0.5,0.5,0.5)] + edge:
        sc.ball(np.array(p) * a, 0.32, C_PURPLE)
    sc.render()
    foot(ax, "4 LiH / 68.0 Å³ → 59 Li/nm³（比金属 Li 还多！）\nρ = 0.78 g/cm³\nLi⁺ 76 pm（紫，小），H⁻ ≈140 pm（蓝）", fontsize=9.8)
    ax = axs[2]
    names = ["Li", "LiH"]
    ax.bar([0, 1], [0.534, 0.78], color=[C_PURPLE, C_BLUE], width=0.5)
    for x, v in zip([0, 1], [0.534, 0.78]):
        ax.text(x, v + 0.02, f"{v} g/cm³", ha="center", fontsize=11)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Li 金属", "LiH"], fontsize=11)
    ax.set_ylabel("密度 / g·cm⁻³"); ax.set_ylim(0, 1.0)
    ax.set_title("密度：LiH 比 Li 大约 46 %", fontsize=11)
    ax.text(0.5, 0.92, "原因：Li 把 2s 电子交给 H，Li → Li⁺ 体积急剧收缩；\n离子键的库仑吸引又把晶格拉紧", ha="center", fontsize=9.3,
            transform=ax.transData)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "A3_05_LiH_vs_Li_density.png")


def a3_6():
    fig, ax = plt.subplots(figsize=(12, 6.2)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.set_title("Downs 电解槽（熔融 NaCl/CaCl₂，≈600 °C）剖面示意", fontsize=12)
    ax.add_patch(Rectangle((1.5, 0.8), 6, 4.6, fc="#fff3e0", ec="k", lw=2))
    ax.text(4.5, 0.4, "电解质：熔融 NaCl（≈40 %）+ CaCl₂（≈60 %）", ha="center", fontsize=10)
    ax.add_patch(Rectangle((4.1, 0.8), 0.8, 4.2, fc="#444", ec="k"))
    ax.text(4.5, 3.0, "石\n墨\n阳\n极\n(+)", ha="center", va="center", color="white", fontsize=10)
    for x in (2.2, 6.4):
        ax.add_patch(Rectangle((x, 1.6), 0.4, 3.0, fc="#9e9e9e", ec="k"))
    ax.text(2.4, 1.35, "铁阴极(−)", ha="center", fontsize=9); ax.text(6.6, 1.35, "铁阴极(−)", ha="center", fontsize=9)
    for x in (3.4, 5.6):
        ax.plot([x, x], [1.6, 5.0], color=C_PURPLE, lw=2, ls=(0, (2, 2)))
    ax.text(5.7, 1.9, "钢网\n隔膜", fontsize=9, color=C_PURPLE)
    ax.plot([3.4, 3.4, 4.5, 5.6, 5.6], [5.0, 5.9, 6.4, 5.9, 5.0], color="k", lw=1.5)
    ax.text(4.5, 6.7, "Cl₂↑", ha="center", fontsize=14, color=C_GREEN)
    for k in range(4):
        ax.add_patch(Circle((3.9 + 0.2 * (k % 2), 2.0 + 0.8 * k), 0.13, fc="#c8e6c9", ec=C_GREEN))
        ax.add_patch(Circle((5.0 - 0.2 * (k % 2), 2.3 + 0.8 * k), 0.13, fc="#c8e6c9", ec=C_GREEN))
    for x in (2.95, 6.05):
        for k in range(3):
            ax.add_patch(Circle((x, 3.2 + 0.6 * k), 0.12, fc=C_YELLOW, ec="#a07d00"))
    ax.add_patch(Rectangle((2.8, 5.4), 0.32, 1.8, fc=C_YELLOW, ec="k"))
    ax.text(2.6, 6.6, "液态 Na 上浮\n经收集管导出", fontsize=10, color="#a07d00", ha="right")
    ax.text(8.0, 7.0, "阴极：Na⁺ + e⁻ → Na(l)（Na 密度小，浮起）", fontsize=10.5)
    ax.text(8.0, 6.3, "阳极：2Cl⁻ → Cl₂(g) + 2e⁻", fontsize=10.5)
    ax.text(8.0, 5.6, "总：2NaCl(l) → 2Na(l) + Cl₂(g)", fontsize=10.5, fontweight="bold")
    ax.text(8.0, 4.4, "为什么加 CaCl₂？\n  熔点 801 °C → ≈600 °C\n  省能、Na 挥发少（Na 沸点 883 °C）", fontsize=10)
    ax.text(8.0, 2.6, "为什么用熔盐、不用水溶液？\n  E°(Na⁺/Na) = −2.71 V\n  水溶液中 H₂O 先被还原放 H₂", fontsize=10)
    ax.text(8.0, 1.1, "隔膜作用：防止 Na 与 Cl₂ 再化合", fontsize=10)
    save(fig, "A3_06_downs_cell_sodium.png")


def a3_7():
    fig, ax = plt.subplots(figsize=(12, 6.2)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.set_title("氯碱工业：离子交换膜电解槽", fontsize=12)
    ax.add_patch(Rectangle((1.5, 1.0), 4.0, 5.0, fc="#fff8e1", ec="k", lw=2))
    ax.add_patch(Rectangle((5.5, 1.0), 4.0, 5.0, fc="#e3f2fd", ec="k", lw=2))
    ax.plot([5.5, 5.5], [1.0, 6.0], color=C_PURPLE, lw=5)
    ax.text(5.5, 0.6, "阳离子交换膜（Nafion）\n只让 Na⁺ 通过", ha="center", va="top", fontsize=9.5, color=C_PURPLE)
    ax.add_patch(Rectangle((2.0, 1.5), 0.35, 4.0, fc="#607d8b", ec="k"))
    ax.add_patch(Rectangle((8.65, 1.5), 0.35, 4.0, fc="#9e9e9e", ec="k"))
    ax.text(2.17, 6.25, "阳极(+)\nDSA：Ti/RuO₂", ha="center", fontsize=9.5)
    ax.text(8.83, 6.25, "阴极(−)\nNi", ha="center", fontsize=9.5)
    ax.text(3.5, 4.8, "饱和 NaCl\n溶液", ha="center", fontsize=10)
    ax.text(7.5, 4.8, "NaOH\n溶液", ha="center", fontsize=10)
    ax.text(3.1, 3.3, "2Cl⁻ → Cl₂ + 2e⁻", fontsize=10, color=C_GREEN)
    ax.text(6.0, 2.3, "2H₂O + 2e⁻\n→ H₂ + 2OH⁻", fontsize=10, color=C_BLUE)
    farrow(ax, (4.6, 3.8), (6.6, 3.8), "Na⁺", color=C_PURPLE, off=(0, 0.3), fs=12)
    farrow(ax, (3.5, 6.0), (3.5, 7.2), "Cl₂↑", color=C_GREEN, off=(0.5, 0), fs=12)
    farrow(ax, (7.5, 6.0), (7.5, 7.2), "H₂↑", color=C_BLUE, off=(0.5, 0), fs=12)
    farrow(ax, (0.3, 2.0), (1.5, 2.0), "盐水入", off=(0, 0.3), fs=9.5)
    farrow(ax, (1.5, 5.4), (0.3, 5.4), "稀盐水出", off=(0, 0.3), fs=9.5)
    farrow(ax, (10.9, 2.0), (9.5, 2.0), "H₂O 入", off=(0, 0.3), fs=9.5)
    farrow(ax, (9.5, 5.4), (10.9, 5.4), "≈32 % NaOH", off=(0, 0.3), fs=9.5)
    ax.text(0.3, 7.6, "总：2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂", fontsize=11, fontweight="bold")
    ax.text(9.8, 7.6, "膜的作用：\n① 阻止 OH⁻ 到阳极：\n   Cl₂ + 2OH⁻ → Cl⁻ + OCl⁻ + H₂O\n② 隔开 H₂/Cl₂（爆炸）\n③ NaOH 不含 NaCl",
            fontsize=9.3, va="top")
    save(fig, "A3_07_chloralkali_membrane_cell.png")


def a3_8():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.4), gridspec_kw=dict(width_ratios=[1.05, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_title("(a) Bayer 法：铝土矿 → 纯 Al₂O₃", fontsize=12)
    steps = [("铝土矿：Al(OH)₃ / AlO(OH) + Fe₂O₃、SiO₂、TiO₂", "#fff3e0", C_ORANGE),
             ("① 溶出：浓 NaOH，150–250 °C，加压\nAl(OH)₃ + OH⁻ → [Al(OH)₄]⁻（两性，溶解）", "#eef3fb", C_BLUE),
             ("② 过滤：Fe₂O₃、TiO₂ 不溶 → 赤泥（red mud）除去", "#fdecea", C_RED),
             ("③ 降温 + 加晶种分解：\n[Al(OH)₄]⁻ → Al(OH)₃↓ + OH⁻（NaOH 循环）", "#eef3fb", C_BLUE),
             ("④ 煅烧 1100–1200 °C：2Al(OH)₃ → Al₂O₃ + 3H₂O", "#e8f5e9", C_GREEN)]
    ys = [9.2, 7.5, 5.8, 4.1, 2.4]
    for (t, fc, ec), y in zip(steps, ys):
        fbox(ax, 5, y, 9.2, 1.15 if "\n" in t else 0.8, t, fc=fc, ec=ec, fs=9.6)
    for y1, y2 in zip(ys[:-1], ys[1:]):
        farrow(ax, (5, y1 - 0.5), (5, y2 + 0.55))
    ax.text(5, 1.0, "核心原理：Al(OH)₃ 两性、Fe(OH)₃/Fe₂O₃ 碱性 → 用强碱把 Al 与 Fe 分开", ha="center", fontsize=10,
            color=C_DARK, bbox=dict(fc="#fffde7", ec=C_YELLOW))
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-2.3, 9.2)
    ax.set_title("(b) Hall–Héroult 电解：Al₂O₃ 溶于冰晶石", fontsize=12)
    ax.add_patch(Rectangle((1, 1.5), 8, 5, fc="#455a64", ec="k", lw=2))
    ax.add_patch(Rectangle((1.4, 1.9), 7.2, 1.2, fc="#cfd8dc", ec="k"))
    ax.text(5, 2.5, "液态 Al（密度大，沉底）", ha="center", fontsize=10)
    ax.add_patch(Rectangle((1.4, 3.1), 7.2, 3.0, fc="#ffe0b2", ec="k"))
    ax.text(5, 3.5, "熔融冰晶石 Na₃AlF₆ + 2–6 % Al₂O₃，≈960 °C", ha="center", fontsize=9.5)
    for x in (2.2, 4.4, 6.6):
        ax.add_patch(Rectangle((x, 4.2), 1.3, 3.6, fc="#212121", ec="k"))
        ax.text(x + 0.65, 6.9, "C", color="white", ha="center", fontsize=12)
    ax.text(5, 8.3, "碳阳极(+)，逐渐被消耗（产生 CO₂）", ha="center", fontsize=10)
    ax.text(5, 1.15, "碳内衬 = 阴极(−)", ha="center", fontsize=10, color="white")
    ax.text(0.3, 0.5, "阴极：Al³⁺ + 3e⁻ → Al(l)\n阳极：C + 2O²⁻ → CO₂ + 4e⁻\n总：2Al₂O₃ + 3C → 4Al + 3CO₂", fontsize=9.8, va="top",
            bbox=dict(fc="white", ec="#999"))
    ax.text(5.6, 0.5, "冰晶石：把熔点 2050 °C\n降到 ≈960 °C，且能溶解 Al₂O₃\n耗电 ≈13–15 kWh/kg Al", fontsize=9.6, va="top")
    save(fig, "A3_08_aluminium_bayer_hall_heroult.png")


def a3_9():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.6), gridspec_kw=dict(width_ratios=[1.45, 0.75]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 11)
    ax.set_title("从石英砂到高纯多晶硅", fontsize=12)
    items = [(10.2, "石英砂 SiO₂ + 焦炭/木屑", "#fff3e0", C_ORANGE),
             (8.6, "电弧炉（埋弧）≈2000 °C\nSiO₂ + 2C → Si(l) + 2CO\n（副反应 SiO₂ + 3C → SiC + 2CO，SiC + SiO₂ 再生成 Si）", "#eef3fb", C_BLUE),
             (6.9, "冶金级硅 MG-Si：98–99 %（含 Fe、Al、B、P…）", "#fdecea", C_RED),
             (5.4, "氢氯化（流化床，≈300 °C，Cu 催化）\nSi + 3HCl → HSiCl₃ + H₂", "#eef3fb", C_BLUE),
             (3.8, "精馏 HSiCl₃（沸点 31.8 °C）\n与 BCl₃、PCl₃、FeCl₃、AlCl₃ 等按沸点分开", "#eef3fb", C_BLUE),
             (2.2, "Siemens 法 CVD（硅棒通电加热到 ≈1100 °C）\nHSiCl₃ + H₂ → Si + 3HCl", "#eef3fb", C_BLUE),
             (0.7, "高纯多晶硅（9N–11N，“电子级”）→ Czochralski / 区熔 → 单晶", "#e8f5e9", C_GREEN)]
    for y, t, fc, ec in items:
        fbox(ax, 6, y, 11.4, 1.25 if t.count("\n") >= 1 else 0.75, t, fc=fc, ec=ec, fs=9.6)
    for (y1, *_), (y2, *_) in zip(items[:-1], items[1:]):
        farrow(ax, (6, y1 - 0.45), (6, y2 + 0.5))
    ax.text(10.6, 4.6, "（副产 SiCl₄\n可加氢回收）", fontsize=8.8, color=C_GRAY)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 11)
    ax.set_title("Siemens 反应器示意", fontsize=12)
    ax.add_patch(FancyBboxPatch((0.6, 1.5), 4.8, 7.6, boxstyle="round,pad=0,rounding_size=2.2", fc="#f5f5f5", ec="k", lw=2))
    ax.plot([2.0, 2.0, 4.0, 4.0], [1.5, 7.6, 7.6, 1.5], color="#5d4037", lw=9, solid_capstyle="butt")
    ax.plot([2.0, 2.0, 4.0, 4.0], [1.5, 7.6, 7.6, 1.5], color="#bcaaa4", lw=3, solid_capstyle="butt")
    ax.text(3.0, 8.2, "U 形细硅棒\n通电加热 1100 °C", ha="center", fontsize=9.5)
    ax.text(3.0, 4.5, "Si 沉积\n棒越长越粗", ha="center", fontsize=9.5)
    farrow(ax, (1.2, 0.4), (1.2, 1.6), "HSiCl₃ + H₂", fs=9.5, off=(0.0, -0.75))
    farrow(ax, (4.8, 1.6), (4.8, 0.4), "HCl、SiCl₄…", fs=9.5, off=(0.0, -0.75))
    ax.plot([2.0, 4.0], [1.0, 1.0], color="k"); ax.text(3.0, 0.6, "电源", ha="center", fontsize=9)
    save(fig, "A3_09_silicon_production.png")


def a3_10():
    fig, axs = plt.subplots(1, 2, figsize=(14, 7.6), gridspec_kw=dict(width_ratios=[1.4, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(-1.2, 12); ax.set_ylim(0, 12)
    ax.set_title("(a) 高炉：炼铁（生铁，≈4 % C）", fontsize=12)
    shape = [(2.6, 11.0), (4.4, 11.0), (5.4, 6.0), (5.0, 3.6), (5.0, 1.0), (2.0, 1.0), (2.0, 3.6), (1.6, 6.0)]
    ax.add_patch(Polygon(shape, fc="#ffe0b2", ec="k", lw=2))
    ax.add_patch(Rectangle((2.0, 1.0), 3.0, 0.8, fc="#b0bec5", ec="k"))
    ax.add_patch(Rectangle((2.0, 1.8), 3.0, 0.5, fc="#8d6e63", ec="k"))
    ax.text(3.5, 1.35, "铁水", ha="center", fontsize=9); ax.text(3.5, 2.05, "炉渣", ha="center", fontsize=9, color="white")
    ax.text(3.5, 11.4, "矿石 Fe₂O₃ + 焦炭 C + 石灰石 CaCO₃ ↓", ha="center", fontsize=9.5)
    farrow(ax, (0.6, 2.55), (1.9, 2.55), "热风", off=(0, 0.3), fs=9); farrow(ax, (6.1, 2.55), (5.1, 2.55), "热风", off=(0, 0.3), fs=9)
    zones = [(10.0, "≈400 °C", "3Fe₂O₃ + CO → 2Fe₃O₄ + CO₂"),
             (8.6, "≈700 °C", "Fe₃O₄ + CO → 3FeO + CO₂"),
             (7.2, "≈900 °C", "FeO + CO → Fe + CO₂（间接还原）\nCaCO₃ → CaO + CO₂"),
             (5.6, "≈1000–1200 °C", "C + CO₂ ⇌ 2CO（Boudouard）\nFeO + C → Fe + CO（直接还原）"),
             (4.1, "≈1500 °C", "CaO + SiO₂ → CaSiO₃（造渣）\nFe 熔化、吸收 C → 生铁"),
             (3.15, "风口 ≈1900 °C", "C + O₂ → CO₂（放热，供热）")]
    for y, T, r in zones:
        ax.plot([4.9 if y > 6 else 5.3, 6.3], [y, y], color="#999", lw=0.8, ls=":")
        ax.text(3.5, y, T, ha="center", va="center", fontsize=9, color=C_RED)
        ax.text(6.4, y, r, va="center", fontsize=9.3)
    farrow(ax, (1.0, 6.5), (1.0, 10.5), color=C_BLUE); ax.text(0.85, 8.5, "CO 气流\n上升\n（还原剂）", ha="right", va="center", fontsize=9, color=C_BLUE)
    farrow(ax, (2.55, 10.6), (2.55, 8.2), color=C_ORANGE); ax.text(2.75, 10.75, "炉料下降", fontsize=8.5, color=C_ORANGE)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 8); ax.set_ylim(0, 12)
    ax.set_title("(b) 转炉（LD / 碱性氧气）：炼钢", fontsize=12)
    shape = [(2.0, 8.0), (3.0, 9.5), (5.0, 9.5), (6.0, 8.0), (6.0, 3.0), (5.0, 2.0), (3.0, 2.0), (2.0, 3.0)]
    ax.add_patch(Polygon(shape, fc="#cfd8dc", ec="k", lw=2))
    ax.add_patch(Polygon([(2.05, 5.0), (5.95, 5.0), (5.95, 3.0), (5.0, 2.05), (3.0, 2.05), (2.05, 3.0)], fc="#ff8a65", ec="none"))
    ax.add_patch(Rectangle((2.05, 5.0), 3.9, 0.5, fc="#8d6e63"))
    ax.plot([4.0, 4.0], [11.5, 5.7], color="#424242", lw=6)
    ax.text(4.3, 10.8, "O₂ 喷枪", fontsize=10)
    ax.text(4.0, 3.6, "铁水", ha="center", fontsize=10)
    ax.text(0.2, 1.4, "吹 O₂ 把杂质氧化掉：\n① 2C + O₂ → 2CO↑（C 4 % → <2 %）\n② Si + O₂ → SiO₂ → CaSiO₃（渣）\n"
                      "③ 4P + 5O₂ → 2P₂O₅；P₂O₅ + 3CaO → Ca₃(PO₄)₂（渣）\n④ 2Mn + O₂ → 2MnO\n反应放热，不需外加燃料",
            fontsize=9.4, va="top")
    ax.set_ylim(-3, 12)
    save(fig, "A3_10_blast_furnace_converter.png")


def a3_11():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw=dict(width_ratios=[1, 1.1]))
    ax = axs[0]
    T = np.linspace(300, 2300, 200)
    lines = [("2Fe + O₂ → 2FeO", -544, -0.138, C_RED), ("Si + O₂ → SiO₂", -911, -0.185, C_PURPLE),
             ("Ti + O₂ → TiO₂", -944, -0.185, C_TEAL), ("4/3Al + O₂ → 2/3Al₂O₃", -1117, -0.208, C_GRAY),
             ("2C + O₂ → 2CO", -221, 0.179, "black")]
    for lab, H, S, c in lines:
        ax.plot(T, H - T * S, color=c, lw=2.2 if c == "black" else 1.8, label=lab)
    ax.set_xlabel("T / K"); ax.set_ylabel("ΔG° / kJ·(mol O₂)⁻¹")
    ax.set_title("(a) 简化 Ellingham 图（近似值，示意）", fontsize=11.5)
    ax.axvline(1019, color=C_RED, ls=":", lw=1); ax.text(1040, -150, "≈1020 K：C 可还原 FeO", color=C_RED, fontsize=9)
    ax.text(1180, -930, "Si、Ti、Al 的线远在 C 线下方：\n要 ≈1900–2300 K 才可能被 C 还原\n（Ti 还会生成 TiC，故用 Kroll 法）", fontsize=9, va="top")
    ax.legend(fontsize=9, loc="lower left"); ax.set_ylim(-1100, -100)
    ax.text(310, -130, "线越低 = 氧化物越稳定", fontsize=9.5, color=C_DARK)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_title("(b) 除铁原理对比", fontsize=12)
    fbox(ax, 5, 9.0, 9.6, 1.4, "Al（Bayer 法）：酸碱性 / 两性\nAl(OH)₃ + OH⁻ → [Al(OH)₄]⁻ 溶解；Fe₂O₃ 不溶 → 赤泥", fc="#eef3fb", fs=10)
    fbox(ax, 5, 6.7, 9.6, 1.6, "Ti（氯化法）：挥发性差异\n碳氯化 → TiCl₄（分子，沸点 136 °C）与 FeCl₃（升华 315 °C）\n冷凝 / 分馏分开", fc="#e0f2f1", ec=C_TEAL, fs=10)
    fbox(ax, 5, 4.3, 9.6, 1.6, "Ti（硫酸法）：溶解度 + 氧化还原\n加铁屑把 Fe³⁺ 还原成 Fe²⁺（Fe²⁺ 不随 Ti 水解沉淀）\n冷却析出 FeSO₄·7H₂O（绿矾）", fc="#e0f2f1", ec=C_TEAL, fs=10)
    fbox(ax, 5, 1.9, 9.6, 1.6, "Ti（钛渣法）：选择性还原（Ellingham）\nFeTiO₃ + C → Fe(l) + TiO₂（渣）+ CO，≈1650 °C 电炉\nFeO 易被 C 还原，TiO₂ 不易 → 铁成金属分离", fc="#e0f2f1", ec=C_TEAL, fs=10)
    save(fig, "A3_11_iron_removal_Al_vs_Ti.png")


def a3_12():
    fig, ax = plt.subplots(figsize=(14, 7.8)); ax.axis("off"); ax.set_xlim(0, 14); ax.set_ylim(0, 11)
    fbox(ax, 7, 10.3, 5, 0.8, "钛铁矿 FeTiO₃（= FeO·TiO₂）", fc="#fff3e0", ec=C_ORANGE, fs=11)
    ax.text(3.4, 9.3, "硫酸法（Sulfate process）", ha="center", fontsize=12, fontweight="bold", color=C_BLUE)
    ax.text(10.6, 9.3, "氯化法（Chloride process）", ha="center", fontsize=12, fontweight="bold", color=C_TEAL)
    L = [(8.3, "① 浓 H₂SO₄ 溶解（150–200 °C）\nFeTiO₃ + 2H₂SO₄ → TiOSO₄ + FeSO₄ + 2H₂O"),
         (6.8, "② 加铁屑：2Fe³⁺ + Fe → 3Fe²⁺"),
         (5.4, "③ 冷却结晶：FeSO₄·7H₂O↓（绿矾）滤除"),
         (3.9, "④ 加热水解：TiOSO₄ + (n+1)H₂O\n→ TiO₂·nH₂O↓ + H₂SO₄"),
         (2.3, "⑤ 煅烧 800–1000 °C → TiO₂\n（锐钛矿或金红石）")]
    R = [(8.3, "① 碳氯化 900–1000 °C（流化床）\n2FeTiO₃ + 7Cl₂ + 6C → 2TiCl₄ + 2FeCl₃ + 6CO\n（工业上多用金红石/钛渣：TiO₂ + 2Cl₂ + 2C → TiCl₄ + 2CO）"),
         (6.6, "② 分离：FeCl₃ 先冷凝成固体除去\n精馏 TiCl₄（沸点 136 °C，液体）"),
         (5.0, "③ 燃烧氧化 ≈1000–1400 °C\nTiCl₄ + O₂ → TiO₂ + 2Cl₂"),
         (3.5, "④ Cl₂ 回收循环使用 → 金红石型颜料")]
    for x, seq, ec, fc in [(3.4, L, C_BLUE, "#eef3fb"), (10.6, R, C_TEAL, "#e0f2f1")]:
        for y, t in seq:
            fbox(ax, x, y, 6.6, 0.55 + 0.38 * (t.count("\n") + 1), t, fc=fc, ec=ec, fs=9.4)
        for (y1, t1), (y2, t2) in zip(seq[:-1], seq[1:]):
            farrow(ax, (x, y1 - 0.25 - 0.19 * (t1.count("\n") + 1)), (x, y2 + 0.28 + 0.19 * (t2.count("\n") + 1)))
    farrow(ax, (5.6, 10.0), (3.6, 9.55)); farrow(ax, (8.4, 10.0), (10.4, 9.55))
    ax.text(0.2, 0.9, "✓ 可用低品位矿；设备简单\n✗ 每吨 TiO₂ 产生数吨废酸 + 绿矾，环保压力大", fontsize=10)
    ax.text(7.4, 0.9, "✓ 产品纯、Cl₂ 循环、废物少；连续化\n✗ 需高品位原料；Cl₂ 有毒，技术要求高", fontsize=10)
    save(fig, "A3_12_TiO2_from_ilmenite.png")


def a3_13():
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.8), gridspec_kw=dict(width_ratios=[1, 1, 1.1]))
    tet = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]) / np.sqrt(3)
    for ax, M, d, cM, title, note in [(axs[0], "Si", 2.02, C_ORANGE, "SiCl₄", "Si–Cl 2.02 Å，键角 109.5°\n无色液体，沸点 57.6 °C"),
                                      (axs[1], "Ti", 2.17, C_GRAY, "TiCl₄", "Ti–Cl 2.17 Å，键角 109.5°\nTi(IV) d⁰，无色液体，沸点 136 °C")]:
        setup_ax(ax, f"{title}：正四面体（T_d）", fs=11.5)
        sc = Scene(ax, azim=-35, elev=20, scale=1)
        sc.ball((0, 0, 0), 0.45, cM, label=M, fs=10)
        for v in tet * d:
            sc.ball(v, 0.55, C_GREEN, label="Cl", fs=9)
            sc.line((0, 0, 0), v, color="#555", lw=3)
        sc.render()
        foot(ax, note, fontsize=10)
    ax = axs[2]; ax.axis("off"); ax.set_title("为什么都是四面体？有何异同", fontsize=11.5)
    txt = ("VSEPR：中心原子 4 对成键电子、0 孤对（AX₄）\n→ 四对电子互相排斥最小 = 正四面体\n\n"
           "TiCl₄ 是 d⁰：没有 d 电子，没有晶体场\n“选择性”，同样按 AX₄ 处理\n\n"
           "共同点：分子型、易挥发、遇潮气剧烈水解冒白烟\n  SiCl₄ + 2H₂O → SiO₂ + 4HCl\n  TiCl₄ + 2H₂O → TiO₂ + 4HCl\n\n"
           "不同点：TiCl₄ 是更强的 Lewis 酸（空 d 轨道），\n可扩展到 CN 6：TiCl₄·2L（八面体），\n用于 Ziegler–Natta 催化剂")
    ax.text(0, 0.97, txt, fontsize=9.8, va="top", transform=ax.transAxes)
    save(fig, "A3_13_SiCl4_TiCl4_structures.png")


if __name__ == "__main__":
    for f in [a3_1, a3_2, a3_3, a3_4, a3_5, a3_6, a3_7, a3_8, a3_9, a3_10, a3_11, a3_12, a3_13]:
        f()
