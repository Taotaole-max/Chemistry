# 作图公用工具：中文字体、简易 3D 正交投影球棍模型、流程图方框/箭头
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import to_rgb

plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "WenQuanYi Zen Hei"
plt.rcParams["mathtext.it"] = "DejaVu Sans:italic"
plt.rcParams["mathtext.bf"] = "DejaVu Sans:bold"
plt.rcParams["mathtext.default"] = "rm"
plt.rcParams["font.size"] = 11

FIG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figs")
os.makedirs(FIG_DIR, exist_ok=True)

# 统一配色
C_BLUE = "#3b6fb6"
C_RED = "#c8453a"
C_GREEN = "#3f9a5a"
C_ORANGE = "#e08a2c"
C_PURPLE = "#7d58b3"
C_GRAY = "#8a8f98"
C_YELLOW = "#e3c13b"
C_TEAL = "#2f9c9c"
C_DARK = "#2b2f36"


def save(fig, name, dpi=170):
    path = os.path.join(FIG_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name)


def blend(c, w, t):
    c = np.array(to_rgb(c)); w = np.array(to_rgb(w))
    return tuple(c * (1 - t) + w * t)


class Scene:
    """简易正交投影：azim/elev 定义视线方向，按深度排序画球、键、多面体。"""

    def __init__(self, ax, azim=-60, elev=20, scale=1.0, offset=(0, 0)):
        self.ax = ax
        a, e = np.radians(azim), np.radians(elev)
        self.d = np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])
        self.ux = np.array([-np.sin(a), np.cos(a), 0.0])
        self.uy = np.cross(self.d, self.ux)
        self.s = scale
        self.off = np.array(offset, float)
        self.items = []
        self.texts = []
        self.shift = np.zeros(2)

    def P(self, p):
        p = np.asarray(p, float)
        return np.array([p @ self.ux, p @ self.uy]) * self.s + self.off, p @ self.d

    def ball(self, p, r, color, label=None, lc="white", fs=8, alpha=1.0, edge=None):
        xy, dep = self.P(p)
        self.items.append(("ball", dep, xy, r * self.s, color, label, lc, fs, alpha, edge))

    def line(self, p1, p2, color="#555", lw=1.0, ls="-", alpha=1.0, front=False):
        (a, d1), (b, d2) = self.P(p1), self.P(p2)
        dep = 1e6 if front else (d1 + d2) / 2 - 1e-3
        self.items.append(("line", dep, a, b, color, lw, ls, alpha))

    def poly(self, pts, fc, alpha=0.35, ec="#333", lw=0.8, dep_shift=0.0):
        xy = [self.P(p)[0] for p in pts]
        dep = np.mean([self.P(p)[1] for p in pts]) + dep_shift
        self.items.append(("poly", dep, xy, fc, alpha, ec, lw))

    def text(self, p, s, **kw):
        xy, _ = self.P(p)
        self.texts.append((xy, s, kw))

    def cube(self, o=(0, 0, 0), a=1.0, color="#555", lw=1.0, ls="-", **kw):
        o = np.array(o, float)
        v = [o + a * np.array(c) for c in [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]]
        for i, j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
            self.line(v[i], v[j], color=color, lw=lw, ls=ls, **kw)

    def box(self, a, b, c, o=(0, 0, 0), color="#555", lw=1.0):
        """任意平行六面体晶胞（a,b,c 为向量）。"""
        o = np.array(o, float); a, b, c = map(np.array, (a, b, c))
        v = [o, o+a, o+a+b, o+b, o+c, o+a+c, o+a+b+c, o+b+c]
        for i, j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
            self.line(v[i], v[j], color=color, lw=lw)

    def render(self, autocenter=True, fit=True, pad=0.12):
        items = sorted(self.items, key=lambda t: t[1])
        if autocenter and items:
            pts = []
            for it in items:
                if it[0] == "ball":
                    pts += [it[2] - it[3], it[2] + it[3]]
                elif it[0] == "line":
                    pts += [it[2], it[3]]
                else:
                    pts += list(it[2])
            pts = np.array(pts)
            sh = self.off - (pts.min(0) + pts.max(0)) / 2
            new = []
            for it in items:
                if it[0] == "ball":
                    it = it[:2] + (it[2] + sh,) + it[3:]
                elif it[0] == "line":
                    it = it[:2] + (it[2] + sh, it[3] + sh) + it[4:]
                else:
                    it = it[:2] + ([np.asarray(q) + sh for q in it[2]],) + it[3:]
                new.append(it)
            items = new
            self.shift = sh
        for z, it in enumerate(items):
            zo = 10 + z
            if it[0] == "ball":
                _, _, xy, r, color, label, lc, fs, alpha, edge = it
                ec = edge if edge else blend(color, "black", 0.45)
                self.ax.add_patch(Circle(xy, r, fc=color, ec=ec, lw=0.7, zorder=zo, alpha=alpha))
                n = 7
                for k in range(1, n):
                    t = k / n
                    rr = r * (1 - t) * 0.92
                    cc = (xy[0] - 0.33 * r * t, xy[1] + 0.33 * r * t)
                    self.ax.add_patch(Circle(cc, rr, fc=blend(color, "white", 0.55 * t), ec="none",
                                             zorder=zo, alpha=alpha))
                if label:
                    self.ax.text(xy[0], xy[1], label, ha="center", va="center", fontsize=fs,
                                 color=lc, zorder=zo, fontweight="bold")
            elif it[0] == "line":
                _, _, a, b, color, lw, ls, alpha = it
                self.ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, alpha=alpha,
                             zorder=zo, solid_capstyle="round")
            else:
                _, _, xy, fc, alpha, ec, lw = it
                self.ax.add_patch(Polygon(xy, closed=True, fc=fc, alpha=alpha, ec=ec, lw=lw, zorder=zo))
        for xy, s, kw in self.texts:
            self.ax.text(xy[0] + self.shift[0], xy[1] + self.shift[1], s, zorder=100000, **kw)
        if fit and items:
            lo, hi = pts.min(0) + sh, pts.max(0) + sh
            span = (hi - lo).max()
            self.ax.set_xlim(lo[0] - pad * span, hi[0] + pad * span)
            self.ax.set_ylim(lo[1] - pad * span, hi[1] + pad * span)
        self.items = []
        self.texts = []


def foot(ax, s, fontsize=10, y=-0.01, **kw):
    kw.pop("ha", None)
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top", fontsize=fontsize, **kw)


def setup_ax(ax, title=None, fs=12):
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=fs)


def fbox(ax, x, y, w, h, text, fc="#eef3fb", ec=C_BLUE, fs=10, lw=1.2, color="black", r=0.02, **kw):
    """以 (x,y) 为中心的圆角方框。"""
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0.01,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=color, zorder=4, **kw)


def farrow(ax, p1, p2, text=None, color="#333", fs=9, lw=1.4, off=(0.0, 0.0), ms=12, ls="-", rad=0.0,
           ha="center", tc=None):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw,
                                 linestyle=ls, connectionstyle=f"arc3,rad={rad}", zorder=2))
    if text:
        mx, my = (p1[0] + p2[0]) / 2 + off[0], (p1[1] + p2[1]) / 2 + off[1]
        ax.text(mx, my, text, ha=ha, va="center", fontsize=fs, color=tc or color, zorder=5)


def canvas(w=10, h=6, xlim=(0, 10), ylim=(0, 6)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def fcc_points(n=1):
    pts = []
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                pts.append((i, j, k))
    base = [(0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                for b in base:
                    p = (i + b[0], j + b[1], k + b[2])
                    if all(0 <= c <= n + 1e-9 for c in p):
                        pts.append(p)
    return sorted(set(pts))


def in_cell(p, eps=1e-9):
    return all(-eps <= c <= 1 + eps for c in p)


def hull_faces(pts, tol=1e-6):
    """凸多面体的面（暴力法，点数少时够用），每个面的顶点按环绕顺序返回。"""
    pts = np.asarray(pts, float)
    n = len(pts)
    faces = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                nrm = np.cross(pts[j] - pts[i], pts[k] - pts[i])
                if np.linalg.norm(nrm) < tol:
                    continue
                nrm /= np.linalg.norm(nrm)
                s = (pts - pts[i]) @ nrm
                if np.all(s <= tol) or np.all(s >= -tol):
                    faces.add(tuple(sorted(np.where(np.abs(s) < 1e-4)[0])))
    out = []
    for f in faces:
        P = pts[list(f)]
        c = P.mean(0)
        nrm = np.cross(P[1] - P[0], P[2] - P[0]); nrm /= np.linalg.norm(nrm)
        u = P[0] - c; u /= np.linalg.norm(u); v = np.cross(nrm, u)
        ang = np.arctan2((P - c) @ v, (P - c) @ u)
        out.append(P[np.argsort(ang)])
    return out
