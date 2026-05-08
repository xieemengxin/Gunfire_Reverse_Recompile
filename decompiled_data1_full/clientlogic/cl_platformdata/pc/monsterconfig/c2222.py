# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2222.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2222.pyc
# Source Generated with Decompyle++
# File: c2222.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORBADGER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2222
    m_Shape = 2222
    m_FightType = WARRIOR_NORBADGER
    m_AttPerform = 22221
    m_PerformList = (22223, 4049, 38021, 38022)
    m_Betree = 'MonsterSelfExplosion.fireExplosionFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSelfExplosion.fireExplosionFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 22221 },
        (1, 0): {
            'PFAI': 22221 },
        (0, 2): {
            'PFAI': 22221 },
        (0, 1): {
            'PFAI': 22221 } }
    m_CombatForce = 0.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6108, 6111, 6112, 6113)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

