#!/usr/bin/env python3
"""把所有关卡配置（mdataN 里的 json 资源）还原成真实文件名，
统一输出到 extracted/levelconf/<mapid>/<sFile>.json，目录结构符合 lib_load 改造逻辑。

依赖：
- extracted/data0/ 下两个 json：levelconf（arealine/map）+ residx（<mapid>/json -> mdataN）
- fls/mdataN.fls
- tools/fls_namehash.py（file_hash 算法）
- tools/fls_unpacker_improved.py（FLS0 解包）
"""
import os, re, json, sys, tempfile, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from fls_namehash import name_hash
import importlib.util
spec = importlib.util.spec_from_file_location('flsunp', os.path.join(ROOT, 'tools', 'fls_unpacker_improved.py'))
flsunp = importlib.util.module_from_spec(spec); sys.modules['flsunp'] = flsunp; spec.loader.exec_module(flsunp)

DATA0 = os.path.join(ROOT, 'extracted', 'data0')
FLS = os.path.join(ROOT, 'fls')
OUT = os.path.join(ROOT, 'extracted', 'levelconf')

# 除 line 外，json 包里可能出现的固定资源名（不带后缀）。未命中会报告，按需补充。
FIXED_NAMES = ['mapinfo', 'levelinfo', 'levelinfodiff', 'minimap', 'navinfo', 'sceneinfo']


def load_data0():
    levelconf = residx = None
    for f in glob.glob(os.path.join(DATA0, '*.json')):
        d = json.load(open(f))
        v = next(iter(d.values())) if d else None
        if isinstance(v, str) and v.startswith('mdata'):
            residx = d
        elif isinstance(v, dict) and 'arealine' in v:
            levelconf = d
    return levelconf, residx


def map_to_lines(levelconf):
    """mapid(str) -> set(line names)"""
    m = {}
    for _lvl, info in levelconf.items():
        if not isinstance(info, dict):
            continue
        mapid = str(info.get('map'))
        s = m.setdefault(mapid, set())
        for _area, lw in info.get('arealine', {}).items():
            for ln in lw:
                s.add(ln)
    return m


def unpack_fls0(path):
    """解包一个 FLS0 包，返回 {file_hash:int -> raw bytes}"""
    out = {}
    with tempfile.TemporaryDirectory() as td:
        up = flsunp.create_unpacker(path)
        up.unpack(td, progress_every=0)
        for fn in os.listdir(td):
            mobj = re.search(r'0x([0-9A-Fa-f]{8})', fn)
            if not mobj:
                continue
            h = int(mobj.group(1), 16)
            with open(os.path.join(td, fn), 'rb') as fp:
                out[h] = fp.read()
    return out


def main():
    levelconf, residx = load_data0()
    if not levelconf or not residx:
        print('[error] 未找到 levelconf / residx，请先解包 data0')
        return
    m2l = map_to_lines(levelconf)
    os.makedirs(OUT, exist_ok=True)

    # 全局 hash 表：所有 line 名（跨 map 复用） + 固定资源名
    all_names = set(FIXED_NAMES)
    for s in m2l.values():
        all_names |= s
    global_h2name = {}
    for n in all_names:
        global_h2name[name_hash(n + '.txt')] = n
    print(f'全局候选名 {len(all_names)} 个 -> hash 表 {len(global_h2name)} 项')

    # mapid -> mdataN  (只取 /json 资源)
    json_pkgs = {}
    for k, v in residx.items():
        if k.endswith('/json'):
            json_pkgs[k.split('/')[0]] = v

    total_files = total_unmatched = done_maps = 0
    unmatched_report = {}
    for mapid, pkg in sorted(json_pkgs.items()):
        fls_path = os.path.join(FLS, pkg + '.fls')
        if not os.path.isfile(fls_path):
            continue
        entries = unpack_fls0(fls_path)
        h2name = global_h2name
        dst = os.path.join(OUT, mapid)
        os.makedirs(dst, exist_ok=True)
        unmatched = []
        for h, raw in entries.items():
            name = h2name.get(h)
            if name is None:
                unmatched.append('0x%08X' % h)
                # 仍保留，便于排查
                with open(os.path.join(dst, '_unknown_0x%08X.json' % h), 'wb') as fp:
                    fp.write(raw)
                continue
            with open(os.path.join(dst, name + '.json'), 'wb') as fp:
                fp.write(raw)
            total_files += 1
        if unmatched:
            unmatched_report[mapid] = unmatched
            total_unmatched += len(unmatched)
        done_maps += 1

    print(f'完成: {done_maps} 个地图, 还原 {total_files} 个命名文件, 未匹配 {total_unmatched} 个')
    if unmatched_report:
        print('未匹配 hash（可能是未枚举的固定资源名）:')
        for mapid, hs in list(unmatched_report.items())[:20]:
            print(f'  map {mapid}: {hs}')


if __name__ == '__main__':
    main()
