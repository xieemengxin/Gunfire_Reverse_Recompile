# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2361.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2361.pyc
# Source Generated with Decompyle++
# File: c2361.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORCANNONFODDER
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2361
    m_Shape = 2361
    m_FightType = WARRIOR_NORCANNONFODDER
    m_AttPerform = 23611
    m_PerformList = (38039, 38040, 23612)
    m_Betree = 'MonsterNear.AshFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterNear.AshFsm' },
        'Common': {
            1: 'MonsterNear.AshFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6201, 6203)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 23611 },
        (1, 2): {
            'PFAI': 23611 },
        (0, 3): {
            'PFAI': 23611 },
        (1, 1): {
            'PFAI': 23611 },
        (0, 2): {
            'PFAI': 23611 },
        (0, 1): {
            'PFAI': 23611 } }
    m_CombatForce = 0.5
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
    m_BanPF = (6104, 6105, 6108, 6111, 6112, 6113)
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_AttackCost = 1
    m_ExtraAIArgs = { }

