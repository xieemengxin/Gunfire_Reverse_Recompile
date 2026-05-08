# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3905.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3905.pyc
# Source Generated with Decompyle++
# File: c3905.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSSDM
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3905
    m_Shape = 3915
    m_FightType = WARRIOR_BOSSDM
    m_AttPerform = 0
    m_PerformList = (39051, 39054, 39056, 39057, 4087, 39060, 39065, 39055, 39066, 4266, 4273)
    m_Betree = 'BossShip.bossShipFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossShip.bossShipFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4090,
        2: 4091,
        3: 4092,
        4: 4093,
        5: 4094,
        6: 4095,
        7: 4096 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { },
        5: { },
        6: { },
        7: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39053 },
        (0, 2): {
            'PFAI': 39052 },
        (1, 0): {
            'PFAI': 39053 },
        (0, 1): {
            'PFAI': 39051 } }
    m_CombatForce = 1
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
    m_ExtraAIArgs = { }

