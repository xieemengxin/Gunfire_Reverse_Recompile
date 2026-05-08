# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2321.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2321.pyc
# Source Generated with Decompyle++
# File: c2321.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORDART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2321
    m_Shape = 2321
    m_FightType = WARRIOR_NORDART
    m_AttPerform = 23211
    m_PerformList = ()
    m_Betree = 'MonsterCrab.CrabFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterCrab.CrabFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 23211 },
        (1, 0): {
            'PFAI': 23211 },
        (0, 2): {
            'PFAI': 23211 },
        (0, 1): {
            'PFAI': 23211 } }
    m_CombatForce = 0.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6108, 6111, 6112, 6113)
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = (6154, 6155, 6158, 6161, 6162, 6163)
    m_AttackCost = 1
    m_ExtraAIArgs = { }

