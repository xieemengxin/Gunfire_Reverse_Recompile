# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/petcon.pyc
# RelativePath: clientlogic/cl_container/petcon.pyc
# Source Generated with Decompyle++
# File: petcon.pyc (Python 3.6)

from cl_object.logging import PetLog
from cl_only import ChooseKey, Functor, GAME_FRAME, DeepCopy, DEAD_FLAG_REAL, ChooseMulKeys
from cl_commondefines import PET_EGG_NORMAL, PET_EGG_RARE, PET_PUT_WAY_HATCH_NORMAL, PET_PUT_WAY_HATCH_RARE, PET_TYPE_ALL, PET_ENTER_BATTLE, PET_LEAVE_BATTLE, SEASONFUNC_FUSE_PET, LEVEL_TYPE_HIDE, BASEATTR_REFRESH, PET_PUT_WAY_FUSE, PET_HANDLE_RESETFUSE, PET_HANDLE_ACTIVEABILITY, PET_HANDLE_ENDFUSE, PET_HANDLE_FUSE, PET_HANDLE_ONECLICKFUSE, PF_TYPE_PETABILITY, PET_ABILITY_LOW, PET_ABILITY_NORMAL, PET_ABILITY_HIGH, PET_EGG_CANHATCH_NORMAL, PET_EGG_CANHATCH_RARE, PET_HANDLE_ONECLICKACTIVE, PET_HANDLE_SETEGGTYPE, PET_HANDLE_USEACTIVE, PET_HANDLE_RAPIDSCREEN, WARRIOR_PET_MINI
from cl_container.mobject import CBaseSeasonContainer
import cl_duonet.dn_cl_container_petcon as petnet
import cl_msgcenter
import cl_pet
import cl_pet.mobject
import cl_netattr
import cl_formula
import cl_platformdata
import cl_notify
import cl_perform
import time
NEWLEVEL_GROW_ATTR = [
    'HPMax',
    'Att']
PET_MAX_COUNT = 100
ABILITY_MAX_COUNT = 5
ABILITY_MARK_COUNT = 8
FUSE_NO_MAINPET_POS = 0
REPEAT_ABILITY_CHOOSE_CNT = 5
QUALITY_SCORE = {
    PET_ABILITY_LOW: 17,
    PET_ABILITY_NORMAL: 30,
    PET_ABILITY_HIGH: 50 }

def GS2CAddPet(oGame, pid, oPet):
    dInfo = cl_netattr.MakePetShowAddPacket(oPet)
    dOffset = oPet.GetAttrOffsetPacketInfo()
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iPetID': oPet.m_ID,
        'iPetSID': oPet.m_SID,
        'dOffset': dOffset,
        'dInfo': dInfo,
        'lstAbility': oPet.Ability(),
        'lstSealedAbility': oPet.SealedAbility(),
        'iIsNew': oPet.QuerySavedData('IsNew'),
        'iLock': oPet.GetLock() }
    petnet.DN_GS2CAddPet(netData)


def GS2CRemovePet(oGame, pid, iPetID):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iPetID': iPetID }
    petnet.DN_GS2CRemovePet(netData)


def GS2CSetCurPet(oGame, pid, iPetID):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iPetID': iPetID }
    petnet.DN_GS2CSetCurPet(netData)


def GS2CRefreshPetEggNum(oGame, pid, iType, iCount):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iType': iType,
        'iCount': iCount }
    petnet.DN_GS2CRefreshPetEggNum(netData)


def GS2CSetHatchEggType(oGame, pid, iType):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iType': iType }
    petnet.DN_GS2CSetHatchEggType(netData)


def GS2CCompanionPet(oGame, iPetID, dPlayer):
    if not iPetID:
        return None
    netData = {
        'iPetID': iPetID,
        'oGame': oGame,
        'dPlayer': dPlayer }
    petnet.DN_GS2CCompanionPet(netData)


def GS2CPetAbility(oGame, iPetID, lstAbility, lstSealedAbility, dPlayer):
    netData = {
        'iPetID': iPetID,
        'lstAbility': lstAbility,
        'lstSealedAbility': lstSealedAbility,
        'oGame': oGame,
        'dPlayer': dPlayer }
    petnet.DN_GS2CPetAbility(netData)


def GS2CFuseResult(oGame, pid, iResetTimes, iResetCost, iMainPetPos, lstPet):
    netData = {
        'iResetTimes': iResetTimes,
        'iResetCost': iResetCost,
        'iMainPetPos': iMainPetPos,
        'lstPet': lstPet,
        'oGame': oGame,
        'pid': pid }
    petnet.DN_GS2CFuseResult(netData)


def GS2CPetOptionCost(oGame, pid, dOptionCost):
    netData = {
        'dOption': dOptionCost,
        'oGame': oGame,
        'pid': pid }
    petnet.DN_GS2CPetOptionCost(netData)


def GS2CPetAbilityMarkList(oGame, pid, lstAbility):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'lstAbility': lstAbility }
    petnet.DN_GS2CPetAbilityMarkList(netData)


def GS2CPetSpellStart(oGame, pid, iSpellSID):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iSpellSID': iSpellSID }
    petnet.DN_GS2CPetSpellStart(netData)


def GS2CPetShowSpell(oGame, pid, lstSpell):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'lstSpell': lstSpell }
    petnet.DN_GS2CPetSpell(netData)


def GS2CUpdateSealedAbilityProgress(oGame, pid, iPetID, lstAbility):
    netData = {
        'oGame': oGame,
        'iPetID': iPetID,
        'pid': pid,
        'lstAbility': lstAbility }
    petnet.DN_GS2CUpdateSealedAbilityProgress(netData)


def GS2CUpdatePetLock(oGame, pid, iPetID, iLock):
    netData = {
        'oGame': oGame,
        'iPetID': iPetID,
        'pid': pid,
        'iLock': iLock }
    petnet.DN_GS2CUpdatePetLock(netData)


def C2GSSetCurPet(who, iPetID):
    who.m_PetCon.SetCurPet(iPetID, bByClient = True)


def C2GSSetHatchEggType(who, iType):
    who.m_PetCon.SetHatchEggType(iType)


def C2GSUnsetNewPet(who, lstPetID):
    who.m_PetCon.UnsetNewPet(lstPetID)


def C2GSOpenPetBag(who):
    who.m_PetCon.OnOpenBag()


def C2GSPetBagOption(who, iOption, lstAnswer):
    who.m_PetCon.ChooseOption(iOption, lstAnswer)


def C2GSMarkPetAbility(who, iAbility, iMark, iTemplateID):
    if not who.m_PetCon:
        return None
    who.m_PetCon.MarkAbility(iAbility, iMark, iTemplateID)


def C2GSHatchEggNum(who, iNormalEggNum, iRareEggNum):
    who.m_PetCon.HatchEgg(iNormalEggNum, iRareEggNum, 'Click')


def C2GSChangePetLock(who, iPetID, iLock):
    who.m_PetCon.ChangePetLock(iPetID, iLock)

FUSE_MAIN_POS = 0

class CPetContainer(CBaseSeasonContainer):
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_Pet = { }
        self.m_DelayRemovePet = { }
        self.m_CurPet = 0
        self.m_CallFlag = '%d-PetCon' % self.m_Owner
        self.m_Enable = 0
        self.m_PetEggCnt = {
            PET_EGG_CANHATCH_RARE: 0,
            PET_EGG_CANHATCH_NORMAL: 0,
            PET_EGG_RARE: 0,
            PET_EGG_NORMAL: 0 }
        self.m_FuseInfo = { }
        self.m_FuseResult = { }
        self.m_OptionCost = {
            PET_HANDLE_ACTIVEABILITY: 300,
            PET_HANDLE_FUSE: 100 }
        self.m_SingleFuseMaxResetTimes = 2
        self.m_EggPriorType = PET_TYPE_ALL
        self.m_PetReportData = { }
        self.m_LastPet = 0
        self.m_CompanionPet = 0
        self.m_AbilityMarkList = []
        self.m_RecordSeedPet = []
        self.m_Options = {
            PET_HANDLE_RAPIDSCREEN: (self.OnRapidScreen, 0),
            PET_HANDLE_ONECLICKACTIVE: (self.OneClickActive, 0),
            PET_HANDLE_ONECLICKFUSE: (self.OneClickFuse, 2),
            PET_HANDLE_ACTIVEABILITY: (self.ActiveAbility, 1),
            PET_HANDLE_RESETFUSE: (self.ResetFusePet, 0),
            PET_HANDLE_ENDFUSE: (self.EndFusePet, 1),
            PET_HANDLE_FUSE: (self.FusePet, 3) }
        self.m_AbilityTemplate = 0

    
    def Release(self):
        self.DoneAttention()
        for oPet in self.m_FuseResult.values():
            oPet.Remove('Release')
        
        self.m_FuseResult = { }
        for oPet in self.m_Pet.values():
            oPet.Remove('Release')
        
        self.m_Pet = { }
        dDelay = self.m_DelayRemovePet
        self.m_DelayRemovePet = { }
        for iPet in dDelay:
            self.DelayRemovePet(iPet)
        
        self.m_Options = { }
        self.m_CurPet = 0
        self.m_Game = None

    
    def ClearAll(self, sReason):
        self.m_PetEggCnt = {
            PET_EGG_CANHATCH_RARE: 0,
            PET_EGG_CANHATCH_NORMAL: 0,
            PET_EGG_RARE: 0,
            PET_EGG_NORMAL: 0 }
        lstPet = list(self.m_Pet)
        for iPet in lstPet:
            self.RemovePet(iPet, sReason)
        
        self.m_CurPet = 0
        self.m_LastPet = 0
        self.m_CompanionPet = 0
        self.m_RecordSeedPet = []

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Save(self):
        dData = { }
        lstPet = []
        for oPet in self.m_Pet.values():
            dPet = oPet.Save()
            if oPet.m_ID == self.m_CurPet:
                dPet['IsCurPet'] = 1
            if oPet.m_ID == self.m_CompanionPet:
                dPet['IsCompanion'] = 1
            lstPet.append(dPet)
        
        dData['Pet'] = lstPet
        dData['PetEggCnt'] = dict(self.m_PetEggCnt)
        dData['EggPriorType'] = self.m_EggPriorType
        if self.m_FuseInfo:
            dData['FuseInfo'] = DeepCopy(self.m_FuseInfo)
            dFuseResult = { }
            for iIdx, oPet in self.m_FuseResult.items():
                dFuseResult[iIdx] = oPet.Save()
            
            dData['FuseResult'] = dFuseResult
        dData['AbilityMark'] = self.m_AbilityMarkList
        dData['Template'] = self.m_AbilityTemplate
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        if not self.CheckElementIsEnable():
            return None
        oOwner = self.GetOwner()
        for dPet in dData['Pet']:
            oPet = cl_pet.LoadPet(self.m_Game, oOwner, dPet)
            if not oPet:
                PetLog.Error('%d %d load fail %s' % (self.m_Game.m_ID, self.m_PlayerID, dPet))
                continue
            self.m_Pet[oPet.m_ID] = oPet
            if 'IsCurPet' in dPet:
                self.m_CurPet = oPet.m_ID
            if 'IsCompanion' in dPet:
                self.m_CompanionPet = oPet.m_ID
        
        if 'PetEggCnt' in dData:
            self.m_PetEggCnt = dData['PetEggCnt']
        if 'FuseInfo' in dData:
            self.m_FuseInfo = dData['FuseInfo']
            for iIdx, dPet in dData['FuseResult'].items():
                oPet = cl_pet.LoadPet(self.m_Game, oOwner, dPet)
                if not oPet:
                    PetLog.Error('%d %d fuse load fail %s' % (self.m_Game.m_ID, self.m_PlayerID, dPet))
                    continue
                self.m_FuseResult[iIdx] = oPet
            
        self.m_EggPriorType = dData.get('EggPriorType', 0)
        self.m_AbilityMarkList = dData.get('AbilityMark', [])
        if 'Template' in dData:
            self.m_AbilityTemplate = dData['Template']
        if self.m_CurPet:
            self.PetEnterBattle()

    
    def Enable(self, dConfig):
        if self.m_Enable:
            return None
        self.m_Enable = 1
        self.InitAttention()
        self.InitOptionConfig()

    
    def InitAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, sFlag)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnOwnerRelife, sFlag, iOnce = 0)

    
    def DoneAttention(self):
        sFlag = self.m_CallFlag
        oHero = self.GetOwner()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(oHero, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, sFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIFE, sFlag)

    
    def CheckIsFull(self):
        iMaxCount = PET_MAX_COUNT - 1 if self.m_FuseInfo else PET_MAX_COUNT
        if len(self.m_Pet) + sum(self.m_PetEggCnt.values()) >= iMaxCount:
            return True
        return False

    
    def SetCompanionPet(self, dData):
        if not dData:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        if oWarMgr.m_IsUseRecord:
            return None
        if not self.CheckElementIsEnable():
            return None
        oPet = cl_pet.CreateCompanionPet(self.m_Game, self.GetOwner(), dData)
        if not oPet:
            PetLog.Error('%d %d set componion fail %s' % (self.m_Game.m_ID, self.m_PlayerID, dData))
            return None
        self.AddPet(oPet)
        self.m_CompanionPet = oPet.m_ID

    
    def OnStartFight(self, oHero, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_HIDE:
            return None
        for oPet in self.m_Pet.values():
            if oPet.m_ID == self.m_CurPet:
                oPet.ResetPetFormulaAttr()
                continue
            cl_formula.ResetPetFormulaAttr(oPet, oPet.m_AttrInfo, BASEATTR_REFRESH, NEWLEVEL_GROW_ATTR)
        

    
    def OnOwnerRelife(self, oHero, dInfo):
        iDead = dInfo['Dead']
        if iDead != DEAD_FLAG_REAL:
            return None
        if self.m_CurPet == 0:
            return None
        oPet = self.GetCurPet()
        if oPet and not oPet.IsDead():
            self.PetEnterBattle()

    
    def SelfRefresh(self):
        if not self.CheckElementIsEnable():
            return None
        oGame = self.m_Game
        pid = self.m_PlayerID
        for oPet in self.m_Pet.values():
            GS2CAddPet(oGame, pid, oPet)
        
        GS2CSetCurPet(oGame, pid, self.m_CurPet)
        for iType, iCnt in self.m_PetEggCnt.items():
            GS2CRefreshPetEggNum(oGame, pid, iType, iCnt)
        
        self.GS2CCompanionPet(dPlayer = {
            pid: 1 })
        if self.m_EggPriorType:
            GS2CSetHatchEggType(oGame, pid, self.m_EggPriorType)
        if self.m_CurPet:
            self.PetEnterBattle()
        GS2CPetOptionCost(oGame, pid, self.m_OptionCost)
        GS2CPetAbilityMarkList(oGame, pid, self.m_AbilityMarkList)
        self.RefreshCompanionPetInfo()

    
    def Refresh(self, dPlayer):
        self.GS2CCompanionPet(dPlayer)

    
    def GS2CCompanionPet(self, dPlayer):
        GS2CCompanionPet(self.m_Game, self.m_CompanionPet, dPlayer)

    
    def RefreshCompanionPetInfo(self):
        oGame = self.m_Game
        oCompanionPet = oGame.GetObject(self.m_CompanionPet)
        if not oCompanionPet:
            return None
        oAbilityCon = oCompanionPet.m_AbilityCon
        if not oAbilityCon.m_SealedAbility:
            return None
        lstAbility = []
        for iAbility in oAbilityCon.m_SealedAbility:
            iProcess = oAbilityCon.m_SealedActiveProgress[iAbility] if iAbility in oAbilityCon.m_SealedActiveProgress else 0
            lstAbility.append((iAbility, iProcess))
        
        GS2CUpdateSealedAbilityProgress(self.m_Game, self.m_PlayerID, oCompanionPet.m_ID, lstAbility)

    
    def ValidAdd(self, oPet):
        if self.CheckIsFull():
            return 0
        return 1

    
    def AddPet(self, oPet):
        if not self.ValidAdd(oPet):
            PetLog.Alert('%s %s addpet full %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oPet.m_ID, oPet.m_SID))
            cl_notify.SendCommonNotify(self.m_Game, [
                self.m_PlayerID], 9591, { })
            return None
        PetLog.Debug('%d %d add pet %d %d' % (self.m_Game.m_ID, self.m_PlayerID, oPet.m_ID, oPet.m_SID))
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_PET, oHero, {
                'TargetPet': oPet.m_ID })
        self.m_Pet[oPet.m_ID] = oPet
        GS2CAddPet(self.m_Game, self.m_PlayerID, oPet)
        self.OnAddPet(oPet)

    
    def OnAddPet(self, oPet):
        if len(self.m_Pet) == 1:
            self.SetCurPet(oPet.m_ID)

    
    def RemovePet(self, iPetID, sReason = '', iReleasePet = 1):
        if iPetID not in self.m_Pet:
            return None
        oPet = self.m_Pet.pop(iPetID)
        PetLog.Debug('%d %d del pet %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iPetID, oPet.m_SID, sReason))
        if iPetID == self.m_CurPet:
            self.SetLastSettleShowReportData(oPet)
            self.SetCurPet(0)
            if iReleasePet:
                oOwner = self.GetOwner()
                if oOwner:
                    self.m_DelayRemovePet[iPetID] = 1
                    oOwner.Call_Out(Functor(self.DelayRemovePet, iPetID), 10 * GAME_FRAME, 'DelayRemovePet')
                else:
                    PetLog.Alert('%s %s no owner' % (self.m_Game.m_ID, self.m_PlayerID))
                    oPet.Remove(sReason)
            elif iReleasePet:
                oPet.Remove(sReason)
        None(self.m_Game, self.m_PlayerID, iPetID)

    
    def DelayRemovePet(self, iPetID):
        self.m_DelayRemovePet.pop(iPetID, 0)
        oPet = self.m_Game.GetObject(iPetID)
        if oPet:
            oPet.Remove('DelayRemovePet')

    
    def ValidSetCurPet(self, iPetID, bByClient):
        if self.m_CurPet == iPetID:
            return 0
        if iPetID == 0:
            return 1
        if iPetID not in self.m_Pet:
            PetLog.Error('%d %d cur pet not exist %d' % (self.m_Game.m_ID, self.m_PlayerID, iPetID))
            return 0
        if bByClient:
            oPet = self.m_Pet[iPetID]
            if oPet.m_FightType == WARRIOR_PET_MINI and oPet.IsDead():
                PetLog.Alert('%s %s petdie %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iPetID, oPet.Ability()))
                return 0
            if oPet.HP() < oPet.QueryAttr('HPMax'):
                PetLog.Alert('%s %s nohp %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iPetID, oPet.Ability()))
                return 0
        return 1

    
    def SetCurPet(self, iPetID, bByClient = False):
        PetLog.Debug('%s %s set %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_CurPet, iPetID))
        if not self.ValidSetCurPet(iPetID, bByClient):
            return None
        if self.m_CurPet:
            self.PetLeaveBattle()
        self.m_CurPet = iPetID
        if iPetID != 0:
            self.PetEnterBattle()
        GS2CSetCurPet(self.m_Game, self.m_PlayerID, iPetID)

    
    def GetCurPet(self):
        if not self.m_CurPet:
            return None
        return self.m_Game.GetObject(self.m_CurPet)

    
    def GetCompanionPet(self):
        if not self.m_CompanionPet:
            return None
        return self.m_Game.GetObject(self.m_CompanionPet)

    
    def GetLastPet(self):
        if not self.m_LastPet:
            return None
        return self.m_Game.GetObject(self.m_LastPet)

    
    def GetAllPet(self):
        return list(self.m_Pet.values())

    
    def GetPetByID(self, iPet):
        if iPet not in self.m_Pet:
            return None
        return self.m_Pet[iPet]

    
    def UnsetNewPet(self, lstPetID):
        for iPetID in lstPetID:
            if iPetID not in self.m_Pet:
                continue
            oPet = self.m_Pet[iPetID]
            oPet.DelSavedData('IsNew')
        

    
    def GS2CPetShowSpell(self, iPetID):
        if iPetID not in self.m_Pet:
            return None
        oPet = self.m_Pet[iPetID]
        GS2CPetShowSpell(self.m_Game, self.m_PlayerID, oPet.m_EnableSpell)

    
    def GS2CPetSpellStart(self, iPetID, iSpellSID):
        if iPetID not in self.m_Pet:
            return None
        GS2CPetSpellStart(self.m_Game, self.m_PlayerID, iSpellSID)

    
    def PetLeaveBattle(self, iLeaveGame = 0):
        oPet = self.GetCurPet()
        if not oPet:
            return None
        self.m_LastPet = self.m_CurPet
        oPet.LeaveBattle(iLeaveGame)
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SET_CURPET, oHero, {
                'TargetPet': self.m_LastPet }, iSub = PET_LEAVE_BATTLE)
        self.m_CurPet = 0

    
    def PetEnterBattle(self):
        oPet = self.GetCurPet()
        if not oPet:
            return None
        if oPet.m_Scene or oPet.m_EnterBattle:
            return None
        oPet.EnterBattle()
        self.AddSeedPet(oPet.m_ID)
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SET_CURPET, oHero, {
                'TargetPet': oPet.m_ID }, iSub = PET_ENTER_BATTLE)

    
    def RewardPet(self, dPet, iPutWay, dInfo):
        oGame = self.m_Game
        iSID = ChooseKey(oGame, dPet)
        oPet = cl_pet.CreatePet(oGame, self.GetOwner(), iSID, iPutWay, dInfo)
        if not oPet:
            return None
        self.AddPet(oPet)

    
    def CheckElementIsEnable(self):
        oConquerElement = self.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement or not (oConquerElement.m_Enable):
            return False
        return True

    
    def InitOptionConfig(self):
        oConquerElement = self.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement or not (oConquerElement.m_Enable):
            return None
        self.m_OptionCost = {
            PET_HANDLE_ACTIVEABILITY: oConquerElement.m_ActiveAbilityCost,
            PET_HANDLE_FUSE: oConquerElement.m_FuseCost }
        self.m_SingleFuseMaxResetTimes = oConquerElement.m_SingleFuseMaxResetTimes

    
    def GetPetShopTypeWeight(self):
        oConquerElement = self.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement or not (oConquerElement.m_Enable):
            return 10
        return oConquerElement.m_PetShopTypeWeight

    
    def ChooseOption(self, iOption, lstAnswer):
        oHero = self.GetOwner()
        if iOption not in self.m_Options:
            PetLog.Alert('%s %s petcon op err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iOption))
            return None
        (func, iMinLen) = self.m_Options[iOption]
        if len(lstAnswer) < iMinLen:
            PetLog.Alert('%s %s petcon res err %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iOption, lstAnswer))
            return None
        func(lstAnswer)

    
    def OnRapidScreen(self, lstAnswer):
        oHero = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, { }, iSub = PET_HANDLE_RAPIDSCREEN)

    
    def OnOpenBag(self):
        self.GS2CFuseResult()

    
    def GetFuseCost(self):
        return self.m_OptionCost[PET_HANDLE_FUSE]

    
    def FusePet(self, lstAnswer):
        oGame = self.m_Game
        oHero = self.GetOwner()
        oConquerElement = self.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement.ChecKOpenFunc(self.m_Owner, SEASONFUNC_FUSE_PET):
            PetLog.Alert('%s %s closefuse %s err' % (oGame.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        iFuseCost = self.GetFuseCost()
        if oHero.m_WarCash < iFuseCost:
            PetLog.Alert('%s %s fusepet %s cash:%s<%s' % (oGame.m_ID, oHero.m_PlayerID, lstAnswer, oHero.m_WarCash, iFuseCost))
            return None
        iMainPet = lstAnswer[0]
        iDeputyPet = lstAnswer[1]
        if iMainPet == iDeputyPet or self.m_CompanionPet in (iMainPet, iDeputyPet):
            PetLog.Alert('%s %s fuse %s err' % (oGame.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        oMainPet = self.GetPetByID(iMainPet)
        oDeputyPet = self.GetPetByID(iDeputyPet)
        if not oMainPet or not oDeputyPet:
            PetLog.Alert('%s %s fuse %s err' % (oGame.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        if oDeputyPet.GetLock():
            PetLog.Alert('%s %s fuseLockPet %s err' % (oGame.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        if self.m_FuseInfo:
            PetLog.Alert('%s %s repeatfuse %s' % (oGame.m_ID, oHero.m_PlayerID, self.m_FuseInfo))
            self.EndFusePet()
        PetLog.Debug('%s %s fuse %s %s' % (oGame.m_ID, oHero.m_PlayerID, iMainPet, iDeputyPet))
        iHandleFrom = lstAnswer[2]
        dMsgInfo = {
            'MainPet': iMainPet,
            'DeputyPet': iDeputyPet,
            'HandleFrom': iHandleFrom }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, dMsgInfo, iSub = PET_HANDLE_FUSE)
        oHero.AddCash(-self.GetFuseCost(), 'FusePet')
        (self.m_FuseInfo, self.m_FuseResult) = self.InitFuseInfo(oMainPet, oDeputyPet)
        self.RemovePet(iMainPet, 'Fuse', iReleasePet = 0)
        self.RemovePet(iDeputyPet, 'Fuse')
        self.TrueFusePet(iPos = FUSE_MAIN_POS + 1)
        self.TrueFusePet(iPos = FUSE_MAIN_POS + 2)
        self.GS2CFuseResult()

    
    def InitFuseInfo(self, oMainPet, oDeputyPet):
        iFuseNum = oMainPet.QuerySavedData('FuseNum', 0)
        dFusePetConfig = cl_platformdata.GetFusePetConfig()
        iMinOffset = dFusePetConfig['MinOffset']
        iBaseAbilityWeight = dFusePetConfig['BaseAbilityWeight']
        iRepeatAddWeight = dFusePetConfig['RepeatAddWeight']
        iSetCur = 1 if self.m_CurPet in (oMainPet.m_ID, oDeputyPet.m_ID) else 0
        dMinOffset = { }
        for sAttr in cl_pet.mobject.PET_BASE_ATTR:
            dMinOffset[sAttr] = cl_formula.GetFormulaResult(self, iMinOffset, {
                'AllPet': [
                    oMainPet,
                    oDeputyPet],
                'Attr': sAttr })
        
        lstAbility1 = oMainPet.Ability()
        lstAbility2 = oDeputyPet.Ability()
        dAbilityWeight = dict.fromkeys(lstAbility1, iBaseAbilityWeight)
        for iAbility in lstAbility2:
            if iAbility not in dAbilityWeight:
                dAbilityWeight[iAbility] = iBaseAbilityWeight
                continue
            dAbilityWeight[iAbility] += iRepeatAddWeight
        
        iMainPetPos = FUSE_MAIN_POS
        dFuseResult = {
            iMainPetPos: oMainPet }
        oHero = self.GetOwner()
        iMainAbilityLen = len(lstAbility1)
        dFuseInfo = {
            'SID': oMainPet.m_SID,
            'MinOffset': dMinOffset,
            'AbilityWeight': dAbilityWeight,
            'ParentAbilityNum': (iMainAbilityLen, len(lstAbility2)),
            'ResetTimes': oHero.Query('ResetPetTimes', 0),
            'ResetCost': oHero.Query('ResetPetCost', 0),
            'SetCur': iSetCur,
            'InheritableInfo': self.BuildInheritableInfo(oMainPet, oDeputyPet),
            'MainPetPos': iMainPetPos,
            'LastPos': iMainPetPos,
            'Cost': self.GetFuseCost(),
            'HistoryAbility': [
                set(lstAbility1)],
            'MainPetFuseNum': iFuseNum + 1 }
        return (dFuseInfo, dFuseResult)

    
    def TrueFusePet(self, iPos):
        oGame = self.m_Game
        dFuseInfo = self.m_FuseInfo
        iSID = dFuseInfo['SID']
        for iCnt in range(REPEAT_ABILITY_CHOOSE_CNT):
            oPet = cl_pet.CreatePet(oGame, self.GetOwner(), iSID, PET_PUT_WAY_FUSE, dFuseInfo)
            setAbility = set(oPet.Ability())
            lstAbilityHistory = dFuseInfo['HistoryAbility']
            if setAbility in lstAbilityHistory and iCnt < REPEAT_ABILITY_CHOOSE_CNT - 1:
                oPet.Remove('FuseRepeat')
                continue
            if setAbility not in lstAbilityHistory:
                lstAbilityHistory.append(setAbility)
            self.m_FuseResult[iPos] = oPet
            dFuseInfo['LastPos'] = iPos
            return None
        

    
    def ResetFusePet(self, lstAnswer):
        oGame = self.m_Game
        oHero = self.GetOwner()
        dFuseInfo = self.m_FuseInfo
        if not dFuseInfo:
            PetLog.Alert('%s %s resetfuse noinfo' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        dFuseResult = self.m_FuseResult
        if not dFuseResult:
            PetLog.Alert('%s %s resetfuse nores' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        iCost = dFuseInfo['ResetCost']
        if oHero.m_WarCash < iCost:
            PetLog.Alert('%s %s resetfuse cash:%s<%s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_WarCash, iCost))
            return None
        iTimes = dFuseInfo['ResetTimes']
        if iTimes <= 0:
            PetLog.Alert('%s %s resetfuse notimes' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        for iPos in list(dFuseResult):
            if iPos == FUSE_MAIN_POS:
                continue
            oPet = dFuseResult.pop(iPos)
            oPet.Remove('ResetFuse')
        
        oHero.AddCash(-iCost, 'ResetFuse')
        dFuseInfo['ResetTimes'] -= 1
        PetLog.Debug('%s %s resetfuse times:%s' % (oGame.m_ID, oHero.m_PlayerID, iTimes))
        self.TrueFusePet(iPos = FUSE_MAIN_POS + 1)
        self.TrueFusePet(iPos = FUSE_MAIN_POS + 2)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, { }, iSub = PET_HANDLE_RESETFUSE)
        self.GS2CFuseResult()

    
    def EndFusePet(self, lstAnswer = None):
        oGame = self.m_Game
        dFuseInfo = self.m_FuseInfo
        self.m_FuseInfo = { }
        dFuseResult = self.m_FuseResult
        self.m_FuseResult = { }
        if not dFuseResult:
            return None
        oHero = self.GetOwner()
        if not lstAnswer:
            iChosenPos = dFuseInfo['LastPos']
        else:
            iChosenPos = lstAnswer[0]
            if iChosenPos not in dFuseResult:
                PetLog.Alert('%s %s endfuse pos%s err %s' % (oGame.m_ID, oHero.m_PlayerID, iChosenPos, dFuseResult))
                iChosenPos = dFuseInfo['LastPos']
        oChosenPet = dFuseResult.pop(iChosenPos)
        oChosenPet.SetSavedData('FuseNum', dFuseInfo['MainPetFuseNum'])
        PetLog.Debug('%s %s endfuse %s' % (oGame.m_ID, oHero.m_PlayerID, oChosenPet.m_ID))
        for oPet in dFuseResult.values():
            oPet.Remove('EndFuse')
        
        self.AddPet(oChosenPet)
        if dFuseInfo.get('SetCur', 0) and not (self.m_CurPet):
            self.SetCurPet(oChosenPet.m_ID)
            cl_notify.SendCommonNotify(oGame, [
                oHero.m_PlayerID], 9521, { })
        dMsgInfo = {
            'RemainResetTime': dFuseInfo['ResetTimes'],
            'ChosenPos': iChosenPos }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, dMsgInfo, iSub = PET_HANDLE_ENDFUSE)

    
    def OneClickFuse(self, lstAns):
        oGame = self.m_Game
        oHero = self.GetOwner()
        pid = oHero.m_PlayerID
        if not self.m_AbilityMarkList:
            PetLog.Debug('%s %s nomark' % (oGame.m_ID, pid))
            cl_notify.SendCommonNotify(oGame, [
                pid], 9557, { })
            return None
        lstMarkAbility = set(self.m_AbilityMarkList)
        iMainPet = lstAns[0]
        iFuseNum = 2 * (1 + oHero.Query('ResetPetTimes', 0))
        PetLog.Debug('%s %s oneclick %s %s %s' % (oGame.m_ID, pid, iFuseNum, iMainPet, lstMarkAbility))
        if self.m_FuseInfo:
            PetLog.Alert('%s %s repeatoneclick %s' % (oGame.m_ID, oHero.m_PlayerID, self.m_FuseInfo))
            return None
        if iMainPet:
            oMainPet = self.GetPetByID(iMainPet)
        else:
            iMainPet = self.m_CurPet
            oMainPet = self.GetCurPet()
        if not oMainPet:
            PetLog.Debug('%s %s nocurpet' % (oGame.m_ID, pid))
            cl_notify.SendCommonNotify(oGame, [
                pid], 9560, { })
            return None
        if oMainPet.m_ID == self.m_CompanionPet:
            PetLog.Alert('%s %s companion' % (oGame.m_ID, oHero.m_PlayerID))
            cl_notify.SendCommonNotify(oGame, [
                pid], 9565, { })
            return None
        setMainPetMark = set()
        for iAbility in oMainPet.Ability():
            if iAbility in lstMarkAbility:
                setMainPetMark.add(iAbility)
        
        fStart = time.time()
        iCost = self.GetFuseCost()
        iNoCashBreak = 0
        iFuseTimes = 0
        dAbilityQuality = { }
        for iAbility in self.m_AbilityMarkList:
            clsPerform = cl_perform.GetPerformModule(iAbility)
            dAbilityQuality[iAbility] = clsPerform.m_Quality
        
        for iFuseTimes in range(PET_MAX_COUNT):
            if oHero.m_WarCash < iCost:
                PetLog.Debug('%s %s nocash' % (oGame.m_ID, pid))
                if iFuseTimes <= 0:
                    cl_notify.SendCommonNotify(oGame, [
                        pid], 2115, { })
                    return None
                iNoCashBreak = 1
                cl_notify.SendCommonNotify(oGame, [
                    pid], 9562, { })
                break
            lstHas = set(oMainPet.Ability())
            lstTargetAbility = lstMarkAbility - lstHas
            if not lstTargetAbility and len(lstHas) >= ABILITY_MAX_COUNT:
                pass
            bHasAll = not (lstHas - lstMarkAbility)
            if bHasAll:
                PetLog.Debug('%s %s hasall' % (oGame.m_ID, pid))
                if iFuseTimes <= 0:
                    cl_notify.SendCommonNotify(oGame, [
                        pid], 9564, { })
                    return None
                break
            oDeputyPet = self.ChooseQuickFusePet(iMainPet, lstTargetAbility, dAbilityQuality)
            if not oDeputyPet:
                PetLog.Debug('%s %s nopet' % (oGame.m_ID, pid))
                if iFuseTimes <= 0:
                    cl_notify.SendCommonNotify(oGame, [
                        pid], 9558, { })
                    return None
                break
            iMainPet = oMainPet.m_ID
            iDeputyPet = oDeputyPet.m_ID
            oHero.AddCash(-iCost, 'FusePet')
            (self.m_FuseInfo, self.m_FuseResult) = self.InitFuseInfo(oMainPet, oDeputyPet)
            self.RemovePet(iMainPet, 'Fuse', iReleasePet = 0)
            self.RemovePet(iDeputyPet, 'Fuse')
            for j in range(1, iFuseNum + 1):
                idx = FUSE_MAIN_POS + j
                self.TrueFusePet(iPos = idx)
            
            iMaxScore = 0
            iChosenPos = FUSE_MAIN_POS
            for iPos, oPet in self.m_FuseResult.items():
                iScore = 0
                for iAbility in oPet.Ability():
                    if iAbility not in lstMarkAbility:
                        continue
                    iQuality = dAbilityQuality[iAbility]
                    iScore += QUALITY_SCORE[iQuality]
                
                if iScore > iMaxScore:
                    iMaxScore = iScore
                    iChosenPos = iPos
            
            iMainPetFuseNum = self.m_FuseInfo['MainPetFuseNum']
            dFuseResult = self.m_FuseResult
            self.m_FuseResult = { }
            self.m_FuseInfo = { }
            oChosenPet = dFuseResult.pop(iChosenPos)
            for oPet in dFuseResult.values():
                oPet.Remove('EndFuse')
            
            oMainPet = oChosenPet
            oMainPet.SetSavedData('FuseNum', iMainPetFuseNum)
        
        self.CheckOffsetMainPetMark(oMainPet, setMainPetMark)
        fCostTime = time.time() - fStart
        PetLog.Debug('%s %s oneclickend %s %s' % (oGame.m_ID, pid, iFuseTimes, fCostTime))
        self.AddPet(oMainPet)
        self.SetCurPet(oMainPet.m_ID)
        lstResult = self.GetPetFuseInfo({
            FUSE_MAIN_POS: oMainPet })
        iHandleFrom = lstAns[1]
        dMsgInfo = {
            'FuseTimes': iFuseTimes,
            'HandleFrom': iHandleFrom }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, dMsgInfo, iSub = PET_HANDLE_ONECLICKFUSE)
        GS2CFuseResult(self.m_Game, oHero.m_PlayerID, iResetTimes = 0, iResetCost = 0, iMainPetPos = FUSE_MAIN_POS, lstPet = lstResult)
        if not iNoCashBreak:
            cl_notify.SendCommonNotify(oGame, [
                pid], 9563, { })

    
    def CheckOffsetMainPetMark(self, oMainPet, setMainPetMark):
        setAbility = set(oMainPet.Ability())
        setAllready = setAbility & setMainPetMark
        if setAllready != setMainPetMark:
            lstRandom = list(setAbility - setMainPetMark)
            setRest = setMainPetMark - setAllready
            sReason = 'OffsetMainPetMark'
            oAbilityCon = oMainPet.m_AbilityCon
            iOffsetNum = len(setRest)
            if len(lstRandom) > iOffsetNum:
                dRandomWeight = dict.fromkeys(lstRandom, 1)
                lstRandom = ChooseMulKeys(self.m_Game, dRandomWeight, iOffsetNum)
            for iRemove in lstRandom:
                oAbilityCon.RemoveAbility(iRemove, sReason)
            
            for iAdd in setRest:
                oAbilityCon.AddAbility(iAdd, sReason)
            

    
    def ChooseQuickFusePet(self, iMainPet, lstTargetAbility, dAbilityQuality):
        lstOption = []
        for iPet, oPet in self.m_Pet.items():
            if iPet == iMainPet or iPet == self.m_CompanionPet:
                continue
            if oPet.GetLock():
                continue
            lstHas = set(oPet.Ability()) & lstTargetAbility
            if not lstHas:
                continue
            iAbilityNum = len(lstHas)
            dQualityNum = {
                PET_ABILITY_LOW: 0,
                PET_ABILITY_NORMAL: 0,
                PET_ABILITY_HIGH: 0 }
            for iAbility in lstHas:
                iQuality = dAbilityQuality[iAbility]
                dQualityNum[iQuality] += 1
            
            lstArgs = [
                iAbilityNum,
                dQualityNum[PET_ABILITY_HIGH],
                dQualityNum[PET_ABILITY_NORMAL],
                dQualityNum[PET_ABILITY_LOW],
                iPet]
            lstOption.append(lstArgs)
        
        if not lstOption:
            return None
        lstOption = sorted(lstOption, reverse = True)
        iPet = lstOption[0][-1]
        oPet = self.m_Game.GetObject(iPet)
        return oPet

    
    def BuildInheritableInfo(self, oMainPet, oDeputyPet):
        dInheritableInfo = oMainPet.m_AbilityCon.GetAllInheritableInfo()
        for iAbility, dDeputyInfo in oDeputyPet.m_AbilityCon.GetAllInheritableInfo().items():
            if iAbility not in dInheritableInfo:
                dInheritableInfo[iAbility] = dDeputyInfo
                continue
            dInfo = dInheritableInfo[iAbility]
            for sKey, iValue in dDeputyInfo.items():
                if not sKey not in dInfo:
                    if iValue > dInfo[sKey]:
                        dInfo[sKey] = iValue
                        continue
            
        
        return dInheritableInfo

    
    def AddPetEgg(self, iType):
        if self.CheckIsFull():
            PetLog.Debug('%s %s addpetegg %s full' % (self.m_Game.m_ID, self.m_PlayerID, iType))
            return None
        iCnt = self.m_PetEggCnt[iType] + 1
        self.m_PetEggCnt[iType] = iCnt
        GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, iType, iCnt)
        oHero = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_PETEGG, oHero, {
            'EggType': iType })

    
    def ChangeAllEggHatchType(self):
        dEggCnt = self.m_PetEggCnt
        iNormalEggCnt = dEggCnt[PET_EGG_NORMAL]
        iRareEggCnt = dEggCnt[PET_EGG_RARE]
        if iNormalEggCnt <= 0 and iRareEggCnt <= 0:
            return False
        if iNormalEggCnt:
            dEggCnt[PET_EGG_NORMAL] = 0
            dEggCnt[PET_EGG_CANHATCH_NORMAL] += iNormalEggCnt
            GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, PET_EGG_NORMAL, dEggCnt[PET_EGG_NORMAL])
            GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, PET_EGG_CANHATCH_NORMAL, dEggCnt[PET_EGG_CANHATCH_NORMAL])
        if iRareEggCnt:
            dEggCnt[PET_EGG_RARE] = 0
            dEggCnt[PET_EGG_CANHATCH_RARE] += iRareEggCnt
            GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, PET_EGG_RARE, dEggCnt[PET_EGG_RARE])
            GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, PET_EGG_CANHATCH_RARE, dEggCnt[PET_EGG_CANHATCH_RARE])
        return True

    
    def HatchEgg(self, iNormalCnt, iRareCnt, sReason):
        self.HatchEggByType(PET_EGG_CANHATCH_RARE, iRareCnt, sReason)
        self.HatchEggByType(PET_EGG_CANHATCH_NORMAL, iNormalCnt, sReason)

    
    def HatchEggByType(self, iEggType, iHatchCnt, sReason):
        iAddCount = PET_MAX_COUNT - len(self.m_Pet)
        if iAddCount <= 0:
            return None
        if iEggType == PET_EGG_CANHATCH_RARE:
            iPutWay = PET_PUT_WAY_HATCH_RARE
            iSub = PET_EGG_RARE
        elif iEggType == PET_EGG_CANHATCH_NORMAL:
            iPutWay = PET_PUT_WAY_HATCH_NORMAL
            iSub = PET_EGG_NORMAL
        else:
            return None
        iCanHatchCnt = self.m_PetEggCnt[iEggType]
        if iHatchCnt > iCanHatchCnt:
            PetLog.Debug('%s %s hatch %s %s > %s' % (self.m_Game.m_ID, self.m_PlayerID, iEggType, iHatchCnt, iCanHatchCnt))
            iHatchCnt = iCanHatchCnt
        iLoopCnt = min(iAddCount, iHatchCnt)
        if iLoopCnt <= 0:
            return None
        iType = self.m_EggPriorType
        dPet = GetEggWeight(iPutWay, iType)
        if not dPet:
            PetLog.Alert('%s %s hatchegg:%s type:%s no pet' % (self.m_Game.m_ID, self.m_PlayerID, iEggType, iType))
            return None
        oHero = self.GetOwner()
        for _ in range(iLoopCnt):
            self.m_PetEggCnt[iEggType] -= 1
            self.RewardPet(dPet, iPutWay, { })
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HATCH_PET, oHero, {
                'EggPriorType': iType,
                'Reason': sReason }, iSub = iSub)
        
        GS2CRefreshPetEggNum(self.m_Game, self.m_PlayerID, iEggType, self.m_PetEggCnt[iEggType])

    
    def HatchAllEgg(self, sReason):
        self.HatchEgg(self.m_PetEggCnt[PET_EGG_CANHATCH_NORMAL], self.m_PetEggCnt[PET_EGG_CANHATCH_RARE], sReason)

    
    def SetHatchEggType(self, iType):
        self.m_EggPriorType = iType
        oHero = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, {
            'EggPriorType': iType }, iSub = PET_HANDLE_SETEGGTYPE)

    
    def GetActiveAbilityCost(self):
        return self.m_OptionCost[PET_HANDLE_ACTIVEABILITY]

    
    def ActiveAbility(self, lstAnswer):
        oGame = self.m_Game
        oHero = self.GetOwner()
        iCost = self.GetActiveAbilityCost()
        if oHero.m_WarCash < iCost:
            PetLog.Alert('%s %s activepet cash:%s<%s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_WarCash, iCost))
            return None
        oCompanionPet = self.GetCompanionPet()
        if not oCompanionPet:
            PetLog.Alert('%s %s nocompanionpet' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        iCostPetID = lstAnswer[0]
        if iCostPetID == oCompanionPet.m_ID:
            PetLog.Alert('%s %s costpet repeat' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        oCostPet = self.GetPetByID(iCostPetID)
        if not oCostPet:
            PetLog.Alert('%s %s costpet err' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        if oCostPet.GetLock():
            PetLog.Alert('%s %s costLockpet err' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        lstSealedAbility = oCompanionPet.SealedAbility()
        lstCostPetAbility = oCostPet.Ability()
        (dChange, _) = self.GetChangeAbleSealedAbility(lstSealedAbility, lstCostPetAbility)
        setActiveAbility = set(dChange)
        if not setActiveAbility:
            PetLog.Alert('%s %s active err %s %s' % (oGame.m_ID, oHero.m_PlayerID, lstSealedAbility, lstCostPetAbility))
            return None
        oHero.AddCash(-iCost, 'ActiveAbility')
        self.RemovePet(oCostPet.m_ID, 'ActiveAbility')
        oAbilityCon = oCompanionPet.m_AbilityCon
        oAbilityCon.AddSealedActiveProgress(dChange)
        setSealedActive = oAbilityCon.CheckActivatableAbility(setActiveAbility)
        cl_notify.SendCommonNotify(oGame, [
            oHero.m_PlayerID], 9589, { })
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, { }, iSub = PET_HANDLE_USEACTIVE)
        if not setSealedActive:
            return None
        oCompanionPet.ActiveAbility(setSealedActive)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, {
            'VID': oCompanionPet.m_ID,
            'ActiveAbility': setSealedActive }, iSub = PET_HANDLE_ACTIVEABILITY)

    
    def OneClickActive(self, lstAns):
        oGame = self.m_Game
        oHero = self.GetOwner()
        pid = oHero.m_PlayerID
        oCompanionPet = self.GetCompanionPet()
        if not oCompanionPet:
            PetLog.Alert('%s %s oneclick nocompanionpet' % (oGame.m_ID, oHero.m_PlayerID))
            return None
        iCompanionPet = oCompanionPet.m_ID
        oAbilityCon = oCompanionPet.m_AbilityCon
        iCost = self.GetActiveAbilityCost()
        if oHero.m_WarCash < iCost:
            PetLog.Debug('%s %s onclick active end nocash' % (oGame.m_ID, pid))
            cl_notify.SendCommonNotify(oGame, [
                pid], 9576, { })
            return None
        for iActiveTimes in range(PET_MAX_COUNT):
            lstSealedAbility = oCompanionPet.SealedAbility()
            if not lstSealedAbility:
                PetLog.Debug('%s %s oneclick nosealedability' % (oGame.m_ID, oHero.m_PlayerID))
                cl_notify.SendCommonNotify(oGame, [
                    pid], 9577, { })
                break
            (oCostPet, dChange) = self.ChooseActiveAbilityPet(lstSealedAbility)
            if not oCostPet:
                PetLog.Debug('%s %s oneclick nopet' % (oGame.m_ID, oHero.m_PlayerID))
                iChat = 9579 if iActiveTimes <= 0 else 9575
                cl_notify.SendCommonNotify(oGame, [
                    pid], iChat, { })
                break
            if oHero.m_WarCash < iCost:
                PetLog.Debug('%s %s onclick active nocash' % (oGame.m_ID, pid))
                cl_notify.SendCommonNotify(oGame, [
                    pid], 9576, { })
                break
            oHero.AddCash(-iCost, 'OnclickActive')
            setActiveAbility = set(dChange)
            self.RemovePet(oCostPet.m_ID, 'OnclickActive')
            oAbilityCon.AddSealedActiveProgress(dChange)
            setSealedActive = oAbilityCon.CheckActivatableAbility(setActiveAbility)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, { }, iSub = PET_HANDLE_USEACTIVE)
            if setSealedActive:
                oCompanionPet.ActiveAbility(setSealedActive)
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, {
                    'VID': iCompanionPet,
                    'ActiveAbility': setSealedActive }, iSub = PET_HANDLE_ACTIVEABILITY)
        
        PetLog.Debug('%s %s oneclick active end %s' % (oGame.m_ID, pid, iActiveTimes))

    
    def GetChangeAbleSealedAbility(self, lstSealedAbility, lstCostPetAbility):
        dChange = { }
        iHasCnt = 0
        for iCostAbility in lstCostPetAbility:
            clsCostAbility = cl_perform.GetPerformModule(iCostAbility)
            tLimit = clsCostAbility.m_LimitPet
            iQuality = clsCostAbility.m_Quality
            for iSealedAbility in lstSealedAbility:
                clsAbility = cl_perform.GetPerformModule(iSealedAbility)
                if not clsAbility:
                    continue
                bActive = False
                if iCostAbility == iSealedAbility:
                    bActive = True
                elif tLimit and clsAbility.m_LimitPet and iQuality == clsAbility.m_Quality:
                    bActive = True
                if bActive:
                    iHasCnt += 1
                    if iSealedAbility in dChange:
                        dChange[iSealedAbility] += 1
                    else:
                        dChange[iSealedAbility] = 1
                    break
            
        
        return (dChange, iHasCnt)

    
    def ChooseActiveAbilityPet(self, lstSealedAbility):
        iMaxCnt = 0
        oChosenPet = None
        dResChange = { }
        for iPet, oPet in self.m_Pet.items():
            if iPet == self.m_CompanionPet:
                continue
            if iPet == self.m_CurPet:
                continue
            if oPet.GetLock():
                continue
            (dChange, iHasCnt) = self.GetChangeAbleSealedAbility(lstSealedAbility, oPet.Ability())
            if iHasCnt and iHasCnt > iMaxCnt:
                oChosenPet = oPet
                iMaxCnt = iHasCnt
                dResChange = dChange
        
        return (oChosenPet, dResChange)

    
    def GetPetFuseInfo(self, dFuseResult):
        lstInfo = []
        for iPos, oPet in dFuseResult.items():
            dOffset = oPet.GetAttrOffsetPacketInfo()
            dAttr = cl_netattr.MakePetShowAddPacket(oPet)
            lstAbility = oPet.Ability()
            lstInfo.append([
                iPos,
                oPet.m_SID,
                dOffset,
                dAttr,
                lstAbility])
        
        return lstInfo

    
    def MarkAbility(self, iAbility, iMark, iTemplateID):
        clsPerform = cl_perform.GetPerformModule(iAbility)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_PETABILITY:
            PetLog.Alert('%s %s markability %s unexist' % (self.m_Game.m_ID, self.m_PlayerID, iAbility))
            return None
        if iMark:
            if len(self.m_AbilityMarkList) >= ABILITY_MARK_COUNT:
                return None
            if iAbility in self.m_AbilityMarkList:
                return None
            self.m_AbilityMarkList.append(iAbility)
        elif iAbility not in self.m_AbilityMarkList:
            return None
        self.m_AbilityMarkList.remove(iAbility)
        self.m_AbilityTemplate = iTemplateID

    
    def GetAllPetWarReportInfo(self):
        dPetInfo = { }
        for iPet, oPet in self.m_Pet.items():
            if iPet == self.m_CompanionPet:
                continue
            if not oPet.m_Game:
                continue
            dPetInfo[iPet] = oPet.GetWarReportInfo()
        
        dResult = {
            'CurPet': self.m_CurPet,
            'PetInfo': dPetInfo }
        return dResult

    
    def GetReportData(self):
        oPet = self.GetCurPet()
        if not oPet:
            oPet = self.GetLastPet()
        if oPet:
            return oPet.GetCurSettleShowData()
        return self.GetLastSettleShowReportData()

    
    def SetLastSettleShowReportData(self, oPet):
        self.m_PetReportData = oPet.GetCurSettleShowData()

    
    def GetLastSettleShowReportData(self):
        if self.m_PetReportData:
            return self.m_PetReportData
        return {
            'PetSID': 0,
            'PetAttr': {
                'Attr': [] },
            'PetOffset': { },
            'PetAbility': [] }

    
    def GS2CPetAbility(self, iPetID, dPlayer = None):
        if iPetID not in self.m_Pet:
            return None
        oPet = self.m_Pet[iPetID]
        if dPlayer is None:
            if iPetID == self.m_CurPet:
                dPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
            else:
                dPlayer = {
                    self.m_PlayerID: 1 }
        GS2CPetAbility(self.m_Game, iPetID, oPet.Ability(), oPet.SealedAbility(), dPlayer)

    
    def GS2CFuseResult(self):
        if not self.m_FuseResult:
            return None
        oHero = self.GetOwner()
        dFuseInfo = self.m_FuseInfo
        iResetTimes = dFuseInfo['ResetTimes']
        iResetCost = dFuseInfo['ResetCost']
        lstPet = self.GetPetFuseInfo(self.m_FuseResult)
        GS2CFuseResult(self.m_Game, oHero.m_PlayerID, iResetTimes, iResetCost, iMainPetPos = FUSE_MAIN_POS, lstPet = lstPet)

    
    def AddSeedPet(self, iPetID):
        if self.m_RecordSeedPet and self.m_RecordSeedPet[-1] == iPetID:
            return None
        if iPetID in self.m_RecordSeedPet:
            self.m_RecordSeedPet.remove(iPetID)
        self.m_RecordSeedPet.append(iPetID)
        if len(self.m_RecordSeedPet) > 10:
            self.m_RecordSeedPet = self.m_RecordSeedPet[-10:]

    
    def SaveSeed(self):
        dData = { }
        if not self.CheckElementIsEnable():
            return dData
        lstPetData = []
        oGame = self.m_Game
        for iPet in self.m_RecordSeedPet:
            oPet = oGame.GetObject(iPet)
            if not oPet:
                continue
            dPet = oPet.Save()
            if iPet == self.m_CurPet:
                dPet['IsCurPet'] = 1
            if iPet == self.m_CompanionPet:
                dPet['IsCompanion'] = 1
            lstPetData.append(dPet)
        
        dData['Pet'] = lstPetData
        return dData

    
    def LoadSeed(self, dData):
        if not dData:
            return None
        oOwner = self.GetOwner()
        if not self.CheckElementIsEnable():
            cl_notify.InternalTips(oOwner, '未进入第三赛季战场，加载妖灵失败！')
            return None
        lstPetData = dData['Pet']
        if not isinstance(lstPetData, list):
            cl_notify.InternalTips(oOwner, '数据格式有更改，当前种子无法加载妖灵！')
            return None
        self.ClearAll('LoadSeed')
        for dPet in lstPetData:
            oPet = cl_pet.LoadPet(self.m_Game, oOwner, dPet)
            if not oPet:
                PetLog.Error('%d %d load fail %s' % (self.m_Game.m_ID, self.m_PlayerID, dPet))
                continue
            self.AddPet(oPet)
            if 'IsCurPet' in dPet:
                self.SetCurPet(oPet.m_ID)
            if 'IsCompanion' in dPet:
                self.m_CompanionPet = oPet.m_ID
        

    
    def ChangePetLock(self, iPetID, iLock):
        oPet = self.GetPetByID(iPetID)
        if not oPet:
            return None
        if iLock == oPet.GetLock():
            return None
        oPet.ChangeLock(iLock)
        GS2CUpdatePetLock(self.m_Game, self.m_PlayerID, iPetID, iLock)

    
    def NeedCreateSeed(self):
        return 0



def GetEggWeight(iPutWay, iFightType):
    dFightTypePut = cl_platformdata.GetRareEggPut() if iPutWay == PET_PUT_WAY_HATCH_RARE else cl_platformdata.GetNormalEggPut()
    if iFightType in dFightTypePut:
        return dFightTypePut[iFightType]
    return { }

