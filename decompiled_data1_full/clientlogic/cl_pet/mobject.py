# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_pet/mobject.pyc
# RelativePath: clientlogic/cl_pet/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, PET_PUT_ATTROFFSET, PET_PUT_ABILITY_QUALITY, MOVE_TYPE_NORMAL, PET_PUT_ABILITY_COUNT, ATT_SHAPE_SPHERE, PF_TYPE_PETACTIVE, WARRIOR_PET, PET_HATE_START, WARRIOR_HERO, PET_HATE_UPDATE, PET_HATE_END, PF_TYPE_PETABILITY, PET_PUT_WAY_FUSE, ATTACKERSUBMSG_NORMAL, PETPF_ACTIVE_SLIP_SPELL, MODEL_TYPE_SCALECTRLAGENT, TYPE_RELIFE_LEAVEBATTLE, MOVE_TYPE_JUMP, PET_PUT_WAY_HATCH_RARE, LINK_ONLINE, LINK_DELEGATE, LINK_ACTIVEDELEGATE, OBJ_ATTACK
from cl_pxlayer import PXMASK_PLAYER, PXMASK_BLOCK
from cl_propdata import BASIC_PROP_NAME, INFO_OBJECT_INIT, PROP_PET_SHOW, PC_SEND_SBC, PC_SEND_SELF
from cl_only import DeepCopy, GAME_FRAME, Functor, SendAlert, TraceLog
from cl_object.logging import PetLog
import cl_pet
import cl_warrior
import cl_formula
import cl_netattr
import cl_container.petabilitycon
import cl_facectrl
import cl_msgcenter
import cl_math
import cl_monster.monsterstatus
import cl_extraattr
import cl_modeldefine
import cl_engphyobj
import cl_modeldata
import cl_platformdata
PET_BASE_ATTR = [
    'HPMax',
    'Att',
    'AttSpeed',
    'SkillInterval']
PET_LEAVEBATTLE_ENABLE = [
    50701,
    50706]

class CPet(cl_warrior.CWarrior):
    m_Type = 'Pet'
    m_EnterDelay = GAME_FRAME
    m_Delete = 0
    m_RelifeCheckRadius = 20
    m_Phase = 0
    m_FightType = WARRIOR_PET
    m_EnterBattle = 0
    m_MaxCloneNum = 0
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_CurLineIdx = None
        self.m_AttrOffset = { }
        self.m_AttrInfo = { }
        self.m_AbilityCon = cl_container.petabilitycon.CPetAbilityContainer(self)
        self.m_Resistance = cl_extraattr.CResistance('Resistance', iVal = 0, iSync = 0)
        self.m_EnableSpell = set()
        self.m_Lock = 0

    
    def InitPet(self, iPutWay, dAddData):
        oGame = self.m_Game
        dMinOffset = dAddData.get('MinOffset', { })
        dConfig = cl_pet.GetPutWayConfig(iPutWay)
        (iBaseMinOffset, iMaxOffset) = dConfig.get(PET_PUT_ATTROFFSET, (-10, 10))
        for sAttr in PET_BASE_ATTR:
            iMinOffset = dMinOffset[sAttr] if sAttr in dMinOffset else iBaseMinOffset
            iRandomRange = (iMaxOffset - iMinOffset) + 1
            self.m_AttrOffset[sAttr] = oGame.Random(iRandomRange) + iMinOffset
        
        if iPutWay == PET_PUT_WAY_HATCH_RARE:
            for sAttr, iOffset in self.m_AttrOffset.items():
                if iOffset == iMaxOffset:
                    break
            else:
                iIdx = oGame.Random(len(PET_BASE_ATTR))
                sAttr = PET_BASE_ATTR[iIdx]
                self.m_AttrOffset[sAttr] = iMaxOffset
        self.Set('Scale', 100)
        cl_formula.ResetPetFormulaAttr(self, self.m_AttrInfo, BASEATTR_REFRESH)
        if oGame.m_WarMgr.IsEndless():
            iLayer = 99
        else:
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            iLayer = oLevelCtrl.m_LayerNum
        if PET_PUT_ABILITY_QUALITY in dConfig and iLayer in dConfig[PET_PUT_ABILITY_QUALITY]:
            dQualityWeight = dConfig[PET_PUT_ABILITY_QUALITY][iLayer]
        else:
            dQualityWeight = { }
        if iPutWay == PET_PUT_WAY_FUSE:
            self.m_AbilityCon.InitFuseAbility(dAddData, dQualityWeight)
        elif PET_PUT_ABILITY_COUNT in dConfig and iLayer in dConfig[PET_PUT_ABILITY_COUNT]:
            dCountWeight = dConfig[PET_PUT_ABILITY_COUNT][iLayer]
        else:
            dCountWeight = { }
        self.m_AbilityCon.InitAbility(iPutWay, dCountWeight, dQualityWeight)
        self.SetSavedData('IsNew', 1)
        PetLog.Debug('%s %s initpet %s-%s putway:%s offset:%s' % (oGame.m_ID, self.m_OwnerPlayerID, self.m_ID, self.m_SID, iPutWay, self.m_AttrOffset))

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        self.RefreshAbility(dPlayer)
        self.RefreshShowSpell(dPlayer)

    
    def LoadCompanionPet(self, dData):
        dAttrOffset = dData['Offset']
        for sAttr in PET_BASE_ATTR:
            self.m_AttrOffset[sAttr] = dAttrOffset.get(sAttr, 0)
        
        cl_formula.ResetPetFormulaAttr(self, self.m_AttrInfo, BASEATTR_REFRESH)
        self.m_AbilityCon.SetSealedAbility(dData['Ability'])
        PetLog.Debug('%s %s loadcompanionpet %s-%s offset:%s %s' % (self.m_Game.m_ID, self.m_OwnerPlayerID, self.m_ID, self.m_SID, self.m_AttrOffset, self.SealedAbility()))

    
    def Release(self):
        self.Remove_Call_Out('DelayEnterScene')
        self.ReleaseAttention()
        if self.m_AbilityCon:
            self.m_AbilityCon.Release()
        self.m_AbilityCon = None
        self.m_MoveStatusMgr = None
        self.m_FightStatusMgr = None
        super().Release()

    
    def GetPerform(self, iPerform, iItemID = 0, iOwnPfid = 0):
        if self.m_ReleaseFlag:
            return None
        oPerform = self.m_Perform.GetPerform(iPerform)
        if not oPerform:
            oPerform = self.m_AbilityCon.GetPerform(iPerform)
        return oPerform

    
    def GetPerformSIDByType(self, iPFType):
        lstPerform = super().GetPerformSIDByType(iPFType)
        lstPerform.extend(self.m_AbilityCon.GetPerformSIDByType(iPFType))
        return lstPerform

    
    def InitAttention(self):
        if not self.m_Owner:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner and oOwner.Online() not in (LINK_ACTIVEDELEGATE, LINK_DELEGATE):
            self.AddSendOwnerAttention()
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_KILL, SendKillMsg2Owner, 'OnKill', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, 'OnDealTotalDam', iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OwnerEnterScene, 'OwnerEnterScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OwnerLeaveScene, 'OwnerLeaveScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, self.OwnerDieDist, 'OwnerDieDist')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OwnerChangeLinkStatus, 'OwnerChangeLinkStatus')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_TRIGGERGATETRANSFER, self.OnOwnerTransfer, 'OwnerTransfer')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_TRIGGERGATECTRL, self.OnHeroTriggerGateCtrl, 'PetOwnerTriggerGateCtrl')

    
    def ReleaseAttention(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        self.DoneSendOwnerAttention()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_KILL, 'OnKill')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'OnDealTotalDam')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, 'OwnerEnterScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, 'OwnerDieDist')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, 'OwnerChangeLinkStatus')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_TRIGGERGATETRANSFER, 'OwnerTransfer')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_TRIGGERGATECTRL, 'PetOwnerTriggerGateCtrl')

    
    def Save(self):
        dData = {
            'SID': self.m_SID,
            'AO': self.m_AttrOffset,
            'SD': DeepCopy(self.m_SavedData) }
        dData['AP'] = self.m_AbilityCon.Save()
        dData['Lock'] = self.GetLock()
        return dData

    
    def Load(self, dInfo):
        self.m_SID = dInfo['SID']
        self.m_AttrOffset = dInfo['AO']
        self.m_SavedData = dInfo['SD']
        cl_formula.ResetPetFormulaAttr(self, self.m_AttrInfo, BASEATTR_REFRESH)
        self.m_AbilityCon.Load(dInfo.get('AP', { }))
        self.m_Lock = dInfo.get('Lock', 0)

    
    def OnCreated(self):
        self.m_PropChangeBCType = PC_SEND_SELF
        self.InitWarValue()
        self.SetCtrlModelData()
        self.m_HP = self.QueryAttr('HPMax')
        self.m_Speed = self.QueryAttr('MoveSpeed')
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)
        self.m_MoveStatusMgr = cl_monster.monsterstatus.CMoveStatusMgr(self)
        self.m_FightStatusMgr = cl_monster.monsterstatus.CFightStatusMgr(self)
        (self.m_PreDodgeTime, self.m_DodgeTime, self.m_PostDodgeTime) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Dodge')
        self.RemoveAgent()
        self.m_Agent.PauseAgent('LeaveScene')

    
    def SetCtrlModelData(self, iScale = 0):
        if not iScale:
            iScale = self.QueryAttr('Scale')
        dParam = {
            'ObjShape': self.m_Shape,
            'Shape': MODEL_TYPE_SCALECTRLAGENT,
            'Scale': iScale / 100 }
        self.m_ModelData = cl_modeldata.GetModel(dParam)

    
    def SetModelScale(self, iScale):
        self.Set('Scale', iScale)
        self.SetCtrlModelData(iScale)
        self.m_ModelRadius = self.m_ModelData.GetModelRadius()
        self.m_ModelHeight = self.m_ModelData.GetModelHeight()
        if self.m_PhyModel:
            self.m_PhyModel.E_Unstall()
            (iPaType, iNavType, iLayer, dParam) = self.GetModelAttr()
            self.m_PhyModel = cl_engphyobj.CreatePhyModel(self, iPaType, iLayer, dParam)

    
    def RemoveAgent(self):
        oAgent = self.m_Agent
        oGameSpace = oAgent.m_GameSpace
        oContext = oGameSpace.GetContext(oAgent.m_ContextID)
        if oContext:
            oContext.RemoveAgent(oAgent)

    
    def AddAgent(self):
        oAgent = self.m_Agent
        oGameSpace = oAgent.m_GameSpace
        oGameSpace.AddAgentToNextContext(oAgent)

    
    def SetOwner(self, oHero):
        self.m_Owner = oHero.m_ID
        self.m_OwnerPlayerID = oHero.m_PlayerID

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakePetAddPacket(self, dPlayer)

    
    def ResetByDie(self):
        if self.m_MoveMode != MOVE_TYPE_NORMAL:
            if self.m_MoveMode == MOVE_TYPE_JUMP:
                self.WalkTo(self.m_MoveCtrl.m_JumpStart, 'resetbydie')
            self.m_MoveMode = MOVE_TYPE_NORMAL
        super().ResetByDie()

    
    def WalkTo(self, vPos, sReason = ''):
        if self.m_MoveCtrl:
            self.m_MoveCtrl.StopJump()
        super().WalkTo(vPos, sReason)

    
    def GotoBornPos(self, tPos = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        if not tPos:
            tPos = self.Query('PetBornPos', None)
        if not tPos:
            tOwnerPos = oOwner.GetPos()
            tInfo = self.Query('BronPosInfo', (0, 5, 120, 180))
            if not tInfo:
                return None
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
        if iScene == self.m_Scene:
            self.WalkTo(tPos)
        else:
            self.Goto(iScene, tPos)

    
    def OnRelife(self):
        super().OnRelife()
        oOwner = self.GetOwner()
        if self.m_MoveCtrl:
            self.m_MoveCtrl.E_Enable()
        if oOwner.IsRealDied():
            return None
        oPetCon = oOwner.m_PetCon
        if oPetCon and oPetCon.m_CurPet != self.m_ID:
            return None
        if not (self.m_EnterBattle) and oPetCon:
            oPetCon.PetEnterBattle()
        else:
            self.TryGotoBornPos()

    
    def Remove(self, sReason):
        PetLog.Debug('%s %s remove %s %s' % (self.m_GameID, self.m_OwnerPlayerID, self.m_ID, sReason))
        super().Remove(sReason)

    
    def TryGotoBornPos(self):
        if self.m_Scene and self.m_RelifeCheckRadius:
            dMask = {
                'Mask': PXMASK_PLAYER,
                'BlockMask': PXMASK_BLOCK }
            lstArgs = [
                self.GetPos(),
                self.m_RelifeCheckRadius]
            lstVLST = cl_math.GetAttackTargetList(self.m_Game, self.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
            if lstVLST:
                return None
        self.GotoBornPos()

    
    def EnterBattle(self):
        self.AttrClear('RHP', 'LeaveBattle')
        self.m_PropChangeBCType = PC_SEND_SBC
        self.GotoBornPos()
        self.AddAgent()
        self.OnEnterBattle()
        self.m_EnterBattle = 1

    
    def LeaveBattle(self, iLeaveGame = 0):
        self.AttrChange('RHP', 50000, 0, 'LeaveBattle')
        if self.IsDead() and not iLeaveGame:
            dReason = {
                'AID': self.m_ID,
                'Type': TYPE_RELIFE_LEAVEBATTLE }
            self.Relife(dReason, {
                'HP': 1 })
        self.LeaveScene(0)
        self.m_PropChangeBCType = PC_SEND_SELF
        self.RemoveAgent()
        self.OnLeaveBattle()
        self.m_EnterBattle = 0

    
    def LeaveScene(self, iNewScene):
        super().LeaveScene(iNewScene)
        self.m_Game.m_SkillMgr.AttackLeaveScene(self.m_ID)
        if self.m_Scene:
            self.RemoveFromScene()

    
    def OnEnterBattle(self):
        self.InitAttention()
        self.m_Perform.AllPerformEnable(iNotify = 0)
        self.m_AbilityCon.AllPerformEnable()

    
    def OnLeaveBattle(self):
        self.Remove_Call_Out('DelayEnterScene')
        self.ReleaseAttention()
        for iPerform in self.m_Perform.GetAllPerformSID():
            if iPerform in PET_LEAVEBATTLE_ENABLE:
                continue
            oPerform = self.m_Perform.GetPerform(iPerform)
            if oPerform:
                oPerform.Disable(self, iNotify = 0)
        
        self.m_AbilityCon.AllPerformDisable()

    
    def GetWarReportInfo(self):
        dPetData = {
            'SID': self.m_SID,
            'BaseAttr': self.GetShowBaseAttrPacketInfo(),
            'Offset': dict(self.m_AttrOffset),
            'Ability': self.Ability() }
        return dPetData

    
    def GetShowBaseAttrPacketInfo(self):
        lstBasePropInfo = []
        clsData = cl_platformdata.GetPetClass(self.m_SID)
        for sAttr in INFO_OBJECT_INIT[PROP_PET_SHOW]:
            if sAttr in self.m_AttrOffset:
                func = cl_formula.g_PetNoGrowthFunc[sAttr]
                iValue = func(clsData, sAttr, self.m_AttrOffset[sAttr])
            elif self.HasAttr(sAttr):
                oAttr = self.GetAttr(sAttr)
                iValue = oAttr.GetBaseAttr()
            else:
                iValue = cl_formula.GetWarriorAttr(sAttr, self)
            (iIdx, _, iType, iLen, _) = BASIC_PROP_NAME[sAttr]
            lstBasePropInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Attr': lstBasePropInfo }

    
    def GetAttrOffsetPacketInfo(self):
        dOffset = { }
        for sAttr, iVal in self.m_AttrOffset.items():
            iIdx = BASIC_PROP_NAME[sAttr][0]
            dOffset[iIdx] = iVal
        
        return dOffset

    
    def OwnerEnterScene(self, _oPet, _oOwner, _dMsgInfo):
        if not self.IsDead():
            self.Remove_Call_Out('DelayEnterScene')
            self.Call_Out(self.GotoBornPos, self.m_EnterDelay, 'DelayEnterScene')

    
    def OwnerLeaveScene(self, _oPet, _oOwner, dMsgInfo):
        self.Remove_Call_Out('DelayEnterScene')
        iNewScene = dMsgInfo['NewScene']
        self.LeaveScene(iNewScene)

    
    def OwnerDieDist(self, _oPet, oOwner, _dMsgInfo):
        self.LeaveBattle()

    
    def OwnerChangeLinkStatus(self, _oPet, oOwner, dMsgInfo):
        if not self.m_EnterBattle:
            return None
        iOwnerLinkStatus = dMsgInfo['LinkStatus']
        if iOwnerLinkStatus == LINK_DELEGATE:
            self.DoneSendOwnerAttention()
            self.m_AbilityCon.AIMemberPetDisable()
        elif iOwnerLinkStatus == LINK_ONLINE:
            self.AddSendOwnerAttention()
            self.m_AbilityCon.AIMemberPetEnable()

    
    def OnOwnerTransfer(self, _oPet, oOwner, dMsgInfo):
        if self.CheckTransfer(dMsgInfo):
            self.GotoBornPos()

    
    def OnHeroTriggerGateCtrl(self, oListener, oLevelCtrl, dMsgInfo):
        if self.CheckTransfer(dMsgInfo):
            self.GotoBornPos()

    
    def CheckTransfer(self, dMsgInfo):
        if dMsgInfo['VID'] == self.m_Owner:
            return 1
        return 0

    
    def AddSendOwnerAttention(self):
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_RECEIVEDAM), 'OnReceiveDam', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PERFORM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_PERFORM), 'OnPerformDamage', iSub = self.m_SubAttackMsg, iOnce = 0)

    
    def DoneSendOwnerAttention(self):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'OnReceiveDam')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PERFORM, 'OnPerformDamage')

    
    def OnHeroRoomTrigger(self, oListener, oLevelCtrl, dMsgInfo):
        oVictim = self.m_Game.GetObject(dMsgInfo['VID'])
        if not oVictim or not (oVictim.m_FightType & WARRIOR_HERO):
            return None
        if oVictim.m_ID != self.m_Owner:
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
        if not (self.m_CurLineIdx) or self.m_CurLineIdx[0] != iLevel or self.m_CurLineIdx[1] != iRoomPos:
            self.m_CurLineIdx = (iLevel, iRoomPos)
            self.GotoBornPos()

    
    def OnDealTotalDam(self, _oPet, dMsgInfo):
        iCurVID = dMsgInfo['CurVID']
        if iCurVID == self.m_ID or iCurVID == self.m_Owner:
            return None
        oGame = self.m_Game
        iAttack = self.m_Owner
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return None
        oVictim = oGame.GetObject(iCurVID)
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

    
    def SetLockEnemy(self, iTarget):
        iOldTarget = self.Query('LockEnemy')
        self.Set('LockEnemy', iTarget)
        self.GS2CPropChange('LockEnemy', iTarget)
        if not iOldTarget and iTarget:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_UPDATE_HATE, self, {
                'LockEnemy': iTarget }, iSub = PET_HATE_START)
        elif iOldTarget:
            if not iTarget:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_UPDATE_HATE, self, {
                    'OldTarget': iOldTarget }, iSub = PET_HATE_END)
            elif iOldTarget != iTarget:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_UPDATE_HATE, self, {
                    'OldTarget': iOldTarget,
                    'LockEnemy': iTarget }, iSub = PET_HATE_UPDATE)

    
    def LockEnemy(self):
        return self.Query('LockEnemy', 0)

    
    def MoveStatus(self):
        return self.m_MoveStatusMgr.GetCurStatus()

    
    def FightStatus(self):
        return self.m_FightStatusMgr.GetCurStatus()

    
    def AddPerform(self, iPerform, iLevel, iItem = 0, iEnable = 1):
        oPerform = self.m_Perform.AddPerform(self, iPerform, iLevel, iEnable, iItem)
        if self.CheckPerformType(oPerform):
            self.UpdateMinPerformUseDis(oPerform)
        return oPerform

    
    def RemovePerform(self, iPerform):
        oPerform = self.m_Perform.RemovePerform(self, iPerform)
        if self.CheckPerformType(oPerform):
            self.UpdateMinPerformUseDis()

    
    def UpdateMinPerformUseDis(self, oPerform = None):
        if not self.m_Agent:
            return None
        fMinDis = 999
        if oPerform:
            fMinDis = self.m_Agent.SetDefaultData('MinPerformUseDis', fMinDis)
            fAttDis = oPerform.GetAttDistance()
            if fMinDis > fAttDis:
                self.m_Agent.SetData('MinPerformUseDis', fAttDis)
            return None
        bUpdate = False
        for oPerform in self.m_Perform.GetAllPerform():
            if self.CheckPerformType(oPerform):
                fAttDis = oPerform.GetAttDistance()
                if fMinDis > fAttDis:
                    fMinDis = fAttDis
                    bUpdate = True
        
        if bUpdate:
            self.m_Agent.SetData('MinPerformUseDis', fMinDis)

    
    def CheckPerformType(self, oPerform):
        if not oPerform:
            return False
        if oPerform.m_PFType != PF_TYPE_PETACTIVE:
            return False
        if oPerform.m_PFSubType == PETPF_ACTIVE_SLIP_SPELL:
            return False
        return True

    
    def AddEnableSpell(self, iSpell):
        self.m_EnableSpell.add(iSpell)
        self.RefreshShowSpell()

    
    def RemoveEnableSpell(self, iSpell):
        if iSpell in self.m_EnableSpell:
            self.m_EnableSpell.remove(iSpell)
            self.RefreshShowSpell()

    
    def GetEnableSpell(self):
        return list(self.m_EnableSpell)

    
    def Ability(self):
        return self.m_AbilityCon.GetPerformSIDByType(PF_TYPE_PETABILITY)

    
    def SealedAbility(self):
        return self.m_AbilityCon.GetSealedAbility()

    
    def ActiveAbility(self, setAbility):
        self.m_AbilityCon.ActiveAbility(setAbility, self.m_EnterBattle)
        self.RefreshAbility()

    
    def RefreshAbility(self, dPlayer = None):
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_PetCon:
            oOwner.m_PetCon.GS2CPetAbility(self.m_ID, dPlayer)

    
    def RefreshShowSpell(self, dPlayer = None):
        if self.IsDead():
            return None
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_PetCon:
            oOwner.m_PetCon.GS2CPetShowSpell(self.m_ID)

    
    def GetCurSettleShowData(self):
        dData = {
            'PetSID': self.m_SID,
            'PetAttr': cl_netattr.MakeFinshWarShowAddPacket(self),
            'PetOffset': self.GetAttrOffsetPacketInfo(),
            'PetAbility': self.Ability() }
        return dData

    
    def SetRelifeCheckRadius(self, fRadius):
        self.m_RelifeCheckRadius = fRadius

    
    def GS2CPropChange(self, sAttr, iVal = None):
        if not self.m_InitScene:
            return None
        cl_netattr.GS2CPetPropChange(self, sAttr, iVal)

    
    def ChangeLock(self, iLock):
        self.m_Lock = iLock

    
    def GetLock(self):
        return self.m_Lock

    
    def ResetPetFormulaAttr(self):
        cl_formula.ResetPetFormulaAttr(self, self.m_AttrInfo, BASEATTR_REFRESH)



def SendOwnerMsgByVictimSub(iMsg, oPet, dMsgInfo):
    if 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    else:
        return None
    oGame = oPet.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAttack = oPet.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['OriginalAID'] = dInfo['AID']
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(iMsg, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)
    if iMsg == cl_msgcenter.MSG_WAR_RECEIVEDAM:
        if 'Skill' not in dMsgInfo:
            return None
        dMsgInfo['DamFactor'][OBJ_ATTACK].update(oAttack.GetBaseDamRatio())


def SendKillMsg2Owner(oServant, dMsgInfo):
    if 'VID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['VID']
    if iVictim == oServant.m_ID:
        return None
    oGame = oServant.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAttack = oServant.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['OriginalAID'] = dInfo['AID']
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILL, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)

