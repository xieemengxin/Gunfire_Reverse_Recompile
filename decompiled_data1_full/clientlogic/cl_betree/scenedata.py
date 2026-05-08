# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/scenedata.pyc
# RelativePath: clientlogic/cl_betree/scenedata.pyc
# Source Generated with Decompyle++
# File: scenedata.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, Functor
from cl_commondefines import WARRIOR_MONSTER
import cl_world
import cl_msgcenter

class CAISceneDataBeTree(cl_world.CEventObject):
    
    def __init__(self, oGame, nid, iScene):
        super(CAISceneDataBeTree, self).__init__(oGame, nid)
        self.m_MsgInfo = { }
        self.m_Scene = iScene
        self.m_Data = { }
        self.m_Sight = { }
        self.m_FigntLogic = { }
        self.m_SyncAttack = { }
        self.m_DisCache = { }
        self.m_FightMonster = { }
        self.m_MonsterNum = { }
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, 'MonsterDie')
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, OnMonsterStartHate, 'MonsterStartHate')
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, OnMonsterEndHate, 'MonsterEndHate')
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_UPDATE_HATE, OnMonsterUpdateHate, 'MonsterUpdateHate')
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, OnMonsterLeaveScene, 'MonsterLeaveScene')

    
    def Release(self):
        self.DoneAllAtention()
        super(CAISceneDataBeTree, self).Release()

    
    def Set(self, key, value):
        self.m_Data[key] = value

    
    def Query(self, key, default = 0):
        if key in self.m_Data:
            default = self.m_Data[key]
        return default

    
    def SetDefault(self, key, value):
        if key not in self.m_Data:
            self.m_Data[key] = value
            return value
        return self.m_Data[key]

    
    def Delete(self, key):
        if key in self.m_Data:
            del self.m_Data[key]

    
    def AddAttention(self, iMsg, iSub, iTarget, sKey, cbfunc):
        tMsgKey = (iMsg, iSub)
        if tMsgKey not in self.m_MsgInfo:
            self.m_MsgInfo[tMsgKey] = { }
            self.m_Game.AddGlobalAttention(self.m_ID, iMsg, Functor(self.OnSendMsg, tMsgKey), 'aiscenedata', iSub)
        dTarget = self.m_MsgInfo[tMsgKey].setdefault(iTarget, { })
        dTarget[sKey] = cbfunc

    
    def DoneAtention(self, iTarget, iMsg, iSub, sDoneKey):
        tMsgKey = (iMsg, iSub)
        if tMsgKey in self.m_MsgInfo and iTarget in self.m_MsgInfo[tMsgKey]:
            self.m_MsgInfo[(iMsg, iSub)][iTarget].pop(sDoneKey, None)
            if not self.m_MsgInfo[(iMsg, iSub)][iTarget]:
                self.m_MsgInfo[(iMsg, iSub)].pop(iTarget)

    
    def DoneAllAtention(self):
        oGame = self.m_Game
        for iMsg, iSub in self.m_MsgInfo:
            oGame.DoneGlobalAttention(self.m_ID, iMsg, 'aiscenedata', iSub)
        
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, 'MonsterDie')
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, 'MonsterStartHate')
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, 'MonsterEndHate')
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_UPDATE_HATE, 'MonsterUpdateHate')
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, 'MonsterLeaveScene')
        self.m_MsgInfo = { }

    
    def OnSendMsg(self, tMsgKey, oAISceneData, oTarget, dMsgInfo):
        if oTarget.m_Scene != self.m_Scene:
            return None
        dInfo = self.m_MsgInfo[tMsgKey]
        oGame = self.m_Game
        for iListener, dAttention in dInfo.items():
            oListener = oGame.GetObject(iListener)
            if not oListener or oListener.m_Scene != self.m_Scene:
                continue
            for cbfunc in dAttention.values():
                cbfunc(oListener, dMsgInfo)
            
        

    
    def GetDisCache(self, iCurFrame, iTarget):
        if iCurFrame in self.m_DisCache:
            if iTarget in self.m_DisCache[iCurFrame]:
                return self.m_DisCache[iCurFrame][iTarget]
            return { }
        return { }

    
    def SetDisCache(self, iCurFrame, iTarget, dDis):
        if iCurFrame not in self.m_DisCache:
            self.m_DisCache = {
                iCurFrame: { } }
        self.m_DisCache[iCurFrame][iTarget] = dDis

    
    def SetSightData(self, iMonster, iHero, bInSight):
        dHeroSight = self.m_Sight.setdefault(iHero, { })
        iNowFrame = self.m_Game.GetFrameNum()
        dHeroSight[iMonster] = (iNowFrame, bInSight)

    
    def CheckSightNum(self, iHero, iSightCnt, iFrame):
        dHeroSight = self.m_Sight.setdefault(iHero, { })
        oGame = self.m_Game
        iLastFrame = oGame.GetFrameNum() - iFrame
        iSee = 0
        for iSeeFrame, bInSight in dHeroSight.values():
            if iSeeFrame > iLastFrame and bInSight:
                iSee += 1
        
        if iSee >= iSightCnt:
            return iSee
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        lstAllMonster = oScene.GetObjectsByType('Monster')
        oHero = oGame.GetObject(iHero)
        for iMonster in set(lstAllMonster) - set(dHeroSight):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or not (oMonster.m_Agent):
                continue
            if oMonster.m_Agent.IsHeroInSight(oMonster, oHero, 180):
                iSee += 1
        
        return iSee

    
    def GetMonsterFightLogicNum(self, iType, iCheckID):
        if iType not in self.m_FigntLogic:
            return 0
        iNum = len(self.m_FigntLogic[iType])
        if iCheckID in self.m_FigntLogic[iType]:
            iNum -= 1
        return iNum

    
    def GetCombatForceByFightLogic(self, iType):
        if iType not in self.m_FigntLogic:
            return 0
        return sum(self.m_FigntLogic[iType].values())

    
    def SetFightLogicType(self, oAgent, iNewType):
        oOwner = oAgent.m_OwnerObj
        iMonster = oOwner.m_ID
        iType = oAgent.GetData('FightLogic', -1)
        if iType in self.m_FigntLogic:
            self.m_FigntLogic[iType].pop(iMonster, None)
        if iNewType not in self.m_FigntLogic:
            self.m_FigntLogic[iNewType] = { }
        dNewInfo = self.m_FigntLogic[iNewType]
        dNewInfo[iMonster] = oOwner.m_CombatForce

    
    def RegisterSyncAttack(self, oAgent, iPerform, iFrame):
        key = iPerform
        iStart = 0
        if key not in self.m_SyncAttack:
            iStart = 1
            self.m_SyncAttack[key] = { }
        self.m_SyncAttack[key][oAgent.m_OwnerObj.m_SID] = 1
        if iStart:
            self.SyncAttack(iPerform, iFrame)

    
    def SyncAttack(self, iPerform, iFrame):
        oGame = self.m_Game
        sKey = 'syncpf%d' % iPerform
        self.Remove_Call_Out(sKey)
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        lstMonster = oScene.GetObjectsByType('Monster') if oScene else []
        iCnt = 0
        for iID in lstMonster:
            oMonster = oGame.GetObject(iID, PY_FLAG_DEAD)
            if not oMonster or oMonster.m_SID not in self.m_SyncAttack[iPerform]:
                continue
            iCnt += 1
            oMonsterAgent = oMonster.m_Agent
            if not oMonsterAgent or not (oMonsterAgent.m_bActive):
                continue
            oMonsterAgent.SyncAttack(iPerform)
        
        if iCnt:
            self.Call_Out(Functor(self.SyncAttack, iPerform, iFrame), iFrame, sKey)
        else:
            self.m_SyncAttack.pop(iPerform)

    
    def AddFightMonster(self, iTarget):
        self.m_FightMonster[iTarget] = 0

    
    def RemoveFightMonster(self, iTarget):
        self.m_FightMonster.pop(iTarget, 0)

    
    def GetFightMonster(self):
        return self.m_FightMonster



def OnMonsterDie(oAISceneData, oTarget, dMsgInfo):
    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER or not (oTarget.m_Agent):
        return None
    iType = oTarget.m_Agent.GetData('FightLogic', -1)
    if iType in oAISceneData.m_FigntLogic:
        oAISceneData.m_FigntLogic[iType].pop(oTarget.m_ID, None)
    if oTarget.m_ID in oAISceneData.m_FightMonster:
        iLockEnemy = oAISceneData.m_FightMonster[oTarget.m_ID]
        if iLockEnemy in oAISceneData.m_MonsterNum and oAISceneData.m_MonsterNum[iLockEnemy] > 0:
            oAISceneData.m_MonsterNum[iLockEnemy] -= 1
        oAISceneData.m_FightMonster.pop(oTarget.m_ID)


def OnMonsterStartHate(oAISceneData, oTarget, dMsgInfo):
    if not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_Scene != oAISceneData.m_Scene:
        return None
    iLockEnemy = dMsgInfo['LockEnemy']
    AddMonsterNum(oAISceneData, iLockEnemy, oTarget.m_ID)
    oAISceneData.m_FightMonster[oTarget.m_ID] = iLockEnemy


def OnMonsterEndHate(oAISceneData, oTarget, dMsgInfo):
    if not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_Scene != oAISceneData.m_Scene:
        return None
    if oTarget.m_ID in oAISceneData.m_FightMonster:
        iOldTarget = dMsgInfo['OldTarget']
        if iOldTarget in oAISceneData.m_MonsterNum and oAISceneData.m_MonsterNum[iOldTarget] > 0:
            oAISceneData.m_MonsterNum[iOldTarget] -= 1
        oAISceneData.m_FightMonster.pop(oTarget.m_ID)


def OnMonsterUpdateHate(oAISceneData, oTarget, dMsgInfo):
    if not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_Scene != oAISceneData.m_Scene:
        return None
    iLockEnemy = dMsgInfo['LockEnemy']
    iOldTarget = dMsgInfo['OldTarget']
    if iOldTarget in oAISceneData.m_MonsterNum and oAISceneData.m_MonsterNum[iOldTarget] > 0:
        oAISceneData.m_MonsterNum[iOldTarget] -= 1
    AddMonsterNum(oAISceneData, iLockEnemy, oTarget.m_ID)
    oAISceneData.m_FightMonster[oTarget.m_ID] = iLockEnemy


def OnMonsterLeaveScene(oAISceneData, oTarget, dMsgInfo):
    if not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_Scene != oAISceneData.m_Scene:
        return None
    if oTarget.m_ID in oAISceneData.m_FightMonster:
        iLockEnemy = oAISceneData.m_FightMonster[oTarget.m_ID]
        if iLockEnemy in oAISceneData.m_MonsterNum and oAISceneData.m_MonsterNum[iLockEnemy] > 0:
            oAISceneData.m_MonsterNum[iLockEnemy] -= 1
        oAISceneData.m_FightMonster.pop(oTarget.m_ID)


def AddMonsterNum(oAISceneData, iLockEnemy, iMonster):
    if iLockEnemy in oAISceneData.m_MonsterNum:
        oAISceneData.m_MonsterNum[iLockEnemy] += 1
    else:
        oAISceneData.m_MonsterNum[iLockEnemy] = 1

