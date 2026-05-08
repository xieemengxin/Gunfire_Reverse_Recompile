# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3924.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3924.pyc
# Source Generated with Decompyle++
# File: c3924.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSSKING
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3924
    m_Shape = 3924
    m_FightType = WARRIOR_BOSSKING
    m_AttPerform = 39241
    m_PerformList = (39242, 39243, 39244, 39245, 39246, 39247, 39248, 4223, 4111, 4243, 39250, 4250, 39249, 39251, 39252, 39253, 39254, 39255, 4269, 4395)
    m_Betree = 'BossDemon.bossDemonFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossDemon.bossDemonFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4232,
        2: 4233,
        3: 4234,
        4: 4235,
        5: 4236,
        6: 4264 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { },
        5: { },
        6: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39243 },
        (1, 2): {
            'PFAI': 39242 },
        (1, 1): {
            'PFAI': 39241 },
        (0, 3): {
            'PFAI': 39243 },
        (0, 2): {
            'PFAI': 39242 },
        (0, 1): {
            'PFAI': 39241 } }
    m_CombatForce = 10
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

