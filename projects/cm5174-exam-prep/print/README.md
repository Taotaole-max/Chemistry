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
