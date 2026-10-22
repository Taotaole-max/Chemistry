# 生成讲义配图 fig/F1–F7
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in font_manager.findSystemFonts():
    if "wqy-zenhei" in f.lower() or "wqy_zenhei" in f.lower():
        font_manager.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": ["WenQuanYi Zen Hei", "DejaVu Sans"],
    "axes.unicode_minus": False,
    "font.size": 10.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.dpi": 200,
    "mathtext.fontset": "dejavusans",
})
BLUE, ORANGE, GREEN, RED, GREY = "#2563eb", "#ea580c", "#16a34a", "#dc2626", "#6b7280"
os.makedirs("fig", exist_ok=True)


def save(name):
    plt.tight_layout()
    plt.savefig(f"fig/{name}.png", bbox_inches="tight")
    plt.close()


# F1 Langmuir 等温式：缔合 vs 解离
x = np.linspace(0, 10, 400)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
ax[0].plot(x, x / (1 + x), color=BLUE, lw=2, label="缔合  θ = Kp/(1+Kp)")
ax[0].plot(x, np.sqrt(x) / (1 + np.sqrt(x)), color=ORANGE, lw=2, label="解离  θ = √(Kp)/(1+√(Kp))")
ax[0].axhline(0.5, color=GREY, ls=":", lw=1)
ax[0].axvline(1, color=GREY, ls=":", lw=1)
ax[0].text(1.15, 0.05, "Kp = 1 时两者都是 θ = 0.5", color=GREY, fontsize=9)
ax[0].set_xlabel("Kp"); ax[0].set_ylabel("覆盖度 θ"); ax[0].set_ylim(0, 1)
ax[0].legend(frameon=False, fontsize=9, loc="lower right"); ax[0].set_title("线性坐标")
xl = np.logspace(-4, 2, 300)
ax[1].loglog(xl, xl / (1 + xl), color=BLUE, lw=2, label="缔合：低压斜率 1")
ax[1].loglog(xl, np.sqrt(xl) / (1 + np.sqrt(xl)), color=ORANGE, lw=2, label="解离：低压斜率 1/2")
ax[1].set_xlabel("Kp（对数）"); ax[1].set_ylabel("θ（对数）")
ax[1].legend(frameon=False, fontsize=9, loc="lower right"); ax[1].set_title("双对数坐标：低压斜率区分是否解离")
save("F1_langmuir")

# F2 LH 单分子：速率与表观级数
K = 2.0
p = np.linspace(0, 5, 400)
th = K * p / (1 + K * p)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
ax[0].plot(p, th, color=BLUE, lw=2)
ax[0].plot(p[p < 0.6], K * p[p < 0.6], color=GREY, ls="--", lw=1)
ax[0].axhline(1, color=GREY, ls="--", lw=1)
pd = np.array([0.1, 0.4, 1.6])
ax[0].plot(pd, K * pd / (1 + K * pd), "o", color=ORANGE, ms=6, zorder=5, label="J3-1 数据点")
ax[0].text(0.17, 0.83, "低压：r ≈ kKp（一级）", fontsize=9, color=GREY, transform=ax[0].transAxes)
ax[0].text(0.42, 0.60, "高压：r → k（零级）", fontsize=9, color=GREY, transform=ax[0].transAxes)
ax[0].set_xlabel("p_A / bar"); ax[0].set_ylabel("r / k  ( = θ_A )"); ax[0].set_ylim(0, 1.1)
ax[0].legend(frameon=False, fontsize=9, loc="lower right"); ax[0].set_title("r = kK_A p_A /(1+K_A p_A)，K_A = 2 bar⁻¹")
pl = np.logspace(-2, 1.5, 300)
ax[1].semilogx(pl, 1 / (1 + K * pl), color=GREEN, lw=2, label="表观级数 n = 1 − θ")
ax[1].semilogx(pl, K * pl / (1 + K * pl), color=BLUE, lw=1.5, ls="--", label="覆盖度 θ")
for pm, n in ((0.2, 0.71), (0.8, 0.39)):
    ax[1].plot(pm, n, "s", color=ORANGE, ms=6, zorder=5)
    ax[1].annotate(f"p={pm}: n≈{n}", (pm, n), xytext=(8, 4), textcoords="offset points", fontsize=9, color=ORANGE)
ax[1].set_xlabel("p_A / bar（对数）"); ax[1].set_ylabel("n 或 θ"); ax[1].set_ylim(0, 1.05)
ax[1].legend(frameon=False, fontsize=9, loc="center right"); ax[1].set_title("级数随压力从 1 连续降到 0")
save("F2_LH_uni")

# F3 LH 双分子 vs ER
xa = np.linspace(0, 8, 400)
KbPb = 1.0
lh = xa * KbPb / (1 + xa + KbPb) ** 2
er = xa / (1 + xa)
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.plot(xa, lh / lh.max(), color=BLUE, lw=2, label="LH：r ∝ K_A p_A K_B p_B /(1+K_A p_A+K_B p_B)²")
ax.plot(xa, er / er.max(), color=ORANGE, lw=2, label="ER：r ∝ K_A p_A p_B /(1+K_A p_A)")
ax.axvline(1 + KbPb, color=GREY, ls=":", lw=1)
ax.text(1 + KbPb + 0.1, 0.12, "最大值：K_A p_A = 1 + K_B p_B\n（此时 θ_A = 1/2）", fontsize=9, color=GREY)
ax.set_xlabel("K_A p_A（固定 K_B p_B = 1）"); ax.set_ylabel("相对速率")
ax.legend(frameon=False, fontsize=8.5, loc="lower right"); ax.set_ylim(0, 1.08)
ax.set_title("固定 p_B、增大 p_A：LH 先升后降，ER 升到平台")
save("F3_LH_vs_ER")

# F4 粘附概率与覆盖度随时间
th = np.linspace(0, 1, 200)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
ax[0].plot(th, 1 - th, color=BLUE, lw=2, label="缔合：s/s₀ = 1 − θ")
ax[0].plot(th, (1 - th) ** 2, color=ORANGE, lw=2, label="解离：s/s₀ = (1 − θ)²")
ax[0].plot([0.5, 0.5], [0, 0.5], color=GREY, ls=":", lw=1)
ax[0].text(0.52, 0.52, "θ=0.5：50%", fontsize=9, color=BLUE)
ax[0].text(0.52, 0.27, "θ=0.5：25%", fontsize=9, color=ORANGE)
ax[0].set_xlabel("覆盖度 θ"); ax[0].set_ylabel("s / s₀")
ax[0].legend(frameon=False, fontsize=9); ax[0].set_title("解离吸附需要两个相邻空位")
t = np.linspace(0, 6, 300)
ax[1].plot(t, 1 - np.exp(-t), color=BLUE, lw=2, label="缔合：θ = 1 − e^(−t/τ)")
ax[1].plot(t, t / (1 + t), color=ORANGE, lw=2, label="解离：θ = (t/τ')/(1 + t/τ')")
ax[1].set_xlabel("t / τ（或 t / τ'）"); ax[1].set_ylabel("θ"); ax[1].set_ylim(0, 1)
ax[1].legend(frameon=False, fontsize=9, loc="lower right"); ax[1].set_title("恒压暴露下覆盖度的增长")
save("F4_sticking")

# F5 J3-1 数据作图
pd = np.array([0.1, 0.4, 1.6]); rd = np.array([0.167, 0.444, 0.762])
fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
ax[0].plot(np.log(pd), np.log(rd), "o-", color=BLUE, lw=1.5, ms=6)
for i, n in enumerate((0.71, 0.39)):
    xm = (np.log(pd[i]) + np.log(pd[i + 1])) / 2; ym = (np.log(rd[i]) + np.log(rd[i + 1])) / 2
    ax[0].annotate(f"斜率 n = {n}", (xm, ym), xytext=(-70, 10), textcoords="offset points", fontsize=9.5, color=ORANGE)
ax[0].set_xlabel("ln p_A"); ax[0].set_ylabel("ln r"); ax[0].set_title("ln r – ln p：每段斜率就是表观级数")
xi = 1 / pd; yi = 1 / rd
a, b = np.polyfit(xi, yi, 1)
xx = np.linspace(0, 11, 50)
ax[1].plot(xi, yi, "o", color=BLUE, ms=6)
ax[1].plot(xx, a * xx + b, color=ORANGE, lw=1.5, label=f"拟合：斜率 {a:.3f}，截距 {b:.3f}")
ax[1].set_xlabel("1 / p_A  (bar⁻¹)"); ax[1].set_ylabel("1 / r")
ax[1].legend(frameon=False, fontsize=9, loc="upper left")
ax[1].set_title(f"1/r – 1/p 线性化：K = 截距/斜率 ≈ {b/a:.2f} bar⁻¹")
save("F5_J31_plots")

# F6 表观活化能随温度变化（LH 单分子）
Rg = 8.314; Et = 100e3; dH = -80e3; K0 = 4.3e-9; pA = 1.0
T = np.linspace(330, 900, 400)
k = 1e13 * np.exp(-Et / (Rg * T)); Kt = K0 * np.exp(-dH / (Rg * T))
r = k * Kt * pA / (1 + Kt * pA)
th = Kt * pA / (1 + Kt * pA)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
ax[0].plot(1000 / T, np.log(r), color=BLUE, lw=2)
ax[0].set_xlabel("1000 / T  (K⁻¹)"); ax[0].set_ylabel("ln r")
ax[0].text(0.60, 0.62, "右段＝低温：θ→1，斜率陡\nE_app = E_true = 100", transform=ax[0].transAxes, fontsize=9, color=GREY)
ax[0].text(0.03, 0.40, "左段＝高温：θ→0，斜率缓\nE_app = E_true + ΔH = 20", transform=ax[0].transAxes, fontsize=9, color=GREY)
ax[0].set_title("Arrhenius 图弯曲（单位 kJ/mol）")
ax[1].plot(T, (Et + dH * (1 - th)) / 1000, color=GREEN, lw=2, label="E_app = E_true + (1−θ)ΔH_ads")
ax[1].plot(T, th * 100, color=BLUE, lw=1.5, ls="--", label="θ × 100")
ax[1].set_xlabel("T / K"); ax[1].set_ylabel("kJ/mol   或   θ×100")
ax[1].legend(frameon=False, fontsize=9, loc="center right"); ax[1].set_title("E_true = 100，ΔH_ads = −80 kJ/mol")
save("F6_Eapp")

# F7 TPD：一级 vs 二级
def tpd(E, order, th0, beta=10.0, nu=1e13, T0=150.0, T1=750.0, n=60000):
    Ts = np.linspace(T0, T1, n); dT = Ts[1] - Ts[0]; th = th0; out = []
    for Tk in Ts:
        rate = nu * th ** order * np.exp(-E / (Rg * Tk)) / beta
        out.append(rate); th = max(th - rate * dT, 0.0)
    return Ts, np.array(out)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
for E, c in ((80e3, BLUE), (100e3, GREEN), (120e3, ORANGE)):
    Ts, rr = tpd(E, 1, 1.0)
    ax[0].plot(Ts, rr, color=c, lw=2, label=f"E_des = {int(E/1000)} kJ/mol")
ax[0].set_xlabel("T / K"); ax[0].set_ylabel("脱附速率（任意单位）"); ax[0].set_xlim(200, 600)
ax[0].legend(frameon=False, fontsize=9); ax[0].set_title("一级脱附：E 越大峰越靠高温")
for th0, c in ((1.0, BLUE), (0.5, GREEN), (0.25, ORANGE)):
    Ts, rr = tpd(100e3, 2, th0)
    ax[1].plot(Ts, rr, color=c, lw=2, label=f"θ₀ = {th0}")
ax[1].set_xlabel("T / K"); ax[1].set_ylabel("脱附速率（任意单位）"); ax[1].set_xlim(250, 600)
ax[1].legend(frameon=False, fontsize=9); ax[1].set_title("二级（复合）脱附：θ₀ 越大峰越靠低温")
save("F7_TPD")
print("figures done")
