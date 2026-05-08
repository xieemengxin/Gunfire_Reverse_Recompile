# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3381.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3381.pyc
# Source Generated with Decompyle++
# File: c3381.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_HARDNESS, DAM_TYPE_WEAKNESS, DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MONSTER_PART_ATTACH_HARDNESS, MONSTER_PART_ATTACH_WEAKNESS, WARRIOR_ELIRIDE
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3381
    m_Shape = 3381
    m_FightType = WARRIOR_ELIRIDE
    m_AttPerform = 33814
    m_PerformList = (4111, 4238, 33812, 33813, 33811, 33815, 33816, 33817, 4074, 33818, 23820)
    m_Betree = 'EliteFar.EliteRideFsm'
    m_BetreeMap = {
        'Default': {
            0: 'EliteFar.EliteRideFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        2: 4239 }
    m_PhaseHitPartToType = {
        1: {
            MONSTER_PART_ATTACH_HARDNESS: DAM_TYPE_HARDNESS,
            MONSTER_PART_ATTACH_WEAKNESS: DAM_TYPE_WEAKNESS },
        2: {
            MONSTER_PART_ATTACH_HARDNESS: DAM_TYPE_HARDNESS,
            MONSTER_PART_ATTACH_WEAKNESS: DAM_TYPE_WEAKNESS } }
    m_AttrPlusPF = (6204, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 33811 },
        (1, 2): {
            'PFAI': 33811 },
        (0, 3): {
            'PFAI': 33811 },
        (1, 1): {
            'PFAI': 33811 },
        (0, 2): {
            'PFAI': 33811 },
        (0, 1): {
            'PFAI': 33811 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 75
    m_CreateEffect = 1022
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = (6104, 6105, 6106, 6108, 6110, 6111, 6112, 6115, 6114, 6107)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 20,
        'WaitPatrolRadius': 4 }

