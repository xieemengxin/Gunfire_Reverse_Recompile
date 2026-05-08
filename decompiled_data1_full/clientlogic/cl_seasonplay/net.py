# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/net.pyc
# RelativePath: clientlogic/cl_seasonplay/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

import cl_duonet.dn_cl_seasonplay_net as seasonplaynet
import cl_seasonplay.net
from cl_cscommondef import CRYSTAL_MASK, MODULE_MASK

def C2GSRemoveS7Item(who, iItemID):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.RemoveS7Item(iItemID, sReason = 'c2gs', iDrop = 1)


def C2GSEquipS7Item(who, iItemID, x, y):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.EquipS7Item(x, y, iItemID)


def C2GSUnEquipS7Item(who, iItemID):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.UnEquipS7ItemByID(iItemID)


def C2GSRotateCrystal(who, iItemID):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.RotateCrystal(iItemID)


def C2GSEnableModule(who):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.AllPerformEnable()


def C2GSAutoEquip(who, iSeasonNum):
    oSeasonCon = who.m_SeasonCon
    if not oSeasonCon or oSeasonCon.m_SeasonNum != iSeasonNum:
        return None
    oSeasonCon.AutoEquip()


def C2GSAutoUnEquip(who, iSeasonNum):
    oSeasonCon = who.m_SeasonCon
    if not oSeasonCon or oSeasonCon.m_SeasonNum != iSeasonNum:
        return None
    oSeasonCon.AutoUnEquip()


def C2GSLockCrystal(who, iID, iLock):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.LockCrystal(iID, iLock)


def C2GSS7ItemOperation(who, lstItem, iOperation):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    if iOperation == 0:
        oBackpackCon.DecreaseModules(lstItem)
    elif iOperation == 1 or iOperation == 2:
        oBackpackCon.EnhanceModules(lstItem, iOperation)


def C2GSSetS7ModuleSign(who, dSignInfo):
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    oBackpackCon.UpdateSignModuleInfo(dSignInfo)


def C2GSRemoveS8Item(who, iID):
    oS8Con = who.m_S8Con
    if not oS8Con:
        return None
    oS8Con.RemoveS8Item(iID)


def C2GSEquipS8GemItem(who, iID, iPos):
    oS8Con = who.m_S8Con
    if not oS8Con:
        return None
    oS8Con.EquipGemItem(iID, iPos)


def C2GSUnEquipS8GemItem(who, iID):
    oS8Con = who.m_S8Con
    if not oS8Con:
        return None
    oS8Con.UnEquipGemItemByID(iID)


def GS2CAddS7Crystal(who, oCrystal, dPlayer = None, dExtInfo = None):
    if not dPlayer:
        return None
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    if not oCrystal:
        return None
    oGame = who.m_Game
    (x, y) = oBackpackCon.GetPos(oCrystal.m_ID)
    netData = {
        'iID': oCrystal.m_ID,
        'iSID': oCrystal.m_SID,
        'x': x,
        'y': y,
        'lstEffPoint': oCrystal.GetEffGrid(),
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer,
        'dExtraInfo': dExtInfo if dExtInfo else { } }
    seasonplaynet.DN_GS2CAddS7Crystal(netData)


def GS2CAddS7Module(who, oModule, dPlayer = None, dExtInfo = None):
    if not dPlayer:
        return None
    oBackpackCon = who.m_BackpackCon
    if not oBackpackCon:
        return None
    if not oModule:
        return None
    oGame = who.m_Game
    (x, y) = oBackpackCon.GetPos(oModule.m_ID)
    netData = {
        'iID': oModule.m_ID,
        'iSID': oModule.m_SID,
        'iQuality': oModule.m_Quality,
        'iPoint': oModule.GetPoint(),
        'x': x,
        'y': y,
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer,
        'dExtraInfo': dExtInfo if dExtInfo else { } }
    seasonplaynet.DN_GS2CAddS7Module(netData)


def GS2CRemoveS7Item(who, iS7Item, dPlayer = None):
    if not dPlayer:
        return None
    oGame = who.m_Game
    netData = {
        'iID': iS7Item,
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CRemoveS7Item(netData)


def GS2CRefreshPosPoint(who, lstPosPoint, dPlayer = None):
    if not dPlayer:
        return None
    oGame = who.m_Game
    netData = {
        'lstPosPoint': lstPosPoint,
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CRefreshPosPoint(netData)


def GS2CS7CrystalDropInfo(iDropID, oCrystal, dPlayer):
    netData = {
        'iID': iDropID,
        'lstEffPoint': oCrystal.GetEffGrid(),
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CS7CrystalDropInfo(netData)


def GS2CCComCrystalResult(pid, iCrystalID, iAddPoint):
    netData = {
        'iID': iCrystalID,
        'pid': pid,
        'iAddPoint': iAddPoint }
    seasonplaynet.DN_GS2CCComCrystalResult(netData)


def GS2CBackpackConInfo(who, iMaxRow, iMaxCol, lstLockPos, dPlayer = None):
    oGame = who.m_Game
    netData = {
        'iMaxRowNum': iMaxRow,
        'iMaxColNum': iMaxCol,
        'lstLockPos': lstLockPos,
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CBackpackConInfo(netData)


def GS2CRefreshSeasonItemAttr(who, oItem, dAttr, dPlayer):
    oGame = who.m_Game
    netData = {
        'iItemID': oItem.m_ID,
        'iItemType': oItem.m_Type,
        'dAttr': dAttr,
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CRefreshSeasonItemAttr(netData)


def GS2CS7InWarSignInfo(pid, dSignInfo):
    netData = {
        'pid': pid,
        'dSignInfo': dSignInfo }
    seasonplaynet.DN_GS2CS7InWarSignInfo(netData)


def GS2CAddS8ThirdItem(who, oItem, dPlayer):
    if not oItem or not dPlayer:
        return None
    oGame = who.m_Game
    dAttr = oItem.GetAllAttr()
    netData = {
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer,
        'iID': oItem.m_ID,
        'iSID': oItem.m_SID,
        'iQuality': oItem.m_Quality,
        'dAbility': oItem.m_Ability,
        'dAttr': dAttr }
    seasonplaynet.DN_GS2CAddS8ThirdItem(netData)


def GS2CAddS8GemItem(who, oItem, dPlayer):
    if not oItem or not dPlayer:
        return None
    oS8Con = who.m_S8Con
    if not oS8Con:
        return None
    oGame = who.m_Game
    iItem = oItem.m_ID
    netData = {
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer,
        'iID': iItem,
        'iSID': oItem.m_SID,
        'iQuality': oItem.m_Quality,
        'iPos': oS8Con.GetPos(iItem) }
    seasonplaynet.DN_GS2CAddS8GemItem(netData)


def GS2CRemoveS8Item(who, iItem, dPlayer = None):
    if not dPlayer:
        return None
    oGame = who.m_Game
    netData = {
        'oGame': oGame,
        'iHero': who.m_ID,
        'dPlayer': dPlayer,
        'iID': iItem }
    seasonplaynet.DN_GS2CRemoveS8Item(netData)


def GS2CThirdItemDropInfo(iDropID, oThirdItem, dPlayer):
    netData = {
        'iID': iDropID,
        'dAbility': oThirdItem.m_Ability,
        'dPlayer': dPlayer }
    seasonplaynet.DN_GS2CThirdItemDropInfo(netData)

