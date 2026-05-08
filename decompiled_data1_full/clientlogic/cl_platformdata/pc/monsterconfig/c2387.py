# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2387.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2387.pyc
# Source Generated with Decompyle++
# File: c2387.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORRIDE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2387
    m_Shape = 2387
    m_FightType = WARRIOR_NORRIDE
    m_AttPerform = 23871
    m_PerformList = (23820,)
    m_Betree = 'MonsterRide.KnightFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterRide.KnightFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = {
        (1, 3): {
            'PFAI': 23871 },
        (1, 2): {
            'PFAI': 23871 },
        (0, 3): {
            'PFAI': 23871 },
        (1, 1): {
            'PFAI': 23871 },
        (0, 2): {
            'PFAI': 23871 },
        (0, 1): {
            'PFAI': 23871 } }
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
    m_BanPF = (6110,)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

