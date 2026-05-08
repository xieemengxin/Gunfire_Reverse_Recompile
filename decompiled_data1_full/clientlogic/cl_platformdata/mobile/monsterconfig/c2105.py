# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2105.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2105.pyc
# Source Generated with Decompyle++
# File: c2105.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMAFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2105
    m_Shape = 2105
    m_FightType = WARRIOR_NORSMAFAR
    m_AttPerform = 21051
    m_PerformList = (38019, 38031, 38032)
    m_Betree = 'MonsterFar.farFuzzyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.farFuzzyFsm' },
        'Common': {
            2: 'MonsterFar.farAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21053 },
        (1, 2): {
            'PFAI': 21052 },
        (0, 3): {
            'PFAI': 21053 },
        (1, 1): {
            'PFAI': 21051 },
        (0, 2): {
            'PFAI': 21052 },
        (0, 1): {
            'PFAI': 21051 } }
    m_CombatForce = 0.75
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
    m_SurvivorAttrPlus = (6251, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

