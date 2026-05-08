# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2005.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2005.pyc
# Source Generated with Decompyle++
# File: c2005.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORBADGER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2005
    m_Shape = 2004
    m_FightType = WARRIOR_NORBADGER
    m_AttPerform = 20041
    m_PerformList = (4083, 20042, 20043, 4325)
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
    m_BanPF = (6104, 6105, 6108, 6111, 6112, 6113)
    m_SurvivorAttrPlus = (6251,)
    m_SurvivorBanPF = (6154, 6155, 6158, 6161, 6163, 6162)
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

