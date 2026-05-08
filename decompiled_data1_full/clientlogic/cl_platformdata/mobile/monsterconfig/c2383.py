# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2383.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2383.pyc
# Source Generated with Decompyle++
# File: c2383.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_HARDNESS, DAM_TYPE_WEAKNESS, DEFEND_TREND_NONE, MISSING_DIS_HARD, MISSING_DIS_NORMAL, MONSTER_PART_ATTACH_HARDNESS, MONSTER_PART_ATTACH_WEAKNESS, WARRIOR_NORRIDE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2383
    m_Shape = 2383
    m_FightType = WARRIOR_NORRIDE
    m_AttPerform = 23811
    m_PerformList = (4111, 4222, 23812, 23813, 23814, 23815, 23816, 23817, 23819, 23818, 23820)
    m_Betree = 'MonsterRide.RideFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterRide.RideFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        2: 4224,
        3: 4225 }
    m_PhaseHitPartToType = {
        1: {
            MONSTER_PART_ATTACH_HARDNESS: DAM_TYPE_HARDNESS,
            MONSTER_PART_ATTACH_WEAKNESS: DAM_TYPE_WEAKNESS },
        2: {
            MONSTER_PART_ATTACH_HARDNESS: DAM_TYPE_HARDNESS,
            MONSTER_PART_ATTACH_WEAKNESS: DAM_TYPE_WEAKNESS },
        3: {
            MONSTER_PART_ATTACH_HARDNESS: DAM_TYPE_HARDNESS,
            MONSTER_PART_ATTACH_WEAKNESS: DAM_TYPE_WEAKNESS } }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_NONE
    m_AIConfig = {
        (1, 3): {
            'PFAI': 23811 },
        (1, 2): {
            'PFAI': 23811 },
        (0, 3): {
            'PFAI': 23811 },
        (1, 1): {
            'PFAI': 23811 },
        (0, 2): {
            'PFAI': 23811 },
        (0, 1): {
            'PFAI': 23811 } }
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
    m_BanPF = (6110,)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

