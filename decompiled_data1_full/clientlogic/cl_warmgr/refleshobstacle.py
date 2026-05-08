# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/refleshobstacle.pyc
# RelativePath: clientlogic/cl_warmgr/refleshobstacle.pyc
# Source Generated with Decompyle++
# File: refleshobstacle.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_only import Frame2Time, Time2Frame, SendAlert, GAME_FRAME
from cl_cscommondef.cs_fight import WARRIOR_OBSTACLE_NORMAL
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_math
MAX_LOG_THRESHOLD_NUM = 50
SECOND_PER_MINUTE = 60

class CRefleshObstacle(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'RefleshObstacle'
        self.m_TimeFlag = 'TimeCheckDistance'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_ObstacleDict = { }
        self.m_Time = self.m_Data.m_Config.get('m_Time', 0)
        self.m_TargetTime = self.m_Data.m_Config.get('m_TargetTime', 0)
        self.m_TargetDistance = self.m_Data.m_Config.get('m_TargetDistance', 0)
        self.m_RefleshMoment = self.m_Game.GetFrameNum()
        self.m_RefleshMaxCnt = 0
        self.m_CurFrameCreateCnt = 0
        self.m_CreateCache = []
        self.m_InitCreateWindow = 6
        self.m_CreateWindow = self.m_InitCreateWindow

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEBUILD, self.OnCreateBuild, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.OnPlayerSettle, self.m_CallFlag)
        self.CheckDistancePer()

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEBUILD, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.m_CallFlag)
        self.Remove_Call_Out('FrameStep')
        self.Remove_Call_Out(self.m_TimeFlag)
        super().Release()

    
    def OnCreateBuild(self, oWarMgr, oTarget, dInfo):
        iBuildID = dInfo['BuildID']
        oBuild = self.m_Game.GetObject(iBuildID)
        if oBuild.m_FightType == WARRIOR_OBSTACLE_NORMAL:
            vPos = oBuild.GetPos()
            dTargetInfo = {
                'Pos': vPos,
                'Prefab': oBuild.m_Prefab,
                'SID': oBuild.m_SID,
                'DieFrame': 0 }
            self.m_ObstacleDict[oBuild.m_Prefab] = dTargetInfo

    
    def OnDie(self, oWarMgr, oTarget, dInfo):
        if oTarget.m_FightType == WARRIOR_OBSTACLE_NORMAL:
            iDieFrame = self.m_Game.GetFrameNum()
            if oTarget.m_Prefab in self.m_ObstacleDict:
                self.m_ObstacleDict[oTarget.m_Prefab]['DieFrame'] = iDieFrame

    
    def Step(self):
        self.Remove_Call_Out('FrameStep')
        self.Call_Out(self.Step, 1, 'FrameStep')
        self.ProcessCreateCache()

    
    def ProcessCreateCache(self):
        self.m_CurFrameCreateCnt = 0
        if not self.m_CreateCache:
            return None
        lstCreate = self.m_CreateCache[:self.m_CreateWindow]
        self.m_CreateCache = self.m_CreateCache[self.m_CreateWindow:]
        for dArgs in lstCreate:
            self.ReCreateBuild(dArgs)
        
        if not self.m_CreateCache:
            self.m_CreateWindow = self.m_InitCreateWindow
            self.Remove_Call_Out('FrameStep')
        else:
            iRestCnt = len(self.m_CreateCache)
            if iRestCnt > self.m_CreateWindow * 2:
                self.m_CreateWindow += self.m_InitCreateWindow

    
    def CheckDistancePer(self):
        if not self.m_Time and self.m_TargetTime and self.m_TargetDistance:
            SendAlert('err', '阻挡物刷新相关参数为零，请检查配置或向策划确认需求')
            return None
        iCheckFrame = self.m_Game.GetFrameNum()
        iRefleshCnt = 0
        iConsistentCnt = 0
        self.Remove_Call_Out(self.m_TimeFlag)
        self.Call_Out(self.CheckDistancePer, Time2Frame(self.m_Time), self.m_TimeFlag)
        lstRoomHero = self.m_Game.m_WarMgr.GetRoomHero()
        for dTargetInfo in self.m_ObstacleDict.values():
            iDieFrame = dTargetInfo['DieFrame']
            if iDieFrame and Frame2Time(iCheckFrame - iDieFrame) > self.m_TargetTime:
                for iHero in lstRoomHero:
                    oHero = self.m_Game.GetObject(iHero)
                    vHero = oHero.GetPos()
                    if cl_math.CheckDistance3D(dTargetInfo['Pos'], vHero, self.m_TargetDistance):
                        continue
                    iConsistentCnt += 1
                
            if iConsistentCnt == len(lstRoomHero):
                self.ReCreateBuild(dTargetInfo)
                iRefleshCnt += 1
            iConsistentCnt = 0
        
        if self.m_CreateCache:
            self.Step()
        if iRefleshCnt > self.m_RefleshMaxCnt:
            self.m_RefleshMaxCnt = iRefleshCnt
            self.m_RefleshMoment = iCheckFrame / GAME_FRAME // SECOND_PER_MINUTE

    
    def ReCreateBuild(self, dInfo):
        if self.m_CurFrameCreateCnt > self.m_InitCreateWindow:
            self.m_CreateCache.append(dInfo)
            return None
        self.m_CurFrameCreateCnt += 1
        iPrefab = dInfo['Prefab']
        iSID = dInfo['SID']
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        oLevelNode = oLevelCtrl.m_CurNode
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        iScene = oLevelNode.m_Scene
        for lstLevelLineObj in oLevelNode.m_RoomList:
            for oLevelLine in lstLevelLineObj:
                dObstacle = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLevelLine.m_Name, 'lineob')
                if iPrefab in dObstacle:
                    dReCreateInfo = dObstacle[iPrefab]
                    oGame.m_ResMgr.CreateBuild(iScene, iSID, dReCreateInfo, oLevelLine.GetLineIdx())
                    break
            
        

    
    def OnLevelNodeFinish(self, oWarMgr, oTarget, dInfo):
        self.m_ObstacleDict = { }
        oSurvivorElement = oWarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            self.Remove_Call_Out(self.m_TimeFlag)

    
    def OnPlayerSettle(self, oWarMgr, oTarget, dInfo):
        if self.m_RefleshMaxCnt > MAX_LOG_THRESHOLD_NUM:
            WarobjLog.Info('moment:%d minutes, max:%d obstacles created' % (self.m_RefleshMoment, self.m_RefleshMaxCnt))



def GetComponentClass(oMgrManager):
    return CRefleshObstacle

