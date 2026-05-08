# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3926.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3926.pyc
# Source Generated with Decompyle++
# File: c3926.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSSKING
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3926
    m_Shape = 3926
    m_FightType = WARRIOR_BOSSKING
    m_AttPerform = 39242
    m_PerformList = (39244, 39245, 4111, 4243, 39250, 39249, 39251, 39252, 39253, 39254, 39255, 4305, 4395)
    m_Betree = 'BossDemon.bossDemonGhostFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossDemon.bossDemonGhostFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39244 },
        (1, 2): {
            'PFAI': 39242 },
        (1, 1): {
            'PFAI': 39241 },
        (0, 3): {
            'PFAI': 39244 },
        (0, 2): {
            'PFAI': 39242 },
        (0, 1): {
            'PFAI': 39241 } }
    m_CombatForce = 0
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

