# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2243.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2243.pyc
# Source Generated with Decompyle++
# File: c2243.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORDART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2243
    m_Shape = 2243
    m_FightType = WARRIOR_NORDART
    m_AttPerform = 22431
    m_PerformList = (22432, 22423, 38028, 38029, 38030)
    m_Betree = 'MonsterFar.throwFuzzyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.throwFuzzyFsm' },
        'Common': {
            2: 'MonsterFar.throwFuzzyAreamoveFsm',
            64: 'MonsterFar.GlobalThrowFsm',
            128: 'MonsterFar.GlobalThrowFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22433 },
        (1, 2): {
            'PFAI': 22432 },
        (0, 3): {
            'PFAI': 22433 },
        (1, 1): {
            'PFAI': 22431 },
        (0, 2): {
            'PFAI': 22432 },
        (0, 1): {
            'PFAI': 22431 } }
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
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 2
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

