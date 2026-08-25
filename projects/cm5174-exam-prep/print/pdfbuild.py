# -*- coding: utf-8 -*-
import re, sys, json, pathlib, markdown
sys.path.insert(0,'/tmp/claude-0/-home-user-Chemistry/6ededadf-7730-5f8a-b573-90f01f881232/scratchpad/gen')
from tex import tex
from data import Q

BASE = pathlib.Path("/home/user/Chemistry/projects/cm5174-exam-prep")
OUT  = BASE / "print"; OUT.mkdir(exist_ok=True)
KEYS = ["A","B","C","D"]

CSS = r"""
@page { size:A4; margin:17mm 15mm 16mm; }
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact; print-color-adjust:exact}
body{
  margin:0; font-family:"Noto Sans CJK SC","Noto Sans CJK SC Regular",sans-serif;
  font-size:9.9pt; line-height:1.62; color:#15202B; background:#fff;
}
/* ---- 版心与标题 ---- */
h1{
  font-size:20pt; line-height:1.25; margin:0 0 2mm; letter-spacing:-.01em;
  color:#0F1B26; font-weight:700;
}
h2{
  font-size:13pt; margin:0 0 3mm; padding:0 0 1.6mm; font-weight:700; color:#0F1B26;
  border-bottom:1.6pt solid #1F4E8C; break-after:avoid; break-inside:avoid;
}
h3{
  font-size:10.8pt; margin:5mm 0 1.8mm; font-weight:700; color:#1F4E8C;
  break-after:avoid; break-inside:avoid;
}
h4{font-size:10pt; margin:4mm 0 1.5mm; font-weight:700; color:#33424F; break-after:avoid}
p{margin:0 0 2.2mm; orphans:3; widows:3}
ul,ol{margin:0 0 2.4mm; padding-left:5.2mm}
li{margin:0 0 1mm}
b,strong{font-weight:700; color:#0F1B26}
a{color:#1F4E8C; text-decoration:none}
hr{border:0; border-top:.5pt solid #D5DDE5; margin:4mm 0}
sub,sup{font-size:.68em; line-height:0}
code{font-family:"Noto Sans Mono CJK SC",monospace; font-size:.9em; background:#F1F4F7; padding:.3mm 1mm; border-radius:1mm}
/* ---- 表格 ---- */
table{
  width:100%; border-collapse:collapse; margin:2.6mm 0 3.4mm;
  font-size:9.1pt; break-inside:avoid;
}
th,td{border:.5pt solid #C3CDD8; padding:1.5mm 2.2mm; text-align:left; vertical-align:top}
th{background:#EDF1F6; font-weight:700; color:#0F1B26}
/* ---- 公式 ---- */
.fmb{
  margin:2.6mm 0; padding:2.4mm 3mm; text-align:center; background:#F5F8FB;
  border-left:1.6pt solid #1F4E8C; font-size:10.4pt; line-height:2.1;
  break-inside:avoid; overflow-wrap:anywhere;
}
.fmi{white-space:nowrap}
.fr{display:inline-block; vertical-align:-0.52em; text-align:center; margin:0 .18em}
.fr-n{display:block; padding:0 .28em}
.fr-d{display:block; padding:.06em .28em 0; border-top:.7pt solid currentColor}
.sq{white-space:nowrap}
.sq-b{border-top:.7pt solid currentColor; padding:0 .12em; margin-left:-.06em}
.op{font-style:normal; padding:0 .1em}
.bx{display:inline-block; border:.9pt solid #1F4E8C; border-radius:1.2mm; padding:1mm 2.4mm; background:#fff}
/* ---- 提示块 ---- */
blockquote{
  margin:2.6mm 0; padding:2mm 3mm; border-left:2pt solid #B8843A; background:#FBF6EC;
  font-size:9.4pt; color:#4A3A22; break-inside:avoid;
}
blockquote p:last-child{margin-bottom:0}
blockquote b,blockquote strong{color:#8A5A12}
/* ---- 封面 ---- */
.cover{break-after:page; padding-top:24mm}
.cover .eyebrow{
  font-size:9pt; letter-spacing:.22em; color:#1F4E8C; font-weight:700; margin:0 0 3mm;
}
.cover h1{font-size:27pt; margin:0 0 4mm}
.cover .tagline{font-size:11.5pt; color:#465costa; margin:0 0 10mm}
.cover .meta{font-size:9.4pt; color:#5A6875; line-height:1.9; border-top:.5pt solid #D5DDE5; padding-top:4mm}
.cover .meta b{color:#15202B}
.toc{margin-top:9mm; border-top:.5pt solid #D5DDE5; padding-top:4mm}
.toc h2{border:0; font-size:10.5pt; margin:0 0 2.5mm; padding:0}
.toc ol{list-style:none; padding:0; margin:0; font-size:9.4pt; columns:2; column-gap:9mm}
.toc li{margin:0 0 1.4mm; break-inside:avoid}
.toc .k{
  display:inline-block; min-width:8.5mm; font-weight:700; color:#1F4E8C;
  font-family:"Noto Sans Mono CJK SC",monospace; font-size:8.6pt;
}
/* ---- 题目 ---- */
.q{
  break-inside:auto; margin:0 0 4.5mm; border:.6pt solid #C9D3DD; border-radius:1.6mm;
  border-left:2.2pt solid #1F4E8C;
}
.q-top{break-inside:avoid; break-after:avoid}
.q-h{
  display:flex; align-items:baseline; gap:2.4mm; padding:2mm 3mm 0; flex-wrap:wrap;
  font-size:8.6pt; color:#5A6875;
}
.q-n{
  font-family:"Noto Sans Mono CJK SC",monospace; font-weight:700; font-size:9.4pt;
  color:#1F4E8C; background:#E7EEF7; padding:.4mm 1.8mm; border-radius:1mm;
}
.q-k{border:.5pt solid #C9D3DD; border-radius:.8mm; padding:.2mm 1.4mm; font-size:8pt}
.q-t{margin-left:auto; font-size:8.6pt}
.q-s{padding:1.8mm 3mm 1.4mm; font-size:9.9pt; line-height:1.5}
.q-o{list-style:none; margin:0; padding:0 3mm 2.4mm; display:block}
.q-o li{
  display:flex; gap:2.4mm; align-items:baseline; margin:0 0 1mm;
  padding:1.1mm 2.2mm; border:.5pt solid #DCE3EA; border-radius:1.2mm; font-size:9.5pt;
}
.q-o li.right{border-color:#1B7A52; background:#EDF7F1; font-weight:700}
.q-o .k{
  font-family:"Noto Sans Mono CJK SC",monospace; font-weight:700; font-size:9pt;
  min-width:4.2mm; color:#5A6875;
}
.q-o li.right .k{color:#1B7A52}
.q-o li.right .tick{margin-left:auto; color:#1B7A52; font-size:8.4pt; font-weight:700; white-space:nowrap}
.q-a{
  border-top:.5pt solid #DCE3EA; background:#FAFBFD; padding:2.2mm 3mm 2.4mm; font-size:9.3pt;
}
.q-a .lab{
  font-size:8.2pt; letter-spacing:.14em; color:#5A6875; font-weight:700;
  margin:0 0 1.6mm; display:flex; align-items:center; gap:2mm;
}
.q-a .lab::after{content:""; flex:1; height:.5pt; background:#DCE3EA}
.q-a .ans{color:#1B7A52; font-weight:700}
.q-a p{margin:0 0 1.6mm}
.q-a p:last-child{margin-bottom:0}
.q-a .fb{
  font-family:"Noto Sans Mono CJK SC",monospace; text-align:center; background:#fff;
  border:.5pt solid #DCE3EA; border-radius:1.2mm; padding:1.8mm 2.4mm; margin:1.8mm 0;
  font-size:9.2pt; line-height:1.75; break-inside:avoid; overflow-wrap:anywhere;
}
.q-a .trap{
  background:#FBF3E4; border-left:1.8pt solid #B8843A; border-radius:0 1.2mm 1.2mm 0;
  padding:1.6mm 2.4mm; margin:1.8mm 0; color:#4A3A22;
}
.q-a .trap b{color:#8A5A12}
.q-a .note{border-left:1.5pt solid #D5DDE5; padding:.4mm 0 .4mm 2.4mm; margin:1.8mm 0; color:#5A6875}
.q-a .note b{color:#33424F}
table.mini{margin:1.8mm 0; font-size:8.8pt}
table.mini th,table.mini td{padding:1.2mm 1.8mm}
/* ---- 速查/陷阱 ---- */
.sheet{break-before:page}
.keytab{font-size:8.8pt}
.keytab td.a{font-family:"Noto Sans Mono CJK SC",monospace; font-weight:700; color:#1B7A52; text-align:center}
.keytab td.n{font-family:"Noto Sans Mono CJK SC",monospace; text-align:center; color:#5A6875}
ol.traps{list-style:none; padding:0; margin:0; counter-reset:t}
ol.traps li{
  counter-increment:t; border-left:2pt solid #B8843A; padding:0 0 0 3mm;
  margin:0 0 3.2mm; break-inside:avoid;
}
ol.traps li::before{
  content:counter(t); font-family:"Noto Sans Mono CJK SC",monospace; font-weight:700;
  color:#B8843A; font-size:8.4pt; margin-right:2mm;
}
ol.traps .t{font-weight:700; font-size:10pt; color:#0F1B26}
ol.traps .jump{font-family:"Noto Sans Mono CJK SC",monospace; font-size:8.4pt; color:#1F4E8C; margin-left:1.5mm}
ol.traps .d{margin:.8mm 0 0; font-size:9.2pt; color:#5A6875}
.lec-break{break-before:page}
"""
CSS = CSS.replace("#465costa", "#465563")

def md2html(path):
    src = pathlib.Path(path).read_text(encoding="utf-8")
    store = []
    def keep(h):
        store.append(h); return "\x00M%d\x00" % (len(store)-1)
    # 块级公式 $$...$$
    src = re.sub(r'\$\$(.+?)\$\$', lambda m: keep('<div class="fmb">%s</div>' % tex(m.group(1).strip())),
                 src, flags=re.S)
    # 行内公式 $...$
    src = re.sub(r'(?<!\$)\$([^\$\n]+?)\$(?!\$)',
                 lambda m: keep('<span class="fmi">%s</span>' % tex(m.group(1))), src)
    html = markdown.markdown(src, extensions=["tables","fenced_code","sane_lists"])
    for i, h in enumerate(store):
        html = html.replace("\x00M%d\x00" % i, h)
    # 占位符被包进 <p> 的块级公式，拆出来
    html = re.sub(r'<p>(<div class="fmb">.*?</div>)</p>', r'\1', html, flags=re.S)
    return html

def page(title, body, cls=""):
    return ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
            '<title>%s</title><style>%s</style></head><body class="%s">%s</body></html>'
            % (title, CSS, cls, body))

# ============ 文档一：知识点整理 ============
def build_notes():
    html = md2html(BASE / "01_知识点整理.md")
    # 去掉 md 顶部的一级标题和引言（封面会重做）
    html = re.sub(r'^.*?<h2>全局地图</h2>', '<h2>全局地图</h2>', html, flags=re.S)
    # 每个 Lecture 从新页开始
    html = re.sub(r'<h2>(Lecture \d+)', r'<h2 class="lec-break">\1', html)
    cover = """
<section class="cover">
  <p class="eyebrow">CM 5174 · 期末复习</p>
  <h1>高分子物理化学<br>知识点整理</h1>
  <p class="tagline">Polymer and Macromolecular Chemistry · Lecture 1–10 全覆盖</p>
  <div class="meta">
    <b>课程</b>　CM5174 Polymer and Macromolecular Chemistry，NUS<br>
    <b>授课</b>　Assoc. Prof. Tan Zhi Kuang<br>
    <b>依据</b>　Lecture 1–10 全部讲义原文<br>
    <b>用法</b>　公式都保留了推导脉络；讲义原文的关键结论、易混淆处和常见误解都单独标出。<br>
    　　　　配套的 30 道模拟题见《CM5174 模拟题库》。
  </div>
  <div class="toc">
    <h2>目录</h2>
    <ol>
      <li><span class="k">L1</span>高分子尺寸与构象</li>
      <li><span class="k">L2</span>混合热力学</li>
      <li><span class="k">L3</span>Flory-Huggins 高分子溶液理论</li>
      <li><span class="k">L4</span>相行为</li>
      <li><span class="k">L5</span>渗透压与粘度法</li>
      <li><span class="k">L6</span>光散射与动态光散射</li>
      <li><span class="k">L7</span>SEC 与质谱</li>
      <li><span class="k">L8</span>玻璃态</li>
      <li><span class="k">L9</span>力学性质与加工</li>
      <li><span class="k">L10</span>弹性态与结晶态</li>
    </ol>
  </div>
</section>"""
    out = OUT / "notes.html"
    out.write_text(page("CM5174 知识点整理", cover + html), encoding="utf-8")
    return out

# ============ 文档二：题库（答案解析直接印在题下）============
TRAPS = [
 ("θ = 180° − 键角", "sp³ 是 <b>70.5°</b> 不是 109.5°，因子恰好 ≈ 2", 2),
 ("M<sub>w</sub> 的分母是 Σn<sub>i</sub>M<sub>i</sub>", "不是 Σn<sub>i</sub>；且 M<sub>w</sub> ≥ M<sub>n</sub> 恒成立", 1),
 ("ΔS / ΔH / ΔG 里的 n 是总摩尔数", "1 mol + 1 mol 要代 n = 2", 4),
 ("Flory-Huggins 只有高分子项除以 N", "φ = 0.5 时熵只减<b>一半</b>，不是 1/N", 7),
 ("ΔG<sub>mix</sub> &lt; 0 不代表不分相", "判据是 ΔG 曲线的<b>凹凸性</b>", 12),
 ("渗透压公式里 c 用 g/m³", "1 g/L = 1000 g/m³，漏掉差 1000 倍", 14),
 ("Fox 方程必须用绝对温度 K", "而且<b>不是</b>线性加权，是倒数加权", 25),
 ("Bragg 定律：题目给 2θ，公式用 θ", "先除以 2 再取 sin", 28),
]
LECFULL = {"L1":"尺寸与构象","L2":"混合热力学","L3":"Flory-Huggins","L4":"相行为",
 "L5":"渗透压与粘度","L6":"光散射","L7":"SEC 与质谱","L8":"玻璃态",
 "L9":"力学性质","L10":"弹性体与结晶","综合":"跨讲综合"}

def build_bank():
    qs = []
    for q in Q:
        opts = "".join(
          '<li class="%s"><span class="k">%s</span><span>%s</span>%s</li>' % (
            "right" if i == q["ans"] else "", KEYS[i], o,
            '<span class="tick">✓ 正确答案</span>' if i == q["ans"] else "")
          for i, o in enumerate(q["opts"]))
        qs.append(
          '<article class="q"><div class="q-top"><div class="q-h">'
          '<span class="q-n">Q%02d</span><span>%s %s</span>'
          '<span class="q-k">%s</span><span class="q-t">%s</span></div>'
          '<p class="q-s">%s</p><ul class="q-o">%s</ul></div>'
          '<div class="q-a"><p class="lab">答案 <span class="ans">%s</span>　·　解析</p>%s</div>'
          '</article>' % (q["n"], q["lec"], LECFULL[q["lec"]], q["kind"], q["topic"],
                          q["stem"], opts, KEYS[q["ans"]], q["exp"]))

    keyrows = "".join(
      '<tr><td class="n">%d</td><td class="a">%s</td><td class="n">%s</td><td>%s</td></tr>'
      % (q["n"], KEYS[q["ans"]], q["kind"], q["topic"]) for q in Q)

    traps = "".join('<li><span class="t">%s</span><span class="jump">→ Q%d</span>'
                    '<p class="d">%s</p></li>' % (t, n, d) for t, d, n in TRAPS)

    cover = """
<section class="cover">
  <p class="eyebrow">CM 5174 · 期末复习</p>
  <h1>高分子物理化学<br>模拟题库 30 题</h1>
  <p class="tagline">题干英文 · 解析中文 · 答案与分步解析直接印在每题下方</p>
  <div class="meta">
    <b>课程</b>　CM5174 Polymer and Macromolecular Chemistry，NUS<br>
    <b>依据</b>　Lecture 1–10 全部讲义，以及课程发布的 28 道 Question 及其答案<br>
    <b>题型</b>　计算 18 · 理解 10 · 跨讲综合 2<br>
    <b>核算</b>　每道计算题的数值都用脚本重算过<br>
    <b>用法</b>　答案就在题目下面，建议先拿纸盖住解析区自己算完再看。<br>
    　　　　常数：R = 8.314 J K⁻¹ mol⁻¹　k = 1.381×10⁻²³ J K⁻¹　N<sub>Av</sub> = 6.022×10²³ mol⁻¹　g = 9.81 m s⁻²
  </div>
  <div class="toc">
    <h2>按讲次分布</h2>
    <ol>
      <li><span class="k">L1</span>尺寸与构象　Q1–3</li>
      <li><span class="k">L2</span>混合热力学　Q4–6</li>
      <li><span class="k">L3</span>Flory-Huggins　Q7–9</li>
      <li><span class="k">L4</span>相行为　Q10–13</li>
      <li><span class="k">L5</span>渗透压与粘度　Q14–16</li>
      <li><span class="k">L6</span>光散射　Q17–18</li>
      <li><span class="k">L7</span>SEC 与质谱　Q19–21</li>
      <li><span class="k">—</span>表征方法综合　Q22</li>
      <li><span class="k">L8</span>玻璃态　Q23–25</li>
      <li><span class="k">L9</span>力学性质　Q26</li>
      <li><span class="k">L10</span>弹性体与结晶　Q27–29</li>
      <li><span class="k">—</span>跨讲综合　Q30</li>
    </ol>
  </div>
</section>"""

    sheet = ('<section class="sheet"><h2>答案速查表</h2>'
      '<table class="keytab"><thead><tr><th style="width:10%">题号</th>'
      '<th style="width:10%">答案</th><th style="width:14%">类型</th><th>考点</th></tr></thead>'
      '<tbody>' + keyrows + '</tbody></table>'
      '<h3>考前最后一小时：八个必记陷阱</h3><ol class="traps">' + traps + '</ol>'
      '<p style="margin-top:4mm;font-size:9.2pt;color:#5A6875">'
      '<b>其余高频：</b>t \u221d \u221am（不是 m）\u3000·\u3000I \u221d \u03bb\u207b\u2074（四次方）'
      '\u3000·\u3000a = 3\u03bd \u2212 1\u3000·\u3000'
      'R<sub>g</sub>\u00b2 = Nb\u00b2/6\u3000·\u30001 mm\u00b2 = 10\u207b\u2076 m\u00b2</p></section>')

    body = cover + '<h2>题目 · 答案 · 解析</h2>' + "".join(qs) + sheet

    out = OUT / "bank.html"
    out.write_text(page("CM5174 模拟题库 30 题", body), encoding="utf-8")
    return out

if __name__ == "__main__":
    print(build_notes()); print(build_bank())
