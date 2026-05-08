# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/herosidepetcon.pyc
# RelativePath: clientlogic/cl_container/herosidepetcon.pyc
# Source Generated with Decompyle++
# File: herosidepetcon.pyc (Python 3.6)

from cl_object.logging import PetLog
from cl_only import DEAD_FLAG_REAL
from cl_commondefines import PET_ENTER_BATTLE
import cl_msgcenter
import cl_pet
import cl_pet.mobject
HEROSIDEPET_MAX_COUNT = 100

class CHeroSidePetContainer(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.m_Game = oGame
        self.m_HeroSidePet = { }
        self.m_CallFlag = '%d-HeroSidePetCon' % self.m_Owner
        self.m_PetSource = { }
        self.InitAttention()

    
    def Release(self):
        self.DoneAttention()
        self.ClearAll('Release')
        self.m_Game = None

    
    def ClearAll(self, sReason):
        lstPet = list(self.m_HeroSidePet)
        self.FixPetSource()
        for iPet in lstPet:
            self.RemoveHeroSidePet(iPet, sReason = sReason, iDieRemove = 0)
            self.m_PetSource.pop(iPet, '')
        
        self.m_HeroSidePet = { }

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Save(self):
        dData = { }
        lstPet = []
        for oPet in self.m_HeroSidePet.values():
            dPet = oPet.Save()
            lstPet.append(dPet)
        
        dData['HSP'] = lstPet
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        oOwner = self.GetOwner()
        for dPet in dData['HSP']:
            oPet = cl_pet.LoadPet(self.m_Game, oOwner, dPet)
            if not oPet:
                PetLog.Error('%d %d load herosidepet fail %s' % (self.m_Game.m_ID, self.m_PlayerID, dPet))
                continue
            self.m_HeroSidePet[oPet.m_ID] = oPet
            if oPet.m_Scene or oPet.m_EnterBattle:
                continue
            oPet.EnterBattle()
        

    
    def InitAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnOwnerReLife, sFlag, iOnce = 0)

    
    def DoneAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIFE, sFlag)

    
    def OnOwnerReLife(self, oHero, dInfo):
        iDead = dInfo['Dead']
        if iDead != DEAD_FLAG_REAL:
            return None
        for oPet in self.m_HeroSidePet.values():
            if not oPet.IsDead():
                oPet.EnterBattle()
        

    
    def SelfRefresh(self):
        for oPet in self.m_HeroSidePet.values():
            if not oPet.IsDead():
                oPet.EnterBattle()
        

    
    def ValidAdd(self):
        if len(self.m_HeroSidePet) >= HEROSIDEPET_MAX_COUNT:
            return 0
        return 1

    
    def AddHeroSidePet(self, oPet, sReason = ''):
        if not self.ValidAdd():
            PetLog.Alert('%s %s addherosidepet full %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oPet.m_ID, oPet.m_SID))
            return None
        PetLog.Debug('%d %d add heroside pet %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, oPet.m_ID, oPet.m_SID, sReason))
        iPet = oPet.m_ID
        self.m_HeroSidePet[iPet] = oPet
        self.FixPetSource()
        self.m_PetSource[iPet] = sReason
        oPet.EnterBattle()
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, oHero, {
                'TargetPet': oPet.m_ID }, iSub = PET_ENTER_BATTLE)

    
    def RemoveHeroSidePet(self, iPetID, sReason = '', iDieRemove = 1):
        if iPetID not in self.m_HeroSidePet:
            return False
        oPet = self.m_HeroSidePet.pop(iPetID)
        self.FixPetSource()
        self.m_PetSource.pop(iPetID, '')
        PetLog.Debug('%d %d del heroside pet %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iPetID, oPet.m_SID, sReason))
        if iDieRemove:
            oPet.DieRemove()
        else:
            oPet.Remove(sReason)
        return True

    
    def GetHeroSidePet(self):
        return self.m_HeroSidePet

    
    def GetHeroSidePetByID(self, iPet):
        if iPet not in self.m_HeroSidePet:
            return None
        return self.m_HeroSidePet[iPet]

    
    def GetHeroSidePetBySID(self, iPetSID):
        for oPet in self.m_HeroSidePet.values():
            if oPet.m_SID == iPetSID:
                return oPet
        

    
    def GetHeroSidePetBySource(self, sSource):
        self.FixPetSource()
        lstPet = []
        for iPet, sPetSource in self.m_PetSource.items():
            if sSource != sPetSource:
                continue
            lstPet.append(iPet)
        
        return lstPet

    
    def FixPetSource(self):
        if not hasattr(self, 'm_PetSource'):
            self.m_PetSource = { }


