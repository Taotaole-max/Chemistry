# Part B3 配图：高温方法、碱金属与石英、化学气相输运（CVT）、Boudouard、TiO2 干凝胶
import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Ellipse
from common import *

R = 8.314


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def b3_1():
    fig, ax = plt.subplots(figsize=(12, 6))
    rows = [("电阻炉：FeCrAl（Kanthal）发热体", 0, 1400, C_BLUE, True),
            ("电阻炉：SiC 发热体", 0, 1600, C_BLUE, True),
            ("电阻炉：MoSi₂ 发热体", 0, 1800, C_BLUE, True),
            ("电阻炉：石墨 / W 发热体（惰性气氛或真空）", 0, 2800, C_BLUE, True),
            ("感应加热（涡流加热导电坩埚，如石墨、W）", 0, 3000, C_GREEN, True),
            ("电弧熔炼（W 电极，水冷铜炉床，Ar）", 2000, 3500, C_RED, True),
            ("铝热反应 / 自蔓延高温合成（SHS）", 2000, 3000, C_ORANGE, False),
            ("氢氧焰（Verneuil 法长宝石）", 1500, 2800, C_ORANGE, False),
            ("激光加热 / 聚光（太阳）炉", 2000, 4000, C_PURPLE, False),
            ("等离子炬 / 电子束熔炼", 3000, 6000, C_PURPLE, False)]
    for k, (lab, a, b, c, main) in enumerate(rows):
        y = len(rows) - k
        ax.barh(y, b - a, left=a, color=c, alpha=0.85 if main else 0.45, height=0.6)
        ax.text(b + 60, y, lab, va="center", fontsize=9.8)
    ax.set_yticks([])
    ax.set_xlabel("可达温度 / °C（量级）")
    ax.set_xlim(0, 8600)
    ax.set_title("获得高温的几种手段（深色 = 实验室最常用的三类）", fontsize=12)
    clean(ax)
    save(fig, "B3_01_high_temperature_methods.png")


def b3_2():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.6), gridspec_kw=dict(width_ratios=[1, 1.05]))
    ax = axs[0]
    labs = ["4Na + SiO₂\n→ 2Na₂O + Si", "4Na + 3SiO₂\n→ 2Na₂SiO₃ + Si", "4Li + SiO₂\n→ 2Li₂O + Si"]
    vals = [2 * (-376.0) + 856.4, 2 * (-1467.4) + 3 * 856.4, 2 * (-561.2) + 856.4]
    cols = [C_GRAY, C_RED, C_RED]
    b = ax.bar(range(3), vals, color=cols, width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + (12 if v > 0 else -30), f"{v:+.0f} kJ", ha="center", fontsize=11)
    ax.axhline(0, color="k", lw=1)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=10)
    ax.set_ylabel("ΔrG°(298 K) / kJ")
    ax.set_title("(a) 碱金属还原 SiO₂（标准生成 Gibbs 能估算）", fontsize=11.5)
    ax.text(0.5, 60, "单看还原：Na 不够强…", fontsize=9.5, color=C_GRAY)
    ax.text(1.35, 110, "…但生成的 Na₂O 立刻和 SiO₂\n结合成硅酸盐，总反应强烈放能", fontsize=9.5, color=C_RED)
    ax.set_ylim(-420, 160); clean(ax)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(b) 正确做法：金属安瓿 + 外套石英管", fontsize=11.5)
    ax.add_patch(FancyBboxPatch((0.5, 4.6), 8.6, 1.6, boxstyle="round,pad=0,rounding_size=0.8", fc="#e3f2fd", ec="#64b5f6", lw=2))
    ax.text(4.8, 6.45, "外层：抽真空熔封的石英管（保护 Ta/Nb 不被空气氧化）", ha="center", fontsize=9.5, color="#1565c0")
    ax.add_patch(Rectangle((1.2, 5.0), 7.2, 0.8, fc="#9e9e9e", ec="k", lw=1.5))
    ax.add_patch(Rectangle((1.0, 4.95), 0.25, 0.9, fc="#616161")); ax.add_patch(Rectangle((8.35, 4.95), 0.25, 0.9, fc="#616161"))
    ax.text(4.8, 5.4, "Ta / Nb 管（两端电弧焊封）内装 碱金属 + 反应物", ha="center", fontsize=9.5)
    txt = ["为什么不能用石英（SiO₂）：",
           "• 碱金属是强还原剂，高温下把 SiO₂ 还原成 Si，",
           "  并生成碱金属硅酸盐 → 石英变色、腐蚀、开裂",
           "• 碱金属蒸气还会渗入、反应，产物被 Si/O 污染",
           "",
           "可用的容器：",
           "• Ta、Nb、Mo、W、Fe（低碳钢）等金属：不与碱金属反应",
           "• 某些氧化物坩埚（MgO、Al₂O₃）可用于 Na/K，但 Li 会侵蚀",
           "• 不用石墨：K/Rb/Cs 会插层（KC₈），Li 生成 Li₂C₂"]
    for k, t in enumerate(txt):
        ax.text(0.3, 3.9 - k * 0.43, t, fontsize=9.8, fontweight="bold" if t.endswith("：") else None)
    save(fig, "B3_02_alkali_metal_vs_silica.png")


def b3_3():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.4), gridspec_kw=dict(width_ratios=[1.1, 1]))
    ax = axs[0]
    T1, T2 = 1000.0, 1100.0
    Tm = (T1 + T2) / 2
    dH = 100e3
    G = np.linspace(-120e3, 120e3, 400)
    dS = (dH - G) / Tm
    K = lambda T: np.exp(-(dH - T * dS) / (R * T))
    dp = K(T2) / (1 + K(T2)) - K(T1) / (1 + K(T1))
    ax.plot(G / 1000, dp, color=C_BLUE, lw=2.5)
    ax.axvspan(-40, 40, color=C_GREEN, alpha=0.12)
    ax.text(0, 0.03, "K ≈ 1 附近\nΔp 最大", ha="center", fontsize=10, color=C_GREEN)
    ax.text(-110, 0.12, "K ≫ 1：两端几乎\n全变成 AB(g)\nΔp ≈ 0，不输运", fontsize=9.5)
    ax.text(55, 0.12, "K ≪ 1：两端几乎\n不生成 AB(g)\nΔp ≈ 0，不输运", fontsize=9.5)
    ax.set_xlabel("ΔrG°(T̄) / kJ·mol⁻¹")
    ax.set_ylabel("Δp(AB) / p₀（源区与沉积区分压差）")
    ax.set_title("(a) 条件 2：平衡要“居中”（ΔrG° ≈ 0）且 ΔrH ≠ 0", fontsize=11.5)
    ax.text(0.98, 0.95, "模型：A(s) + B(g) ⇌ AB(g)\nΔrH = +100 kJ/mol，T₂ = 1100 K，T₁ = 1000 K", transform=ax.transAxes,
            ha="right", va="top", fontsize=9.5, bbox=dict(fc="white", ec="#999"))
    clean(ax)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(b) 两个必要条件", fontsize=11.5)
    fbox(ax, 5, 6.4, 9.6, 1.9, "① 固体能与输运剂发生可逆的多相反应，\n且所有产物都是气体：\n i A(s) + k B(g) ⇌ j C(g) + …\n（输运剂只需少量，循环使用）",
         fc="#eef3fb", fs=10.5)
    fbox(ax, 5, 3.4, 9.6, 2.9, "② 反应平衡既不过分偏左也不过分偏右：\n ΔrG° ≈ 0，K ≈ 1（经验 |lg K| ≲ 4）\n 同时 ΔrH ≠ 0 → K 随温度变化 → 源区与沉积区\n 之间产生分压差，驱动气相扩散\n\n 输运方向（Schäfer）：ΔrH > 0 热 → 冷；ΔrH < 0 冷 → 热",
         fc="#e8f5e9", ec=C_GREEN, fs=10.5)
    save(fig, "B3_03_CVT_conditions.png")


def ampoule(ax, y, left_T, right_T, left_lab, right_lab, src_left, title, eq, steps, colL, colR):
    ax.add_patch(FancyBboxPatch((0.5, y - 0.6), 9, 1.2, boxstyle="round,pad=0,rounding_size=0.6", fc="#f7fbff", ec="#64b5f6", lw=2))
    ax.add_patch(Rectangle((0.5, y - 1.3), 4.5, 0.35, fc=colL, alpha=0.6, ec="none"))
    ax.add_patch(Rectangle((5.0, y - 1.3), 4.5, 0.35, fc=colR, alpha=0.6, ec="none"))
    ax.text(2.75, y - 1.12, left_T, ha="center", va="center", fontsize=9.5)
    ax.text(7.25, y - 1.12, right_T, ha="center", va="center", fontsize=9.5)
    sx = 1.6 if src_left else 8.4
    dx = 8.4 if src_left else 1.6
    for k in range(6):
        ax.add_patch(Circle((sx - 0.5 + 0.2 * k, y - 0.42 + 0.06 * (k % 2)), 0.13, fc="#795548", ec="k", lw=0.5))
    for k in range(3):
        ax.add_patch(Rectangle((dx - 0.6 + 0.4 * k, y - 0.55), 0.22, 0.32, fc="#ffca28", ec="k", lw=0.6, angle=10 * k))
    ax.text(sx, y + 0.25, left_lab if src_left else right_lab, ha="center", fontsize=9.5)
    ax.text(dx, y + 0.25, right_lab if src_left else left_lab, ha="center", fontsize=9.5)
    a, b = (2.6, 7.4) if src_left else (7.4, 2.6)
    ax.annotate("", xy=(b, y + 0.05), xytext=(a, y + 0.05), arrowprops=dict(arrowstyle="-|>", lw=2.2, color=C_RED))
    ax.annotate("", xy=(a, y - 0.25), xytext=(b, y - 0.25), arrowprops=dict(arrowstyle="-|>", lw=1.2, color=C_BLUE, ls="--"))
    ax.text(5, y + 1.05, title, ha="center", fontsize=11.5, fontweight="bold")
    ax.text(5, y + 0.72, eq, ha="center", fontsize=10.5)
    for k, s in enumerate(steps):
        ax.text(0.5, y - 1.7 - 0.38 * k, s, fontsize=9.5)


def b3_4():
    fig, ax = plt.subplots(figsize=(12, 9.6)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-0.6, 10.6)
    ampoule(ax, 8.6, "T₂ = 900 °C（热）", "T₁ = 800 °C（冷）", "源：ZnS 粉末", "ZnS 单晶", True,
            "(a) 吸热输运：ZnS / I₂（ΔrH > 0 → 热端 → 冷端）",
            "ZnS(s) + I₂(g) ⇌ ZnI₂(g) + ½S₂(g)",
            ["① 源区（热）：平衡右移，ZnS 被 I₂“溶解”成气体 ZnI₂ + S₂",
             "② 气相扩散（红箭头）：ZnI₂、S₂ 从高分压的热端扩散到冷端",
             "③ 沉积区（冷）：平衡左移，ZnS 重新析出、长成晶体",
             "④ 释放的 I₂ 扩散回源区（蓝虚线），继续循环 → 只需少量 I₂"], "#ef9a9a", "#90caf9")
    ampoule(ax, 3.2, "T₁ ≈ 50–80 °C（冷）", "T₂ ≈ 200 °C（热）", "源：粗 Ni", "纯 Ni", True,
            "(b) 放热输运：Mond 法（ΔrH < 0 → 冷端 → 热端）",
            "Ni(s) + 4CO(g) ⇌ Ni(CO)₄(g)    ΔrH ≈ −160 kJ/mol",
            ["① 冷端：放热反应平衡右移，Ni 生成挥发性 Ni(CO)₄（杂质 Fe、Co 几乎不反应）",
             "② Ni(CO)₄ 扩散到热端",
             "③ 热端：平衡左移，Ni(CO)₄ 分解，析出高纯 Ni（99.99 %）",
             "④ CO 回到冷端循环。同理：van Arkel–de Boer 法 Ti + 2I₂ ⇌ TiI₄（热钨丝上析出 Ti）"], "#90caf9", "#ef9a9a")
    save(fig, "B3_04_CVT_examples_ZnS_Mond.png")


def b3_5():
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.9), gridspec_kw=dict(width_ratios=[1, 1, 1.1]))
    dH, dS = 172.5, 0.17586
    T = np.linspace(600, 1400, 200)
    ax = axs[0]
    ax.plot(T, dH - T * dS, color=C_RED, lw=2.5)
    ax.axhline(0, color="k", lw=0.8); ax.axvline(dH / dS, color=C_GRAY, ls="--")
    ax.text(dH / dS + 10, 40, f"T ≈ {dH/dS:.0f} K\n(≈ {dH/dS-273:.0f} °C)\nΔG° = 0, K = 1", fontsize=10)
    ax.set_xlabel("T / K"); ax.set_ylabel("ΔrG° / kJ·mol⁻¹")
    ax.set_title("(a) C(s) + CO₂(g) ⇌ 2CO(g)", fontsize=11.5)
    ax.text(620, -60, "ΔrH° = 2(−110.5) − (−393.5)\n       = +172.5 kJ/mol\nΔrS° = 2(197.7) − 213.8 − 5.7\n       = +175.9 J/(mol·K)",
            fontsize=9.3)
    clean(ax)
    ax = axs[1]
    K = np.exp(-(dH * 1000 - T * dS * 1000) / (R * T))
    x = (-K + np.sqrt(K * K + 4 * K)) / 2
    ax.plot(T, 100 * x, color=C_BLUE, lw=2.5, label="CO")
    ax.plot(T, 100 * (1 - x), color=C_GRAY, lw=2, label="CO₂")
    ax.set_xlabel("T / K"); ax.set_ylabel("平衡气体组成 / %（p = 1 bar）")
    ax.set_title("(b) 高温 CO 多，低温 CO₂ 多", fontsize=11.5)
    ax.legend(); clean(ax)
    ax = axs[2]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(c) 碳的化学输运：吸热 → 热端到冷端", fontsize=11.5)
    ax.add_patch(FancyBboxPatch((0.3, 4.8), 9.4, 1.4, boxstyle="round,pad=0,rounding_size=0.7", fc="#f7fbff", ec="#64b5f6", lw=2))
    for k in range(6):
        ax.add_patch(Circle((1.0 + 0.25 * k, 5.2), 0.15, fc="#333", ec="k"))
    ax.text(1.6, 5.65, "C（热，≈1000 °C）", fontsize=9.5)
    for k in range(5):
        ax.add_patch(Circle((7.8 + 0.25 * k, 5.2), 0.12, fc="#555", ec="k"))
    ax.text(7.4, 5.65, "C 析出（冷，≈600 °C）", fontsize=9.5)
    ax.annotate("", xy=(7.4, 5.3), xytext=(3.0, 5.3), arrowprops=dict(arrowstyle="-|>", lw=2, color=C_RED))
    ax.text(5.2, 5.4, "2CO", color=C_RED, fontsize=10, ha="center")
    ax.annotate("", xy=(3.0, 4.95), xytext=(7.4, 4.95), arrowprops=dict(arrowstyle="-|>", lw=1.2, color=C_BLUE, ls="--"))
    ax.text(5.2, 4.55, "CO₂", color=C_BLUE, fontsize=10, ha="center")
    ax.text(0.2, 3.7, "热端：C + CO₂ → 2CO（吸热，高温有利）\n冷端：2CO → C + CO₂（CO 歧化，析出碳）\n\n"
                      "工业上出现在：高炉炼铁\n• 下部高温区：CO₂ + C → 2CO，再生还原剂 CO\n"
                      "• 上部较冷区：2CO → C + CO₂，碳沉积（积碳）\n（类似地：重整/催化中的“积碳”、CVD 制碳纳米管）",
            fontsize=9.5, va="top")
    save(fig, "B3_05_boudouard_carbon_transport.png")


def rdkit_png(smiles, size=(360, 300)):
    from rdkit import Chem
    from rdkit.Chem.Draw import rdMolDraw2D
    m = Chem.MolFromSmiles(smiles)
    d = rdMolDraw2D.MolDraw2DCairo(*size)
    d.drawOptions().bondLineWidth = 2
    d.DrawMolecule(m); d.FinishDrawing()
    import matplotlib.image as mpimg
    return mpimg.imread(io.BytesIO(d.GetDrawingText()))


def b3_6():
    fig = plt.figure(figsize=(15, 8.4))
    gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.05])
    ax = fig.add_subplot(gs[0, 0]); ax.imshow(rdkit_png("CC(C)O[Ti](OC(C)C)(OC(C)C)OC(C)C")); ax.axis("off")
    ax.set_title("前驱体：Ti(OⁱPr)₄（钛酸四异丙酯）", fontsize=11)
    ax = fig.add_subplot(gs[0, 1:]); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.set_title("关键化学反应", fontsize=11.5)
    eqs = [("水解", "Ti(OR)₄ + H₂O → Ti(OR)₃(OH) + ROH   …→ Ti(OH)₄", C_BLUE),
           ("缩合（失水）", "≡Ti–OH + HO–Ti≡ → ≡Ti–O–Ti≡ + H₂O", C_GREEN),
           ("缩合（失醇）", "≡Ti–OR + HO–Ti≡ → ≡Ti–O–Ti≡ + ROH", C_GREEN),
           ("总", "Ti(OR)₄ + 2H₂O → TiO₂ + 4ROH", C_DARK),
           ("控速", "Ti 的烷氧化物水解极快 → 加乙酰丙酮/乙酸螯合、酸催化、限量加水，否则直接沉淀", C_RED)]
    for k, (a, b, c) in enumerate(eqs):
        ax.text(0.1, 4.4 - k * 0.95, a, fontsize=10.5, color=c, fontweight="bold")
        ax.text(1.9, 4.4 - k * 0.95, b, fontsize=10.5)
    ax = fig.add_subplot(gs[1, :]); ax.axis("off"); ax.set_xlim(0, 20); ax.set_ylim(0, 6)
    rng = np.random.default_rng(1)
    def panel(x0, title, mode):
        ax.add_patch(Rectangle((x0, 1.2), 3.4, 3.4, fc="#e3f2fd" if mode in ("sol", "gel") else "#fafafa", ec="#555"))
        ax.text(x0 + 1.7, 4.85, title, ha="center", fontsize=10.5, fontweight="bold")
        if mode == "sol":
            for _ in range(22):
                ax.add_patch(Circle((x0 + 0.3 + rng.random() * 2.8, 1.5 + rng.random() * 2.8), 0.1, fc=C_ORANGE, ec="k", lw=0.4))
        elif mode in ("gel", "xero"):
            s = 1.0 if mode == "gel" else 0.62
            cx, cy = x0 + 1.7, 2.9
            pts = [(cx + (rng.random() - 0.5) * 3.0 * s, cy + (rng.random() - 0.5) * 3.0 * s) for _ in range(40)]
            for i, p in enumerate(pts):
                for q in pts[i + 1:]:
                    if np.hypot(p[0] - q[0], p[1] - q[1]) < 0.62 * s:
                        ax.plot([p[0], q[0]], [p[1], q[1]], color="#555", lw=1)
            for p in pts:
                ax.add_patch(Circle(p, 0.1, fc=C_ORANGE, ec="k", lw=0.4))
        else:
            ax.add_patch(Rectangle((x0 + 1.1, 2.3), 1.2, 1.2, fc="white", ec=C_DARK, lw=1.5))
            ax.text(x0 + 1.7, 2.9, "TiO₂\n锐钛矿", ha="center", va="center", fontsize=9)
    steps = [(0.2, "① 溶胶 sol", "sol", "Ti(OⁱPr)₄ + iPrOH\n+ acac + HNO₃\n滴加 H₂O，搅拌\n→ 纳米胶粒"),
             (4.3, "② 凝胶 gel", "gel", "Ti–O–Ti 网络贯通\n整个容器（凝胶点）\n孔中充满溶剂\n→ 老化增强"),
             (8.4, "③ 常压干燥 → 干凝胶", "xero", "溶剂蒸发，毛细管力\n把网络压塌\n体积大幅收缩、开裂\n= xerogel"),
             (12.5, "④ 煅烧 400–500 °C", "calc", "除去有机物/OH\n无定形 → 锐钛矿 TiO₂\n（更高温 → 金红石）")]
    for x0, t, m, desc in steps:
        panel(x0, t, m)
        ax.text(x0 + 1.7, 1.0, desc, ha="center", va="top", fontsize=9.3)
    for x0 in (3.65, 7.75, 11.85):
        ax.annotate("", xy=(x0 + 0.6, 2.9), xytext=(x0 - 0.05, 2.9), arrowprops=dict(arrowstyle="-|>", lw=2))
    ax.text(16.4, 4.5, "对比：若第②步后改用\n超临界干燥（无气–液\n界面 → 无毛细管力）\n→ 网络不塌：气凝胶\naerogel，孔隙率 > 90 %", fontsize=9.8,
            bbox=dict(fc="#fff6e0", ec=C_ORANGE), va="top")
    save(fig, "B3_06_TiO2_xerogel_sol_gel.png")


if __name__ == "__main__":
    for f in [b3_1, b3_2, b3_3, b3_4, b3_5, b3_6]:
        f()
