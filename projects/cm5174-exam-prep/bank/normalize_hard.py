# -*- coding: utf-8 -*-
"""HARD.py -> hard_all.json：剥离选项加粗 + 平衡答案分布（跳过解析里引用选项字母的题）。"""
import sys, re, json, collections
sys.path.insert(0, '/home/user/Chemistry/projects/cm5174-exam-prep/bank')
import HARD

REF = re.compile(r'选项\s*([ABCD])')
strip_b = lambda s: s.replace('<b>', '').replace('</b>', '')

out = []
for i, q in enumerate(HARD.L, 1):
    out.append(dict(n=i, kind=q['kind'], tag=q['tag'], topic=q['topic'],
                    stem=q['stem'], opts=[strip_b(o) for o in q['opts']],
                    ans=q['ans'], exp=q['exp'], kp=q['kp'], src=q['src'],
                    locked=bool(REF.search(q['exp']))))

cnt = collections.Counter(q['ans'] for q in out if q['locked'])
for q in out:
    if q['locked']:
        continue
    tgt = min(range(4), key=lambda i: (cnt[i], i))
    if tgt != q['ans']:
        o = q['opts']; o[q['ans']], o[tgt] = o[tgt], o[q['ans']]; q['ans'] = tgt
    cnt[q['ans']] += 1

json.dump(out, open('/home/user/Chemistry/projects/cm5174-exam-prep/bank/hard_all.json',
                    'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = collections.Counter(q['ans'] for q in out)
print('题数:', len(out), '| 答案分布 A/B/C/D:', [c[i] for i in range(4)],
      '| 最大占比 %.0f%%' % (100*max(c.values())/len(out)))
print('锁定（引用选项字母）:', sum(q['locked'] for q in out))
for a, b in zip(HARD.L, out):
    if b['locked']:
        assert a['ans'] == b['ans'] and [strip_b(o) for o in a['opts']] == b['opts']
assert not any('<b>' in o for q in out for o in q['opts'])
print('锁定题校验通过 · 选项加粗已清除')
