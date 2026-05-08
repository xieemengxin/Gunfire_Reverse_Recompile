# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2422.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2422.pyc
# Source Generated with Decompyle++
# File: c2422.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORHEVNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2422
    m_Shape = 2422
    m_FightType = WARRIOR_NORHEVNEAR
    m_AttPerform = 24221
    m_PerformList = (4111, 24222, 24223, 24224)
    m_Betree = 'MonsterSpider.SpiderFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSpider.SpiderFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201,)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 24223 },
        (0, 3): {
            'PFAI': 24223 },
        (1, 2): {
            'PFAI': 24222 },
        (0, 2): {
            'PFAI': 24222 },
        (1, 1): {
            'PFAI': 24221 },
        (0, 1): {
            'PFAI': 24221 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
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

