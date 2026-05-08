# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2107.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2107.pyc
# Source Generated with Decompyle++
# File: c2107.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORPETRO
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2107
    m_Shape = 2107
    m_FightType = WARRIOR_NORPETRO
    m_AttPerform = 21021
    m_PerformList = (21023, 21024, 38012, 21022, 4044, 4120)
    m_Betree = 'MonsterShield.farShieldFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterShield.farShieldFsm' },
        'Common': {
            2: 'MonsterShield.farShieldAreaFsm',
            1: 'MonsterShield.farShieldFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 21021 },
        (1, 0): {
            'PFAI': 21021 },
        (0, 2): {
            'PFAI': 21021 },
        (0, 1): {
            'PFAI': 21021 } }
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
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

