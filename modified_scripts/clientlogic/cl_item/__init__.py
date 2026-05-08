# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/__init__.pyc
# RelativePath: clientlogic/cl_item/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
from cl_item.defines import EQUIP_MASK_DEF, EQUIP_MASK_WEAPON, EQUIP_TYPE_MAINWEAPON, ITEM_SOURCE_DEF, RAREITEM_MASK
import importlib
import cl_msgcenter
import cl_platformdata
import cl_test as cl_customconfig
if 'g_TempItem' not in globals():
    g_TempItem = { }
if 'g_ItemModule' not in globals():
    g_ItemModule = { }


def ImportdItemMod(sImport, iItemSID):

    try:
        mod = importlib.import_module('%s.i%d' % (sImport, iItemSID))
    except:
        PythonError()
        return None

    return mod


def GetItemCls(iItemSID):
    if iItemSID not in g_ItemModule:
        if cl_platformdata.IsRunPCData():
            sPath = cl_platformdata.pc.GetItemPath(iItemSID)
            sImport = 'cl_platformdata.pc.%s' % sPath
        else:
            sPath = cl_platformdata.mobile.GetItemPath(iItemSID)
            sImport = 'cl_platformdata.mobile.%s' % sPath
        if not sPath:
            return None
        mod = ImportdItemMod(sImport, iItemSID)
        if not mod:
            return None
        g_ItemModule[iItemSID] = mod
    return g_ItemModule[iItemSID].CItem


def GetAllCanSellWeapon(oGame):
    oWarMgr = oGame.m_WarMgr
    lstCanSellItem = oWarMgr.Query('CanSellWeapon', [])
    if not lstCanSellItem:
        lstCanSellItem = []
        if cl_platformdata.IsRunPCData():
            dItemPath = cl_platformdata.pc.g_ItemPath
        else:
            dItemPath = cl_platformdata.mobile.g_ItemPath
        for iItemSID, sType in dItemPath.items():
            if sType == 'weapon':
                clsItem = GetItemCls(iItemSID)
                if clsItem.m_bCanSell:
                    lstCanSellItem.append(iItemSID)

        oWarMgr.Set('CanSellWeapon', lstCanSellItem)
    return cl_customconfig.GetFilteredSequence(lstCanSellItem[:], cl_customconfig.GetWeaponWhitelist(), cl_customconfig.GetWeaponBlacklist())


def CreateEquip(oGame, iEquip, iEquipGrade = 1, iPointID = 0, oOwner = None, iSource = ITEM_SOURCE_DEF, dExtraAttr = None):
    clsItem = GetItemCls(iEquip)
    if not clsItem or not (clsItem.m_Type & (EQUIP_MASK_DEF | EQUIP_MASK_WEAPON)):
        return None
    if oOwner:
        dMsgData = {
            'Grade': iEquipGrade,
            'Source': iSource,
            'EquipSID': iEquip,
            'ExtraAttr': dExtraAttr if dExtraAttr else { } }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, oOwner, dMsgData)
        iEquipGrade = dMsgData['Grade']
        dExtraAttr = dMsgData['ExtraAttr']
    oEquip = clsItem.Create(oGame, 0, iEquipGrade, iPointID, dExtraAttr)
    if oOwner:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEWEAPON, oOwner, {
            'Weapon': oEquip,
            'Source': iSource })
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEWEAPON, oGame.GetWarMgr(), {
        'Weapon': oEquip })
    return oEquip


def CreateRareItem(oGame, iItemSID):
    clsItem = GetItemCls(iItemSID)
    if not clsItem or not (clsItem.m_Type & RAREITEM_MASK):
        return None
    oRareItem = clsItem.Create(oGame, 0)
    return oRareItem


def LoadAll():
    if cl_platformdata.IsRunPCData():
        lstAllItem = cl_platformdata.pc.GetAllItem()
    else:
        lstAllItem = cl_platformdata.mobile.GetAllItem()
    for iItemSID in lstAllItem:
        clsItem = GetItemCls(iItemSID)
        if clsItem.m_Type & (EQUIP_MASK_WEAPON | EQUIP_MASK_DEF):
            continue
        GetTemp(iItemSID)


def GetTemp(iItemSID, dData = None):
    if iItemSID in g_TempItem:
        oItem = g_TempItem[iItemSID]
        oItem.InitTemp()
    else:
        oItem = CreateTemp(None, iItemSID)
        if not oItem:
            return None
        g_TempItem[iItemSID] = oItem
    if dData:
        oItem.Load(dData)
    return oItem


def CreateTemp(oGame, iItemSID, dData = None):
    clsItem = GetItemCls(iItemSID)
    if not clsItem:
        return None
    oItem = clsItem.Create(oGame, 1)
    if not oItem:
        return None
    oItem.Create()
    if dData:
        oItem.Load(dData)
    return oItem


def Load(oGame, dData):
    if 'SID' not in dData:
        return None
    iItemSID = dData['SID']
    clsItem = GetItemCls(iItemSID)
    if not clsItem:
        return None
    oItem = clsItem.Create(oGame)
    if not oItem:
        return None
    oItem.Load(dData)
    return oItem


def GetBaseGrade(dData):
    iBaseGrade = dData.get('BaseGrade', None)
    if iBaseGrade is None:
        iBaseGrade = dData['Grade'] if 'Grade' in dData else 1
    return iBaseGrade
