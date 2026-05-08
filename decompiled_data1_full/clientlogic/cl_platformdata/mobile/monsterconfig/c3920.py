# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3920.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3920.pyc
# Source Generated with Decompyle++
# File: c3920.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3920
    m_Shape = 3920
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 0
    m_PerformList = (39201, 39203, 39202, 4205, 39205, 4111, 39206, 39207, 39208, 39209, 4267)
    m_Betree = 'BossSeaMonster.bossSeaMonsterFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossSeaMonster.bossSeaMonsterFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4202,
        2: 4203,
        3: 4204 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = {
        (1, 3): {
            'PFAI': 39203 },
        (1, 2): {
            'PFAI': 39202 },
        (1, 1): {
            'PFAI': 39201 },
        (0, 3): {
            'PFAI': 39203 },
        (0, 2): {
            'PFAI': 39202 },
        (0, 1): {
            'PFAI': 39201 } }
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

