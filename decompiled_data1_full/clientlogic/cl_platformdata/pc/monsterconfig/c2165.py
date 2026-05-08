# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2165.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2165.pyc
# Source Generated with Decompyle++
# File: c2165.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORSNIPE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2165
    m_Shape = 2165
    m_FightType = WARRIOR_NORSNIPE
    m_AttPerform = 21651
    m_PerformList = (21652, 21653, 38061)
    m_Betree = 'MonsterSniper.comboFuzzyfsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSniper.comboFuzzyfsm' },
        'Common': {
            1: 'MonsterSniper.comboFuzzyfsm',
            2: 'MonsterSniper.comboFuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21653 },
        (1, 2): {
            'PFAI': 21652 },
        (0, 3): {
            'PFAI': 21653 },
        (1, 1): {
            'PFAI': 21651 },
        (0, 2): {
            'PFAI': 21652 },
        (0, 1): {
            'PFAI': 21651 } }
    m_CombatForce = 1.25
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

