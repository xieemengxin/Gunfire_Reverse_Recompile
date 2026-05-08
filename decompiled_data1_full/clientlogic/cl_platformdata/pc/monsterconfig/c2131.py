# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2131.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2131.pyc
# Source Generated with Decompyle++
# File: c2131.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_EASY, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2131
    m_Shape = 2131
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21312
    m_PerformList = (4111, 21311, 4400)
    m_Betree = 'MonsterBigShield.DesertAntShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterBigShield.DesertAntShieldFsm' },
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
            'PFAI': 21313 },
        (1, 2): {
            'PFAI': 21312 },
        (0, 3): {
            'PFAI': 21313 },
        (1, 1): {
            'PFAI': 21311 },
        (0, 2): {
            'PFAI': 21312 },
        (0, 1): {
            'PFAI': 21311 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_EASY,
        2: MISSING_DIS_EASY,
        3: MISSING_DIS_EASY }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

