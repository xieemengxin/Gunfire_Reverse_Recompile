# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3907.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3907.pyc
# Source Generated with Decompyle++
# File: c3907.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_SHIELD, DAM_TYPE_WEAKNESS, DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MONSTER_PART_ELBOWLEFT, MONSTER_PART_ELBOWRIGHT, MONSTER_PART_STOMACH, MONSTER_PART_UNDERLEFT, MONSTER_PART_UNDERRIGHT, MONSTER_PART_UPPERBODY, MONSTER_PART_UPPERLEFT, MONSTER_PART_UPPERRIGHT, MONSTER_PART_WEAKNESS, WARRIOR_BOSSSTAT
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3907
    m_Shape = 3902
    m_FightType = WARRIOR_BOSSSTAT
    m_AttPerform = 39071
    m_PerformList = (39071, 39072, 39073, 39074, 39075, 39076, 39077, 39078)
    m_Betree = 'BossLuoHou.bossLuoHouFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossLuoHou.bossLuoHouFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4108,
        2: 4109,
        3: 4110 }
    m_PhaseHitPartToType = {
        1: {
            MONSTER_PART_UPPERBODY: DAM_TYPE_SHIELD,
            MONSTER_PART_ELBOWRIGHT: DAM_TYPE_WEAKNESS,
            MONSTER_PART_ELBOWLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_WEAKNESS: DAM_TYPE_SHIELD,
            MONSTER_PART_UPPERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UPPERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_STOMACH: DAM_TYPE_SHIELD },
        2: {
            MONSTER_PART_UPPERBODY: DAM_TYPE_SHIELD,
            MONSTER_PART_ELBOWRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_ELBOWLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_WEAKNESS: DAM_TYPE_WEAKNESS,
            MONSTER_PART_UPPERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UPPERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_STOMACH: DAM_TYPE_SHIELD },
        3: {
            MONSTER_PART_UPPERBODY: DAM_TYPE_SHIELD,
            MONSTER_PART_ELBOWRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_ELBOWLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UNDERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_WEAKNESS: DAM_TYPE_SHIELD,
            MONSTER_PART_UPPERRIGHT: DAM_TYPE_SHIELD,
            MONSTER_PART_UPPERLEFT: DAM_TYPE_SHIELD,
            MONSTER_PART_STOMACH: DAM_TYPE_WEAKNESS } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39071 },
        (1, 0): {
            'PFAI': 39071 },
        (0, 2): {
            'PFAI': 39071 },
        (0, 1): {
            'PFAI': 39071 } }
    m_CombatForce = 10
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }

