# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3422.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3422.pyc
# Source Generated with Decompyle++
# File: c3422.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3422
    m_Shape = 3421
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 34211
    m_PerformList = (34212, 34213, 34214, 4111, 4387)
    m_Betree = 'MonsterSpider.EliteSpiderFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterSpider.EliteSpiderFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6201,)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 34213 },
        (0, 3): {
            'PFAI': 34213 },
        (1, 2): {
            'PFAI': 34212 },
        (0, 2): {
            'PFAI': 34211 },
        (1, 1): {
            'PFAI': 34212 },
        (0, 1): {
            'PFAI': 34211 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1011
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

