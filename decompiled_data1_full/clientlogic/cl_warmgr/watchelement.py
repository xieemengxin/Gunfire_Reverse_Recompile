# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/watchelement.pyc
# RelativePath: clientlogic/cl_warmgr/watchelement.pyc
# Source Generated with Decompyle++
# File: watchelement.pyc (Python 3.6)

from cl_commondefines import WARRIOR_HERO, TYPE_RELIFE_GSCASH, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE
from cl_warmgr.mobject import CBaseElement
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_snetwar
import cl_formula

class CWatchElement(CBaseElement):
    m_CallFlag = 'WarMgr.WatchElement'
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Watch2Focus = { }
        self.m_Focus2Watch = { }
        self.m_WatchPlayer = { }
        dConfig = self.m_Data.m_Config
        self.m_WatchPF = dConfig.get('WatchPF', 0)
        self.m_RelifeNeedGoalRoomNum = dConfig.get('RelifeNeedGoalRoomNum', 0)
        self.m_RelifeCost = dConfig.get('RelifeCost', 100)
        self.m_RelifeInfo = { }
        self.m_RelifeCache = { }

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.IsSingleGame():
            return None
        oGame = self.m_Game
        iWarMgr = oWarMgr.m_ID
        oGame.AddGlobalAttention(iWarMgr, cl_msgcenter.MSG_WAR_DIEDIST, self.PlayerRealDie, 'PlayerRealDie%s' % self.m_CallFlag)
        oGame.AddGlobalAttention(iWarMgr, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.PlayerMapLoadOK, 'PlayerMapLoadOK%s' % self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.PlayerRemove, 'PlayerRemove%s' % self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, 'AddAllPlayer%s' % self.m_CallFlag)
        oWarMgr.Set('PutRealDiedRelife', 1)
        if self.m_RelifeNeedGoalRoomNum:
            oGame.AddGlobalAttention(iWarMgr, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, 'RoomGoal%s' % self.m_CallFlag)

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        if not oWarMgr.IsSingleGame():
            oGame = self.m_Game
            iWarMgr = oWarMgr.m_ID
            oGame.DoneGlobalAttention(iWarMgr, cl_msgcenter.MSG_WAR_DIEDIST, 'PlayerRealDie%s' % self.m_CallFlag)
            oGame.DoneGlobalAttention(iWarMgr, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'PlayerMapLoadOK%s' % self.m_CallFlag)
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'PlayerRemove%s' % self.m_CallFlag)
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'AddAllPlayer%s' % self.m_CallFlag)
            if self.m_RelifeNeedGoalRoomNum:
                oGame.DoneGlobalAttention(iWarMgr, cl_msgcenter.MSG_LEVEL_ROOMGOAL, 'RoomGoal%s' % self.m_CallFlag)
        super().Release()

    
    def Save(self):
        dData = { }
        if self.m_WarMgr.Query('PutRealDiedRelife', 0):
            dData['RLI'] = dict(self.m_RelifeInfo)
            dData['RLC'] = dict(self.m_RelifeCache)
        return dData

    
    def Load(self, dData):
        if self.m_WarMgr.Query('PutRealDiedRelife', 0):
            self.m_RelifeInfo = dData.get('RLI', { })
            self.m_RelifeCache = dData.get('RLC', { })

    
    def OnHalfOpen(self):
        self.Init()
        self.OnAddAllPlayer(self.m_WarMgr, { })

    
    def GetWatcherByFocus(self, iFocus):
        if iFocus in self.m_Focus2Watch:
            return self.m_Focus2Watch[iFocus]
        return []

    
    def SwitchWatch(self, iWatch, iTarget):
        if iWatch not in self.m_Watch2Focus or self.m_Watch2Focus[iWatch] == iTarget:
            return None
        oGame = self.m_Game
        oWatch = oGame.GetObject(iWatch)
        if not oWatch.IsRealDied():
            return None
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO or oTarget.IsRealDied():
            return None
        self.SetWatch(oWatch, oTarget)

    
    def SetWatch(self, oWatch, oFocus):
        iWatch = oWatch.m_ID
        iFocus = oFocus.m_ID
        self.RemoveWatch(iWatch)
        self.m_Watch2Focus[iWatch] = iFocus
        self.m_WatchPlayer[oWatch.m_PlayerID] = 1
        lstWatch = self.m_Focus2Watch.setdefault(iFocus, [])
        lstWatch.append(iWatch)
        if oFocus.m_Scene and oFocus.m_Scene != oWatch.m_Scene:
            tPos = oFocus.GetPos()
            tFace = oFocus.GetFacing()
            oWatch.Goto(oFocus.m_Scene, tPos, tFace)
        else:
            dPlayer = self.m_Game.GetRealPlayers()
            cl_snetwar.GS2CEnterWatch(self.m_Game, iWatch, iFocus, dPlayer)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENTERWATCH, oWatch, {
            'pid': oWatch.m_PlayerID,
            'Focus': oFocus.m_PlayerID })
        cl_msgcenter.AddAttentionFunc(oWatch, iFocus, cl_msgcenter.MSG_WAR_ENTERSCENE, self.PlayerEnterScene, 'WatchEnterScene')

    
    def RemoveWatch(self, iWatch):
        if iWatch not in self.m_Watch2Focus:
            return None
        iFocus = self.m_Watch2Focus.pop(iWatch)
        self.m_Focus2Watch[iFocus].remove(iWatch)
        oWatch = self.m_Game.GetObject(iWatch)
        if not oWatch:
            return None
        self.m_WatchPlayer.pop(oWatch.m_PlayerID, 0)
        cl_msgcenter.DoneAttention(oWatch, iFocus, cl_msgcenter.MSG_WAR_ENTERSCENE, 'WatchEnterScene')

    
    def RemoveFocus(self, iHero):
        if iHero not in self.m_Focus2Watch:
            return []
        lstWatch = self.m_Focus2Watch[iHero][:]
        for iWatch in lstWatch:
            self.RemoveWatch(iWatch)
        
        return lstWatch

    
    def PlayerRealDie(self, oWarMgr, oWarrior, dInfo):
        if not oWarrior.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            return None
        iHero = oWarrior.m_ID
        lstWatch = self.RemoveFocus(iHero)
        oFocus = self.GetDefaultFocus(oWarrior)
        if not oFocus:
            return None
        self.EnableWatchPerform(oWarrior)
        oGame = self.m_Game
        for iWatch in lstWatch:
            oHero = oGame.GetObject(iWatch)
            if not oHero:
                continue
            self.SetWatch(oHero, oFocus)
        
        self.SetWatch(oWarrior, oFocus)

    
    def PlayerMapLoadOK(self, oWarMgr, oWarrior, dInfo):
        iWatch = oWarrior.m_ID
        if iWatch not in self.m_Watch2Focus:
            return None
        iFocus = self.m_Watch2Focus[iWatch]
        dPlayer = self.m_Game.GetRealPlayers()
        cl_snetwar.GS2CEnterWatch(self.m_Game, iWatch, iFocus, dPlayer)
        self.GS2CRealDiedRelifeConfirm(oWarrior.m_PlayerID)

    
    def PlayerEnterScene(self, oWatch, oFocus, dInfo):
        if oFocus.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if oFocus.m_Scene != oWatch.m_Scene:
            tPos = oFocus.GetPos()
            tFace = oFocus.GetFacing()
            oWatch.Goto(oFocus.m_Scene, tPos, tFace)

    
    def OnAddAllPlayer(self, _oWarMgr, _dInfo):
        oGame = self.m_Game
        lstHero = self.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero or not oHero.IsRealDied():
                continue
            oFocus = self.GetDefaultFocus(oHero)
            if not oFocus:
                continue
            self.SetWatch(oHero, oFocus)
        

    
    def PlayerRemove(self, _oWarMgr, dInfo):
        iHero = dInfo['Hero']
        self.RemoveWatch(iHero)
        lstWatch = self.RemoveFocus(iHero)
        oGame = self.m_Game
        for iWatch in lstWatch:
            oWatch = oGame.GetObject(iWatch)
            if not oWatch:
                continue
            oFocus = self.GetDefaultFocus(oWatch, iHero)
            if not oFocus:
                return None
            self.SetWatch(oWatch, oFocus)
        

    
    def GetDefaultFocus(self, oHero, iExcept = 0):
        oGame = self.m_Game
        iWatch = oHero.m_ID
        lstLiveHero = self.m_WarMgr.GetLiveHero()
        if iWatch in lstLiveHero:
            lstLiveHero.remove(iWatch)
        if iExcept in lstLiveHero:
            lstLiveHero.remove(iExcept)
        if not lstLiveHero:
            return None
        oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
        lstSceneHero = oScene.GetHeros() if oScene else []
        for iHero in lstSceneHero:
            if iHero not in lstLiveHero:
                continue
            oSameSceneFocus = oGame.GetObject(iHero)
            if oSameSceneFocus:
                return oSameSceneFocus
        
        for iLive in lstLiveHero:
            oFocus = oGame.GetObject(iLive)
            if oFocus:
                return oFocus
        

    
    def EnableWatchPerform(self, oWatch):
        WarobjLog.Debug('%d addwatchpf %d' % (self.m_Game.m_ID, oWatch.m_PlayerID))
        oWatch.m_Perform.AddPerform(oWatch, self.m_WatchPF, 1, iEnable = 1, iItem = 0)
        self.AddRelifeInfo(oWatch.m_PlayerID, 'RealDiedCnt', 1)
        iRealDiedCnt = self.GetRelifeInfo(oWatch.m_PlayerID, 'RealDiedCnt')
        iCost = cl_formula.GetFormulaResult(oWatch, self.m_RelifeCost, {
            'RealDiedCnt': iRealDiedCnt })
        self.SetRelifeInfo(oWatch.m_PlayerID, 'RelifeCost', iCost)

    
    def RelifeWatch(self, oWatch):
        WarobjLog.Debug('%d relifewatch %d' % (self.m_Game.m_ID, oWatch.m_PlayerID))
        oWatch.m_Perform.RemovePerform(oWatch, self.m_WatchPF)
        self.RemoveWatch(oWatch.m_ID)
        self.SetRelifeInfo(oWatch.m_PlayerID, 'GoalRoomNum', 0)
        if oWatch.m_PlayerID in self.m_RelifeCache:
            self.m_RelifeCache.pop(oWatch.m_PlayerID)

    
    def GetFocus(self, iWatch):
        if iWatch not in self.m_Watch2Focus:
            return None
        iFocus = self.m_Watch2Focus[iWatch]
        oFocus = self.m_Game.GetObject(iFocus)
        if not oFocus:
            return None
        return oFocus

    
    def OnRoomGoal(self, _oWarMgr, oLevelCtrl, dInfo):
        iType = oLevelCtrl.GetLevelType(dInfo['Level'])
        if iType not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE):
            return None
        for iWatchPlayer in self.m_WatchPlayer:
            if iWatchPlayer in self.m_RelifeCache:
                continue
            iGoalRoomNum = self.AddRelifeInfo(iWatchPlayer, 'GoalRoomNum', 1)
            if iGoalRoomNum >= self.m_RelifeNeedGoalRoomNum:
                self.m_RelifeCache[iWatchPlayer] = self.GetRelifeInfo(iWatchPlayer, 'RelifeCost')
                self.GS2CRealDiedRelifeConfirm(iWatchPlayer)
        

    
    def AddRelifeInfo(self, iPlayer, sKey, iVal):
        dRelifeInfo = self.m_RelifeInfo.setdefault(iPlayer, { })
        if sKey in dRelifeInfo:
            dRelifeInfo[sKey] += iVal
        else:
            dRelifeInfo[sKey] = iVal
        return dRelifeInfo[sKey]

    
    def SetRelifeInfo(self, iPlayer, sKey, iVal):
        if iPlayer in self.m_RelifeInfo:
            self.m_RelifeInfo[iPlayer][sKey] = iVal
        else:
            self.m_RelifeInfo[iPlayer] = {
                sKey: iVal }

    
    def GetRelifeInfo(self, iPlayer, sKey):
        if iPlayer not in self.m_RelifeInfo:
            return 0
        if sKey not in self.m_RelifeInfo[iPlayer]:
            return 0
        return self.m_RelifeInfo[iPlayer][sKey]

    
    def GS2CRealDiedRelifeConfirm(self, iPlayerID):
        if iPlayerID not in self.m_RelifeCache:
            return None
        cl_snetwar.GS2CRealDiedRelifeConfirm(iPlayerID, self.m_Game, self.m_RelifeCache[iPlayerID])

    
    def RealDiedRelife(self, oHero):
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in self.m_RelifeCache:
            return None
        iCost = self.m_RelifeCache[iPlayerID]
        if oHero.m_WarGSCash < iCost:
            return None
        oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
        if not oDieElement:
            return None
        WarobjLog.Info('%d %d realdiedrelife %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iCost))
        self.m_RelifeCache.pop(iPlayerID)
        oHero.ConsumeGSCash(iCost, 'realdiedrelife')
        oFocus = self.GetFocus(oHero.m_ID)
        self.RelifeWatch(oHero)
        oDieElement.WatcherRelife(oHero, TYPE_RELIFE_GSCASH, oHero.m_ID)
        if oFocus:
            self.SyncAssignBornPos(oHero.m_ID, oFocus.m_ID, oFocus.m_Scene)
            if oHero.m_Scene == oFocus.m_Scene:
                oHero.WalkTo(oFocus.GetPos())
                oHero.Stop()
            else:
                oHero.Goto(oFocus.m_Scene, oFocus.GetPos(), oFocus.GetFacing())

    
    def SyncAssignBornPos(self, iHero, iFocus, iScene):
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        iLevel = oLevelCtrl.GetConfigLevel(oScene.m_Level)
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType != LEVEL_TYPE_HIDE:
            return None
        dAssignBornPos = oLevelNode.m_CtrlMgr.m_LevelAssignBornPos
        iCurMainLevel = oLevelCtrl.m_CurNode.m_Level
        if iFocus not in dAssignBornPos or iCurMainLevel not in dAssignBornPos[iFocus]:
            return None
        if iHero not in dAssignBornPos:
            dAssignBornPos[iHero] = { }
        if iCurMainLevel not in dAssignBornPos[iHero]:
            dAssignBornPos[iHero][iCurMainLevel] = dAssignBornPos[iFocus][iCurMainLevel]



def GetComponentClass(oMgrManager):
    return CWatchElement

