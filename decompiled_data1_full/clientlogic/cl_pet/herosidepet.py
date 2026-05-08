# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_pet/herosidepet.pyc
# RelativePath: clientlogic/cl_pet/herosidepet.pyc
# Source Generated with Decompyle++
# File: herosidepet.pyc (Python 3.6)

from cl_propdata import PC_SEND_SBC, PC_SEND_SELF
from cl_commondefines import BASEATTR_REFRESH, LINK_DELEGATE, LINK_ONLINE, LINK_QUIT
from cl_object.logging import PetLog
from cl_warrior import CWarrior
from cl_only import Functor
from . import mobject
import cl_formula
import cl_msgcenter

class CHeroSidePet(mobject.CPet):
    m_Delete = 1
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_PetSkillInfo = { }

    
    def InitPet(self, iPutWay, dAddData):
        oGame = self.m_Game
        for sAttr in mobject.PET_BASE_ATTR:
            self.m_AttrOffset[sAttr] = 0
            if sAttr in dAddData and sAttr in self.m_AttrInfo:
                iInitVal = dAddData[sAttr]
                if iInitVal:
                    self.m_AttrInfo[sAttr] = iInitVal
        
        self.Set('Scale', 100)
        cl_formula.ResetPetFormulaAttr(self, self.m_AttrInfo, BASEATTR_REFRESH)
        self.m_PetSkillInfo = dAddData
        self.SetSavedData('IsNew', 1)
        PetLog.Debug('%s %s init heroside pet %s-%s putway:%s' % (oGame.m_ID, self.m_OwnerPlayerID, self.m_ID, self.m_SID, iPutWay))

    
    def Remove(self, sReason):
        super().Remove(sReason)

    
    def InitAttention(self):
        super().InitAttention()
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIEDIST, self.OnDieDist, 'OnDieDist', iOnce = 0)

    
    def ReleaseAttention(self):
        super().ReleaseAttention()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DIEDIST, 'OnDieDist')

    
    def NetAddTo(self, dPlayer):
        CWarrior.NetAddTo(self, dPlayer)

    
    def OnDieDist(self, _oPet, dMsgInfo):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oHeroSidePetCon = oOwner.m_HeroSidePetCon
        if not oHeroSidePetCon:
            return None
        oHeroSidePetCon.RemoveHeroSidePet(_oPet.m_ID, sReason = 'DieDist')

    
    def OnRelife(self):
        CWarrior.OnRelife(self)
        if self.m_MoveCtrl:
            self.m_MoveCtrl.E_Enable()

    
    def OwnerChangeLinkStatus(self, _oPet, oOwner, dMsgInfo):
        iOwnerLinkStatus = dMsgInfo['LinkStatus']
        if self.m_EnterBattle:
            if iOwnerLinkStatus == LINK_DELEGATE:
                self.DoneSendOwnerAttention()
            elif iOwnerLinkStatus == LINK_ONLINE:
                self.AddSendOwnerAttention()
        if iOwnerLinkStatus == LINK_QUIT:
            sReason = 'ownerquit'
            PetLog.Debug('%s %s owner quit %s-%s %s' % (self.m_Game.m_ID, self.m_OwnerPlayerID, self.m_ID, self.m_SID, sReason))
            oHeroSidePetCon = oOwner.m_HeroSidePetCon
            if not oHeroSidePetCon or not oHeroSidePetCon.RemoveHeroSidePet(self.m_ID, sReason = sReason, iDieRemove = 0):
                self.Remove(sReason)

    
    def AddSendOwnerAttention(self):
        super().AddSendOwnerAttention()
        if 'WeaponCreate' in self.m_PetSkillInfo and self.m_PetSkillInfo['WeaponCreate']:
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DP, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_DP), 'OnAttack', iOnce = 0)
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_WEAPONFIRE, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_WEAPONFIRE), 'OnWeaponFire', iOnce = 0)
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_ATTACK, Functor(mobject.SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_ATTACK), 'OnAttack', iOnce = 0)

    
    def EnterBattle(self):
        self.m_PropChangeBCType = PC_SEND_SBC
        self.GotoBornPos()
        self.AddAgent()
        self.OnEnterBattle()
        self.m_EnterBattle = 1

    
    def LeaveBattle(self, iLeaveGame = 0):
        self.LeaveScene(0)
        self.m_PropChangeBCType = PC_SEND_SELF
        self.RemoveAgent()
        self.OnLeaveBattle()
        self.m_EnterBattle = 0

    
    def GotoBornPos(self, tPos = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        if not tPos:
            tOwnerPos = oOwner.GetPos()
            if tOwnerPos:
                tPos = tOwnerPos
            else:
                tPos = (10000, 10000, 10000)
        if iScene == self.m_Scene:
            self.WalkTo(tPos)
        else:
            self.Goto(iScene, tPos)



def SendOwnerMsg(iMsg, oPet, dMsgInfo):
    oGame = oPet.m_Game
    oAttack = oPet.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(iMsg, oAttack, dMsgInfo, oGame = oGame)

