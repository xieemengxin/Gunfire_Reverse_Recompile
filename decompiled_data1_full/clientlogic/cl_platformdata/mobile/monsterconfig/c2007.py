# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2007.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2007.pyc
# Source Generated with Decompyle++
# File: c2007.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORBADGER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2007
    m_Shape = 2007
    m_FightType = WARRIOR_NORBADGER
    m_AttPerform = 20061
    m_PerformList = (20062,)
    m_Betree = 'MonsterNear.SmallNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.SmallNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201,)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20061 },
        (1, 0): {
            'PFAI': 20061 },
        (0, 2): {
            'PFAI': 20061 },
        (0, 1): {
            'PFAI': 20061 } }
    m_CombatForce = 0.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
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

