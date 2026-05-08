# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3128.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3128.pyc
# Source Generated with Decompyle++
# File: c3128.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3128
    m_Shape = 3128
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 21282
    m_PerformList = (21281, 38039, 38040, 4111, 4311)
    m_Betree = 'MonsterMediumNear.weakpointNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumNear.weakpointNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21283 },
        (1, 2): {
            'PFAI': 21282 },
        (0, 3): {
            'PFAI': 21281 },
        (1, 1): {
            'PFAI': 21283 },
        (0, 2): {
            'PFAI': 21282 },
        (0, 1): {
            'PFAI': 21281 } }
    m_CombatForce = 1.25
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

