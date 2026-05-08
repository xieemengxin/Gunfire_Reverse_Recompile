# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/__init__.pyc
# RelativePath: clientlogic/cl_monster/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from . import mobject
from . import monsterpart, monsterdurability, monsterclone
from cl_cscommondef import WARRIOR_NORPART, WARRIOR_ELIPART, WARRIOR_NODURABILITY, MONSTER_DATASID_SEAMONSTERCLONE
g_MonsterClass = {
    WARRIOR_NODURABILITY: monsterdurability.CMonsterDurability,
    WARRIOR_ELIPART: monsterpart.CMonsterPart,
    WARRIOR_NORPART: monsterpart.CMonsterPart }
g_DataSIDToMonsterClass = {
    MONSTER_DATASID_SEAMONSTERCLONE: monsterclone.CSeaMonsterClone }

def NewMonster(oGame, clsData, dAddData):
    if 'ID' in dAddData:
        nid = dAddData['ID']
    else:
        nid = oGame.NewNPCID()
    if clsData.m_FightType in g_MonsterClass:
        oMonster = g_MonsterClass[clsData.m_FightType](oGame, nid)
    elif clsData.m_DataSID in g_DataSIDToMonsterClass:
        oMonster = g_DataSIDToMonsterClass[clsData.m_DataSID](oGame, nid)
    else:
        oMonster = mobject.CMonster(oGame, nid)
    oMonster.InitMonster(clsData, dAddData)
    return oMonster

