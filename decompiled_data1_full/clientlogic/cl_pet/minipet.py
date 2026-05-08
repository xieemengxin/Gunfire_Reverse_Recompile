# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_pet/minipet.pyc
# RelativePath: clientlogic/cl_pet/minipet.pyc
# Source Generated with Decompyle++
# File: minipet.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, WARRIOR_PET_MINICLONE, PET_HANDLE_ACTIVEABILITY, DAM_TYPE_SCENE, DAM_USE_HP, STATUS_JUMP, PF_SUBMSG_PETACTIVE, LEVEL_TYPE_HIDE
from cl_propdata import PC_SEND_SBC, PC_SEND_SELF
from cl_object.logging import PetLog
from . import mobject
import cl_formula
import cl_netattr
import cl_facectrl
import cl_msgcenter
import cl_monster.monsterstatus
import cl_modeldefine
import cl_platformdata
import cl_betree
import cl_object
MINIPET_PERFORM_INIT = 50706
NOTRANSMIT_PERFORM_LIST = [
    50706]
PET_PERFORM_INIT = 50701

class CMiniPet(mobject.CPet):
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_Clone = { }
        self.m_MaxCloneNum = 1
        self.m_WaitRemove = { }

    
    def SetMaxClone(self, iNum):
        self.m_MaxCloneNum = iNum
        cl_netattr.GS2CPetPropChange(self, 'MaxCloneNum', iNum)

    
    def OnCreated(self):
        self.m_PropChangeBCType = PC_SEND_SELF
        self.InitWarValue()
        self.m_HP = self.QueryAttr('HPMax')
        self.m_Speed = self.QueryAttr('MoveSpeed')
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)
        self.m_MoveStatusMgr = cl_monster.monsterstatus.CMoveStatusMgr(self)
        self.m_FightStatusMgr = cl_monster.monsterstatus.CFightStatusMgr(self)
        (self.m_PreDodgeTime, self.m_DodgeTime, self.m_PostDodgeTime) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Dodge')
        self.RemoveAgent()
        self.m_Agent.PauseAgent('MiniPet')

    
    def CreateClone(self, tPos = None, sReason = ''):
        if not self.m_EnterBattle:
            return None
        oGame = self.m_Game
        iCloneNum = len(self.m_Clone)
        if iCloneNum >= self.m_MaxCloneNum:
            return None
        iPetSID = self.m_SID
        clsData = cl_platformdata.GetPetClass(iPetSID)
        nid = oGame.NewNPCID()
        oClonePet = CMiniClonePet(oGame, nid)
        oOwner = self.GetOwner()
        oClonePet.SetOwner(oOwner)
        oClonePet.InitPetData(self, clsData)
        oClonePet.m_Agent.PauseAgent('LeaveScene')
        cl_formula.ResetPetFormulaAttr(oClonePet, self.m_AttrInfo, BASEATTR_REFRESH)
        oClonePet.SetCtrlModelData()
        for iPerform, iLevel in self.m_Perform.GetAllPerformLevel().items():
            if iPerform in NOTRANSMIT_PERFORM_LIST:
                continue
            oClonePet.AddPerform(iPerform, iLevel)
        
        oClonePet.AddPerform(PET_PERFORM_INIT, 1)
        oHpMaxAttr = self.GetAttr('HPMax')
        oClonePet.m_HP = oHpMaxAttr.GetBaseAttr()
        oMoveSpeedAttr = self.GetAttr('MoveSpeed')
        oClonePet.m_Speed = oMoveSpeedAttr.GetBaseAttr()
        oClonePet.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(oClonePet)
        oClonePet.m_MoveStatusMgr = cl_monster.monsterstatus.CMoveStatusMgr(oClonePet)
        oClonePet.m_FightStatusMgr = cl_monster.monsterstatus.CFightStatusMgr(oClonePet)
        (oClonePet.m_PreDodgeTime, oClonePet.m_DodgeTime, oClonePet.m_PostDodgeTime) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Dodge')
        oClonePet.InitAttention()
        oAbilityCon = oClonePet.m_AbilityCon
        for iAbility in self.m_AbilityCon.GetAllPerformSID():
            oAbilityCon.AddAbility(iAbility, 'FollowOwnerPet')
        
        oClonePet.m_AbilityCon.AllPerformEnable()
        oClonePet.GotoBornPos(tPos = tPos)
        self.m_Clone[oClonePet.m_ID] = 1
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_MINICLONE, oOwner, {
            'ClonePet': oClonePet.m_ID,
            'Reason': sReason })

    
    def InitAttention(self):
        if not self.m_Owner:
            return None
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OwnerEnterScene, 'OwnerEnterScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OwnerLeaveScene, 'OwnerLeaveScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, self.OwnerDieDist, 'OnMiniOwnerDieDist')

    
    def ReleaseAttention(self):
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, 'OwnerEnterScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, 'OnMiniOwnerDieDist')

    
    def Release(self):
        self.ClonePetRelease()
        super().Release()

    
    def ClonePetRelease(self):
        oGame = self.m_Game
        dRemovePet = { }
        dRemovePet.update(self.m_Clone)
        dRemovePet.update(self.m_WaitRemove)
        for iClonePet in dRemovePet:
            oClonePet = oGame.GetObject(iClonePet)
            if not oClonePet:
                continue
            oClonePet.Remove('ClonePetRelease')
        

    
    def GotoBornPos(self, tPos = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        vPos = (10000, 10000, 10000)
        if iScene == self.m_Scene:
            self.WalkTo(vPos)
        else:
            self.Goto(iScene, vPos)

    
    def EnterBattle(self):
        self.m_PropChangeBCType = PC_SEND_SBC
        self.GotoBornPos()
        self.OnEnterBattle()
        self.m_EnterBattle = 1
        self.CreateClone(sReason = 'EnterBattle')

    
    def LeaveBattle(self, iLeaveGame = 0):
        self.LeaveScene(0)
        self.m_PropChangeBCType = PC_SEND_SELF
        self.OnLeaveBattle()
        self.m_EnterBattle = 0
        self.CloneLeaveScene()

    
    def ActiveAbility(self, setAbility):
        super().ActiveAbility(setAbility)
        oGame = self.m_Game
        for iClonePet in self.m_Clone:
            oClonePet = oGame.GetObject(iClonePet)
            if oClonePet:
                oClonePet.OnOwnerPetActiveAbility(setAbility)
        

    
    def CloneLeaveScene(self):
        oGame = self.m_Game
        for iClonePet in self.m_Clone:
            oClonePet = oGame.GetObject(iClonePet)
            if not oClonePet:
                continue
            if oClonePet.m_Agent:
                oClonePet.m_Agent.HaltPerform(oClonePet.m_Agent)
                oClonePet.m_Agent.PauseAgent('CloneLeaveScene')
            oClonePet.Stop()
            oClonePet.LeaveScene(0)
            oClonePet.ReleaseAttention()
            oClonePet.m_AbilityCon.AllPerformDisable()
            self.m_WaitRemove[iClonePet] = 1
            oClonePet.DieRemove()
        
        self.m_Clone = { }

    
    def OwnerDieDist(self, _oPet, oOwner, _dMsgInfo):
        self.LeaveBattle()

    
    def OnRelife(self):
        super().OnRelife()
        self.CreateClone()

    
    def ResetPetFormulaAttr(self):
        super().ResetPetFormulaAttr()
        oGame = self.m_Game
        for iClonePet in self.m_Clone:
            oClonePet = oGame.GetObject(iClonePet)
            if not oClonePet:
                continue
            cl_formula.ResetPetFormulaAttr(oClonePet, oClonePet.m_AttrInfo, BASEATTR_REFRESH)
        



class CMiniClonePet(mobject.CPet):
    m_Delete = 1
    m_FightType = WARRIOR_PET_MINICLONE
    m_OwnerPet = 0
    
    def InitPetData(self, oPet, clsData):
        self.m_SID = oPet.m_SID
        self.m_OwnerPet = oPet.m_ID
        self.m_MonsterDataSID = oPet.m_MonsterDataSID
        self.m_Name = oPet.m_Name
        self.m_Shape = oPet.m_Shape
        self.m_PetType = oPet.m_PetType
        self.m_Quality = oPet.m_Quality
        self.SetSide(oPet.m_Side)
        self.m_AttPerform = oPet.m_AttPerform
        self.m_AbilityGroup = oPet.m_AbilityGroup
        self.m_AttrInfo = dict(oPet.m_AttrInfo)
        self.m_OffsetRange = dict(oPet.m_OffsetRange)
        self.m_AttrOffset = dict(oPet.m_AttrOffset)
        self.m_RunSpeedUpMul = oPet.m_RunSpeedUpMul
        self.m_SprintSpeedUpMul = oPet.m_SprintSpeedUpMul
        self.m_HateFactor = oPet.m_HateFactor
        self.m_BaseHate = oPet.m_BaseHate
        self.m_HateDisEff = { }
        self.m_HateDisEff.update(oPet.m_HateDisEff)
        dAllAIConfig = { }
        dAllAIConfig.update(oPet.m_Agent.m_Config)
        self.m_Agent = cl_betree.InitFsmAI(self, 'cl_betree.servantagent', clsData.m_Betree, dAllAIConfig)
        self.m_AttrGrowth = oPet.m_AttrGrowth
        self.m_ShareSpell = set()

    
    def InitAttention(self):
        super().InitAttention()
        if not self.m_Owner:
            return None
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIE, self.OnMiniPetDie, 'OnMiniPetDie', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, self.OnMiniPetPassiveSpellSetCD, 'OnMiniPetPassiveSpellSetCD', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPetActiveStart, 'OnPetActiveStart', iSub = PF_SUBMSG_PETACTIVE, iOnce = 0)

    
    def ReleaseAttention(self):
        super().ReleaseAttention()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DIE, 'OnMiniPetDie')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, 'OnMiniPetPassiveSpellSetCD')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PERFORM_START, 'OnPetActiveStart', iSub = PF_SUBMSG_PETACTIVE)

    
    def OnOwnerPetActiveAbility(self, setSealedActive):
        for iSealedActive in setSealedActive:
            self.m_AbilityCon.AddAbility(iSealedActive, 'FollowOwnerPet', iEnable = 1)
        

    
    def OnMiniPetPassiveSpellSetCD(self, _oPet, dMsgInfo):
        oOwnerPet = self.m_Game.GetObject(self.m_OwnerPet)
        if oOwnerPet:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, oOwnerPet, dMsgInfo, iSub = -1)

    
    def OnPetActiveStart(self, _oPet, dMsgInfo):
        oOwnerPet = self.m_Game.GetObject(self.m_OwnerPet)
        if oOwnerPet:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_START, oOwnerPet, dMsgInfo, iSub = PF_SUBMSG_PETACTIVE)

    
    def OnMiniPetDie(self, _oPet, dMsgInfo):
        self.ReleaseAttention()
        self.m_AbilityCon.AllPerformDisable()
        oGame = self.m_Game
        oOwnerPet = oGame.GetObject(self.m_OwnerPet)
        if oOwnerPet:
            if self.m_ID in oOwnerPet.m_Clone:
                oOwnerPet.m_Clone.pop(self.m_ID)
            oOwner = self.GetOwner()
            if oOwner:
                if self.m_MoveCtrl and self.m_MoveCtrl.m_CurStatus == STATUS_JUMP:
                    tPos = self.m_MoveCtrl.m_JumpStart
                else:
                    tPos = self.GetPos()
                dMsgInfo = {
                    'DieClonePet': self.m_ID,
                    'DiePos': tPos }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MINICLONE_DIE, oOwner, dMsgInfo)
            oOwnerPet.m_WaitRemove[self.m_ID] = 1
            if not oOwnerPet.m_Clone:
                oReason = cl_object.reason.CStrReason('AllCloneDie', None, {
                    'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
                oOwnerPet.HPDirectModify('HP', 0, -(oOwnerPet.m_HP), oReason)

    
    def Remove(self, sReason):
        oGame = self.m_Game
        oOwnerPet = oGame.GetObject(self.m_OwnerPet)
        if oOwnerPet and self.m_ID in oOwnerPet.m_WaitRemove:
            oOwnerPet.m_WaitRemove.pop(self.m_ID)
        super().Remove(sReason)

    
    def AddShareSpell(self, iSpell):
        oOwnerPet = self.m_Game.GetObject(self.m_OwnerPet)
        if not oOwnerPet or not oOwnerPet.GetPerform(iSpell):
            return None
        self.m_ShareSpell.add(iSpell)
        self.AddEnableSpell(iSpell)

    
    def RemoveShareSpell(self, iSpell):
        if iSpell not in self.m_ShareSpell:
            return None
        self.m_ShareSpell.remove(iSpell)
        self.RemoveEnableSpell(iSpell)

    
    def AddEnableSpell(self, iSpell):
        self.m_EnableSpell.add(iSpell)
        oOwnerPet = self.m_Game.GetObject(self.m_OwnerPet)
        if oOwnerPet and iSpell not in oOwnerPet.m_EnableSpell:
            oOwnerPet.AddEnableSpell(iSpell)

    
    def RemoveEnableSpell(self, iSpell):
        if iSpell in self.m_EnableSpell:
            self.m_EnableSpell.remove(iSpell)


