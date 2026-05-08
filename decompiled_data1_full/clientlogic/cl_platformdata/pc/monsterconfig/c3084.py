# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3084.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3084.pyc
# Source Generated with Decompyle++
# File: c3084.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELISMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3084
    m_Shape = 3083
    m_FightType = WARRIOR_ELISMANEAR
    m_AttPerform = 30832
    m_PerformList = (30831, 38021, 38022, 30833, 4074, 30834, 30835, 4111)
    m_Betree = 'MonsterNear.PlotFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.PlotFsm' },
        'Common': {
            1: 'MonsterNear.PlotFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4159,
        2: 4160 }
    m_PhaseHitPartToType = {
        1: { },
        2: { } }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 30841 },
        (1, 0): {
            'PFAI': 30841 },
        (0, 2): {
            'PFAI': 30841 },
        (0, 1): {
            'PFAI': 30841 } }
    m_CombatForce = 10
    m_BornActionInfo = {
        'Show': 130 }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1010
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
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

