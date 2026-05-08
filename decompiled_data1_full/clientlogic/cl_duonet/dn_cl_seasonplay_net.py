# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_seasonplay_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_seasonplay_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_seasonplay_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_seasonplay.net

def DN_GS2CAddS7Crystal(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['x'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['y'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstEffPoint']), 1)
    for iEffX, iEffY, iPoint in netdata['lstEffPoint']:
        cl_duonet.netfunc.PacketAddI(iEffX, 4)
        cl_duonet.netfunc.PacketAddI(iEffY, 4)
        cl_duonet.netfunc.PacketAddI(iPoint, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['dExtraInfo']), 1)
    for sKey, iValue in netdata['dExtraInfo'].items():
        cl_duonet.netfunc.PacketAddSL(sKey, 1)
        cl_duonet.netfunc.PacketAddI(iValue, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CAddS7Module(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iQuality'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPoint'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['x'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['y'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dExtraInfo']), 1)
    for sKey, iValue in netdata['dExtraInfo'].items():
        cl_duonet.netfunc.PacketAddSL(sKey, 1)
        cl_duonet.netfunc.PacketAddI(iValue, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRemoveS7Item(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRefreshPosPoint(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstPosPoint']), 1)
    for x, y, iPoint, iExtraFlag in netdata['lstPosPoint']:
        cl_duonet.netfunc.PacketAddI(x, 1)
        cl_duonet.netfunc.PacketAddI(y, 1)
        cl_duonet.netfunc.PacketAddI(iPoint, 2)
        cl_duonet.netfunc.PacketAddI(iExtraFlag, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CS7CrystalDropInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstEffPoint']), 1)
    for iEffX, iEffY, iPoint in netdata['lstEffPoint']:
        cl_duonet.netfunc.PacketAddI(iEffX, 4)
        cl_duonet.netfunc.PacketAddI(iEffY, 4)
        cl_duonet.netfunc.PacketAddI(iPoint, 2)
    
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CCComCrystalResult(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iAddPoint'], 2)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CBackpackConInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxRowNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxColNum'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstLockPos']), 1)
    for x, y, iIsNextUnlock in netdata['lstLockPos']:
        cl_duonet.netfunc.PacketAddI(x, 1)
        cl_duonet.netfunc.PacketAddI(y, 1)
        cl_duonet.netfunc.PacketAddI(iIsNextUnlock, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRefreshSeasonItemAttr(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemType'], 4)
    cl_duonet.netfunc.PacketMarshal(netdata['dAttr'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CS7InWarSignInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dSignInfo']), 1)
    for iPos, iSID in netdata['dSignInfo'].items():
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSID, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CAddS8ThirdItem(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iQuality'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dAbility']), 1)
    for iAbilitySID, iLv in netdata['dAbility'].items():
        cl_duonet.netfunc.PacketAddI(iAbilitySID, 2)
        cl_duonet.netfunc.PacketAddI(iLv, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['dAttr']), 1)
    for sAttr, iValue in netdata['dAttr'].items():
        cl_duonet.netfunc.PacketAddSL(sAttr, 1)
        cl_duonet.netfunc.PacketAddI(iValue, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CAddS8GemItem(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iQuality'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRemoveS8Item(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CThirdItemDropInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(109)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['dAbility']), 1)
    for iAbilitySID, iQuality in netdata['dAbility'].items():
        cl_duonet.netfunc.PacketAddI(iAbilitySID, 2)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
    
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_C2GSRemoveS7Item(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_seasonplay.net.C2GSRemoveS7Item(who, iID)


def DN_C2GSEquipS7Item(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    iPosX = cl_duonet.netfunc.UnpackInt(1)
    iPosY = cl_duonet.netfunc.UnpackInt(1)
    cl_seasonplay.net.C2GSEquipS7Item(who, iID, iPosX, iPosY)


def DN_C2GSUnEquipS7Item(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_seasonplay.net.C2GSUnEquipS7Item(who, iID)


def DN_C2GSRotateCrystal(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_seasonplay.net.C2GSRotateCrystal(who, iID)


def DN_C2GSEnableModule(who):
    cl_seasonplay.net.C2GSEnableModule(who)


def DN_C2GSAutoEquip(who):
    iSeasonNum = cl_duonet.netfunc.UnpackInt(1)
    cl_seasonplay.net.C2GSAutoEquip(who, iSeasonNum)


def DN_C2GSAutoUnEquip(who):
    iSeasonNum = cl_duonet.netfunc.UnpackInt(1)
    cl_seasonplay.net.C2GSAutoUnEquip(who, iSeasonNum)


def DN_C2GSLockCrystal(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    iLock = cl_duonet.netfunc.UnpackInt(2)
    cl_seasonplay.net.C2GSLockCrystal(who, iID, iLock)


def DN_C2GSS7ItemOperation(who):
    lstItem = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iID = cl_duonet.netfunc.UnpackInt(4)
        iNum = cl_duonet.netfunc.UnpackInt(1)
        lstItem.append((iID, iNum))
    
    iOperation = cl_duonet.netfunc.UnpackInt(1)
    cl_seasonplay.net.C2GSS7ItemOperation(who, lstItem, iOperation)


def DN_C2GSSetS7ModuleSign(who):
    dSignInfo = { }
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iPos = cl_duonet.netfunc.UnpackInt(1)
        iSID = cl_duonet.netfunc.UnpackInt(2)
        dSignInfo[iPos] = iSID
    
    cl_seasonplay.net.C2GSSetS7ModuleSign(who, dSignInfo)


def DN_C2GSRemoveS8Item(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_seasonplay.net.C2GSRemoveS8Item(who, iID)


def DN_C2GSEquipS8GemItem(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    cl_seasonplay.net.C2GSEquipS8GemItem(who, iID, iPos)


def DN_C2GSUnEquipS8GemItem(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_seasonplay.net.C2GSUnEquipS8GemItem(who, iID)

