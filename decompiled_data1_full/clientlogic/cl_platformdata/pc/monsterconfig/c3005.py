# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3005.pyc
# Source Generated with Decompyle++
# File: c3005.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORBADGER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3005
    m_Shape = 3004
    m_FightType = WARRIOR_NORBADGER
    m_AttPerform = 30041
    m_PerformList = (4134, 30042, 4111, 4074, 30043, 4325)
    m_Betree = 'MonsterSelfExplosion.lanternSelfExplosionFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSelfExplosion.lanternSelfExplosionFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201,)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20041 },
        (1, 0): {
            'PFAI': 20041 },
        (0, 2): {
            'PFAI': 20041 },
        (0, 1): {
            'PFAI': 20041 } }
    m_CombatForce = 1
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
    m_SurvivorAttrPlus = (6251,)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

