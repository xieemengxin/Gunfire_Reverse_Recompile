# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3909.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3909.pyc
# Source Generated with Decompyle++
# File: c3909.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3909
    m_Shape = 3913
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 39091
    m_PerformList = (39092, 39093, 39094, 39095, 39096, 4152)
    m_Betree = 'BossStoneGiant.bossStoneGiantFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossStoneGiant.bossStoneGiantFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4153,
        2: 4154,
        3: 4155,
        4: 4156 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39093 },
        (1, 2): {
            'PFAI': 39092 },
        (0, 3): {
            'PFAI': 39093 },
        (1, 1): {
            'PFAI': 39091 },
        (0, 2): {
            'PFAI': 39092 },
        (0, 1): {
            'PFAI': 39091 } }
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
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

