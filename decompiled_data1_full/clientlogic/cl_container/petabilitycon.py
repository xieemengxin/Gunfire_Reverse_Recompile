# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/petabilitycon.pyc
# RelativePath: clientlogic/cl_container/petabilitycon.pyc
# Source Generated with Decompyle++
# File: petabilitycon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_PETABILITY, PF_TYPE_PETABILITY, PET_ABILITY_NORMAL, PET_PUT_WAY_FUSE, PET_PUT_WAY_HATCH_RARE, PET_ABILITY_HIGH, PET_ABILITY_LOW
from cl_only import ChooseKey, DeepCopy
from cl_object.logging import PetLog
from cl_container.petcon import GS2CUpdateSealedAbilityProgress, ABILITY_MAX_COUNT
import cl_container.performcon
import cl_perform
import cl_msgcenter
import cl_platformdata
import cl_formula
REASON_INIT = 'init'
REASON_LOAD = 'load'
REASON_FUSE = 'fuse'
REASON_SEALED = 'sealed'
dQualityToActive = {
    PET_ABILITY_HIGH: 3,
    PET_ABILITY_NORMAL: 3,
    PET_ABILITY_LOW: 3 }

class CPetAbilityContainer(cl_container.performcon.CPerformContainer):
    m_BagType = BAG_TYPE_PETABILITY
    m_Flag = 'PetAbilityCon'
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_ExcludeAbility = set()
        self.m_SealedAbility = []
        self.m_SealedActiveProgress = { }
        self.m_InheritableInfo = { }

    
    def Refresh(self, dPlayer = None):
        pass

    
    def Save(self):
        dData = super().Save()
        dData['IA'] = self.GetAllInheritableInfo()
        dData['SA'] = list(self.m_SealedAbility)
        dData['SAS'] = DeepCopy(self.m_SealedActiveProgress)
        return dData

    
    def Load(self, dData):
        self.m_InheritableInfo = dData.get('IA', { })
        self.m_SealedAbility = dData.get('SA', [])
        self.m_SealedActiveProgress = dData.get('SAS', { })
        for iAbility in dData.get('PF', { }):
            self.AddAbility(iAbility, REASON_LOAD)
        

    
    def SetSealedAbility(self, lstAbility):
        self.m_SealedAbility = lstAbility

    
    def GetSealedAbility(self):
        return list(self.m_SealedAbility)

    
    def AddSealedActiveProgress(self, dChange):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        PetLog.Debug('%s %s %s addseale progress %s' % (self.m_Game.m_ID, self.m_Owner, oOwner.m_OwnerPlayerID, dChange))
        lstAbility = []
        for iAbility, iValue in dChange.items():
            if iAbility not in self.m_SealedActiveProgress:
                self.m_SealedActiveProgress[iAbility] = iValue
            else:
                self.m_SealedActiveProgress[iAbility] += iValue
            lstAbility.append((iAbility, self.m_SealedActiveProgress[iAbility]))
        
        GS2CUpdateSealedAbilityProgress(self.m_Game, oOwner.m_OwnerPlayerID, oOwner.m_ID, lstAbility)

    
    def CheckActivatableAbility(self, setActiveAbility):
        setSealedActive = set()
        for iAbility in setActiveAbility:
            if iAbility not in self.m_SealedActiveProgress:
                continue
            clsActive = cl_perform.GetPerformModule(iAbility)
            if clsActive.m_Quality not in dQualityToActive:
                PetLog.Alert('%s no ability quality in map %s' % (self.m_Game.m_ID, clsActive.m_Quality))
                continue
            iProgress = self.m_SealedActiveProgress[iAbility]
            if iProgress >= dQualityToActive[clsActive.m_Quality]:
                setSealedActive.add(iAbility)
        
        return setSealedActive

    
    def ActiveAbility(self, setAbility, iEnable):
        for iAbility in setAbility:
            self.m_SealedAbility.remove(iAbility)
            self.AddAbility(iAbility, REASON_SEALED, iEnable = iEnable)
        

    
    def GetAllInheritableInfo(self):
        return DeepCopy(self.m_InheritableInfo)

    
    def SetInheritableInfo(self, iAbility, sKey, iVal):
        if iAbility not in self.m_Perform:
            return None
        dInfo = self.m_InheritableInfo.setdefault(iAbility, { })
        dInfo[sKey] = iVal

    
    def QueryInheritableInfo(self, iAbility, sKey):
        if iAbility not in self.m_InheritableInfo:
            return 0
        if sKey not in self.m_InheritableInfo[iAbility]:
            return 0
        return self.m_InheritableInfo[iAbility][sKey]

    
    def RemoveInheritableInfo(self, iAbility, sKey):
        if iAbility not in self.m_InheritableInfo:
            return None
        self.m_InheritableInfo[iAbility].pop(sKey, 0)

    
    def GetAbilityWeight(self, iAbility):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if not ValidAddAbility(oOwner.m_SID, iAbility, self.m_Perform, self.m_ExcludeAbility):
            return 0
        for iGroup in oOwner.m_AbilityGroup:
            dGroupWeight = cl_platformdata.GetPetAbilityGroup(iGroup)
            if iAbility in dGroupWeight:
                return dGroupWeight[iAbility]
        
        clsAbility = cl_perform.GetPerformModule(iAbility)
        return clsAbility.m_Weight

    
    def InitAbility(self, iPutWay, dCount, dQuality):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not dCount or not dQuality:
            return None
        dChooseCount = { }
        for iCount, iWeight in dCount.items():
            dChooseCount[iCount] = cl_formula.GetResultByData(oOwner, iWeight, {
                'MaxLayer': 4,
                'MaxLevel': 3 }, { })
        
        iCount = ChooseKey(oGame, dChooseCount)
        dMsgInfo = {
            'Pet': self.m_Owner,
            'Count': iCount }
        oHero = oGame.GetObject(oOwner.m_Owner)
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_INITPETABILITY, oHero, dMsgInfo)
        iCount = dMsgInfo['Count']
        if iPutWay == PET_PUT_WAY_HATCH_RARE:
            lstAbility = self.GetPerformSIDByType(PF_TYPE_PETABILITY)
            dAbility = cl_platformdata.GetPetAbilityByQuality(PET_ABILITY_HIGH)
            for iAbility in lstAbility:
                if iAbility in dAbility:
                    break
            else:
                iCount -= 1
                self.ChooseAbilityByQuality(oOwner, PET_ABILITY_HIGH, sReason = REASON_INIT)
        for _ in range(iCount):
            iQuality = ChooseKey(oGame, dQuality)
            self.ChooseAbilityByQuality(oOwner, iQuality, sReason = REASON_INIT)
        

    
    def InitFuseAbility(self, dAddData, dQualityWeight):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        dFusePetConfig = cl_platformdata.GetFusePetConfig()
        self.m_InheritableInfo = DeepCopy(dAddData.get('InheritableInfo', { }))
        dBaseNumWeight = dFusePetConfig['BaseAbilityNum']
        tParentAbilityNum = dAddData['ParentAbilityNum']
        if tParentAbilityNum in dBaseNumWeight:
            dAbilityNumWeight = dBaseNumWeight[tParentAbilityNum]
        else:
            PetLog.Alert('%s fusepet %s-%s abilitynum %s err' % (oGame.m_ID, oOwner.m_ID, oOwner.m_SID, tParentAbilityNum))
            return None
        iCount = ChooseKey(oGame, dAbilityNumWeight)
        iTotalCount = iCount
        dExtAbilityConfig = dFusePetConfig['ExtAbility']
        iLimitCnt = dExtAbilityConfig['LimitCnt']
        if iCount <= iLimitCnt:
            iExtCount = ChooseKey(oGame, dExtAbilityConfig['ExtNumWeight'])
            iTotalCount += iExtCount
            for _ in range(iExtCount):
                iProp = self.m_Game.Random(100)
                if iProp < dExtAbilityConfig['ChooseParentAbilityProp']:
                    iCount += 1
            
        dParentAbilityWeight = dAddData['AbilityWeight']
        dMsgInfo = {
            'Pet': self.m_Owner,
            'Count': iCount,
            'TotalCount': iTotalCount,
            'ParentAbilityWeight': dParentAbilityWeight }
        oHero = oGame.GetObject(oOwner.m_Owner)
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_INITFUSEPETABILITY, oHero, dMsgInfo)
        iCount = dMsgInfo['Count']
        iTotalCount = dMsgInfo['TotalCount']
        for _ in range(iCount):
            if not self.ChooseParentAbility(dParentAbilityWeight, sReason = REASON_FUSE):
                break
            iTotalCount -= 1
        
        if iTotalCount > 0:
            self.InitAbility(PET_PUT_WAY_FUSE, {
                iTotalCount: 10 }, dQualityWeight)
        for iAbility in list(self.m_InheritableInfo):
            if iAbility not in self.m_Perform:
                self.m_InheritableInfo.pop(iAbility)
        

    
    def ChooseAbilityByQuality(self, oOwner, iQuality, sReason, dExcludeAbility = None):
        oGame = self.m_Game
        dAbility = self.GetAbilityWeightByQuality(iQuality, dExcludeAbility)
        if not dAbility and iQuality != PET_ABILITY_NORMAL:
            dAbility = self.GetAbilityWeightByQuality(PET_ABILITY_NORMAL, dExcludeAbility)
        if not dAbility:
            lstAbility = self.GetPerformSIDByType(PF_TYPE_PETABILITY)
            PetLog.Alert(f'''{oGame.m_ID} {oOwner.m_ID} {oOwner.m_SID} initability fail {iQuality} {lstAbility} {self.m_ExcludeAbility}''')
            return 0
        iAbility = ChooseKey(oGame, dAbility)
        self.AddAbility(iAbility, sReason)
        return iAbility

    
    def GetAbilityWeightByQuality(self, iQuality, dExcludeAbility):
        dAbility = cl_platformdata.GetPetAbilityByQuality(iQuality)
        if not dAbility:
            return { }
        dAvailable = { }
        if dExcludeAbility is None:
            dExcludeAbility = { }
        for iAbility in dAbility:
            if iAbility in dExcludeAbility:
                continue
            iWeight = self.GetAbilityWeight(iAbility)
            if iWeight:
                dAvailable[iAbility] = iWeight
        
        return dAvailable

    
    def ChooseParentAbility(self, dParentAbilityWeight, sReason):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        iSID = oOwner.m_SID
        dAvailable = { }
        for iAbility, iWeight in dParentAbilityWeight.items():
            if ValidAddAbility(iSID, iAbility, self.m_Perform, self.m_ExcludeAbility):
                dAvailable[iAbility] = iWeight
        
        if not dAvailable:
            return 0
        iAbility = ChooseKey(oGame, dAvailable)
        self.AddAbility(iAbility, sReason)
        return iAbility

    
    def AddAbility(self, iAbility, sReason, iLevel = 1, iEnable = 0, iItem = 0):
        if len(self.GetPerformSIDByType(PF_TYPE_PETABILITY)) >= ABILITY_MAX_COUNT:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        PetLog.Debug('%s %s %s addability %s %s' % (self.m_Game.m_ID, oOwner.m_ID, oOwner.m_SID, iAbility, sReason))
        oPerform = self.AddPerform(oOwner, iAbility, iLevel, iEnable, iItem)
        if oPerform:
            self.EnableAttr(iAbility)
            lstExclude = cl_platformdata.GetPetAbilityExclude(iAbility)
            self.m_ExcludeAbility = self.m_ExcludeAbility | set(lstExclude)
        else:
            PetLog.Alert('%s %s %s addabilityfail %s %s' % (self.m_Game.m_ID, oOwner.m_ID, oOwner.m_SID, iAbility, sReason))

    
    def RemoveAbility(self, iAbility, sReason):
        oAbility = self.GetPerform(iAbility)
        if not oAbility:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        PetLog.Debug('%s %s %s removeability %s %s' % (self.m_Game.m_ID, oOwner.m_ID, oOwner.m_SID, iAbility, sReason))
        self.RemovePerform(oOwner, iAbility)
        self.DisableAttr(iAbility)
        self.UpdateExcludeAbility()

    
    def UpdateExcludeAbility(self):
        self.m_ExcludeAbility = set()
        for iAbility in self.GetPerformSIDByType(PF_TYPE_PETABILITY):
            lstExclude = cl_platformdata.GetPetAbilityExclude(iAbility)
            self.m_ExcludeAbility = self.m_ExcludeAbility | set(lstExclude)
        

    
    def GetFormulaAttr(self, iAbility):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        clsPerform = cl_perform.GetPerformModule(iAbility)
        dAttr = { }
        for sAttr, (iAdd, iMul, iForce) in clsPerform.m_PetAttr.items():
            iAdd = cl_formula.GetFormulaResult(oOwner, iAdd)
            iMul = cl_formula.GetFormulaResult(oOwner, iMul)
            iForce = cl_formula.GetFormulaResult(oOwner, iForce)
            dAttr[sAttr] = (iAdd, iMul, iForce)
        
        return dAttr

    
    def EnableAttr(self, iAbility):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dFormulaAttr = self.GetFormulaAttr(iAbility)
        sKey = 'PetAbility%d' % iAbility
        for sAttr, (iAdd, iMul, iForce) in dFormulaAttr.items():
            if iForce:
                oOwner.AttrForceSet(sAttr, iForce, sKey)
                continue
            oOwner.AttrChange(sAttr, iMul, iAdd, sKey)
        

    
    def DisableAttr(self, iAbility):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dFormulaAttr = self.GetFormulaAttr(iAbility)
        sKey = 'PetAbility%d' % iAbility
        for sAttr, (_, _, iForce) in dFormulaAttr.items():
            if iForce:
                oOwner.AttrForceClear(sAttr, sKey)
                continue
            oOwner.AttrClear(sAttr, sKey)
        

    
    def RandomAddAbility(self, iCount, sReason):
        dAbility = { }
        for iAbility in cl_platformdata.GetPetAbilityPut():
            iWeight = self.GetAbilityWeight(iAbility)
            if iWeight:
                dAbility[iAbility] = iWeight
        
        oGame = self.m_Game
        for _ in range(iCount):
            iAddAbility = ChooseKey(oGame, dAbility)
            self.AddAbility(iAddAbility, sReason)
        

    
    def GetAbilityNumByQualityType(self, dQualityType):
        lstAbility = self.GetPerformSIDByType(PF_TYPE_PETABILITY)
        if not dQualityType:
            return len(lstAbility)
        iNum = 0
        for iAbility in lstAbility:
            oAbility = self.GetPerform(iAbility)
            if oAbility and oAbility.m_Quality in dQualityType:
                iNum += 1
        
        return iNum

    
    def HasAbility(self, iAbility):
        oAbility = self.GetPerform(iAbility)
        if oAbility and oAbility.m_PFType == PF_TYPE_PETABILITY:
            return 1
        return 0

    
    def AIMemberPetEnable(self, iNotify = 1):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in self.m_Perform.values():
            if not oPerform.CheckIsAIMemberPetDisable():
                continue
            oPerform.Enable(oOwner, iNotify)
        

    
    def AIMemberPetDisable(self):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in list(self.m_Perform.values()):
            if not oPerform.CheckIsAIMemberPetDisable():
                continue
            oPerform.Disable(oOwner)
        



def ValidAddAbility(iPetSID, iAbility, lstHas, lstExclude):
    clsAbility = cl_perform.GetPerformModule(iAbility)
    if not clsAbility:
        return 0
    if iAbility in lstHas:
        return 0
    if iAbility in lstExclude:
        return 0
    if clsAbility.m_LimitPet and iPetSID not in clsAbility.m_LimitPet:
        return 0
    if clsAbility.m_ExcludePet and iPetSID in clsAbility.m_ExcludePet:
        return 0
    return 1

