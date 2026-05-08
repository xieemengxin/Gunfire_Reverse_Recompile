# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2144.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2144.pyc
# Source Generated with Decompyle++
# File: c2144.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORPETRO
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2144
    m_Shape = 2144
    m_FightType = WARRIOR_NORPETRO
    m_AttPerform = 21412
    m_PerformList = (21411, 38012, 38021, 38022, 4120)
    m_Betree = 'MonsterMediumFar.MediumFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumFar.MediumFarFsm' },
        'Common': {
            1: 'MonsterMediumFar.MediumFarFsm',
            16: 'MonsterMediumFar.MediumFarFuzzyFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 21411 },
        (1, 0): {
            'PFAI': 21411 },
        (0, 2): {
            'PFAI': 21411 },
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
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

