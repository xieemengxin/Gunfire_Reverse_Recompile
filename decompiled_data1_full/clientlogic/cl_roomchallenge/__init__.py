# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_roomchallenge/__init__.pyc
# RelativePath: clientlogic/cl_roomchallenge/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_cscommondef.cs_other import CHALLENGE_ELITE, CHALLENGE_NOTIFY, CHALLENGE_BOXMONSTER, CHALLENGE_SIGHT, CHALLENGE_TRAP, CHALLENGE_LIMITLIVE, CHALLENGE_NOTIFYLIMITTIME, CHALLENGE_DEFEND, CHALLENGE_LIMITDEFEND, CHALLENGE_LIMITTIME, CHALLENGE_LIMITCONVOY, CHALLENGE_ABERRANCE, CHALLENGE_PLAYERPERFORM, CHALLENGE_APPENDSKILL, CHALLENGE_EXTRAMONSTER, CHALLENGE_KILLSUMMON, CHALLENGE_SUPERMONSTER, CHALLENGE_EXTRAELITE, CHALLENGE_ELITEINTRUDE, CHALLENGE_KILLSUMMON_TRAP, CHALLENGE_MORALE_ELITEINTRUDE, CHALLENGE_OBSTACLEALIENATION, CHALLENGE_BOXFLASH, CHALLENGE_SEASONELITEINTRUDE, CHALLENGE_DICESEASON_APPENDSKILL, CHALLENGE_COUNT_MUTANTMONSTER
from . import mobject
from . import roomchallenge
g_ChallengeClass = {
    CHALLENGE_COUNT_MUTANTMONSTER: mobject.CCountMutantMonster,
    CHALLENGE_DICESEASON_APPENDSKILL: mobject.CDiceSeasonAppendSkillChallenge,
    CHALLENGE_SEASONELITEINTRUDE: mobject.CSeasonEliteIntrudeChallenge,
    CHALLENGE_BOXFLASH: mobject.CBoxFlashChallenge,
    CHALLENGE_OBSTACLEALIENATION: mobject.CObstacleAlienationChallenge,
    CHALLENGE_MORALE_ELITEINTRUDE: mobject.CMoraleEliteIntrudeChallenge,
    CHALLENGE_KILLSUMMON_TRAP: mobject.CKillSummonTrapChallenge,
    CHALLENGE_ELITEINTRUDE: mobject.CEliteIntrudeChallenge,
    CHALLENGE_EXTRAELITE: mobject.CExtraEliteChallenge,
    CHALLENGE_SIGHT: mobject.CSightChallenge,
    CHALLENGE_SUPERMONSTER: mobject.CSuperMonsterChallenge,
    CHALLENGE_NOTIFY: mobject.CNotifyChallenge,
    CHALLENGE_TRAP: mobject.CTrapChallenge,
    CHALLENGE_BOXMONSTER: mobject.CBoxMonsterChallenge,
    CHALLENGE_ELITE: mobject.CEliteChallenge,
    CHALLENGE_NOTIFYLIMITTIME: mobject.CNotifyLimitChallenge,
    CHALLENGE_LIMITLIVE: mobject.CLimitLiveChallenge,
    CHALLENGE_LIMITDEFEND: mobject.CLimitDefendChallenge,
    CHALLENGE_DEFEND: mobject.CDefendChallenge,
    CHALLENGE_LIMITCONVOY: mobject.CLimitConvoyChallenge,
    CHALLENGE_LIMITTIME: mobject.CTimeChallenge,
    CHALLENGE_ABERRANCE: mobject.CAberranceChallenge,
    CHALLENGE_PLAYERPERFORM: mobject.CPlayerPerformChallenge,
    CHALLENGE_APPENDSKILL: mobject.CAppendSkillChallenge,
    CHALLENGE_EXTRAMONSTER: mobject.CExtraMonsterChallenge,
    CHALLENGE_KILLSUMMON: mobject.CKillSummonChallenge }

def NewChallenge(oGame, clsData, dAddData):
    iLevel = dAddData['LevelID']
    iRoomPos = dAddData['RoomPos']
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oChallengeMgr = oLevelCtrl.m_RoomChallenge
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    iChallengeType = clsData.m_Type
    if oLevelNode and iChallengeType in g_ChallengeClass:
        clsChallenge = g_ChallengeClass[iChallengeType]
        if not clsChallenge.ValidCreate(oGame, iLevel, iRoomPos, dAddData, clsData):
            return None
        oChallenge = clsChallenge(oChallengeMgr, oLevelNode, iRoomPos)
        oChallenge.Init(clsData, dAddData)
        return oChallenge


def NewRoomChallenge(oLevelCtrl):
    return roomchallenge.CRoomChallengeMgr(oLevelCtrl)

