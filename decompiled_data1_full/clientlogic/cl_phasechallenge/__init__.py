# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_phasechallenge/__init__.pyc
# RelativePath: clientlogic/cl_phasechallenge/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import PHASE_CHALLENGE_SINGLEPOINTOCCUPY, PHASE_CHALLENGE_BOXMONSTER, PHASE_CHALLENGE_KILLBOXMONSTER, PHASE_CHALLENGE_SEARCHTREASURE, PHASE_CHALLENGE_GOLDENELITE, PLAYMODE_NEWSURVIVOR
from cl_only import SendAlert
from . import mobject
g_PhaseChallengeClass = {
    PHASE_CHALLENGE_SINGLEPOINTOCCUPY: (None, mobject.CSinglePointOccupyChallenge),
    PHASE_CHALLENGE_GOLDENELITE: (mobject.CGoldenEliteChallenge, None),
    PHASE_CHALLENGE_SEARCHTREASURE: (mobject.CSearchTreasureChallenge, None),
    PHASE_CHALLENGE_KILLBOXMONSTER: (mobject.CKillBoxMonsterChallenge, mobject.CNewKillBoxMonsterChallenge),
    PHASE_CHALLENGE_BOXMONSTER: (mobject.CBoxMonsterChallenge, mobject.CNewBoxMonsterChallenge) }

def NewPhaseChallenge(oGame, clsData, dAddData):
    oSurvivorElelement = oGame.m_WarMgr.GetSurvivorElement()
    if not oSurvivorElelement:
        return None
    iPhase = dAddData['Phase']
    oChallengeMgr = oSurvivorElelement.m_PhaseChallengeMgr
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    iChallengeType = clsData.m_Type
    if oLevelNode and iChallengeType in g_PhaseChallengeClass:
        (clsOld, clsNew) = g_PhaseChallengeClass[iChallengeType]
        clsChallenge = clsNew if oGame.m_WarMgr.m_PlayMode == PLAYMODE_NEWSURVIVOR else clsOld
        if not clsChallenge:
            SendAlert('err', '战场%d 无对应阶段挑战 %s' % (oGame.GetWarMgr().m_SID, iChallengeType))
            return None
        oChallenge = clsChallenge(oChallengeMgr, oLevelNode, iPhase)
        oChallenge.Init(clsData, dAddData)
        return oChallenge


def NewPhaseChallengeMgr(oSurvivorElement, iNew = 0):
    oGame = oSurvivorElement.m_Game
    iID = oGame.NewNPCID()
    if iNew:
        oPhaseChallengeMgr = mobject.CNewPhaseChallengeMgr(oSurvivorElement, iID)
    else:
        oPhaseChallengeMgr = mobject.CPhaseChallengeMgr(oSurvivorElement, iID)
    oGame.CreateObject(iID, oPhaseChallengeMgr)
    return oPhaseChallengeMgr

