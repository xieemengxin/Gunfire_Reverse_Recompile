# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_build/mobject.pyc
# RelativePath: clientlogic/cl_build/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_BUILD, WARRIOR_STONEPILLAR, WARRIOR_PROTEGE_NORMAL, MODEL_TYPE_BOX, WARRIOR_AIRWALL_PHY, INTERACT_STATUS_DONE, WARRIOR_BUILD, INTERACT_TYPE_ALLOW, INTERACT_STATUS_PEND, STATE_CLS_ABNORMAL, INTERACT_TYPE_FORBID, BUILD_DEFENDNPC, WARRIOR_SUMMON_STELE, MODEL_TYPE_SPHERE, WARRIOR_HERO, STATE_TIME_FOREVER, WARRIOR_ELITE, STATE_WUDI, STATE_SUMMONSTELE_HPDECREASE, CBEHAVIOR_SUMMONSTELE_SHOWHP, ATTACKERSUBMSG_NORMAL, WARRIOR_DEVICE, WARRIOR_MONSTERBUILD, WARRIOR_GEYSER, WARRIOR_MONSTERHINDER, WARRIOR_MONSTENOPHYRHINDER, STATE_MONSTER_HINDER, WARRIOR_MOVEBUILD, MOVE_BUILD_LINE, MOVE_BUILD_COMEANDGO
from cl_only import PY_FLAG_IGNORESCENEEVT, Functor, SendAlert, TraceLog, ChooseRange, ChooseKey, Time2Frame, Second2Frame, Frame2Time, DEAD_FLAG_DIED
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_OBJECT, PXLAYER_DEVENT, PXMASK_STATIC, PXMASK_IMPENETRABLE
from cl_object.logging import SeasonLog, OtherLog
from . import net
import math
import cl_state
import cl_warrior
import cl_msgcenter
import cl_netattr
import cl_math
import cl_scene
import cl_notify
import cl_engphyobj
import cl_object.reason
import cl_war
import cl_snetwar
import cl_modeldefine

class CBuild(cl_warrior.CWarrior):
    m_Type = 'Build'
    m_FightType = WARRIOR_BUILD
    m_RemoveDelay = 1
    m_Delete = 1
    m_Reward = None
    m_Prefab = 0
    m_SmashFunc = None
    m_InteractFunc = None
    m_SmashReserveGroup = { }
    m_LimitDam = 0
    m_ValidShowTips = 0
    m_SubAttackMsg = ATTACKERSUBMSG_BUILD
    m_ClassifyList = ()
    m_CheckInteractDistance = False
    m_InteractDis = 5
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_ClientGlobalArea = 0
        self.m_PendRemove = False
        self.m_PlayerInteractStatus = { }
        self.m_PlayerInteractType = { }
        self.SetInitInteract(INTERACT_TYPE_FORBID)

    
    def InitBuild(self, clsData, dAddData):
        clsData.InitBuildData(self, dAddData)
        self.OnInitBuild(clsData, dAddData)
        self.InitWarValue()
        self.AddMaxAttr('IgnoreST%d' % STATE_CLS_ABNORMAL, 'OBSTACLE', 99, 9999999)

    
    def OnInitBuild(self, clsData, dAddData):
        pass

    
    def SetFacing(self, tFace):
        pass

    
    def OnInitToScene(self, tPos):
        super(CBuild, self).OnInitToScene(tPos)
        self.m_Game.SetPyFlag(self.m_ID, PY_FLAG_IGNORESCENEEVT, 1)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIE, self.OnBuildDie, 'ObstacleReward')

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeBuildAddPacket(self, dPlayer)

    
    def GetLastPos(self, iFrame):
        return self.GetPos()

    
    def Shield(self):
        return 0

    
    def RShield(self):
        return 0

    
    def HP(self):
        if self.IsDead():
            return 0
        return self.m_HP

    
    def OnBuildDie(self, oOwner, dMsgInfo):
        iAttack = dMsgInfo['AID']
        oKiller = self.m_Game.GetObject(iAttack)
        if oKiller and oKiller.m_Owner:
            oKiller = self.m_Game.GetObject(oKiller.m_Owner)
        func = self.m_SmashFunc
        self.m_SmashFunc = None
        if func:
            func(self, oKiller)

    
    def DirectRemove(self, sReason):
        self.m_PendRemove = True
        iDelay = max(1, self.m_RemoveDelay)
        self.Call_Out(Functor(self.Remove, sReason), iDelay, 'DirectRemove')

    
    def SetInitInteract(self, iType):
        oWarMgr = self.m_Game.m_WarMgr
        for pid in oWarMgr.GetAllPlayer():
            self.m_PlayerInteractStatus[pid] = INTERACT_STATUS_PEND
            self.m_PlayerInteractType[pid] = iType
        

    
    def ValidInteract(self, oHero):
        if self.m_Scene != oHero.m_Scene:
            return False
        if self.m_CheckInteractDistance and not cl_math.CheckDistance3D(oHero.GetPos(), self.GetPos(), self.m_InteractDis):
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, 'NPC距离过远')
            return False
        iStatus = self.m_PlayerInteractType[oHero.m_PlayerID]
        if iStatus & INTERACT_TYPE_ALLOW != INTERACT_TYPE_ALLOW:
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, 'NPC不可交互')
            return False
        return True

    
    def Interact(self, oHero):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.OnInteract(oHero)
        self.SetHeroInteractStatus(pid)
        iInteractType = self.m_PlayerInteractType[pid]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BUILD_INTERACT, self, {
            'pid': oHero.m_PlayerID,
            'Hero': oHero.m_ID,
            'Type': iInteractType,
            'Build': self.m_ID })
        if self.m_InteractFunc:
            self.m_InteractFunc(self, oHero)

    
    def OnInteract(self, oHero):
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
            oHero.m_PlayerID])

    
    def StopInteract(self, oHero):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BUILD_STOP_INTERACT, self, {
            'Hero': oHero.m_ID })
        self.OnStopInteract(oHero)

    
    def OnStopInteract(self, oHero):
        pass

    
    def GetHeroInteractStatus(self, pid):
        if pid not in self.m_PlayerInteractStatus:
            return 0
        return self.m_PlayerInteractStatus[pid]

    
    def SetHeroInteractStatus(self, pid, iNotify = 1):
        if self.m_PlayerInteractStatus[pid] == INTERACT_STATUS_DONE:
            return None
        self.m_PlayerInteractStatus[pid] = INTERACT_STATUS_DONE
        if iNotify:
            self.NotifyInteractInfo(pid)

    
    def GetPlayerInteractType(self, pid):
        if pid not in self.m_PlayerInteractType:
            return 0
        return self.m_PlayerInteractType[pid]

    
    def SetPlayerInteractType(self, iInteractType, lstPlayer):
        if iInteractType not in (INTERACT_TYPE_FORBID, INTERACT_TYPE_ALLOW):
            return None
        for pid in lstPlayer:
            iOldType = self.m_PlayerInteractType.get(pid, -1)
            if iOldType == iInteractType:
                continue
            self.m_PlayerInteractType[pid] = iInteractType
            self.NotifyInteractInfo(pid)
        

    
    def NotifyInteractInfo(self, pid):
        iType = self.m_PlayerInteractType[pid]
        iStatus = self.m_PlayerInteractStatus[pid]
        net.GS2CBuildInteractState(pid, self.m_ID, iStatus | iType)

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        for iPlayer in dPlayer:
            iStatus = self.GetHeroInteractStatus(iPlayer)
            iType = self.GetPlayerInteractType(iPlayer)
            net.GS2CBuildInteractState(iPlayer, self.m_ID, iStatus | iType)
        

    
    def DoAction(seif, iAction, dParam):
        pass



class CPhyWall(CBuild):
    m_FightType = WARRIOR_AIRWALL_PHY
    
    def OnInitToScene(self, tPos):
        super(CPhyWall, self).OnInitToScene(tPos)
        if self.m_ModelData.m_ModelShape != MODEL_TYPE_BOX:
            return None
        vOrigin = tPos
        vAngle = self.m_ModelData.m_ModelAngle
        vAngle = (int(vAngle[0]), int(vAngle[1]), int(vAngle[2]))
        vOffset = self.m_ModelData.m_ModelCenter
        vSize = self.m_ModelData.m_ModelSize
        vScale = self.m_ModelData.m_ModelScale
        oGame = self.m_Game
        lstHero = []
        for iHero in oGame.m_WarMgr.GetLiveHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.m_Scene != self.m_Scene:
                continue
            vPos = oHero.GetPos()
            if cl_math.PosInOBB(vOrigin, vOffset, vSize, vScale, vAngle, vPos):
                lstHero.append(oHero)
        
        if not lstHero:
            return None
        vCenter = cl_math.Vec3MulV(vOffset, vScale)
        vCenter = cl_math.RotateByEuler(vCenter, vAngle)
        vCenter = cl_math.Vec3Add(vCenter, tPos)
        iLen = min(vSize[0] * vScale[0] * 0.5, vSize[2] * vScale[2] * 0.5)
        vDir = cl_math.RotateByEuler((0, 0, 1), vAngle)
        vForce = cl_math.Vec3DisplaceDir(vCenter, vDir, iLen * 1.5)
        vForce = (vForce[0], vForce[1] + 1.8, vForce[2])
        fGroundDis = oGame.Scene_GroundDistance(self.m_Scene, vForce, 5, PXMASK_MOVEBLK | PXMASK_OBJECT, self.m_ID)
        if fGroundDis < 5:
            vForce = (vForce[0], (vForce[1] - fGroundDis) + 1.8, vForce[2])
        for oHero in lstHero:
            oHero.Stop()
            oHero.WalkTo(vForce)
        



class CProtege(CBuild):
    m_Type = 'Protege'
    m_FightType = WARRIOR_PROTEGE_NORMAL
    m_ValidShowTips = 1
    
    def __init__(self, oGame, nid):
        super(CProtege, self).__init__(oGame, nid)
        self.SetInitInteract(INTERACT_TYPE_ALLOW)

    
    def InitBuild(self, clsData, dAddData):
        clsData.InitBuildData(self, dAddData)
        self.OnInitBuild(clsData, dAddData)
        self.InitWarValue()

    
    def Interact(self, oHero):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.OnInteract(oHero)
        iInteractType = self.m_PlayerInteractType[pid]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BUILD_INTERACT, self, {
            'pid': oHero.m_PlayerID,
            'Hero': oHero.m_ID,
            'Type': iInteractType,
            'Build': self.m_ID })
        if self.m_InteractFunc:
            self.m_InteractFunc(self, oHero)

    
    def OnInteract(self, oHero):
        pass

    
    def OnStopInteract(self, oHero):
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        for pid in lstPlayer:
            self.SetHeroInteractStatus(pid, 0)
        
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)

    
    def HPModifyDam(self, iAttack, lstChange):
        if iAttack and iAttack != self.m_ID and self.m_SID == BUILD_DEFENDNPC:
            oAttack = self.m_Game.GetObject(iAttack)
            if oAttack and oAttack.m_PlayerID:
                sText = f'''hpmodifydam {self.m_SID} recvdam from {oAttack.m_SID} {oAttack.m_ID}'''
                SendAlert('err', sText)
                TraceLog('err', sText)
                return ([
                    0,
                    0,
                    0], [], [])
        return super().HPModifyDam(iAttack, lstChange)



class CStonePillar(CBuild):
    m_Type = 'StonePillar'
    m_FightType = WARRIOR_STONEPILLAR
    m_ValidShowTips = 1
    
    def __init__(self, oGame, nid):
        super(CStonePillar, self).__init__(oGame, nid)
        self.m_Action = { }

    
    def OnInitBuild(self, clsData, dAddData):
        dAction = dAddData.get('Other', { }).get('Action', { })
        self.m_Action = dAction

    
    def DoAction(self, iAction, dParam):
        if iAction not in self.m_Action:
            return None
        tPos = self.m_Action[iAction]
        self.m_Game.Scene_Walk(self.m_ID, tPos)
        self.RefreshPos()
        if self.m_NavObstacle:
            self.m_NavObstacle.E_UpdatePosition()
        cl_scene.GS2CMapTriggerGate(self, iAction)



class CSummonStele(CBuild):
    m_Type = 'SummonStele'
    m_FightType = WARRIOR_SUMMON_STELE
    m_ValidShowTips = 1
    m_SubAttackMsg = ATTACKERSUBMSG_NORMAL
    
    def __init__(self, oGame, nid):
        super(CSummonStele, self).__init__(oGame, nid)
        self.m_Key = 'SummonStele'
        self.m_ActivatedRadius = 0
        self.m_HPDecreaseRadius = 0
        self.m_SpawnMonsterRadius = 0
        self.m_SpawnMonsterList = []
        self.m_SpawnMonsterEffect = 0
        self.m_HPDecreaseCoefficient = 0
        self.m_HeroCountCoefficient = 0
        self.m_TriggerHeroSet = set()
        self.m_CreateMonsterSet = set()
        self.m_MaxMonsterCount = 0
        self.m_SuperProbability = 0
        self.m_MonsterAfDict = { }
        self.m_HintEffect = 0
        self.m_HintEffectID = 0
        self.m_bActivated = False
        self.m_bActivatedListen = False
        self.m_SupplementHP = 0
        self.m_ForceRefreshFrame = 0
        self.m_AllDeadRefreshFrame = 0
        self.m_ForceRefreshTimerFlag = 'ForceRefreshTimerFlag'
        self.m_AllDeadRefreshTimerFlag = 'AllDeadRefreshTimer'
        self.m_HeroTriggerFrame = { }
        self.m_DamageCollectList = [
            0,
            0,
            0,
            0]

    
    def OnInitBuild(self, clsData, dAddData):
        self.m_ActivatedTrigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self, PXLAYER_DEVENT, {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': self.m_ActivatedRadius }, self.OnActivatedTrigger)
        self.m_ActivatedTrigger.rigidbody.E_SetKinematic(1)
        self.m_ActivatedTrigger.Disable()
        self.m_HPDecreaseTrigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self, PXLAYER_DEVENT, {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': self.m_HPDecreaseRadius }, self.OnHPDecreaseTrigger)
        self.m_HPDecreaseTrigger.rigidbody.E_SetKinematic(1)
        self.m_HPDecreaseTrigger.Disable()
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnWarriorDie, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.OnCreateMonsterBefore, self.m_Key)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_HP_CHANGE, self.OnHPChange, self.m_Key, -1, 0)
        self.WudiStart()

    
    def OnCreateMonsterBefore(self, oListener, oWarMgr, dMsgInfo):
        tPos = dMsgInfo['Pos']
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        iLevel = tLineIdx[0]
        iMyLevel = self.m_LineIdx[0]
        if iLevel != iMyLevel:
            return None
        if tLineIdx[1] == self.m_LineIdx[1] and not (self.m_bActivatedListen):
            self.m_bActivatedListen = True
            self.m_ActivatedTrigger.Enable()
        if tPos == self.m_Pos:
            dMsgInfo['ReplacePos'] = self.GetRandomPos(self.m_ModelData.GetModelRadius() + 1)

    
    def WudiStart(self):
        dArgs = {
            'AID': self.m_ID,
            'RS': cl_object.reason.CStrReason('SummonSteleWudi') }
        oState = cl_state.AddState(self, STATE_WUDI, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(self)
            SeasonLog.Debug('game:%d : SummonStele wudi start' % self.m_Game.m_ID)

    
    def WudiEnd(self):
        self.m_State.RemoveAllItemBySID(STATE_WUDI)
        SeasonLog.Debug('game:%d : SummonStele wudi end' % self.m_Game.m_ID)

    
    def OnHPChange(self, oSelf, dInfo):
        if not dInfo['IsDam']:
            return None
        iAttack = dInfo['AID']
        oAttack = self.m_Game.GetObject(iAttack)
        for iRealChange, oReason in dInfo['TrueChange']:
            sReason = oReason.GetStrReason()
            if sReason == 'SummonStele.OnWarriorDie':
                self.m_DamageCollectList[0] += iRealChange
                continue
            if sReason == 'SummonStele.OnHPDecreaseStart':
                self.m_DamageCollectList[1] += iRealChange
                continue
            if oAttack and oAttack.m_FightType & WARRIOR_DEVICE:
                self.m_DamageCollectList[3] += iRealChange
                continue
            self.m_DamageCollectList[2] += iRealChange
        

    
    def ShowHP(self, lstPlayer):
        if not self.m_bActivated:
            return None
        cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_ID, CBEHAVIOR_SUMMONSTELE_SHOWHP, lstPlayer)

    
    def GetSummonMonster(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, iRoomPos, _) = self.m_LineIdx
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not self.m_SpawnMonsterList:
            iExcludeMonster = 24011
            lstMonster = []
            oWarData = self.m_Game.m_WarData
            for iMonsterSID in oLevelNode.GetMonsterSpawnInfo(iRoomPos):
                clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
                if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                    continue
                if iMonsterSID == iExcludeMonster:
                    continue
                lstMonster.append(iMonsterSID)
            
            if not lstMonster:
                return 0
            self.m_SpawnMonsterList = lstMonster
        return self.m_SpawnMonsterList[self.m_Game.Random(len(self.m_SpawnMonsterList))]

    
    def OnActivatedTrigger(self, obj, iLeave):
        if not obj:
            return None
        if not obj.m_FightType & WARRIOR_HERO:
            return None
        if not iLeave:
            self.m_ActivatedTrigger.Disable()
            self.OnActivated()

    
    def OnActivated(self):
        if self.m_bActivated:
            return None
        self.m_bActivated = True
        self.ClearMaxAttr('IgnoreST%d' % STATE_CLS_ABNORMAL, 'OBSTACLE')
        self.WudiEnd()
        self.SummonMonster(self.m_MaxMonsterCount)
        self.DelayForceRefresh()
        self.ShowHP(self.GetScenePlayers())
        self.m_HPDecreaseTrigger.Enable()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SUMMONSTELE_TRIGGER, self, { })

    
    def OnHPDecreaseTrigger(self, obj, iLeave):
        if not obj:
            return None
        if not obj.m_FightType & WARRIOR_HERO:
            return None
        iHeroID = obj.m_ID
        if iLeave or iHeroID not in self.m_TriggerHeroSet:
            self.m_TriggerHeroSet.add(iHeroID)
            self.OnTriggerHeroCountChanged()
            self.OnHeroEnter(iHeroID)
        elif iHeroID in self.m_TriggerHeroSet:
            self.m_TriggerHeroSet.remove(iHeroID)
            self.OnTriggerHeroCountChanged()
            self.OnHeroLeave(obj)

    
    def OnHeroEnter(self, iHeroID):
        iCurFrame = self.m_Game.GetFrameNum()
        self.m_HeroTriggerFrame[iHeroID] = iCurFrame

    
    def OnHeroLeave(self, oHero):
        if oHero.m_ID in self.m_HeroTriggerFrame:
            iCurFrame = self.m_Game.GetFrameNum()
            iEnterFrame = self.m_HeroTriggerFrame.pop(oHero.m_ID)
            iTriggerFrame = iCurFrame - iEnterFrame
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SUMMONSTELE_END, oHero, {
                'TriggerFrame': iTriggerFrame })

    
    def DealHeroTriggerTime(self):
        for iHero in self.m_TriggerHeroSet:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.OnHeroLeave(oHero)
        

    
    def OnTriggerHeroCountChanged(self):
        if self.m_TriggerHeroSet:
            self.HPDecreaseStart()
        else:
            self.HPDecreaseEnd()

    
    def HPDecreaseStart(self):
        oState = self.m_State.GetItemBySID(STATE_SUMMONSTELE_HPDECREASE)
        if not oState:
            dArgs = {
                'AID': self.m_ID,
                'RS': cl_object.reason.CStrReason('SummonStele.OnHPDecreaseStart') }
            oState = cl_state.AddState(self, STATE_SUMMONSTELE_HPDECREASE, STATE_TIME_FOREVER, 0, dArgs)
            if not oState:
                return None
            oState.Enable(self)
        iNowCount = oState.GetCount()
        iAddCount = len(self.m_TriggerHeroSet) - iNowCount
        oState.AddCount(self, iAddCount)

    
    def HPDecreaseEnd(self):
        self.m_State.RemoveAllItemBySID(STATE_SUMMONSTELE_HPDECREASE)

    
    def OnWarriorDie(self, oListener, oVictim, dMsgInfo):
        iVictimID = oVictim.m_ID
        if iVictimID in self.m_TriggerHeroSet:
            self.m_TriggerHeroSet.remove(iVictimID)
            self.OnTriggerHeroCountChanged()
            self.OnHeroLeave(oVictim)
        if iVictimID == self.m_ID:
            self.OnDead()
            return None
        if self.IsDead():
            return None
        if iVictimID in self.m_CreateMonsterSet:
            self.m_CreateMonsterSet.remove(iVictimID)
            if not self.m_CreateMonsterSet:
                self.Remove_Call_Out(self.m_AllDeadRefreshTimerFlag)
                self.Call_Out(self.SupplementMonster, self.m_AllDeadRefreshFrame, self.m_AllDeadRefreshTimerFlag)

    
    def GetRandomPos(self, fRadius):
        tPos = self.m_Game.Scene_RandomPointSectorInMesh(self.m_Scene, self.m_Pos, (1, 0, 0), self.m_ModelData.GetModelRadius(), fRadius, 0, 180)
        if tPos:
            return tPos
        return self.m_Pos

    
    def SummonMonster(self, iCount):
        tFace = self.GetFacing()
        vFixDropPos = self.Query('FixDropPos', None)
        dCheckDropInfo = self.Query('CheckDropInfo', None)
        for _ in range(iCount):
            tPos = self.GetRandomPos(self.m_SpawnMonsterRadius)
            iMonsterSID = self.GetSummonMonster()
            if not iMonsterSID:
                SendAlert('err', 'summonStele summonMonster err %d, %s' % (self.m_Game.m_ID, self.m_LineIdx))
                return None
            self.CreateMonster(iMonsterSID, tPos, tFace, vFixDropPos, dCheckDropInfo)
        

    
    def SupplementMonster(self):
        iSummonCount = self.m_MaxMonsterCount - len(self.m_CreateMonsterSet)
        for _ in range(iSummonCount):
            if self.IsDead():
                return None
            self.SummonMonster(1)
            oReason = cl_object.reason.CStrReason('SummonStele.OnWarriorDie')
            self.HPDirectModify('HP', self.m_ID, -(self.m_SupplementHP), oReason)
        
        self.Remove_Call_Out(self.m_AllDeadRefreshTimerFlag)
        self.DelayForceRefresh()

    
    def DelayForceRefresh(self):
        self.Remove_Call_Out(self.m_ForceRefreshTimerFlag)
        self.Call_Out(self.SupplementMonster, self.m_ForceRefreshFrame, self.m_ForceRefreshTimerFlag)

    
    def GetScenePlayers(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return []
        return oScene.GetPlayers()

    
    def CreateMonster(self, iMonsterSID, tPos, tFace, vFixDropPos, dCheckDropInfo):
        oDeviceElement = self.m_Game.m_WarMgr.GetComponent('DeviceElement')
        tLineIdx = self.m_LineIdx
        oDeviceElement.m_DeviceChallengeMgr.IncreaseCreatingCount(tLineIdx)
        oPerform = self.GetPerformIfNoThenNew(self.m_SpawnMonsterEffect)
        dData = {
            'vStart': self.GetAttackPos(),
            'Custom': {
                'vEnd': tPos,
                'dInfo': {
                    'iScene': self.m_Scene,
                    'iMonsterSID': iMonsterSID,
                    'tFace': tFace,
                    'vFixDropPos': vFixDropPos,
                    'dCheckDropInfo': dCheckDropInfo,
                    'tMonsterSuper': self.GetSuperMonster(),
                    'tLineIdx': tLineIdx } } }
        cl_war.UsePerform(self, oPerform, dData)

    
    def GetSuperMonster(self):
        if not (self.m_SuperProbability) or not (self.m_MonsterAfDict):
            return (0, 0, 0)
        iRange = ChooseRange(self.m_Game, 1, 10000)
        if iRange > self.m_SuperProbability:
            return (0, 0, 0)
        oWarMgr = self.m_Game.m_WarMgr
        oMonsterSuper = oWarMgr.GetComponent('MonsterSuper')
        if not oMonsterSuper:
            return (0, 0, 0)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        iSuperLevel = oMonsterSuper.GetMonsterSuperLevel(oLevelNode.m_LevelType)
        iAf = ChooseKey(self.m_Game, self.m_MonsterAfDict)
        return (iSuperLevel, 0, iAf)

    
    def NetAddTo(self, dPlayer):
        super(CSummonStele, self).NetAddTo(dPlayer)
        self.ShowHP(dPlayer)

    
    def OnDead(self):
        self.DealHeroTriggerTime()
        self.m_HPDecreaseTrigger.Disable()
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_Key)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_HP_CHANGE, self.m_Key)
        self.Remove_Call_Out(self.m_ForceRefreshTimerFlag)
        self.Remove_Call_Out(self.m_AllDeadRefreshTimerFlag)

    
    def Release(self):
        self.m_ActivatedTrigger.Unstall()
        self.m_HPDecreaseTrigger.Unstall()
        self.m_ActivatedTrigger = None
        self.m_HPDecreaseTrigger = None
        super(CSummonStele, self).Release()



class CMonsterBuild(CBuild):
    m_Type = 'MonsterBuild'
    m_FightType = WARRIOR_MONSTERBUILD
    m_ValidShowTips = 1
    
    def InitBuild(self, clsData, dAddData):
        clsData.InitBuildData(self, dAddData)
        self.OnInitBuild(clsData, dAddData)
        self.InitWarValue()



class CGeyserBuild(CBuild):
    m_Type = 'GeyserBuild'
    m_FightType = WARRIOR_GEYSER
    m_ShowHight = 0
    m_DropSpeedPercent = 100
    m_EnablePreTime = 50
    
    def __init__(self, oGame, iOwner):
        super(CGeyserBuild, self).__init__(oGame, iOwner)
        self.m_Center = (0, 0, 0)
        self.m_HalfExt = (0, 0, 0)
        self.m_Direction = (0, 0, 0)
        self.m_Distance = 0
        self.m_HoldingFrame = 0
        self.m_DelayFrame = 0
        self.m_EnableFrame = 0

    
    def OnInitBuild(self, clsData, dAddData):
        if 'Center' in dAddData:
            self.m_Center = dAddData['Center']
        if 'HalfExt' in dAddData:
            self.m_HalfExt = dAddData['HalfExt']
        if 'Direction' in dAddData:
            self.m_Direction = dAddData['Direction']
        if 'Distance' in dAddData:
            self.m_Distance = int(dAddData['Distance'])
        if 'HoldingTime' in dAddData:
            self.m_HoldingFrame = Time2Frame(int(dAddData['HoldingTime']))
            if self.m_HoldingFrame:
                self.m_HoldingFrame += Time2Frame(self.m_EnablePreTime)
        if 'DelayTime' in dAddData:
            self.m_DelayFrame = Time2Frame(int(dAddData['DelayTime']))
        if 'ShowHight' in dAddData:
            self.m_ShowHight = dAddData['ShowHight']
        if 'DropSpeedPercent' in dAddData:
            self.m_DropSpeedPercent = dAddData['DropSpeedPercent']
        self.Enable()

    
    def Enable(self):
        self.m_EnableFrame = self.m_Game.GetFrameNum()
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)
        if self.m_HoldingFrame:
            self.Call_Out(self.Disable, self.m_HoldingFrame, 'DelayDisableGeyser')

    
    def Disable(self):
        self.m_EnableFrame = 0
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)
        if self.m_DelayFrame:
            self.Call_Out(self.Enable, self.m_DelayFrame, 'DelayEnableGeyser')

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        net.GS2CGeyserInfo(self.m_Game, self.m_ID, self.m_Center, self.m_HalfExt, self.m_Direction, self.m_Distance, self.m_ShowHight, self.m_EnableFrame, self.m_EnablePreTime, self.m_DropSpeedPercent, dPlayer)



class CMonsterHinder(CBuild):
    m_FightType = WARRIOR_MONSTERHINDER
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_DieRemoveState = { }
        self.m_OwnerBuild = 0

    
    def OnContact(self, iTarget, dArgs):
        pass

    
    def SetOwnerBuild(self, iBuild):
        self.m_OwnerBuild = iBuild

    
    def OnInitToScene(self, tPos):
        self.m_PhyModel.SetEnableSimulation(0)
        self.m_PhyModel.SetTrigger(1)
        super().OnInitToScene(tPos)

    
    def OnTriggerEnter(self, oTarget):
        oState = oTarget.m_State.GetItemBySID(STATE_MONSTER_HINDER)
        iTarget = oTarget.m_ID
        if not oState:
            oReason = cl_object.reason.CStrReason('MonsterHinder')
            dStateArgs = {
                'AID': self.m_ID,
                'RS': oReason }
            oState = cl_state.AddState(oTarget, STATE_MONSTER_HINDER, STATE_TIME_FOREVER, 0, dStateArgs)
            if not oState:
                return None
            oState.Enable(oTarget)
        self.m_DieRemoveState[iTarget] = 1
        dArgValue = oState.SetArgValueDefault('Soure', { })
        dArgValue[self.m_ID] = 1

    
    def OnTriggerLeave(self, oTarget):
        iTarget = oTarget.m_ID
        if iTarget in self.m_DieRemoveState:
            self.m_DieRemoveState.pop(iTarget)
        self.RemoveTriggerState(iTarget)

    
    def RemoveTriggerState(self, iTarget):
        oGame = self.m_Game
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            return None
        oState = oTarget.m_State.GetItemBySID(STATE_MONSTER_HINDER)
        if not oState:
            return None
        dArgValue = oState.GetArgValue('Soure', { })
        if self.m_ID in dArgValue:
            dArgValue.pop(self.m_ID)
        if not dArgValue:
            oTarget.m_State.RemoveItem(oState.m_ID)

    
    def DieRemove(self):
        oGame = self.m_Game
        oOwnerBuild = oGame.GetObject(self.m_OwnerBuild, DEAD_FLAG_DIED)
        if oOwnerBuild:
            if oOwnerBuild.m_FightType == WARRIOR_MONSTENOPHYRHINDER:
                oOwnerBuild.TryRemoveBySonDie(self.m_ID)
            else:
                OtherLog.Debug('game:%d: monsterhinder err, %d' % (oGame.m_ID, self.m_ID))
        super().DieRemove()

    
    def Remove(self, sReason):
        for iTarget in self.m_DieRemoveState:
            self.RemoveTriggerState(iTarget)
        
        super().Remove(sReason)



class CMonsterNoPhyHinder(CBuild):
    m_FightType = WARRIOR_MONSTENOPHYRHINDER
    m_SonHinderSID = 1207
    m_ShowModelData = (1.3, 1.3, 1.3)
    m_MaxColumn = 3
    m_MaxRow = 3
    m_GroundRow = 2
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_SonHinder = { }
        self.m_HinderToPos = { }
        self.m_PosToHinder = [
            [
                0] * 3,
            [
                0] * 3,
            [
                0] * 3]
        self.m_RemovHindering = False

    
    def TryRemoveBySonDie(self, iHinder):
        self.m_SonHinder.pop(iHinder, 0)
        (iRows, iColumns) = self.m_HinderToPos.pop(iHinder, (0, 0))
        self.m_PosToHinder[iRows][iColumns] = 0
        if self.m_RemovHindering:
            return None
        lstDisconnectedHinder = self.GetDisconnectedHinder()
        if lstDisconnectedHinder:
            self.m_RemovHindering = True
            for iSonHinder in lstDisconnectedHinder:
                oSonHinder = self.m_Game.GetObject(iSonHinder, DEAD_FLAG_DIED)
                if oSonHinder:
                    cl_snetwar.GS2CDie(oSonHinder, self.m_ID, iFinalDam = 0)
                    oSonHinder.DieRemove()
            
            self.m_RemovHindering = False
        if not self.m_SonHinder:
            self.DieRemove()

    
    def GetDisconnectedHinder(self):
        lstQueue = []
        dVisited = { }
        for i in range(self.m_MaxColumn):
            iHinder = self.m_PosToHinder[self.m_GroundRow][i]
            if iHinder:
                lstQueue.append((self.m_GroundRow, i))
                dVisited[iHinder] = 1
        
        lstOffset = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)]
        for i in range(9):
            if not lstQueue:
                break
            (iRow, iCol) = lstQueue.pop(0)
            for iOffsetRow, iOffsetCol in lstOffset:
                iResRow = iRow + iOffsetRow
                iResCol = iCol + iOffsetCol
                if not self.IsLegalPos(iResRow, iResCol):
                    continue
                iHinder = self.m_PosToHinder[iResRow][iResCol]
                if iHinder and iHinder not in dVisited:
                    dVisited[iHinder] = 1
                    lstQueue.append((iResRow, iResCol))
            
        
        lstDisconnected = []
        for iHinder in self.m_SonHinder:
            if iHinder not in dVisited:
                lstDisconnected.append(iHinder)
        
        return lstDisconnected

    
    def IsLegalPos(self, iRow, iCol):
        if 0 <= iRow and iRow < self.m_MaxRow:
            if 0 <= iCol and iCol < self.m_MaxColumn:
                return 1
        return 0

    
    def MapSendPacket(self, dPlayer):
        pass

    
    def DieRemove(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            dMonsterHinder = oScene.m_SceneData.Query('MonsterHinder', { })
            if self.m_ID in dMonsterHinder:
                dMonsterHinder.pop(self.m_ID)
        super().DieRemove()

    
    def CreateSonHinderByNum(self, lstNum, vCenter, iRotate):
        oGame = self.m_Game
        clsSummonData = oGame.m_WarData.GetBuildData(self.m_SonHinderSID)
        tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Box')
        for iNum in lstNum:
            tPos = self.GetPosByNum(vCenter, iNum, iRotate)
            iSonHinder = self.CreateSonHinder(tModelData, tPos, iRotate)
            if iSonHinder:
                (iRows, iColumns) = divmod(iNum - 1, self.m_MaxColumn)
                self.m_PosToHinder[iRows][iColumns] = iSonHinder
                self.m_HinderToPos[iSonHinder] = (iRows, iColumns)
        
        OtherLog.Debug('game:%d: nophyhinder %s, son:%s' % (oGame.m_ID, self.m_ID, self.m_SonHinder))

    
    def CreateSonHinder(self, tModelData, tPos, iRotate):
        dAddData = {
            'Angle': [
                0,
                iRotate,
                0],
            'Center': [
                0,
                tModelData[1] * 0.5,
                0],
            'Origin': tPos,
            'GlobalArea': 0,
            'SID': self.m_SonHinderSID,
            'Scale': [
                1,
                1,
                1],
            'Shape': MODEL_TYPE_BOX,
            'Size': tModelData }
        oGame = self.m_Game
        oSonHinder = oGame.m_ResMgr.CreateBuild(self.m_Scene, self.m_SonHinderSID, dAddData)
        if not oSonHinder:
            return 0
        self.m_SonHinder[oSonHinder.m_ID] = 1
        self.m_FollowDieObjs[oSonHinder.m_ID] = 1
        oSonHinder.SetOwnerBuild(self.m_ID)
        return oSonHinder.m_ID

    
    def GetPosByNum(self, tPos, iNum, iRotate):
        tModelData = self.m_ShowModelData
        if iNum == 1:
            vOffset = [
                -tModelData[0],
                tModelData[1] * 2,
                0]
        elif iNum == 2:
            vOffset = [
                0,
                tModelData[1] * 2,
                0]
        elif iNum == 3:
            vOffset = [
                tModelData[0],
                tModelData[1] * 2,
                0]
        elif iNum == 4:
            vOffset = [
                -tModelData[0],
                tModelData[1],
                0]
        elif iNum == 5:
            vOffset = [
                0,
                tModelData[1],
                0]
        elif iNum == 6:
            vOffset = [
                tModelData[0],
                tModelData[1],
                0]
        elif iNum == 7:
            vOffset = [
                -tModelData[0],
                0,
                0]
        elif iNum == 9:
            vOffset = [
                tModelData[0],
                0,
                0]
        else:
            return tPos
        vOffset = cl_math.RotateByEuler(vOffset, (0, iRotate, 0))
        tPos = cl_math.Vec3Add(tPos, vOffset)
        return tPos



class CMoveBuild(CBuild):
    m_FightType = WARRIOR_MOVEBUILD
    
    def __init__(self, oGame, iOwner):
        super().__init__(oGame, iOwner)
        self.m_StartPos = None
        self.m_EndPos = None
        self.m_MoveType = 0

    
    def OnInitBuild(self, clsData, dAddData):
        self.m_StartPos = dAddData['Origin']
        self.m_EndPos = dAddData['EndPos']
        self.m_MoveType = dAddData['MoveType']
        self.m_MoveSecond = dAddData['MoveTime']

    
    def OnInitToScene(self, tPos):
        super().OnInitToScene(tPos)
        self.m_StartPos = tPos
        iFrame = Second2Frame(self.m_MoveSecond)
        oGame = self.m_Game
        if iFrame:
            self.DoMove(self.m_StartPos, self.m_EndPos, iFrame)
        else:
            SendAlert('err', 'movesecond err %d, %s' % (oGame.m_ID, self.m_StartPos))

    
    def TerminalPos(self):
        pass

    
    def UpdatePos(self, tVec):
        tPos = self.m_Pos
        tNewPos = (tPos[0] + tVec[0], tPos[1] + tVec[1], tPos[2] + tVec[2])
        self.m_Game.Scene_Walk(self.m_ID, tNewPos)
        self.RefreshPos()

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        oGame = self.m_Game
        tMoveInfo = oGame.m_FrameMoveMgr.GetMoveInfo(self)
        if not tMoveInfo:
            return None
        (_tVec, iDstFrame) = tMoveInfo
        iCurFrame = oGame.GetFrameNum()
        iRemainFrame = iDstFrame - iCurFrame
        if iRemainFrame <= 0:
            return None
        tStart = self.GetPos()
        iMoveTime = Frame2Time(iRemainFrame)
        net.GS2CBuildMove(self.m_ID, tStart, self.m_EndPos, iMoveTime, dPlayer)

    
    def DoMove(self, tStart, tEnd, iFrame):
        tMoveDisp = cl_math.Vec3Minus(tEnd, tStart)
        tVec = (tMoveDisp[0] / iFrame, tMoveDisp[1] / iFrame, tMoveDisp[2] / iFrame)
        oGame = self.m_Game
        oGame.m_FrameMoveMgr.AddSimObj(self, tVec, iFrame)
        if self.m_MoveType == MOVE_BUILD_LINE:
            self.SendMoveInfo(tStart, tEnd, iFrame)
        elif self.m_MoveType == MOVE_BUILD_COMEANDGO:
            self.Remove_Call_Out('BuildLineRemove')
            self.m_StartPos = tStart
            self.m_EndPos = tEnd
            self.Call_Out(Functor(self.DoMove, tEnd, tStart, iFrame), iFrame, 'BuildLineRemove')
            self.SendMoveInfo(tStart, tEnd, iFrame)

    
    def SendMoveInfo(self, tStart, tEnd, iFrame):
        iMoveTime = Frame2Time(iFrame)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            dPlayer = oScene.GetPlayers()
            net.GS2CBuildMove(self.m_ID, tStart, tEnd, iMoveTime, dPlayer)


