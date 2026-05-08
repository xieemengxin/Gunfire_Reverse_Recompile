# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3283.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3283.pyc
# Source Generated with Decompyle++
# File: c3283.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_ELIMAGIC
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3283
    m_Shape = 3283
    m_FightType = WARRIOR_ELIMAGIC
    m_AttPerform = 32831
    m_PerformList = (32832, 32833, 32834, 4088, 32835, 32836, 32837, 32838, 4111)
    m_Betree = 'EliteFar.BloodEliteFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.BloodEliteFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 32831 },
        (1, 0): {
            'PFAI': 32831 },
        (0, 2): {
            'PFAI': 32831 },
        (0, 1): {
            'PFAI': 32831 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1012
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6114, 6109, 6107)
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = (6154, 6155, 6156, 6158, 6160, 6161, 6163, 6162, 6165, 6157)
    m_AttackCost = 1
    m_ExtraAIArgs = { }

