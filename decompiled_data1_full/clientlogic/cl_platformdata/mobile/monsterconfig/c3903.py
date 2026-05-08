# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3903.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3903.pyc
# Source Generated with Decompyle++
# File: c3903.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3903
    m_Shape = 3903
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 39034
    m_PerformList = (39031, 39032, 39033, 39035, 39036, 39037, 39038, 39039, 39040, 39041, 4081, 39042, 4151)
    m_Betree = 'BossDesertTest.bossDesertFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossDesertTest.bossDesertFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4076,
        2: 4077,
        3: 4078,
        4: 4079,
        5: 4080 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { },
        5: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39031 },
        (1, 0): {
            'PFAI': 39031 },
        (0, 2): {
            'PFAI': 39031 },
        (0, 1): {
            'PFAI': 39031 } }
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
    m_ExtraAIArgs = { }

