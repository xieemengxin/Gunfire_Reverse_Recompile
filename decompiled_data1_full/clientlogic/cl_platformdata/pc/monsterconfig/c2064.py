# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2064.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2064.pyc
# Source Generated with Decompyle++
# File: c2064.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORTHROW
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2064
    m_Shape = 2064
    m_FightType = WARRIOR_NORTHROW
    m_AttPerform = 20641
    m_PerformList = (38021, 38022)
    m_Betree = 'MonsterFar.handbombGuerrillaFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.handbombGuerrillaFsm' },
        'Common': {
            2: 'MonsterFar.handbombAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20641 },
        (1, 0): {
            'PFAI': 20641 },
        (0, 2): {
            'PFAI': 20641 },
        (0, 1): {
            'PFAI': 20641 } }
    m_CombatForce = 0.75
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

