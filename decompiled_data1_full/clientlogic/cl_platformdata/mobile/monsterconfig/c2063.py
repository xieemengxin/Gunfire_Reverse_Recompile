# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2063.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2063.pyc
# Source Generated with Decompyle++
# File: c2063.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORTHROW
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2063
    m_Shape = 2063
    m_FightType = WARRIOR_NORTHROW
    m_AttPerform = 20631
    m_PerformList = (38021, 38022)
    m_Betree = 'MonsterFar.handbombGuerrillaFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFar.handbombGuerrillaFsm' },
        'Common': {
            2: 'MonsterFar.handbombAreamoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20631 },
        (1, 0): {
            'PFAI': 20631 },
        (0, 2): {
            'PFAI': 20631 },
        (0, 1): {
            'PFAI': 20631 } }
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

