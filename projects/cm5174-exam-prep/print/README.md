# PDF 生成

两份 PDF 由脚本从源文件生成，改内容后重跑即可。

| 文件 | 作用 |
|---|---|
| `tex.py` | LaTeX 子集 → HTML 转换器（分式真正上下堆叠、根号、装框公式） |
| `data.py` | 30 道题的结构化数据（题干、选项、答案、解析） |
| `pdfbuild.py` | markdown / 题目数据 → 打印版 HTML（A4 版式、分页控制） |

```bash
pip install pymupdf markdown playwright
apt-get install -y fonts-noto-cjk      # 缺 CJK 字体中文会变方块
python3 pdfbuild.py                    # 生成 notes.html / bank.html
python3 topdf.py                       # Chromium 渲染成 PDF
```

`topdf.py` 用 Playwright 的 `page.pdf()`，带页眉页码。

## 版式上的两个决定

- **知识点**：每个 Lecture `break-before:page`，从新页开始，方便按讲复习
- **题库**：卡片允许跨页，但 `.q-top`（题干 + 选项）锁成整块不拆。
  最初整张卡片 `break-inside:avoid`，导致一页只放得下一道题、31 页里全是空白；
  改成现在这样压到 21 页

## 分讲题库（301 题）

| 文件 | 作用 |
|---|---|
| `../bank/L01.py` … `L10.py` | 每讲的题目源数据，各 30 题以上 |
| `../bank/normalize.py` | 合并十讲 → `bank_all.json`，并做两件事（见下） |
| `bank_pdf.py` | 由 `bank_all.json` 生成 184 页打印版 HTML |

```bash
cd bank && python3 normalize.py          # 生成 bank_all.json
cd .. && python3 print/bank_pdf.py       # 生成 bank_all.html
python3 topdf2.py                        # 渲染成 PDF
```

### normalize.py 解决的两个质量问题

出题时无意中埋了两个坑，全局质检才发现：

1. **只给正确选项加了 `<b>`** ——301 题里有 200 题如此，等于把答案印在题面上。
   normalize 统一剥掉选项里的加粗。
2. **答案分布严重失衡** ——原始分布 A/B/C/D = 60/147/76/18，蒙 B 能得 49%。
   normalize 把正确项挪到当前用得最少的位置，重新平衡到 76/75/75/75。

**但不能无脑打乱**：有 34 题的解析里写了「选项 A 是…」「选项 C 就是这个陷阱」这类引用，
打乱会让解析对不上。normalize 用正则 `选项\s*([ABCD])` 识别这些题并**跳过**，
只重排其余 267 题，最后断言锁定题的选项与答案未被改动。

### 每题的五要素

题目 / 答案 / 解析 / **知识点** / **出处**。出处精确到讲义页码与页标题
（如「讲义 Lectures_1-4 · p.6「Molecular Weight of Polymers」」），可直接翻回原文核对。
页码索引由 PyMuPDF 逐页提取标题建立，不是凭印象写的。
