# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3183.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3183.pyc
# Source Generated with Decompyle++
# File: c3183.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIHEVNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3183
    m_Shape = 3183
    m_FightType = WARRIOR_ELIHEVNEAR
    m_AttPerform = 31833
    m_PerformList = (31831, 31832, 31834, 31835, 31836, 31837, 31838, 31839, 31840)
    m_Betree = 'EliteNear.EliteHugeNearMoveFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteHugeNearMoveFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 5331,
        2: 5332,
        3: 5333,
        4: 5339 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { } }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 31831 },
        (1, 2): {
            'PFAI': 31831 },
        (0, 3): {
            'PFAI': 31831 },
        (1, 1): {
            'PFAI': 31831 },
        (0, 2): {
            'PFAI': 31831 },
        (0, 1): {
            'PFAI': 31831 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 3
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

