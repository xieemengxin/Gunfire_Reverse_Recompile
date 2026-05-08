# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3921.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3921.pyc
# Source Generated with Decompyle++
# File: c3921.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, WARRIOR_BOSSCANNON
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3921
    m_Shape = 3921
    m_FightType = WARRIOR_BOSSCANNON
    m_AttPerform = 0
    m_PerformList = (39211, 39213, 39212, 4211, 4111, 39216, 39217, 39219, 4001)
    m_Betree = ''
    m_BetreeMap = {
        'Default': {
            0: 'BossSeaMonster.bossSingleFsm' },
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

