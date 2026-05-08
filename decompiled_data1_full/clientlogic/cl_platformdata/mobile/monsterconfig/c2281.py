# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2281.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2281.pyc
# Source Generated with Decompyle++
# File: c2281.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMAGIC
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2281
    m_Shape = 2281
    m_FightType = WARRIOR_NORMAGIC
    m_AttPerform = 22813
    m_PerformList = ()
    m_Betree = 'MonsterWizard.WizardFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterWizard.WizardFsm' },
        'Common': {
            2: 'Common.FuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22813 },
        (1, 2): {
            'PFAI': 22812 },
        (0, 3): {
            'PFAI': 22813 },
        (1, 1): {
            'PFAI': 22811 },
        (0, 2): {
            'PFAI': 22812 },
        (0, 1): {
            'PFAI': 22811 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = {
        1: 200,
        2: 200,
        3: 100 }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6253, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

