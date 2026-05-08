# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3165.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3165.pyc
# Source Generated with Decompyle++
# File: c3165.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_NORSNIPE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3165
    m_Shape = 3165
    m_FightType = WARRIOR_NORSNIPE
    m_AttPerform = 31651
    m_PerformList = (31652, 4111, 4074, 31643, 4253)
    m_Betree = 'EliteFar.EliteSniperIllusionFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.EliteSniperIllusionFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31651 },
        (1, 0): {
            'PFAI': 31651 },
        (0, 2): {
            'PFAI': 31651 },
        (0, 1): {
            'PFAI': 31651 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
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
    m_ExtraAIArgs = { }

