# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2112.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2112.pyc
# Source Generated with Decompyle++
# File: c2112.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_NORSMAFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2112
    m_Shape = 2112
    m_FightType = WARRIOR_NORSMAFAR
    m_AttPerform = 21061
    m_PerformList = (38012, 38031, 38032, 21121, 21122, 5310, 21123, 21124)
    m_Betree = 'MonsterShield.SeaShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterShield.SeaShieldFsm' },
        'Common': {
            2: 'MonsterShield.SeaShieldAreaFsm',
            128: 'MonsterFar.SurvivalfarAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21123 },
        (1, 2): {
            'PFAI': 21122 },
        (0, 3): {
            'PFAI': 21123 },
        (1, 1): {
            'PFAI': 21121 },
        (0, 2): {
            'PFAI': 21122 },
        (0, 1): {
            'PFAI': 21121 } }
    m_CombatForce = 0.75
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6251, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

