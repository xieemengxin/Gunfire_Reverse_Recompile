# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2204.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2204.pyc
# Source Generated with Decompyle++
# File: c2204.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_EASY, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2204
    m_Shape = 2202
    m_FightType = WARRIOR_NORHEVFAR
    m_AttPerform = 22024
    m_PerformList = (22022, 22023, 4111)
    m_Betree = 'MonsterLargeFar.LargeFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterLargeFar.LargeFarFsm' },
        'Common': {
            2: 'Common.FuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 22022 },
        (1, 0): {
            'PFAI': 22022 },
        (0, 2): {
            'PFAI': 22022 },
        (0, 1): {
            'PFAI': 22022 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_EASY,
        2: MISSING_DIS_NORMAL,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

