# Part B2 配图：相图（边缘固溶度、匀晶、杠杆规则、共晶）、点缺陷、掺杂
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from common import *

R = 8.314


def ideal_lens(TA, TB, HA, HB, n=200):
    """理想溶液（液、固均理想）的匀晶相图：返回 T, x_B(液相线), x_B(固相线)。"""
    T = np.linspace(min(TA, TB) + 0.01, max(TA, TB) - 0.01, n)
    kA = np.exp(HA * (1 - T / TA) / (R * T))
    kB = np.exp(HB * (1 - T / TB) / (R * T))
    xl = (1 - kA) / (kB - kA)
    xs = kB * xl
    return T, xl, xs


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def b2_1():
    fig, ax = plt.subplots(figsize=(10, 6))
    TA, TB, TE, xE = 327, 232, 183, 61.9
    xa, xb = 18.3, 97.8
    x1 = np.linspace(0, xE, 100); liq1 = TA - (TA - TE) * (x1 / xE) ** 1.15
    x2 = np.linspace(xE, 100, 100); liq2 = TE + (TB - TE) * ((x2 - xE) / (100 - xE)) ** 0.9
    s1x = np.linspace(0, xa, 50); s1 = TA - (TA - TE) * (s1x / xa) ** 1.1
    s2x = np.linspace(xb, 100, 50); s2 = TE + (TB - TE) * ((s2x - xb) / (100 - xb)) ** 0.9
    Tv = np.linspace(TE, 0, 60)
    solv1 = 1.5 + (xa - 1.5) * ((Tv - 0) / TE) ** 2.2
    solv2 = 99.6 - (99.6 - xb) * ((Tv - 0) / TE) ** 2.2
    ax.fill_betweenx(np.r_[Tv[::-1], s1[::-1]], 0, np.r_[solv1[::-1], s1x[::-1]], color=C_BLUE, alpha=0.25)
    ax.fill_betweenx(np.r_[Tv[::-1], s2], np.r_[solv2[::-1], s2x], 100, color=C_ORANGE, alpha=0.3)
    ax.plot(x1, liq1, color=C_RED, lw=2); ax.plot(x2, liq2, color=C_RED, lw=2, label="液相线")
    ax.plot(s1x, s1, color=C_BLUE, lw=2); ax.plot(s2x, s2, color=C_BLUE, lw=2, label="固相线")
    ax.plot([xa, xb], [TE, TE], color=C_BLUE, lw=2)
    ax.plot(solv1, Tv, color=C_GREEN, lw=2, ls="--", label="固溶度线（solvus）")
    ax.plot(solv2, Tv, color=C_GREEN, lw=2, ls="--")
    ax.text(45, 280, "L（熔体）", fontsize=13, ha="center")
    ax.text(16, 245, "L + α", fontsize=11); ax.text(75, 205, "L + β", fontsize=11)
    ax.text(50, 90, "α + β", fontsize=13, ha="center")
    ax.text(5, 120, "α", fontsize=14, color=C_BLUE, fontweight="bold")
    ax.text(97.2, 120, "β", fontsize=14, color="#b06000", fontweight="bold")
    ax.plot(xa, TE, "o", color=C_BLUE, ms=8); ax.plot(xb, TE, "o", color="#b06000", ms=8)
    ax.annotate("Sn 在 Pb 中的边缘溶解度\n最大 18.3 %（183 °C）", xy=(xa, TE), xytext=(20, 40), fontsize=10,
                arrowprops=dict(arrowstyle="->", color=C_BLUE), color=C_BLUE)
    ax.annotate("Pb 在 Sn 中最大 2.2 %", xy=(xb, TE), xytext=(68, 125), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="#b06000"), color="#b06000")
    ax.plot(xE, TE, "ko"); ax.text(xE, TE + 8, "E（共晶点）", ha="center", fontsize=10)
    ax.set_xlim(0, 100); ax.set_ylim(0, 350)
    ax.set_xlabel("Sn 质量分数 / %（左端纯 Pb，右端纯 Sn）"); ax.set_ylabel("T / °C")
    ax.set_title("边缘固溶度（border / terminal solubility）：以 Pb–Sn 为例", fontsize=12)
    ax.legend(loc="upper right", fontsize=9.5)
    clean(ax)
    save(fig, "B2_01_border_solubility_PbSn.png")


def b2_2():
    fig, ax = plt.subplots(figsize=(9.5, 6))
    TA, TB = 1500.0, 1000.0
    T, xl, xs = ideal_lens(TA, TB, 30 * TA, 30 * TB)
    ax.fill_betweenx(T, xs, xl, color=C_YELLOW, alpha=0.3)
    ax.plot(xl, T, color=C_RED, lw=2.5, label="液相线（liquidus）")
    ax.plot(xs, T, color=C_BLUE, lw=2.5, label="固相线（solidus）")
    ax.plot(0, TA, "ko"); ax.plot(1, TB, "ko")
    ax.text(0.02, TA + 15, "Tₘ(A)（较高）", fontsize=10); ax.text(0.84, TB - 45, "Tₘ(B)（较低）", fontsize=10)
    ax.text(0.72, 1400, "① 液相 L（熔体）\n     1 相", fontsize=12, ha="center")
    ax.text(0.52, 1195, "② L + α\n   2 相", fontsize=12, ha="center")
    ax.text(0.25, 1080, "③ 固溶体 α（固）\n     1 相", fontsize=12, ha="center")
    Tt = 1300
    i = np.argmin(abs(T - Tt))
    ax.plot([xs[i], xl[i]], [Tt, Tt], "k-", lw=1)
    ax.plot([xs[i], xl[i]], [Tt, Tt], "ko", ms=5)
    ax.text(xs[i] - 0.01, Tt - 28, "固相组成", ha="right", fontsize=9); ax.text(xl[i] + 0.01, Tt - 28, "液相组成", fontsize=9)
    ax.set_xlim(0, 1); ax.set_ylim(950, 1580)
    ax.set_xlabel("组成：B 的摩尔分数 x(B)（左 = 纯 A，右 = 纯 B）")
    ax.set_ylabel("温度 T")
    ax.set_yticks([])
    ax.set_title("A–B 完全互溶（匀晶）相图，B 熔点较低", fontsize=12)
    ax.legend(loc="upper right", fontsize=10)
    clean(ax)
    save(fig, "B2_02_complete_solid_solution_lens.png")


def b2_3():
    fig = plt.figure(figsize=(14, 9.6))
    gs = fig.add_gridspec(2, 2)
    ax = fig.add_subplot(gs[0, 0])
    TMo, TW = 2896.0, 3695.0
    T, xl, xs = ideal_lens(TW, TMo, 52300, 37500)  # x_B = x_Mo
    ax.fill_betweenx(T - 273, 1 - xl, 1 - xs, color=C_YELLOW, alpha=0.3)
    ax.plot(1 - xl, T - 273, color=C_RED, lw=2, label="液相线")
    ax.plot(1 - xs, T - 273, color=C_BLUE, lw=2, label="固相线")
    ax.text(0.3, 3300, "L", fontsize=14)
    ax.annotate("L + bcc（两相，很窄）", xy=(0.5, 3040), xytext=(0.55, 2780), fontsize=10.5, arrowprops=dict(arrowstyle="->"))
    ax.text(0.6, 2550, "bcc 固溶体 (Mo,W)\n（全组成范围单相）", fontsize=10.5, ha="center")
    ax.set_xlabel("W 的摩尔分数（左 = Mo，右 = W）"); ax.set_ylabel("T / °C")
    ax.set_title("(a) Mo–W 相图：完全互溶的“透镜”", fontsize=11.5)
    ax.text(0.02, 2560, "Mo 2623 °C", fontsize=9); ax.text(0.8, 3450, "W 3422 °C", fontsize=9)
    ax.set_ylim(2400, 3550); ax.legend(loc="upper left", fontsize=9.5); clean(ax)
    ax = fig.add_subplot(gs[0, 1]); setup_ax(ax, "(b) 原子统计（无序）分布在 bcc 格位上", fs=11.5)
    rng = np.random.default_rng(3)
    sc = Scene(ax, azim=-60, elev=18, scale=1.4)
    pts = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                pts.append((i, j, k))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                pts.append((i + 0.5, j + 0.5, k + 0.5))
    for i in range(2):
        for (a, b) in [(0, 1), (1, 2)]:
            pass
    for o in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]:
        sc.cube(o, 1, color="#bbb", lw=0.7)
    for p in pts:
        w = rng.random() < 0.5
        sc.ball(p, 0.17, C_GRAY if w else C_GREEN)
    sc.render()
    foot(ax, "灰 = W，绿 = Mo（50:50 示意）：每个格位被 Mo 或 W 随机占据\n无长程有序 → 平均看是“混合原子”的 bcc，空间群仍为 Im3̄m", fontsize=9.8)
    ax = fig.add_subplot(gs[1, 0])
    x = np.linspace(0, 1, 50)
    aMo, aW = 3.1470, 3.1652
    ax.plot(x, aMo + (aW - aMo) * x, color=C_PURPLE, lw=2.5)
    ax.plot([0, 1], [aMo, aW], "ko")
    xm = 0.5; am = aMo + (aW - aMo) * xm
    ax.plot([xm, xm, 0], [3.143, am, am], "k--", lw=1)
    ax.text(0.02, aMo - 0.0015, "a(Mo) = 3.1470 Å", fontsize=9.5, va="top")
    ax.text(0.98, aW + 0.0008, "a(W) = 3.1652 Å", fontsize=9.5, ha="right")
    ax.text(0.52, am - 0.004, "测得 a = 3.1561 Å\n→ x(W) = 0.50", fontsize=9.5)
    ax.set_xlabel("W 的摩尔分数 x"); ax.set_ylabel("晶格常数 a / Å")
    ax.set_title("(c) Vegard 定律：a(x) = (1 − x)·a(Mo) + x·a(W)", fontsize=11.5); clean(ax)
    ax.set_ylim(3.143, 3.168)
    ax = fig.add_subplot(gs[1, 1])
    lam = 1.5406
    hkls = [(1, 1, 0), (2, 0, 0), (2, 1, 1), (2, 2, 0), (3, 1, 0), (2, 2, 2), (3, 2, 1)]
    for xi, col, lab in [(0, C_GREEN, "Mo"), (0.5, C_PURPLE, "Mo₀.₅W₀.₅"), (1, C_GRAY, "W")]:
        a = aMo + (aW - aMo) * xi
        for h in hkls:
            d = a / np.sqrt(sum(c * c for c in h))
            tt = 2 * np.degrees(np.arcsin(lam / (2 * d)))
            ax.plot([tt, tt], [0, 1 - 0.07 * hkls.index(h)], color=col, lw=1.6, label=lab if h == hkls[0] else None)
    for h in hkls:
        d = aMo / np.sqrt(sum(c * c for c in h))
        tt = 2 * np.degrees(np.arcsin(lam / (2 * d)))
        ax.text(tt, 1.03 - 0.07 * hkls.index(h), "".join(map(str, h)), ha="center", fontsize=8.5)
    ax.set_xlabel("2θ / °（Cu Kα，λ = 1.5406 Å）"); ax.set_yticks([])
    ax.set_title("(d) 衍射峰随组成平移：高角度峰移得更多", fontsize=11.5)
    ax.text(60, 1.45, "110 峰：Mo 40.51° → W 40.26°（只差 0.25°）\n321 峰：Mo 132.7° → W 131.2°（差 ≈1.5°，更好测）", fontsize=9.5,
            va="top", bbox=dict(fc="white", ec="#999"))
    ax.legend(fontsize=9, loc="upper left"); clean(ax); ax.set_xlim(35, 140); ax.set_ylim(0, 1.5)
    plt.tight_layout()
    save(fig, "B2_03_MoW_alloy_vegard_XRD.png")


def b2_4():
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 100, 200)
    liq = 1300 + 6.838 * x - 0.01838 * x ** 2
    sol = 1300 + 3.99 * x + 0.0101 * x ** 2
    ax.fill_between(x, sol, liq, color=C_YELLOW, alpha=0.3)
    ax.plot(x, liq, color=C_RED, lw=2, label="液相线"); ax.plot(x, sol, color=C_BLUE, lw=2, label="固相线")
    ax.plot([32, 45], [1500, 1500], "k-", lw=2)
    ax.plot([32], [1500], "o", color=C_RED, ms=9); ax.plot([45], [1500], "o", color=C_BLUE, ms=9)
    ax.plot([40], [1500], "s", color="k", ms=9)
    ax.annotate("", xy=(32, 1462), xytext=(40, 1462), arrowprops=dict(arrowstyle="<->", color=C_RED, lw=1.5))
    ax.annotate("", xy=(40, 1462), xytext=(45, 1462), arrowprops=dict(arrowstyle="<->", color=C_BLUE, lw=1.5))
    ax.text(36, 1440, "8", color=C_RED, ha="center", fontsize=12); ax.text(42.5, 1440, "5", color=C_BLUE, ha="center", fontsize=12)
    ax.text(31, 1525, "液相 32 % A", ha="right", fontsize=10, color=C_RED)
    ax.text(46, 1525, "固相 45 % A", fontsize=10, color=C_BLUE)
    ax.text(40, 1555, "体系 40 % A", ha="center", fontsize=10)
    ax.text(58, 1380, "杠杆规则（支点 = 体系组成）：\n"
                      "液相分数 = (45 − 40)/(45 − 32) = 5/13 = 38.5 %\n"
                      "固相分数 = (40 − 32)/(45 − 32) = 8/13 = 61.5 %\n\n"
                      "“对边臂长”：离液相点越远，液相越少", fontsize=10.5,
            bbox=dict(fc="#fff6e0", ec=C_ORANGE))
    ax.set_xlim(0, 100); ax.set_ylim(1300, 1820)
    ax.set_xlabel("A 的含量 / %"); ax.set_ylabel("T / °C")
    ax.set_title("1500 °C 下的连结线（tie line）与杠杆规则", fontsize=12)
    ax.legend(loc="upper left"); clean(ax)
    save(fig, "B2_04_lever_rule.png")


def b2_5():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    ax = axs[0]
    TA, TB, TE, xE = 1000, 800, 550, 0.6
    x1 = np.linspace(0, xE, 80); l1 = TA - (TA - TE) * (x1 / xE) ** 1.3
    x2 = np.linspace(xE, 1, 80); l2 = TE + (TB - TE) * ((x2 - xE) / (1 - xE)) ** 1.0
    ax.plot(x1, l1, color=C_RED, lw=2.5); ax.plot(x2, l2, color=C_RED, lw=2.5)
    ax.plot([0, 1], [TE, TE], color=C_BLUE, lw=2.5)
    ax.plot([0, 0], [300, TA], color=C_BLUE, lw=2.5); ax.plot([1, 1], [300, TB], color=C_BLUE, lw=2.5)
    ax.plot(xE, TE, "ko", ms=7)
    ax.text(0.55, 920, "液相区 L\n（一相区）", fontsize=11, ha="center")
    ax.text(0.2, 700, "L + A(s)\n（两相区）", fontsize=10.5, ha="center")
    ax.text(0.82, 610, "L + B(s)\n（两相区）", fontsize=10.5, ha="center")
    ax.text(0.3, 420, "A(s) + 共晶固体\n（两相区）", fontsize=10.5, ha="center")
    ax.text(0.8, 420, "B(s) + 共晶固体\n（两相区）", fontsize=10.5, ha="center")
    ax.annotate("液相线", xy=(0.3, l1[40]), xytext=(0.35, 980), arrowprops=dict(arrowstyle="->", color=C_RED), color=C_RED)
    ax.annotate("液相线", xy=(0.8, TE + (TB - TE) * 0.5), xytext=(0.82, 760), arrowprops=dict(arrowstyle="->", color=C_RED), color=C_RED)
    ax.annotate("固相线（共晶线，T = T(E)）", xy=(0.15, TE), xytext=(0.03, 500), arrowprops=dict(arrowstyle="->", color=C_BLUE),
                color=C_BLUE)
    ax.annotate("E：共晶点\nL ⇌ A(s) + B(s)", xy=(xE, TE), xytext=(0.62, 470), arrowprops=dict(arrowstyle="->"), fontsize=10)
    ax.add_patch(Rectangle((xE - 0.015, 310), 0.03, TE - 315, fc=C_PURPLE, alpha=0.35))
    ax.text(xE, 330, "共晶组成：\n全部为共晶固体\n（A、B 细晶交替）", ha="center", fontsize=9, color=C_PURPLE,
            bbox=dict(fc="white", ec=C_PURPLE, lw=0.6))
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(300, 1050)
    ax.set_xlabel("x(B)"); ax.set_ylabel("T"); ax.set_yticks([])
    ax.set_title("(a) 简单共晶相图：六个术语全部适用", fontsize=12); clean(ax)
    ax = axs[1]
    T, xl, xs = ideal_lens(1500.0, 1000.0, 30 * 1500.0, 30 * 1000.0)
    ax.fill_betweenx(T, xs, xl, color=C_YELLOW, alpha=0.3)
    ax.plot(xl, T, color=C_RED, lw=2.5, label="液相线"); ax.plot(xs, T, color=C_BLUE, lw=2.5, label="固相线")
    ax.text(0.7, 1400, "液相区 L（一相区）", fontsize=11, ha="center")
    ax.text(0.5, 1240, "L + α\n（两相区）", fontsize=11, ha="center")
    ax.text(0.25, 1080, "固溶体 α\n（一相区）", fontsize=11, ha="center")
    ax.text(0.5, 900, "“共晶固体”：不适用（没有共晶点）", fontsize=11, ha="center", color=C_GRAY)
    ax.set_xlim(0, 1); ax.set_ylim(870, 1560); ax.set_yticks([])
    ax.set_xlabel("x(B)"); ax.set_ylabel("T")
    ax.set_title("(b) 完全互溶（匀晶）相图：无共晶", fontsize=12); ax.legend(loc="upper right"); clean(ax)
    save(fig, "B2_05_phase_diagram_terms.png")


def ion(ax, x, y, kind, label=None, r=None, alpha=1.0, lw=1.0, ec="k"):
    st = {"Na": (0.22, "#cbbdf0", "Na⁺"), "Cl": (0.36, "#bfe3c0", "Cl⁻"), "Ag": (0.25, "#d0d0d0", "Ag⁺"),
          "Ca": (0.25, "#ffd59e", "Ca²⁺"), "F": (0.3, "#bfe3c0", "F⁻"), "Y": (0.27, "#f4a6a6", "Y³⁺"),
          "CaNa": (0.24, "#f4a6a6", "Ca²⁺")}[kind]
    ax.add_patch(Circle((x, y), r or st[0], fc=st[1], ec=ec, lw=lw, alpha=alpha))
    ax.text(x, y, label if label is not None else st[2], ha="center", va="center", fontsize=7.5)


def vac(ax, x, y, s=0.3, color=C_RED):
    ax.add_patch(Rectangle((x - s, y - s), 2 * s, 2 * s, fc="white", ec=color, lw=1.8, ls="--"))


def b2_6():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.4))
    ax = axs[0]; setup_ax(ax, "(a) Schottky 缺陷：NaCl", fs=12)
    vacs = {(1, 2), (3, 1)}
    for i in range(5):
        for j in range(5):
            if (i, j) in vacs:
                vac(ax, i, j); continue
            ion(ax, i, j, "Na" if (i + j) % 2 == 0 else "Cl")
    ax.text(1, 2, "V$_{Na}'$", ha="center", va="center", fontsize=9, color=C_RED)
    ax.text(3, 1, "V$_{Cl}^{\\bullet}$", ha="center", va="center", fontsize=9, color=C_RED)
    ax.text(2, -0.95, "成对的阳、阴离子空位（离子移到表面）\n密度略降；保持电中性", ha="center", fontsize=10)
    ax.text(2, -1.75, "null → V$_{Na}'$ + V$_{Cl}^{\\bullet}$", ha="center", fontsize=12, color=C_DARK)
    ax.set_xlim(-0.6, 4.6); ax.set_ylim(-2.1, 4.6)
    ax = axs[1]; setup_ax(ax, "(b) Frenkel 缺陷：AgCl", fs=12)
    for i in range(5):
        for j in range(5):
            if (i, j) == (2, 2):
                vac(ax, i, j); continue
            ion(ax, i, j, "Ag" if (i + j) % 2 == 0 else "Cl")
    ion(ax, 2.5, 2.5, "Ag", r=0.2, ec=C_RED, lw=2)
    ax.annotate("", xy=(2.38, 2.38), xytext=(2.12, 2.12), arrowprops=dict(arrowstyle="->", color=C_RED, lw=1.8))
    ax.text(2, 1.62, "V$_{Ag}'$", ha="center", fontsize=9, color=C_RED)
    ax.text(2.95, 2.75, "Ag$_i^{\\bullet}$", fontsize=10, color=C_RED)
    ax.text(2, -0.95, "小的 Ag⁺ 离开格位进入间隙\n空位 + 间隙离子成对；密度不变", ha="center", fontsize=10)
    ax.text(2, -1.75, "Ag$_{Ag}^{\\times}$ → Ag$_i^{\\bullet}$ + V$_{Ag}'$", ha="center", fontsize=12, color=C_DARK)
    ax.set_xlim(-0.6, 4.6); ax.set_ylim(-2.1, 4.6)
    ax = axs[2]; ax.axis("off"); ax.set_title("Kröger–Vink 记号", fontsize=12)
    ax.text(0.45, 0.93, "$\\mathrm{M}_\\mathrm{S}^\\mathrm{C}$", fontsize=20, transform=ax.transAxes, ha="center")
    rows = [("M", None, "什么：原子/离子符号，空位写 V"),
            ("S", None, "在哪：所占格位的原主人；间隙写 i"),
            ("C", None, "有效电荷 = 实际电荷 − 该格位原电荷"),
            ("", None, "  •  = +1　　′ = −1　　× = 0"),
            ("例", "$V_{Na}'$", "Na⁺ 位空了 → 少了 +1 → 有效 −1"),
            ("", "$V_{Cl}^{\\bullet}$", "Cl⁻ 位空了 → 少了 −1 → 有效 +1"),
            ("", "$Ag_i^{\\bullet}$", "Ag⁺ 进入间隙（原电荷 0）→ +1"),
            ("", "$Ag_{Ag}^{\\times}$", "Ag⁺ 在自己格位上 → 0"),
            ("规律", None, "Schottky：CN 高、正负离子大小相近"),
            ("", None, "　NaCl、KCl、CsCl"),
            ("", None, "Frenkel：阳离子小/易极化、CN 低"),
            ("", None, "　AgCl、AgBr、ZnS"),
            ("", None, "反 Frenkel：CaF₂（F⁻ 进间隙）")]
    for k, (a, m, b) in enumerate(rows):
        y = 0.8 - k * 0.066
        ax.text(0.0, y, a, fontsize=10.5, fontweight="bold", transform=ax.transAxes)
        if m:
            ax.text(0.12, y, m, fontsize=12, transform=ax.transAxes, color=C_RED)
            ax.text(0.3, y, b, fontsize=10, transform=ax.transAxes)
        else:
            ax.text(0.12, y, b, fontsize=10, transform=ax.transAxes)
    save(fig, "B2_06_point_defects_schottky_frenkel.png")


def b2_7():
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.4))
    ax = axs[0]; setup_ax(ax, "(a) NaCl 掺 CaCl₂：Ca²⁺ 占 Na⁺ 位 + 一个 Na⁺ 空位", fs=11.5)
    for i in range(5):
        for j in range(5):
            if (i, j) == (2, 2):
                ion(ax, i, j, "CaNa", ec=C_RED, lw=2); continue
            if (i, j) == (3, 3):
                vac(ax, i, j); continue
            ion(ax, i, j, "Na" if (i + j) % 2 == 0 else "Cl")
    ax.text(2.0, 1.58, "Ca$_{Na}^{\\bullet}$", ha="center", fontsize=10, color=C_RED)
    ax.text(3, 3, "V$_{Na}'$", ha="center", va="center", fontsize=9, color=C_RED)
    ax.text(2, -0.9, "CaCl₂ →(NaCl) Ca$_{Na}^{\\bullet}$ + V$_{Na}'$ + 2Cl$_{Cl}^{\\times}$", ha="center", fontsize=12)
    ax.text(2, -1.6, "化学式：Na₁₋₂ₓCaₓ□ₓCl（□ = 空位）", ha="center", fontsize=12, color=C_BLUE)
    ax.text(2, -2.25, "1 个 Ca²⁺ 顶替 2 个 Na⁺：一个位被 Ca 占，另一个空出", ha="center", fontsize=9.8)
    ax.set_xlim(-0.6, 4.6); ax.set_ylim(-2.6, 4.6)
    ax = axs[1]; setup_ax(ax, "(b) CaF₂ 掺 YF₃：Y³⁺ 占 Ca²⁺ 位 + 一个间隙 F⁻", fs=11.5)
    for i in range(6):
        for j in range(6):
            ion(ax, i, j, "F")
    for i in range(5):
        for j in range(5):
            cx, cy = i + 0.5, j + 0.5
            if (i + j) % 2 == 0:
                if (i, j) == (2, 2):
                    ion(ax, cx, cy, "Y", ec=C_RED, lw=2)
                else:
                    ion(ax, cx, cy, "Ca")
            else:
                ax.add_patch(Circle((cx, cy), 0.06, fc="#bbb", ec="none"))
    ion(ax, 3.5, 2.5, "F", label="F⁻", ec=C_RED, lw=2, r=0.27)
    ax.text(2.5, 1.98, "Y$_{Ca}^{\\bullet}$", ha="center", fontsize=10, color=C_RED)
    ax.text(3.5, 2.03, "F$_i'$", ha="center", fontsize=10, color=C_RED)
    ax.text(2.5, -0.9, "YF₃ →(CaF₂) Y$_{Ca}^{\\bullet}$ + F$_i'$ + 2F$_F^{\\times}$", ha="center", fontsize=12)
    ax.text(2.5, -1.6, "化学式：Ca₁₋ₓYₓF₂₊ₓ（阴离子过量萤石）", ha="center", fontsize=12, color=C_BLUE)
    ax.text(2.5, -2.25, "萤石中一半“F₈ 立方体”是空的（灰点）→ 正好容纳间隙 F⁻", ha="center", fontsize=9.8)
    ax.set_xlim(-0.6, 5.6); ax.set_ylim(-2.6, 5.6)
    save(fig, "B2_07_doping_NaCl_Ca_CaF2_Y.png")


if __name__ == "__main__":
    for f in [b2_1, b2_2, b2_3, b2_4, b2_5, b2_6, b2_7]:
        f()
