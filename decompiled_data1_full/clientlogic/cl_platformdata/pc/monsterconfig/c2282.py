# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2282.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2282.pyc
# Source Generated with Decompyle++
# File: c2282.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMAGIC
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2282
    m_Shape = 2282
    m_FightType = WARRIOR_NORMAGIC
    m_AttPerform = 22821
    m_PerformList = (4084, 22822)
    m_Betree = 'MonsterWizard.WizardFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterWizard.WizardFsm' },
        'Common': {
            2: 'Common.FuzzyAreamoveFsm',
            128: 'MonsterWizard.SurvivalWizardFsm',
            64: 'MonsterWizard.SurvivalWizardFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 22821 },
        (1, 0): {
            'PFAI': 22821 },
        (0, 2): {
            'PFAI': 22821 },
        (0, 1): {
            'PFAI': 22821 } }
    m_CombatForce = 2
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6109,)
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = (6159, 6157)
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

