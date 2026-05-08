# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2225.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2225.pyc
# Source Generated with Decompyle++
# File: c2225.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_NORFLY
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2225
    m_Shape = 2225
    m_FightType = WARRIOR_NORFLY
    m_AttPerform = 22251
    m_PerformList = (22252, 5343, 22253)
    m_Betree = 'MonsterFlyable.FlyExplosionFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFlyable.FlyExplosionFsm' },
        'Common': {
            2: 'MonsterFlyable.FlyExplosionFsm',
            128: 'MonsterFlyable.FlyExplosionFsm',
            64: 'MonsterFlyable.FlyExplosionFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = {
        2: 5352 }
    m_PhaseHitPartToType = {
        1: { },
        2: { } }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22251 },
        (0, 3): {
            'PFAI': 22251 },
        (1, 2): {
            'PFAI': 22251 },
        (0, 2): {
            'PFAI': 22251 },
        (1, 1): {
            'PFAI': 22251 },
        (0, 1): {
            'PFAI': 22251 } }
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
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 2
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

