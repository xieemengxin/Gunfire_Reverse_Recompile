# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3242.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3242.pyc
# Source Generated with Decompyle++
# File: c3242.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_ELIDART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3242
    m_Shape = 3242
    m_FightType = WARRIOR_ELIDART
    m_AttPerform = 32421
    m_PerformList = (32424, 32423, 32422, 38028, 38029, 38030, 4111)
    m_Betree = 'EliteFar.throwEliteFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.throwEliteFsm' },
        'Common': {
            1: 'EliteFar.throwEliteFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 32421 },
        (1, 0): {
            'PFAI': 32421 },
        (0, 2): {
            'PFAI': 32421 },
        (0, 1): {
            'PFAI': 32421 } }
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
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6114, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

