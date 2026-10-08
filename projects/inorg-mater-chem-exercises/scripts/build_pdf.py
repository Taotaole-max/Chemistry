# 把 content/*.txt（紧凑标记）转成 HTML，再用无头 Chromium 打印成 PDF
#
# 标记约定（每行开头）：
#   # A2 | 标题            —— 一个 Part 的开始
#   >>> 说明文字           —— Part 开头的导读（可多行）
#   @@ 1 | 英文原题         —— 一道题开始（可续行）
#   %% skip               —— 该题 2026 年标注“跳过”
#   ?? 中文题意
#   >> 答案
#   !! 文件名.png | 图注
#   ## 解析
#   ** 考点 / 易错
# 块内：空行分段；"- " 开头为列表；"| a | b |" 为表格（第一行表头）。
# 行内：[[Fe2O3]]、[[SO4^2-]]、[[Na_{1-2x}]] 自动排化学式；KV(V,Na,') 为 Kröger–Vink 记号。
import html
from PIL import Image
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
FIGS = os.path.join(ROOT, "figs")
PARTS = ["A2", "A3", "B2", "B3", "B4", "B5"]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def chem(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "^":
            j = i + 1
            if j < len(s) and s[j] == "{":
                k = s.index("}", j)
                sup = s[j + 1:k]; i = k + 1
            else:
                k = j
                while k < len(s) and s[k] not in " ,;)]":
                    k += 1
                sup = s[j:k]; i = k
            sup = sup.replace("-", "−")
            out.append(f"<sup>{sup}</sup>")
            continue
        if c == "_":
            j = i + 1
            if s[j] == "{":
                k = s.index("}", j)
                out.append(f"<sub>{s[j + 1:k].replace('-', '−')}</sub>"); i = k + 1
            else:
                out.append(f"<sub>{s[j]}</sub>"); i = j + 1
            continue
        if c.isdigit() and out and (out[-1][-1:].isalpha() or out[-1][-1:] in ")]") and not out[-1].endswith(">"):
            j = i
            while j < len(s) and (s[j].isdigit() or (s[j] == "." and j + 1 < len(s) and s[j + 1].isdigit())):
                j += 1
            out.append(f"<sub>{s[i:j]}</sub>"); i = j
            continue
        out.append(c)
        i += 1
    return "".join(out)


KV_CHARGE = {"'": "′", "''": "″", ".": "•", "..": "••", "x": "×"}


def inline(t):
    t = re.sub(r"\[\[(.+?)\]\]", lambda m: chem(m.group(1)), t)
    t = re.sub(r"KV\(([^,]+),([^,]+),([^)]+)\)",
               lambda m: f'<span class="kv">{m.group(1)}<span class="ss"><sup>{KV_CHARGE.get(m.group(3), m.group(3))}</sup>'
                         f'<sub>{m.group(2)}</sub></span></span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"==(.+?)==", r'<mark>\1</mark>', t)
    return t


def block_html(lines):
    """段落 / 列表 / 表格。"""
    out, para, items, rows = [], [], [], []

    def flush():
        nonlocal para, items, rows
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); items = []
        if rows:
            h = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f'<table>{h}{b}</table>'); rows = []

    for ln in lines:
        s = ln.rstrip()
        if not s.strip():
            flush(); continue
        if s.lstrip().startswith("- "):
            if para or rows:
                tmp_items = items; items = []; flush(); items = tmp_items
            items.append(s.lstrip()[2:])
        elif s.strip().startswith("|"):
            if para or items:
                tmp = rows; rows = []; flush(); rows = tmp
            rows.append([c.strip() for c in s.strip().strip("|").split("|")])
        else:
            if items and s.startswith("  "):
                items[-1] += " " + s.strip(); continue
            if items or rows:
                flush()
            para.append(s.strip())
    flush()
    return "\n".join(out)


def parse(path):
    part = None
    qs = []
    cur = None
    key = None
    for raw in open(path, encoding="utf-8").read().split("\n"):
        m = re.match(r"^(##|#|>>>|>>|@@|%%|\?\?|!!|\*\*)\s?(.*)$", raw)
        if m and not (m.group(1) == "**" and raw.startswith("**") and raw[2:3] not in (" ", "")):
            tag, rest = m.group(1), m.group(2)
            if tag == "#":
                pid, title = [x.strip() for x in rest.split("|", 1)]
                part = {"id": pid, "title": title, "intro": []}
                key = "intro"; cur = None
                continue
            if tag == ">>>":
                part["intro"].append(rest); key = "intro"; cur = None; continue
            if tag == "@@":
                num, q = [x.strip() for x in rest.split("|", 1)]
                cur = {"num": num, "q": [q], "zh": [], "ans": [], "figs": [], "exp": [], "tip": [], "skip": False, "order": []}
                qs.append(cur); key = "q"; continue
            if tag == "%%":
                cur["skip"] = True; continue
            if tag == "!!":
                f, cap = [x.strip() for x in rest.split("|", 1)]
                cur["figs"].append((f, cap)); cur["order"].append(("fig", len(cur["figs"]) - 1)); key = None; continue
            key = {"??": "zh", ">>": "ans", "##": "exp", "**": "tip"}[tag]
            cur[key].append(rest)
            if (key, None) not in cur["order"]:
                cur["order"].append((key, None))
            continue
        if cur is None:
            if key == "intro" and part:
                part["intro"].append(raw)
            continue
        if key:
            cur[key].append(raw)
    return part, qs


LABEL = {"ans": ("答案", "ans"), "exp": ("解析", "exp"), "tip": ("考点 / 易错", "tip")}


def render_q(pid, q, fig_counter):
    sid = f"{pid}-{q['num']}"
    skip = '<span class="skip">2026 不考（讲义标注 skip）</span>' if q["skip"] else ""
    h = [f'<section class="q" id="{sid}">',
         f'<div class="qhead"><span class="qn">{pid}.{q["num"]}</span>{skip}'
         f'<div class="qen">{inline(" ".join(x.strip() for x in q["q"] if x.strip()))}</div>',
         f'<div class="qzh">题意：{inline(" ".join(x.strip() for x in q["zh"] if x.strip()))}</div></div>']
    for kind, idx in q["order"]:
        if kind == "zh":
            continue
        if kind == "fig":
            f, cap = q["figs"][idx]
            fig_counter[0] += 1
            try:
                wpx = Image.open(os.path.join(FIGS, f)).size[0]
            except Exception:
                wpx = 2400
            wmm = min(184, wpx / 170 * 13.2)
            h.append(f'<figure><img src="../figs/{f}" style="width:{wmm:.0f}mm"><figcaption>图 {pid}.{q["num"]}{"" if len(q["figs"]) == 1 else chr(96 + idx + 1)}　{inline(cap)}</figcaption></figure>')
            if not os.path.exists(os.path.join(FIGS, f)):
                print("缺图:", f, file=sys.stderr)
        else:
            lab, cls = LABEL[kind]
            h.append(f'<div class="box {cls}"><div class="t">{lab}</div>{block_html(q[kind])}</div>')
    h.append("</section>")
    return "\n".join(h)


CSS = """
@page { size: A4; margin: 14mm 13mm 16mm 13mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-size: 9pt; color: #777; } }
:root { --blue:#3b6fb6; --red:#c8453a; --green:#3f9a5a; --orange:#e08a2c; --ink:#22262c; }
html { font-family: "Liberation Sans", "WenQuanYi Zen Hei", sans-serif; color: var(--ink); font-size: 10.6pt; line-height: 1.6; }
body { margin: 0; background: white; }
h1.part { font-size: 19pt; color: white; background: var(--blue); padding: 8px 14px; border-radius: 6px; margin: 0 0 10px 0; break-before: page; }
.intro { background:#f4f7fc; border-left: 4px solid var(--blue); padding: 6px 12px; margin-bottom: 14px; font-size: 10pt; }
.q { margin: 0 0 18px 0; }
.qhead { background: #eef3fb; border: 1px solid #c8d6ee; border-radius: 6px; padding: 8px 12px; margin-bottom: 8px; break-inside: avoid; break-after: avoid; }
.qn { display:inline-block; background: var(--blue); color:white; font-weight:bold; border-radius:4px; padding:0 8px; margin-right:8px; }
.skip { display:inline-block; background:#fff3e0; color:#b45f06; border:1px solid #f0b46a; border-radius:4px; padding:0 6px; font-size:9pt; }
.qen { font-style: italic; margin-top: 4px; }
.qzh { color:#444; margin-top: 3px; }
.box { border-radius: 6px; padding: 6px 12px; margin: 8px 0; }
.box > .t { font-weight: bold; margin-bottom: 2px; break-after: avoid; }
.box.ans { background: #f2fbf4; border: 1px solid #b9dfc3; }
.box.ans > .t { color: var(--green); }
.box.exp { background: #ffffff; border: 1px solid #ddd; }
.box.exp > .t { color: var(--blue); }
.box.tip { background: #fff8ec; border: 1px solid #f2d3a2; }
.box.tip > .t { color: #b45f06; }
.box p { margin: 4px 0; }
.box ul { margin: 3px 0 3px 0; padding-left: 20px; }
.box li { margin: 1px 0; }
figure { margin: 8px 0; text-align: center; break-inside: avoid; }
figure img { max-width: 100%; max-height: 225mm; }
figcaption { font-size: 9pt; color: #555; margin-top: 3px; }
table { border-collapse: collapse; margin: 6px 0; font-size: 9.6pt; width: 100%; }
th, td { border: 1px solid #ccd; padding: 3px 6px; vertical-align: top; }
th { background: #eef3fb; }
td:first-child, th:first-child { min-width: 4.6em; }
tr { break-inside: avoid; }
sub, sup { font-size: 72%; line-height: 0; }
.kv { white-space: nowrap; }
.kv .ss { display: inline-flex; flex-direction: column; vertical-align: middle; font-size: 68%; line-height: 1.05; margin-left: 1px; }
.kv .ss sup, .kv .ss sub { font-size: 100%; line-height: 1.05; vertical-align: baseline; }
mark { background: #fff2a8; padding: 0 2px; }
.cover { padding-top: 18mm; }
.cover h1 { font-size: 26pt; color: var(--blue); margin: 0 0 8px 0; }
.cover h2 { font-size: 15pt; color: #555; font-weight: normal; margin: 0 0 24px 0; }
.toc { columns: 2; font-size: 9.8pt; }
.toc a { color: var(--ink); text-decoration: none; }
.toc div { break-inside: avoid; margin: 1px 0; }
.toc .tp { font-weight: bold; color: var(--blue); margin-top: 6px; }
.note { font-size: 9.8pt; color: #555; border-top: 1px solid #ddd; padding-top: 8px; margin-top: 18px; }
"""


def main():
    global PARTS
    if len(sys.argv) > 1:
        PARTS = sys.argv[1:]
    body = []
    toc = []
    fig_counter = [0]
    nq = 0
    for pid in PARTS:
        part, qs = parse(os.path.join(CONTENT, f"{pid}.txt"))
        toc.append(f'<div class="tp">{pid}　{html.escape(part["title"])}</div>')
        body.append(f'<h1 class="part" id="{pid}">Part {pid}　{inline(part["title"])}</h1>')
        intro = "\n".join(part["intro"]).strip()
        if intro:
            body.append(f'<div class="intro">{block_html(intro.split(chr(10)))}</div>')
        for q in qs:
            nq += 1
            en = re.sub(r"<[^>]+>", "", inline(" ".join(q["q"])))
            en = re.sub(r"\[\[|\]\]", "", en)
            toc.append(f'<div><a href="#{pid}-{q["num"]}">{pid}.{q["num"]}　{html.escape(en[:58])}{"…" if len(en) > 58 else ""}'
                       f'{"（2026 不考）" if q["skip"] else ""}</a></div>')
            body.append(render_q(pid, q, fig_counter))
    cover = (f'<div class="cover"><h1>无机材料化学 练习题<br>详细答案与解析</h1>'
             f'<h2>Inorganic Materials Chemistry — Exercises A2, A3, B2, B3, B4, B5</h2>'
             f'<div class="toc">{"".join(toc)}</div>'
             f'<div class="note">共 {nq} 题、{fig_counter[0]} 张配图。每题结构：英文原题 → 题意 → <b style="color:#3f9a5a">答案</b>（考试可直接写的要点）'
             f' → 配图 → <b style="color:#3b6fb6">解析</b>（为什么） → <b style="color:#b45f06">考点/易错</b>。'
             f'讲义标注 2026 年跳过的 A3.2、A3.3、A3.5、B4.8–B4.10 也给了答案，并在题号旁标出。'
             f'图中热力学数据为标准值或示意近似值，已在图注中说明。</div></div>')
    doc = (f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>无机材料化学练习答案</title>'
           f'<style>{CSS}</style></head><body>{cover}{"".join(body)}</body></html>')
    out_dir = os.path.join(ROOT, "build")
    os.makedirs(out_dir, exist_ok=True)
    hp = os.path.join(out_dir, "inorg_mater_chem_A2-B5_answers.html")
    open(hp, "w", encoding="utf-8").write(doc)
    pdf = os.path.join(ROOT, "无机材料化学_A2-B5_练习详细答案与解析.pdf")
    cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
           "--allow-file-access-from-files", f"--print-to-pdf={pdf}", "file://" + hp]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(r.stderr[-800:] if r.returncode else "", "题数", nq, "图数", fig_counter[0])
    print("PDF:", pdf, os.path.getsize(pdf) // 1024, "KB")


if __name__ == "__main__":
    main()
