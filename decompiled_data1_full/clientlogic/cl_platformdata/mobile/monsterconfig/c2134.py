# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2134.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2134.pyc
# Source Generated with Decompyle++
# File: c2134.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2134
    m_Shape = 2134
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21341
    m_PerformList = (21342, 4111, 5347, 5370)
    m_Betree = 'MonsterMediumNear.dashNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumNear.dashNearFsm' },
        'Common': {
            64: 'Common.GlobalAreaMoveFsm',
            128: 'Common.GlobalAreaMoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21341 },
        (1, 2): {
            'PFAI': 21341 },
        (0, 3): {
            'PFAI': 21341 },
        (1, 1): {
            'PFAI': 21341 },
        (0, 2): {
            'PFAI': 21341 },
        (0, 1): {
            'PFAI': 21341 } }
    m_CombatForce = 1.5
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
    m_AttackCost = 3
    m_ExtraAIArgs = {
        'FightMinDis': 7,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

