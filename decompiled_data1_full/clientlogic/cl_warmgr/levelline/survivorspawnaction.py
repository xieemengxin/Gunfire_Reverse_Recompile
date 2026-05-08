# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/survivorspawnaction.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/survivorspawnaction.pyc
# Source Generated with Decompyle++
# File: survivorspawnaction.pyc (Python 3.6)

from cl_commondefines import SURVIVOR_SPAWN_CREATEAREAMONSTER, SURVIVOR_SPAWN_ADDPHASE, SURVIVOR_SPAWN_REWARDRARECUP, MG_SOURCE_ELITEPHASEREWARD, SURVIVOR_SPAWN_CHALLENGE, SURVIVOR_SPAWN_HEROPOSMONSTER, SURVIVOR_SPAWN_STARTELITEPHASENOTIFY, SURVIVOR_SPAWN_STOPELITEPHASENOTIFY
from cl_commondefines import SURVIVOR_SPAWN_SETWARMONSTERMAXNUM
from cl_object.logging import SurvivorLog
import cl_reward

def SpawnCreateAreaMonster(oLineNode, tParam, *args):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    oMonsterCtrl.StartSpawn(tParam)


def SpawnAddPhase(oLineNode, tParam, *args):
    oGame = oLineNode.m_Game
    oNewSurvivorElement = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
    oNewSurvivorElement.PreAddPhase()


def SpawnRewardRareCup(oLineNode, tParam, *args):
    oTarget = args[0]
    oGame = oLineNode.m_Game
    oSurvivor = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
    SurvivorLog.Debug('game:%d elitechallengereward:%d' % (oGame.m_ID, oSurvivor.m_Phase))
    dRareInfo = oSurvivor.m_RareTalentInfo
    dReward = {
        dRareInfo['DropMiniGm']: (dRareInfo['DropProb'], dRareInfo['DropTimes']) }
    lstRoomHero = oGame.m_WarMgr.GetRoomHero()
    if not lstRoomHero:
        return None
    iRewarder = lstRoomHero[oGame.Random(len(lstRoomHero))]
    dExtInfo = {
        'CalOffset': 0,
        'CheckGoldenCup': 1,
        'Abandoner': oTarget.m_ID,
        'CanReward': 1,
        'AutoReward': 1 }
    cl_reward.RewardItemByMiniGame(oTarget, iRewarder, dReward, 'EliteChallengeReward%d' % iRewarder, MG_SOURCE_ELITEPHASEREWARD, dExtInfo)


def SpawnChallenge(oLineNode, tParam, *args):
    iChallenge = tParam[0]
    oGame = oLineNode.m_Game
    oSurvivor = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
    oSurvivor.m_PhaseChallengeMgr.AddChallenge(oSurvivor.m_Phase, iChallenge)


def SpawnHeroPosMonster(oLineNode, tParam, *args):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    oMonsterCtrl.SpawnHeroPosMonster(tParam)


def SpawnStartElitePhaseNotify(oLineNode, tParam, *args):
    (iChat, iDelay, iGroup) = tParam
    oGame = oLineNode.m_Game
    oSurvivor = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
    oSurvivor.StartElitePhaseNotify(iChat, iDelay, iGroup)


def SpawnStopElitePhaseNotify(oLineNode, tParam, *args):
    oGame = oLineNode.m_Game
    oSurvivor = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
    oSurvivor.StopElitePhaseNotify()


def SpawnSetWarMonsterMaxNum(oLineNode, tParam, *args):
    iLimitNum = tParam[0]
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    oMonsterCtrl.SetMonsterLimitNum(iLimitNum)
    oMonsterCtrl.EnableMonsterLimit()

g_SpawnFunc = {
    SURVIVOR_SPAWN_SETWARMONSTERMAXNUM: SpawnSetWarMonsterMaxNum,
    SURVIVOR_SPAWN_STOPELITEPHASENOTIFY: SpawnStopElitePhaseNotify,
    SURVIVOR_SPAWN_STARTELITEPHASENOTIFY: SpawnStartElitePhaseNotify,
    SURVIVOR_SPAWN_HEROPOSMONSTER: SpawnHeroPosMonster,
    SURVIVOR_SPAWN_CHALLENGE: SpawnChallenge,
    SURVIVOR_SPAWN_REWARDRARECUP: SpawnRewardRareCup,
    SURVIVOR_SPAWN_ADDPHASE: SpawnAddPhase,
    SURVIVOR_SPAWN_CREATEAREAMONSTER: SpawnCreateAreaMonster }

def GetSpawnFunc(idx):
    if idx in g_SpawnFunc:
        return g_SpawnFunc[idx]

