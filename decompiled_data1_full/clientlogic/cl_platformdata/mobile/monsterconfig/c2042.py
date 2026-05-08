# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterconfig/c2042.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterconfig/c2042.pyc
# Source Generated with Decompyle++
# File: c2042.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, WARRIOR_NORBATTERY
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2042
    m_Shape = 2041
    m_FightType = WARRIOR_NORBATTERY
    m_AttPerform = 20411
    m_PerformList = (4082,)
    m_Betree = 'MonsterCannon.CannonFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterCannon.CannonFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6203, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (0, 3): {
            'PFAI': 20421 },
        (1, 0): {
            'PFAI': 20421 },
        (0, 2): {
            'PFAI': 20421 },
        (0, 1): {
            'PFAI': 20421 } }
    m_CombatForce = 1.25
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

