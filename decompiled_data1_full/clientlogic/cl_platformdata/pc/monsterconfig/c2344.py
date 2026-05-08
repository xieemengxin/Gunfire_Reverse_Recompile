# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2344.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2344.pyc
# Source Generated with Decompyle++
# File: c2344.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_NORBOX
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2344
    m_Shape = 2344
    m_FightType = WARRIOR_NORBOX
    m_AttPerform = 20011
    m_PerformList = (4300, 4163)
    m_Betree = 'MonsterNear.BoxNearNewFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.BoxNearNewFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 23411 },
        (1, 0): {
            'PFAI': 23411 },
        (0, 2): {
            'PFAI': 23411 },
        (0, 1): {
            'PFAI': 23411 } }
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
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

