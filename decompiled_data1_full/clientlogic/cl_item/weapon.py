# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/weapon.pyc
# RelativePath: clientlogic/cl_item/weapon.pyc
# Source Generated with Decompyle++
# File: weapon.pyc (Python 3.6)

from cl_only import RaiseError
from cl_commondefines import BAG_TYPE_WIELD, CURWEAPON_ADD, UPINS_TO_RARE, UPINS_TO_EXCLUSIVE, DAM_TYPE_NORMAL, INSCRIPTION_TYPE_GEMINI, INSCRIPTION_TYPE_NORMAL, INSCRIPTION_TYPE_RARE, INSCRIPTION_TYPE_EXCLUSIVE, WEAPON_MAIN_PERFORM, WEAPON_MINOR_PERFORM
from cl_cscommondef.cs_itemdef import EQUIP_TYPE_MAINWEAPON, WEAPON_ACTION_UPGRADE, WEAPON_ACTION_RECAST, WEAPON_ACTION_UPGRADEINSCRIPTION, WEAPON_LIMIT, INSCRIPTION_LIMIT, WEAPON_ACTION_ENHANCE
from cl_item.equip import CEquip
from cl_item.component.cominscription import MAX_INSCRIPTION_NUM
from cl_item.component.comenhance import MAX_ENHANCE_NUM
from cl_platformdata import GetInscriptionLib
from cl_newformula import Func837
import cl_item.defines as itemdef
import cl_drop
import cl_msgcenter
import cl_notify
import cl_object.elementtype as elementtype
import cl_forbid
import cl_formula
import cl_perform
import cllib.lib_flag as lib_flag
CHECK_WEAPON_ACTION = {
    WEAPON_ACTION_ENHANCE: (lambda oItem, dArgs: oItem.CanEnhance()),
    WEAPON_ACTION_UPGRADEINSCRIPTION: (lambda oItem, dArgs: oItem.CanUpgradeInscription(dArgs)),
    WEAPON_ACTION_RECAST: (lambda oItem, dArgs: oItem.CanRecast()),
    WEAPON_ACTION_UPGRADE: (lambda oItem, dArgs: oItem.CanUpgrade()) }
WEAPON_ACTION = {
    WEAPON_ACTION_ENHANCE: (lambda oItem, dArgs: oItem.Enhance()),
    WEAPON_ACTION_UPGRADEINSCRIPTION: (lambda oItem, dArgs: oItem.UpgradeInscription(dArgs)),
    WEAPON_ACTION_RECAST: (lambda oItem, dArgs: oItem.Recast()),
    WEAPON_ACTION_UPGRADE: (lambda oItem, dArgs: oItem.Upgrade(dArgs['WeaponUpgradeLevel'] if 'WeaponUpgradeLevel' in dArgs else 1)) }

FUNDAMENTALWEAPON_GRADEFORMULA = lambda *a: Func837(*a)

class CWeapon(CEquip):
    m_MaxGrade = 0
    m_ElementType = DAM_TYPE_NORMAL
    m_CanDoubleHold = 1
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super(CWeapon, self).__init__(oGame, iTemp, iPointID, dTmp)
        self.m_BallisticType = 0
        self.m_ElementTypeObj = None
        self.m_ForbidRuleInfo = { }
        self.m_ForbidTypeInfo = { }
        self.m_CheckedPlayer = { }
        self.m_Pos = -1
        self.m_UpgradeTimes = 0
        self.m_WeaponGeminiExcludeInfo = []

    
    def Init(self, iGrade = 1):
        self.m_ElementTypeObj = elementtype.CWeaponElementType(self, self.m_ElementType)
        iWarMaxGrade = self.m_Game.m_WarData.GetMaxWeaponGrade(self.m_Game)
        self.m_MaxGrade = iWarMaxGrade
        self.m_WeaponGeminiExcludeInfo = self.GetWeaponGeminiExcludeInfo()
        super(CWeapon, self).Init(iGrade)

    
    def Save(self):
        dData = super(CWeapon, self).Save()
        dData['Upgrade'] = self.m_UpgradeTimes
        dData['S'] = self.m_Source
        dData['SH'] = self.m_Shape
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        super(CWeapon, self).Load(dData)
        self.m_UpgradeTimes = dData.get('Upgrade', 0)
        self.m_Source = dData.get('S', 0)
        if 'SH' in dData:
            self.m_Shape = dData['SH']

    
    def CanUpgrade(self):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        if self.m_MaxGrade and self.m_Grade >= self.m_MaxGrade:
            return 0
        return 1

    
    def CanRecastGemini(self):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return 0
        iGemini = oInscriptionCom.m_Type2Num.get(INSCRIPTION_TYPE_GEMINI, 0)
        return iGemini > 0

    
    def CanRecast(self):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        oInscriptionCom = self.GetComponent('Inscription')
        if oInscriptionCom.GetInscriptionNum() == 0:
            return 0
        return 1

    
    def CanUpgradeInscription(self, dArgs):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        oInscriptionCom = self.GetComponent('Inscription')
        tUpType = oInscriptionCom.GetInscriptionUpgradeType(dArgs)
        sUpType = tUpType[0] if tUpType else UPINS_TO_RARE
        lstInscription = oInscriptionCom.GetInscriptionByType(INSCRIPTION_TYPE_NORMAL)
        if sUpType == UPINS_TO_EXCLUSIVE:
            if not oInscriptionCom.ValidChooseInscription(INSCRIPTION_TYPE_EXCLUSIVE):
                return 0
            lstInscription.extend(oInscriptionCom.GetInscriptionByType(INSCRIPTION_TYPE_RARE))
        if len(lstInscription) == 0:
            return 0
        return 1

    
    def CanExtraInscription(self):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        if not oOwner.Query('ExtraInscription', 0) and not oOwner.Query('SuitExtraInscription', 0):
            return 0
        if self.Query('UnWarWeapon', 0):
            return 0
        return 1

    
    def CanEnhance(self):
        if self.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return 0
        oEnhanceCom = self.GetComponent('Enhance')
        if not oEnhanceCom:
            return 0
        lstEnhance = oEnhanceCom.GetAllEnhanceSID()
        if len(lstEnhance) > MAX_ENHANCE_NUM:
            return 0
        return 1

    
    def AddEnhance(self, iNum, sReason):
        oEnhanceCom = self.GetComponent('Enhance')
        if oEnhanceCom:
            oEnhanceCom.AddEnhance(iNum, sReason)

    
    def AddEnhanceBySID(self, iEnhance, sReason):
        oEnhanceCom = self.GetComponent('Enhance')
        if oEnhanceCom:
            oEnhanceCom.AddEnhanceBySID(iEnhance, sReason)

    
    def OnSetGrade(self):
        if self.m_Owner:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            iHoldPos = self.GetComponent('Hold').HoldPos()
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, oOwner, {
                'ItemID': self.m_ID,
                'HoldType': iHoldPos })
        dAttr = self.m_Game.m_WarData.GetWeaponGradeAddition(self.m_Grade)
        for sAttr, (iAdd, iMul) in dAttr.items():
            self.AttrChange(sAttr, iMul, iAdd, 'GradeAddition', iRefresh = 1, iRemoveClear = 0)
        

    
    def Upgrade(self, iLevel = 1, iNotify = 1):
        self.m_UpgradeTimes += 1
        oOwner = self.GetOwner()
        if iLevel == 1:
            iLevel = oOwner.Query('ForceSetWeaponUpgradeLevel', 1) if oOwner else 1
        if self.m_MaxGrade and self.m_Grade + iLevel > self.m_MaxGrade:
            iLevel = self.m_MaxGrade - self.m_Grade
        self.SetBaseGrade(self.m_BaseGrade + iLevel, iSendMsg = 1)
        self.m_CheckedPlayer = { }
        if iNotify and self.m_Owner and not (lib_flag.g_IsMobileRun):
            iPlayer = self.m_Game.GetObject(self.m_Owner).m_PlayerID
            cl_notify.SendCommonNotify(self.m_Game, [
                iPlayer], 2113, { })

    
    def Degrade(self, iLevel):
        if iLevel < 0:
            RaiseError('Equip Degrade Level < 0')
            return None
        if self.m_BaseGrade - iLevel < 0:
            iLevel = self.m_BaseGrade
        if not iLevel:
            return None
        self.SetBaseGrade(self.m_BaseGrade - iLevel, iSendMsg = 1)

    
    def GetRecastTimes(self):
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return 0
        return oInscriptionCom.GetRecastTimes()

    
    def GetWeaponGeminiExcludeInfo(self):
        dGeminiInscription = GetInscriptionLib()[INSCRIPTION_TYPE_GEMINI]
        lstGeminiInscriptionLimit = []
        for iGeminiInscription, iWeight in dGeminiInscription.items():
            if not iWeight:
                continue
            clsPerform = cl_perform.GetPerformModule(iGeminiInscription)
            if not clsPerform.CheckValidItemByWeapon(self):
                lstGeminiInscriptionLimit.append((WEAPON_LIMIT, iGeminiInscription))
        
        return lstGeminiInscriptionLimit

    
    def GetGeminiExcludeInfo(self):
        lstGeminiInfo = []
        lstGeminiInfo.extend(self.m_WeaponGeminiExcludeInfo)
        lstGeminiInfo.extend(self.GetInscriptionGeminiExcludeInfo())
        return lstGeminiInfo

    
    def GetInscriptionGeminiExcludeInfo(self):
        dGeminiInscription = GetInscriptionLib()[INSCRIPTION_TYPE_GEMINI]
        lstGeminiInscriptionLimit = []
        oInscriptionCom = self.GetComponent('Inscription')
        lstHas = oInscriptionCom.m_Inscription
        for iGeminiInscription, iWeight in dGeminiInscription.items():
            if not iWeight:
                continue
            clsPerform = cl_perform.GetPerformModule(iGeminiInscription)
            if not clsPerform.CheckValidItemByInscription(lstHas):
                lstGeminiInscriptionLimit.append((INSCRIPTION_LIMIT, iGeminiInscription))
        
        return lstGeminiInscriptionLimit

    
    def Recast(self):
        oInscriptionCom = self.GetComponent('Inscription')
        if oInscriptionCom:
            oInscriptionCom.Recast()
        self.m_CheckedPlayer = { }

    
    def RecastGemini(self):
        oInscriptionCom = self.GetComponent('Inscription')
        if oInscriptionCom:
            oInscriptionCom.RecastGemini()
        self.m_CheckedPlayer = { }
        if self.m_Owner and not (lib_flag.g_IsMobileRun):
            iPlayer = self.m_Game.GetObject(self.m_Owner).m_PlayerID
            cl_notify.SendCommonNotify(self.m_Game, [
                iPlayer], 2114, { })

    
    def UpgradeInscription(self, dArgs):
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return None
        oInscriptionCom.UpgradeInscription(dArgs)
        self.m_CheckedPlayer = { }

    
    def ExtraInscription(self):
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return None
        if oInscriptionCom.m_InscriptionNum >= MAX_INSCRIPTION_NUM:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not oOwner.Query('SuitExtraInscription') and oInscriptionCom.GetExtraInscriptionTimes():
            return None
        oInscriptionCom.ExtraInscription()
        self.m_CheckedPlayer = { }
        if self.m_Owner and not (lib_flag.g_IsMobileRun):
            iPlayer = self.m_Game.GetObject(self.m_Owner).m_PlayerID
            cl_notify.SendCommonNotify(self.m_Game, [
                iPlayer], 2345, { })

    
    def Enhance(self):
        oEnhanceCom = self.GetComponent('Enhance')
        lstEnhance = oEnhanceCom.GetAllEnhanceSID()
        if lstEnhance:
            oEnhanceCom.RemoveEnhance(1)
        oEnhanceCom.AddEnhance(1, 'weaponaction', lstEnhance)
        self.m_CheckedPlayer = { }

    
    def GetWeaponPerformByType(self, iType):
        oPerformCom = self.GetComponent('Perform')
        if iType == WEAPON_MAIN_PERFORM:
            return oPerformCom.m_AttPerform
        if iType == WEAPON_MINOR_PERFORM:
            return oPerformCom.m_MinorPeform
        return 0

    
    def IsInitWeapon(self):
        if self.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            return True
        return False

    
    def CheckWeaponType2(self, iType):
        if 15 & iType:
            if self.m_Type == iType:
                return 1
            return 0
        if self.m_Type & iType == iType:
            return 1
        return 0

    
    def RefreshAttr(self, sAttr, iValue):
        if not self.m_Owner:
            return None
        self.GS2CItemPropChange(sAttr, iValue)
        dMsgInfo = {
            'ItemID': self.m_ID,
            'RefreshAttribute': sAttr }
        self.SendMsg(itemdef.MSG_ITEM_REFRESHATTRIBUTE, dMsgInfo)

    
    def OnMaxPFBulletChange(self, oPerform):
        dMsgInfo = {
            'ItemID': self.m_ID,
            'pfid': oPerform.m_SID }
        self.SendMsg(itemdef.MSG_ITEM_MAXPFBULLET_CHANGE, dMsgInfo)

    
    def AttrCache(self):
        dData = super(CWeapon, self).AttrCache()
        dData['ElementType'] = self.m_ElementType
        dData['BallisticType'] = self.m_BallisticType
        for sAttr in self.m_SpecialAttr:
            dData[sAttr] = self.m_SpecialAttr[sAttr][0]
        
        return dData

    
    def Fire(self):
        self.SendMsg(itemdef.MSG_ITEM_FIRE)

    
    def FillBullet(self):
        self.SendMsg(itemdef.MSG_ITEM_FILLBULLET)

    
    def Forbid(self, iRule, sReason):
        dForbidRule = self.m_ForbidRuleInfo
        if iRule not in dForbidRule:
            dForbidRule[iRule] = { }
        if sReason in dForbidRule[iRule]:
            return None
        dForbidRule[iRule][sReason] = 1
        dForbidType = self.m_ForbidTypeInfo
        dForbid = cl_forbid.GetRule2Forbid(iRule)
        for iType in dForbid:
            if iType not in dForbidType:
                dForbidType[iType] = 1
                continue
            dForbidType[iType] += 1
        

    
    def UnForbid(self, iRule, sReason):
        dForbidRule = self.m_ForbidRuleInfo
        if iRule not in dForbidRule:
            return None
        if sReason not in dForbidRule[iRule]:
            return None
        dForbidRule[iRule].pop(sReason)
        if not dForbidRule[iRule]:
            dForbidRule.pop(iRule)
        dForbidType = self.m_ForbidTypeInfo
        dForbid = cl_forbid.GetRule2Forbid(iRule)
        for iType in dForbid:
            if dForbidType[iType] > 1:
                dForbidType[iType] -= 1
                continue
            dForbidType.pop(iType)
        

    
    def ClearAllForbid(self):
        self.m_ForbidRuleInfo = { }
        self.m_ForbidTypeInfo = { }

    
    def PutToContainer(self, lstCon, sReason, iReplacePos = 0):
        if not self.m_ID:
            RaiseError('Equip PutContainer NoTemp %s' % sReason)
            return 0
        for oContainer in lstCon:
            oOwner = oContainer.GetOwner()
            iFirstAdd = 1 if oOwner.m_PlayerID not in self.m_WarPickInfo else 0
            if iReplacePos and not oContainer.GetAllItemByType(EQUIP_TYPE_MAINWEAPON):
                iReplacePos = 0
            iPos = oContainer.AddItem(self, iReplacePos)
            if oContainer.m_BagType == BAG_TYPE_WIELD:
                if not iPos:
                    oReplace = self.GetReplaceWeapon(oContainer, iReplacePos)
                    if oReplace and oContainer.ValidReplace(oReplace, self):
                        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, oOwner, {
                            'CanDoubleHold': self.m_CanDoubleHold,
                            'ReplaceID': oReplace.m_ID })
                        iPos = oReplace.m_Pos
                        if sReason == 'ChangeWithContainer':
                            iOldPos = self.m_Pos
                            oOldContainer = self.m_Container
                            oContainer.RemoveItem(oReplace, sReason)
                            oOldContainer.RemoveItem(self, sReason)
                            oContainer.AddItem(self, iReplacePos)
                            oOldContainer.AddItem(oReplace, iOldPos)
                        else:
                            oContainer.ItemReplace(oReplace, self)
                            cl_drop.DropItem(oOwner, oReplace, True)
                        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REPLACEWEAPON, oOwner, {
                            'ItemID': self.m_ID,
                            'Pos': iPos })
                if iPos:
                    if self.ValidChangeWeapon(oContainer, iReplacePos):
                        oContainer.SetCurWeapon(iPos, CURWEAPON_ADD)
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WIELDWEAPON, oOwner, {
                        'FirstAdd': iFirstAdd,
                        'pid': oOwner.m_ID,
                        'ID': self.m_ID,
                        'SID': self.m_SID,
                        'Type': self.m_Type })
            if iPos:
                self.InitSource(oOwner.m_PlayerID)
                return iPos
        
        return 0

    
    def GetReplaceWeapon(self, oContainer, iReplacePos):
        oCurWeapon = oContainer.GetCurWeapon()
        if not iReplacePos and oCurWeapon.m_Type & itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            iReplacePos = 1
        if iReplacePos:
            oReplace = oContainer.GetItemByPos(iReplacePos)
        else:
            oReplace = oCurWeapon
        return oReplace

    
    def ValidChangeWeapon(self, oContainer, iReplacePos):
        bChangeWeapon = True
        oCurWeapon = oContainer.GetCurWeapon()
        if oCurWeapon:
            if self.Query('OneWeaponNotChange', 0) and not oContainer.GetEmptySize():
                bChangeWeapon = False
            if iReplacePos and iReplacePos != oContainer.GetCurWeaponPos():
                bChangeWeapon = False
        return bChangeWeapon

    
    def ReplaceToContainer(self, oContainer, iReplacePos, sReason):
        if not self.m_ID:
            RaiseError('Equip PutContainer NoTemp %s' % sReason)
            return 0
        oOwner = oContainer.GetOwner()
        iFirstAdd = 1 if oOwner.m_PlayerID not in self.m_WarPickInfo else 0
        oReplace = oContainer.GetItemByPos(iReplacePos)
        if oReplace and oContainer.ValidReplace(oReplace, self):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, oOwner, {
                'CanDoubleHold': self.m_CanDoubleHold,
                'ReplaceID': oReplace.m_ID })
            oContainer.ItemReplace(oReplace, self)
            cl_drop.DropItem(oOwner, oReplace)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REPLACEWEAPON, oOwner, {
                'ItemID': self.m_ID })
            if self.ValidChangeWeapon(oContainer, iReplacePos):
                oContainer.SetCurWeapon(iReplacePos, CURWEAPON_ADD)
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WIELDWEAPON, oOwner, {
                    'FirstAdd': iFirstAdd,
                    'pid': oOwner.m_ID,
                    'ID': self.m_ID,
                    'SID': self.m_SID,
                    'Type': self.m_Type })
            return iReplacePos
        return 0

    
    def ChangeBallisticType(self, iAdd, iMax):
        iNew = self.m_BallisticType + iAdd
        if iNew > iMax:
            iNew = 0
        self.m_BallisticType = iNew

    
    def GetWeaponUpgradeCost(self):
        oOwner = self.GetOwner()
        iPrceReverse = 0
        if oOwner:
            iForceCost = oOwner.Query('ForceSetWeaponUpgradeCost')
            iPrceReverse = oOwner.Query('PriceReverse', 0)
            if iForceCost:
                return iForceCost
        oGame = self.m_Game
        iGrade = self.m_BaseGrade
        iCost = oGame.m_WarData.GetWeaponUpgradeCost(iGrade)
        if iPrceReverse:
            iCost = -iCost
        return iCost

    
    def GetWeaponExtraInscriptionCost(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return 600
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return 600
        iPrceReverse = oOwner.Query('PriceReverse', 0)
        iCost = oOwner.Query('WeaponExtraInscriptionCost', 0)
        dCost = oOwner.Query('WeaponExtraEtchingCost', { })
        if (not iCost or oInscriptionCom.GetExtraInscriptionTimes()) and dCost:
            iNum = oInscriptionCom.m_InscriptionNum
            iCost = dCost[iNum] if iNum in dCost else 600
        iCost = cl_formula.GetResultByData(oOwner, iCost, { }, { }, {
            'Weapon': self })
        if iPrceReverse:
            iCost = -iCost
        return iCost

    
    def PreviewWeaponUpgradeAttr(self):
        dPreview = { }
        oOwner = self.GetOwner()
        iUpGradeLevel = oOwner.Query('ForceSetWeaponUpgradeLevel', 1) if oOwner else 1
        iGrade = self.m_Grade + iUpGradeLevel
        dOldAttr = self.m_Game.m_WarData.GetWeaponGradeAddition(self.m_Grade)
        dNewAttr = self.m_Game.m_WarData.GetWeaponGradeAddition(iGrade)
        for sAttr, (iAdd, iMul) in dNewAttr.items():
            if sAttr not in self.m_PrivateAttr:
                continue
            if sAttr in dOldAttr:
                iAdd -= dOldAttr[sAttr][0]
                iMul -= dOldAttr[sAttr][1]
            oAttr = self.m_PrivateAttr[sAttr]
            iCurVal = oAttr.GetValue(None)
            iUpVal = oAttr.PreviewChange(iMul, iAdd)
            dPreview[sAttr] = iUpVal - iCurVal
        
        return dPreview

    
    def GetAttrValueByGrade(self, sAttr, iGrade):
        iValue = None
        if sAttr not in self.m_PrivateAttr:
            return iValue
        if self.m_MaxGrade and iGrade >= self.m_MaxGrade:
            iGrade = self.m_MaxGrade
        dNewAttr = self.m_Game.m_WarData.GetWeaponGradeAddition(iGrade)
        if sAttr not in dNewAttr:
            return iValue
        dOldAttr = self.m_Game.m_WarData.GetWeaponGradeAddition(self.m_Grade)
        (iNewAdd, iNewMul) = dNewAttr[sAttr]
        if sAttr in dOldAttr:
            iNewAdd -= dOldAttr[sAttr][0]
            iNewMul -= dOldAttr[sAttr][1]
        oAttr = self.m_PrivateAttr[sAttr]
        iValue = oAttr.CalGradePreviewChangeValue(iNewMul, iNewAdd)
        return iValue

    
    def GetSaveInfo(self, oHero, iWeapon, iReset):
        if iReset:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SAVERESET, oHero, {
            'ItemID': iWeapon })

    
    def GetBulletType(self):
        if 'Bullet' not in self.m_ComponentAttr:
            return 0
        return self.m_ComponentAttr['Bullet']['BulletType']

    
    def GetPFBulletPerform(self):
        oPerformCom = self.GetComponent('Perform')
        if not oPerformCom:
            return None
        sAttr = 'MaxPFBullet'
        iAttackPerform = oPerformCom.GetAttPerform()
        oAttackPerform = oPerformCom.GetPerform(iAttackPerform)
        if oAttackPerform and oAttackPerform.GetAttr(sAttr):
            return oAttackPerform
        iMinorPerform = oPerformCom.GetMinorPerform()
        oMinorPerform = oPerformCom.GetPerform(iMinorPerform)
        if oMinorPerform and oMinorPerform.GetAttr(sAttr):
            return oMinorPerform

    
    def UpdateCheckedPlayer(self, dCheckedPlayer):
        self.m_CheckedPlayer.update(dCheckedPlayer)
        return self.m_CheckedPlayer

    
    def OnRemoveFromContainer(self):
        super(CWeapon, self).OnRemoveFromContainer()
        self.ClearAllExtGrade()

    
    def CheckHasMaxInscriptionNum(self):
        oInscriptionCom = self.GetComponent('Inscription')
        if not oInscriptionCom:
            return 0
        if oInscriptionCom.m_InscriptionNum >= MAX_INSCRIPTION_NUM:
            return 1
        return 0

    
    def SetRepeatInfo(self, sKey, iRepeatCnt, iRepeatCold):
        tRepeatInfo = self.QueryTmp('RepeatInfo', ())
        if tRepeatInfo and tRepeatInfo[0] != sKey:
            return None
        self.SendMsg(itemdef.MSG_ITEM_REPEAT_CHANGE, {
            'ItemID': self.m_ID,
            'RepeatCnt': iRepeatCnt })
        self.SetTmp('RepeatInfo', (sKey, iRepeatCnt, iRepeatCold))
        self.ItemAttrForceSet('FillBulletCnt', iRepeatCnt, sKey)

    
    def RemoveRepeatInfo(self, sKey):
        tRepeatInfo = self.QueryTmp('RepeatInfo', ())
        if tRepeatInfo and tRepeatInfo[0] != sKey:
            return None
        self.SendMsg(itemdef.MSG_ITEM_REPEAT_CHANGE, {
            'ItemID': self.m_ID,
            'RepeatCnt': 0 })
        self.RemoveTmp('RepeatInfo')
        self.ItemAttrForceClear('FillBulletCnt', sKey)



class CGun(CWeapon):
    m_Type = itemdef.EQUIP_TYPE_MAINWEAPON


class CFundamentalWeapon(CWeapon):
    m_Type = itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_GradeFormula = FUNDAMENTALWEAPON_GRADEFORMULA

    
    def ValidDrop(self):
        return 0

    
    def ValidBeReplaced(self, oOther):
        return 0

    
    def OnAddToContainer(self):
        super(CFundamentalWeapon, self).OnAddToContainer()
        self.InitAttention()

    
    def OnRemoveFromContainer(self):
        super(CFundamentalWeapon, self).OnRemoveFromContainer()
        self.ReleaseAttention()

    
    def InitAttention(self):
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnWieldChange, 'FundamentalWield', -1, 0)
            cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, self.OnGradeUp, 'FundamentalWield', -1, 0)
            cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.OnRemove, 'FundamentalWield', -1, 0)

    
    def ReleaseAttention(self):
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_ADDWEAPON, 'FundamentalWield')
            cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, 'FundamentalWield')
            cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_REMOVEWEAPON, 'FundamentalWield')

    
    def OnWieldChange(self, oTarget, dInfo):
        self.FundamentalChangeWeapon(oTarget)

    
    def OnGradeUp(self, oTarget, dInfo):
        self.FundamentalChangeWeapon(oTarget)

    
    def OnRemove(self, oTarget, dInfo):
        self.FundamentalChangeWeapon(oTarget)

    
    def FundamentalChangeWeapon(self, oOwner):
        iGrade = cl_formula.GetResultByData(oOwner, self.m_GradeFormula, { })
        self.SetBaseGrade(iGrade)

    
    def ChangeGradeFormula(self, oOwner, iFormula):
        self.SetTmp('ReplaceLevelFormula', 1)
        self.m_GradeFormula = iFormula
        self.FundamentalChangeWeapon(oOwner)
        self.RefreshGrade()

    
    def RestoreGradeFormula(self, oOwner):
        self.m_GradeFormula = FUNDAMENTALWEAPON_GRADEFORMULA
        self.SetTmp('ReplaceLevelFormula', 0)
        self.FundamentalChangeWeapon(oOwner)
        self.GS2CItemPropChange('ExtGradeGroup')

    
    def Release(self):
        self.ReleaseAttention()
        super(CFundamentalWeapon, self).Release()

    
    def RefreshGrade(self):
        if not self.QueryTmp('ReplaceLevelFormula'):
            return None
        super().RefreshGrade()

    
    def GetExtGrade(self):
        if not self.QueryTmp('ReplaceLevelFormula'):
            return 0
        return super().GetExtGrade()


