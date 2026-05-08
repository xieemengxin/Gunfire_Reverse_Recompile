# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2244.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2244.pyc
# Source Generated with Decompyle++
# File: c2244.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORDART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2244
    m_Shape = 2244
    m_FightType = WARRIOR_NORDART
    m_AttPerform = 22441
    m_PerformList = (22442, 22423, 38028, 38029, 38030)
    m_Betree = 'MonsterFar.throwFuzzyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.throwFuzzyFsm' },
        'Common': {
            2: 'MonsterFar.throwFuzzyAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22443 },
        (1, 2): {
            'PFAI': 22442 },
        (0, 3): {
            'PFAI': 22443 },
        (1, 1): {
            'PFAI': 22441 },
        (0, 2): {
            'PFAI': 22442 },
        (0, 1): {
            'PFAI': 22441 } }
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
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

