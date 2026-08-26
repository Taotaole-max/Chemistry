# -*- coding: utf-8 -*-
import sys, pathlib, collections
sys.path.insert(0, '/home/user/Chemistry/projects/cm5174-exam-prep/bank')
sys.path.insert(0, '/home/user/Chemistry/projects/cm5174-exam-prep/print')
import json, pathlib
Q = json.loads(pathlib.Path("/home/user/Chemistry/projects/cm5174-exam-prep/bank/bank_all.json").read_text(encoding="utf-8"))
from pdfbuild import CSS          # 复用已调好的 A4 打印样式

OUT = pathlib.Path("/home/user/Chemistry/projects/cm5174-exam-prep/print")
KEYS = ["A", "B", "C", "D"]

EXTRA = """
.lec-head{break-before:page; margin:0 0 4mm}
.lec-head .n{font-size:9pt; letter-spacing:.2em; color:#1F4E8C; font-weight:700; margin:0 0 1mm}
.lec-head h2{font-size:16pt; border-bottom:2pt solid #1F4E8C; padding-bottom:2mm; margin:0}
.lec-head .en{font-size:9.5pt; color:#5A6875; margin:1.5mm 0 0}
.lec-head .meta{font-size:8.6pt; color:#8A97A4; margin:1mm 0 0}
.q-kp,.q-src{
  display:flex; gap:2.2mm; font-size:8.8pt; margin:1.4mm 0 0; line-height:1.5;
  padding-top:1.4mm; border-top:.4pt dotted #C9D3DD;
}
.q-kp .lb,.q-src .lb{
  flex:none; font-size:7.6pt; font-weight:700; letter-spacing:.06em; padding:.4mm 1.6mm;
  border-radius:.9mm; height:fit-content; white-space:nowrap;
}
.q-kp .lb{background:#E7EEF7; color:#1F4E8C}
.q-src .lb{background:#EDEFF2; color:#5A6875}
.q-kp .tx{color:#33424F}
.q-src .tx{color:#5A6875}
.toc-lec{list-style:none; padding:0; margin:0; font-size:9.6pt; columns:2; column-gap:9mm}
.toc-lec li{margin:0 0 1.8mm; break-inside:avoid; display:flex; gap:2.5mm}
.toc-lec .k{font-family:"Noto Sans Mono CJK SC",monospace; font-weight:700; color:#1F4E8C;
  font-size:8.8pt; flex:none; min-width:9mm}
.toc-lec .r{margin-left:auto; font-family:"Noto Sans Mono CJK SC",monospace;
  font-size:8.6pt; color:#8A97A4; flex:none}
"""

def card(q):
    opts = "".join(
        '<li class="%s"><span class="k">%s</span><span>%s</span>%s</li>' % (
            "right" if i == q["ans"] else "", KEYS[i], o,
            '<span class="tick">✓</span>' if i == q["ans"] else "")
        for i, o in enumerate(q["opts"]))
    return (
      '<article class="q"><div class="q-top"><div class="q-h">'
      '<span class="q-n">%03d</span><span>L%d</span>'
      '<span class="q-k">%s</span><span class="q-t">%s</span></div>'
      '<p class="q-s">%s</p><ul class="q-o">%s</ul></div>'
      '<div class="q-a"><p class="lab">答案 <span class="ans">%s</span>　·　解析</p>%s'
      '<div class="q-kp"><span class="lb">知识点</span><span class="tx">%s</span></div>'
      '<div class="q-src"><span class="lb">出处</span><span class="tx">%s · %s</span></div>'
      '</div></article>'
      % (q["n"], q["lec"], q["kind"], q["topic"], q["stem"], opts,
         KEYS[q["ans"]], q["exp"], q["kp"], q["srcfile"], q["src"]))

by_lec = collections.OrderedDict()
for q in Q:
    by_lec.setdefault(q["lec"], []).append(q)

toc = "".join(
    '<li><span class="k">L%d</span><span>%s</span><span class="r">%03d–%03d</span></li>'
    % (l, qs[0]["leccn"], qs[0]["n"], qs[-1]["n"]) for l, qs in by_lec.items())

kinds = collections.Counter(q["kind"] for q in Q)
cover = """
<section class="cover">
  <p class="eyebrow">CM 5174 · 分讲题库</p>
  <h1>高分子物理化学<br>分讲题库 %d 题</h1>
  <p class="tagline">每讲 30 题以上 · 题目 / 答案 / 解析 / 知识点 / 出处 五要素齐全</p>
  <div class="meta">
    <b>课程</b>　CM5174 Polymer and Macromolecular Chemistry，NUS · Assoc. Prof. Tan Zhi Kuang<br>
    <b>依据</b>　Lecture 1–10 全部讲义原文，以及课程发布的 28 道 Question 及其答案<br>
    <b>题型</b>　理解 %d · 计算 %d<br>
    <b>出处</b>　每题都标到<b>具体讲义页码与页标题</b>，可直接翻回原文核对<br>
    <b>核对</b>　答案在 A/B/C/D 四个位置均衡分布（各约 25%%），不能靠蒙<br>
    <b>用法</b>　答案就印在题目下方，建议用纸盖住解析区先自己做<br>
    　　　　常数：R = 8.314 J K⁻¹ mol⁻¹　k = 1.381×10⁻²³ J K⁻¹　N<sub>Av</sub> = 6.022×10²³ mol⁻¹　g = 9.81 m s⁻²
  </div>
  <div class="toc"><h2>分讲目录</h2><ul class="toc-lec">%s</ul></div>
</section>""" % (len(Q), kinds["理解"], kinds["计算"], toc)

body = [cover]
for l, qs in by_lec.items():
    body.append('<section class="lec-head"><p class="n">LECTURE %d</p>'
                '<h2>%s</h2><p class="en">%s</p>'
                '<p class="meta">%d 题（%03d–%03d）　·　%s</p></section>'
                % (l, qs[0]["leccn"], qs[0]["lectitle"], len(qs),
                   qs[0]["n"], qs[-1]["n"], qs[0]["srcfile"]))
    body += [card(q) for q in qs]

# 分讲答案速查表
body.append('<section class="sheet"><h2>答案速查表</h2>')
for l, qs in by_lec.items():
    rows = "".join('<tr><td class="n">%03d</td><td class="a">%s</td>'
                   '<td class="n">%s</td><td>%s</td></tr>'
                   % (q["n"], KEYS[q["ans"]], q["kind"], q["topic"]) for q in qs)
    body.append('<h3>Lecture %d · %s</h3><table class="keytab"><thead><tr>'
                '<th style="width:10%%">题号</th><th style="width:10%%">答案</th>'
                '<th style="width:14%%">类型</th><th>考点</th></tr></thead>'
                '<tbody>%s</tbody></table>' % (l, qs[0]["leccn"], rows))
body.append('</section>')

html = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<title>CM5174 分讲题库</title><style>%s\n%s</style></head><body>%s</body></html>'
        % (CSS, EXTRA, "".join(body)))
(OUT / "bank_all.html").write_text(html, encoding="utf-8")
print("written", OUT / "bank_all.html", len(html), "bytes")
