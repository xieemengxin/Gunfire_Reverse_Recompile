# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3142.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3142.pyc
# Source Generated with Decompyle++
# File: c3142.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3142
    m_Shape = 3142
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 31422
    m_PerformList = (31421, 38018, 31423, 31424, 31425, 38028, 38029, 31426, 4111, 4074)
    m_Betree = 'EliteFar.EliteInvisibleFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.EliteInvisibleFarFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4179,
        2: 4061 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31421 },
        (1, 0): {
            'PFAI': 31421 },
        (0, 2): {
            'PFAI': 31421 },
        (0, 1): {
            'PFAI': 31421 } }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1011
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

