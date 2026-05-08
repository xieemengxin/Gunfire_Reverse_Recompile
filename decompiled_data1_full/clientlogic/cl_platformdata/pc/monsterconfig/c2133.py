# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2133.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2133.pyc
# Source Generated with Decompyle++
# File: c2133.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2133
    m_Shape = 2133
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21331
    m_PerformList = (21332, 21333, 21334, 21335, 21336, 21337, 4111, 21338, 5328)
    m_Betree = 'MonsterMediumNear.MonsterSharkFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumNear.MonsterSharkFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21333 },
        (1, 2): {
            'PFAI': 21332 },
        (0, 3): {
            'PFAI': 21333 },
        (1, 1): {
            'PFAI': 21331 },
        (0, 2): {
            'PFAI': 21332 },
        (0, 1): {
            'PFAI': 21331 } }
    m_CombatForce = 1.5
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
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

