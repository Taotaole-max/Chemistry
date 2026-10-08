# Part B4 配图：化学键类型、各向异性金属、电导率-温度、带隙、dxy 链能带、直接/间接带隙、掺杂、同电子系列、正方网格
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, Ellipse
from common import *

kB = 8.617e-5


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ---------------- B4.1 ----------------
def b4_1():
    fig = plt.figure(figsize=(15, 6.2))
    gs = fig.add_gridspec(1, 2, width_ratios=[0.85, 1.4])
    ax = fig.add_subplot(gs[0])
    r = np.linspace(1, 6, 200)
    ax.plot(r, -1 / r, color=C_RED, lw=2.5, label="离子键：库仑 ∝ −1/r（长程）")
    ax.plot(r, -1 / r ** 6, color=C_BLUE, lw=2.5, label="范德华：∝ −1/r⁶（短程）")
    ax.plot(r, -np.exp(-2.5 * (r - 1)), color=C_GREEN, lw=2.5, ls="--", label="共价：∝ 轨道重叠 ~ e^(−r)（短程）")
    ax.set_xlabel("距离 r（以最近邻距离为 1）"); ax.set_ylabel("相互作用能（归一化）")
    ax.text(3.2, -0.42, "r = 3 时库仑仍剩 33 %\n范德华只剩 0.14 %", fontsize=10)
    ax.legend(fontsize=9.5, loc="lower right"); ax.set_title("(a) 作用程：长程 vs 短程", fontsize=11.5); clean(ax)
    ax = fig.add_subplot(gs[1]); ax.axis("off"); ax.set_xlim(0, 15); ax.set_ylim(0, 8)
    ax.set_title("(b) 五种键：方向性与作用程", fontsize=11.5)
    xs = [1.5, 4.5, 7.5, 10.5, 13.5]
    names = ["离子键", "共价键", "金属键", "范德华力", "氢键"]
    for x, n in zip(xs, names):
        ax.text(x, 7.5, n, ha="center", fontsize=11.5, fontweight="bold")
    # 离子
    for i in range(3):
        for j in range(3):
            plus = (i + j) % 2 == 0
            ax.add_patch(Circle((xs[0] - 0.8 + 0.8 * i, 4.7 + 0.8 * j), 0.25 if plus else 0.35,
                                fc="#cbbdf0" if plus else "#bfe3c0", ec="k", lw=0.6))
            ax.text(xs[0] - 0.8 + 0.8 * i, 4.7 + 0.8 * j, "+" if plus else "−", ha="center", va="center", fontsize=9)
    # 共价 sp3
    c = (xs[1], 5.5)
    for ang in (90, 210, 330, 270):
        t = np.radians(ang)
        L = 1.2 if ang != 270 else 0.6
        ax.plot([c[0], c[0] + L * np.cos(t)], [c[1], c[1] + L * np.sin(t)], color="k", lw=2.5)
        ax.add_patch(Circle((c[0] + L * np.cos(t), c[1] + L * np.sin(t)), 0.18, fc="#555"))
    ax.add_patch(Circle(c, 0.22, fc="#222"))
    ax.text(xs[1], 3.9, "109.5°", ha="center", fontsize=9)
    # 金属
    ax.add_patch(FancyBboxPatch((xs[2] - 1.2, 4.2), 2.4, 2.4, boxstyle="round,pad=0,rounding_size=0.3", fc="#d6e8fb", ec="none"))
    for i in range(3):
        for j in range(3):
            ax.add_patch(Circle((xs[2] - 0.8 + 0.8 * i, 4.6 + 0.8 * j), 0.25, fc="#9e9e9e", ec="k", lw=0.6))
            ax.text(xs[2] - 0.8 + 0.8 * i, 4.6 + 0.8 * j, "+", ha="center", va="center", fontsize=9)
    rng = np.random.default_rng(2)
    for _ in range(14):
        ax.text(xs[2] - 1.1 + 2.2 * rng.random(), 4.3 + 2.2 * rng.random(), "e⁻", fontsize=7, color=C_BLUE)
    # vdW
    for k, y in enumerate((6.2, 4.7)):
        ax.add_patch(Ellipse((xs[3], y), 1.8, 0.8, fc="#fff3e0", ec=C_ORANGE))
        ax.text(xs[3] - 0.55, y, "δ+", fontsize=9); ax.text(xs[3] + 0.3, y, "δ−", fontsize=9)
    ax.text(xs[3], 5.45, "瞬时偶极–诱导偶极", ha="center", fontsize=8.5)
    # H 键
    ax.text(xs[4] - 1.3, 5.5, "O–H", fontsize=13, va="center"); ax.text(xs[4] + 0.75, 5.5, "O", fontsize=13, va="center")
    ax.plot([xs[4] + 0.0, xs[4] + 0.65], [5.5, 5.5], ls=(0, (2, 2)), color=C_RED, lw=2)
    ax.text(xs[4], 4.7, "D–H···A 近直线\n（≈180°）", ha="center", fontsize=9)
    rows = [("方向性", ["无", "强", "无", "无", "有"]),
            ("作用程", ["长程 1/r", "短程", "中等（离域）", "短程 1/r⁶", "短程"]),
            ("各向异性", ["否（各向同性）", "是", "否（多数）", "否", "是"]),
            ("典型", ["NaCl", "金刚石、Si", "Cu、Fe", "Ar(s)、石墨层间", "冰"])]
    for k, (lab, vals) in enumerate(rows):
        y = 3.0 - 0.75 * k
        ax.text(-0.2, y, lab, fontsize=10.5, fontweight="bold", ha="left")
        for x, v in zip(xs, vals):
            col = C_RED if v in ("强", "是", "有") else "black"
            ax.text(x + 0.3, y, v, ha="center", fontsize=10, color=col)
    save(fig, "B4_01_bond_types_in_solids.png")


# ---------------- B4.2 ----------------
def b4_2():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.2))
    ax = axs[0]; setup_ax(ax, "(a) KCP：K₂[Pt(CN)₄]Br₀.₃·3H₂O —— 一维金属", fs=11.5)
    sc = Scene(ax, azim=-72, elev=18, scale=1.0)
    for n in range(5):
        x = n * 2.88
        rot = 45 * (n % 2)
        sc.ball((x, 0, 0), 0.38, C_BLUE, label="Pt", fs=8)
        for k in range(4):
            t = np.radians(rot + 90 * k)
            c = np.array([x, 1.95 * np.cos(t), 1.95 * np.sin(t)])
            nn = np.array([x, 3.1 * np.cos(t), 3.1 * np.sin(t)])
            sc.line((x, 0, 0), c, color="#555", lw=2)
            sc.line(c, nn, color="#555", lw=3)
            sc.ball(c, 0.22, C_DARK); sc.ball(nn, 0.22, "#6a8fd8")
        if n < 4:
            sc.line((x, 0, 0), (x + 2.88, 0, 0), color=C_RED, lw=3, ls="--")
    sc.render()
    foot(ax, "平面 [Pt(CN)₄] 沿链轴堆叠，Pt–Pt 仅 2.88 Å（Pt 金属 2.77 Å）\nPt 的 dz² 沿链重叠成能带；部分氧化（Pt²·³⁺）→ 能带未填满 → 金属性\n"
         "σ(沿链) / σ(垂直链) ≈ 10⁵：导电极度各向异性", fontsize=9.8)
    ax = axs[1]; setup_ax(ax, "(b) Zn（Cd 类似）：hcp 但 c/a 被拉长", fs=11.5)

    def hcp(sc, c, col, off):
        hexv = [(np.cos(np.radians(60 * k)), np.sin(np.radians(60 * k))) for k in range(6)]
        for z in (0, c):
            for k in range(6):
                sc.line((hexv[k][0] + off, hexv[k][1], z), (hexv[(k + 1) % 6][0] + off, hexv[(k + 1) % 6][1], z), color="#888")
        for k in range(6):
            sc.line((hexv[k][0] + off, hexv[k][1], 0), (hexv[k][0] + off, hexv[k][1], c), color="#888")
        for z in (0, c):
            sc.ball((off, 0, z), 0.17, col)
            for (x, y) in hexv:
                sc.ball((x + off, y, z), 0.17, col)
        for ang in (30, 150, 270):
            t = np.radians(ang)
            sc.ball((np.cos(t) / np.sqrt(3) + off, np.sin(t) / np.sqrt(3), c / 2), 0.17, col)
    sc = Scene(ax, azim=-80, elev=10, scale=1.0)
    hcp(sc, 1.633, C_GRAY, -1.6)
    hcp(sc, 1.856, C_ORANGE, 1.6)
    sc.text((-1.6, 0, 2.15), "理想 hcp\nc/a = 1.633", ha="center", fontsize=10)
    sc.text((1.6, 0, 2.35), "Zn：c/a = 1.856", ha="center", fontsize=10)
    sc.render()
    foot(ax, "层内 6 个近邻 2.66 Å，层间 6 个 2.91 Å → 键合在基面内更强\n热膨胀：沿 c 轴约为基面内的 4–5 倍；只沿基面滑移\n"
         "其他例子：石墨（层内导电 ≫ 层间）、Bi、α-Ga", fontsize=9.8)
    save(fig, "B4_02_anisotropic_metals_KCP_Zn.png")


# ---------------- B4.3 ----------------
def b4_3():
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.9))
    ax = axs[0]
    T = np.linspace(50, 600, 200)
    rho = 1.7 * (T / 293) ** 1 + 0.02
    ax.plot(T, 1 / rho, color=C_RED, lw=2.5)
    ax.set_xlabel("T / K"); ax.set_ylabel("σ（相对值）")
    ax.set_title("(a) 金属（如 Cu）：σ 随 T 升高而下降", fontsize=11)
    ax.text(250, 1.6, "n ≈ 8.5×10²² cm⁻³，几乎不随 T 变\nμ ↓（声子散射 ∝ 1/T）\n→ ρ ∝ T，σ = neμ ↓", fontsize=9.6)
    clean(ax)
    ax = axs[1]
    Eg = 1.12
    invT = np.linspace(1.6, 4.0, 100)
    Tt = 1000 / invT
    lnsig = np.log(Tt ** 1.5 * np.exp(-Eg / (2 * kB * Tt)) * (Tt / 300) ** -1.5)
    ax.plot(invT, lnsig - lnsig.max(), color=C_BLUE, lw=2.5)
    ax.set_xlabel("1000 / T（K⁻¹）"); ax.set_ylabel("ln σ（相对值）")
    ax.set_title("(b) 本征半导体（如 Si）：σ 随 T 指数上升", fontsize=11)
    ax.text(2.55, -2.5, "n = p ∝ T^(3/2)·exp(−E_g / 2kT)\n斜率 = −E_g / 2k\nμ 也随 T 下降，\n但 n 的指数增长占绝对优势", fontsize=9.6)
    clean(ax)
    ax = axs[2]
    T = np.linspace(20, 900, 400)
    ND, Ed = 1e16, 0.045
    Nc = 2.8e19 * (T / 300) ** 1.5; Nv = 1.04e19 * (T / 300) ** 1.5
    Egt = 1.17 - 4.73e-4 * T ** 2 / (T + 636)
    ni = np.sqrt(Nc * Nv) * np.exp(-Egt / (2 * kB * T))
    a = Nc / 2 * np.exp(-Ed / (kB * T))
    next_ = (-a + np.sqrt(a * a + 4 * a * ND)) / 2
    n = next_ / 2 + np.sqrt((next_ / 2) ** 2 + ni ** 2)
    ax.semilogy(1000 / T, n, color=C_PURPLE, lw=2.5)
    ax.semilogy(1000 / T, ni, color=C_GRAY, ls="--", lw=1.2)
    ax.set_xlim(1, 30); ax.set_ylim(1e10, 1e18)
    ax.set_xlabel("1000 / T（K⁻¹）"); ax.set_ylabel("电子浓度 n / cm⁻³")
    ax.set_title("(c) n 型 Si（N_D = 10¹⁶ cm⁻³）：三个区", fontsize=11)
    ax.text(18, 2e16, "冻析区\n（施主未电离）", fontsize=9.3, ha="center")
    ax.text(6.5, 2.2e16, "饱和区\nn ≈ N_D", fontsize=9.3, ha="center")
    ax.text(1.3, 3e17, "本征区", fontsize=9.3)
    ax.text(5, 3e11, "灰虚线：本征 nᵢ", fontsize=9, color=C_GRAY)
    clean(ax)
    save(fig, "B4_03_conductivity_vs_temperature.png")


# ---------------- B4.4 ----------------
def b4_4():
    fig, ax = plt.subplots(figsize=(13, 6.4)); ax.axis("off"); ax.set_xlim(0, 16); ax.set_ylim(-1, 10.6)
    cfg = [(1.5, "绝缘体", 5.0, "E_g > 4 eV（常见 5–10 eV）\n金刚石 5.5、NaCl ≈ 8.5、SiO₂ ≈ 9", False),
           (6.0, "半导体", 1.2, "E_g ≈ 0.1–3 eV\nGe 0.66、Si 1.12、GaAs 1.42", False),
           (10.5, "金属", 0, "E_g = 0 eV\n能带部分填充（或价带导带重叠）", True)]
    for x, name, gap, txt, metal in cfg:
        ax.text(x + 1.25, 10.0, name, ha="center", fontsize=13, fontweight="bold")
        if metal:
            ax.add_patch(Rectangle((x, 1.0), 2.5, 5.5, fc="white", ec="k", lw=1.5))
            ax.add_patch(Rectangle((x, 1.0), 2.5, 3.0, fc=C_BLUE, alpha=0.6, ec="k"))
            ax.plot([x - 0.3, x + 2.8], [4.0, 4.0], color=C_RED, ls="--", lw=1.5); ax.text(x + 2.9, 4.0, "E_F", color=C_RED, va="center")
            ax.text(x + 1.25, 5.3, "空能级", ha="center"); ax.text(x + 1.25, 2.5, "已占据", ha="center", color="white")
        else:
            top = 1.0 + 2.0
            ax.add_patch(Rectangle((x, 1.0), 2.5, 2.0, fc=C_BLUE, alpha=0.6, ec="k"))
            g = gap * 0.8
            ax.add_patch(Rectangle((x, top + g), 2.5, 2.0, fc="white", ec="k", lw=1.5))
            ax.text(x + 1.25, 2.0, "价带（满）", ha="center", color="white")
            ax.text(x + 1.25, top + g + 1.0, "导带（空）", ha="center")
            ax.annotate("", xy=(x + 2.75, top + g), xytext=(x + 2.75, top), arrowprops=dict(arrowstyle="<->", color=C_RED))
            ax.text(x + 2.9, top + g / 2, "E_g", color=C_RED, va="center")
        ax.text(x + 1.25, 0.5, txt, ha="center", va="top", fontsize=10)
    ax.annotate("", xy=(0.5, 9.5), xytext=(0.5, 1.0), arrowprops=dict(arrowstyle="->"))
    ax.text(0.35, 4.5, "E", fontsize=12, ha="right")
    save(fig, "B4_04_band_gaps_classes.png")


# ---------------- B4.5 dxy 链 ----------------
def petals(sc, center, sign, scale=0.95, plane=("y", "z"), col_p=C_BLUE, col_m=C_RED, alpha=0.85):
    """在垂直于链（链沿 x）的平面内画 4 瓣 d 轨道（局部坐标里就是 dxy）。"""
    phi = np.linspace(0, 2 * np.pi, 400)
    for q in range(4):
        a0 = q * np.pi / 2
        ph = np.linspace(a0, a0 + np.pi / 2, 100)
        r = np.abs(np.sin(2 * ph)) * scale
        pts = [(center[0], center[1] + rr * np.cos(p), center[2] + rr * np.sin(p)) for rr, p in zip(r, ph)]
        s = np.sign(np.sin(2 * (a0 + np.pi / 4))) * sign
        sc.poly(pts, col_p if s > 0 else col_m, alpha=alpha, ec="k", lw=0.6)


def b4_5():
    fig = plt.figure(figsize=(15, 13))
    gs = fig.add_gridspec(3, 3, height_ratios=[1, 0.62, 0.62], width_ratios=[1, 1, 0.9], hspace=0.32)
    k = np.linspace(0, np.pi, 200)
    ax = fig.add_subplot(gs[0, 0])
    ax.plot(k, -0.35 * np.cos(k), color=C_BLUE, lw=3.5, label="dxy（δ）：窄，向上")
    ax.plot(k, -2.0 * np.cos(k) - 0.2, color=C_GRAY, lw=1.3, ls="--", label="dz²（σ）：宽，向上")
    ax.plot(k, 1.0 * np.cos(k) + 0.1, color=C_GRAY, lw=1.3, ls=":", label="dxz, dyz（π）：向下")
    ax.set_xticks([0, np.pi]); ax.set_xticklabels(["k = 0", "k = π/a"])
    ax.set_ylabel("E"); ax.set_yticks([])
    ax.set_title("(a) 能带图 E(k)", fontsize=12)
    ax.text(0.05, -0.62, "δ 成键（最低）", color=C_BLUE, fontsize=10)
    ax.text(2.2, 0.48, "δ 反键（最高）", color=C_BLUE, fontsize=10)
    ax.annotate("", xy=(3.25, 0.35), xytext=(3.25, -0.35), arrowprops=dict(arrowstyle="<->", color=C_BLUE))
    ax.text(3.3, 0, "带宽 W = 4|β(δ)|\n（很小）", fontsize=9.5, va="center", color=C_BLUE)
    ax.legend(fontsize=9, loc="lower right"); ax.set_xlim(0, 3.9); clean(ax)
    ax = fig.add_subplot(gs[0, 1])
    E = np.linspace(-0.3499, 0.3499, 400)
    dos = 1 / np.sqrt(0.35 ** 2 - E ** 2)
    ax.fill_betweenx(E, 0, dos, color=C_BLUE, alpha=0.35); ax.plot(dos, E, color=C_BLUE, lw=2)
    E2 = np.linspace(-1.999, 1.999, 400) - 0.2
    ax.plot(1 / np.sqrt(4 - (E2 + 0.2) ** 2), E2, color=C_GRAY, lw=1.2, ls="--")
    ax.set_xlim(0, 12); ax.set_ylim(-2.4, 2.0)
    ax.set_xlabel("态密度 DOS(E)"); ax.set_yticks([]); ax.set_ylabel("E")
    ax.set_title("(c) 态密度 DOS", fontsize=12)
    ax.text(3.0, 0.55, "dxy 带：窄而高\n两端（k = 0、π/a）dE/dk = 0\n→ van Hove 奇点（发散）", fontsize=9.5, color=C_BLUE)
    ax.text(2.0, -1.6, "灰虚线：宽的 dz² 带作对比\n（同样多的态摊在更宽的能量上）", fontsize=9, color=C_GRAY)
    ax.text(6.5, -0.15, "DOS ∝ 1/|dE/dk|", fontsize=10)
    clean(ax)
    ax = fig.add_subplot(gs[0, 2]); ax.axis("off"); ax.set_title("要点", fontsize=12)
    ax.text(0.0, 0.97, "• dxy 位于 xy 平面，垂直于链轴 z\n• 相邻原子的 dxy “面对面”平行\n  → δ 型重叠（4 瓣对 4 瓣）\n"
            "• δ 重叠最弱（σ > π > δ）\n  → 能带最窄\n• k = 0：同相，同号瓣相对\n  → δ 成键，能量最低\n• k = π/a：相邻反号\n  → δ 反键，能量最高\n"
            "• 所以 dxy 带从 k = 0 向上走\n  （与 s、dz² 同向；与 pz、dxz 反向）",
            fontsize=10.2, va="top", transform=ax.transAxes)
    for row, (sgn_fn, title) in enumerate([(lambda n: 1, "(b1) k = 0：所有原子系数相同 → 相邻瓣同号相对 → δ 成键（能量最低）"),
                                           (lambda n: (-1) ** n, "(b2) k = π/a：系数 + − + − 交替 → 相邻瓣异号 → δ 反键（能量最高）")]):
        ax = fig.add_subplot(gs[1 + row, :])
        setup_ax(ax, title, fs=11.5)
        sc = Scene(ax, azim=-62, elev=16, scale=1.0)
        for n in range(6):
            x = n * 2.0
            sc.line((x - 1.0, 0, 0), (x + 1.0, 0, 0), color="#999", lw=1)
            petals(sc, (x, 0, 0), sgn_fn(n), scale=1.05)
            sc.ball((x, 0, 0), 0.1, C_DARK)
        sc.text((11.3, 0, -0.1), "z（链轴）", fontsize=10)
        sc.render()
        foot(ax, "蓝 = +，红 = −。每个 dxy 的四瓣位于垂直于链的 xy 平面内" + ("；k = 0 时相邻原子“蓝对蓝、红对红”，原子间无节面" if row == 0 else "；k = π/a 时相邻原子“蓝对红”，每两个原子之间都多一个节面"), fontsize=9.8)
    save(fig, "B4_05_dxy_chain_band_DOS.png")


# ---------------- B4.6 ----------------
def b4_6():
    fig, axs = plt.subplots(1, 2, figsize=(13, 5.6))
    k = np.linspace(-1, 1, 300)
    for ax, direct in zip(axs, (True, False)):
        vb = -0.8 * k ** 2
        cb = 1.4 + 1.2 * k ** 2 if direct else 1.1 + 1.6 * (k - 0.75) ** 2
        ax.plot(k, vb, color=C_BLUE, lw=2.5); ax.plot(k, cb, color=C_RED, lw=2.5)
        ax.fill_between(k, -1.2, vb, color=C_BLUE, alpha=0.15)
        ax.set_ylim(-1.0, 3.2); ax.set_yticks([]); ax.set_xticks([0]); ax.set_xticklabels(["k = 0（Γ）"])
        ax.set_ylabel("E"); ax.set_xlabel("波矢 k")
        if direct:
            ax.annotate("", xy=(0, 1.4), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=C_GREEN, lw=2.5))
            ax.text(0.05, 0.65, "hν ≥ E_g\n竖直跃迁\n（光子动量≈0）", fontsize=10, color=C_GREEN)
            ax.set_title("(a) 直接带隙：VB 顶与 CB 底在同一 k\n例：GaAs 1.42 eV、GaN 3.4 eV、InP 1.34 eV", fontsize=11)
            ax.text(0.5, -0.2, "吸收强、发光效率高 → LED、激光二极管；\n薄膜太阳能电池（GaAs 吸收层约 1–2 µm 即可）", fontsize=9.8, transform=ax.transAxes, ha="center", va="top")
        else:
            ax.annotate("", xy=(0, 1.9), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=C_GREEN, lw=2, ls="--"))
            ax.annotate("", xy=(0.73, 1.12), xytext=(0, 1.12), arrowprops=dict(arrowstyle="-|>", color=C_ORANGE, lw=2.5))
            ax.annotate("", xy=(0.0, 1.12), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=C_GREEN, lw=2.5))
            ax.text(-0.05, 0.5, "光子\n（提供能量）", fontsize=9.6, color=C_GREEN, ha="right")
            ax.text(0.37, 0.92, "声子（提供动量 Δk）", fontsize=9.6, color=C_ORANGE, ha="center", va="top")
            ax.text(0.5, -0.2, "需光子 + 声子同时参与的二级过程 → 概率小\n吸收弱（Si 电池需约 100–200 µm 厚）、几乎不发光", fontsize=9.8, transform=ax.transAxes, ha="center", va="top")
            ax.set_title("(b) 间接带隙：CB 底在 k ≠ 0（如 Si 在 Γ→X 的 85 % 处）\n例：Si 1.12 eV、Ge 0.66 eV、GaP 2.26 eV", fontsize=11)
            ax.set_xticks([0, 0.75]); ax.set_xticklabels(["k = 0（Γ）", "k₀"])
        clean(ax)
    save(fig, "B4_06_direct_vs_indirect_gap.png")


# ---------------- B4.7 ----------------
def b4_7():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.4), gridspec_kw=dict(width_ratios=[1, 1, 1.05]))
    for ax, dop, col, title in [(axs[0], "P", C_RED, "(a) n 型：Si 中掺 P（5 价电子）"), (axs[1], "B", C_GREEN, "(b) p 型：Si 中掺 B（3 价电子）")]:
        setup_ax(ax, title, fs=11.5)
        for i in range(5):
            for j in range(5):
                if i < 4:
                    ax.plot([i, i + 1], [j, j], color="#888", lw=3, zorder=0)
                if j < 4:
                    ax.plot([i, i], [j, j + 1], color="#888", lw=3, zorder=0)
        for i in range(5):
            for j in range(5):
                c = (i, j) == (2, 2)
                ax.add_patch(Circle((i, j), 0.28, fc=col if c else "#cfd8dc", ec="k", zorder=2))
                ax.text(i, j, dop if c else "Si", ha="center", va="center", fontsize=9, zorder=3, color="white" if c else "k")
        if dop == "P":
            ax.add_patch(Circle((2.55, 2.55), 0.1, fc=C_BLUE, zorder=4))
            ax.add_patch(Circle((2, 2), 0.9, fc="none", ec=C_BLUE, ls="--", zorder=1))
            ax.text(2.0, -0.75, "P 用 4 个电子成键，多出 1 个 e⁻（蓝点）\n只被弱束缚（≈45 meV）→ 室温即进入导带", fontsize=9.8, color=C_BLUE, ha="center", va="top")
        else:
            ax.add_patch(Circle((2.5, 2.0), 0.11, fc="white", ec=C_RED, lw=2, zorder=4))
            ax.text(2.0, -0.75, "B 只有 3 个价电子，一根键缺 1 个 e⁻ = 空穴 h⁺\n邻近价电子跳来填补 → 空穴在价带中移动", fontsize=9.8, color=C_RED, ha="center", va="top")
        ax.set_xlim(-0.5, 4.6); ax.set_ylim(-1.9, 4.6)
    ax = axs[2]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 9)
    ax.set_title("(c) 能带图中的杂质能级", fontsize=11.5)
    for x0, lev, lab, fe in [(0.3, 5.85, "施主能级 E_D\n（CB 下 ≈0.045 eV）", 5.35), (5.3, 2.45, "受主能级 E_A\n（VB 上 ≈0.045 eV）", 2.95)]:
        ax.add_patch(Rectangle((x0, 0.8), 4.2, 1.5, fc=C_BLUE, alpha=0.55, ec="k"))
        ax.add_patch(Rectangle((x0, 6.0), 4.2, 1.5, fc="white", ec="k"))
        ax.text(x0 + 2.1, 1.55, "价带", ha="center", color="white"); ax.text(x0 + 2.1, 6.75, "导带", ha="center")
        for q in range(5):
            ax.plot([x0 + 0.4 + 0.8 * q, x0 + 0.8 + 0.8 * q], [lev, lev], color=C_RED if x0 < 1 else C_GREEN, lw=2.5)
        ax.text(x0 + 2.1, 4.1, lab, ha="center", fontsize=9.3)
        ax.plot([x0, x0 + 4.2], [fe, fe], ls="--", color=C_PURPLE); ax.text(x0 + 4.25, fe, "E_F", color=C_PURPLE, fontsize=9, va="center")
    for q in range(3):
        ax.add_patch(Circle((1.0 + 1.1 * q, 6.25), 0.12, fc=C_BLUE))
        ax.add_patch(Circle((6.0 + 1.1 * q, 2.05), 0.12, fc="white", ec=C_RED, lw=1.5))
    ax.text(2.4, 8.3, "n 型：多子 = 电子\nE_F 靠近导带", ha="center", fontsize=10)
    ax.text(7.4, 8.3, "p 型：多子 = 空穴\nE_F 靠近价带", ha="center", fontsize=10)
    save(fig, "B4_07_n_p_doping.png")


# ---------------- B4.8 ----------------
def b4_8():
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    names = ["C\n（金刚石）", "Si", "Ge", "α-Sn"]
    d = [1.54, 2.35, 2.45, 2.81]; Eg = [5.47, 1.12, 0.66, 0.08]
    ax.plot(d, Eg, "o-", color=C_BLUE, lw=2, ms=9)
    for x, y, n in zip(d, Eg, names):
        ax.text(x + 0.03, y + 0.2, f"{n}  {y} eV", fontsize=10)
    ax.set_xlabel("E–E 键长 / Å"); ax.set_ylabel("带隙 E_g / eV（300 K）")
    ax.set_title("(a) 第 14 族金刚石结构：键越长，带隙越小", fontsize=11.5); ax.set_ylim(-0.3, 6.6); ax.set_xlim(1.4, 3.3); clean(ax)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(b) 原因：成键–反键分裂随重叠减小", fontsize=11.5)
    for x0, split, lab in [(1.0, 2.6, "Si（Si–Si 2.35 Å）"), (5.6, 1.9, "Ge（Ge–Ge 2.45 Å）")]:
        mid = 4.0
        ax.plot([x0, x0 + 1.0], [mid, mid], color="k", lw=2); ax.text(x0 - 0.1, mid, "sp³", ha="right", va="center")
        ax.plot([x0 + 1.8, x0 + 3.2], [mid + split, mid + split], color=C_RED, lw=3)
        ax.plot([x0 + 1.8, x0 + 3.2], [mid - split * 0.8, mid - split * 0.8], color=C_BLUE, lw=3)
        ax.plot([x0 + 1.0, x0 + 1.8], [mid, mid + split], ls=":", color="#777"); ax.plot([x0 + 1.0, x0 + 1.8], [mid, mid - split * 0.8], ls=":", color="#777")
        ax.text(x0 + 3.3, mid + split, "反键 → 导带", va="center", fontsize=9, color=C_RED)
        ax.text(x0 + 3.3, mid - split * 0.8, "成键 → 价带", va="center", fontsize=9, color=C_BLUE)
        ax.text(x0 + 2.0, 0.6, lab, ha="center", fontsize=10)
    ax.text(5, 7.6, "原子越大 → 轨道越弥散、键越长 → 重叠 β 越小 → 分裂越小 → E_g 越小", ha="center", fontsize=9.8)
    save(fig, "B4_08_Si_vs_Ge_gap.png")


# ---------------- B4.9/10 ----------------
def b4_9_10():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.4))
    ax = axs[0]
    names = ["Ge", "GaAs", "ZnSe", "CuBr"]
    Eg = [0.66, 1.42, 2.70, 2.95]; dchi = [0, 2.18 - 1.81, 2.55 - 1.65, 2.96 - 1.90]
    a = [5.658, 5.653, 5.668, 5.69]
    cols = [C_GRAY, C_BLUE, C_GREEN, C_PURPLE]
    ax.bar(range(4), Eg, color=cols, width=0.6)
    for i in range(4):
        ax.text(i, Eg[i] + 0.06, f"{Eg[i]} eV", ha="center", fontsize=11)
        ax.text(i, 0.15, f"Δχ = {dchi[i]:.2f}\na = {a[i]} Å", ha="center", fontsize=9, color="white")
    ax.set_xticks(range(4)); ax.set_xticklabels(["Ge\n(IV–IV)", "GaAs\n(III–V)", "ZnSe\n(II–VI)", "CuBr\n(I–VII)"], fontsize=10.5)
    ax.set_ylabel("E_g / eV（300 K）"); ax.set_ylim(0, 3.4)
    ax.set_title("(a) 第 4 周期同电子系列：晶格常数几乎相同，E_g 随离子性增大", fontsize=11)
    ax.annotate("", xy=(2.3, 3.2), xytext=(-0.3, 3.2), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(1.0, 3.25, "Ge < GaAs < ZnSe（B4.10 的答案）", ha="center", fontsize=10)
    clean(ax)
    ax = axs[1]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.set_title("(b) 原因：两原子轨道能级不同 → 分裂加大", fontsize=11.5)
    for x0, dA, lab in [(0.3, 0.0, "Ge–Ge（同核）"), (5.3, 0.9, "Ga–As（异核）")]:
        mid = 4.0
        ax.plot([x0, x0 + 0.8], [mid + dA, mid + dA], color="k", lw=2)
        ax.plot([x0 + 3.4, x0 + 4.2], [mid - dA, mid - dA], color="k", lw=2)
        lab1, lab2 = ("Ge", "Ge") if dA == 0 else ("Ga", "As")
        ax.text(x0 + 0.4, mid + dA + 0.25, lab1, ha="center"); ax.text(x0 + 3.8, mid - dA + 0.25, lab2, ha="center")
        V2, C = 1.6, dA
        split = np.sqrt(V2 ** 2 + C ** 2)
        ax.plot([x0 + 1.6, x0 + 2.6], [mid + split, mid + split], color=C_RED, lw=3)
        ax.plot([x0 + 1.6, x0 + 2.6], [mid - split, mid - split], color=C_BLUE, lw=3)
        for xa, ya in [(x0 + 0.8, mid + dA), (x0 + 3.4, mid - dA)]:
            ax.plot([xa, x0 + 1.6 if xa < x0 + 2 else x0 + 2.6], [ya, mid + split], ls=":", color="#777")
            ax.plot([xa, x0 + 1.6 if xa < x0 + 2 else x0 + 2.6], [ya, mid - split], ls=":", color="#777")
        ax.annotate("", xy=(x0 + 2.1, mid + split), xytext=(x0 + 2.1, mid - split), arrowprops=dict(arrowstyle="<->", color=C_PURPLE))
        ax.text(x0 + 2.2, mid, f"∝ E_g", color=C_PURPLE, fontsize=9)
        ax.text(x0 + 2.1, 0.8, lab, ha="center", fontsize=10.5)
    ax.text(5, 7.5, "E_g² ≈ E_h²（共价部分） + C²（离子部分）    —— Phillips–Van Vechten", ha="center", fontsize=10)
    ax.text(5, 0.1, "电负性差越大，成键态越偏向 As（阴离子），反键态越偏向 Ga → 间隔变大", ha="center", fontsize=9.5)
    save(fig, "B4_09_10_isoelectronic_gaps.png")


# ---------------- B4.11 正方网格 ----------------
def sqnet_bands(fx=1.0, fy=1.0):
    bs, sig, pi = -1.0, 1.2, 0.35
    path = [(0, 0), (np.pi, 0), (np.pi, np.pi), (0, 0), (0, np.pi), (np.pi, np.pi)]
    ks, xs = [], []
    x = 0
    ticks = [0]
    for (a, b), (c, d) in zip(path[:-1], path[1:]):
        L = np.hypot(c - a, d - b)
        t = np.linspace(0, 1, 80)
        for tt in t:
            ks.append((a + (c - a) * tt, b + (d - b) * tt)); xs.append(x + L * tt)
        x += L; ticks.append(x)
    ks = np.array(ks); xs = np.array(xs)
    kx, ky = ks[:, 0], ks[:, 1]
    Es = -9.0 + 2 * bs * fx * np.cos(kx) + 2 * bs * fy * np.cos(ky)
    Epx = 2 * sig * fx * np.cos(kx) - 2 * pi * fy * np.cos(ky)
    Epy = -2 * pi * fx * np.cos(kx) + 2 * sig * fy * np.cos(ky)
    Epz = 1.0 - 2 * pi * fx * np.cos(kx) - 2 * pi * fy * np.cos(ky)
    return xs, ticks, Es, Epx, Epy, Epz


def b4_11():
    fig, axs = plt.subplots(1, 3, figsize=(15.5, 6), gridspec_kw=dict(width_ratios=[0.6, 1, 1]))
    ax = axs[0]; ax.axis("off"); ax.set_xlim(0, 6); ax.set_ylim(0, 10); ax.set_aspect("equal")
    ax.set_title("实空间", fontsize=11.5)
    for j in range(3):
        for i in range(3):
            ax.add_patch(Circle((1.8 + 1.2 * i, 6.3 + 1.2 * j), 0.15, fc=C_GRAY))
    for j in range(3):
        for i in range(3):
            ax.add_patch(Circle((2.2 + 0.8 * i, 1.3 + 1.2 * j), 0.15, fc=C_ORANGE))
    ax.annotate("", xy=(5.6, 1.3), xytext=(4.6, 1.3), arrowprops=dict(arrowstyle="-|>", color=C_RED))
    ax.annotate("", xy=(0.6, 1.3), xytext=(1.6, 1.3), arrowprops=dict(arrowstyle="-|>", color=C_RED))
    ax.text(3.0, 9.6, "正方网格 a × a", ha="center", fontsize=10)
    ax.text(3.0, 5.1, "↓ 沿 x 方向压缩", ha="center", fontsize=11, color=C_RED)
    ax.text(3.0, 0.2, "矩形网格：x 间距 a' < a，y 间距仍为 a", ha="center", fontsize=10)
    ax.set_xlim(0, 6)
    for ax, (fx, fy), title in [(axs[1], (1, 1), "(a) 正方网格：X 与 Y(X') 等价"),
                                (axs[2], (1.6, 1.0), "(b) 沿 x 压缩：x 方向相互作用增强")]:
        xs, ticks, Es, Epx, Epy, Epz = sqnet_bands(fx, fy)
        ax.plot(xs, Es, color=C_DARK, lw=2, label="s")
        ax.plot(xs, Epx, color=C_RED, lw=2, label="p$_x$")
        ax.plot(xs, Epy, color=C_BLUE, lw=2, label="p$_y$")
        ax.plot(xs, Epz, color=C_GREEN, lw=1.5, ls="--", label="p$_z$")
        for t in ticks:
            ax.axvline(t, color="#ccc", lw=0.8)
        ax.set_xticks(ticks); ax.set_xticklabels(["Γ", "X", "M", "Γ", "Y(X')", "M"])
        ax.set_xlim(ticks[0], ticks[-1]); ax.set_yticks([]); ax.set_ylabel("E")
        ax.set_title(title, fontsize=11.5); ax.legend(fontsize=9, loc="lower right", ncol=4)
    axs[2].annotate("Γ 点 px / py 简并解除", xy=(0.05, 2 * 1.2 * 1.6 - 2 * 0.35), xytext=(0.6, -2.0),
                    arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    axs[2].annotate("", xy=(0.05, -2 * 0.35 * 1.6 + 2 * 1.2), xytext=(0.6, -2.0), arrowprops=dict(arrowstyle="->"))
    axs[2].text(0.5, -0.1, "Γ→X（压缩方向）：s、px 等带色散变大（变宽）；Γ→Y 基本不变 → X 与 Y 不再等价", fontsize=9.8, transform=axs[2].transAxes, ha="center", va="top")
    axs[1].annotate("Γ 点 px = py（简并）", xy=(0.05, 2 * 1.2 - 2 * 0.35), xytext=(0.6, -2.0),
                    arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    save(fig, "B4_11_square_net_compressed.png")


if __name__ == "__main__":
    for f in [b4_1, b4_2, b4_3, b4_4, b4_5, b4_6, b4_7, b4_8, b4_9_10, b4_11]:
        f()
