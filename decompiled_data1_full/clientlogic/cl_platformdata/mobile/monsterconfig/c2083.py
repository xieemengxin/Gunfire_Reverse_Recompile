# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2083.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2083.pyc
# Source Generated with Decompyle++
# File: c2083.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORSMANEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2083
    m_Shape = 2083
    m_FightType = WARRIOR_NORSMANEAR
    m_AttPerform = 20832
    m_PerformList = (20831, 38021, 38022, 20834)
    m_Betree = 'MonsterNear.nearFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.nearFsm' },
        'Common': {
            1: 'MonsterNear.nearFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 20833 },
        (1, 2): {
            'PFAI': 20832 },
        (0, 3): {
            'PFAI': 20833 },
        (1, 1): {
            'PFAI': 20831 },
        (0, 2): {
            'PFAI': 20832 },
        (0, 1): {
            'PFAI': 20831 } }
    m_CombatForce = 0.75
    m_BornActionInfo = {
        'Show': 130 }
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

