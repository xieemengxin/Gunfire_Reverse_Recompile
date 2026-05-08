# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2089.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2089.pyc
# Source Generated with Decompyle++
# File: c2089.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2089
    m_Shape = 2089
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 20891
    m_PerformList = (20892, 38036, 38037, 38038, 20893, 20894, 20897, 20898, 20899)
    m_Betree = 'MonsterNear.nearMonkeyFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.nearMonkeyFsm' },
        'Common': {
            1: 'MonsterNear.nearMonkeyFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 20891 },
        (1, 2): {
            'PFAI': 20891 },
        (1, 1): {
            'PFAI': 20891 },
        (0, 3): {
            'PFAI': 20891 },
        (0, 2): {
            'PFAI': 20891 },
        (0, 1): {
            'PFAI': 20891 } }
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

