# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2205.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2205.pyc
# Source Generated with Decompyle++
# File: c2205.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2205
    m_Shape = 2205
    m_FightType = WARRIOR_NORHEVFAR
    m_AttPerform = 22051
    m_PerformList = (22052, 22053, 38013, 4071, 4111, 22055)
    m_Betree = 'MonsterNear.MonsterElectricFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.MonsterElectricFsm' },
        'Common': {
            64: 'MonsterNear.GlobalFireFsm',
            192: 'MonsterNear.GlobalFireFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22053 },
        (1, 2): {
            'PFAI': 22052 },
        (0, 3): {
            'PFAI': 22052 },
        (1, 1): {
            'PFAI': 22051 },
        (0, 2): {
            'PFAI': 22052 },
        (0, 1): {
            'PFAI': 22051 } }
    m_CombatForce = 1.25
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
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 3
    m_ExtraAIArgs = {
        'FightMinDis': 7,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

