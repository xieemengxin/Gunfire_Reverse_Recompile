# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c3914.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c3914.pyc
# Source Generated with Decompyle++
# File: c3914.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3914
    m_Shape = 3912
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 39134
    m_PerformList = (4055, 39131, 39132, 39133, 39135, 39136, 39137, 39138, 39139, 39140, 39141, 39142)
    m_Betree = 'BossDesert.bossDesertFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossDesert.bossDesertFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4056,
        2: 4057,
        3: 4058,
        4: 4059,
        5: 4065 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { },
        4: { },
        5: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39131 },
        (1, 0): {
            'PFAI': 39131 },
        (0, 2): {
            'PFAI': 39131 },
        (0, 1): {
            'PFAI': 39131 } }
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
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

