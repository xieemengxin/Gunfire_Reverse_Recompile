# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2245.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2245.pyc
# Source Generated with Decompyle++
# File: c2245.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORPETRO
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2245
    m_Shape = 2245
    m_FightType = WARRIOR_NORPETRO
    m_AttPerform = 22411
    m_PerformList = (22412, 22413, 38025, 38026, 38027, 4120)
    m_Betree = 'MonsterFar.throwFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.throwFsm' },
        'Common': {
            1: 'MonsterFar.throwFsm',
            2: 'MonsterFar.farAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 22411 },
        (1, 0): {
            'PFAI': 22411 },
        (0, 2): {
            'PFAI': 22411 },
        (0, 1): {
            'PFAI': 22411 } }
    m_CombatForce = 0.75
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
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

