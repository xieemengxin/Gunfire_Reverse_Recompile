# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3910.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3910.pyc
# Source Generated with Decompyle++
# File: c3910.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, WARRIOR_NODURABILITY
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3910
    m_Shape = 1020
    m_FightType = WARRIOR_NODURABILITY
    m_AttPerform = 0
    m_PerformList = (4316, 4366)
    m_Betree = ''
    m_BetreeMap = {
        'Default': {
            0: 'Common.standfsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = { }
    m_CombatForce = 0
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
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

