# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/baselevelnode.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/baselevelnode.pyc
# Source Generated with Decompyle++
# File: baselevelnode.pyc (Python 3.6)

from cl_cscommondef import CLEVEL_FIRDOOR_OPEN, LEVEL_TYPE_FIGHT, LEVEL_STATUS_WAIT, LEVEL_SPAWN_TRIGGERNPC, LEVEL_TYPE_NONE, GAMETYPE_NONE, LEVEL_STATUS_FINISH, LEVEL_STATUS_GOAL, LEVEL_STATUS_START
from cl_commondefines import STATE_UNDER_ATTACK
from cl_only import ShufferList, ChooseKey, Functor, SendAlert
from cl_object.logging import LevelLog
from cl_commondecorator import CheckFaultTolerance
import cl_msgcenter
import cl_snetwar
import cl_notify
import cl_state
import cl_platformdata
import cllib.lib_flag
from . import levellinenode
from . import levelspawnaction
from . import levelnodeplug

class CBaseLevelNode(object):
    m_LevelType = LEVEL_TYPE_NONE
    m_GameType = GAMETYPE_NONE
    m_TargetName = ''
    
    def __init__(self, oCtrlMgr, iLevel):
        oLevelConfData = oCtrlMgr.m_LevelConfData
        self.m_Status = LEVEL_STATUS_WAIT
        self.m_PassLevel = True
        self.m_CtrlMgr = oCtrlMgr
        self.m_Game = oCtrlMgr.m_Game
        self.m_Level = iLevel
        self.m_LevelNum = self.m_CtrlMgr.m_LevelNum
        self.m_LayerNum = self.m_CtrlMgr.m_LayerNum
        self.m_Difficulty = oLevelConfData.GetLevelConfig(iLevel, 'Difficult', default = 0)
        self.m_SceneConfigPos = {
            'reward': { },
            'shop': { },
            'event': { },
            'bossreward': { } }
        self.m_CurRoomPos = -1
        self.m_LockRoomPos = { }
        self.m_InUseBorn = []
        self.m_NodePlug = levelnodeplug.GetLevelNodePlug(self)
        self.m_PendEnterHero = []
        self.m_NotifyPlayerCntChange = False
        self.m_QuittedPlayerInfo = { }
        self.m_NotifiedPlayer = { }
        self.m_SkipCGPlayer = { }
        self.m_MonsterCategory = []
        self.m_CustomData = { }
        lstLineName = []
        self.m_RoomList = self.CreateLineInfo(lstLineName)
        oLevelConfData = self.m_CtrlMgr.m_LevelConfData
        dResData = oLevelConfData.GetLevelResData(self.m_Level, lstLineName)
        self.m_Map = oLevelConfData.GetLevelConfig(self.m_Level, 'map')
        self.m_Scene = self.m_CtrlMgr.m_Game.GetResMgr().CreateScene(self.m_Map, self.m_Level, dResData)
        self.InitEvent()

    
    def Release(self):
        lstLineIdx = []
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                lstLineIdx.append(oLine.GetLineIdx())
                oLine.Release()
            
        
        if self.m_NodePlug:
            self.m_NodePlug.Release()
            self.m_NodePlug = None
        self.ReleaseEvent()
        self.OnRelease()
        self.m_CtrlMgr.m_LevelTrigger.ClearLevel(self.m_Scene, lstLineIdx)
        self.m_CtrlMgr.m_RoomChallenge.ClearLevel(self.m_Level)
        self.CleanSceneObj()
        self.m_CtrlMgr = None
        self.m_Game = None

    Release = CheckFaultTolerance(Release)
    
    def ReleaseEvent(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_SCENELOAD, 'SceneLoad%s' % self.m_Scene)
        self.m_Game.DoneGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'LevelNode%d' % self.m_Scene)

    
    def OnRelease(self):
        pass

    
    def CleanSceneObj(self):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return None
        lstHero = oScene.GetObjectsByType('Hero')
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero or not (oHero.m_PlayerID):
                continue
            oHero.LeaveScene(0)
        
        oResMgr = oGame.m_ResMgr
        if oResMgr:
            oResMgr.ReleaseScene(self.m_Scene)

    
    def HasGoaledCurNode(self):
        if self.m_Status in (LEVEL_STATUS_FINISH, LEVEL_STATUS_GOAL):
            return 1
        return 0

    
    def GetCurNodeProgress(self):
        if self.m_Status == LEVEL_STATUS_FINISH:
            return 100
        iTotalLine = 0
        iPassLine = 0
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                iTotalLine += 1
                if oLine.IsGoal():
                    iPassLine += 1
            
        
        iTotalLine = max(1, iTotalLine)
        iProgress = min(99, iPassLine * 100 // iTotalLine)
        return iProgress

    
    def GetBornPos(self):
        oBornLine = self.m_RoomList[0][0]
        return oBornLine.GetBornPos()

    
    def GetRelifePos(self):
        oLine = self.m_RoomList[0][0]
        return oLine.GetRelifePos()

    
    def GetMaxRoomCnt(self):
        return len(self.m_RoomList)

    
    def GetLevelMonsterCategory(self):
        if not self.m_MonsterCategory:
            lstAllCategory = []
            for lstRoomList in self.m_RoomList:
                for oLineNode in lstRoomList:
                    lstCategory = oLineNode.m_MonsterCtrl.GetMonsterCategory()
                    lstAllCategory.extend(lstCategory)
                
            
            if self.m_Game.GetWarMgr().Query('PreLoad', 1):
                oRoomChallenge = self.m_CtrlMgr.m_RoomChallenge
                oPreCollect = oRoomChallenge.m_PreCollect
                lstCategory = oPreCollect.QueryMonsterCategory(self.m_Level)
                lstAllCategory.extend(lstCategory)
                oSurvivor = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
                if oSurvivor:
                    lstAllCategory.extend(oSurvivor.m_PhaseChallengeMgr.GetMonsterPreCollect())
                dOtherMonster = cl_platformdata.GetOtherMonster()
                for iDataSID in set(lstAllCategory):
                    lstOther = dOtherMonster.get(iDataSID, [])
                    for iSID in lstOther:
                        clsData = self.m_Game.m_WarData.GetMonsterData(iSID)
                        if not clsData:
                            continue
                        lstAllCategory.append(clsData.m_DataSID)
                    
                
            self.m_MonsterCategory = set(lstAllCategory)
        return self.m_MonsterCategory

    
    def GetRefreshNpcWeight(self, sType):
        oLevelCtrl = self.m_CtrlMgr
        iLayerNum = oLevelCtrl.m_LayerNum
        dLayerData = oLevelCtrl.m_LevelCtrlConf[iLayerNum]
        dNpcInfo = dLayerData['NpcInfo']
        if sType in dNpcInfo:
            return dNpcInfo[sType]
        if sType == 'event':
            oLevelConfData = oLevelCtrl.m_LevelConfData
            lstSpawnRule = oLevelConfData.GetLevelConfig(self.m_Level, 'SpawnRule')
            for dSpawn in lstSpawnRule:
                tAction = dSpawn['Action']
                for dAction in tAction:
                    iFunc = dAction['func']
                    if iFunc == LEVEL_SPAWN_TRIGGERNPC:
                        (sName, dNpcWeight, _dAmount) = dAction['param']
                        if sName == sType:
                            return dNpcWeight
                
            
        else:
            SendAlert('err', '幕数%d未配置%sNPC' % (iLayerNum, sType))
        return { }

    
    def IsSceneLoaded(self):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return False
        return oScene.m_SceneLoad

    
    def LevelInit(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        if iLevel != self.m_Level:
            return None
        dData = {
            'GameType': self.m_GameType,
            'LevelType': self.m_LevelType,
            'LevelID': self.m_Level,
            'Layer': self.m_CtrlMgr.m_LayerNum,
            'Level': self.m_CtrlMgr.m_LevelNum,
            'Scene': self.m_Scene }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_Game.m_WarMgr, dData)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_SCENELOAD, 'SceneLoad%s' % self.m_Scene)
        self.InitSceneConfigPos()
        self.m_NodePlug.OnLevelInit()
        self.InitAllLine()
        self.OnLevelInit()
        if self.m_PendEnterHero:
            lstPendHero = list(set(self.m_PendEnterHero))
            self.HeroEnterLevel(lstPendHero)
            self.TryTriggerLevelStart()
        self.m_PendEnterHero = []
        oLevelCtrl = self.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        oLevelTrigger = oLevelCtrl.m_LevelTrigger
        lstSpawnRule = oLevelConfData.GetLevelConfig(self.m_Level, 'SpawnRule')
        for dSpawn in lstSpawnRule:
            oCondition = dSpawn['Cond']
            tAction = dSpawn['Action']
            cbFunc = Functor(self.DownSpawn, tAction)
            oLevelTrigger.LevelAttention(cbFunc, self, oCondition)
        

    
    def OnLevelInit(self):
        pass

    
    def InitEvent(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_SCENELOAD, self.LevelInit, 'SceneLoad%s' % self.m_Scene, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'LevelNode%d' % self.m_Scene)

    
    def OnPlayerMapLoadOK(self, _oLevelCtrl, oHero, dInfo):
        if self.m_Level != dInfo['LevelID']:
            return None
        if self.m_Status != LEVEL_STATUS_WAIT:
            LevelLog.Info('%s %s delayjoin mapid:%d levelid:%d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_Map, self.m_Level))
            cl_snetwar.GS2CLevelNodeLoadOk(self.m_Game, self.m_Scene, oHero.m_PlayerID, self.m_Level)
            lstLineName = []
            for oLine in self.m_RoomList[self.m_CurRoomPos]:
                lstLineName.append(oLine.m_Name)
            
            cl_snetwar.GS2CUpdateLevelRoomPos(self.m_Game, self.m_Scene, self.m_CurRoomPos, lstLineName)
        else:
            self.TryTriggerLevelStart()
        pid = oHero.m_PlayerID
        self.m_NodePlug.OnPlayerMapLoadOK([
            oHero.m_ID])
        if self.m_NotifyPlayerCntChange and pid not in self.m_NotifiedPlayer:
            self.m_NotifiedPlayer[pid] = 1
            dQuittedPlayer = self.m_QuittedPlayerInfo
            if dQuittedPlayer:
                for _iQuittedPlayer, dInfo in dQuittedPlayer.items():
                    cl_notify.SendCommonNotify(self.m_Game, [
                        pid], 1311, {
                        '$$playername': dInfo['Name'] })
                
            cl_notify.SendCommonNotify(self.m_Game, [
                pid], 2130, { })

    
    def TryTriggerLevelStart(self):
        LevelLog.Debug('%s trylevelstart %s %s' % (self.m_Game.m_ID, self.m_Status, self.m_Level))
        if self.CheckAllPlayerReady():
            self.LevelStart()

    
    def CheckAllPlayerReady(self):
        if self.m_Status != LEVEL_STATUS_WAIT:
            return False
        if not self.IsSceneLoaded():
            return False
        return True

    
    def LevelStart(self):
        if self.m_Status != LEVEL_STATUS_WAIT:
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        lstPlayer = list(oScene.GetPlayers())
        lstLivePlayer = self.m_Game.m_WarMgr.GetLivePlayer(iCalAI = 0)
        if not lstPlayer and lstLivePlayer:
            self.m_NodePlug.OverTimeStart()
            return None
        self.m_Status = LEVEL_STATUS_START
        LevelLog.Info('%s players%s levelstart mapid:%d levelid:%d' % (self.m_Game.m_ID, lstPlayer, self.m_Map, self.m_Level))
        for pid in lstPlayer:
            cl_snetwar.GS2CLevelNodeLoadOk(self.m_Game, self.m_Scene, pid, self.m_Level)
        
        dData = {
            'LevelType': self.m_LevelType,
            'LevelID': self.m_Level }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_Game.m_WarMgr, dData)
        self.LineStart(0)
        self.m_NodePlug.OnLevelStart()
        self.OnLevelStart()

    
    def OnLevelStart(self):
        pass

    
    def TryTriggerLevelGoal(self):
        if self.m_Status == LEVEL_STATUS_START:
            self.LevelGoal({ })

    
    def LevelGoal(self, dTrigger):
        self.m_Status = LEVEL_STATUS_GOAL
        dData = {
            'Scene': self.m_Scene,
            'LevelType': self.m_LevelType,
            'LevelID': self.m_Level,
            'Layer': self.m_CtrlMgr.m_LayerNum,
            'Level': self.m_CtrlMgr.m_LevelNum,
            'PassLevel': dTrigger['PassLevel'] if 'PassLevel' in dTrigger else True }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_Game.m_WarMgr, dData)
        cl_snetwar.GS2CLevelNodeGoalOk(self.m_Game, self.m_Scene, { })
        self.m_NodePlug.OnLevelGoal()
        self.OnLevelGoal(dTrigger)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_TRANSFERENABLE, self.m_Game.m_WarMgr, dData)

    
    def OnLevelGoal(self, dTrigger):
        pass

    
    def TryTriggerPassLevel(self, lstPlayer, dTransfer):
        if self.CheckLevelPass():
            self.m_CtrlMgr.CleanTranserInfo()
            self.PassLevel(lstPlayer, dTransfer)

    
    def CheckLevelPass(self):
        if self.m_Status != LEVEL_STATUS_GOAL:
            return False
        return True

    
    def PassLevel(self, lstPlayer, dTransfer):
        self.m_Status = LEVEL_STATUS_FINISH
        self.m_NodePlug.OnLevelFinish()
        self.OnPassLevel(lstPlayer, dTransfer)

    
    def OnPassLevel(self, lstPlayer, dTransfer):
        pass

    
    def IsPassLevel(self):
        return self.m_PassLevel

    
    def TryHeroEnterLevel(self, lstHero):
        if self.CheckHeroEnterLevel(lstHero):
            self.HeroEnterLevel(lstHero)

    
    def CheckHeroEnterLevel(self, _lstHero):
        return True

    
    def HeroEnterLevel(self, lstHero):
        if not self.IsSceneLoaded():
            self.m_PendEnterHero.extend(lstHero)
            return None
        self.m_NodePlug.OnHeroEnterLevel(lstHero)
        oGame = self.m_Game
        lstPlayer = [ oGame.GetObject(iHero).m_PlayerID for iHero in lstHero ]
        LevelLog.Info('%s players%s enterlevel mapid:%d levelid:%d lineinfo%s' % (self.m_Game.m_ID, lstPlayer, self.m_Map, self.m_Level, self.GetLevelLineInfo()))
        dGotoPos = self.GetGotoPos(lstHero)
        for iHero in lstHero:
            dBornInfo = dGotoPos[iHero]
            tBornPos = dBornInfo['Pos']
            tBornFace = dBornInfo['Facing']
            oHero = oGame.GetObject(iHero)
            oHero.SwitchSnipe(0)
            oHero.Goto(self.m_Scene, tBornPos, tBornFace)
        

    
    def GetGotoPos(self, lstHero):
        oGame = self.m_Game
        dGotoPos = { }
        dArchivePos = self.GetArchiveAssignPos()
        if dArchivePos:
            for iHero in lstHero:
                dGotoPos[iHero] = dArchivePos
            
            return dGotoPos
        dAssignBornPos = self.m_CtrlMgr.m_LevelAssignBornPos
        tBornInfo = self.GetBornPos()
        lstTempBornInfo = []
        for dBorn in tBornInfo:
            if dBorn not in self.m_InUseBorn:
                lstTempBornInfo.append(dBorn)
        
        if len(lstTempBornInfo) >= len(lstHero):
            tBornInfo = lstTempBornInfo
        lstBornShuf = ShufferList(oGame, tBornInfo)
        iLen = len(lstBornShuf)
        for idx, iHero in enumerate(lstHero):
            if idx >= iLen:
                idx = oGame.Random(iLen - 1)
            if iHero in dAssignBornPos and self.m_Level in dAssignBornPos[iHero]:
                dBornInfo = dAssignBornPos[iHero].pop(self.m_Level)
            else:
                dBornInfo = lstBornShuf[idx]
            dGotoPos[iHero] = dBornInfo
            self.m_InUseBorn.append(dBornInfo)
        
        return dGotoPos

    
    def GetArchiveAssignPos(self):
        oSaveElement = self.m_Game.m_WarMgr.GetComponent('SaveElement')
        if not oSaveElement:
            return { }
        dHero = oSaveElement.GetSavedHeroInfo()
        if not dHero:
            return { }
        if 'BLG' not in dHero:
            return { }
        dArchivePos = dHero['BLG']
        if dArchivePos['Level'] != self.m_Level:
            return { }
        return dArchivePos

    
    def GetLineNode(self, tLineIdx):
        if not tLineIdx:
            return None
        (_, iRoomIdx, iLineIdx) = tLineIdx
        if iRoomIdx >= len(self.m_RoomList) or iLineIdx >= len(self.m_RoomList[iRoomIdx]):
            return None
        return self.m_RoomList[iRoomIdx][iLineIdx]

    
    def GetLineNodeByArea(self, iArea):
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                if oLine.m_Area != iArea:
                    continue
                return oLine
            
        

    
    def LineStart(self, iRoomPos):
        if iRoomPos >= len(self.m_RoomList) or self.IsDirectLevelGoal():
            self.TryTriggerLevelGoal()
            return None
        if iRoomPos <= self.m_CurRoomPos:
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        lstPlayer = list(oScene.GetPlayers())
        LevelLog.Info('%s players%s levelid:%d room%d start' % (self.m_Game.m_ID, lstPlayer, self.m_Level, iRoomPos))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMSTART, self.m_CtrlMgr, {
            'Room': iRoomPos,
            'Level': self.m_Level,
            'oScene': oScene })
        self.m_CurRoomPos = iRoomPos
        lstLineName = []
        for oLine in self.m_RoomList[iRoomPos]:
            lstLineName.append(oLine.m_Name)
            oLine.LineStart()
        
        cl_snetwar.GS2CUpdateLevelRoomPos(self.m_Game, self.m_Scene, self.m_CurRoomPos, lstLineName)

    
    def LineGoal(self, iRoomPos):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        lstPlayer = list(oScene.GetPlayers())
        LevelLog.Debug('%s players%s levelid:%d room%d lockroom%s' % (self.m_Game.m_ID, lstPlayer, self.m_Level, iRoomPos, self.m_LockRoomPos))
        lstLine = self.m_RoomList[iRoomPos]
        for oLine in lstLine:
            if not oLine.IsGoal():
                LevelLog.Debug('game%s players%s levelid:%d room%d linenoGoal %s' % (self.m_Game.m_ID, lstPlayer, self.m_Level, iRoomPos, oLine.m_Name))
                return None
        
        cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_CtrlMgr, {
            'Room': iRoomPos,
            'Level': self.m_Level })
        if self.m_CurRoomPos != iRoomPos or self.CheckLevelPass():
            LevelLog.Debug('game%s players%s levelid:%d room%d wrongroom%d %s' % (self.m_Game.m_ID, lstPlayer, self.m_Level, iRoomPos, self.m_CurRoomPos, oLine.m_Name))
            return None
        if self.IsLockRoom(iRoomPos):
            return None
        LevelLog.Info('%s players%s levelid:%d room%d goal' % (self.m_Game.m_ID, lstPlayer, self.m_Level, iRoomPos))
        for oLine in lstLine:
            oLine.LineTargetReward()
        
        cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_CtrlMgr, {
            'Room': iRoomPos,
            'Level': self.m_Level,
            'oScene': oScene })
        self.EndUnderAttack(oScene)
        if self.m_LevelType == LEVEL_TYPE_FIGHT:
            lstBuild = oScene.GetObjectsByTypes([
                'Trap'])
            for iBuild in lstBuild:
                oBuild = self.m_Game.GetObject(iBuild)
                if not (oBuild.m_LineIdx) or oBuild.m_LineIdx[1] != iRoomPos:
                    continue
                oBuild.StopPerform()
            
        self.LineStart(iRoomPos + 1)
        if not (cllib.lib_flag.g_IsMobile) or self.m_LayerNum != 1 or self.m_LevelType != LEVEL_TYPE_FIGHT or len(self.m_RoomList) <= 1:
            return None
        iTimes = 0
        if (0) < iRoomPos:
            pass
        elif iRoomPos < len(self.m_RoomList) - 1:
            pass
        
        iSoundTimes = 1
        dPlayer = oScene.GetPlayers()
        lstBuild = oScene.GetObjectsByTypes([
            'GateControl'])
        for iBuild in lstBuild:
            if iTimes >= iSoundTimes:
                break
            oBuild = self.m_Game.GetObject(iBuild)
            if not oBuild:
                continue
            if not (oBuild.m_LineIdx) or oBuild.m_LineIdx[1] != iRoomPos:
                continue
            clsBuildData = self.m_Game.m_WarData.GetBuildData(oBuild.m_SID)
            if not clsBuildData or clsBuildData.m_DataSID != 1046:
                continue
            iTimes += 1
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, oBuild.m_ID, CLEVEL_FIRDOOR_OPEN, dPlayer)
        

    
    def CreateLineInfo(self, lstLineName):
        oLevelConfData = self.m_CtrlMgr.m_LevelConfData
        lstTopo = oLevelConfData.GetLevelConfig(self.m_Level, 'topology')
        dLineStore = oLevelConfData.GetLevelConfig(self.m_Level, 'arealine')
        oGame = self.m_Game
        lstLevelLine = []
        lstRoomLine = []
        iRound = self.m_Game.m_WarMgr.m_Round
        for iArea in lstTopo[0]:
            dRatio = dLineStore[iArea]
            sLine = ChooseKey(oGame, dRatio)
            iMerge = oLevelConfData.GetLineMergeFlag(self.m_Level, sLine, iRound)
            lstRoomLine.append(sLine)
            lstLineName.append(sLine)
            if not iMerge:
                lstLevelLine.append(lstRoomLine)
                lstRoomLine = []
        
        return levellinenode.CreateLineList(self, lstLevelLine)

    
    def InitAllLine(self):
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                oLine.LineInit()
            
        

    
    def GetLineIdxByArea(self, iTarArea):
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                iArea = oLine.m_Area
                if iArea == iTarArea:
                    return oLine.GetLineIdx()
            
        

    
    def GetLevelLineInfo(self):
        dLevelLine = { }
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                iArea = oLine.m_Area
                sLineName = oLine.m_Name
                dLevelLine[iArea] = sLineName
            
        
        return dLevelLine

    
    def IsDirectLevelGoal(self):
        if self.m_CustomData.get('BossLevelGoal', 0):
            return True
        return False

    
    def InitSceneConfigPos(self):
        oLevelConfData = self.m_CtrlMgr.m_LevelConfData
        dPosMap = {
            'rewardpos': 'reward',
            'shoppos': 'shop',
            'eventpos': 'event',
            'bossrewardpos': 'bossreward' }
        dLevelLine = oLevelConfData.GetLevelConfig(self.m_Level, 'arealine')
        for skey, sval in dPosMap.items():
            dPos = oLevelConfData.GetMapConfig(self.m_Level, skey)
            lstPos = []
            for iArea, _ in dLevelLine.items():
                if iArea not in dPos:
                    continue
                lstPos.extend(list(dPos[iArea]))
            
            lstPos = ShufferList(self.m_Game, lstPos)
            self.m_SceneConfigPos[sval] = {
                'Pos': lstPos,
                'Cur': 0 }
        

    
    def GetLineConfigPos(self, tLineIdx, sType, iAmount):
        oLine = self.GetLineNode(tLineIdx)
        if sType not in self.m_SceneConfigPos:
            return []
        lstPos = []
        iArea = oLine.m_Area
        dPosInfo = self.m_SceneConfigPos[sType]
        for dPos in dPosInfo['Pos']:
            if dPos['Area'] != iArea:
                continue
            lstPos.append(dPos)
        
        iTotal = len(dPosInfo['Pos'])
        iCur = dPosInfo['Cur']
        iNew = min(iTotal, iCur + iAmount)
        dPosInfo['Cur'] += iNew
        return lstPos[iCur:iNew]

    
    def GetSceneConfigPos(self, sType, iAmount, bMonopolize = True):
        if sType not in self.m_SceneConfigPos:
            return []
        dPosInfo = self.m_SceneConfigPos[sType]
        iTotal = len(dPosInfo['Pos'])
        if bMonopolize:
            iCur = dPosInfo['Cur']
            iNew = min(iTotal, iCur + iAmount)
            dPosInfo['Cur'] = iNew
            return dPosInfo['Pos'][iCur:iNew]
        iAmount = min(iTotal, iAmount)
        lstPos = ShufferList(self.m_Game, dPosInfo['Pos'])
        return lstPos[:iAmount]

    
    def ChooseRewardNpcPos(self, tLineIdx, iAmount):
        return self.GetLineConfigPos(tLineIdx, 'reward', iAmount)

    
    def ChooseLastEventNpcPos(self, iAmount):
        dPosInfo = self.m_SceneConfigPos['event']
        oLine = self.m_RoomList[-1][-1]
        iArea = oLine.m_Area
        lstPosInfo = dPosInfo['Pos']
        iTotal = len(lstPosInfo)
        iCur = dPosInfo['Cur']
        dReplace = { }
        for iPosIndex in range(iCur, iTotal):
            dPos = lstPosInfo[iPosIndex]
            if dPos['Area'] == iArea:
                iAmount -= 1
                dReplace[iPosIndex] = 1
                if iAmount <= 0:
                    break
        
        iNew = iCur
        for iPosIndex in dReplace:
            lstPosInfo[iNew] = lstPosInfo[iPosIndex]
            lstPosInfo[iPosIndex] = lstPosInfo[iNew]
            iNew += 1
        
        dPosInfo['Cur'] = iNew
        return dPosInfo['Pos'][iCur:iNew]

    
    def GetAllNpcPosCount(self, sType):
        if sType not in self.m_SceneConfigPos:
            return 0
        return len(self.m_SceneConfigPos[sType]['Pos'])

    
    def LockRoom(self, iRoomPos, sKey):
        setLock = self.m_LockRoomPos.setdefault(iRoomPos, set())
        setLock.add(sKey)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            LevelLog.Debug('%s players%s lock %d %s %s' % (self.m_Game.m_ID, list(oScene.GetPlayers()), iRoomPos, sKey, setLock))

    
    def UnlockRoom(self, iRoomPos, sKey):
        if iRoomPos not in self.m_LockRoomPos:
            return None
        setLock = self.m_LockRoomPos[iRoomPos]
        if sKey in setLock:
            setLock.remove(sKey)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            LevelLog.Debug('%s players%s unlock %d %s %s' % (self.m_Game.m_ID, list(oScene.GetPlayers()), iRoomPos, sKey, setLock))
        if not setLock:
            self.LineGoal(iRoomPos)

    
    def IsLockRoom(self, iRoomPos):
        if iRoomPos not in self.m_LockRoomPos:
            return False
        if not self.m_LockRoomPos[iRoomPos]:
            return False
        return True

    
    def GetAllLineMonsterCnt(self):
        dGroupCnt = { }
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                tLineIdx = oLine.GetLineIdx()
                iCnt = oLine.m_MonsterCtrl.GetRealMonsterCnt()
                dGroupCnt[tLineIdx] = iCnt
            
        
        return dGroupCnt

    
    def GetAllLineMonsterInfo(self):
        dMonsterSum = {
            'Live': 0,
            'Die': 0,
            'Wait': 0 }
        for lstLine in self.m_RoomList:
            for oLine in lstLine:
                sName = oLine.m_Name
                dSummary = oLine.m_MonsterCtrl.GetMonsterSummary()
                dMonsterSum[sName] = dSummary
                dMonsterSum['Live'] += dSummary['Live']
                dMonsterSum['Die'] += dSummary['Die']
                for iCnt in dSummary['Wait'].values():
                    dMonsterSum['Wait'] += iCnt
                
            
        
        return dMonsterSum

    
    def GetRoomMonsterInfo(self, iRoomPos):
        dMonsterSum = {
            'Live': 0,
            'Die': 0,
            'Wait': 0 }
        if iRoomPos < len(self.m_RoomList):
            for oRoomLine in self.m_RoomList[iRoomPos]:
                dSummary = oRoomLine.m_MonsterCtrl.GetMonsterSummary()
                dMonsterSum['Live'] += dSummary['Live']
                dMonsterSum['Die'] += dSummary['Die']
                for iCnt in dSummary['Wait'].values():
                    dMonsterSum['Wait'] += iCnt
                
            
        return dMonsterSum

    
    def DownSpawn(self, tAction, _oTarget):
        for dAction in tAction:
            if not levelspawnaction.CheckSpawn(self, dAction):
                continue
            func = dAction['func']
            func = levelspawnaction.GetSpawnFunc(func)
            if not func:
                continue
            param = dAction['param']
            func(self, param)
        

    
    def GetEliteInfo(self, iRoomPos, oLevelConfData):
        oGame = self.m_Game
        vElitePos = None
        dEliteDrop = None
        lstAllPos = []
        for oRoomLine in self.m_RoomList[iRoomPos]:
            dElitePos = oLevelConfData.GetLineConfig(self.m_Level, oRoomLine.m_Name, 'monsterelitepos')
            if not dElitePos:
                continue
            for dPos in dElitePos.values():
                lstAllPos.append(dPos)
            
        
        if lstAllPos:
            dPos = ShufferList(oGame, lstAllPos, 1)[0]
            vElitePos = dPos['Center']
            if 'FixDropPos' in dPos:
                dEliteDrop = {
                    'CheckDropInfo': dPos['CheckDropInfo'],
                    'FixDropPos': dPos['FixDropPos'] }
        return (vElitePos, dEliteDrop)

    
    def EndUnderAttack(self, oScene):
        for iHero in oScene.GetHeros():
            oHero = self.m_Game.GetObject(iHero)
            cl_state.RemoveState(oHero, STATE_UNDER_ATTACK)
        
        levelspawnaction.SpawnTriggerRoomGoalMusic(self, oScene)

    
    def GetMonsterSpawnInfo(self, iRoomPos):
        dSpawn = { }
        for oRoomLine in self.m_RoomList[iRoomPos]:
            dSpawn.update(oRoomLine.GetMonsterSpawnInfo())
        
        return dSpawn


