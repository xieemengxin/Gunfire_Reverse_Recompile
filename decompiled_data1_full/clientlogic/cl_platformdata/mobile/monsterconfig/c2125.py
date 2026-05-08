# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2125.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2125.pyc
# Source Generated with Decompyle++
# File: c2125.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2125
    m_Shape = 2125
    m_FightType = WARRIOR_NORMEDNEAR
    m_AttPerform = 21251
    m_PerformList = (21252, 21253, 4045, 4111, 4125)
    m_Betree = 'MonsterBigShield.DesertShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterBigShield.DesertShieldFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21253 },
        (1, 2): {
            'PFAI': 21252 },
        (0, 3): {
            'PFAI': 21253 },
        (1, 1): {
            'PFAI': 21251 },
        (0, 2): {
            'PFAI': 21252 },
        (0, 1): {
            'PFAI': 21251 } }
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

