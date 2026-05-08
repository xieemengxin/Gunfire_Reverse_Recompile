# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3001.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3001.pyc
# Source Generated with Decompyle++
# File: c3001.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_ELIBADGER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3001
    m_Shape = 3001
    m_FightType = WARRIOR_ELIBADGER
    m_AttPerform = 30011
    m_PerformList = (30012, 4111)
    m_Betree = 'EliteNear.EliteSmallNearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteNear.EliteSmallNearFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4074 }
    m_PhaseHitPartToType = {
        1: { } }
    m_AttrPlusPF = (6201,)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 30011 },
        (1, 0): {
            'PFAI': 30011 },
        (0, 2): {
            'PFAI': 30011 },
        (0, 1): {
            'PFAI': 30011 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1010
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

