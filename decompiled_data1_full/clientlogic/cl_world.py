# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_world.pyc
# RelativePath: clientlogic/cl_world.pyc
# Source Generated with Decompyle++
# File: cl_world.pyc (Python 3.6)

from C_component import ComNavObstacle
from C_customnet import TransVarLong
from cl_only import DeepCopy, CELL_SPACESIZE, TraceLog
from cl_commondefines import SPEED_BASE, NAV_TYPE_NULL, MODEL_TYPE_CTRLAGENT, WARRIOR_HERO, NAV_TYPE_CROWDAGENT, NAV_TYPE_OBSTACLE, NAV_TYPE_FLY, PAMOD_TYPE_NULL, MOVE_TYPE_NORMAL, WARRIOR_SERVANT, WARRIOR_DEVICE, WARRIOR_PET, WARRIOR_OBSTACLE_NORMAL
from cl_object.logging import WarobjLog
from cl_propdata import PC_SEND_SBC
import struct
import cllib.lib_json as json
import cllib.lib_flag
import cl_duonet.netfunc as net
import cl_msgcenter
import cl_scene
import cl_netattr
import cl_modeldata
import cl_engobjconf
import cl_snetwar
import cl_pxlayer
import cl_timer
import cl_netattr
import cl_modeldefine
PACKET_TYPE_LEN = 1

class CObject(object):
    
    def __init__(self, oGame, iObjID):
        self.m_ID = iObjID
        self.m_Game = oGame

    
    def Remove(self, sReason):
        
        try:
            self.m_Game.Scene_DelObject(self.m_ID)
            cl_scene.GS2CMapDel(self)
        except RuntimeError:
            print('NPC %d 已经从场景内删除' % self.m_ID)

        
        try:
            self.m_Game.DeleteObject(self.m_ID)
        except RuntimeError:
            print('NPC %d 物件已经删除过' % self.m_ID)

        self.m_Game = None

    
    def RemoveFromScene(self):
        self.m_Game.Scene_DelObject(self.m_ID)
        cl_scene.GS2CMapDel(self)
        self.m_Scene = 0

    
    def RemoveFromList(self):
        self.m_Game.DeleteObject(self.m_ID)
        self.m_Game = None

    
    def Call_Out(self, func, iDelay, sFlag):
        if iDelay < 1:
            sText = '%d:%s delay is %d' % (self.m_ID, sFlag, iDelay)
            if cllib.lib_flag.g_IsAuthorityRun:
                TraceLog('err', sText)
            WarobjLog.Error(sText)
            iDelay = 1
        self.m_Game.TimerCall(self.m_ID, func, iDelay, sFlag)

    
    def Remove_Call_Out(self, sFlag):
        self.m_Game.RemoveTimerCall(self.m_ID, sFlag)

    
    def Find_Call_Out(self, sFlag):
        return self.m_Game.FindTimerCall(self.m_ID, sFlag)

    
    def RemoveAllCallOut(self):
        self.m_Game.RemoveAllCallOut(self.m_ID)

    
    def IsSceneObj(self):
        return 0



class CSceneObject(CObject):
    m_SID = 0
    m_Shape = 0
    m_Name = '无名'
    m_Type = 'SceneObj'
    m_FightType = 0
    m_PropType = 0
    m_PropChangeBCType = PC_SEND_SBC
    
    def __str__(self):
        return '%s-%s-%s-%s-%s-%s' % (self.__class__, self.m_GameID, self.m_PlayerID, self.m_SID, self.m_ID, self.m_Scene)

    
    def __repr__(self):
        return '%s-%s-%s-%s-%s-%s' % (self.__class__, self.m_GameID, self.m_PlayerID, self.m_SID, self.m_ID, self.m_Scene)

    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        oGame.CreateObject(nid, self)
        self.m_GameID = oGame.m_ID
        self.m_PlayerID = 0
        self.m_OwnerPlayerID = 0
        self.m_ReleaseFlag = 0
        self.m_InitScene = 0
        self.m_Scene = 0
        self.m_Pos = (1, 1, 1)
        self.m_Side = 1
        self.m_Speed = SPEED_BASE
        self.m_WinkSpeed = 0
        self.m_Agent = None
        self.m_MoveMode = MOVE_TYPE_NORMAL
        self.m_EvtCtrl = cl_msgcenter.NewEventCtrl()
        self.m_ReceiveAttention = []
        self.m_MoveCtrl = None
        self.m_FaceCtrl = None
        self.m_Area = { }
        self.m_Data = { }
        self.m_SavedData = { }
        self.m_ExtPacketFunc = { }
        self.m_ModelData = None
        self.m_ModelRadius = 0.3
        self.m_ModelHeight = 1.7
        self.m_LineIdx = None
        self.m_NavObstacle = None
        self.m_PhyModel = None
        self.m_FlyNavObstacle = None

    
    def IsSceneObj(self):
        return 1

    
    def ClearPacket(self, iPacketIdx = -1):
        if iPacketIdx == -1:
            self.m_ExtPacketFunc = { }

    
    def AddExtPacket(self, sKey, func):
        self.m_ExtPacketFunc[sKey] = func

    
    def RemoveExtPacket(self, sKey):
        if sKey in self.m_ExtPacketFunc:
            self.m_ExtPacketFunc.pop(sKey)

    
    def NetAddTo(self, dPlayer):
        if not dPlayer:
            return None
        self.MapSendPacket(dPlayer)
        for func in self.m_ExtPacketFunc.values():
            func(self, dPlayer)
        

    
    def ID(self):
        return self.m_ID

    
    def Name(self):
        return self.m_Name

    
    def Shape(self):
        return self.m_Shape

    
    def Type(self):
        return self.m_Type

    
    def Set(self, key, value):
        self.m_Data[key] = value

    
    def SetDefault(self, key, value):
        if key not in self.m_Data:
            self.m_Data[key] = value
            return value
        return self.m_Data[key]

    
    def Add(self, key, value):
        if key in self.m_Data:
            self.m_Data[key] += value
        else:
            self.m_Data[key] = value

    
    def Query(self, key, default = 0):
        if key in self.m_Data:
            return self.m_Data[key]
        return default

    
    def Delete(self, key):
        if key in self.m_Data:
            del self.m_Data[key]

    
    def Save(self):
        return DeepCopy(self.m_SavedData)

    
    def Load(self, dInfo):
        self.m_SavedData = dInfo

    
    def QuerySavedData(self, sArg, default = 0):
        if sArg not in self.m_SavedData:
            return default
        return self.m_SavedData[sArg]

    
    def SetDefaultSavedData(self, sArg, default):
        if sArg not in self.m_SavedData:
            self.m_SavedData[sArg] = default
            return default
        return self.m_SavedData[sArg]

    
    def SetSavedData(self, sArg, val):
        self.m_SavedData[sArg] = val

    
    def DelSavedData(self, sArg):
        if sArg in self.m_SavedData:
            self.m_SavedData.pop(sArg)

    
    def AddSavedData(self, sArg, val):
        if sArg in self.m_SavedData:
            self.m_SavedData[sArg] += val
        else:
            self.m_SavedData[sArg] = val

    
    def SetSide(self, iSide):
        if not iSide:
            return None
        self.m_Side = iSide
        self.m_Game.SetSide(self.m_ID, iSide)
        self.GS2CPropChange('Side', self.m_Side)

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        self.m_ReleaseFlag = 1
        self.m_EvtCtrl.Release()
        self.m_EvtCtrl = None
        if self.m_MoveCtrl:
            self.m_MoveCtrl.Release(self)
            self.m_MoveCtrl = None
        if self.m_FaceCtrl:
            self.m_FaceCtrl.Release()
            self.m_FaceCtrl = None
        self.m_PhyModel = None
        self.ClearAttention()
        self.ClearPacket()
        self.m_Data = { }
        self.m_SavedData = { }

    
    def Remove(self, sReason):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEOBJ, self, {
            'Reason': sReason })
        self.m_Game.m_MiniGameMgr.DeleteOwnerMiniGame(self.m_ID)
        if self.m_Agent:
            self.m_Agent.Release()
            self.m_Agent = None
        if self.m_Scene:
            self.LeaveScene(0)
        self.Release()
        if self.m_Scene:
            super(CSceneObject, self).Remove(sReason)
        else:
            self.RemoveFromList()

    
    def InitToScene(self, tPos):
        import cl_engphyobj
        import cl_movectrl.clientctrl
        import cl_movectrl.crowdctrl
        if self.m_InitScene:
            return None
        self.m_InitScene = 1
        (iPaType, iNavType, iLayer, dParam) = self.GetModelAttr()
        if not iPaType != PAMOD_TYPE_NULL and self.m_PhyModel:
            self.m_PhyModel = cl_engphyobj.CreatePhyModel(self, iPaType, iLayer, dParam)
        if iNavType == NAV_TYPE_OBSTACLE:
            if not self.m_NavObstacle:
                self.m_NavObstacle = ComNavObstacle(self.m_Game.m_ID, self.m_ID, 'NavObstacle')
            self.m_NavObstacle.E_SetModel(dParam['Shape'], dParam)
            if not (cllib.lib_flag.g_IsMobile) and self.m_FightType != WARRIOR_OBSTACLE_NORMAL:
                (bRet, _) = self.m_Game.Scene_FlyGetSpace(self.m_Scene, tPos)
                if bRet:
                    from C_component import ComFlyNavObstacle
                    if not self.m_FlyNavObstacle:
                        self.m_FlyNavObstacle = ComFlyNavObstacle(self.m_Game.m_ID, self.m_ID, 'NavObstacle')
                        self.m_FlyNavObstacle.E_SetModel(dParam['Shape'], dParam)
                    elif iNavType == NAV_TYPE_FLY:
                        import cl_movectrl.flyctrl
                        self.m_MoveCtrl = cl_movectrl.flyctrl.CFlyCtrlMgr(self)
                    elif iNavType == NAV_TYPE_CROWDAGENT and not (self.m_MoveCtrl):
                        if self.m_FightType & WARRIOR_HERO:
                            self.m_MoveCtrl = cl_movectrl.clientctrl.CClientCtrlMgr(self)
                        elif self.m_FightType & (WARRIOR_SERVANT | WARRIOR_DEVICE | WARRIOR_PET):
                            self.m_MoveCtrl = cl_movectrl.crowdctrl.CServantCrowCtrlMgr(self)
                        else:
                            self.m_MoveCtrl = cl_movectrl.crowdctrl.CCrowdCtrlMgr(self)
        if None.m_ModelData:
            self.m_ModelRadius = self.m_ModelData.GetModelRadius()
            self.m_ModelHeight = self.m_ModelData.GetModelHeight()
        self.m_PropType = cl_netattr.GetPropType(self.m_FightType)
        self.OnInitToScene(tPos)

    
    def OnInitToScene(self, tPos):
        pass

    
    def SetCtrlModelData(self):
        dParam = {
            'ObjShape': self.m_Shape,
            'Shape': MODEL_TYPE_CTRLAGENT }
        self.m_ModelData = cl_modeldata.GetModel(dParam)

    
    def GetModelAttr(self):
        (iPaType, iNavType, iLayer) = cl_engobjconf.GetEngineObjConf(self.m_FightType)
        if self.m_ModelData:
            dParam = self.m_ModelData.GetServerData()
        else:
            dParam = { }
        dParam['layer'] = iLayer
        return (iPaType, iNavType, iLayer, dParam)

    
    def IsInPhysx(self):
        (iPaType, _, _) = cl_engobjconf.GetEngineObjConf(self.m_FightType)
        return iPaType != PAMOD_TYPE_NULL

    
    def IsInNav(self):
        (_, iNavType, _) = cl_engobjconf.GetEngineObjConf(self.m_FightType)
        return iNavType != NAV_TYPE_NULL

    
    def IsNeglectAttack(self, oSkill):
        (_, _, iPxLayer) = cl_engobjconf.GetEngineObjConf(self.m_FightType)
        if iPxLayer not in cl_pxlayer.g_PxLayerMap:
            return True
        iPxMask = cl_pxlayer.g_PxLayerMap[iPxLayer][2]
        if iPxMask & cl_pxlayer.PXMASK_SKILLBLK == iPxMask:
            return True
        return False

    
    def MapSendPacket(self, dPlayer):
        pass

    
    def Goto(self, iScene, tPos, tFace = None, tEuler = None, bNotifySceneEnter = True):
        iOldScene = self.m_Scene
        if iOldScene and iScene != iOldScene:
            self.LeaveScene(iScene)
        self.m_Scene = iScene
        if not self.m_InitScene:
            self.InitToScene(tPos)
        if tEuler:
            self.m_Game.SetEuler(self.m_ID, tEuler)
        elif tFace:
            self.SetFacing(tFace, iTurnTime = 0, fSpeed = 360)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            WarobjLog.TraceAlert('noscene %s %s %s' % (self.m_Game.m_ID, self.m_SID, self.m_Scene))
            return None
        oScene.SceneGoto(self, tPos)
        self.RefreshPos()
        if self.m_PlayerID and bNotifySceneEnter:
            cl_scene.GS2CMapSceneEnter(self, iScene, self.GetPos(), self.GetNetFacing())
        self.OnGoto()
        self.EnterScene(iOldScene)

    
    def OnGoto(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        if dPlayer:
            self.NetAddTo(dPlayer)

    
    def SendScenePacket(self):
        iPlayer = self.m_PlayerID
        if iPlayer in self.m_Game.GetRealPlayers():
            for obj in self.m_Game.Scene_GetObjects(self.m_Scene):
                obj.NetAddTo({
                    iPlayer: 1 })
            

    
    def EnterScene(self, iOldScene):
        if iOldScene != self.m_Scene:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            oScene.Enter(self)
            if self.m_Agent:
                self.m_Agent.EnterScene(oScene)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENTERSCENE, self, {
            'OldScene': iOldScene }, iSub = self.m_Side)

    
    def LeaveScene(self, iNewScene):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            oScene.Leave(self)
        self.m_Area = { }
        if self.m_Agent:
            self.m_Agent.LeaveScene()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_LEAVESCENE, self, {
            'NewScene': iNewScene }, iSub = self.m_Side)

    
    def IsStop(self):
        if not self.m_MoveCtrl:
            return 1
        return self.m_MoveCtrl.IsStop(self)

    
    def Stop(self):
        if self.m_MoveCtrl:
            self.m_MoveCtrl.Stop(self)
        self.OnStopMove()

    
    def OnStartMove(self, dInfo):
        pass

    
    def OnStopMove(self):
        pass

    
    def SetPos(self, tPos):
        self.m_Pos = tPos

    
    def GetPos(self):
        return self.m_Pos

    
    def RefreshPos(self):
        self.m_Pos = self.m_Game.GetPosition(self.m_ID)
        return self.m_Pos

    
    def GetPixelPosition(self):
        (x, y, z) = self.m_Pos
        return (int(x * CELL_SPACESIZE), int(y * CELL_SPACESIZE), int(z * CELL_SPACESIZE))

    
    def GetLastPos(self, iFrame):
        return self.m_Game.GetLastPos(self.m_ID, iFrame)

    
    def GetKeyPoint(self):
        vPos = self.GetPos()
        fFixedTopHeight = cl_modeldefine.GetModelDefine(self.m_Shape, 'FixedTopHeight')
        vTopPos = (vPos[0], vPos[1] + self.m_ModelHeight + fFixedTopHeight, vPos[2])
        return [
            vPos,
            vTopPos]

    
    def SetFacing(self, tFace, iTurnTime = 8, fSpeed = 0):
        if self.m_FaceCtrl:
            return self.m_FaceCtrl.FaceDir(self, tFace, 'WorldSet', iTurnTime = iTurnTime, fSpeed = fSpeed)
        self.m_Game.SetFacing(self.m_ID, tFace)
        if self.m_Scene:
            vFace = self.GetNetFacing()
            cl_snetwar.GS2CFace(self.m_Game, self.m_Scene, self.m_ID, vFace, iTurnTime)

    
    def GetFacing(self):
        if self.m_FaceCtrl:
            return self.m_FaceCtrl.GetFacing(self)
        return self.m_Game.GetFacing(self.m_ID)

    
    def GetNetFacing(self):
        (x, y, z) = self.m_Game.GetFacing(self.m_ID)
        return (int(x * 127) + 128, int(y * 127) + 128, int(z * 127) + 128)

    
    def SetEuler(self, tEuler):
        self.m_Game.SetEuler(self.m_ID, tEuler)

    
    def GetEuler(self):
        return self.m_Game.GetEuler(self.m_ID)

    
    def GetDirection(self):
        return self.m_Game.GetDirection(self.m_ID)

    
    def GetCenterPosition(self):
        return self.m_Game.GetCenterPosition(self.m_ID)

    
    def GetPathDir(self):
        if self.m_MoveCtrl:
            return self.m_MoveCtrl.GetPathDir()
        return (0, 0)

    
    def ReceiveAttention(self, iKey):
        self.m_ReceiveAttention.append(iKey)

    
    def ClearAttention(self):
        for iKey in self.m_ReceiveAttention:
            cl_msgcenter.ClearAttention(self.m_Game, self.m_ID, iKey)
        

    
    def GS2CPropChange(self, sAttr, iVal = None):
        if not self.m_InitScene:
            return None
        cl_netattr.GS2CPropChange(self, sAttr, iVal)

    
    def GS2CCachePropChange(self, sAttr, iNew, iAttackPlayer):
        if not self.m_InitScene:
            return None
        if self.m_OwnerPlayerID:
            cl_netattr.GS2CPropChange(self, sAttr, iNew)
        else:
            self.m_Game.CachePropChange(self.m_ID, sAttr, iNew, iAttackPlayer)

    
    def SetSpeed(self, fSpeed):
        self.m_Speed = fSpeed
        self.GS2CPropChange('Speed')
        if self.m_MoveCtrl:
            self.m_MoveCtrl.SetSpeed(self, fSpeed)

    
    def Speed(self):
        return int(self.m_Speed * CELL_SPACESIZE)

    
    def WalkTo(self, tPos, sReason = ''):
        self.m_Game.Scene_Walk(self.m_ID, tPos)
        self.RefreshPos()
        tPos = self.GetPos()
        cl_scene.GS2CMapGoto(self, tPos)

    
    def MoveSpeed(self):
        return self.m_Speed

    
    def SetReleaseFlag(self, iFlag):
        self.m_ReleaseFlag = iFlag

    
    def CanSharedByAI(self, oHero):
        return True



class CEventObject(CObject):
    
    def __init__(self, oGame, nid):
        super(CEventObject, self).__init__(oGame, nid)
        self.m_EvtCtrl = cl_msgcenter.NewEventCtrl()
        self.m_ReceiveAttention = []

    
    def Release(self):
        self.m_EvtCtrl.Release()
        self.m_EvtCtrl = None
        self.ClearAttention()
        self.RemoveFromList()

    
    def ReceiveAttention(self, iKey):
        self.m_ReceiveAttention.append(iKey)

    
    def ClearAttention(self):
        for iKey in self.m_ReceiveAttention:
            cl_msgcenter.ClearAttention(self.m_Game, self.m_ID, iKey)
        



class CGameGlobalTimer(CObject):
    
    def __init__(self, oGame, iObjID):
        super(CGameGlobalTimer, self).__init__(oGame, iObjID)
        self.m_TimerID = cl_timer.g_TimerMgr.CreateTimer()

    
    def Release(self):
        cl_timer.g_TimerMgr.DeleteTimer(self.m_TimerID)
        self.RemoveFromList()

    
    def Logic_Call_Out(self, func, delaytime, flag):
        if delaytime <= 0:
            delaytime = 1
        cl_timer.g_TimerMgr.TimerCall(self.m_TimerID, flag, delaytime, func)

    
    def Logic_Find_Call_Out(self, flag):
        return cl_timer.g_TimerMgr.FindTimer(self.m_TimerID, flag)

    
    def Logic_Remove_Call_Out(self, flag):
        cl_timer.g_TimerMgr.RemoveTimerCall(self.m_TimerID, flag)

    
    def Logic_Remove_All_Call_Out(self):
        cl_timer.g_TimerMgr.ClearTimerCall(self.m_TimerID)



def CreateGlobalTimer(oGame):
    iID = oGame.NewNPCID()
    obj = CGameGlobalTimer(oGame, iID)
    oGame.CreateObject(iID, obj)
    return obj

