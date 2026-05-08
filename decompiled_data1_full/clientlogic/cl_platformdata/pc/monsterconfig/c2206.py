# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2206.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2206.pyc
# Source Generated with Decompyle++
# File: c2206.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2206
    m_Shape = 2206
    m_FightType = WARRIOR_NORHEVFAR
    m_AttPerform = 22061
    m_PerformList = (22062, 22063, 5342)
    m_Betree = 'MonsterLargeFar.LaserFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterLargeFar.LaserFsm' },
        'Common': {
            2: 'Common.FuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22033 },
        (1, 2): {
            'PFAI': 22062 },
        (0, 3): {
            'PFAI': 22063 },
        (1, 1): {
            'PFAI': 22061 },
        (0, 2): {
            'PFAI': 22062 },
        (0, 1): {
            'PFAI': 22061 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
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

