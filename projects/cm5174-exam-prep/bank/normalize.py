# -*- coding: utf-8 -*-
"""把 L01–L10 合并成 bank_all.py：
   ① 去掉选项里的 <b>（只给正确项加粗等于泄题）
   ② 在不破坏解析中「选项 X」引用的前提下，重新平衡正确答案的 A/B/C/D 分布
"""
import sys, re, importlib, collections
sys.path.insert(0, '/home/user/Chemistry/projects/cm5174-exam-prep/bank')

REF = re.compile(r'选项\s*([ABCD])')
strip_b = lambda s: s.replace('<b>', '').replace('</b>', '')

mods = [importlib.import_module('L%02d' % i) for i in range(1, 11)]
out, n = [], 0
for m in mods:
    for q in m.L:
        n += 1
        out.append(dict(n=n, lec=m.LEC, leccn=m.CN, lectitle=m.TITLE, srcfile=m.SRC,
                        kind=q['kind'], topic=q['topic'], stem=q['stem'],
                        opts=[strip_b(o) for o in q['opts']], ans=q['ans'],
                        exp=q['exp'], kp=q['kp'], src=q['src'],
                        locked=bool(REF.search(q['exp']))))

# --- 重新平衡：把可自由重排的题的正确项挪到当前最少用的槽位 ---
cnt = collections.Counter(q['ans'] for q in out if q['locked'])
for q in out:
    if q['locked']:
        continue
    tgt = min(range(4), key=lambda i: (cnt[i], i))     # 选当前最少用的位置
    cur = q['ans']
    if tgt != cur:
        o = q['opts']
        o[cur], o[tgt] = o[tgt], o[cur]                 # 交换两个选项
        q['ans'] = tgt
    cnt[q['ans']] += 1

if __name__ == '__main__':
    import json
    with open('/home/user/Chemistry/projects/cm5174-exam-prep/bank/bank_all.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    c = collections.Counter(q['ans'] for q in out)
    print('题目总数:', len(out))
    print('答案分布 A/B/C/D:', [c[i] for i in range(4)],
          '  最大占比 %.1f%%' % (100*max(c.values())/len(out)))
    print('锁定（解析引用选项字母）:', sum(q['locked'] for q in out))
    # 校验：锁定题的答案没被动过
    for m, q in zip([x for mm in mods for x in mm.L], out):
        if q['locked']:
            assert m['ans'] == q['ans'], q['n']
            assert [strip_b(o) for o in m['opts']] == q['opts'], q['n']
    print('锁定题校验通过')
    assert not any('<b>' in o for q in out for o in q['opts']), '仍有加粗选项'
    print('选项加粗已清除')
