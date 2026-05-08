# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3300.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3300.pyc
# Source Generated with Decompyle++
# File: c3300.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_ELIMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3300
    m_Shape = 3300
    m_FightType = WARRIOR_ELIMEDNEAR
    m_AttPerform = 31261
    m_PerformList = (31263, 31262, 31264, 38033, 38034, 4111, 4074)
    m_Betree = 'EliteNear.EliteMediumNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteMediumNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4126,
        2: 4127 }
    m_PhaseHitPartToType = {
        1: { },
        2: { } }
    m_AttrPlusPF = (6204, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 31261 },
        (1, 0): {
            'PFAI': 31261 },
        (0, 2): {
            'PFAI': 31261 },
        (0, 1): {
            'PFAI': 31261 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1012
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6107)
    m_SurvivorAttrPlus = (6253, 6254)
    m_SurvivorBanPF = (6154, 6155, 6156, 6158, 6160, 6161, 6163, 6162, 6165, 6157)
    m_AttackCost = 1
    m_ExtraAIArgs = { }

