# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3089.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3089.pyc
# Source Generated with Decompyle++
# File: c3089.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELISMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3089
    m_Shape = 3089
    m_FightType = WARRIOR_ELISMANEAR
    m_AttPerform = 30872
    m_PerformList = (30871, 38031, 38032, 38035, 30873, 4111, 30875, 30876, 30874, 30877)
    m_Betree = 'EliteNear.EliteSwordFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteSwordFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 30872 },
        (1, 0): {
            'PFAI': 30872 },
        (0, 2): {
            'PFAI': 30872 },
        (0, 1): {
            'PFAI': 30872 } }
    m_CombatForce = 10
    m_BornActionInfo = {
        'Show': 80 }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1012
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

