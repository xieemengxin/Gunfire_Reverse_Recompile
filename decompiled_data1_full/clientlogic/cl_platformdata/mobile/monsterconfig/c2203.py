# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2203.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2203.pyc
# Source Generated with Decompyle++
# File: c2203.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2203
    m_Shape = 2203
    m_FightType = WARRIOR_NORHEVFAR
    m_AttPerform = 22032
    m_PerformList = (22031, 22033, 22034, 4107, 4111)
    m_Betree = 'MonsterLargeFar.LargeFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterLargeFar.LargeFarFsm' },
        'Common': {
            2: 'Common.FuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22033 },
        (1, 2): {
            'PFAI': 22032 },
        (0, 3): {
            'PFAI': 22033 },
        (1, 1): {
            'PFAI': 22031 },
        (0, 2): {
            'PFAI': 22032 },
        (0, 1): {
            'PFAI': 22031 } }
    m_CombatForce = 1.5
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
    m_ExtraAIArgs = { }

