# Part A2 配图：堆积、空隙、配位多面体、Madelung、结构关系、MO、Lewis、氢键、碳/硅酸盐/锡
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle
from common import *

CORN = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]
FACE = [(0.5,0.5,0),(0.5,0.5,1),(0.5,0,0.5),(0.5,1,0.5),(0,0.5,0.5),(1,0.5,0.5)]
EDGE = [p for p in itertools.product([0,0.5,1], repeat=3) if sorted(p).count(0.5) == 1]
TD = list(itertools.product([0.25,0.75], repeat=3))


# ---------------- A2.1 ccp 晶胞 ----------------
def a2_1():
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.6))
    # (a) 球棍晶胞
    ax = axs[0]; setup_ax(ax, "(a) ccp = fcc 晶胞：8 个顶点 + 6 个面心")
    sc = Scene(ax, azim=-62, elev=18, scale=3)
    sc.cube()
    for p in CORN: sc.ball(p, 0.12, C_BLUE)
    for p in FACE: sc.ball(p, 0.12, C_BLUE)
    sc.render()
    foot(ax, "每晶胞原子数 = 8×1/8 + 6×1/2 = 4", ha="center", fontsize=10.5)
    # (b) 按 (111) 层着色：ABC 沿体对角线
    ax = axs[1]; setup_ax(ax, "(b) 沿体对角线 [111] 看：A-B-C 三层")
    sc = Scene(ax, azim=-62, elev=18, scale=3)
    sc.cube(color="#999")
    col = {0: C_RED, 1: C_GREEN, 2: C_ORANGE, 3: C_RED}
    lay = {0: "A", 1: "B", 2: "C", 3: "A"}
    for p in CORN + FACE:
        s = int(round(sum(p)))
        sc.ball(p, 0.12, col[s], label=lay[s], fs=7)
    sc.poly([(1,0,0),(0,1,0),(0,0,1)], C_GREEN, alpha=0.18)
    sc.poly([(1,1,0),(1,0,1),(0,1,1)], C_ORANGE, alpha=0.18)
    sc.line((0,0,0), (1,1,1), color=C_DARK, lw=1.4, ls="--", front=True)
    sc.render()
    foot(ax, "(111) 面就是最密排层；顺序 A→B→C→A", ha="center", fontsize=10.5)
    # (c) 面对角线上球相切
    ax = axs[2]; setup_ax(ax, "(c) 一个立方面：球沿面对角线相切")
    a = 2.0; r = a * np.sqrt(2) / 4
    ax.add_patch(Rectangle((0, 0), a, a, fc="none", ec="k", lw=1.2, zorder=5))
    for (x, y) in [(0,0),(a,0),(a,a),(0,a),(a/2,a/2)]:
        ax.add_patch(Circle((x, y), r, fc=blend(C_BLUE, "white", 0.35), ec=C_BLUE, lw=1.2, alpha=0.9))
    ax.plot([0, a], [0, a], color=C_RED, lw=1.6, zorder=6)
    ax.text(a * 0.62, a * 0.42, "4r = √2·a", color=C_RED, fontsize=11, rotation=45, zorder=7)
    ax.text(a / 2, -0.25, "a", ha="center", fontsize=12, zorder=7)
    ax.text(a / 2, -0.85, "a = 2√2·r，空间利用率 74%", ha="center", fontsize=10.5)
    ax.set_xlim(-0.9, a + 0.9); ax.set_ylim(-1.1, a + 0.9)
    save(fig, "A2_01_ccp_unit_cell.png")


# ---------------- A2.2 堆积序列 ----------------
def tri_lattice(n=4):
    pts = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            pts.append((i + 0.5 * j, j * np.sqrt(3) / 2))
    return pts


def a2_2():
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.6), gridspec_kw=dict(width_ratios=[1.25, 1, 1]))
    ax = axs[0]; setup_ax(ax, "(a) 俯视：A 层上方有两套空穴 B、C")
    R = 2.2
    for (x, y) in tri_lattice(4):
        if x * x + y * y < R * R:
            ax.add_patch(Circle((x, y), 0.5, fc=blend(C_RED, "white", 0.45), ec=C_RED, lw=1))
            ax.text(x, y, "A", ha="center", va="center", fontsize=8, color=C_RED)
    for (x, y) in tri_lattice(4):
        bx, by = x + 0.5, y + np.sqrt(3) / 6
        cx, cy = x + 1.0, y + np.sqrt(3) / 3
        if bx * bx + by * by < (R - 0.4) ** 2:
            ax.add_patch(Circle((bx, by), 0.13, fc=C_GREEN, ec="k", lw=0.5, zorder=5))
        if cx * cx + cy * cy < (R - 0.4) ** 2:
            ax.add_patch(Polygon([(cx - 0.13, cy - 0.1), (cx + 0.13, cy - 0.1), (cx, cy + 0.14)], fc=C_ORANGE,
                                 ec="k", lw=0.5, zorder=5))
    ax.add_patch(Circle((-2.0, -2.75), 0.13, fc=C_GREEN, ec="k", lw=0.5))
    ax.text(-1.8, -2.75, "B 位（下三角空穴）", va="center", fontsize=9.5)
    ax.add_patch(Polygon([(0.37, -2.85), (0.63, -2.85), (0.5, -2.61)], fc=C_ORANGE, ec="k", lw=0.5))
    ax.text(0.7, -2.75, "C 位（上三角空穴）", va="center", fontsize=9.5)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-3.1, 2.6)

    def column(ax, seq, title):
        setup_ax(ax, title)
        off = {"A": 0.0, "B": 1 / 3, "C": 2 / 3}
        colr = {"A": C_RED, "B": C_GREEN, "C": C_ORANGE}
        h = 0.82
        for L, s in enumerate(seq):
            y = L * h
            for i in range(-1, 4):
                x = i + off[s]
                if -0.6 < x < 3.4:
                    ax.add_patch(Circle((x, y), 0.5, fc=blend(colr[s], "white", 0.4), ec=colr[s], lw=1))
            ax.text(-1.0, y, s, ha="center", va="center", fontsize=13, color=colr[s], fontweight="bold")
        ax.set_xlim(-1.4, 3.6); ax.set_ylim(-0.7, len(seq) * h + 0.1)

    column(axs[1], "ABABAB", "(b) hcp：…ABAB…（两层重复）")
    column(axs[2], "ABCABC", "(c) ccp：…ABCABC…（三层重复）")
    save(fig, "A2_02_stacking_sequences.png")


# ---------------- A2.3 hcp/ccp/bcc 晶胞 ----------------
def hcp_points(c=1.633):
    pts = []
    for z in (0, c):
        pts.append((0, 0, z))
        for k in range(6):
            t = np.radians(60 * k)
            pts.append((np.cos(t), np.sin(t), z))
    for ang in (30, 150, 270):
        t = np.radians(ang)
        pts.append((np.cos(t) / np.sqrt(3), np.sin(t) / np.sqrt(3), c / 2))
    return pts


def a2_3():
    fig, axs = plt.subplots(1, 3, figsize=(13, 5))
    # hcp
    ax = axs[0]; setup_ax(ax, "hcp（六方最密堆积）")
    sc = Scene(ax, azim=-70, elev=14, scale=1.6)
    c = 1.633
    hexv = [(np.cos(np.radians(60 * k)), np.sin(np.radians(60 * k))) for k in range(6)]
    for z in (0, c):
        for k in range(6):
            sc.line((*hexv[k], z), (*hexv[(k + 1) % 6], z), color="#888")
    for k in range(6):
        sc.line((*hexv[k], 0), (*hexv[k], c), color="#888")
    for p in hcp_points(c):
        layer_mid = abs(p[2] - c / 2) < 1e-6
        sc.ball(p, 0.17, C_GREEN if layer_mid else C_RED, label="B" if layer_mid else "A", fs=7)
    # 原胞（菱形底）
    v = [(0,0,0),(1,0,0),(0.5,np.sqrt(3)/2,0),(-0.5,np.sqrt(3)/2,0)]
    sc.line((0,0,0),(1,0,0),color=C_BLUE,lw=2); sc.line((0,0,0),(0.5,np.sqrt(3)/2,0),color=C_BLUE,lw=2)
    sc.render()
    foot(ax, "ABAB…；CN = 12\n原胞含 2 个原子；理想 c/a = 1.633\n空间利用率 74%", ha="center", fontsize=10)
    # ccp
    ax = axs[1]; setup_ax(ax, "ccp（立方最密堆积）= fcc")
    sc = Scene(ax, azim=-62, elev=18, scale=2.2, offset=(0, -0.2))
    sc.cube()
    for p in CORN + FACE:
        sc.ball(p, 0.13, C_BLUE)
    sc.render()
    foot(ax, "ABCABC…；CN = 12\n晶胞含 4 个原子；a = 2√2 r\n空间利用率 74%", ha="center", fontsize=10)
    # bcc
    ax = axs[2]; setup_ax(ax, "bcc（体心立方，非最密）")
    sc = Scene(ax, azim=-62, elev=18, scale=2.2, offset=(0, -0.2))
    sc.cube()
    for p in CORN:
        sc.ball(p, 0.13, C_PURPLE)
    sc.ball((0.5, 0.5, 0.5), 0.13, C_ORANGE)
    sc.line((0,0,0),(1,1,1),color=C_RED,lw=1.6,ls="--")
    sc.render()
    foot(ax, "CN = 8（+6 个次近邻，远 15%）\n晶胞含 2 个原子；√3 a = 4r\n空间利用率 68%", ha="center", fontsize=10)
    save(fig, "A2_03_hcp_ccp_bcc_cells.png")


# ---------------- A2.4 空隙 ----------------
def a2_4():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 5.2))
    ax = axs[0]; setup_ax(ax, "(a) 八面体空隙：体心 1 + 棱心 12×1/4 = 4")
    sc = Scene(ax, azim=-62, elev=18, scale=2.6)
    sc.cube(color="#999")
    for p in CORN + FACE:
        sc.ball(p, 0.10, C_BLUE)
    for p in [(0.5,0.5,0.5)] + EDGE:
        sc.ball(p, 0.07, C_RED)
    octa = [np.array(p) for p in FACE]
    for f in hull_faces(octa):
        sc.poly(f, C_RED, alpha=0.13, ec=C_RED, lw=0.6)
    sc.render()
    foot(ax, "蓝 = 堆积原子(4)  红 = 八面体空隙(4)", ha="center", fontsize=10)
    ax = axs[1]; setup_ax(ax, "(b) 四面体空隙：(¼,¼,¼) 型 8 个，全在晶胞内")
    sc = Scene(ax, azim=-62, elev=18, scale=2.6)
    sc.cube(color="#999")
    for p in CORN + FACE:
        sc.ball(p, 0.10, C_BLUE)
    for p in TD:
        sc.ball(p, 0.06, C_GREEN)
    tet = [np.array(p) for p in [(0,0,0),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5)]]
    for f in hull_faces(tet):
        sc.poly(f, C_GREEN, alpha=0.2, ec=C_GREEN, lw=0.7)
    sc.render()
    foot(ax, "绿 = 四面体空隙(8)；N 个原子 → N 个 O_h + 2N 个 T_d", ha="center", fontsize=10)
    save(fig, "A2_04_voids_octa_tetra.png")


# ---------------- A2.5 配位多面体 ----------------
def cubo(eclipsed):
    pts = []
    for k in range(6):
        t = np.radians(60 * k)
        pts.append((np.cos(t), np.sin(t), 0))
    h = np.sqrt(2 / 3)
    for ang in (30, 150, 270):
        t = np.radians(ang)
        pts.append((np.cos(t) / np.sqrt(3), np.sin(t) / np.sqrt(3), h))
    for ang in ((30, 150, 270) if eclipsed else (90, 210, 330)):
        t = np.radians(ang)
        pts.append((np.cos(t) / np.sqrt(3), np.sin(t) / np.sqrt(3), -h))
    return np.array(pts)


def a2_5():
    fig, axs = plt.subplots(1, 3, figsize=(13, 5))
    for ax, ecl, title, col, txt in [
        (axs[0], False, "ccp：立方八面体（cuboctahedron）", C_BLUE,
         "上下两组三角形错开 60°（A-B-C）\n8 个三角面 + 6 个正方形面"),
        (axs[1], True, "hcp：反立方八面体（anticuboctahedron）", C_RED,
         "上下两组三角形重叠（A-B-A）\n= 立方八面体的上半部旋转 60°")]:
        setup_ax(ax, title)
        sc = Scene(ax, azim=-75, elev=12, scale=1.5)
        P = cubo(ecl)
        for f in hull_faces(P):
            sc.poly(f, C_ORANGE if len(f) == 3 else col, alpha=0.22, ec="#333", lw=0.8)
        for i, p in enumerate(P):
            lay = "mid" if abs(p[2]) < 1e-6 else ("up" if p[2] > 0 else "dn")
            sc.ball(p, 0.11, {"mid": C_GRAY, "up": C_GREEN, "dn": C_PURPLE}[lay])
        sc.ball((0, 0, 0), 0.16, C_DARK)
        sc.render()
        foot(ax, txt, ha="center", fontsize=10)
    ax = axs[2]; setup_ax(ax, "bcc：立方体（CN 8）+ 八面体（次近邻 6）")
    sc = Scene(ax, azim=-62, elev=18, scale=1.4)
    s = 1.0
    cube_pts = [np.array(p) * 2 - 1 for p in CORN]
    for f in hull_faces(cube_pts):
        sc.poly(f, C_PURPLE, alpha=0.18, ec="#333", lw=0.8)
    for p in cube_pts:
        sc.ball(p, 0.13, C_PURPLE)
    for p in [(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2)]:
        sc.ball(p, 0.11, blend(C_ORANGE, "white", 0.3), alpha=0.85)
        sc.line((0,0,0), p, color=C_ORANGE, lw=1, ls=":")
    sc.ball((0, 0, 0), 0.16, C_DARK)
    sc.render()
    foot(ax, "8 个最近邻在立方体顶点（d = √3a/2）\n6 个次近邻在 d = a，仅远 15% → 常记为 CN 8+6", ha="center",
            fontsize=10)
    save(fig, "A2_05_coordination_polyhedra.png")


# ---------------- A2.6 堆积密度 ----------------
def a2_6():
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    names = ["简单立方 sc\n（参考）", "bcc", "hcp", "ccp (fcc)"]
    vals = [np.pi / 6, np.pi * np.sqrt(3) / 8, np.pi / (3 * np.sqrt(2)), np.pi / (3 * np.sqrt(2))]
    cols = [C_GRAY, C_PURPLE, C_RED, C_BLUE]
    b = ax.bar(names, [v * 100 for v in vals], color=cols, width=0.6)
    for bi, v in zip(b, vals):
        ax.text(bi.get_x() + bi.get_width() / 2, v * 100 + 1.2, f"{v*100:.1f}%", ha="center", fontsize=11)
    ax.set_ylabel("空间利用率 / %")
    ax.set_ylim(0, 90)
    ax.text(1, 20, "2·(4/3)πr³ / a³\na = 4r/√3\n= π√3/8", ha="center", color="white", fontsize=9.5)
    ax.text(2.5, 30, "4·(4/3)πr³ / a³，a = 2√2 r\n= π/(3√2) = 0.7405\n（hcp 算出来同值）", ha="center", color="black", fontsize=9.5,
            bbox=dict(fc="white", ec="#999"))
    ax.annotate("", xy=(3.35, 80), xytext=(0.7, 80), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(2.0, 83, "密度增大：bcc < hcp = ccp", ha="center", fontsize=11)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "A2_06_packing_density.png")


# ---------------- A2.7 Madelung ----------------
def madelung_shells(nmax=8):
    d = {}
    rng = range(-nmax, nmax + 1)
    for i in rng:
        for j in rng:
            for k in rng:
                if i == j == k == 0:
                    continue
                r2 = i * i + j * j + k * k
                if r2 > nmax * nmax:
                    continue
                sgn = 1 if (i + j + k) % 2 else -1  # 异号 → 吸引 → 正贡献
                d.setdefault(r2, [0, sgn])
                d[r2][0] += 1
    return sorted(d.items())


def evjen(n):
    s = 0.0
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            for k in range(-n, n + 1):
                if i == j == k == 0:
                    continue
                w = 1.0
                for c in (i, j, k):
                    if abs(c) == n:
                        w *= 0.5
                sgn = 1 if (i + j + k) % 2 else -1
                s += w * sgn / np.sqrt(i * i + j * j + k * k)
    return s


def a2_7():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5), gridspec_kw=dict(width_ratios=[0.9, 0.9, 1.2]))
    ax = axs[0]; setup_ax(ax, "(a) 以中心 Na⁺ 逐壳层计数（(100) 截面）", fs=11)
    shell_col = {1: C_GREEN, 2: C_PURPLE, 4: C_ORANGE, 5: C_TEAL}
    for i in range(-2, 3):
        for j in range(-2, 3):
            na = (i + j) % 2 == 0
            r2 = i * i + j * j
            ec = shell_col.get(r2, "#999")
            lw = 2.6 if r2 in shell_col else 0.8
            if na:
                ax.add_patch(Circle((i, j), 0.22, fc="#cbbdf0", ec=ec, lw=lw))
                ax.text(i, j, "Na⁺", ha="center", va="center", fontsize=7)
            else:
                ax.add_patch(Circle((i, j), 0.34, fc="#bfe3c0", ec=ec, lw=lw))
                ax.text(i, j, "Cl⁻", ha="center", va="center", fontsize=7)
    ax.add_patch(Circle((0, 0), 0.26, fc=C_RED, ec="k"))
    ax.text(0, 0, "Na⁺", ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    foot(ax, "边框颜色 = 壳层：绿 1（r）、紫 2（√2 r）、橙 4（2r）、青 5（√5 r）\n第 3 壳层（√3 r）在上下相邻层，截面上看不到", fontsize=9)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
    ax = axs[1]; ax.axis("off"); ax.set_title("(b) 每个壳层：个数 × 符号 / 距离", fontsize=11)
    rows = [("壳层", "离子", "个数", "距离", "贡献"), ("1", "Cl⁻", "6", "r", "+6/1"),
            ("2", "Na⁺", "12", "√2 r", "−12/√2"), ("3", "Cl⁻", "8", "√3 r", "+8/√3"),
            ("4", "Na⁺", "6", "2 r", "−6/2"), ("5", "Cl⁻", "24", "√5 r", "+24/√5"), ("…", "", "", "", "")]
    xs = [0.08, 0.27, 0.46, 0.65, 0.87]
    for k, row in enumerate(rows):
        for m, cell in enumerate(row):
            ax.text(xs[m], 0.9 - k * 0.085, cell, fontsize=10.5, ha="center", transform=ax.transAxes,
                    fontweight="bold" if k == 0 else None)
    ax.text(0.5, 0.18, "E = −(N_A z²e²/4πε₀r₀)·A·(1 − 1/n)\nA = 6 − 12/√2 + 8/√3 − 6/2 + 24/√5 − …\n  = 1.7476（NaCl 型 Madelung 常数）",
            ha="center", va="center", fontsize=10, transform=ax.transAxes, bbox=dict(fc="#fff6e0", ec=C_ORANGE))
    ax = axs[2]
    sh = madelung_shells(9)
    s_ = 0; xs = []; ys = []
    for n, (r2, (cnt, sgn)) in enumerate(sh[:22]):
        s_ += sgn * cnt / np.sqrt(r2)
        xs.append(n + 1); ys.append(s_)
    ax.plot(xs, ys, "o-", color=C_GRAY, label="按球壳直接逐层加和（振荡不收敛）")
    ev = [evjen(n) for n in range(1, 9)]
    ax.plot(range(1, 9), ev, "s-", color=C_RED, label="Evjen 电中性立方块（面/棱/角离子计 ½/¼/⅛）")
    ax.axhline(1.7476, color=C_BLUE, ls="--")
    ax.text(21.5, 2.3, "A = 1.7476", color=C_BLUE, ha="right", fontsize=11)
    ax.set_xlabel("加入的壳层数 / 立方块半边长 n")
    ax.set_ylabel("Madelung 常数部分和")
    ax.set_ylim(-8, 14)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_title("(c) 必须按电中性单元加和才收敛", fontsize=11)
    for s2 in ("top", "right"):
        ax.spines[s2].set_visible(False)
    save(fig, "A2_07_madelung_shells.png")


# ---------------- A2.8 fcc 派生结构 ----------------
def a2_8():
    fig, axs = plt.subplots(2, 4, figsize=(15, 8.2))
    S = 2.2

    def cell(ax, title, big, bigc, small=(), smallc=None, rb=0.12, rs=0.09, bonds=False, txt=None):
        setup_ax(ax, title, fs=11)
        sc = Scene(ax, azim=-62, elev=18, scale=S)
        sc.cube(color="#999")
        for p in big:
            sc.ball(p, rb, bigc)
        for p in small:
            sc.ball(p, rs, smallc)
        if bonds:
            for p in small:
                for q in big:
                    if np.linalg.norm(np.subtract(p, q)) < 0.45:
                        sc.line(p, q, color="#444", lw=1.2)
        sc.render()
        if txt:
            foot(ax, txt, ha="center", fontsize=9.3)

    fccp = CORN + FACE
    cell(axs[0, 0], "fcc（Cl⁻ 骨架）", fccp, C_GREEN, txt="4 个 O_h 空隙全空")
    cell(axs[0, 1], "a) NaCl：Na⁺ 填满全部 O_h 空隙", fccp, C_GREEN, [(0.5,0.5,0.5)] + EDGE, C_PURPLE, rb=0.13,
         rs=0.08, txt="两套 fcc 相互穿插（错开 ½a）\nCN 6:6")
    cell(axs[0, 2], "fcc（O²⁻ 骨架）", fccp, C_RED, txt="8 个 T_d 空隙全空")
    cell(axs[0, 3], "b) Li₂O（反萤石）：Li⁺ 填满全部 T_d", fccp, C_RED, TD, C_ORANGE, rb=0.13, rs=0.07, bonds=True,
         txt="O:Li = 4:8 = 1:2；CN(Li)=4, CN(O)=8\n（CaF₂ 萤石：阴阳离子位置互换）")
    zn = [(0.25,0.25,0.25),(0.75,0.75,0.25),(0.75,0.25,0.75),(0.25,0.75,0.75)]
    cell(axs[1, 0], "fcc（S²⁻ 骨架）", fccp, C_YELLOW, txt="8 个 T_d 空隙")
    cell(axs[1, 1], "c) ZnS（闪锌矿）：Zn²⁺ 填一半 T_d", fccp, C_YELLOW, zn, C_GRAY, rb=0.13, rs=0.09, bonds=True,
         txt="隔一个填一个（四面体分布）\nCN 4:4，= 两种原子的金刚石结构")
    # W / CsCl
    ax = axs[1, 2]; setup_ax(ax, "W 型（bcc）：顶点和体心同种原子", fs=11)
    sc = Scene(ax, azim=-62, elev=18, scale=S); sc.cube(color="#999")
    for p in CORN: sc.ball(p, 0.13, C_BLUE)
    sc.ball((0.5,0.5,0.5), 0.13, C_BLUE); sc.render()
    foot(ax, "体心立方 I 格子，2 原子/晶胞", ha="center", fontsize=9.3)
    ax = axs[1, 3]; setup_ax(ax, "d) CsCl 型：体心换成另一种离子", fs=11)
    sc = Scene(ax, azim=-62, elev=18, scale=S); sc.cube(color="#999")
    for p in CORN: sc.ball(p, 0.12, C_GREEN)
    sc.ball((0.5,0.5,0.5), 0.15, C_PURPLE)
    for p in CORN: sc.line(p, (0.5,0.5,0.5), color="#444", lw=1)
    sc.render()
    foot(ax, "Cl⁻ 顶点、Cs⁺ 体心 → 简单立方 P 格子\n（不是 bcc！）CN 8:8，bcc 的有序变体", ha="center",
            fontsize=9.3)
    plt.subplots_adjust(wspace=0.05, hspace=0.25)
    save(fig, "A2_08_fcc_derived_structures.png")


# ---------------- A2.9 MO：dxy 与 py ----------------
def lobe(ax, c, ang, L, W, sign, col_p=C_BLUE, col_m=C_RED):
    t = np.radians(ang)
    cx, cy = c[0] + 0.5 * L * np.cos(t), c[1] + 0.5 * L * np.sin(t)
    fc = blend(col_p, "white", 0.25) if sign > 0 else blend(col_m, "white", 0.35)
    ax.add_patch(Ellipse((cx, cy), L, W, angle=ang, fc=fc, ec="k", lw=0.8, alpha=0.85))
    ax.text(cx, cy, "+" if sign > 0 else "−", ha="center", va="center", fontsize=12, fontweight="bold")


def dxy(ax, c, s=1, L=1.3, W=0.62):
    for ang, sg in [(45, 1), (135, -1), (225, 1), (315, -1)]:
        lobe(ax, c, ang, L, W, sg * s)
    ax.add_patch(Circle(c, 0.07, fc="k"))


def p_orb(ax, c, ang, s=1, L=1.1, W=0.55):
    lobe(ax, c, ang, L, W, s)
    lobe(ax, c, ang + 180, L, W, -s)
    ax.add_patch(Circle(c, 0.06, fc="k"))


def a2_9():
    fig = plt.figure(figsize=(14, 4.8))
    gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.05])
    titles = ["(a) 同相组合：π 成键", "(b) 反相组合：π* 反键", "(c) 对称性不匹配：净重叠 = 0"]
    for k in range(3):
        ax = fig.add_subplot(gs[k]); setup_ax(ax, titles[k], fs=11)
        ax.axhline(0, color="#bbb", lw=0.8, zorder=0); ax.axvline(0, color="#bbb", lw=0.8, zorder=0)
        dxy(ax, (0, 0))
        if k == 0:
            p_orb(ax, (2.0, 0), 90, s=1)
        elif k == 1:
            p_orb(ax, (2.0, 0), 90, s=-1)
        else:
            p_orb(ax, (2.0, 0), 0, s=1)
        ax.text(0, -1.55, "M: d$_{xy}$", ha="center", fontsize=11)
        ax.text(2.0, -1.55, "L: p$_y$" if k < 2 else "L: p$_x$ / s", ha="center", fontsize=11)
        ax.text(2.75, 0.12, "x", fontsize=10, color="#888"); ax.text(0.08, 1.45, "y", fontsize=10, color="#888")
        note = ["+ 叠 +、− 叠 −：重叠积分 S > 0\n电子密度在核间增加 → 能量降低",
                "+ 叠 −：S < 0，核间出现节面\n能量升高",
                "上半 (+ 叠 +) 与下半 (+ 叠 −) 抵消\nS = 0 → 不成键（非键）"][k]
        ax.text(1.0, -2.25, note, ha="center", fontsize=9.5)
        ax.set_xlim(-1.3, 3.2); ax.set_ylim(-2.8, 1.7)
    ax = fig.add_subplot(gs[3]); ax.axis("off"); ax.set_title("(d) 能级图（L 电负性更大，p 能级更低）", fontsize=11)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.plot([0.5, 2.3], [6.5, 6.5], color=C_BLUE, lw=3); ax.text(1.4, 6.9, "M d$_{xy}$", ha="center")
    ax.plot([7.7, 9.5], [3.6, 3.6], color=C_GREEN, lw=3); ax.text(8.6, 4.0, "L p$_y$", ha="center")
    ax.plot([4.1, 5.9], [8.3, 8.3], color=C_RED, lw=3); ax.text(5.0, 8.75, "π*（主要 M 成分）", ha="center")
    ax.plot([4.1, 5.9], [2.2, 2.2], color=C_PURPLE, lw=3); ax.text(5.0, 1.45, "π（主要 L 成分）", ha="center")
    for (a, b) in [((2.3, 6.5), (4.1, 8.3)), ((2.3, 6.5), (4.1, 2.2)), ((7.7, 3.6), (5.9, 8.3)), ((7.7, 3.6), (5.9, 2.2))]:
        ax.plot([a[0], b[0]], [a[1], b[1]], ls="--", color="#777", lw=1)
    ax.plot([2.3, 4.1], [6.5, 6.5], color=C_BLUE, lw=0.8, ls=":")
    ax.plot([5.9, 7.7], [3.6, 3.6], color=C_GREEN, lw=0.8, ls=":")
    ax.annotate("", xy=(3.7, 8.3), xytext=(3.7, 6.5), arrowprops=dict(arrowstyle="<->", color=C_RED))
    ax.text(2.6, 7.4, "ΔE*", color=C_RED)
    ax.annotate("", xy=(6.3, 3.6), xytext=(6.3, 2.2), arrowprops=dict(arrowstyle="<->", color=C_PURPLE))
    ax.text(6.5, 2.8, "ΔE", color=C_PURPLE)
    ax.text(5, 0.3, "反键升高 ΔE* > 成键降低 ΔE", ha="center", fontsize=9.5)
    save(fig, "A2_09_MO_dxy_py.png")


# ---------------- A2.10 Lewis 结构 ----------------
def atom(ax, x, y, s, fs=20, color="black"):
    ax.text(x, y, s, ha="center", va="center", fontsize=fs, color=color, zorder=5,
            bbox=dict(fc="white", ec="none", pad=0.05))


def bond(ax, p, q, order=1, gap=0.09, shrink=0.28, color="black"):
    p, q = np.array(p, float), np.array(q, float)
    d = q - p; L = np.linalg.norm(d); u = d / L; n = np.array([-u[1], u[0]])
    a, b = p + u * shrink, q - u * shrink
    offs = {1: [0], 2: [-gap / 2, gap / 2], 3: [-gap, 0, gap]}[order]
    for o in offs:
        ax.plot([a[0] + n[0] * o, b[0] + n[0] * o], [a[1] + n[1] * o, b[1] + n[1] * o], color=color, lw=2)


def lp(ax, x, y, ang, r=0.3, sep=0.07, color=C_BLUE):
    t = np.radians(ang)
    cx, cy = x + r * np.cos(t), y + r * np.sin(t)
    n = np.array([-np.sin(t), np.cos(t)])
    for s in (-1, 1):
        ax.add_patch(Circle((cx + s * sep * n[0], cy + s * sep * n[1]), 0.035, fc=color, ec="none", zorder=6))


def fc_mark(ax, x, y, s, color=C_RED):
    ax.text(x, y, s, ha="center", va="center", fontsize=10, color=color, zorder=7,
            bbox=dict(boxstyle="circle,pad=0.1", fc="white", ec=color, lw=1))


def a2_10():
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.4), gridspec_kw=dict(width_ratios=[0.8, 0.95, 1.5]))
    ax = axs[0]; setup_ax(ax, "CO（10 个价电子）")
    atom(ax, 0, 0, "C"); atom(ax, 1, 0, "O"); bond(ax, (0, 0), (1, 0), 3)
    lp(ax, 0, 0, 180); lp(ax, 1, 0, 0)
    fc_mark(ax, -0.05, 0.38, "−"); fc_mark(ax, 1.05, 0.38, "+")
    ax.text(0.5, -0.8, "C≡O 三键，各 1 对孤对电子\n形式电荷 C −1 / O +1\n（偶极很小，C 端为配位端）", ha="center", fontsize=10)
    ax.set_xlim(-0.8, 1.8); ax.set_ylim(-1.5, 0.9)
    ax = axs[1]; setup_ax(ax, "[NO₂]⁺（16 e，与 CO₂ 等电子）")
    atom(ax, -1, 0, "O"); atom(ax, 0, 0, "N"); atom(ax, 1, 0, "O")
    bond(ax, (-1, 0), (0, 0), 2); bond(ax, (0, 0), (1, 0), 2)
    for x, a0 in [(-1, 180), (1, 0)]:
        lp(ax, x, 0, a0 + 60); lp(ax, x, 0, a0 - 60)
    fc_mark(ax, 0, 0.42, "+")
    ax.text(0, -0.8, "O=N=O，直线形（180°）\nN 无孤对，形式电荷 +1 在 N 上", ha="center", fontsize=10)
    ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.5, 0.9)
    ax = axs[2]; setup_ax(ax, "[NO₂]⁻（18 e）：两个共振式，弯曲 ≈115°")
    for dx, dbl in [(0, "L"), (3.8, "R")]:
        N = (dx, 0.3); O1 = (dx - 0.85, -0.35); O2 = (dx + 0.85, -0.35)
        atom(ax, *N, "N"); atom(ax, *O1, "O"); atom(ax, *O2, "O")
        bond(ax, N, O1, 2 if dbl == "L" else 1); bond(ax, N, O2, 1 if dbl == "L" else 2)
        lp(ax, *N, 90)
        dO, sO = (O1, O2) if dbl == "L" else (O2, O1)
        base_d = 200 if dbl == "L" else -20
        lp(ax, *dO, base_d + 50); lp(ax, *dO, base_d - 70)
        base_s = -20 if dbl == "L" else 200
        for a0 in (base_s + 70, base_s - 30, base_s - 120 if dbl == "L" else base_s + 160):
            lp(ax, *sO, a0)
        fc_mark(ax, sO[0] + (0.4 if dbl == "L" else -0.4), sO[1] + 0.45, "−")
    ax.text(1.9, 0.0, "⟷", fontsize=24, ha="center", va="center")
    ax.text(1.9, -1.35, "N 上 1 对孤对 → VSEPR AX₂E → 弯曲\n真实结构 = 两式平均：两个 N–O 键等长（键级 1.5）", ha="center", fontsize=10)
    ax.set_xlim(-1.5, 5.3); ax.set_ylim(-1.9, 1.0)
    save(fig, "A2_10_lewis_CO_NO2.png")


# ---------------- A2.11 氢键 ----------------
def a2_11():
    fig, axs = plt.subplots(1, 2, figsize=(14, 4.8))
    ax = axs[0]; setup_ax(ax, "(a) EtOH + H₂O：两种方向的 O–H···O 都能形成")
    # 乙醇供体 → 水受体
    atom(ax, 0, 1.2, "Et", fs=15); atom(ax, 0.9, 1.2, "O", fs=16); atom(ax, 1.5, 0.75, "H", fs=14, color=C_BLUE)
    bond(ax, (0, 1.2), (0.9, 1.2)); bond(ax, (0.9, 1.2), (1.5, 0.75), shrink=0.22)
    lp(ax, 0.9, 1.2, 60, color="#555"); lp(ax, 0.9, 1.2, 120, color="#555")
    atom(ax, 2.3, 0.2, "O", fs=16); atom(ax, 2.9, 0.65, "H", fs=14); atom(ax, 2.5, -0.5, "H", fs=14)
    bond(ax, (2.3, 0.2), (2.9, 0.65), shrink=0.22); bond(ax, (2.3, 0.2), (2.5, -0.5), shrink=0.22)
    ax.plot([1.62, 2.12], [0.66, 0.3], ls=(0, (2, 2)), color=C_RED, lw=2)
    ax.text(1.95, 0.8, "O–H···O", color=C_RED, fontsize=10)
    ax.text(1.5, -1.0, "EtOH 作供体，H₂O 作受体", ha="center", fontsize=10)
    # 水供体 → 乙醇受体
    ox = 4.6
    atom(ax, ox, 1.2, "O", fs=16); atom(ax, ox - 0.5, 1.75, "H", fs=14); atom(ax, ox + 0.6, 0.75, "H", fs=14, color=C_BLUE)
    bond(ax, (ox, 1.2), (ox - 0.5, 1.75), shrink=0.22); bond(ax, (ox, 1.2), (ox + 0.6, 0.75), shrink=0.22)
    atom(ax, ox + 1.4, 0.2, "O", fs=16); atom(ax, ox + 2.3, 0.2, "Et", fs=15); atom(ax, ox + 1.4, -0.55, "H", fs=14)
    bond(ax, (ox + 1.4, 0.2), (ox + 2.3, 0.2)); bond(ax, (ox + 1.4, 0.2), (ox + 1.4, -0.55), shrink=0.22)
    ax.plot([ox + 0.72, ox + 1.22], [0.66, 0.3], ls=(0, (2, 2)), color=C_RED, lw=2)
    ax.text(ox + 1.0, -1.0, "H₂O 作供体，EtOH 作受体", ha="center", fontsize=10)
    ax.text(3.3, 2.35, "两者都既有 O–H（供体）又有 O 孤对（受体）→ 完全互溶", ha="center", fontsize=10.5,
            color=C_DARK)
    ax.set_xlim(-0.6, 7.4); ax.set_ylim(-1.4, 2.7)
    ax = axs[1]; setup_ax(ax, "(b) EtNH₂ + Et₂O：只有 N–H···O 一种方向")
    atom(ax, 0, 0.6, "Et", fs=15); atom(ax, 1.0, 0.6, "N", fs=16)
    atom(ax, 1.0, 1.45, "H", fs=14); atom(ax, 1.8, 0.2, "H", fs=14, color=C_BLUE)
    bond(ax, (0, 0.6), (1.0, 0.6)); bond(ax, (1.0, 0.6), (1.0, 1.45), shrink=0.22)
    bond(ax, (1.0, 0.6), (1.8, 0.2), shrink=0.22)
    lp(ax, 1.0, 0.6, 235, color="#555")
    atom(ax, 2.8, -0.3, "O", fs=16); atom(ax, 3.6, 0.3, "Et", fs=15); atom(ax, 3.6, -0.9, "Et", fs=15)
    bond(ax, (2.8, -0.3), (3.6, 0.3)); bond(ax, (2.8, -0.3), (3.6, -0.9))
    lp(ax, 2.8, -0.3, 140, color="#555"); lp(ax, 2.8, -0.3, 220, color="#555")
    ax.plot([1.93, 2.58], [0.12, -0.18], ls=(0, (2, 2)), color=C_RED, lw=2)
    ax.text(2.25, 0.35, "N–H···O", color=C_RED, fontsize=10)
    ax.text(5.6, 0.95, "✗ Et₂O 没有 O–H（无供体 H）\n   不可能形成 O–H···N", fontsize=10, color=C_GRAY)
    ax.text(5.6, -0.4, "✓ 胺的 N–H 作供体\n✓ 醚的 O 孤对作受体\n→ 两者之间有氢键（较弱）", fontsize=10)
    ax.set_xlim(-0.6, 8.4); ax.set_ylim(-1.4, 2.0)
    save(fig, "A2_11_hbond_solvents.png")


# ---------------- A2.12 碳同素异形体 ----------------
def c60():
    phi = (1 + np.sqrt(5)) / 2
    base = [(0, 1, 3 * phi), (1, 2 + phi, 2 * phi), (phi, 2, 2 * phi + 1)]
    pts = set()
    for b in base:
        for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            v = [b[perm[0]], b[perm[1]], b[perm[2]]]
            for sx in (1, -1):
                for sy in (1, -1):
                    for sz in (1, -1):
                        pts.add((round(sx * v[0], 6), round(sy * v[1], 6), round(sz * v[2], 6)))
    return np.array(sorted(pts))


def a2_12():
    fig, axs = plt.subplots(1, 3, figsize=(14, 5))
    ax = axs[0]; setup_ax(ax, "金刚石：sp³，四面体三维网络")
    sc = Scene(ax, azim=-62, elev=18, scale=2.4)
    sc.cube(color="#aaa")
    fcc = CORN + FACE
    zn = [(0.25,0.25,0.25),(0.75,0.75,0.25),(0.75,0.25,0.75),(0.25,0.75,0.75)]
    for p in fcc: sc.ball(p, 0.08, C_DARK)
    for p in zn: sc.ball(p, 0.08, C_GRAY)
    for p in zn:
        for q in fcc:
            if np.linalg.norm(np.subtract(p, q)) < 0.45:
                sc.line(p, q, color="#333", lw=1.6)
    sc.render()
    foot(ax, "C–C 1.54 Å，CN 4，立方 a = 3.567 Å\n最硬、绝缘体（带隙 ≈ 5.5 eV）、导热好", ha="center", fontsize=9.8)
    ax = axs[1]; setup_ax(ax, "石墨：sp² 层（石墨烯）ABAB 堆叠")
    sc = Scene(ax, azim=-75, elev=16, scale=0.42)
    acc = 1.42; c2 = 3.35
    a1 = np.array([acc * np.sqrt(3), 0]); a2 = np.array([acc * np.sqrt(3) / 2, acc * 1.5])
    for L, z in enumerate([0, c2, 2 * c2]):
        shift = np.array([0, 0]) if L % 2 == 0 else np.array([0, acc])
        atoms = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                o = i * a1 + j * a2 + shift
                for b in (np.array([0, 0]), np.array([0, acc])):
                    q = o + b
                    if q[0] ** 2 + q[1] ** 2 < 4.3 ** 2:
                        atoms.append((q[0], q[1], z))
        atoms = [p for p in atoms if sum(np.linalg.norm(np.subtract(p, q)) < acc * 1.05 for q in atoms) >= 3]
        for i, p in enumerate(atoms):
            for q in atoms[i + 1:]:
                if np.linalg.norm(np.subtract(p, q)) < acc * 1.05:
                    sc.line(p, q, color=[C_DARK, C_BLUE, C_DARK][L], lw=1.3)
        for p in atoms:
            sc.ball(p, 0.16, [C_DARK, C_BLUE, C_DARK][L])
    sc.text((3.4, -1.0, 0.5 * c2), "层间 3.35 Å\n范德华力", fontsize=9.5, color=C_RED)
    sc.render()
    foot(ax, "层内 C–C 1.42 Å（强共价 + 离域 π）\n层间 3.35 Å（弱）→ 各向异性：层内导电、易滑移", ha="center",
            fontsize=9.8)
    ax = axs[2]; setup_ax(ax, "富勒烯 C₆₀：截角二十面体（分子）")
    P = c60() * 0.55
    sc = Scene(ax, azim=-50, elev=25, scale=1)
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            if np.linalg.norm(P[i] - P[j]) < 2 * 0.55 * 1.05:
                sc.line(P[i], P[j], color="#333", lw=1.1)
    for p in P:
        sc.ball(p, 0.13, C_DARK)
    sc.render()
    foot(ax, "60 个 C：12 个五元环 + 20 个六元环\n分子晶体（fcc 堆积），可溶于甲苯", ha="center", fontsize=9.8)
    save(fig, "A2_12_carbon_allotropes.png")


# ---------------- A2.13 [Si4O12]8- ----------------
def a2_13():
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.9), gridspec_kw=dict(width_ratios=[1, 1, 1.05]))
    Rsi = 1.0
    si = [np.array([Rsi * np.cos(np.radians(45 + 90 * k)), Rsi * np.sin(np.radians(45 + 90 * k))]) for k in range(4)]
    ob = [(si[k] + si[(k + 1) % 4]) / 2 * 1.32 for k in range(4)]
    ot = [si[k] * 1.85 for k in range(4)]
    ax = axs[0]; setup_ax(ax, "(a) 多面体表示（俯视）")
    for k in range(4):
        tri = [ob[k - 1], ob[k], ot[k]]
        ax.add_patch(Polygon(tri, fc=blend(C_BLUE, "white", 0.45), ec=C_BLUE, lw=1.5))
        ax.add_patch(Circle(si[k] * 1.12, 0.06, fc=C_RED))  # 指向上方的端氧（投影）
    ax.text(0, 0, "Si₄O₄\n八元环", ha="center", va="center", fontsize=10)
    ax.text(0, -2.6, "4 个 SiO₄ 四面体各共用 2 个顶点\n闭合成环（环状硅酸盐）", ha="center", fontsize=10)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-3.1, 2.4)
    ax = axs[1]; setup_ax(ax, "(b) 球棍表示")
    for k in range(4):
        for o in (ob[k - 1], ob[k], ot[k]):
            ax.plot([si[k][0], o[0]], [si[k][1], o[1]], color="#444", lw=2, zorder=1)
    for k in range(4):
        ax.add_patch(Circle(si[k], 0.18, fc=C_BLUE, ec="k", zorder=3))
        ax.text(*si[k], "Si", ha="center", va="center", fontsize=8, color="white", zorder=4)
        ax.add_patch(Circle(ob[k], 0.15, fc=C_RED, ec="k", zorder=3))
        ax.add_patch(Circle(ot[k], 0.15, fc=blend(C_RED, "white", 0.4), ec="k", zorder=3))
        ax.text(ot[k][0] * 1.17, ot[k][1] * 1.17, "O⁻", ha="center", va="center", fontsize=9)
        up = si[k] * 1.25 + np.array([0.0, 0.0])
    ax.text(0, 0, "桥氧 ×4\n端氧 ×8", ha="center", va="center", fontsize=9.5)
    ax.text(0, -2.6, "每个 Si：2 个桥氧 + 2 个端氧（Q² 单元）\n另一个端氧朝纸面外，未画出", ha="center", fontsize=10)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-3.1, 2.4)
    ax = axs[2]; ax.axis("off"); ax.set_title("(c) 由组成推结构", fontsize=12)
    lines = ["Si : O = 4 : 12 = 1 : 3  → 每个 SiO₄ 共用 2 个顶点",
             "O 总数 = 4×4 − 桥氧数 = 12  → 桥氧 = 4",
             "4 个四面体 + 4 根桥 → 必有 1 个环（树只需 3 根桥）",
             "电荷：4×(+4) + 12×(−2) = −8 ✓",
             "",
             "对比同 1:3 的其他硅酸盐：",
             "  [Si₃O₉]⁶⁻ 三元环（蓝锥矿 BaTiSi₃O₉）",
             "  [Si₆O₁₈]¹²⁻ 六元环（绿柱石 Be₃Al₂Si₆O₁₈）",
             "  [SiO₃]ₙ²ⁿ⁻ 无限单链（辉石）",
             "",
             "（3 元环 + 1 个支链四面体在计数上也满足，",
             "  但含 3 元环张力大，通常不出现）"]
    for k, s in enumerate(lines):
        ax.text(0.0, 0.95 - k * 0.083, s, fontsize=10.2, transform=ax.transAxes)
    save(fig, "A2_13_Si4O12_ring.png")


# ---------------- A2.14 锡 ----------------
def a2_14():
    fig, axs = plt.subplots(1, 3, figsize=(14, 5.2), gridspec_kw=dict(width_ratios=[1, 1, 0.95]))
    ax = axs[0]; setup_ax(ax, "α-Sn（灰锡）：金刚石型，立方")
    a = 6.49
    sc = Scene(ax, azim=-62, elev=18, scale=0.36)
    sc.box((a,0,0),(0,a,0),(0,0,a), color="#999")
    fcc = [np.array(p) * a for p in CORN + FACE]
    zn = [np.array(p) * a for p in [(0.25,0.25,0.25),(0.75,0.75,0.25),(0.75,0.25,0.75),(0.25,0.75,0.75)]]
    for p in fcc: sc.ball(p, 0.45, C_GRAY)
    for p in zn: sc.ball(p, 0.45, C_GRAY)
    for p in zn:
        for q in fcc:
            if np.linalg.norm(p - q) < 3.0:
                sc.line(p, q, color="#333", lw=1.6)
    sc.render()
    foot(ax, "a = 6.49 Å；CN 4（Sn–Sn 2.81 Å）\nρ = 5.77 g/cm³；带隙 ≈ 0（半金属）\n稳定于 < 13.2 °C，脆、粉末状",
            ha="center", fontsize=9.8)
    ax = axs[1]; setup_ax(ax, "β-Sn（白锡）：四方 I4₁/amd")
    a, c = 5.83, 3.18
    sc = Scene(ax, azim=-58, elev=15, scale=0.42, offset=(0, 0.2))
    sc.box((a,0,0),(0,a,0),(0,0,c), color="#999")
    basis = [(0,0,0),(0,0.5,0.25),(0.5,0.5,0.5),(0.5,0,0.75)]
    pts = []
    for b in basis:
        for t in itertools.product([-1,0,1], repeat=3):
            f = np.array(b) + np.array(t)
            if all(-1e-6 <= f[i] <= 1 + 1e-6 for i in (0, 1)) and -0.5 - 1e-6 <= f[2] <= 1.5 + 1e-6:
                pts.append(f * np.array([a, a, c]))
    pts = [p for p in pts if -1e-6 <= p[2] <= c + 1e-6 or (abs(p[0] - a/2) < 1e-6 and abs(p[1] - a/2) < 1e-6)]
    cen = np.array([a/2, a/2, c/2])
    for p in pts:
        d = np.linalg.norm(p - cen)
        if 0.1 < d < 3.05:
            sc.line(cen, p, color=C_RED, lw=2.2)
        elif 3.1 < d < 3.25:
            sc.line(cen, p, color=C_BLUE, lw=2.2, ls="--")
    for p in pts:
        isc = np.linalg.norm(p - cen) < 0.1
        sc.ball(p, 0.45, C_ORANGE if isc else C_GRAY)
    sc.render()
    foot(ax, "a = 5.83 Å, c = 3.18 Å；CN 4 + 2\n红：4 × 3.02 Å　蓝虚线：2 × 3.18 Å\nρ = 7.29 g/cm³；金属，延展性好", ha="center",
            fontsize=9.8)
    ax = axs[2]; ax.set_title("相变：13.2 °C", fontsize=12)
    T = np.array([-40, 13.2, 13.2, 120]); ax.axvline(13.2, color="k", ls="--")
    ax.fill_between([-40, 13.2], 0, 1, color=C_GRAY, alpha=0.25); ax.fill_between([13.2, 120], 0, 1, color=C_ORANGE, alpha=0.25)
    ax.text(-14, 0.75, "α-Sn\n灰锡\nCN 4", ha="center", fontsize=11)
    ax.text(66, 0.75, "β-Sn\n白锡\nCN 4+2", ha="center", fontsize=11)
    ax.text(-14, 0.58, "ρ 5.77", ha="center"); ax.text(66, 0.58, "ρ 7.29", ha="center")
    ax.annotate("", xy=(-25, 0.5), xytext=(80, 0.5), arrowprops=dict(arrowstyle="->", color=C_RED, lw=2))
    ax.text(40, 0.12, "低温放置：β → α\n体积增大约 27%\n→ 锡器碎裂成粉\n“锡疫”（tin pest）", ha="center", fontsize=9.5, color=C_RED,
            bbox=dict(fc="white", ec=C_RED, lw=0.8))
    ax.set_xlim(-40, 120); ax.set_ylim(0, 1); ax.set_yticks([]); ax.set_xlabel("T / °C")
    save(fig, "A2_14_tin_polymorphs.png")


if __name__ == "__main__":
    for f in [a2_1, a2_2, a2_3, a2_4, a2_5, a2_6, a2_7, a2_8, a2_9, a2_10, a2_11, a2_12, a2_13, a2_14]:
        f()
