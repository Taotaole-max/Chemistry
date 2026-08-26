# -*- coding: utf-8 -*-
"""由 03_知识点总结_完整版.md 生成打印版 HTML。"""
import sys, pathlib, re
BASE = pathlib.Path("/home/user/Chemistry/projects/cm5174-exam-prep")
sys.path.insert(0, str(BASE / "print"))
from pdfbuild import md2html, CSS

EXTRA = """
h1.bigsec{font-size:19pt; border-bottom:2.2pt solid #1F4E8C; padding-bottom:2.5mm; margin:0 0 5mm}
h1.bigsec + blockquote{margin-top:0}
blockquote{break-inside:avoid}
table td, table th{font-size:8.9pt}
"""

COVER = """
<section class="cover">
  <p class="eyebrow">CM 5174 · 期末复习</p>
  <h1>高分子物理化学<br>知识点总结（完整版）</h1>
  <p class="tagline">Lecture 1–10 全章节 · 公式速查 · 跨讲串联</p>
  <div class="meta">
    <b>课程</b>　CM5174 Polymer and Macromolecular Chemistry，NUS · Assoc. Prof. Tan Zhi Kuang<br>
    <b>依据</b>　Lecture 1–10 全部讲义原文<br>
    <b>出处</b>　每讲标注对应的讲义文件与页码范围，可直接翻回原文核对<br>
    <b>三部分</b>　① <b>公式速查表</b>——按讲次汇总全部公式，考前最后一遍看这个<br>
    　　　　　② <b>十讲正文</b>——保留推导脉络，标出讲义原文结论与常见误解<br>
    　　　　　③ <b>跨讲串联</b>——12 条贯穿多讲的主线，综合题几乎全出自这里
  </div>
  <div class="toc">
    <h2>目录</h2>
    <ol>
      <li><span class="k">速查</span>公式速查表</li>
      <li><span class="k">L1</span>高分子尺寸与构象</li>
      <li><span class="k">L2</span>混合热力学</li>
      <li><span class="k">L3</span>Flory-Huggins 溶液理论</li>
      <li><span class="k">L4</span>相行为</li>
      <li><span class="k">L5</span>渗透压与粘度法</li>
      <li><span class="k">L6</span>光散射与动态光散射</li>
      <li><span class="k">L7</span>SEC 与质谱</li>
      <li><span class="k">L8</span>玻璃态</li>
      <li><span class="k">L9</span>力学性质与加工</li>
      <li><span class="k">L10</span>弹性态与结晶态</li>
      <li><span class="k">串联</span>跨讲串联 12 条</li>
    </ol>
  </div>
</section>"""

html = md2html(BASE / "03_知识点总结_完整版.md")
html = re.sub(r'^.*?<h2>全局地图</h2>', '<h2>全局地图</h2>', html, flags=re.S)
html = re.sub(r'<h2>(Lecture \d+)', r'<h2 class="lec-break">\1', html)
html = html.replace('<h1>公式速查表</h1>', '<h1 class="lec-break bigsec">公式速查表</h1>')
html = html.replace('<h1>跨讲串联</h1>',   '<h1 class="lec-break bigsec">跨讲串联</h1>')

page = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<title>CM5174 知识点总结</title><style>%s\n%s</style></head><body>%s%s</body></html>'
        % (CSS, EXTRA, COVER, html))
out = BASE / "print" / "notes_full.html"
out.write_text(page, encoding="utf-8")
print("written", out, len(page), "bytes")
