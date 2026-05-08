# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2085.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2085.pyc
# Source Generated with Decompyle++
# File: c2085.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2085
    m_Shape = 2085
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 20821
    m_PerformList = (20851, 20852, 38023, 38024)
    m_Betree = 'MonsterNear.nearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.nearFsm' },
        'Common': {
            1: 'MonsterNear.nearFsm',
            64: 'MonsterNear.GlobalNearFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20851 },
        (1, 0): {
            'PFAI': 20851 },
        (0, 2): {
            'PFAI': 20851 },
        (0, 1): {
            'PFAI': 20851 } }
    m_CombatForce = 0.75
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
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
        'FightMinDis': 5,
        'FightMaxDis': 7,
        'WaitPatrolRadius': 4 }

