# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2201.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2201.pyc
# Source Generated with Decompyle++
# File: c2201.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2201
    m_Shape = 2201
    m_FightType = WARRIOR_NORHEVFAR
    m_AttPerform = 22011
    m_PerformList = (22012, 22013, 38013, 4063, 4111)
    m_Betree = 'MonsterNear.MonsterFireFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.MonsterFireFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 22013 },
        (1, 2): {
            'PFAI': 22012 },
        (0, 3): {
            'PFAI': 22013 },
        (1, 1): {
            'PFAI': 22011 },
        (0, 2): {
            'PFAI': 22012 },
        (0, 1): {
            'PFAI': 22011 } }
    m_CombatForce = 1.25
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
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

