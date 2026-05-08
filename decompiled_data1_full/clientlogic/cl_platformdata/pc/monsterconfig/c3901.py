# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3901.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3901.pyc
# Source Generated with Decompyle++
# File: c3901.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3901
    m_Shape = 3901
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 39016
    m_PerformList = (39011, 39012, 39013, 39014, 39015, 4111, 4150)
    m_Betree = 'BossLuWu.bossLuWuFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossLuWu.bossLuWuFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4036,
        2: 4037,
        3: 4038 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39016 },
        (1, 2): {
            'PFAI': 39015 },
        (0, 3): {
            'PFAI': 39014 },
        (1, 1): {
            'PFAI': 39012 },
        (0, 2): {
            'PFAI': 39013 },
        (0, 1): {
            'PFAI': 39011 } }
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

