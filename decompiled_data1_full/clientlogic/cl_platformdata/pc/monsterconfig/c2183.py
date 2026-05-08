# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterconfig/c2183.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterconfig/c2183.pyc
# Source Generated with Decompyle++
# File: c2183.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, MISSING_DIS_HARD, MISSING_DIS_NORMAL, WARRIOR_NORHEVNEAR
from . import monsterconfigdata

class CMonsterData(monsterconfigdata.CMonsterData):
    m_DataSID = 2183
    m_Shape = 2183
    m_FightType = WARRIOR_NORHEVNEAR
    m_AttPerform = 21833
    m_PerformList = (21832, 21831)
    m_Betree = 'MonsterHugeNear.HugeNearMoveFsm'
    m_BetreeMap = {
        'Default': {
            0: 'MonsterHugeNear.HugeNearMoveFsm' },
        'Common': { } }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = (6202, 6203)
    m_DefendTrend = DEFEND_TREND_ARMOR
    m_AIConfig = {
        (1, 3): {
            'PFAI': 21831 },
        (1, 2): {
            'PFAI': 21831 },
        (0, 3): {
            'PFAI': 21831 },
        (1, 1): {
            'PFAI': 21831 },
        (0, 2): {
            'PFAI': 21831 },
        (0, 1): {
            'PFAI': 21831 } }
    m_CombatForce = 1.5
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 1
    m_MissingDisType = {
        1: MISSING_DIS_NORMAL,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = (6252, 6253)
    m_SurvivorBanPF = ()
    m_AttackCost = 3
    m_ExtraAIArgs = {
        'FightMinDis': 4,
        'FightMaxDis': 10,
        'WaitPatrolRadius': 4 }

