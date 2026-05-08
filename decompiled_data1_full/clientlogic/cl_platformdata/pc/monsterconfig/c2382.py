# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2382.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2382.pyc
# Source Generated with Decompyle++
# File: c2382.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORPART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2382
    m_Shape = 2381
    m_FightType = WARRIOR_NORPART
    m_AttPerform = 0
    m_PerformList = ()
    m_Betree = ''
    m_BetreeMap = {
        'Default': {
            0: '' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = { }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6110,)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

