# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2122.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2122.pyc
# Source Generated with Decompyle++
# File: c2122.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2122
    m_Shape = 2122
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21223
    m_PerformList = (21221, 21222, 4062, 4111)
    m_Betree = 'MonsterMediumNear.armourNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumNear.armourNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21223 },
        (1, 2): {
            'PFAI': 21222 },
        (0, 3): {
            'PFAI': 21222 },
        (1, 1): {
            'PFAI': 21221 },
        (0, 2): {
            'PFAI': 21222 },
        (0, 1): {
            'PFAI': 21221 } }
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
    m_AttackCost = 1
    m_ExtraAIArgs = { }

