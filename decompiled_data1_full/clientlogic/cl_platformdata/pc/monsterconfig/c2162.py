# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2162.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2162.pyc
# Source Generated with Decompyle++
# File: c2162.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORSNIPE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2162
    m_Shape = 2162
    m_FightType = WARRIOR_NORSNIPE
    m_AttPerform = 21621
    m_PerformList = (21612, 38015, 21622, 38028, 38029)
    m_Betree = 'MonsterSniper.snipeFuzzyfsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSniper.snipeFuzzyfsm' },
        'Common': {
            1: 'MonsterSniper.snipeFuzzyfsm',
            2: 'MonsterSniper.BrokenshieldAreamoveFsm',
            128: 'MonsterSniper.BrokenshieldAreamoveFsm',
            64: 'Common.GlobalAreaMoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 21621 },
        (1, 0): {
            'PFAI': 21621 },
        (0, 2): {
            'PFAI': 21621 },
        (0, 1): {
            'PFAI': 21621 } }
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
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

