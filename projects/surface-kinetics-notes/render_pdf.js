// 拼接 HTML 片段 → MathJax 服务端渲染成 SVG → Chromium 打印 PDF
// 用法：node render_pdf.js 输出.pdf
const fs = require('fs');
const path = require('path');

const parts = ['head.html', 'part1.html', 'part2.html', 'part2b.html', 'part3.html', 'part4.html', 'part5.html', 'tail.html'];
let html = parts.filter(p => fs.existsSync(p)).map(p => fs.readFileSync(p, 'utf8')).join('\n');

require('mathjax').init({
  loader: { load: ['input/tex', 'output/svg'] },
  tex: { packages: { '[+]': [] } },
  svg: { fontCache: 'local' },
}).then(async (MathJax) => {
  const ad = MathJax.startup.adaptor;
  const conv = (tex, display) => ad.outerHTML(MathJax.tex2svg(tex, { display }));
  let n = 0;
  html = html.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => { n++; return conv(t.trim(), true); });
  html = html.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => { n++; return conv(t.trim(), false); });
  const css = ad.textContent(MathJax.svgStylesheet());
  html = html.replace('</head>', `<style>${css}</style></head>`);
  fs.writeFileSync('final.html', html);
  console.log('公式数', n);

  const { chromium } = require('playwright-core');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve('final.html'), { waitUntil: 'networkidle' });
  await page.pdf({
    path: process.argv[2] || 'out.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '14mm', bottom: '16mm', left: '13mm', right: '13mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#888;text-align:center;">表面吸附与表面反应动力学 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });
  await browser.close();
  console.log('PDF 完成');
});
