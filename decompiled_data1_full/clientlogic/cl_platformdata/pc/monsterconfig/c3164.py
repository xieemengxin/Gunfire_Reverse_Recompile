# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3164.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3164.pyc
# Source Generated with Decompyle++
# File: c3164.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_ELISNIPE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3164
    m_Shape = 3164
    m_FightType = WARRIOR_ELISNIPE
    m_AttPerform = 31642
    m_PerformList = (31641, 31644, 31643, 4111, 4074, 4252)
    m_Betree = 'EliteFar.EliteSniperFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.EliteSniperFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31641 },
        (1, 0): {
            'PFAI': 31641 },
        (0, 2): {
            'PFAI': 31641 },
        (0, 1): {
            'PFAI': 31641 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1022
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

