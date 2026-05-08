# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2141.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2141.pyc
# Source Generated with Decompyle++
# File: c2141.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2141
    m_Shape = 2141
    m_FightType = WARRIOR_NORMEDFAR
    m_AttPerform = 21412
    m_PerformList = (21411, 38012, 38021, 38022)
    m_Betree = 'MonsterMediumFar.MediumFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumFar.MediumFarFsm' },
        'Common': {
            1: 'MonsterMediumFar.MediumFarFsm',
            16: 'MonsterMediumFar.MediumFarFuzzyFsm',
            2: 'MonsterMediumFar.MediumFarAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21413 },
        (1, 2): {
            'PFAI': 21412 },
        (0, 3): {
            'PFAI': 21413 },
        (1, 1): {
            'PFAI': 21411 },
        (0, 2): {
            'PFAI': 21412 },
        (0, 1): {
            'PFAI': 21411 } }
    m_CombatForce = 1
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
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 15,
        'WaitPatrolRadius': 4 }

