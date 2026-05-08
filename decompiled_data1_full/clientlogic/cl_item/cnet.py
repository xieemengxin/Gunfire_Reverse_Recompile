# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/cnet.pyc
# RelativePath: clientlogic/cl_item/cnet.pyc
# Source Generated with Decompyle++
# File: cnet.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_GLOBAL, BAG_TYPE_ITEM, BAG_TYPE_WIELD, FORBID_DROPWEAPON, BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE, NWARRIOR_DROP_EQUIP
from cl_cscommondef import RAREITEM_MASK
import cl_drop
import cl_item
import cl_item.snet
import cl_msgcenter
import cl_notify
WIELD_TO_GLOBAL = 'RemoveFromWieldToGlobal'
WIELD_TO_OTHERCOM = 'RemoveFromWieldToOtherCom'

def GetInfo(oGame, oHero, iContainer, iIsFrom):
    dInfo = { }
    oContainer = None
    if iContainer == BAG_TYPE_ITEM:
        oContainer = oHero.m_ItemCon
        if iIsFrom:
            dInfo['Num'] = oGame.UnpackInt(2)
    if iContainer == BAG_TYPE_WIELD:
        oContainer = oHero.m_WieldCon
        if not iIsFrom:
            dInfo['Pos'] = oGame.UnpackInt(1)
    return (1, oContainer, dInfo)


def GetInfoList(iContainer, dInfo, iIsFrom):
    lstInfo = []
    if not iContainer == BAG_TYPE_WIELD or iIsFrom:
        lstInfo = [
            dInfo['Pos']]
    elif iContainer == BAG_TYPE_ITEM and iIsFrom:
        lstInfo = [
            dInfo['Num']]
    return lstInfo


def DropItemFromEquip(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    if oHero.IsForbid(FORBID_DROPWEAPON):
        return None
    if not oFromCon:
        return None
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem or not oItem.ValidDrop():
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, oHero, {
        'ItemID': oItem.m_ID })
    oCurWeapon = oHero.m_WieldCon.GetCurWeapon()
    oFromCon.RemoveItem(oItem, WIELD_TO_GLOBAL)
    cl_drop.DropItem(oHero, oItem, True)
    if oCurWeapon and oCurWeapon.m_ID == oItem.m_ID:
        oFromCon.RefreshCurWeapon()


def GetContainer(oHero, iContainer):
    oContainer = None
    if iContainer == BAG_TYPE_ITEM:
        oContainer = oHero.m_ItemCon
    elif iContainer == BAG_TYPE_WIELD:
        oContainer = oHero.m_WieldCon
    elif iContainer == BAG_TYPE_EXWEAPON:
        oContainer = oHero.m_ExWeaponCon
    elif iContainer == BAG_TYPE_WEAPONSTORE:
        oContainer = oHero.m_WeaponStoreCon
    return oContainer


def DropItemFromItem(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    if oHero.InDualWield():
        return None
    if not oFromCon:
        return None
    iAmount = iFromInfo
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem or not oItem.ValidDrop():
        return None
    if iAmount < oItem.Amount():
        iDropNum = iAmount
        oFromCon.SubItemAmount(iDropNum, iTarget, 'RemoveFromItemCon')
        oDropItem = cl_item.GetTemp(oItem.m_SID)
        oDropItem.SetAmount(iDropNum, 'SetDrop')
        oDropItem.SetWarPickInfo(oItem.GetWarPickInfo())
        oFromCon.SortOutItem(oItem.m_SID)
    else:
        oFromCon.RemoveItem(oItem, 'RemoveFromItemCon')
        oDropItem = oItem
    cl_drop.DropItem(oHero, oItem, True)


def ChangeEquipPos(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    if oHero.InDualWield():
        return None
    if oFromCon is not oHero.m_WieldCon:
        return None
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem or not oFromCon.IsValidPos(oItem, iToInfo, 1):
        return None
    oSrc = oFromCon.GetItem(iToInfo)
    if not oSrc:
        oFromCon.ItemPos(oItem, iToInfo)
    else:
        oFromCon.ItemChange(oSrc, oItem)


def UnwieldEquip(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    if oHero.InDualWield():
        return None
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem:
        return None
    oHoldCom = oItem.GetComponent('Hold')
    if oHoldCom and oHoldCom.IsHold():
        return None
    iToPos = iToInfo
    iFromPos = oItem.m_Pos
    oSrc = oToCon.GetItem(iToPos)
    if oSrc and not oFromCon.IsValidPos(oSrc, iFromPos, 1):
        return None
    oFromCon.RemoveItem(oItem, 'RaplaceWeapon')
    if oSrc:
        oToCon.RemoveItem(oSrc, 'RaplaceWeapon')
        oFromCon.AddItem(oSrc, iFromPos)
    oToCon.AddItem(oItem, iToPos)


def WieldEquip(oHero, oFromContainer, oToContainer, iTarget, iFromInfo, iToInfo):
    if oHero.InDualWield():
        return None
    oItem = oFromContainer.GetItemByID(iTarget)
    if not oItem:
        return None
    iToPos = iToInfo
    iFromPos = oItem.m_Pos
    oSrc = oToContainer.GetItemByPos(iToPos)
    if oSrc:
        oHoldCom = oSrc.GetComponent('Hold')
        if oHoldCom and oHoldCom.IsHold():
            return None
    if oToContainer.IsValidPos(oItem, iToPos, 1):
        oFromContainer.RemoveItem(oItem, 'RaplaceWeapon')
        if oSrc:
            oToContainer.RemoveItem(oSrc, 'RaplaceWeapon')
            oFromContainer.AddItem(oSrc, iFromPos)
        oToContainer.AddItem(oItem, iToPos)


def UseRareItem(oHero, iItemID):
    oItem = oHero.m_ItemCon.GetItemByID(iItemID)
    oGame = oHero.m_Game
    if not oItem or not (oItem.Type() & RAREITEM_MASK == RAREITEM_MASK):
        return None
    ofunc = oItem.m_UseAction
    if not ofunc:
        return None
    oHero.m_ItemCon.RemoveItem(oItem, 'UseItem')
    ofunc(oHero, oItem.m_LifeCycle)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USERAREITEM, oHero, {
        'Item': oItem })
    if oItem.m_UseNotify:
        cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), oItem.m_UseNotify, {
            '$$playername': oHero.Name() })


def AddWeaponToWeaponCon(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    iToPos = iToInfo
    oSrc = oToCon.GetItem(iToPos)
    if oSrc:
        return None
    oGame = oHero.m_Game
    oWeaponDrop = oGame.GetObject(iTarget)
    if not oWeaponDrop or oWeaponDrop.m_FightType != NWARRIOR_DROP_EQUIP or not oWeaponDrop.ValidPick(oHero):
        return None
    oItem = oWeaponDrop.m_DropInfo[0]
    sReason = 'Pick:%d-%d' % (oItem.Type(), oItem.m_SID)
    if oItem.PutToContainer([
        oToCon], sReason):
        oWeaponDrop.m_DropInfo.pop(0)
        oWeaponDrop.Remove(sReason)


def RemoveWeaponFromWeaponCon(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    if not oFromCon:
        return None
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem or not oItem.ValidDrop():
        return None
    oFromCon.RemoveItem(oItem, 'RemoveFromWeaponCon')
    cl_drop.DropItem(oHero, oItem, True)


def ChangeWeaponFromDifferentWeaponCon(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem:
        return None
    iToPos = iToInfo
    iFromPos = oItem.m_Pos
    oSrc = oToCon.GetItem(iToPos)
    oRefreshCon = None
    if oToCon.IsValidPos(oItem, iToPos, 1):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGEWEAPON_FROM_DIFFERENTWAEAPONCON, oHero, {
            'ItemID': iTarget })
        if oToCon.m_BagType == BAG_TYPE_WIELD:
            if not oSrc:
                oFromCon.RemoveItem(oItem, 'ChangeWithContainer')
            oItem.PutToContainer([
                oToCon], 'ChangeWithContainer', iToPos)
            oRefreshCon = oToCon
        elif oFromCon.m_BagType == BAG_TYPE_WIELD:
            if not oSrc:
                oFromCon.RemoveItem(oItem, WIELD_TO_OTHERCOM)
                oToCon.AddItem(oItem, iToPos)
            else:
                oSrc.PutToContainer([
                    oFromCon], 'ChangeWithContainer', iFromPos)
            oRefreshCon = oFromCon
        else:
            oFromCon.RemoveItem(oItem, 'RaplaceWeapon')
            if oSrc:
                oToCon.RemoveItem(oSrc, 'RaplaceWeapon')
                oFromCon.AddItem(oSrc, iFromPos)
            oToCon.AddItem(oItem, iToPos)
        if oRefreshCon:
            oRefreshCon.RefreshCurWeapon()


def ChangeWeaponConEquipPos(oHero, oFromCon, oToCon, iTarget, iFromInfo, iToInfo):
    oItem = oFromCon.GetItemByID(iTarget)
    if not oItem or not oFromCon.IsValidPos(oItem, iToInfo, 1):
        return None
    oSrc = oFromCon.GetItem(iToInfo)
    if not oSrc:
        oFromCon.ItemPos(oItem, iToInfo)
    else:
        oFromCon.ItemChange(oSrc, oItem)

g_ItemOPFunc = {
    (BAG_TYPE_EXWEAPON, BAG_TYPE_EXWEAPON): ChangeWeaponConEquipPos,
    (BAG_TYPE_WIELD, BAG_TYPE_EXWEAPON): ChangeWeaponFromDifferentWeaponCon,
    (BAG_TYPE_EXWEAPON, BAG_TYPE_WIELD): ChangeWeaponFromDifferentWeaponCon,
    (BAG_TYPE_EXWEAPON, BAG_TYPE_GLOBAL): RemoveWeaponFromWeaponCon,
    (BAG_TYPE_GLOBAL, BAG_TYPE_EXWEAPON): AddWeaponToWeaponCon,
    (BAG_TYPE_WIELD, BAG_TYPE_WIELD): ChangeEquipPos,
    (BAG_TYPE_WIELD, BAG_TYPE_GLOBAL): DropItemFromEquip,
    (BAG_TYPE_ITEM, BAG_TYPE_GLOBAL): DropItemFromItem }

def C2GSItemContainerOp(oHero, iFromContainer, iToContainer, iTarget, iFromInfo, iToInfo):
    tKey = (iFromContainer, iToContainer)
    if tKey not in g_ItemOPFunc:
        return None
    oFromContainer = GetContainer(oHero, iFromContainer)
    oToContainer = GetContainer(oHero, iToContainer)
    g_ItemOPFunc[tKey](oHero, oFromContainer, oToContainer, iTarget, iFromInfo, iToInfo)


def C2GSUseRareItem(oHero, iItemID):
    UseRareItem(oHero, iItemID)


def C2GSChangeItemMode(oHero, iContainer, iItemID, iMode, iStatus):
    oContainer = GetContainer(oHero, iContainer)
    oItem = oContainer.GetItemByID(iItemID)
    if not oItem:
        return None
    oItem.ChangeMode(iMode, iStatus)

