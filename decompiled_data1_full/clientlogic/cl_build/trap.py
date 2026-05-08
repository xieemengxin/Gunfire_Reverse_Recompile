# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_build/trap.pyc
# RelativePath: clientlogic/cl_build/trap.pyc
# Source Generated with Decompyle++
# File: trap.pyc (Python 3.6)

from cl_commondefines import FAKERPLANK_STATUS_DISAPPEAR, FAKERPLANK_STATUS_APPEAR, WARRIOR_TRAP_VENT, WARRIOR_TRAP_ROTATEPILLAR, BUILD_SIMMASK_STOP, WARRIOR_TRAP_NORMAL, BUILD_SIMMASK_OPEN, WARRIOR_TRAP_UPSTONE, WARRIOR_TRAP_STONE, WARRIOR_TRAP_SMASH, LEVEL_STATUS_WAIT, WARRIOR_TRAP_MOVEPLANE, MOVE_CONTINUITY, MOVE_UNIDIRECTION, WARRIOR_TRAP_FAKERPLANK, PLAYMODE_SURVIVOR, WARRIOR_TRAP_THUNDERBUCKET
from cl_only import Functor, Time2Frame, Second2Frame, GAME_FRAME, Frame2Time, SendAlert
import cl_war
import cl_math
import cl_snetwar
import cl_msgcenter
import cl_scene
import cl_modeldefine
import math
from . import mobject
from . import net

class CTrap(mobject.CBuild):
    m_Type = 'Trap'
    m_FightType = WARRIOR_TRAP_NORMAL
    
    def __init__(self, oGame, iOwner):
        super(CTrap, self).__init__(oGame, iOwner)
        self.m_PerformInfo = { }
        self.m_BeginBehavior = 0
        self.m_OverBehavior = 0
        self.m_CloseBehavior = 8076
        self.m_Trigger = False
        self.m_Close = False

    
    def AttrCache(self):
        dCache = super().AttrCache()
        dTemp = { }
        for iPerform, dPerform in self.m_PerformInfo.items():
            dTemp[iPerform] = dict(dPerform)
            dTemp[iPerform]['IntervalTimeList'] = list(dPerform['IntervalTimeList'])
            dTemp[iPerform]['CustomParam'] = []
            for dParam in dPerform['CustomParam']:
                dTemp[iPerform]['CustomParam'].append(dict(dParam))
            
        
        dCache['TrapPerformInfo'] = dTemp
        return dCache

    
    def OnInitBuild(self, clsData, dAddData):
        iLiveTime = dAddData['Live']
        lstPerform = dAddData['Perform']
        self.DelayRemove(iLiveTime)
        for dPerform in lstPerform:
            self.AddPerformInfo(dPerform['Perform'], dPerform)
        

    
    def EnterScene(self, iOldScene):
        super(CTrap, self).EnterScene(iOldScene)
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode.m_Status != LEVEL_STATUS_WAIT:
            self.OnLevelStartFight(self, oGame.m_WarMgr, { })
        else:
            cl_msgcenter.AddAttentionFunc(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStartFight, 'TrapLevelStart')

    
    def DoAction(self, iAction, dParam):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        if self.m_BeginBehavior:
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_BeginBehavior, dPlayer)
            self.m_Trigger = True

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        if self.m_Trigger and self.m_OverBehavior:
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_OverBehavior, dPlayer)
        if self.m_Close and self.m_CloseBehavior:
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_CloseBehavior, dPlayer)

    
    def OnLevelStartFight(self, oTrap, oWarMgr, dInfo):
        if oWarMgr.m_PlayMode == PLAYMODE_SURVIVOR:
            return None
        if not self.Find_Call_Out('DonePerform'):
            self.DonePerform()

    
    def AddPerformInfo(self, iPerform, dPerform):
        if not dPerform['IntervalTimeList']:
            return None
        iTimes = dPerform['Times']
        lstIntervalFrame = []
        for iIntervalTime in dPerform['IntervalTimeList']:
            lstIntervalFrame.append(Time2Frame(iIntervalTime))
        
        oPerform = self.m_Perform.GetPerform(iPerform)
        if not oPerform:
            oPerform = self.AddPerform(iPerform, 1)
        if not oPerform:
            return None
        oGame = self.m_Game
        iNextFrame = oGame.GetFrameNum() + 1
        self.m_PerformInfo[iPerform] = {
            'MaxTimes': iTimes,
            'CurTimes': 0,
            'IntervalTimeList': lstIntervalFrame,
            'NextFrame': iNextFrame,
            'CustomParam': dPerform['CustomParam'] }

    
    def DelPerformInfo(self, iPerform):
        if iPerform in self.m_PerformInfo:
            self.m_PerformInfo.pop(iPerform)
        self.m_Perform.RemovePerform(self, iPerform)

    
    def DonePerform(self):
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        lstRemove = []
        lstNextFrame = []
        for iPerform, dInfo in self.m_PerformInfo.items():
            iNextFrame = dInfo['NextFrame']
            if iNextFrame > iCurFrame:
                continue
            oPerform = self.m_Perform.GetPerform(iPerform)
            cl_war.UsePerform(self, oPerform, { })
            iCurTimes = dInfo['CurTimes']
            iMaxTimes = dInfo['MaxTimes']
            if iMaxTimes and iCurTimes + 1 >= iMaxTimes:
                lstRemove.append(iPerform)
                continue
            lstInterval = dInfo['IntervalTimeList']
            iInterval = lstInterval[iCurTimes % len(lstInterval)]
            iNextFrame = oPerform.GetCDTime(self) + iInterval + iCurFrame
            dInfo['NextFrame'] = max(1, iNextFrame)
            dInfo['CurTimes'] = iCurTimes + 1
            lstNextFrame.append(iNextFrame - iCurFrame)
        
        for iPerform in lstRemove:
            self.m_PerformInfo.pop(iPerform)
        
        if not self.m_PerformInfo:
            return None
        iDelayFrame = 0xFFFFFFFF
        for dPerform in self.m_PerformInfo.values():
            iDelayFrame = min(iDelayFrame, dPerform['NextFrame'] - iCurFrame)
        
        self.Call_Out(self.DonePerform, iDelayFrame, 'DonePerform')

    
    def StopPerform(self):
        self.Remove_Call_Out('DonePerform')
        self.m_Close = True
        if self.m_CloseBehavior:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            dPlayer = oScene.GetPlayers()
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_CloseBehavior, dPlayer)

    
    def DelayRemove(self, iLiveTime):
        if not iLiveTime:
            return None
        iLifeFrame = Time2Frame(iLiveTime)
        self.Call_Out(Functor(self.Remove, '到时删除'), iLifeFrame, 'Remove')

    
    def Release(self):
        super(CTrap, self).Release()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'TrapLevelStart')



class CMashTrap(CTrap):
    m_FightType = WARRIOR_TRAP_SMASH
    m_ValidShowTips = 1


class CStoneTrap(CTrap):
    m_FightType = WARRIOR_TRAP_STONE
    
    def __init__(self, oGame, iOwner):
        super(CStoneTrap, self).__init__(oGame, iOwner)
        self.m_RollTime = 1
        self.m_RollLineID = 0

    
    def OnInitBuild(self, clsData, dAddData):
        super(CStoneTrap, self).OnInitBuild(clsData, dAddData)
        self.m_RollTime = dAddData['RollTime']
        if 'RollLineID' in dAddData:
            self.m_RollLineID = dAddData['RollLineID']

    
    def RollTime(self):
        return self.m_RollTime

    
    def AttrCache(self):
        dAttr = super(CStoneTrap, self).AttrCache()
        dAttr.update({
            'RollTime': self.RollTime(),
            'RollLineID': self.m_RollLineID })
        return dAttr



class CUpStoneTrap(CTrap):
    m_FightType = WARRIOR_TRAP_UPSTONE
    
    def __init__(self, oGame, nid):
        super(CUpStoneTrap, self).__init__(oGame, nid)
        self.m_Action = { }
        self.m_DoAction = 0
        self.m_NextFrame = 0

    
    def OnInitBuild(self, clsData, dAddData):
        self.m_Action = dAddData['Action']
        self.m_NextFrame = Time2Frame(dAddData['TotalTime'])
        super(CUpStoneTrap, self).OnInitBuild(clsData, dAddData)

    
    def OnLevelStartFight(self, oTrap, oWarMgr, dInfo):
        super(CUpStoneTrap, self).OnLevelStartFight(oTrap, oWarMgr, dInfo)
        if self.m_NextFrame:
            self.RepeatCallAction()

    
    def RepeatCallAction(self):
        for sAction, dAction in self.m_Action.items():
            iDelayFrame = Time2Frame(dAction['DelayTime'])
            if iDelayFrame:
                self.Call_Out(Functor(self.DoAction, sAction), iDelayFrame, 'RepeatCallOne')
                continue
            self.DoAction(sAction)
        
        self.Call_Out(self.RepeatCallAction, self.m_NextFrame, 'RepeatCallAll')

    
    def DoAction(self, sAction):
        dAction = self.m_Action[sAction]
        fSpeed = dAction['Speed']
        if fSpeed <= 0:
            return None
        tPos = dAction['EndPos']
        fSecond = cl_math.CalDistance3D(self.GetPos(), tPos) / fSpeed
        iFrame = Second2Frame(fSecond)
        cl_scene.GS2CMapTriggerUpStone(self, tPos, fSpeed)
        if iFrame:
            oGame = self.m_Game
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, 'UpStoneTrap')
            self.m_DoAction = sAction
            cl_snetwar.GS2CMapBuildSimMask(oGame, self.m_ID, BUILD_SIMMASK_OPEN, oGame.m_WarMgr.GetRoomPlayer())
            tMoveDisp = (tPos[0] - self.m_Pos[0], tPos[1] - self.m_Pos[1], tPos[2] - self.m_Pos[2])
            tVec = (tMoveDisp[0] / iFrame, tMoveDisp[1] / iFrame, tMoveDisp[2] / iFrame)
            self.m_Game.m_FrameMoveMgr.AddSimObj(self, tVec, iFrame)
        else:
            self.RefreshPos()

    
    def UpdatePos(self, tVec):
        tPos = self.m_Pos
        tNewPos = (tPos[0] + tVec[0], tPos[1] + tVec[1], tPos[2] + tVec[2])
        self.m_Game.Scene_Walk(self.m_ID, tNewPos)
        self.RefreshPos()

    
    def TerminalPos(self):
        oGame = self.m_Game
        cl_snetwar.GS2CMapBuildSimMask(oGame, self.m_ID, BUILD_SIMMASK_STOP, oGame.m_WarMgr.GetRoomPlayer())
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'UpStoneTrap')
        self.m_DoAction = ''

    
    def OnMapLoadOK(self, oListener, oSender, dInfo):
        dAction = self.m_Action[self.m_DoAction]
        fSpeed = dAction['Speed']
        tPos = dAction['EndPos']
        cl_scene.GS2CMapTriggerUpStone(self, tPos, fSpeed)
        cl_snetwar.GS2CMapBuildSimMask(oListener.m_Game, oListener.m_ID, BUILD_SIMMASK_OPEN, [
            oSender.m_PlayerID])

    
    def Release(self):
        super(CUpStoneTrap, self).Release()
        self.TerminalPos()



class CRotatePillar(mobject.CBuild):
    m_FightType = WARRIOR_TRAP_ROTATEPILLAR
    
    def __init__(self, oGame, iOwner):
        super(CRotatePillar, self).__init__(oGame, iOwner)
        self.m_StartFrame = 0
        self.m_RotateLayer = { }
        self.m_VentInfo = { }
        self.m_VentNum = 0
        self.m_NetRecord = []

    
    def AttrCache(self):
        dCache = super().AttrCache()
        return dCache

    
    def OnInitBuild(self, clsData, dAddData):
        self.m_VentInfo = {
            'Perform': dAddData['Perform'],
            'VentSID': dAddData['VentSID'],
            'Live': dAddData['Live'],
            'Vents': { } }
        for dLayerParam in dAddData['RotateLayer']:
            iLayer = dLayerParam['Layer']
            fVelocity = dLayerParam['Velocity']
            self.m_RotateLayer[iLayer] = {
                'Velocity': fVelocity / GAME_FRAME,
                'Vents': { } }
            self.m_VentInfo['Vents'][iLayer] = dLayerParam['Vents']
        

    
    def OnInitToScene(self, tPos):
        super(CRotatePillar, self).OnInitToScene(tPos)
        iVentSID = self.m_VentInfo['VentSID']
        oGame = self.m_Game
        self.m_StartFrame = oGame.GetFrameNum()
        for iLayer, lstVent in self.m_VentInfo['Vents'].items():
            for dVent in lstVent:
                radiansy = cl_math.CalRotate2D(dVent['Dir'])
                dAddData = { }
                dAddData['Perform'] = self.m_VentInfo['Perform']
                dAddData['Live'] = self.m_VentInfo['Live']
                dAddData['Origin'] = self.GetPos()
                dAddData['Center'] = dVent['Offset']
                dAddData['Size'] = (0.1, 0.1, 0.1)
                dAddData['Scale'] = (1, 1, 1)
                dAddData['Shape'] = 1
                dAddData['Angle'] = (0, radiansy, 0)
                dAddData['Bind'] = self
                dAddData['Layer'] = iLayer
                dAddData['LocalDir'] = dVent['Dir']
                oBuild = self.m_Game.m_ResMgr.CreateBuild(self.m_Scene, iVentSID, dAddData, self.m_LineIdx)
                iVent = dVent['Idx']
                self.m_RotateLayer[iLayer]['Vents'][iVent] = oBuild.m_ID
                self.m_VentNum += 1
            
        

    
    def UpdateLayerRadian(self, iLayer):
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        dLayerInfo = self.m_RotateLayer[iLayer]
        fVelocity = dLayerInfo['Velocity']
        fRadian = (iCurFrame - self.m_StartFrame) * fVelocity
        fRadian = fRadian % 360
        iRadian = int(fRadian) if fRadian > 0 else int(fRadian + 360)
        return iRadian

    
    def GetLayerVentInfo(self, iLayer, vOffset, vDir):
        iRadian = self.UpdateLayerRadian(iLayer)
        vOri = cl_math.RotateAroundVector(vOffset, (0, 1, 0), iRadian)
        vDest = cl_math.Vec3Add(vOffset, vDir)
        vDest = cl_math.RotateAroundVector(vDest, (0, 1, 0), iRadian)
        vNewDir = cl_math.Vec3Minus(vDest, vOri)
        radiany = cl_math.CalRotate2D(vNewDir)
        radiany = radiany * cl_math.g_InvRa
        vPos = self.GetPos()
        vCur = cl_math.Vec3Add(vPos, vOffset)
        return ((0, radiany, 0), vCur)

    
    def RecordNetAdd(self, iBuild, dPlayer):
        if iBuild in self.m_NetRecord:
            return None
        self.m_NetRecord.append(iBuild)
        if len(self.m_NetRecord) > self.m_VentNum:
            self.m_NetRecord.clear()
            net.GS2CPillarInfo(self.m_Game, self.m_ID, self.m_StartFrame, self.m_RotateLayer, dPlayer)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        self.RecordNetAdd(self.m_ID, dPlayer)



class CVentTrap(CTrap):
    m_FightType = WARRIOR_TRAP_VENT
    
    def __init__(self, oGame, iOwner):
        super(CVentTrap, self).__init__(oGame, iOwner)
        self.m_Bind = None
        self.m_Layer = 0
        self.m_Offset = (0, 0, 0)
        self.m_Dir = (0, 0, 1)
        self.m_Euler = (0, 0, 0)

    
    def OnInitBuild(self, clsData, dAddData):
        super(CVentTrap, self).OnInitBuild(clsData, dAddData)
        self.m_Bind = dAddData['Bind']
        self.m_Layer = dAddData['Layer']
        self.m_Offset = dAddData['Center']
        self.m_Dir = dAddData['LocalDir']

    
    def RefreshPosInfo(self):
        if self.m_Bind:
            (tEuler, tPos) = self.m_Bind.GetLayerVentInfo(self.m_Layer, self.m_Offset, self.m_Dir)
            self.m_Euler = tEuler
            self.m_Pos = tPos

    
    def SetEuler(self, tEuler):
        pass

    
    def GetEuler(self):
        self.RefreshPosInfo()
        return self.m_Euler

    
    def SetPos(self, tPos):
        pass

    
    def GetPos(self):
        self.RefreshPosInfo()
        return self.m_Pos

    
    def RefreshPos(self):
        return self.GetPos()

    
    def Release(self):
        super(CVentTrap, self).Release()
        self.m_Bind = None

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        oBind = self.m_Bind
        if oBind:
            oBind.RecordNetAdd(self.m_ID, dPlayer)



class CMovePlaneTrap(CTrap):
    m_FightType = WARRIOR_TRAP_MOVEPLANE
    
    def __init__(self, oGame, iOwner):
        super(CMovePlaneTrap, self).__init__(oGame, iOwner)
        self.m_StartFrame = 0
        self.m_DelayTime = 0
        self.m_Action = { }
        self.m_PrePathNum = { }
        self.m_CurPathNum = ''
        self.m_StartPath = ''
        self.m_StartPos = None
        self.m_BornPos = None
        self.m_Type = 0

    
    def OnInitBuild(self, clsData, dAddData):
        super(CMovePlaneTrap, self).OnInitBuild(clsData, dAddData)
        self.m_Action = dAddData['Action']
        self.m_Type = dAddData['MovePlaneType']
        self.m_DelayTime = dAddData['DelayTime']
        lstNum = list(self.m_Action.keys())
        for index, iPathNum in enumerate(lstNum):
            if index > 0:
                self.m_PrePathNum[lstNum[index - 1]] = iPathNum
        
        self.m_StartPath = lstNum[0]

    
    def OnInitToScene(self, tPos):
        super(CMovePlaneTrap, self).OnInitToScene(tPos)
        self.m_BornPos = tPos
        self.m_StartPos = tPos
        if self.m_DelayTime:
            iDelayFrame = Time2Frame(self.m_DelayTime)
            self.Call_Out(Functor(self.DoMove, self.m_StartPath, tPos), iDelayFrame, 'CallDoMove')
        else:
            self.DoMove(self.m_StartPath, tPos)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        if not self.m_StartFrame:
            return None
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        iFrame = iCurFrame - self.m_StartFrame
        if not self.m_CurPathNum:
            sStartPath = self.m_StartPath
        else:
            sStartPath = self.m_CurPathNum
        fSpeed = self.m_Action[sStartPath]['Speed']
        tEnd = self.m_Action[sStartPath]['EndPos']
        iRunTime = Frame2Time(iFrame) / 100
        fAcceSpeed = self.m_Action[sStartPath]['AcceSpeed']
        if fAcceSpeed:
            fMoveDis = fSpeed * iRunTime + fAcceSpeed * iRunTime * iRunTime / 2
        else:
            fMoveDis = fSpeed * iRunTime
        vStart = cl_math.Vec3DisplacePos(self.m_StartPos, tEnd, fMoveDis)
        net.GS2CPlankMove(self.m_ID, iCurFrame, fSpeed, fAcceSpeed, vStart, tEnd, dPlayer)

    
    def DoMove(self, sPath, tStartPos):
        self.m_CurPathNum = sPath
        self.m_StartPos = tStartPos
        oGame = self.m_Game
        dPlayer = oGame.GetRealPlayers()
        self.m_StartFrame = oGame.GetFrameNum()
        fSpeed = self.m_Action[sPath]['Speed']
        tEnd = self.m_Action[sPath]['EndPos']
        fAcceSpeed = self.m_Action[sPath]['AcceSpeed']
        net.GS2CPlankMove(self.m_ID, self.m_StartFrame, fSpeed, fAcceSpeed, tStartPos, tEnd, dPlayer)
        if fAcceSpeed:
            iDelayTime = int(((-fSpeed + math.sqrt(fSpeed * fSpeed + 2 * fAcceSpeed * cl_math.CalDistance3D(tStartPos, tEnd))) / fAcceSpeed) * 100 + self.m_Action[sPath]['MoveInterval'])
        else:
            iDelayTime = int((cl_math.CalDistance3D(tStartPos, tEnd) / fSpeed) * 100 + self.m_Action[sPath]['MoveInterval'])
        iDelayFrame = Time2Frame(iDelayTime)
        if self.m_Type == MOVE_UNIDIRECTION:
            sNextNum = self.m_StartPath
            tEnd = self.m_BornPos
        elif self.m_Type == MOVE_CONTINUITY:
            if self.m_CurPathNum not in self.m_PrePathNum:
                sNextNum = self.m_StartPath
                tEnd = self.m_BornPos
            else:
                sNextNum = self.m_PrePathNum[self.m_CurPathNum]
        else:
            iScene = self.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            iLevel = oScene.m_Level
            SendAlert('err', f'''关卡{iLevel} 不存在移动板类型 {self.m_Type}''')
            return None
        if iDelayFrame:
            self.Remove_Call_Out('CallDoMove')
            self.Call_Out(Functor(self.DoMove, sNextNum, tEnd), iDelayFrame, 'CallDoMove')
        else:
            self.DoMove(sNextNum, tEnd)



class CFakerPlanKTrap(CTrap):
    m_FightType = WARRIOR_TRAP_FAKERPLANK
    
    def __init__(self, oGame, iOwner):
        super(CFakerPlanKTrap, self).__init__(oGame, iOwner)
        self.m_RecoveryFrame = 75
        self.m_Status = FAKERPLANK_STATUS_APPEAR

    
    def OnInitBuild(self, clsData, dAddData):
        super(CFakerPlanKTrap, self).OnInitBuild(clsData, dAddData)
        self.m_RecoveryFrame = Time2Frame(dAddData['DisappearTime'])

    
    def OnContact(self, iTarget, dArgs):
        self.TriggerBehavior(0)
        self.m_PhyModel.SetEnableSimulation(0)
        self.m_PhyModel.SetEnableSceneQuery(0)
        self.m_Status = FAKERPLANK_STATUS_DISAPPEAR
        self.Remove_Call_Out('PlankRecovery')
        self.Call_Out(self.PlankRecovery, self.m_RecoveryFrame, 'PlankRecovery')

    
    def PlankRecovery(self):
        self.TriggerBehavior(1)
        self.m_Status = FAKERPLANK_STATUS_APPEAR
        self.m_PhyModel.SetEnableSimulation(1)
        self.m_PhyModel.SetEnableSceneQuery(1)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        if self.m_Status == FAKERPLANK_STATUS_DISAPPEAR:
            self.TriggerBehavior(0, dPlayer)

    
    def TriggerBehavior(self, iStop, dPlayer = None):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not dPlayer:
            dPlayer = oScene.GetPlayers()
        cl_snetwar.GS2CTriggerBehavior(oGame, self.m_ID, 8077, dPlayer, iStop)



class CThunderBucket(CTrap):
    m_FightType = WARRIOR_TRAP_THUNDERBUCKET

