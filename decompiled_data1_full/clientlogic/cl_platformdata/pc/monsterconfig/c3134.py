# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3134.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3134.pyc
# Source Generated with Decompyle++
# File: c3134.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3134
    m_Shape = 3134
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 31341
    m_PerformList = (31342, 4111, 5347, 31343, 5357, 5370, 4074)
    m_Betree = 'EliteNear.EliteDashNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteDashNearFsm' },
        'Common': {
            64: 'Common.GlobalAreaMoveFsm',
            128: 'Common.GlobalAreaMoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 31341 },
        (1, 2): {
            'PFAI': 31341 },
        (0, 3): {
            'PFAI': 31341 },
        (1, 1): {
            'PFAI': 31341 },
        (0, 2): {
            'PFAI': 31341 },
        (0, 1): {
            'PFAI': 31341 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1010
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 3
    m_ExtraAIArgs = {
        'FightMinDis': 7,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

