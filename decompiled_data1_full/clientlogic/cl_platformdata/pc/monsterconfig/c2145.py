# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2145.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2145.pyc
# Source Generated with Decompyle++
# File: c2145.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2145
    m_Shape = 2145
    m_FightType = WARRIOR_NORMEDFAR
    m_AttPerform = 21432
    m_PerformList = (21451, 21452, 38033, 38034, 21453, 21454, 21455)
    m_Betree = 'MonsterMediumFar.MediumFarFuzzyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumFar.MediumFarFuzzyFsm' },
        'Common': {
            2: 'MonsterMediumFar.MediumFarAreamoveFsm',
            128: 'MonsterMediumFar.SurvivalMediumFarAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21453 },
        (1, 2): {
            'PFAI': 21452 },
        (0, 3): {
            'PFAI': 21453 },
        (1, 1): {
            'PFAI': 21451 },
        (0, 2): {
            'PFAI': 21452 },
        (0, 1): {
            'PFAI': 21451 } }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

