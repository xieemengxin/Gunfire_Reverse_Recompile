# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c1026.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c1026.pyc
# Source Generated with Decompyle++
# File: c1026.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 1026
    m_Shape = 2101
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 0
    m_PerformList = ()
    m_Betree = 'Common.standfsm'
    m_BetreeMap = {
        'Default': {
            0: 'Common.standfsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = { }
    m_CombatForce = 0
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

