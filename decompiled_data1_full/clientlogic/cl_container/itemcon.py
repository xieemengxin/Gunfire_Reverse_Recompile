# Path: converted/converted_data1/clientlogic/cl_container/itemcon.pyc
# RelativePath: clientlogic/cl_container/itemcon.pyc
# Source Generated with Decompyle++
# File: itemcon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_WIELD, BAG_TYPE_ITEM, DESC_NUM, CURWEAPON_SWITCH, CURWEAPON_POS, BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE, PF_TYPE_INSCRIPTION, INSCRIPTION_TYPE_GEMINI, INSCRIPTION_TYPE_EXCLUSIVE
from cl_item.defines import EQUIP_TYPE_MAINWEAPON, DEPUTY_HOLD, EQUIP_MASK_WEAPON, MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_only import RaiseError, PythonError
from cl_object.logging import WeaponstoreLog
from cl_platformdata import GetInscriptionLib
from cl_item.component.comenhance import MAX_ENHANCE_NUM
from cl_item.component.cominscription import MAX_INSCRIPTION_NUM, SEALEDINSCRIPTION_POOL
from cl_perform.load import GetWeaponEnhanceLib
from cl_inscriptionpool import GetInscritionPool
import cl_item
import cl_netattr
import cl_msgcenter
import cl_duonet.dn_cl_item_cnet
import cl_item.cnet as cnet
import cl_putdata
import cl_perform
GEMINI_NUM = 1
EXCLUSIVE_NUM = 3

def GS2CItemAdd(oGame, iWarrior, iBagType, oItem, iPos, dPlayer = None):
    if dPlayer is None:
        dPlayer = oGame.GetRealPlayers()
        if not dPlayer:
            return None
    dInfo = cl_netattr.MakeItemAddPacket(oItem)
    netData = {
        'iItemID': oItem.m_ID,
        'iPos': iPos,
        'dInfo': dInfo,
        'iWarrior': iWarrior,
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iBagType': iBagType }
    if iBagType in (BAG_TYPE_WIELD, BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE):
        cl_duonet.dn_cl_item_cnet.DN_GS2CEquipAdd(netData)
    elif iBagType == BAG_TYPE_ITEM:
        cl_duonet.dn_cl_item_cnet.DN_GS2CItemAdd(netData)


def GS2CItemDel(oGame, iWarrior, iBagType, oItem):
    dPlayer = oGame.GetRealPlayers()
    if not dPlayer:
        return None
    netData = {
        'iItemID': oItem.m_ID,
        'iWarrior': iWarrior,
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iBagType': iBagType }
    if iBagType in (BAG_TYPE_WIELD, BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE):
        cl_duonet.dn_cl_item_cnet.DN_GS2CEquipDel(netData)
    elif iBagType == BAG_TYPE_ITEM:
        cl_duonet.dn_cl_item_cnet.DN_GS2CItemDel(netData)


class CContainer(object):
    m_BagType = 0
    m_InitCarryNum = 0
    m_CanExtendSize = 0
    m_PickUp = 0
    
    def __init__(self, oGame, iOwner):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_Item = { }
        self.m_ItemID = { }
        self.m_ItemSID = { }
        self.m_ExtendSize = 0

    
    def Release(self):
        for oItem in self.m_Item.values():
            oItem.Release()
            oItem.m_Container = None
        
        self.m_Item = { }
        self.m_ItemID = { }
        self.m_ItemSID = { }
        self.m_Game = None

    
    def Refresh(self, dPlayer = None):
        for iPos, oItem in self.m_Item.items():
            self.GS2CItemAdd(oItem, iPos, dPlayer)
            oItem.Refresh()
        

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def GetItem(self, iPos):
        if iPos not in self.m_Item:
            return None
        return self.m_Item[iPos]

    
    def GetItemByPos(self, iPos):
        if iPos not in self.m_Item:
            return None
        return self.m_Item[iPos]

    
    def GetItemByID(self, iItemID):
        if iItemID not in self.m_ItemID:
            return None
        return self.m_ItemID[iItemID]

    
    def GetItemBySID(self, iSid):
        if iSid not in self.m_ItemSID:
            return None
        for iItemID in self.m_ItemSID[iSid]:
            return self.m_ItemID[iItemID]
        

    
    def GetAllItemBySID(self, iSid):
        if iSid not in self.m_ItemSID:
            return []
        lstItem = []
        for iItemID in self.m_ItemSID[iSid]:
            oItem = self.m_ItemID[iItemID]
            lstItem.append(oItem)
        
        return lstItem

    
    def GetItemAmountBySID(self, iSid):
        if iSid not in self.m_ItemSID:
            return 0
        iCount = 0
        for iItemID in self.m_ItemSID[iSid]:
            oItem = self.m_ItemID[iItemID]
            iCount += oItem.Amount()
        
        return iCount

    
    def CarryInitNum(self):
        return self.m_InitCarryNum

    
    def CarryNum(self):
        return self.m_InitCarryNum + self.m_ExtendSize

    
    def ItemList(self):
        return list(self.m_Item.values())

    
    def ItemValidPos(self):
        return list(range(1, 1 + self.CarryNum()))

    
    def Expand(self, iSize):
        if self.m_ExtendSize + iSize > self.m_CanExtendSize:
            return 0
        self.m_ExtendSize += iSize
        if self.m_ExtendSize > self.m_CanExtendSize:
            self.m_ExtendSize = self.m_CanExtendSize
        self.GS2CBagSize()
        return iSize

    
    def GetEmptySize(self):
        return self.CarryNum() - len(self.ItemList())

    
    def IsValidPos(self, oItem, iPos, iReplace = 0):
        if iPos < 1 or iPos > self.CarryNum():
            return 0
        if not iReplace and iPos in self.m_Item:
            return 0
        return 1

    
    def GetValidPos(self, oItem):
        lstValidPos = self.ItemValidPos()
        for iPos in lstValidPos:
            if self.IsValidPos(oItem, iPos):
                return iPos
        
        return 0

    
    def GetAllValidPos(self, oItem):
        lstValidPos = self.ItemValidPos()
        lstPos = []
        for iPos in lstValidPos:
            if self.IsValidPos(oItem, iPos):
                lstPos.append(iPos)
        
        return lstPos

    
    def ValidReplace(self, oSrc, oOther):
        if oSrc.m_ID not in self.m_ItemID:
            return 0
        iPos = oSrc.m_Pos
        if not self.IsValidPos(oOther, iPos, 1):
            return 0
        if not oSrc.ValidBeReplaced(oOther):
            return 0
        if not oOther.ValidAddToContainer(self):
            return 0
        return 1

    
    def ItemReplace(self, oSrc, oOther):
        iPos = oSrc.m_Pos
        oOther.SetOwner(self.m_Owner)
        oSrc.OnBeReplaced(oOther)
        self.RemoveItem(oSrc, '被替换')
        self.AddItem(oOther, iPos)

    
    def OnLoadItemToPos(self, oItem, iPos):
        pass

    
    def LoadItemToPos(self, oItem, iPos):
        oItem.m_Pos = iPos
        iSID = oItem.m_SID
        if iSID not in self.m_ItemSID:
            self.m_ItemSID[iSID] = { }
        self.m_ItemSID[iSID][oItem.m_ID] = 1
        self.m_Item[iPos] = oItem
        self.m_ItemID[oItem.m_ID] = oItem
        if oItem.Query('TraceNo') == 0 and oItem.m_ID:
            iTraceNo = self.m_Game.NewTraceNo()
            oItem.Set('TraceNo', (self.m_Owner, iTraceNo * 100 + self.m_BagType))
        self.OnLoadItemToPos(oItem, iPos)

    
    def ValidGive(self, oDest):
        if oDest.m_ID:
            RaiseError('Item had ID when ValidGive %s' % oDest.m_SID)
            return 0
        iSid = oDest.m_SID
        iMaxAmount = oDest.GetMaxAmount()
        for oSource in self.GetAllItemBySID(iSid):
            if not oSource.CanCombine(oDest):
                continue
            iAdd = iMaxAmount - oSource.Amount()
            if iAdd > 0:
                return 1
        
        iGridCnt = len(self.GetAllValidPos(oDest))
        if iGridCnt > 0:
            return 1
        return 0

    
    def OnAddItem(self, oItem, iPos):
        pass

    
    def AddItem(self, oItem, iPos = 0):
        if not oItem or not oItem.ValidAddToContainer(self):
            return 0
        if not iPos:
            iPos = self.GetValidPos(oItem)
        elif not self.IsValidPos(oItem, iPos):
            return 0
        if iPos:
            self.LoadItemToPos(oItem, iPos)
            self.GS2CItemAdd(oItem, iPos)
            self.OnAddItem(oItem, iPos)
            oItem.AddToContainer(self)
            self.AfterAddItem(oItem)
            return iPos
        return 0

    
    def AfterAddItem(self, oItem):
        pass

    
    def AddCombineItem(self, oDest, sReason):
        if oDest.m_ID:
            RaiseError('Item had ID when AddCombineItem %s' % sReason)
            return 0
        iOldAmount = oDest.Amount()
        if iOldAmount <= 0:
            return 0
        iCanAddAmount = iOldAmount
        iLeftAmount = iOldAmount - iCanAddAmount
        oDest.SetAmount(iCanAddAmount, sReason)
        for oSource in self.GetAllItemBySID(oDest.m_SID):
            if not oSource.CanCombine(oDest):
                continue
            iAdd = oSource.GetMaxAmount() - oSource.Amount()
            iLeft = oDest.Amount()
            if iAdd > iLeft:
                iAdd = iLeft
                iLeft = 0
            else:
                iLeft -= iAdd
            oDest.AddAmount(-iAdd, sReason)
            oSource.AddAmount(iAdd, sReason)
            self.GS2CItemAmount(oSource)
            if iLeft <= 0:
                break
        
        iGridCnt = len(self.GetAllValidPos(oDest))
        for _ in range(iGridCnt):
            if not oDest.Amount():
                break
            dData = oDest.Save()
            oNewItem = cl_item.Load(self.m_Game, dData)
            if not oNewItem:
                RaiseError('%d no item %d when addcombine %s' % (self.m_Owner, oDest.m_SID, sReason))
                break
            iLeft = oDest.Amount()
            iAdd = oNewItem.GetMaxAmount()
            if iAdd > iLeft:
                iAdd = iLeft
                iLeft = 0
            else:
                iLeft -= iAdd
            oNewItem.SetAmount(iAdd, sReason)
            iRet = self.AddItem(oNewItem)
            if not iRet:
                break
            oDest.AddAmount(-iAdd, sReason)
        
        oOwner = self.GetOwner()
        oDest.AddAmount(iLeftAmount, sReason)
        iAddAmount = iOldAmount - oDest.Amount()
        dMsgInfo = {
            'SID': oDest.m_SID,
            'Amount': iAddAmount,
            'Type': oDest.m_Type }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDITEM, oOwner, dMsgInfo)
        return iAddAmount

    
    def SubItemAmount(self, iCnt, iItem, sReason):
        if iItem not in self.m_ItemID:
            return 0
        oItem = self.m_ItemID[iItem]
        iRemain = oItem.Amount()
        if iRemain < iCnt:
            iSub = iRemain
        else:
            iSub = iCnt
        oItem.AddAmount(-iSub, sReason)
        if oItem.Amount() > 0:
            self.GS2CItemAmount(oItem)
        else:
            self.RemoveItem(oItem, sReason)
        return iSub

    
    def SubItemAmountBySID(self, iSid, iCnt, sReason):
        iAll = iCnt
        for oItem in self.GetAllItemBySID(iSid):
            iSub = self.SubItemAmount(iCnt, oItem.m_ID, sReason)
            iCnt -= iSub
            if iCnt <= 0:
                break
        
        if iCnt > 0:
            RaiseError('%d Sub Item %d remain %d %s' % (self.m_Owner, iSid, iCnt, sReason))
        return iAll - iCnt

    
    def OnRemoveItem(self, oItem, sReason):
        pass

    
    def RemoveItem(self, oItem, sReason):
        if oItem.m_ID not in self.m_ItemID:
            return None
        oItem.RemoveFromContainer(sReason)
        self.m_ItemID.pop(oItem.m_ID)
        self.m_Item.pop(oItem.m_Pos)
        iSID = oItem.m_SID
        self.m_ItemSID[iSID].pop(oItem.m_ID)
        if not self.m_ItemSID[iSID]:
            self.m_ItemSID.pop(iSID)
        self.OnRemoveItem(oItem, sReason)
        self.GS2CItemDel(oItem)

    
    def OnItemChange(self, oSrc, oDest):
        pass

    
    def ItemChange(self, oSrc, oDest):
        iSrcPos = oSrc.m_Pos
        iDestPos = oDest.m_Pos
        self.m_Item[iDestPos] = oSrc
        self.m_Item[iSrcPos] = oDest
        oSrc.m_Pos = iDestPos
        oDest.m_Pos = iSrcPos
        self.GS2CItemDel(oDest)
        self.GS2CItemDel(oSrc)
        self.GS2CItemAdd(oSrc, iDestPos)
        self.GS2CItemAdd(oDest, iSrcPos)
        self.OnItemChange(oSrc, oDest)

    
    def OnItemPos(self, oItem, iPos):
        pass

    
    def ItemPos(self, oItem, iPos):
        self.m_Item.pop(oItem.m_Pos)
        self.m_Item[iPos] = oItem
        oItem.m_Pos = iPos
        self.GS2CItemDel(oItem)
        self.GS2CItemAdd(oItem, iPos)
        self.OnItemPos(oItem, iPos)

    
    def ClearAll(self, sReason):
        for oItem in self.ItemList():
            self.RemoveItem(oItem, sReason)
        

    
    def GS2CItemAdd(self, oItem, iPos, dPlayer = None):
        GS2CItemAdd(self.m_Game, self.m_Owner, self.m_BagType, oItem, iPos, dPlayer)

    
    def GS2CItemDel(self, oItem):
        GS2CItemDel(self.m_Game, self.m_Owner, self.m_BagType, oItem)

    
    def GS2CItemAmount(self, oItem):
        oItem.GS2CItemPropChange('Amount')

    
    def GS2CBagSize(self):
        pass

    
    def GetAllItem(self):
        return list(self.m_Item.values())

    
    def GetWeaponItemSaveInfo(self, oWeapon):
        dAllWeaponData = oWeapon.Save()
        dSaveWeaponData = { }
        dCom = { }
        dCom['Enhance'] = dAllWeaponData['Com']['Enhance']
        dInscription = { }
        dInscription['Inscription'] = dAllWeaponData['Com']['Inscription']['Inscription']
        dInscription['SealedIns'] = dAllWeaponData['Com']['Inscription']['SealedIns']
        dCom['Inscription'] = dInscription
        dSaveWeaponData = {
            'SID': dAllWeaponData['SID'],
            'Com': dCom }
        return dSaveWeaponData



class CWieldContainer(CContainer):
    m_BagType = BAG_TYPE_WIELD
    m_InitCarryNum = 3
    m_CanExtendSize = 0
    m_Pos2Type = {
        1: EQUIP_TYPE_MAINWEAPON,
        2: EQUIP_TYPE_MAINWEAPON,
        3: EQUIP_TYPE_FUNDAMENTALWEAPON }
    m_Type2Pos = {
        EQUIP_TYPE_FUNDAMENTALWEAPON: (3,),
        EQUIP_TYPE_MAINWEAPON: (1, 2) }
    m_MainDeputyPos = {
        1: 2,
        2: 1,
        3: 4,
        4: 3 }
    
    def __init__(self, oGame, iOwner):
        super(CWieldContainer, self).__init__(oGame, iOwner)
        self.m_WeaponChangeSign = 0

    
    def SetWeaponChangeSign(self, iSign):
        self.m_WeaponChangeSign = iSign

    
    def OnAddItem(self, oItem, iPos):
        oHero = self.GetOwner()
        if oHero:
            oHero.GS2CPropChange('Desc')
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDWEAPON, oHero, {
                'ItemID': oItem.m_ID,
                'Weapon': oItem,
                'Hero': oHero.m_ID })

    
    def AfterAddItem(self, oItem):
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AFTERADDWEAPON, oHero, {
                'ItemID': oItem.m_ID })

    
    def OnRemoveItem(self, oItem, sReason):
        oHero = self.GetOwner()
        if oHero:
            oHero.GS2CPropChange('Desc')
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEWEAPON, oHero, {
                'ItemID': oItem.m_ID,
                'SID': oItem.m_SID,
                'Hero': oHero.m_ID,
                'Reason': sReason,
                'ItemKey': oItem.Key(),
                'Weapon': oItem })
            if sReason in (cnet.WIELD_TO_GLOBAL, cnet.WIELD_TO_OTHERCOM):
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ACREMOVEWEAPON, oHero, {
                    'ItemID': oItem.m_ID,
                    'SID': oItem.m_SID })

    
    def OnItemChange(self, oSrc, oDest):
        oHero = self.GetOwner()
        if oHero:
            oHero.GS2CPropChange('Desc')
            oCurWeapon = self.GetCurWeapon()
            if oSrc.m_ID == oCurWeapon.m_ID or oDest.m_ID == oCurWeapon.m_ID:
                self.SetWeaponChangeSign(CURWEAPON_POS)
                oHero.SyncWeaponChange()

    
    def OnItemPos(self, oItem, iPos):
        oHero = self.GetOwner()
        if oHero:
            oHero.GS2CPropChange('Desc')
            oCurWeapon = self.GetCurWeapon()
            if oItem.m_ID == oCurWeapon.m_ID:
                self.SetWeaponChangeSign(CURWEAPON_POS)
                oHero.SyncWeaponChange()

    
    def IsValidPos(self, oItem, iPos, iReplace = 0):
        iItemType = oItem.ClassType()
        if iItemType not in self.m_Type2Pos:
            return 0
        if iPos not in self.m_Type2Pos[iItemType]:
            return 0
        if not iReplace and iPos in self.m_Item:
            return 0
        return 1

    
    def GetValidPos(self, oItem):
        iItemType = oItem.ClassType()
        if iItemType not in self.m_Type2Pos:
            return 0
        tPos = self.m_Type2Pos[iItemType]
        for iPos in tPos:
            if iPos not in self.m_Item:
                return iPos
        
        return 0

    
    def GetAllValidPos(self, oItem):
        iItemType = oItem.ClassType()
        if iItemType not in self.m_Type2Pos:
            return []
        lstPos = []
        tPos = self.m_Type2Pos[iItemType]
        for iPos in tPos:
            if iPos not in self.m_Item:
                lstPos.append(iPos)
        
        return lstPos

    
    def GetCurWeapon(self, iHoldPos = MAIN_HOLD):
        lstItem = self.GetAllItemByMask(EQUIP_MASK_WEAPON)
        for oItem in lstItem:
            if oItem.GetComponent('Hold').HoldPos() == iHoldPos:
                return oItem
        

    
    def GetCurWeaponPos(self, iHoldPos = MAIN_HOLD):
        oItem = self.GetCurWeapon(iHoldPos)
        if not oItem:
            return 0
        return oItem.m_Pos

    
    def GetMainWeaponByPos(self, iPos):
        lstItem = self.GetAllItemByMask(EQUIP_MASK_WEAPON)
        for oItem in lstItem:
            if oItem.m_Pos == iPos:
                return oItem
        

    
    def GetCurWeaponName(self):
        oItem = self.GetCurWeapon()
        if oItem:
            return oItem.m_Name
        return '拳头'

    
    def IsCanHoldPos(self, iPos, iHoldPos = MAIN_HOLD):
        if iPos not in self.m_Pos2Type:
            return 0
        if self.m_Pos2Type[iPos] & EQUIP_TYPE_MAINWEAPON == EQUIP_TYPE_MAINWEAPON:
            return 1
        if iHoldPos == MAIN_HOLD and self.m_Pos2Type[iPos] == EQUIP_TYPE_FUNDAMENTALWEAPON:
            return 1
        return 0

    
    def GetPosType(self, iPos):
        if iPos not in self.m_Pos2Type:
            return 0
        return self.m_Pos2Type[iPos]

    
    def OnSetCurWeapon(self, iChangeType, iHoldPos = MAIN_HOLD):
        oHero = self.GetOwner()
        self.SetWeaponChangeSign(iChangeType)
        oHero.SyncWeaponChange(iHoldPos)

    
    def SetCurWeapon(self, iPos, iChangeType):
        if not self.IsCanHoldPos(iPos):
            return 0
        if iPos not in self.m_Item:
            return 0
        oOldItem = self.GetCurWeapon()
        if oOldItem:
            oOldItem.GetComponent('Hold').Unhold()
        oItem = self.m_Item[iPos]
        oItem.GetComponent('Hold').Hold(MAIN_HOLD)
        self.OnSetCurWeapon(iChangeType)
        return 1

    
    def ValidOpenDualWield(self):
        oMainWeapon = self.GetCurWeapon()
        if not oMainWeapon or oMainWeapon.Type() & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON or not (oMainWeapon.m_CanDoubleHold):
            return False
        iDeputyPos = self.m_MainDeputyPos[oMainWeapon.m_Pos]
        oDeputy = self.GetItemByPos(iDeputyPos)
        if not oDeputy or oDeputy.GetComponent('Hold').IsHold() or not (oDeputy.m_CanDoubleHold):
            return False
        return True

    
    def GetDeputyPosWeapon(self):
        iCurPos = self.GetCurWeaponPos()
        if not iCurPos:
            return None
        iDeputyPos = self.m_MainDeputyPos[iCurPos]
        oDeputy = self.GetItemByPos(iDeputyPos)
        return oDeputy

    
    def SetDeputyWeapon(self, iWeapon, iChangeType):
        oWeapon = self.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oOldItem = self.GetCurWeapon(DEPUTY_HOLD)
        if oOldItem:
            oOldItem.GetComponent('Hold').Unhold()
        oWeapon.GetComponent('Hold').Hold(DEPUTY_HOLD)
        self.OnSetCurWeapon(iChangeType, DEPUTY_HOLD)

    
    def ClearDeputyWeapon(self):
        oWeapon = self.GetCurWeapon(DEPUTY_HOLD)
        if oWeapon:
            oWeapon.GetComponent('Hold').Unhold()
        self.OnSetCurWeapon(CURWEAPON_POS, DEPUTY_HOLD)

    
    def GetHoldWeapon(self, tHoldPos = None):
        lstItem = self.GetAllItemByMask(EQUIP_MASK_WEAPON)
        lstRet = []
        for oItem in lstItem:
            oHoldCom = oItem.GetComponent('Hold')
            iHoldPos = oHoldCom.HoldPos()
            if not iHoldPos or not tHoldPos:
                if iHoldPos in tHoldPos:
                    lstRet.append((oItem, iHoldPos))
                    continue
        
        return lstRet

    
    def IsWeaponPosHolded(self, iHoldPos = MAIN_HOLD):
        lstItem = self.GetAllItemByMask(EQUIP_MASK_WEAPON)
        for oItem in lstItem:
            oHoldCom = oItem.GetComponent('Hold')
            iHPos = oHoldCom.HoldPos()
            if iHPos and iHPos & iHoldPos:
                iHoldPos = iHoldPos & ~iHPos
            if iHoldPos == 0:
                break
        
        return iHoldPos == 0

    
    def RefreshCurWeapon(self):
        oCurWeapon = self.GetCurWeapon()
        if oCurWeapon:
            return None
        for oItem in self.GetAllItemByMask(EQUIP_MASK_WEAPON):
            if oItem.IsInitWeapon():
                continue
            if self.SetCurWeapon(oItem.m_Pos, CURWEAPON_SWITCH):
                return None
        
        iPos = self.m_Type2Pos[EQUIP_TYPE_FUNDAMENTALWEAPON][0]
        self.SetCurWeapon(iPos, CURWEAPON_SWITCH)

    
    def ItemValidPosByItem(self, oItem):
        iType = oItem.ClassType()
        if iType not in self.m_Type2Pos:
            return []
        return self.m_Type2Pos[iType]

    
    def GetItemByType(self, iItemType):
        if iItemType not in self.m_Type2Pos:
            return None
        for iPos in self.m_Type2Pos[iItemType]:
            oItem = self.GetItemByPos(iPos)
            if not oItem:
                continue
            return oItem
        

    
    def GetAllItemByType(self, iItemType):
        if iItemType not in self.m_Type2Pos:
            return []
        lstItem = []
        for iPos in self.m_Type2Pos[iItemType]:
            oItem = self.GetItemByPos(iPos)
            if not oItem:
                continue
            lstItem.append(oItem)
        
        return lstItem

    
    def GetAllItemIDByType(self, iItemType):
        if iItemType not in self.m_Type2Pos:
            return []
        lstItemID = []
        for iPos in self.m_Type2Pos[iItemType]:
            oItem = self.GetItemByPos(iPos)
            if not oItem:
                continue
            lstItemID.append(oItem.m_ID)
        
        return lstItemID

    
    def GetAllItemByMask(self, iItemMask):
        lstItem = []
        for oItem in self.m_Item.values():
            if oItem.m_Type & iItemMask:
                lstItem.append(oItem)
        
        return lstItem

    
    def CurWeaponDesc(self, iHoldType):
        oItem = self.GetCurWeapon(iHoldType)
        if not oItem:
            return [
                0,
                0,
                0,
                0]
        return [
            oItem.m_Pos,
            oItem.m_SID,
            self.m_WeaponChangeSign,
            oItem.m_ID]

    
    def GetAllItemDesc(self, oOwner):
        lstItem = []
        for iPos in range(1, DESC_NUM + 1, 1):
            iShape = 0
            if iPos in self.m_Item:
                oItem = self.m_Item[iPos]
                iShape = oItem.Shape()
            lstItem.append(iShape)
        
        return lstItem

    
    def GetWeapons(self, iFlag = 0, iLimitTag = 0):
        lstWeapon = []
        if not iFlag:
            tHoldType = (MAIN_HOLD, DEPUTY_HOLD)
        elif iFlag == -1:
            tHoldType = (0,)
        else:
            tHoldType = (iFlag,)
        for oEquip in self.m_Item.values():
            if not oEquip.m_Type & (EQUIP_TYPE_MAINWEAPON | EQUIP_TYPE_FUNDAMENTALWEAPON):
                continue
            if oEquip.GetComponent('Hold').HoldPos() not in tHoldType:
                continue
            if iLimitTag and iLimitTag not in oEquip.m_ClassifyTag:
                continue
            lstWeapon.append(oEquip)
        
        return lstWeapon

    
    def GetAssistantWeapon(self):
        lstWeapon = self.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        tHoldType = (0, DEPUTY_HOLD)
        for oWeapon in lstWeapon:
            if oWeapon.GetComponent('Hold').HoldPos() in tHoldType:
                return oWeapon
        

    
    def SaveEquip(self):
        dEquip = { }
        for oEquip in self.m_Item.values():
            dEquip[oEquip.m_Pos] = oEquip.Save()
        
        return dEquip

    
    def LoadEquip(self, dData):
        oGame = self.m_Game
        
        try:
            for iPos, dEquip in dData.items():
                iSuccess = 0
                oEquip = cl_item.CreateEquip(oGame, dEquip['SID'], cl_item.GetBaseGrade(dEquip), dEquip.get('ID', 0))
                if oEquip and oEquip.IsInitWeapon():
                    oFundWeapon = self.GetItemByType(EQUIP_TYPE_FUNDAMENTALWEAPON)
                    if oFundWeapon:
                        iSuccess = 1
                        self.ItemReplace(oFundWeapon, oEquip)
                        oFundWeapon.Release()
                if not iSuccess:
                    self.AddItem(oEquip, iPos)
                oEquip.Load(dEquip)
            
        except:
            PythonError()

        self.RefreshCurWeapon()



class CItemContainer(CContainer):
    m_BagType = BAG_TYPE_ITEM
    m_InitCarryNum = 200
    m_CanExtendSize = 0
    
    def GetAllItemByType(self, iType):
        lstItem = []
        for oItem in self.m_Item.values():
            if oItem.Type() & iType == iType:
                lstItem.append(oItem)
        
        return lstItem

    
    def SubItemAmountBySID(self, iSid, iCnt, sReason):
        iAll = iCnt
        lstUnFull = self.GetUnFullItemListBySID(iSid)
        for oItem in lstUnFull:
            iSub = self.SubItemAmount(iCnt, oItem.m_ID, sReason)
            iCnt -= iSub
            if iCnt <= 0:
                return iAll - iCnt
        
        for oItem in self.GetAllItemBySID(iSid):
            iSub = self.SubItemAmount(iCnt, oItem.m_ID, sReason)
            iCnt -= iSub
            if iCnt <= 0:
                return iAll - iCnt
        
        if iCnt > 0:
            RaiseError('%d Sub Item %d remain %d %s' % (self.m_Owner, iSid, iCnt, sReason))
        return iAll - iCnt

    
    def SortOutItem(self, iSID):
        lstUnFull = self.GetUnFullItemListBySID(iSID)
        if not lstUnFull:
            return None
        iLen = len(lstUnFull)
        iMaxAmount = lstUnFull[0].GetMaxAmount()
        iHeadItem = 0
        iBackItem = iLen - 1
        oHeadItem = lstUnFull[iHeadItem]
        oBackItem = lstUnFull[iBackItem]
        sReason = '整理合并'
        for _ in range(iLen):
            if iBackItem <= iHeadItem:
                return None
            iHeadAmount = oHeadItem.Amount()
            iBackAmount = oBackItem.Amount()
            iNeedAmount = iMaxAmount - iHeadAmount
            if iNeedAmount >= iBackAmount:
                self.RemoveItem(oBackItem, sReason)
                iBackItem -= 1
                oBackItem = lstUnFull[iBackItem]
                iAddAmount = iBackAmount
            else:
                oBackItem.AddAmount(-iNeedAmount, sReason)
                self.GS2CItemAmount(oBackItem)
                iAddAmount = iNeedAmount
            oHeadItem.AddAmount(iAddAmount, sReason)
            self.GS2CItemAmount(oHeadItem)
            if oHeadItem.Amount() == iMaxAmount:
                iHeadItem += 1
                oHeadItem = lstUnFull[iHeadItem]
        

    
    def GetUnFullItemListBySID(self, iSID):
        lstItem = self.GetAllItemBySID(iSID)
        if not lstItem:
            return []
        lstUnFull = []
        iMaxAmount = lstItem[0].GetMaxAmount()
        for oItem in lstItem:
            if oItem.Amount() < iMaxAmount:
                lstUnFull.append(oItem)
        
        return lstUnFull

    
    def CompactItem(self):
        iIndex = 0
        for iPos, oItem in self.m_Item.items():
            iIndex += 1
            if iPos == iIndex:
                continue
            self.ItemPos(oItem, iIndex)
        



class CExWeaponContainer(CContainer):
    m_BagType = BAG_TYPE_EXWEAPON
    m_InitCarryNum = 3
    
    def IsValidPos(self, oItem, iPos, iReplace = 0):
        if not iReplace and iPos in self.m_Item:
            return 0
        if iPos > self.m_InitCarryNum:
            return 0
        return 1

    
    def SaveEquip(self):
        dEquip = { }
        for oEquip in self.m_Item.values():
            dEquip[oEquip.m_Pos] = oEquip.Save()
        
        return dEquip

    
    def SetInitCarryNum(self, iNum):
        self.m_InitCarryNum = iNum

    
    def LoadEquip(self, dData):
        oGame = self.m_Game
        
        try:
            for iPos, dEquip in dData.items():
                oEquip = cl_item.CreateEquip(oGame, dEquip['SID'], cl_item.GetBaseGrade(dEquip), dEquip.get('ID', 0))
                self.AddItem(oEquip, iPos)
                oEquip.Load(dEquip)
            
        except:
            PythonError()


    
    def OnAddItem(self, oItem, iPos):
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDWEAPONCOM, oHero, {
                'Weapon': oItem,
                'BagType': self.m_BagType })

    
    def OnRemoveItem(self, oItem, sReason):
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEWEAPONCOM, oHero, {
                'Weapon': oItem,
                'BagType': self.m_BagType })



class CWeaponStoreContainer(CContainer):
    m_BagType = BAG_TYPE_WEAPONSTORE
    m_InitCarryNum = 16
    m_SaveAttr = [
        'Att',
        'Trajectory',
        'CrazyEff',
        'DebuffProb',
        'MaxBullet',
        'FillTime',
        'AttSpeed',
        'LuckyHit']
    m_ShowGrade = 0
    
    def __init__(self, oGame, iOwner):
        super(CWeaponStoreContainer, self).__init__(oGame, iOwner)
        self.m_LevelSavePos = []
        self.m_LoadFlag = 0

    
    def IsValidPos(self, oItem, iPos, iReplace = 0):
        if not iReplace and iPos in self.m_Item:
            return 0
        if iPos > self.m_InitCarryNum:
            return 0
        return 1

    
    def SetInitCarryNum(self, iNum):
        self.m_InitCarryNum = iNum

    
    def SaveEquip(self):
        dEquip = { }
        for oEquip in self.m_Item.values():
            dEquip[oEquip.m_Pos] = oEquip.Save()
        
        return dEquip

    
    def LoadEquip(self, dData, bInit = False):
        oHero = self.GetOwner()
        
        try:
            (dWeaponDataCheck, lstReSave) = CheckWeaponData(oHero.m_PlayerID, dData)
            DealWeaponChangeData(self.m_Game, oHero.m_PlayerID, dWeaponDataCheck, lstReSave)
            for iPos, dEquip in dWeaponDataCheck.items():
                iID = 0 if bInit else dEquip.get('ID', 0)
                oEquip = cl_item.CreateEquip(self.m_Game, dEquip['SID'], cl_item.GetBaseGrade(dEquip), iID)
                oEquip.Load(dEquip)
                if bInit:
                    oHero.m_WeaponSkinCon.SetWeaponShapBySkin(oEquip)
                self.AddItem(oEquip, iPos)
            
            if lstReSave:
                oHero.Set('WeaponStore', dWeaponDataCheck)
                dSaveData = self.GetWeaponSaveInfo(lstReSave)
                self.SaveWeaponToPlayerInfo(dSaveData)
        except:
            0
            PythonError()

        self.m_LoadFlag = 1
        self.m_LevelSavePos = []

    
    def GetWeaponSaveInfo(self, lstPos):
        dSaveData = { }
        for iPos in lstPos:
            dSaveData[iPos] = { }
            oWeapon = self.GetItemByPos(iPos)
            if not oWeapon:
                continue
            dSaveWeaponData = self.GetWeaponItemSaveInfo(oWeapon)
            dSaveData[iPos] = dSaveWeaponData
        
        return dSaveData

    
    def SaveWeaponToPlayerInfo(self, dSaveData):
        self.m_Game.m_WarMgr.HandleWeaponStoreSave(self.GetOwner().m_PlayerID, dSaveData)

    
    def OnAddItem(self, oItem, iPos):
        if iPos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(iPos)
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDWEAPONCOM, oHero, {
                'Weapon': oItem,
                'BagType': self.m_BagType })

    
    def OnRemoveItem(self, oItem, sReason):
        if oItem.m_Pos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(oItem.m_Pos)
        oHero = self.GetOwner()
        if oHero:
            oItem.Set('WeaponStoreSourcePos', (oHero.m_PlayerID, oItem.m_Pos))
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEWEAPONCOM, oHero, {
                'Weapon': oItem,
                'BagType': self.m_BagType })

    
    def ItemChange(self, oSrc, oDest):
        super().ItemChange(oSrc, oDest)
        if oSrc.m_Pos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(oSrc.m_Pos)
        if oDest.m_Pos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(oDest.m_Pos)

    
    def ItemPos(self, oItem, iPos):
        super().ItemPos(oItem, iPos)
        if oItem.m_Pos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(oItem.m_Pos)
        if iPos not in self.m_LevelSavePos:
            self.m_LevelSavePos.append(iPos)

    
    def GetEmptyPos(self):
        if len(self.m_Item) >= self.m_InitCarryNum:
            return []
        lstEmptyPos = []
        for iPos in range(1, self.m_InitCarryNum + 1):
            if not iPos not in self.m_Item:
                if not self.m_Item[iPos]:
                    lstEmptyPos.append(iPos)
                    continue
        
        return lstEmptyPos



def CheckWeaponData(pid, dWeaponData):
    lstReSave = []
    dWeaponDataCheck = { }
    lstAllPutWeapon = cl_putdata.GetAllPutWeapon()
    for iPos, dWeapon in dWeaponData.items():
        (dWeapon, iResult) = CheckWeapon(dWeapon, lstAllPutWeapon, pid)
        if iResult:
            lstReSave.append(iPos)
        if dWeapon:
            dWeaponDataCheck[iPos] = dWeapon
    
    return (dWeaponDataCheck, lstReSave)


def CheckCompensateWeaponData(pid, dCompensateData):
    lstAllPutWeapon = cl_putdata.GetAllPutWeapon()
    dCompensateWeaponCheck = { }
    iReSave = 0
    for iSecond, lstWeaponData in dCompensateData.items():
        lstResultData = []
        for dWeapon in lstWeaponData:
            (dWeapon, iResult) = CheckWeapon(dWeapon, lstAllPutWeapon, pid)
            lstResultData.append(dWeapon)
            if iResult:
                iReSave = 1
                WeaponstoreLog.Info('%d %d compenstateweapon check:%s' % (pid, iSecond, lstWeaponData))
        
        dCompensateWeaponCheck[iSecond] = lstResultData
    
    return (dCompensateWeaponCheck, iReSave)


def CheckWeapon(dWeapon, lstAllPutWeapon, pid):
    iResult = 0
    iWeapon = dWeapon['SID']
    if iWeapon not in lstAllPutWeapon:
        WeaponstoreLog.Info('no put weapon:%d %d' % (iWeapon, pid))
        return ({ }, 1)
    clsWeapon = cl_item.GetItemCls(iWeapon)
    if clsWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
        WeaponstoreLog.Info('fundament weapon:%d %d' % (iWeapon, pid))
        return ({ }, 1)
    dEnhance = dWeapon['Com']['Enhance']['EH']
    dInscription = dWeapon['Com']['Inscription']
    lstInscription = dInscription['Inscription']
    (lstInscriptionCheck, iInscriptionResult) = CheckInscription(lstInscription, clsWeapon, pid)
    (dEnhanceCheck, idEnhanceResult) = CheckEnhance(dEnhance, clsWeapon, pid)
    if 'SealedIns' in dInscription:
        (lstSealedInscription, iSealedResult) = CheckSealedInscription(dInscription['SealedIns'], lstInscription, clsWeapon, pid)
        if iSealedResult:
            dInscription['SealedIns'] = lstSealedInscription
            iResult = 1
    if 'DisableIns' in dInscription:
        lstDisableInscription = dInscription['DisableIns']
        (lstDisableCheck, iDisableResult) = CheckDisableInscription(lstDisableInscription, lstInscription, clsWeapon, pid)
        if iDisableResult:
            dInscription['DisableIns'] = lstDisableCheck
            iResult = 1
    if iInscriptionResult:
        dInscription['Inscription'] = lstInscriptionCheck
        iResult = 1
    if idEnhanceResult:
        dWeapon['Com']['Enhance']['EH'] = dEnhanceCheck
        iResult = 1
    return (dWeapon, iResult)


def CheckInscription(lstInscription, clsWeapon, pid):
    lstCheck = []
    iResult = 0
    iNum = len(lstInscription)
    if iNum > MAX_INSCRIPTION_NUM:
        WeaponstoreLog.Info('invalid inscription num:%d %d' % (iNum, pid))
        return ([], 1)
    dAllInscription = GetInscriptionLib()
    iGeminiNum = 0
    iExclusiveNum = 0
    for iInscription in lstInscription:
        clsPerform = cl_perform.GetPerformModule(iInscription)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            WeaponstoreLog.Info('error inscription :%d %d' % (iInscription, pid))
            iResult = 1
            continue
        if clsPerform.m_InscriptionType == INSCRIPTION_TYPE_GEMINI:
            iGeminiNum += 1
        elif clsPerform.m_InscriptionType == INSCRIPTION_TYPE_EXCLUSIVE:
            iExclusiveNum += 1
        dGeminiInscription = dAllInscription[clsPerform.m_InscriptionType]
        if iInscription not in dGeminiInscription or not dGeminiInscription[iInscription]:
            WeaponstoreLog.Info('no put inscription :%d %d' % (iInscription, pid))
            iResult = 1
            continue
        if not clsPerform.CheckValidItem(clsWeapon, lstCheck):
            WeaponstoreLog.Info('inscription checkvalid fail:%d %d' % (iInscription, pid))
            iResult = 1
            continue
        lstCheck.append(iInscription)
    
    if iGeminiNum > GEMINI_NUM:
        lstCheck = []
        iResult = 1
        WeaponstoreLog.Info('invalid geminiinscription num:%d %d' % (iGeminiNum, pid))
    if iExclusiveNum > EXCLUSIVE_NUM:
        lstCheck = []
        iResult = 1
        WeaponstoreLog.Info('invalid exclusiveinscription num:%d %d' % (iExclusiveNum, pid))
    return (lstCheck, iResult)


def CheckEnhance(dEnhance, clsWeapon, pid):
    dEnhanceCheck = { }
    iResult = 0
    iNum = len(dEnhance)
    if iNum > MAX_ENHANCE_NUM:
        WeaponstoreLog.Info('invalid enhance num:%s %s' % (iNum, pid))
        return ({ }, 1)
    for iEnhance, dAttr in dEnhance.items():
        clsPerform = cl_perform.GetPerformModule(iEnhance)
        if not clsPerform:
            WeaponstoreLog.Info('error enhance :%s %s' % (iEnhance, pid))
            iResult = 1
            continue
        iCheck = 1
        for sAttr, tData in dAttr.items():
            if sAttr not in clsPerform.m_EnhanceAttr:
                iCheck = 0
                break
            (iMinMul, iMaxMul, iMinAdd, iMaxAdd) = clsPerform.m_EnhanceAttr[sAttr]
            (iMul, iAdd) = tData
            if not iMul < iMinMul or iMul > iMaxMul or iAdd < iMinAdd:
                if iAdd > iMaxAdd:
                    WeaponstoreLog.Info('enhance %s attr %s value error %s %s %s' % (iEnhance, sAttr, tData, clsPerform.m_EnhanceAttr[sAttr], pid))
                    iCheck = 0
                    break
        
        if not iCheck:
            iResult = 1
            continue
        dEnhanceCheck[iEnhance] = dAttr
    
    return (dEnhanceCheck, iResult)


def CheckSealedInscription(lstInscription, lstHasInscription, clsWeapon, pid):
    iResult = 0
    for iIndex, iInscription in enumerate(lstInscription):
        if iInscription not in GetInscritionPool(SEALEDINSCRIPTION_POOL[iIndex]) or iInscription in lstHasInscription:
            iResult = 1
            break
        clsPerform = cl_perform.GetPerformModule(iInscription)
        if not clsPerform.CheckValidItem(clsWeapon, lstHasInscription):
            iResult = 1
            break
    
    if not iResult:
        return (lstInscription, iResult)
    WeaponstoreLog.Info('%s %s err sealedinscription %s %s' % (pid, clsWeapon.m_SID, lstInscription, lstHasInscription))
    return ([], iResult)


def CheckDisableInscription(lstInscription, lstHasInscription, clsWeapon, pid):
    iResult = 0
    lstCheck = []
    for iInscription in lstInscription:
        if iInscription not in lstHasInscription:
            WeaponstoreLog.Info('%s %s no has disableinscription %s %s' % (pid, clsWeapon.m_SID, iInscription, lstHasInscription))
            iResult = 1
            continue
        lstCheck.append(iInscription)
    
    return (lstCheck, iResult)


def DealWeaponChangeData(oGame, pid, dWeaponData, lstReSave):
    for iPos, dWeapon in dWeaponData.items():
        iWeapon = dWeapon['SID']
        clsWeapon = cl_item.GetItemCls(iWeapon)
        dEnhance = dWeapon['Com']['Enhance']['EH']
        dEnhanceCheck = { }
        iChange = 0
        for iEnhance, dAttr in dEnhance.items():
            iReplaceEnhance = DealInvalidEnhance(oGame, pid, iEnhance, clsWeapon, dEnhanceCheck)
            if iReplaceEnhance:
                WeaponstoreLog.Info('%d replace validenhance from %d to %d' % (pid, iEnhance, iReplaceEnhance))
                iChange = 1
                continue
            dEnhanceCheck[iEnhance] = dAttr
        
        if iChange:
            dWeapon['Com']['Enhance']['EH'] = dEnhanceCheck
            if iPos not in lstReSave:
                lstReSave.append(iPos)
    


def DealInvalidEnhance(oGame, pid, iEnhance, clsWeapon, dEnhanceCheck):
    if oGame:
        from cl_only import ChooseKey, Functor
        choosefunc = Functor(ChooseKey, oGame)
        randomfunc = oGame.Random
    else:
        from only import ChooseKey, Random, Functor
        choosefunc = Functor(ChooseKey)
        randomfunc = Random
    dAllEnhance = GetWeaponEnhanceLib()
    iReChoose = 0
    clsPerform = cl_perform.GetPerformModule(iEnhance)
    if iEnhance in dAllEnhance and not dAllEnhance[iEnhance]:
        WeaponstoreLog.Info('%d enhance wight fail:%d' % (pid, iEnhance))
        iReChoose = 1
    if not clsPerform.CheckValidItem(clsWeapon, dEnhanceCheck):
        WeaponstoreLog.Info('%d enhance checkvalid fail:%d' % (pid, iEnhance))
        iReChoose = 1
    if iReChoose:
        dWeight = { }
        for iSID, iWeight in dAllEnhance.items():
            if iSID in dEnhanceCheck:
                continue
            clsPerform = cl_perform.GetPerformModule(iSID)
            if not clsPerform.CheckValidItem(clsWeapon, dEnhanceCheck):
                continue
            dWeight[iSID] = iWeight
        
        iNewEnhance = choosefunc(dWeight)
        dAttr = { }
        dAllAttr = cl_perform.GetPerformClassAttr(iNewEnhance, 'm_EnhanceAttr')
        for sAttr, (iMulMin, iMulMax, iAddMin, iAddMax) in dAllAttr.items():
            if sAttr in dAttr:
                (iMul, iAdd) = dAttr[sAttr]
                continue
            iMul = 0
            if iMulMin < iMulMax:
                iMul = randomfunc((iMulMax - iMulMin) + 1) + iMulMin
                iMul = (iMul // 100) * 100
            iAdd = 0
            if iAddMin < iAddMax:
                iAdd = randomfunc((iAddMax - iAddMin) + 1) + iAddMin
            dAttr[sAttr] = (iMul, iAdd)
        
        dEnhanceCheck[iNewEnhance] = dAttr
        return iNewEnhance
    return 0

