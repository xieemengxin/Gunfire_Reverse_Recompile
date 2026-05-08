# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2119.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2119.pyc
# Source Generated with Decompyle++
# File: c2119.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_EASY, MISSING_DIS_NORMAL, WARRIOR_NORSMAFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2119
    m_Shape = 2119
    m_FightType = WARRIOR_NORSMAFAR
    m_AttPerform = 21011
    m_PerformList = (38011, 38021, 38022)
    m_Betree = 'GuideScene.FarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'GuideScene.FarFsm' },
        'Common': {
            2: 'GuideScene.FarFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 21011 },
        (1, 0): {
            'PFAI': 21011 },
        (0, 2): {
            'PFAI': 21011 },
        (0, 1): {
            'PFAI': 21011 } }
    m_CombatForce = 0.75
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1.2
    m_MissingDisType = {
        1: MISSING_DIS_EASY,
        2: MISSING_DIS_EASY,
        3: MISSING_DIS_NORMAL }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

