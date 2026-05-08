# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3123.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3123.pyc
# Source Generated with Decompyle++
# File: c3123.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3123
    m_Shape = 3123
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 31231
    m_PerformList = (31232, 4045, 31233, 4111, 4125)
    m_Betree = 'EliteNear.EliteBigShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteBigShieldFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31231 },
        (1, 0): {
            'PFAI': 31231 },
        (0, 2): {
            'PFAI': 31231 },
        (0, 1): {
            'PFAI': 31231 } }
    m_CombatForce = 10
    m_BornActionInfo = {
        'Show': 135 }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1010
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

