# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2302.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2302.pyc
# Source Generated with Decompyle++
# File: c2302.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORFLY
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2302
    m_Shape = 2301
    m_FightType = WARRIOR_NORFLY
    m_AttPerform = 23011
    m_PerformList = (23012, 23013)
    m_Betree = 'MonsterFlyTest.FlyFsmTest'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFlyTest.FlyFsmTest' },
        'Common': {
            2: 'MonsterFlyTest.FlyAreamoveFsmTest',
            128: 'MonsterFlyTest.FlyFsmTest',
            64: 'MonsterFlyTest.FlyFsmTest' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 23011 },
        (1, 0): {
            'PFAI': 23011 },
        (0, 2): {
            'PFAI': 23011 },
        (0, 1): {
            'PFAI': 23011 } }
    m_CombatForce = 0.75
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
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

