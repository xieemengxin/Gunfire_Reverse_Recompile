# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3902.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3902.pyc
# Source Generated with Decompyle++
# File: c3902.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSSSTAT
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3902
    m_Shape = 3902
    m_FightType = WARRIOR_BOSSSTAT
    m_AttPerform = 39021
    m_PerformList = (39026, 39022, 39023, 39024, 39025, 4111, 4074, 39027, 4308, 39028, 39029, 39121, 39122, 39123, 4315, 4316, 4320, 4380)
    m_Betree = 'BossLuoHou.bossLuoHouFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossLuoHou.bossLuoHouFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4108,
        2: 4109,
        3: 4110 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39021 },
        (1, 2): {
            'PFAI': 39021 },
        (0, 3): {
            'PFAI': 39021 },
        (1, 1): {
            'PFAI': 39021 },
        (0, 2): {
            'PFAI': 39021 },
        (0, 1): {
            'PFAI': 39021 } }
    m_CombatForce = 0
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

