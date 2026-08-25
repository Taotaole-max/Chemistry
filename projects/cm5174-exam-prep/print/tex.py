# -*- coding: utf-8 -*-
"""把讲义里用到的 LaTeX 子集转成 HTML（分式真正上下堆叠）。"""
import html as H

SYM = {
 'Delta':'Δ','Omega':'Ω','alpha':'α','beta':'β','gamma':'γ','chi':'χ','phi':'φ','varphi':'φ',
 'mu':'μ','eta':'η','sigma':'σ','varepsilon':'ε','epsilon':'ε','theta':'θ','nu':'ν','pi':'π',
 'lambda':'λ','rho':'ρ','tau':'τ','zeta':'ζ','psi':'ψ','omega':'ω','Pi':'Π','Sigma':'Σ',
 'infty':'∞','partial':'∂','propto':'∝','approx':'≈','neq':'≠','le':'≤','leq':'≤','ge':'≥','geq':'≥',
 'Rightarrow':'⇒','rightarrow':'→','to':'→','Leftrightarrow':'⇔','leftrightarrow':'↔',
 'cdot':'·','times':'×','pm':'±','div':'÷','ll':'≪','gg':'≫','sim':'∼','equiv':'≡',
 'sum':'Σ','int':'∫','prod':'∏','in':'∈','circ':'°','ldots':'…','cdots':'⋯','dots':'…',
 'langle':'⟨','rangle':'⟩','lvert':'|','rvert':'|','perp':'⊥','nabla':'∇',
 'ln':'ln','log':'log','cos':'cos','sin':'sin','tan':'tan','exp':'exp','max':'max','min':'min','lim':'lim',
 'quad':' ','qquad':'  ',';':' ',',':' ','!':'',':':' ',
 '%':'%','&':'&amp;','#':'#','$':'$','_':'_','{':'{','}':'}',
}
PLAIN = {'text','mathrm','mathbf','textbf','mathit','operatorname','left','right','displaystyle','limits','bigl','bigr','Bigl','Bigr'}

def _grp(s, i):
    """读一个参数：{...} 或单字符 或 \\cmd。返回 (原文, 下一位置)"""
    while i < len(s) and s[i] == ' ': i += 1
    if i >= len(s): return '', i
    if s[i] == '{':
        d, j = 0, i
        while j < len(s):
            if s[j] == '{': d += 1
            elif s[j] == '}':
                d -= 1
                if d == 0: return s[i+1:j], j+1
            j += 1
        return s[i+1:], len(s)
    if s[i] == '\\':
        j = i+1
        while j < len(s) and s[j].isalpha(): j += 1
        if j == i+1: j = i+2
        return s[i:j], j
    return s[i], i+1

def conv(s):
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == '\\':
            j = i+1
            while j < n and s[j].isalpha(): j += 1
            if j == i+1:                       # \, \; \! \{ \\ 等
                cmd, j = s[i+1:i+2], i+2
                if cmd == '\\': out.append('<br>'); i = j; continue
            else:
                cmd = s[i+1:j]
                while j < n and s[j] == ' ': j += 1   # 控制字吞掉后随空格
            if cmd == 'frac' or cmd == 'dfrac' or cmd == 'tfrac':
                a, j = _grp(s, j); b, j = _grp(s, j)
                out.append('<span class="fr"><span class="fr-n">%s</span>'
                           '<span class="fr-d">%s</span></span>' % (conv(a), conv(b)))
            elif cmd == 'sqrt':
                a, j = _grp(s, j)
                out.append('<span class="sq">√<span class="sq-b">%s</span></span>' % conv(a))
            elif cmd == 'boxed':
                a, j = _grp(s, j)
                out.append('<span class="bx">%s</span>' % conv(a))
            elif cmd in PLAIN:
                a, j2 = _grp(s, j)
                if cmd in ('left','right'):
                    out.append(conv(a) if a not in ('.',) else ''); j = j2
                elif cmd in ('mathbf','textbf'):
                    out.append('<b>%s</b>' % conv(a)); j = j2
                elif cmd in ('displaystyle','limits'):
                    pass
                else:
                    out.append(H.escape(a) if cmd in ('text','mathrm','operatorname') else conv(a)); j = j2
            elif cmd in SYM:
                v = SYM[cmd]
                if cmd in ('ln','log','cos','sin','tan','exp','max','min','lim'):
                    out.append('<span class="op">%s</span>' % v)
                else:
                    out.append(v)
            else:
                out.append(H.escape(cmd))
            i = j
        elif c in '^_':
            a, j = _grp(s, i+1)
            out.append(('<sup>%s</sup>' if c == '^' else '<sub>%s</sub>') % conv(a))
            i = j
        elif c == '{':
            a, j = _grp(s, i)
            out.append(conv(a)); i = j
        elif c == '}':
            i += 1
        elif c == '&':
            out.append('&amp;'); i += 1
        elif c == '<':
            out.append('&lt;'); i += 1
        elif c == '>':
            out.append('&gt;'); i += 1
        else:
            out.append(c); i += 1
    return ''.join(out)


import re as _re
_REL = _re.compile(r'(?<![\w])([=≈≤≥∝⇒→↔≠≡])(?!\w)')
def _space_text(h):
    parts, out, intag = _re.split(r'(<[^>]*>)', h), [], None
    for p in parts:
        if p.startswith('<'): out.append(p)
        else: out.append(_REL.sub(lambda m: '\u2009'+m.group(1)+'\u2009', p))
    return ''.join(out)

def tex(s):
    """对外入口：LaTeX 子集 -> 排版好的 HTML"""
    return _space_text(conv(s))
