# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2142.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2142.pyc
# Source Generated with Decompyle++
# File: c2142.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORMEDFAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2142
    m_Shape = 2142
    m_FightType = WARRIOR_NORMEDFAR
    m_AttPerform = 21422
    m_PerformList = (21421, 38018, 21423, 21424, 4070, 38028, 38029)
    m_Betree = 'MonsterMediumFar.InvisibleFarFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterMediumFar.InvisibleFarFsm' },
        'Common': {
            2: 'MonsterMediumFar.InvisibleFarAreamoveFsm',
            64: 'Common.GlobalAreaMoveFsm',
            128: 'Common.GlobalAreaMoveFsm' } }
    m_DefaultPhase = 1
    m_PhasePF = {
        1: 4060,
        2: 4061 }
    m_PhaseHitPartToType = {
        1: { },
        2: { },
        3: { } }
    m_AttrPlusPF = (6202, 6204)
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21423 },
        (1, 2): {
            'PFAI': 21422 },
        (0, 3): {
            'PFAI': 21423 },
        (1, 1): {
            'PFAI': 21421 },
        (0, 2): {
            'PFAI': 21422 },
        (0, 1): {
            'PFAI': 21421 } }
    m_CombatForce = 1.25
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0.8
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6254)
    m_SurvivorBanPF = ()
    m_AttackCost = 2
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 15,
        'WaitPatrolRadius': 4 }

