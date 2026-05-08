# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2301.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2301.pyc
# Source Generated with Decompyle++
# File: c2301.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORDART
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2301
    m_Shape = 2301
    m_FightType = WARRIOR_NORDART
    m_AttPerform = 23011
    m_PerformList = (23012, 23013)
    m_Betree = 'MonsterFly.FlyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFly.FlyFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 23011 },
        (1, 0): {
            'PFAI': 23011 },
        (0, 2): {
            'PFAI': 23011 },
        (0, 1): {
            'PFAI': 23011 } }
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

