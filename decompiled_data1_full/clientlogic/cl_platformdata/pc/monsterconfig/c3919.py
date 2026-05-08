# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c3919.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c3919.pyc
# Source Generated with Decompyle++
# File: c3919.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_BOSS
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 3919
    m_Shape = 3919
    m_FightType = WARRIOR_BOSS
    m_AttPerform = 0
    m_PerformList = (39161, 39191, 39192, 39193, 39194, 39195, 39196, 39197, 39201, 39202, 39204)
    m_Betree = 'BossLuWu.bossLuWuFsm'
    m_BetreeMap = {
        'Default': {
            0: 'BossLuWu.bossLuWuFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4036,
        2: 4037,
        3: 4038 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 39011 },
        (1, 0): {
            'PFAI': 39012 },
        (0, 2): {
            'PFAI': 39011 },
        (0, 1): {
            'PFAI': 39011 } }
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

