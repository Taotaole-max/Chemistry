# -*- coding: utf-8 -*-
import sys, json, pathlib, collections
BASE = pathlib.Path("/home/user/Chemistry/projects/cm5174-exam-prep")
sys.path.insert(0, str(BASE / "print"))
from pdfbuild import CSS
Q = json.loads((BASE / "bank" / "hard_all.json").read_text(encoding="utf-8"))
KEYS = ["A", "B", "C", "D"]

KINDS = [("链式","多步链式计算","把 2–4 个概念串起来，任何一步跳过都得不到答案"),
         ("逆向","逆向求解","给结果反推输入；指数、系数都要反着用"),
         ("判别","判别与证伪","哪条结论站不住 / 从数据能推出什么、不能推出什么"),
         ("标度","数量级与标度推理","幂律的指数差如何放大成数量级差异"),
         ("设计","实验设计与方法选择","给定目标与样品限制，选出可行方案"),
         ("综合","跨讲综合","一条主线贯穿多讲，认出它才能作答"),
         ("陷阱","陷阱换皮","同一个坑换个场景，还认得出来吗")]

EXTRA = """
.kind-head{break-before:page; margin:0 0 4mm}
.kind-head .n{font-size:9pt; letter-spacing:.2em; color:#1F4E8C; font-weight:700; margin:0 0 1mm}
.kind-head h2{font-size:16pt; border-bottom:2pt solid #1F4E8C; padding-bottom:2mm; margin:0}
.kind-head .en{font-size:9.5pt; color:#5A6875; margin:1.5mm 0 0}
.q-kp,.q-src{display:flex; gap:2.2mm; font-size:8.8pt; margin:1.4mm 0 0; line-height:1.5;
  padding-top:1.4mm; border-top:.4pt dotted #C9D3DD;}
.q-kp .lb,.q-src .lb{flex:none; font-size:7.6pt; font-weight:700; letter-spacing:.06em;
  padding:.4mm 1.6mm; border-radius:.9mm; height:fit-content; white-space:nowrap;}
.q-kp .lb{background:#E7EEF7; color:#1F4E8C}
.q-src .lb{background:#EDEFF2; color:#5A6875}
.q-kp .tx{color:#33424F} .q-src .tx{color:#5A6875}
.q-k{background:#F3E8DC; color:#8A5A12; border-color:#D9BE97}
.toc-k{list-style:none; padding:0; margin:0; font-size:9.6pt}
.toc-k li{margin:0 0 2mm; display:flex; gap:3mm; break-inside:avoid}
.toc-k .k{font-weight:700; color:#1F4E8C; flex:none; min-width:22mm}
.toc-k .d{color:#5A6875; font-size:9pt}
.toc-k .r{margin-left:auto; font-family:"Noto Sans Mono CJK SC",monospace; font-size:8.6pt; color:#8A97A4; flex:none}
"""

def card(q):
    opts = "".join('<li class="%s"><span class="k">%s</span><span>%s</span>%s</li>'
        % ("right" if i == q["ans"] else "", KEYS[i], o,
           '<span class="tick">✓</span>' if i == q["ans"] else "")
        for i, o in enumerate(q["opts"]))
    return ('<article class="q"><div class="q-top"><div class="q-h">'
      '<span class="q-n">H%02d</span><span>%s</span><span class="q-k">%s</span>'
      '<span class="q-t">%s</span></div><p class="q-s">%s</p><ul class="q-o">%s</ul></div>'
      '<div class="q-a"><p class="lab">答案 <span class="ans">%s</span>　·　解析</p>%s'
      '<div class="q-kp"><span class="lb">知识点</span><span class="tx">%s</span></div>'
      '<div class="q-src"><span class="lb">出处</span><span class="tx">%s</span></div>'
      '</div></article>' % (q["n"], q["tag"], q["kind"], q["topic"], q["stem"], opts,
                            KEYS[q["ans"]], q["exp"], q["kp"], q["src"]))

by = collections.OrderedDict((k, [q for q in Q if q["kind"] == k]) for k, _, _ in KINDS)
toc = "".join('<li><span class="k">%s</span><span class="d">%s</span>'
              '<span class="r">%d 题</span></li>' % (cn, desc, len(by[k]))
              for k, cn, desc in KINDS)

cover = """
<section class="cover">
  <p class="eyebrow">CM 5174 · 进阶</p>
  <h1>高分子物理化学<br>进阶应用题 %d 题</h1>
  <p class="tagline">多步推理 · 逆向求解 · 跨讲综合 · 强调运用</p>
  <div class="meta">
    <b>定位</b>　这份不是知识点复述题，每一道都要求<b>把知识用起来</b>：
    多步串联、反着推、判断哪条站不住、或认出跨讲的同一条主线。<br>
    <b>与前两份的关系</b>　先做完《分讲题库 301 题》打牢基础，再来做这份。<br>
    <b>核算</b>　每道计算题的数值都用脚本重算过；答案在 A/B/C/D 均衡分布。<br>
    <b>用法</b>　答案与解析印在题下。<b>建议先用纸盖住，限时 3 分钟一题</b>——
    这类题的难点不在算，在<b>想清楚该用哪几个公式、按什么顺序</b>。<br>
    　　　　常数：R = 8.314 J K⁻¹ mol⁻¹　k = 1.381×10⁻²³ J K⁻¹　N<sub>Av</sub> = 6.022×10²³ mol⁻¹　g = 9.81 m s⁻²
  </div>
  <div class="toc"><h2>七类题型</h2><ul class="toc-k">%s</ul></div>
</section>""" % (len(Q), toc)

body = [cover]
for k, cn, desc in KINDS:
    body.append('<section class="kind-head"><p class="n">%s</p><h2>%s</h2>'
                '<p class="en">%s　·　共 %d 题</p></section>' % (k, cn, desc, len(by[k])))
    body += [card(q) for q in by[k]]

rows = "".join('<tr><td class="n">H%02d</td><td class="a">%s</td><td class="n">%s</td>'
               '<td class="n">%s</td><td>%s</td></tr>'
               % (q["n"], KEYS[q["ans"]], q["kind"], q["tag"], q["topic"]) for q in Q)
body.append('<section class="sheet"><h2>答案速查表</h2><table class="keytab"><thead><tr>'
            '<th style="width:9%">题号</th><th style="width:9%">答案</th><th style="width:12%">类型</th>'
            '<th style="width:14%">涉及讲次</th><th>考点</th></tr></thead><tbody>'
            + rows + '</tbody></table></section>')

html = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<title>CM5174 进阶应用题</title><style>%s\n%s</style></head><body>%s</body></html>'
        % (CSS, EXTRA, "".join(body)))
(BASE / "print" / "hard.html").write_text(html, encoding="utf-8")
print("written", len(html), "bytes")
