# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3915.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3915.pyc
# Source Generated with Decompyle++
# File: c3915.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3915
    m_Shape = 3917
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 39157
    m_PerformList = (39161, 39151, 39153, 39152, 39154, 39155, 39156, 39160, 4111, 4268)
    m_Betree = 'BossTornado.bossTornadoFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossTornado.bossTornadoFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4182,
        2: 4183,
        3: 4184 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39151 },
        (1, 0): {
            'PFAI': 39152 },
        (0, 2): {
            'PFAI': 39151 },
        (0, 1): {
            'PFAI': 39151 } }
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

