# -*- coding: utf-8 -*-
"""把正文里裸写的 T_m / M_n 这类下标转成真下标；跳过 $$...$$、$...$ 与代码段。"""
import re, sys, pathlib

SUB = ['T_m','T_g','T_c','M_n','M_w','M_v','M_0','R_g','R_h','R_0',
       'x_A','x_B','C_p','B_3','V_h','V_m','n_i','M_i','m_A','m_B','I_0',
       'phi_A','phi_B','w_A','w_B','p_A','p_B','mu_A','n_A','n_B','L_0','D_m','D_t','V_R','I_s','H_A','H_B','S_A','S_B','G_i','G_f']

# 关键：$$...$$ 必须先于 $...$ 匹配，否则奇偶配对错位，
# 之后的正文会被整段误判成公式而跳过替换。
SKIP = re.compile(r'(\$\$.*?\$\$|\$[^\$\n]+\$|`[^`]+`)', re.S)

def fix(text):
    parts, n = SKIP.split(text), 0
    for j, seg in enumerate(parts):
        if seg.startswith('$') or seg.startswith('`'):
            continue
        for t in SUB:
            base, sub = t.split('_')
            cnt = seg.count(t)
            if cnt:
                seg = seg.replace(t, '%s<sub>%s</sub>' % (base, sub)); n += cnt
        parts[j] = seg
    return "".join(parts), n

if __name__ == '__main__':
    p = pathlib.Path(sys.argv[1])
    s, n = fix(p.read_text(encoding='utf-8'))
    p.write_text(s, encoding='utf-8')
    print('下标修复:', n, '处')
