# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3125.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3125.pyc
# Source Generated with Decompyle++
# File: c3125.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3125
    m_Shape = 3125
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 31251
    m_PerformList = (31252, 31255, 31256, 4045, 4111, 4125)
    m_Betree = 'EliteBigShield.EliteDesertShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteBigShield.EliteDesertShieldFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6204, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31252 },
        (1, 0): {
            'PFAI': 31252 },
        (0, 2): {
            'PFAI': 31252 },
        (0, 1): {
            'PFAI': 31252 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1011
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

