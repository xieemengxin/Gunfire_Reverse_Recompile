# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2022.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2022.pyc
# Source Generated with Decompyle++
# File: c2022.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORFOOT
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2022
    m_Shape = 2022
    m_FightType = WARRIOR_NORFOOT
    m_AttPerform = 20221
    m_PerformList = (20222, 20223, 38028, 38029, 20225, 4176, 20226)
    m_Betree = 'MonsterFourLeg.fourInvisibleFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterFourLeg.fourInvisibleFsm' },
        'Common': { } }
    m_DefaultPhase = 2
    m_PhasePF = {
        1: 4173,
        2: 4174 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20221 },
        (1, 0): {
            'PFAI': 20221 },
        (0, 2): {
            'PFAI': 20221 },
        (0, 1): {
            'PFAI': 20221 } }
    m_CombatForce = 1
    m_BornActionInfo = {
        'Show': 100 }
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

