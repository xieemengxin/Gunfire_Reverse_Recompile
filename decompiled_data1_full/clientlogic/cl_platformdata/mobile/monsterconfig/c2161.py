# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2161.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2161.pyc
# Source Generated with Decompyle++
# File: c2161.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORSNIPE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2161
    m_Shape = 2161
    m_FightType = WARRIOR_NORSNIPE
    m_AttPerform = 21611
    m_PerformList = (38016, 21612, 21621, 38025, 38026)
    m_Betree = 'MonsterSniper.snipeFuzzyfsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSniper.snipeFuzzyfsm' },
        'Common': {
            1: 'MonsterSniper.snipeFuzzyfsm',
            2: 'MonsterSniper.snipeFuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21613 },
        (1, 2): {
            'PFAI': 21612 },
        (0, 3): {
            'PFAI': 21613 },
        (1, 1): {
            'PFAI': 21611 },
        (0, 2): {
            'PFAI': 21612 },
        (0, 1): {
            'PFAI': 21611 } }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = {
        1: 200,
        2: 200,
        3: 100 }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

