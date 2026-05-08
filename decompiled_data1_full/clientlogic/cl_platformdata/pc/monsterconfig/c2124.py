# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2124.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2124.pyc
# Source Generated with Decompyle++
# File: c2124.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2124
    m_Shape = 2124
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21241
    m_PerformList = (38012, 4111, 4363)
    m_Betree = 'MonsterMediumNear.shotgunfsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumNear.shotgunfsm' },
        'Common': {
            64: 'Common.GlobalAreaMoveFsm',
            128: 'Common.GlobalAreaMoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21243 },
        (1, 2): {
            'PFAI': 21242 },
        (0, 3): {
            'PFAI': 21243 },
        (1, 1): {
            'PFAI': 21241 },
        (0, 2): {
            'PFAI': 21242 },
        (0, 1): {
            'PFAI': 21241 } }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 2
    m_ExtraAIArgs = {
        'FightMinDis': 7,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

