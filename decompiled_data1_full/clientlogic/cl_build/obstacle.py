# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_build/obstacle.pyc
# RelativePath: clientlogic/cl_build/obstacle.pyc
# Source Generated with Decompyle++
# File: obstacle.pyc (Python 3.6)

from C_component import ComNavObstacle
from cl_commondefines import PAMOD_TYPE_DYNA, WARRIOR_OBSTACLE_BROKENPILLAR, SCENE_EVT_SHAPE_RECTANGLE, WARRIOR_OBSTACLE_LVTRIDESTORY, WARRIOR_OBSTACLE_TRIDESTROY, GATE_TRANSFER_OPEN, WARRIOR_OBSTACLE_NORMAL, GATE_STATUS_OPEN, GATE_TRANSFER_CLOSE, GATE_STATUS_CLOSE, WARRIOR_OBSTACLE_SLIDEDOOR, WARRIOR_OBSTACLE_TRANGATE, WARRIOR_OBSTACLE_STATICTRAN, BUILD_SIMMASK_STOP, BUILD_SIMMASK_OPEN, WARRIOR_OBSTACLE_SIMCTRL, WARRIOR_OBSTACLE_CTRLGATE, WARRIOR_OBSTACLE_HINDER
from cl_pxlayer import PXLAYER_TRIDSTEVENT
from cl_only import Time2Frame, Functor
from cl_math import RotateByEuler, Vec3DisplaceDir
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_OBJECT
import cl_scene
import cl_snetwar
import cl_msgcenter
import cl_modeldata
import cl_engphyobj
from . import mobject
from . import net

class CObstacle(mobject.CBuild):
    m_Type = 'Obstacle'
    m_FightType = WARRIOR_OBSTACLE_NORMAL
    m_Source = 0
    
    def __init__(self, oGame, nid):
        super(CObstacle, self).__init__(oGame, nid)
        self.m_Action = { }

    
    def OnInitBuild(self, clsData, dAddData):
        self.m_Source = dAddData.get('Source', 0)
        dAction = dAddData.get('Other', { }).get('Action', { })
        for sAction, dInfo in dAction.items():
            self.m_Action[int(sAction)] = dInfo
        

    
    def OnInitToScene(self, tPos):
        super(CObstacle, self).OnInitToScene(tPos)
        if self.m_Source:
            if self.m_NavObstacle:
                self.m_NavObstacle.E_SetSrouceInit(self.m_Source)
            if self.m_FlyNavObstacle:
                self.m_FlyNavObstacle.E_SetSrouceInit(self.m_Source)

    
    def CalcRealDamage(self, sAttr, iDamType, _lstExtraFactorElement, iChange, iHas, oAttack, oReason):
        if self.m_LimitDam:
            iRealChange = min(iChange, self.m_LimitDam, iHas)
        else:
            iRealChange = min(iChange, iHas)
        return (iRealChange, 0)

    
    def DoAction(self, iAction, dParam):
        if iAction not in self.m_Action:
            return None
        tPos = self.m_Action[iAction]
        self.m_Game.Scene_Walk(self.m_ID, tPos)
        self.RefreshPos()
        if self.m_NavObstacle:
            self.m_NavObstacle.E_UpdatePosition()
        if self.m_FlyNavObstacle:
            self.m_FlyNavObstacle.E_UpdatePosition()
        cl_scene.GS2CMapTriggerGate(self, iAction)



class CGatecontrol(CObstacle):
    m_Type = 'GateControl'
    m_FightType = WARRIOR_OBSTACLE_CTRLGATE


class CSimcontrol(CObstacle):
    m_FightType = WARRIOR_OBSTACLE_SIMCTRL
    
    def __init__(self, oGame, nid):
        super(CSimcontrol, self).__init__(oGame, nid)
        self.m_MoveDisp = (0, 0, 0)

    
    def DoAction(self, iAction, dParam):
        if iAction not in self.m_Action:
            return None
        tMoveDisp = dParam['Disp']
        iTime = dParam['Time']
        iFrame = Time2Frame(iTime)
        tPos = (self.m_Pos[0] + tMoveDisp[0], self.m_Pos[1] + tMoveDisp[1], self.m_Pos[2] + tMoveDisp[2])
        self.m_MoveDisp = tMoveDisp
        cl_scene.GS2CMapTriggerGate(self, iAction)
        if iFrame:
            oGame = self.m_Game
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, Functor(self.OnMapLoadOK, iAction), 'SimObstacle')
            cl_snetwar.GS2CMapBuildSimMask(oGame, self.m_ID, BUILD_SIMMASK_OPEN, oGame.m_WarMgr.GetRoomPlayer())
            tVec = (tMoveDisp[0] / iFrame, tMoveDisp[1] / iFrame, tMoveDisp[2] / iFrame)
            self.m_Game.m_FrameMoveMgr.AddSimObj(self, tVec, iFrame)
        else:
            self.m_Game.Scene_Walk(self.m_ID, tPos)
            self.RefreshPos()
            self.m_NavObstacle.E_UpdatePosition()

    
    def UpdatePos(self, tVec):
        tPos = self.m_Pos
        tNewPos = (tPos[0] + tVec[0], tPos[1] + tVec[1], tPos[2] + tVec[2])
        self.m_Game.Scene_Walk(self.m_ID, tNewPos)
        self.RefreshPos()

    
    def TerminalPos(self):
        oGame = self.m_Game
        cl_snetwar.GS2CMapBuildSimMask(oGame, self.m_ID, BUILD_SIMMASK_STOP, oGame.m_WarMgr.GetRoomPlayer())
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'SimObstacle')
        self.m_NavObstacle.E_UpdatePosition()

    
    def OnMapLoadOK(self, iAction, oListener, oSender, dInfo):
        cl_scene.GS2CMapTriggerGate(oListener, iAction)
        cl_snetwar.GS2CMapBuildSimMask(oListener.m_Game, oListener.m_ID, BUILD_SIMMASK_OPEN, [
            oSender.m_PlayerID])



class CBaseGateTransfer(CObstacle):
    m_Type = 'GateControl'
    m_FightType = WARRIOR_OBSTACLE_TRANGATE
    
    def __init__(self, oGame, nid):
        super(CBaseGateTransfer, self).__init__(oGame, nid)
        self.m_TransferCom = CTransferCom(self)
        self.m_CloseBehavior = 0
        self.m_OpenBehavior = 0
        self.m_DelayTransferTime = 100
        self.m_HeroHideBehavior = 0
        self.m_HeroBornBehavior = 0
        self.m_DelayShowCloseTime = 100
        self.m_TransAreaInfo = { }

    
    def OnInitBuild(self, clsData, dAddData):
        super(CBaseGateTransfer, self).OnInitBuild(clsData, dAddData)
        self.m_TransAreaInfo = dAddData.get('Transfer', { })

    
    def EnterScene(self, iOldScene):
        super(CBaseGateTransfer, self).EnterScene(iOldScene)
        tPos = self.GetPos()
        tFace = self.GetFacing()
        if 'Trigger' not in self.m_TransAreaInfo:
            dParam = self.m_ModelData.GetServerData()
            tHalf = dParam['HalfExt']
            iLen = max(tHalf[0], tHalf[2])
            tHalf = (iLen, tHalf[1], iLen)
            tDir = RotateByEuler(tFace, (0, 180, 0))
            tCenter = Vec3DisplaceDir(tPos, tDir, iLen)
            tCenter = (tCenter[0], tCenter[1] + tHalf[1], tCenter[2])
        else:
            dTriggerArea = self.m_TransAreaInfo['Trigger']
            tCenter = dTriggerArea['Center']
            tHalf = dTriggerArea['HalfExt']
            tDir = dTriggerArea['Facing']
            iLen = max(tHalf[0], tHalf[2])
        if 'Transfer' not in self.m_TransAreaInfo:
            tTransPos = Vec3DisplaceDir(tPos, tFace, iLen + 1)
        else:
            dTransferArea = self.m_TransAreaInfo['Transfer']
            tTransPos = dTransferArea['Center']
        self.m_TransferCom.SetTransferInfo(tCenter, tHalf, tDir, tTransPos)

    
    def StartTransfer(self):
        pass

    
    def StopTransfer(self):
        pass

    
    def TriggerTransfer(self, oHero):
        pass

    
    def Release(self):
        self.m_TransferCom.Release()
        self.m_TransferCom = None
        super(CBaseGateTransfer, self).Release()

    
    def TriggerBehavior(self, iBehavior):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, iBehavior, dPlayer)



class CStaticGateTransfer(CBaseGateTransfer):
    m_FightType = WARRIOR_OBSTACLE_STATICTRAN
    m_RemoveDelay = 50
    
    def __init__(self, oGame, nid):
        super(CStaticGateTransfer, self).__init__(oGame, nid)
        self.m_Trigger = False

    
    def DirectRemove(self, sReason):
        self.m_TransferCom.DestoryTriggerArea()
        self.TriggerBehavior(self.m_OpenBehavior)
        super(CStaticGateTransfer, self).DirectRemove(sReason)

    
    def DoAction(self, iAction, dParam):
        self.m_Trigger = True
        self.TriggerBehavior(self.m_CloseBehavior)
        self.m_TransferCom.CreateTriggerArea()

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        if self.m_Trigger:
            for iPlayer in dPlayer:
                cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_CloseBehavior, [
                    iPlayer])
            

    
    def OnInitToScene(self, tPos):
        super(CStaticGateTransfer, self).OnInitToScene(tPos)
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iLayerNum = self.m_Game.m_WarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        if iLayerNum != 1:
            return None
        if not self.m_LineIdx:
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return None
        lstBuild = oScene.GetObjectsByTypes([
            'GateControl'])
        for iBuild in lstBuild:
            oBuild = self.m_Game.GetObject(iBuild)
            if not oBuild:
                continue
            if not (oBuild.m_LineIdx) or oBuild.m_LineIdx != self.m_LineIdx:
                continue
            if not oBuild.m_PendRemove:
                continue
            if oBuild.m_Prefab == self.m_Prefab:
                oBuild.Remove('SourceReplace')
        



class CGateTransfer(CBaseGateTransfer):
    m_FightType = WARRIOR_OBSTACLE_TRANGATE
    
    def __init__(self, oGame, nid):
        super(CGateTransfer, self).__init__(oGame, nid)
        self.m_TriggerCnt = 0

    
    def DoAction(self, iAction, dParam):
        super(CGateTransfer, self).DoAction(iAction, dParam)
        self.m_TriggerCnt += 1
        if not self.m_TriggerCnt % 2:
            self.m_TransferCom.CreateTriggerArea()
        else:
            self.m_TransferCom.DestoryTriggerArea()

    
    def StartTransfer(self):
        if self.m_DelayShowCloseTime:
            func = Functor(self.TriggerBehavior, self.m_CloseBehavior)
            self.Call_Out(func, Time2Frame(self.m_DelayShowCloseTime), 'TriggerCloseBehavior')
        else:
            self.TriggerBehavior(self.m_CloseBehavior)

    
    def StopTransfer(self):
        self.TriggerBehavior(self.m_OpenBehavior)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        if not self.m_TransferCom.IsOpenTrigger():
            return None
        for iPlayer in dPlayer:
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, self.m_CloseBehavior, [
                iPlayer])
        



class CSlidingDoorTransfer(CBaseGateTransfer):
    m_FightType = WARRIOR_OBSTACLE_SLIDEDOOR
    
    def __init__(self, oGame, nid):
        super(CSlidingDoorTransfer, self).__init__(oGame, nid)
        self.m_GateStatus = GATE_STATUS_CLOSE
        self.m_TranferStatus = GATE_TRANSFER_CLOSE

    
    def EnterScene(self, iOldScene):
        super(CSlidingDoorTransfer, self).EnterScene(iOldScene)
        self.TriggerBehavior(self.m_CloseBehavior)

    
    def DoAction(self, iAction, dParam):
        if not iAction:
            if not self.m_GateStatus == GATE_STATUS_OPEN:
                return None
            self.m_GateStatus = GATE_STATUS_CLOSE
            self.m_TranferStatus = GATE_TRANSFER_OPEN
            self.m_TransferCom.CreateTriggerArea()
            if self.m_NavObstacle:
                self.m_NavObstacle.E_Enable()
            if self.m_PhyModel:
                self.m_PhyModel.E_SetEnableSimulation(1)
            self.TriggerBehavior(self.m_CloseBehavior)
        elif not self.m_GateStatus == GATE_STATUS_CLOSE:
            return None
        self.m_GateStatus = GATE_STATUS_OPEN
        self.m_TranferStatus = GATE_TRANSFER_CLOSE
        self.m_TransferCom.DestoryTriggerArea()
        if self.m_NavObstacle:
            self.m_NavObstacle.E_Disable()
        if self.m_PhyModel:
            self.m_PhyModel.E_SetEnableSimulation(0)
        self.TriggerBehavior(self.m_OpenBehavior)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        iStatus = self.m_GateStatus | self.m_TranferStatus
        for pid in dPlayer:
            net.GS2CBuildGateStatus(pid, self.m_ID, iStatus)
        



class CTransferCom(object):
    
    def __init__(self, oOwner):
        self.m_Owner = oOwner
        self.m_Game = oOwner.m_Game
        self.m_Event = 0
        self.m_TriCenter = (0, 0, 0)
        self.m_TriHalf = (0, 0, 0)
        self.m_TriDir = (0, 0, 0)
        self.m_TransPos = (0, 0, 0)

    
    def Release(self):
        self.DestoryTriggerArea()
        self.m_Owner = None
        self.m_Game = None

    
    def IsOpenTrigger(self):
        return self.m_Event

    
    def SetTransferInfo(self, tTriCenter, tTriHalf, tTriDir, tTranferPos):
        self.m_TriCenter = tTriCenter
        self.m_TriHalf = tTriHalf
        self.m_TriDir = tTriDir
        oGame = self.m_Game
        fGroundDis = oGame.Scene_GroundDistance(self.m_Owner.m_Scene, (tTranferPos[0], tTranferPos[1] + 1.8, tTranferPos[2]), 5, PXMASK_MOVEBLK | PXMASK_OBJECT, self.m_Owner.m_ID)
        self.m_TransPos = (tTranferPos[0], (tTranferPos[1] - fGroundDis) + 1.8, tTranferPos[2])

    
    def CreateTriggerArea(self):
        oListener = self.m_Owner
        iScene = self.m_Owner.m_Scene
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        enterfunc = OnHeroTriggerTransfer
        leavefunc = None
        self.m_Event = oScene.AddSceneEvent(oListener, enterfunc, leavefunc, SCENE_EVT_SHAPE_RECTANGLE, (self.m_TriCenter, self.m_TriHalf), {
            'Dir': self.m_TriDir }, False)
        self.m_Owner.StartTransfer()

    
    def DestoryTriggerArea(self):
        if self.m_Event:
            oGame = self.m_Game
            iScene = self.m_Owner.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            oScene.RemoveSceneEvent(self.m_Event)
            self.m_Event = None
            self.m_Owner.StopTransfer()

    
    def HandleTransfer(self, oHero, iDelayTime):
        iHero = oHero.m_ID
        oFunc = Functor(self.DelayHandleTransfer, iHero)
        iDelayFrame = Time2Frame(iDelayTime)
        if iDelayTime:
            self.m_Owner.Call_Out(oFunc, iDelayFrame, 'TranferHero%d' % iHero)
        else:
            self.DelayHandleTransfer(iHero)

    
    def DelayHandleTransfer(self, iHero):
        iScene = self.m_Owner.m_Scene
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not oScene or iScene != oHero.m_Scene:
            return None
        oHero.Stop()
        oHero.WalkTo(self.m_TransPos)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERGATETRANSFER, oHero, {
            'VID': oHero.m_ID })
        self.m_Owner.TriggerTransfer(oHero)



def OnHeroTriggerTransfer(oListener, dMsgInfo):
    if not oListener:
        return None
    iTriggerObj = dMsgInfo['VID']
    obj = oListener.m_Game.GetObject(iTriggerObj)
    if obj.m_Side != 1:
        return None
    oTransCom = oListener.m_TransferCom
    iDelayTime = oListener.m_DelayTransferTime
    if oTransCom:
        oTransCom.HandleTransfer(obj, iDelayTime)


class CTriggerDestroy(CObstacle):
    m_Type = 'TriDestroy'
    m_FightType = WARRIOR_OBSTACLE_TRIDESTROY
    
    def __init__(self, oGame, nid):
        super(CTriggerDestroy, self).__init__(oGame, nid)
        self.m_TriggerShapeData = { }
        self.m_Trigger = None
        self.m_Triggered = False

    
    def OnInitBuild(self, clsData, dAddData):
        super(CTriggerDestroy, self).OnInitBuild(clsData, dAddData)
        dParam = dict(dAddData)
        dParam.update(dAddData['Trigger'])
        oModel = cl_modeldata.GetModel(dParam)
        self.m_TriggerShapeData = oModel.GetServerData()

    
    def OnInitToScene(self, tPos):
        super(CTriggerDestroy, self).OnInitToScene(tPos)
        if self.m_TriggerShapeData:
            self.m_Trigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self, PXLAYER_TRIDSTEVENT, self.m_TriggerShapeData, self.OnMonsterTrigger)

    
    def OnMonsterTrigger(self, obj, iLeave):
        if not obj:
            return None
        if self.m_Triggered or iLeave:
            return None
        self.m_Triggered = True
        vPos = obj.GetPos()
        vFace = obj.GetFacing()
        oFunc = Functor(self.DelayTriggerBehavior, vPos, vFace)
        self.Call_Out(oFunc, 2, 'DelayTriggerBehavior')

    
    def DelayTriggerBehavior(self, vPos, vFace):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        cl_snetwar.GS2CTriggerDestroyEffect(self.m_Game, self.m_ID, vPos, vFace, dPlayer)
        self.Remove('Triggered')

    
    def Release(self):
        self.m_Trigger = None
        super(CTriggerDestroy, self).Release()



class CLevelTriggerDestory(CObstacle):
    m_Type = 'LvTriDestroy'
    m_FightType = WARRIOR_OBSTACLE_LVTRIDESTORY
    
    def __init__(self, oGame, nid):
        super(CLevelTriggerDestory, self).__init__(oGame, nid)
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnTriggerDestory, 'LevelTriggerDestory')

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelTriggerDestory')
        super(CLevelTriggerDestory, self).Release()

    
    def OnTriggerDestory(self, oBuild, oOwner, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        tLineIdx = self.m_LineIdx
        if not tLineIdx or tLineIdx[0] != iLevel:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelTriggerDestory')
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        vPos = self.GetPos()
        vFace = self.GetFacing()
        cl_snetwar.GS2CTriggerDestroyEffect(self.m_Game, self.m_ID, vPos, vFace, dPlayer)
        self.Remove('LevelTrigger')



class CBrokenPillar(CObstacle):
    m_Type = 'brokenpillar'
    m_FightType = WARRIOR_OBSTACLE_BROKENPILLAR
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_PaModelData = []
        self.m_PaModel = []

    
    def OnInitBuild(self, clsData, dAddData):
        super().OnInitBuild(clsData, dAddData)
        self.m_PaModelData = dAddData['Models']

    
    def OnInitToScene(self, tPos):
        super().OnInitToScene(tPos)
        (_, _, iLayer, dParam) = self.GetModelAttr()
        for dModelData in sorted(self.m_PaModelData, key = (lambda item: item['Center'][1])):
            dParam.update(dModelData)
            oModel = cl_engphyobj.CreatePhyModel(self, PAMOD_TYPE_DYNA, iLayer, dParam)
            self.m_PaModel.append(oModel)
        

    
    def Release(self):
        for oModel in self.m_PaModel:
            oModel.m_Owner = None
        
        self.m_PaModel = []
        super().Release()



class CHinder(CObstacle):
    m_FightType = WARRIOR_OBSTACLE_HINDER

