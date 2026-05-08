# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_device/mobject.pyc
# RelativePath: clientlogic/cl_device/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_object.logging import DeviceLog
from cl_commondefines import MAIN_DEBUFF, MINOR_DEBUFF, BASEATTR_REFRESH, LEVEL_TYPE_BOSS, MODEL_TYPE_BOX, LINK_QUIT, LINK_DISCONNECT, DEVICE_CONTROL_DEPLOY, DEVICE_CONTROL_RECYCLE, DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_UNACTIVE, WARRIOR_SERVANT, WARRIOR_HERO, DEVICE_CONTROL_FOLLOW, DEVICE_CONTROL_UNFOLLOW, ATTACKERSUBMSG_NORMAL, LINK_ONLINE
from cl_only import Functor, CTRL_FLAG_FOR_ALL, GAME_FRAME, SendAlert, TraceLog
import cl_formula
import cl_warrior
import cl_msgcenter
import cl_netattr
import cl_modeldata
import cl_modeldefine
import cl_facectrl
import cl_forbid
import cl_engphyobj
import cl_math
import cl_snetwar as warnet
import types
import cl_platformdata
import cl_notify

class CDeviceMgr(object):
    
    def __init__(self, oOwner):
        self.m_Game = oOwner.m_Game
        self.m_Owner = oOwner.m_ID
        self.m_Device = 0
        self.m_DeviceSID = 0
        self.m_ReardLayer = { }
        self.m_AddExtComponentPosLayer = []
        self.m_CallFlag = '%d-Device' % oOwner.m_PlayerID
        self.m_Enable = 0

    
    def Release(self):
        self.DoneAttention()
        self.RemoveDevice('Release')
        self.m_Game = None

    
    def Save(self):
        if not self.m_DeviceSID:
            return { }
        dData = {
            'SID': self.m_DeviceSID,
            'DC': self.GetDeviceCompSaveInfo(),
            'RL': dict(self.m_ReardLayer) }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        oDeviceElement = self.m_Game.m_WarMgr.GetComponent('DeviceElement')
        if not oDeviceElement or not (oDeviceElement.m_Enable):
            return None
        oHero = self.GetOwner()
        self.AddDevice(dData['SID'], 'Load')
        self.m_ReardLayer = dData['RL']
        dDeviceCompSaveInfo = dData['DC']
        oHero.m_DevicePerformCon.Load(dDeviceCompSaveInfo)

    
    def Enable(self, dConfig):
        if self.m_Enable:
            return None
        self.m_Enable = 1
        oHero = self.GetOwner()
        iMaxComponentPos = dConfig['MaxComponentPos']
        oHero.m_DevicePerformCon.InitMaxPos(iMaxComponentPos)
        self.m_AddExtComponentPosLayer = dConfig['AddExtComponentPosLayer']
        self.InitAttention()

    
    def ClearAll(self):
        oHero = self.GetOwner()
        oHero.m_DevicePerformCon.ClearAll()
        self.RemoveDevice('ClearAll')
        self.m_DeviceSID = 0

    
    def GetDeviceCompSaveInfo(self):
        oHero = self.GetOwner()
        return oHero.m_DevicePerformCon.Save()

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def AddDevice(self, iDeviceSID, sReason):
        if self.m_DeviceSID:
            return None
        oGame = self.m_Game
        oHero = self.GetOwner()
        clsDeviceData = cl_platformdata.GetDeviceClass(iDeviceSID)
        if not clsDeviceData:
            DeviceLog.Alert('%d %d add device %d %s err' % (oGame.m_ID, oHero.m_PlayerID, iDeviceSID, sReason))
            return None
        DeviceLog.Info('%d %d add device %d %s' % (oGame.m_ID, oHero.m_PlayerID, iDeviceSID, sReason))
        self.m_DeviceSID = clsDeviceData.m_SID
        self.GS2CAddDevice()
        self.InitHeroExtAttr(clsDeviceData)
        self.CreateDevice()
        self.InitPerform(clsDeviceData)
        oHero = self.GetOwner()
        oHero.m_DevicePerformCon.OnAddDevice(sReason)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEVICE_INIT, oHero, {
            'DeviceSID': self.m_DeviceSID,
            'Reason': sReason })

    
    def InitHeroExtAttr(self, clsDeviceData):
        oHero = self.GetOwner()
        iRefreshFlag = BASEATTR_REFRESH
        for sAttr, iVal in clsDeviceData.m_HeroExtAttr.items():
            iVal = cl_formula.GetResultByData(oHero, iVal, { })
            oHero.SetAttr(sAttr, iVal, iRefresh = iRefreshFlag)
            oHero.GS2CPropChange(sAttr)
        
        oHero.DeviceEnergyModify(oHero.QueryAttr('MaxDeviceEnergy'))
        oHero.UpdateDeviceEnergyRecoverStatus()

    
    def InitPerform(self, clsDeviceData):
        oHero = self.GetOwner()
        oPerformCon = oHero.m_DevicePerformCon
        for iPerformSID in clsDeviceData.m_HeroPerformInfo.values():
            oPerformCon.AddPerform(oHero, iPerformSID, 1, iEnable = 1, iItem = 0)
        
        for iPerformSID in clsDeviceData.m_HeroExtPassive:
            oPerformCon.AddPerform(oHero, iPerformSID, 1, iEnable = 1, iItem = 0)
        

    
    def InitAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnHeroDieDist, sFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnLinkStatusChange, sFlag, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, sFlag)

    
    def DoneAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIEDIST, sFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, sFlag)
        cl_msgcenter.DoneAttention(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, sFlag)
        cl_msgcenter.DoneAttention(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, sFlag)

    
    def Refresh(self, dPlayer = None):
        if not self.m_Device:
            return None
        self.GS2CAddDevice(dPlayer)

    
    def SelfRefresh(self):
        oHero = self.GetOwner()
        if not oHero or not (oHero.m_DevicePerformCon):
            return None
        oHero.m_DevicePerformCon.Refresh()

    
    def GS2CAddDevice(self, dPlayer = None):
        if not self.m_DeviceSID:
            return None
        oHero = self.GetOwner()
        if not dPlayer:
            dPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        warnet.GS2CAddDevice(self.m_Game, oHero.m_ID, self.m_DeviceSID, dPlayer)

    
    def OnHeroDieDist(self, oHero, dMsgInfo):
        oDevice = self.GetDevice()
        if not oDevice:
            return None
        if oDevice.DeployStatus():
            oDevice.Recycle()

    
    def OnLinkStatusChange(self, oHero, dMsgInfo):
        if oHero.Online() in (LINK_QUIT, LINK_DISCONNECT):
            self.RecycleDevice()

    
    def CreateDevice(self):
        if not self.m_DeviceSID:
            return None
        if self.m_Device:
            return self.m_Game.GetObject(self.m_Device)
        oHero = self.GetOwner()
        oDevice = self.m_Game.m_ResMgr.CreateDevice(oHero, self.m_DeviceSID, { })
        if oDevice:
            self.m_Device = oDevice.m_ID
        return oDevice

    
    def RemoveDevice(self, sReason):
        oDevice = self.GetDevice()
        if not oDevice:
            return None
        oDevice.Remove(sReason)
        self.m_Device = 0

    
    def GetDevice(self):
        if not self.m_Device:
            return None
        return self.m_Game.GetObject(self.m_Device)

    
    def CheckDeciveStatus(self, iDeployed, iAcitve):
        oDevice = self.GetDevice()
        if not oDevice:
            return False
        if oDevice.DeployStatus() == iDeployed:
            pass
        return oDevice.ActiveStatus() == iAcitve

    
    def DeployDevice(self, iScene, vPos, vFace, dInfo):
        oDevice = self.GetDevice()
        if not oDevice or oDevice.DeployStatus():
            return None
        oDevice.Deploy(iScene, vPos, vFace, dInfo)

    
    def RecycleDevice(self):
        oDevice = self.GetDevice()
        if not oDevice or not oDevice.DeployStatus():
            return None
        oDevice.Recycle()

    
    def SetDeciveActiveStatus(self, iActive):
        oDevice = self.GetDevice()
        if not oDevice or iActive == oDevice.ActiveStatus():
            return None
        iStatus = 1 if iActive else 0
        oDevice.SetActiveStatus(iStatus)

    
    def OnLevelNodeInit(self, oHero, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            cl_msgcenter.AddAttentionFunc(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOK, self.m_CallFlag)

    
    def ValidAddComponentMaxPos(self, iLayer, iLevelType):
        if iLayer in self.m_ReardLayer:
            return False
        if iLayer not in self.m_AddExtComponentPosLayer:
            return False
        if iLevelType != LEVEL_TYPE_BOSS:
            return False
        return True

    
    def OnLevelNodeGoalOK(self, oHero, oWarMgr, dMsgInfo):
        cl_msgcenter.DoneAttention(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        iLayer = dMsgInfo['Layer']
        if self.ValidAddComponentMaxPos(iLayer, dMsgInfo['LevelType']):
            self.m_ReardLayer[iLayer] = 1
            oHero = self.GetOwner()
            oHero.m_DevicePerformCon.AddMaxPos(1)

    
    def NeedCreateSeed(self):
        return 1

    
    def AllPerformDisable(self, iNotify = 0):
        pass

    
    def GetPerform(self, iPerform, iItem = 0):
        oHero = self.GetOwner()
        if not oHero or not (oHero.m_DevicePerformCon):
            return None
        return oHero.m_DevicePerformCon.GetPerform(iPerform)

    
    def GetItemByID(self, iItem):
        pass



class CDevice(cl_warrior.CWarrior):
    m_ActiveDisablePerform = ()
    m_ActiveStopEnergyRecover = 0
    
    def InitDevice(self, dAddData):
        self.m_DeployStatus = 0
        self.m_ActiveStatus = 0
        self.InitWarValue()
        oOwner = self.GetOwner()
        self.InitAttention()
        oScene = self.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if oScene:
            self.Goto(oOwner.m_Scene, (0, 0, 0))
        self.OnInitDevice(dAddData)

    
    def OnInitDevice(self, dAddData):
        pass

    
    def OnInitToScene(self, tPos):
        super().OnInitToScene(tPos)
        self.SwitchPhyAbleAndNavAble(iEnable = 0)

    
    def Release(self):
        self.DoneAttention()
        super().Release()

    
    def SetOwner(self, oOwner):
        self.m_Owner = oOwner.m_ID
        self.m_OwnerPlayerID = oOwner.m_PlayerID

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def InitAttention(self):
        iOwner = self.m_Owner
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_RECEIVEDAM), 'OnReceiveDam', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_KILL, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_KILL), 'OnKill', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PERFORM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_PERFORM), 'OnPerformDamage', iSub = self.m_SubAttackMsg, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF), 'OnCauseDebuff', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MINOR_DEBUFF), 'OnCauseMinorDebuff', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1), 'OnCausedFinalDebuff', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, 'OnDealTotalDam', iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, iOwner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnHeroEnterScene, 'OnHeroEnterScene')
        cl_msgcenter.AddAttentionFunc(self, iOwner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnHeroLeaveScene, 'OnHeroLeaveScene')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, self.OnHeroEnterRoom, 'OnHeroChangeRoomPos')

    
    def DoneAttention(self):
        iOwner = self.m_Owner
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'OnReceiveDam')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_KILL, 'OnKill')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PERFORM, 'OnPerformDamage')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseDebuff', iSub = MAIN_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseMinorDebuff', iSub = MINOR_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, 'OnCausedFinalDebuff')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'OnDealTotalDam')
        cl_msgcenter.DoneAttention(self, iOwner, cl_msgcenter.MSG_WAR_ADDTALENT, 'OwnerAddTalent')
        cl_msgcenter.DoneAttention(self, iOwner, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, 'OwnerRemoveTalent')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, 'OnHeroChangeRoomPos')
        cl_msgcenter.DoneAttention(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'OnLevelNodeInit')

    
    def OnDealTotalDam(self, oListener, dMsgInfo):
        oGame = self.m_Game
        iAttack = self.m_Owner
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return None
        oVictim = oGame.GetObject(dMsgInfo['CurVID'])
        if not oVictim:
            return None
        iCurFrame = oGame.GetFrameNum()
        oVictim.Set('Injured%d' % iAttack, iCurFrame)
        dInfo = { }
        dInfo.update(dMsgInfo)
        dInfo['OriginalAID'] = dInfo['AID']
        dInfo['AID'] = iAttack
        iSubAttackMsg = oVictim.m_SubAttackMsg
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEALTOTALDAM, oAttack, dInfo, iSub = iSubAttackMsg, oGame = oGame)

    
    def OnHeroEnterScene(self, oListener, oHero, dMsgInfo):
        self.Goto(oHero.m_Scene, self.GetPos())

    
    def OnHeroLeaveScene(self, oListener, oHero, dMsgInfo):
        if self.m_DeployStatus:
            self.Recycle()
        iNewScene = dMsgInfo['NewScene'] if 'NewScene' in dMsgInfo else 0
        self.LeaveScene(iNewScene)

    
    def OnHeroEnterRoom(self, oListener, oLevelCtrl, dMsgInfo):
        oVictim = self.m_Game.GetObject(dMsgInfo['VID'])
        if not oVictim.m_FightType & WARRIOR_HERO:
            return None
        iScene = dMsgInfo['Scene']
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        iLevel = oScene.m_Level
        oCurLevelNode = oLevelCtrl.m_CurNode
        if iLevel != oCurLevelNode.m_Level:
            return None
        iRoomPos = dMsgInfo['RoomPos']
        if not (self.m_LineIdx) or self.m_LineIdx[0] != iLevel or self.m_LineIdx[1] != iRoomPos:
            self.m_LineIdx = (iLevel, iRoomPos, 0)
            self.OnHeroChangeRoomPos()

    
    def OnHeroChangeRoomPos(self):
        if self.m_DeployStatus:
            self.Recycle()

    
    def OnUpdateEnableDeviceComp(self):
        if self.m_DeployStatus:
            self.Recycle()
            cl_notify.SendCommonNotify(self.m_Game, [
                self.m_OwnerPlayerID], 9474, { })

    
    def LockEnemy(self):
        return self.Query('LockEnemy', 0)

    
    def SetLockEnemy(self, iTarget):
        self.Set('LockEnemy', iTarget)
        self.GS2CPropChange('LockEnemy', iTarget)

    
    def DeployStatus(self):
        return self.m_DeployStatus

    
    def ActiveStatus(self):
        return self.m_ActiveStatus

    
    def SetActiveStatus(self, iActive):
        if iActive == self.m_ActiveStatus:
            return None
        self.m_ActiveStatus = iActive
        iSubMsg = DEVICE_CONTROL_ACTIVE if iActive else DEVICE_CONTROL_UNACTIVE
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTROL_DEVICE, oOwner, { }, iSub = iSubMsg)
        self.GS2CPropChange('ActiveStatus', iActive)
        self.OnActiveStatusChange()

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeDeviceAddPacket(self, dPlayer)

    
    def Deploy(self, iScene, vPos, vFace, dInfo):
        self.Goto(iScene, vPos, vFace)
        self.m_DeployStatus = 1
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTROL_DEVICE, oOwner, { }, iSub = DEVICE_CONTROL_DEPLOY)
        self.GS2CPropChange('DeployStatus', 1)
        oHero = self.GetOwner()
        oHero.m_DevicePerformCon.OnDeployDevice()
        self.OnDeploy(dInfo)

    
    def OnDeploy(self, dInfo):
        self.SwitchPhyAbleAndNavAble(iEnable = 1)

    
    def Recycle(self):
        self.m_DeployStatus = 0
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTROL_DEVICE, oOwner, { }, iSub = DEVICE_CONTROL_RECYCLE)
        self.GS2CPropChange('DeployStatus', 0)
        oHero = self.GetOwner()
        oHero.m_DevicePerformCon.OnRecycleDevice()
        self.OnRecycle()

    
    def OnRecycle(self):
        self.SwitchPhyAbleAndNavAble(iEnable = 0)

    
    def SwitchPhyAbleAndNavAble(self, iEnable):
        if iEnable:
            if self.m_PhyModel:
                self.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 1)
            if self.m_MoveCtrl:
                self.UnForbid(cl_forbid.NAVSEEK_RULE, 'DeviceSwitch')
                self.m_MoveCtrl.E_Enable()
            elif self.m_PhyModel:
                self.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 0)
        if None.m_MoveCtrl:
            self.Forbid(cl_forbid.NAVSEEK_RULE, 'DeviceSwitch')
            self.m_MoveCtrl.E_Disable()

    
    def LeaveScene(self, iNewScene):
        super().LeaveScene(iNewScene)
        self.m_Game.m_SkillMgr.AttackLeaveScene(self.m_ID)
        if self.m_Scene:
            self.RemoveFromScene()

    
    def EnterScene(self, iOldScene):
        super().EnterScene(iOldScene)
        if iOldScene != self.m_Scene:
            self.GS2CPropChange('Scene', self.m_Scene)

    
    def OnActiveStatusChange(self):
        oHero = self.GetOwner()
        if self.m_ActiveStopEnergyRecover and not (oHero.m_ReleaseFlag):
            if self.m_ActiveStatus:
                oHero.StopDeviceEnergyRecover('DeviceActive')
            else:
                oHero.StartDeviceEnergyRecover('DeviceActive')
        if not self.m_ActiveDisablePerform:
            return None
        oPerformCon = oHero.m_DevicePerformCon
        for iPerform in self.m_ActiveDisablePerform:
            oPerform = oPerformCon.GetPerform(iPerform)
            if not oPerform:
                continue
            if self.m_ActiveStatus:
                oPerform.Disable(oHero, iNotify = 0)
                continue
            oPerform.Enable(oHero)
        

    
    def HPModifyDam(self, iAttack, lstChange):
        if self.CheckDamTraceCD():
            sText = f'''device hpmodifydam {self.m_SID}'''
            SendAlert('err', sText)
            TraceLog('err', sText)
        return ([
            0,
            0,
            0], [], [])

    
    def Die(self, iAttack, oReason):
        sText = f'''device die {self.m_SID} {oReason}'''
        SendAlert('err', sText)
        TraceLog('err', sText)



class CPoisonDevice(CDevice):
    m_AttachPart = 0
    m_AttachTarget = 0
    m_UnAutoRecycleFightType = WARRIOR_HERO | WARRIOR_SERVANT
    
    def OnDeploy(self, dInfo):
        self.m_AttachTarget = dInfo['Victim'] if 'Victim' in dInfo else 0
        self.m_AttachPart = dInfo['AttachPart'] if 'AttachPart' in dInfo else 0
        self.GS2CPropChange('AttachTarget', self.m_AttachTarget)
        self.GS2CPropChange('AttachPart', self.m_AttachPart)
        if not self.m_AttachTarget:
            return None
        iTarget = self.m_AttachTarget
        cl_msgcenter.AddAttentionFunc(self, iTarget, cl_msgcenter.MSG_WAR_DIE, DeviceDrop, 'VictimDie')
        cl_msgcenter.AddAttentionFunc(self, iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, DeviceDrop, 'VictimRemoveObject')
        cl_msgcenter.AddAttentionFunc(self, iTarget, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnVictimEnterScene, 'VictimEnterScene')
        cl_msgcenter.AddAttentionFunc(self, iTarget, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnVictimLeaveScene, 'VictimLeaveScene')

    
    def OnRecycle(self):
        self.SetActiveStatus(0)
        if self.m_AttachTarget:
            self.ResetAttachTarget()
        oHero = self.GetOwner()
        if self.m_Scene != oHero.m_Scene:
            self.Goto(oHero.m_Scene, oHero.GetPos())

    
    def OnHeroLeaveScene(self, oListener, oHero, dMsgInfo):
        if self.m_AttachTarget:
            oTarget = self.m_Game.GetObject(self.m_AttachTarget)
            if oTarget and oTarget.m_FightType & self.m_UnAutoRecycleFightType:
                self.SetActiveStatus(0)
                return None
        super().OnHeroLeaveScene(oListener, oHero, dMsgInfo)

    
    def OnHeroEnterScene(self, oListener, oHero, dMsgInfo):
        if not self.m_AttachTarget:
            super().OnHeroEnterScene(oListener, oHero, dMsgInfo)
        if self.m_DeployStatus and oHero.m_Scene == self.m_Scene:
            self.SetActiveStatus(1)

    
    def OnVictimLeaveScene(self, oListener, oTarget, dMsgInfo):
        if oTarget.m_FightType & self.m_UnAutoRecycleFightType:
            iNewScene = dMsgInfo['NewScene'] if 'NewScene' in dMsgInfo else 0
            self.LeaveScene(iNewScene)
        else:
            self.Recycle()

    
    def OnVictimEnterScene(self, oListener, oTarget, dMsgInfo):
        self.Goto(oTarget.m_Scene, self.GetPos())

    
    def OnHeroChangeRoomPos(self):
        if self.m_DeployStatus and not (self.m_AttachTarget):
            self.Recycle()

    
    def LeaveScene(self, iNewScene):
        super().LeaveScene(iNewScene)
        if self.m_DeployStatus:
            self.SetActiveStatus(0)

    
    def EnterScene(self, iOldScene):
        super().EnterScene(iOldScene)
        if self.m_DeployStatus:
            oHero = self.GetOwner()
            if oHero.m_Scene == self.m_Scene:
                self.SetActiveStatus(1)

    
    def ResetAttachTarget(self):
        iTarget = self.m_AttachTarget
        self.m_AttachTarget = 0
        self.m_AttachPart = 0
        self.GS2CPropChange('AttachTarget', 0)
        self.GS2CPropChange('AttachPart', 0)
        cl_msgcenter.DoneAttention(self, iTarget, cl_msgcenter.MSG_WAR_DIE, 'VictimDie')
        cl_msgcenter.DoneAttention(self, iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, 'VictimRemoveObject')
        cl_msgcenter.DoneAttention(self, iTarget, cl_msgcenter.MSG_WAR_ENTERSCENE, 'VictimEnterScene')
        cl_msgcenter.DoneAttention(self, iTarget, cl_msgcenter.MSG_WAR_LEAVESCENE, 'VictimLeaveScene')



class CTurretDevice(CDevice):
    m_Phase = 1
    m_BaseHate = { }
    m_HateDisEff = { }
    
    def InitAttention(self):
        super().InitAttention()
        iHero = self.m_Owner
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, 'OnAttack', iSub = ATTACKERSUBMSG_NORMAL, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_ATTACKPF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL), 'OnAttackPF', iSub = ATTACKERSUBMSG_NORMAL, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnHeroRelife, 'OnHeroRelife')
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnPlayerLinkStatus, 'OnPlayerLinkStatus')

    
    def DoneAttention(self):
        super().DoneAttention()
        iHero = self.m_Owner
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_ATTACK, 'OnAttack', iSub = ATTACKERSUBMSG_NORMAL)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_ATTACKPF, 'OnAttackPF', iSub = ATTACKERSUBMSG_NORMAL)
        cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, 'OnHeroRelife')
        cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, 'OnPlayerLinkStatus')

    
    def SetPhase(self, iPhase):
        if iPhase == self.m_Phase:
            return None
        iOldPhase = self.m_Phase
        self.m_Phase = iPhase
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SWITCH_PHASE, self, {
            'OldPhase': iOldPhase,
            'NewPhase': iPhase })
        self.GS2CPropChange('Phase')

    
    def OnInitDevice(self, dAddData):
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)
        oAgent = self.m_Agent
        if oAgent:
            oAgent.PauseAgent('Recycle')
        self.AutoDeploy()

    
    def AutoDeploy(self):
        oOwner = self.GetOwner()
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        vPos = self.GetBronPos()
        self.SwitchFollowMoveStatus(iStatus = 1)
        self.Deploy(iScene, vPos, oOwner.GetFacing(), { })

    
    def OnDeploy(self, dInfo):
        super().OnDeploy(dInfo)
        oAgent = self.m_Agent
        if oAgent:
            oAgent.ResumeAgent('Recycle')

    
    def OnRecycle(self):
        super().OnRecycle()
        oAgent = self.m_Agent
        if oAgent:
            oAgent.StopMoving(oAgent)
            oAgent.PauseAgent('Recycle')

    
    def OnHeroEnterScene(self, oListener, oHero, dMsgInfo):
        if self.m_DeployStatus:
            self.Remove_Call_Out('DelayEnterScene')
            self.Call_Out(self.GotoBornPos, GAME_FRAME, 'DelayEnterScene')
        elif oHero.IsRealDied():
            self.Goto(oHero.m_Scene, self.GetPos())
        else:
            self.AutoDeploy()

    
    def GotoBornPos(self):
        oOwner = self.GetOwner()
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        tPos = self.GetBronPos()
        if iScene == self.m_Scene:
            self.WalkTo(tPos)
        else:
            self.Goto(iScene, tPos)
        if self.Query('AutoFollow', 1):
            self.SwitchFollowMoveStatus(iStatus = 1)

    
    def GetBronPos(self):
        oOwner = self.GetOwner()
        tOwnerPos = oOwner.GetPos()
        iScene = oOwner.m_Scene
        if not iScene:
            return tOwnerPos
        tInfo = self.Query('BronPosInfo', None)
        if not tInfo:
            DeviceLog.Alert('%d %d turretdevice%s not bronposinfo' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID))
            return tOwnerPos
        (fMinRadius, fMaxRadius, iMinAngle, iMaxAngle) = tInfo
        tDir = oOwner.GetFacing()
        tPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, tOwnerPos, tDir, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle)
        if not tPos:
            for _ in range(5):
                fMaxRadius += 1
                tPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, tOwnerPos, tDir, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle)
                if tPos:
                    break
            else:
                (ret, tPos) = self.m_Game.Scene_GetSpace(iScene, tOwnerPos)
                if not ret:
                    tPos = tOwnerPos
        return tPos

    
    def WalkTo(self, vPos, sReason = ''):
        self.m_MoveCtrl.StopJump()
        super().WalkTo(vPos, sReason)

    
    def OnHeroLeaveScene(self, oListener, oHero, dMsgInfo):
        iNewScene = dMsgInfo['NewScene'] if 'NewScene' in dMsgInfo else 0
        self.LeaveScene(iNewScene)

    
    def OnHeroChangeRoomPos(self):
        if self.m_DeployStatus:
            self.GotoBornPos()

    
    def OnAttack(self, oListener, dMsgInfo):
        oHero = self.GetOwner()
        dInfo = { }
        dInfo.update(dMsgInfo)
        dInfo['AID'] = oHero.m_ID
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTACK, oHero, dInfo, iSub = ATTACKERSUBMSG_NORMAL)
        dMsgInfo['LuckyHit'] = dInfo['LuckyHit']

    
    def OnHeroRelife(self, oListener, oHero, dMsgInfo):
        self.AutoDeploy()

    
    def OnPlayerLinkStatus(self, oListener, oHero, dMsgInfo):
        if oHero.Online() == LINK_ONLINE:
            self.AutoDeploy()

    
    def OnUpdateEnableDeviceComp(self):
        pass

    
    def MixPFAttrCache(self, dAttrCache):
        if 'DebuffProb' in self.m_PrivateAttr:
            oDebuffProb = self.m_PrivateAttr['DebuffProb']
            dAttrCache['DebuffProb'] = oDebuffProb.GetValue(self)
        return super().MixPFAttrCache(dAttrCache)

    
    def SwitchFollowMoveStatus(self, iStatus):
        oAgent = self.m_Agent
        if oAgent:
            iStatus = 1 if iStatus else 0
            if iStatus == oAgent.GetData('FollowMoveStatus'):
                return None
            oAgent.SetData('FollowMoveStatus', iStatus)
            iSubMsg = DEVICE_CONTROL_FOLLOW if iStatus else DEVICE_CONTROL_UNFOLLOW
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTROL_DEVICE, self.GetOwner(), { }, iSub = iSubMsg)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)



class CBarrierDevice(CDevice):
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_ModelScale = (100, 100, 100)
        self.m_Phase = 0
        self.SetAttr('AttBuff', 0, 0)
        self.SetAttr('SubSpeed', 0, 0)
        self.m_Facing = None

    
    def OnInitDevice(self, dAddData):
        self.ClearSkillCheckArgs()
        self.SetPosFuncBinding()

    
    def OnInitToScene(self, tPos):
        self.SwitchPhyAbleAndNavAble(iEnable = 0)

    
    def IsNeglectAttack(self, oSkill):
        if not self.m_DeployStatus:
            return True
        return super().IsNeglectAttack(oSkill)

    
    def ClearSkillCheckArgs(self):
        iRadius = self.m_ModelData.GetModelRadius()
        iHeight = self.m_ModelData.GetModelHeight()
        self.SkillCheckArgs = (iRadius, iHeight)

    
    def Deploy(self, iScene, vPos, vFace, dInfo):
        self.ClearPosFuncBinding()
        super().Deploy(iScene, vPos, vFace, dInfo)

    
    def Release(self):
        super().Release()
        self.ClearPosFuncBinding()

    
    def Goto(self, iScene, tPos, tFace = None, tEuler = None):
        if not tEuler and tFace:
            self.m_Facing = tFace
            tEuler = cl_math.Dir2Radians(tFace)
            tFace = None
        return super().Goto(iScene, tPos, tFace, tEuler)

    
    def GetNetFacing(self):
        (x, y, z) = self.m_Facing if self.m_Facing else self.m_Game.GetFacing(self.m_ID)
        return (int(x * 127) + 128, int(y * 127) + 128, int(z * 127) + 128)

    
    def SetPosFuncBinding(self):
        self.GetPos = types.MethodType(GetOwnerPos, self)
        self.GetFacing = types.MethodType(GetOwnerFacing, self)
        self.GetLastPos = types.MethodType(GetOwnerLastPos, self)

    
    def ClearPosFuncBinding(self):
        if 'GetPos' in self.__dict__:
            del self.GetPos
        if 'GetFacing' in self.__dict__:
            del self.GetFacing
        if 'GetLastPos' in self.__dict__:
            del self.GetLastPos

    
    def OnRecycle(self):
        self.SetPosFuncBinding()

    
    def GetBuffData(self):
        return {
            'Att': self.QueryAttr('AttBuff') }

    
    def SetBaseFactor(self, dInfo):
        iBaseAtt = dInfo['AttBuff'] if 'AttBuff' in dInfo else 20
        self.SetAttr('AttBuff', iBaseAtt, 0)
        iBaseSubSpeed = dInfo['SubSpeed'] if 'SubSpeed' in dInfo else 6000
        self.SetAttr('SubSpeed', iBaseSubSpeed, 0)

    
    def SetModelScale(self, iWidthScale, iHeightScale):
        tScale = (iWidthScale, iHeightScale, 100)
        if tScale == self.m_ModelScale:
            return None
        self.m_ModelScale = tScale
        self.GS2CPropChange('ModelScale', tScale)
        self.SetCtrlModelData()
        self.ClearSkillCheckArgs()
        if self.m_PhyModel:
            (iPaType, iNavType, iLayer, dParam) = self.GetModelAttr()
            self.m_PhyModel.E_Unstall()
            self.m_PhyModel = cl_engphyobj.CreatePhyModel(self, iPaType, iLayer, dParam)

    
    def SetCtrlModelData(self):
        tBox = cl_modeldefine.GetModelDefine(self.m_Shape, 'Box')
        dParam = {
            'Shape': MODEL_TYPE_BOX,
            'Angle': (0, 0, 0),
            'Center': (0, tBox[1] * 0.5, 0),
            'Scale': cl_math.Vec3MulF(self.m_ModelScale, 0.01),
            'Size': tBox }
        self.m_ModelData = cl_modeldata.GetModel(dParam)
        self.m_ModelRadius = self.m_ModelData.GetModelRadius()
        self.m_ModelHeight = self.m_ModelData.GetModelHeight()

    
    def SwitchPhyAbleAndNavAble(self, iEnable):
        if iEnable and self.m_DeployStatus and not (self.m_PhyModel):
            (iPaType, iNavType, iLayer, dParam) = self.GetModelAttr()
            self.m_PhyModel = cl_engphyobj.CreatePhyModel(self, iPaType, iLayer, dParam)
        elif not iEnable and self.m_PhyModel:
            self.m_PhyModel.E_Unstall()
            self.m_PhyModel = None

    
    def OnActiveStatusChange(self):
        self.SwitchPhyAbleAndNavAble(self.m_ActiveStatus)
        super().OnActiveStatusChange()

    
    def OnContact(self, iTarget, dArgs):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_COLLIDED, oOwner, {
                'AID': self.m_Owner,
                'VID': iTarget,
                'dArgs': dArgs })



def GetOwnerPos(oDevice):
    oOwner = oDevice.GetOwner()
    return oOwner.GetPos()


def GetOwnerFacing(oDevice):
    oOwner = oDevice.GetOwner()
    return oOwner.GetFacing()


def GetOwnerLastPos(oDevice, iFrame):
    oOwner = oDevice.GetOwner()
    return oOwner.GetLastPos(iFrame)


def SendOwnerMsg(iMsg, iSub, oDevice, dMsgInfo):
    oOwner = oDevice.GetOwner()
    if oOwner:
        dInfo = { }
        dInfo.update(dMsgInfo)
        dInfo['AID'] = oOwner.m_ID
        cl_msgcenter.SendMsg(iMsg, oOwner, dInfo, iSub = iSub)


def SendOwnerMsgByVictimSub(iMsg, oDevice, dMsgInfo):
    if 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    else:
        return None
    oGame = oDevice.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAttack = oDevice.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(iMsg, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)


def DeviceDrop(oDevice, oWarrior, dMsgInfo):
    oHero = oDevice.GetOwner()
    if oHero.m_Scene != oWarrior.m_Scene:
        oDevice.Recycle()
        return None
    oDevice.ResetAttachTarget()

