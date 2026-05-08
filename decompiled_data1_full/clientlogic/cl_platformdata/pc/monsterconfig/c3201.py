# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3201.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3201.pyc
# Source Generated with Decompyle++
# File: c3201.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3201
    m_Shape = 3201
    m_FightType = WARRIOR_ELIHEVFAR
    m_AttPerform = 32011
    m_PerformList = (32012, 32013, 38013, 4068, 4111, 4074)
    m_Betree = 'EliteNear.EliteFireFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteFireFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 32011 },
        (1, 0): {
            'PFAI': 32011 },
        (0, 2): {
            'PFAI': 32011 },
        (0, 1): {
            'PFAI': 32011 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1011
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6114, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

