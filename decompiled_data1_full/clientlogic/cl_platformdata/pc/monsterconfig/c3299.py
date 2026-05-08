# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3299.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3299.pyc
# Source Generated with Decompyle++
# File: c3299.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMAGIC
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3299
    m_Shape = 3299
    m_FightType = WARRIOR_NORMAGIC
    m_AttPerform = 32823
    m_PerformList = (4133, 32821, 32822, 4111, 4074, 4147)
    m_Betree = 'EliteFar.SummonCloneEliteFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.SummonCloneEliteFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 32822 },
        (1, 0): {
            'PFAI': 32822 },
        (0, 2): {
            'PFAI': 32822 },
        (0, 1): {
            'PFAI': 32822 } }
    m_CombatForce = 5
    m_BornActionInfo = {
        'Show': 143 }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6114, 6107)
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = (6154, 6155, 6156, 6158, 6160, 6161, 6163, 6162, 6165, 6157)
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

