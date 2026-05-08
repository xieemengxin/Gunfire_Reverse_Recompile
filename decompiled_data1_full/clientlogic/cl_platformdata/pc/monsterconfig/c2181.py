# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2181.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2181.pyc
# Source Generated with Decompyle++
# File: c2181.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2181
    m_Shape = 2181
    m_FightType = WARRIOR_NORHEVNEAR
    m_AttPerform = 21811
    m_PerformList = (21812, 21813, 4111)
    m_Betree = 'MonsterHugeNear.HugeNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterHugeNear.HugeNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 21811 },
        (1, 0): {
            'PFAI': 21811 },
        (0, 2): {
            'PFAI': 21811 },
        (0, 1): {
            'PFAI': 21811 } }
    m_CombatForce = 1.5
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
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

