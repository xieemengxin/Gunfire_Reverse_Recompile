#!/usr/bin/env python3
"""把 extracted/levelconf 统一成 hash 命名（<mapid>/0x<HASH>.json），
并生成归属清单 manifest.csv / manifest.json：每个 json 属于哪个地图、哪个关卡、什么类型。

外部加载用 hash 作 key（与 m1logic4.dll 包内索引一致），不依赖 name 反推。
清单只为「让人看懂每个文件是什么」，name 已还原的也附上。
"""
import os, re, json, sys, glob, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from fls_namehash import name_hash

OUT = os.path.join(ROOT, 'extracted', 'levelconf')
DATA0 = os.path.join(ROOT, 'extracted', 'data0')


def load_levelconf():
    for f in glob.glob(os.path.join(DATA0, '*.json')):
        d = json.load(open(f))
        v = next(iter(d.values())) if d else None
        if isinstance(v, dict) and 'arealine' in v:
            return d
    return {}


def build_line_index(levelconf):
    """(mapid:str, lineName) -> list[(levelid, area)]"""
    idx = {}
    for lvl, info in levelconf.items():
        if not isinstance(info, dict):
            continue
        mapid = str(info.get('map'))
        for area, lw in info.get('arealine', {}).items():
            for ln in lw:
                idx.setdefault((mapid, ln), []).append((lvl, area))
    return idx


def classify(content):
    if isinstance(content, dict):
        ks = set(content.keys())
        if 'monsterconf' in ks or 'SpawnRule' in ks or 'LineLoc' in ks:
            return 'line'
        if ks and all(re.fullmatch(r'\d+', k) for k in ks):
            return 'levelinfo'
        if {'shoppos', 'rewardpos', 'bossrewardpos'} & ks:
            return 'mapinfo'
    return 'other'


def main():
    levelconf = load_levelconf()
    line_idx = build_line_index(levelconf)
    rows = []
    for d in sorted(glob.glob(os.path.join(OUT, '*'))):
        if not os.path.isdir(d):
            continue
        mapid = os.path.basename(d)
        for f in glob.glob(os.path.join(d, '*.json')):
            b = os.path.basename(f)
            if b == 'manifest.json':
                continue
            mobj = re.match(r'_unknown_0x([0-9A-Fa-f]{8})\.json', b)
            if mobj:                       # 隐藏 line：只有 hash
                h = int(mobj.group(1), 16)
                name = ''
            else:                          # 已还原 name：反算 hash
                name = b[:-5]
                h = name_hash(name + '.txt')
            try:
                content = json.load(open(f, encoding='utf-8'))
            except Exception:
                content = None
            typ = classify(content)
            area = ''
            levels = []
            if typ == 'line':
                if isinstance(content, dict):
                    area = content.get('area', '')
                if name:
                    levels = [lvl for lvl, _a in line_idx.get((mapid, name), [])]
            elif typ == 'levelinfo' and isinstance(content, dict):
                levels = list(content.keys())
            # 统一重命名为 hash
            dst = os.path.join(d, '0x%08X.json' % h)
            if os.path.abspath(f) != os.path.abspath(dst):
                os.replace(f, dst)
            rows.append({
                'mapid': mapid,
                'hash': '0x%08X' % h,
                'type': typ,
                'name': name,
                'area': str(area),
                'levels': ';'.join(map(str, levels)),
            })

    # 写 csv
    rows.sort(key=lambda r: (r['mapid'], r['type'], r['hash']))
    with open(os.path.join(OUT, 'manifest.csv'), 'w', newline='', encoding='utf-8') as fp:
        w = csv.DictWriter(fp, fieldnames=['mapid', 'hash', 'type', 'name', 'area', 'levels'])
        w.writeheader()
        w.writerows(rows)
    # 写 json（按 map 分组）
    grouped = {}
    for r in rows:
        grouped.setdefault(r['mapid'], {})[r['hash']] = {k: r[k] for k in ('type', 'name', 'area', 'levels')}
    with open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8') as fp:
        json.dump(grouped, fp, ensure_ascii=False, indent=1)

    # 统计
    from collections import Counter
    c = Counter(r['type'] for r in rows)
    named = sum(1 for r in rows if r['name'])
    print(f'地图 {len(grouped)} 个, 文件 {len(rows)} 个')
    print('类型分布:', dict(c))
    print(f'其中带 name 的: {named} ({100*named/len(rows):.1f}%)')
    print('清单: extracted/levelconf/manifest.csv , manifest.json')


if __name__ == '__main__':
    main()
