# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2088.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2088.pyc
# Source Generated with Decompyle++
# File: c2088.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORPETRO
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2088
    m_Shape = 2088
    m_FightType = WARRIOR_NORPETRO
    m_AttPerform = 20832
    m_PerformList = (20831, 38021, 38022, 20834, 4120)
    m_Betree = 'MonsterNear.nearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.nearFsm' },
        'Common': {
            1: 'MonsterNear.nearFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20831 },
        (1, 0): {
            'PFAI': 20831 },
        (0, 2): {
            'PFAI': 20831 },
        (0, 1): {
            'PFAI': 20831 } }
    m_CombatForce = 0.75
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
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

