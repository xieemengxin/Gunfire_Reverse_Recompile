# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2097.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2097.pyc
# Source Generated with Decompyle++
# File: c2097.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2097
    m_Shape = 2097
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 20811
    m_PerformList = (20812, 38021, 38022)
    m_Betree = 'GuideScene.NearSquatFsm'
    m_BetreeMap = {
        'Default': {
            0: 'GuideScene.NearSquatFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20811 },
        (1, 0): {
            'PFAI': 20811 },
        (0, 2): {
            'PFAI': 20811 },
        (0, 1): {
            'PFAI': 20811 } }
    m_CombatForce = 0.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = {
        1: 200,
        2: 200,
        3: 100 }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

