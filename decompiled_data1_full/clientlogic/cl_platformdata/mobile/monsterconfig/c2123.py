# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2123.pyc
# Source Generated with Decompyle++
# File: c2123.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2123
    m_Shape = 2123
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21231
    m_PerformList = (21232, 4045, 4111)
    m_Betree = 'MonsterBigShield.bigShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterBigShield.bigShieldFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21233 },
        (1, 2): {
            'PFAI': 21232 },
        (0, 3): {
            'PFAI': 21233 },
        (1, 1): {
            'PFAI': 21231 },
        (0, 2): {
            'PFAI': 21232 },
        (0, 1): {
            'PFAI': 21231 } }
    m_CombatForce = 1.25
    m_BornActionInfo = {
        'Show': 135 }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

