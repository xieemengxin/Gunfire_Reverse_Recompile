# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3906.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3906.pyc
# Source Generated with Decompyle++
# File: c3906.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSSCANNON
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3906
    m_Shape = 3916
    m_FightType = WARRIOR_BOSSCANNON
    m_AttPerform = 0
    m_PerformList = (39061, 39062, 4098, 4272, 4001)
    m_Betree = ''
    m_BetreeMap = {
        'Default': {
            0: 'Common.standfsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6202, 6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = { }
    m_CombatForce = 1
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
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

