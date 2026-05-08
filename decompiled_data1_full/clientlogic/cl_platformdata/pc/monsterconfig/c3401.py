# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3401.pyc
# Source Generated with Decompyle++
# File: c3401.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIBATTERY
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3401
    m_Shape = 3401
    m_FightType = WARRIOR_ELIBATTERY
    m_AttPerform = 24011
    m_PerformList = (4237, 4111, 24013, 4259)
    m_Betree = 'MonsterLargeSummon.LargeSummonFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterLargeSummon.LargeSummonFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203,)
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = {
        (0, 3): {
            'PFAI': 24011 },
        (1, 0): {
            'PFAI': 24011 },
        (0, 2): {
            'PFAI': 24011 },
        (0, 1): {
            'PFAI': 24011 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6110, 6108, 6112, 6114, 6111)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

