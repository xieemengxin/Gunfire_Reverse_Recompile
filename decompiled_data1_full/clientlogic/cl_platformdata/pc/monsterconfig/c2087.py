# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2087.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2087.pyc
# Source Generated with Decompyle++
# File: c2087.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2087
    m_Shape = 2087
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 20871
    m_PerformList = (20872, 38031, 38032, 38035)
    m_Betree = 'MonsterNear.NearSwordFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.NearSwordFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 20873 },
        (1, 2): {
            'PFAI': 20872 },
        (0, 3): {
            'PFAI': 20873 },
        (1, 1): {
            'PFAI': 20871 },
        (0, 2): {
            'PFAI': 20872 },
        (0, 1): {
            'PFAI': 20871 } }
    m_CombatForce = 0.5
    m_BornActionInfo = {
        'Show': 80 }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6251, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

