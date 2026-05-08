# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2109.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2109.pyc
# Source Generated with Decompyle++
# File: c2109.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_EASY, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMAFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2109
    m_Shape = 2109
    m_FightType = WARRIOR_NORSMAFAR
    m_AttPerform = 21091
    m_PerformList = (38020, 38036, 38037)
    m_Betree = 'MonsterFar.farFuzzyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.farFuzzyFsm' },
        'Common': {
            1: 'MonsterFar.farGuerrillaFsm',
            2: 'MonsterFar.farAreamoveFsm',
            4: 'MonsterFar.farCoverFsm',
            8: 'MonsterFar.farHideFsm',
            16: 'MonsterFar.farFuzzyFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21093 },
        (1, 2): {
            'PFAI': 21092 },
        (1, 1): {
            'PFAI': 21091 },
        (0, 3): {
            'PFAI': 21093 },
        (0, 2): {
            'PFAI': 21092 },
        (0, 1): {
            'PFAI': 21091 } }
    m_CombatForce = 0.75
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_EASY,
        2: MISSING_DIS_NORMAL,
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

