# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_dice_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_dice_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_dice_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_dice.net

def DN_GS2CRefreshDiceInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iReason'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstDiceInfo']), 1)
    for dDiceInfo in netdata['lstDiceInfo']:
        cl_duonet.netfunc.PacketMarshal(dDiceInfo, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CAddDice(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iDiceID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iQuality'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iDiceAbilitySID'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['dPointsRange']), 1)
    for iAbilityQuality, lstRange in netdata['dPointsRange'].items():
        cl_duonet.netfunc.PacketAddI(iAbilityQuality, 1)
        cl_duonet.netfunc.PacketAddI(len(lstRange), 1)
        for iPoint in lstRange:
            cl_duonet.netfunc.PacketAddI(iPoint, 1)
        
    
    cl_duonet.netfunc.PacketAddI(netdata['iRollPoint'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTime'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['bRetDot'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRollTime'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRemoveDice(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iDiceID'], 4)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRefreshMaxDiceAssemblyNum(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iExtraNum'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CSyncActiveDiceSpecialItem(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSpecialItem'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCanUseTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCurDiceEnergy'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTriggerEnergy'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceSpecialItemInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dSpecialItem']), 1)
    for iSpecialItem, iNum in netdata['dSpecialItem'].items():
        cl_duonet.netfunc.PacketAddI(iSpecialItem, 2)
        cl_duonet.netfunc.PacketAddI(iNum, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceSpecialItemResult(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iDiceID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSPItem']), 1)
    for iSpecialItem in netdata['lstSPItem']:
        cl_duonet.netfunc.PacketAddI(iSpecialItem, 2)
    
    cl_duonet.netfunc.PacketMarshal(netdata['sDiceInfo'], 2)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceSelectionPacketInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iQuality'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dDice']), 1)
    for iDiceSID, iPoint in netdata['dDice'].items():
        cl_duonet.netfunc.PacketAddI(iDiceSID, 4)
        cl_duonet.netfunc.PacketAddI(iPoint, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['dPointRange']), 1)
    for iQuality, lstPointRange in netdata['dPointRange'].items():
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(len(lstPointRange), 1)
        for iPoint in lstPointRange:
            cl_duonet.netfunc.PacketAddI(iPoint, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CUpdateUnLockAbilityDesc(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dAbilityDesc']), 1)
    for iDiceAbilitySID, lstQuality in netdata['dAbilityDesc'].items():
        cl_duonet.netfunc.PacketAddI(iDiceAbilitySID, 2)
        cl_duonet.netfunc.PacketAddI(len(lstQuality), 1)
        for iQuality in lstQuality:
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceSpecialItemGrooveInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSpecialItem']), 1)
    for iPos, iSpecialItem in netdata['lstSpecialItem']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSpecialItem, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceEnergy(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(14, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iEnergy'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iChangeReason'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CS6PackSignInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(15, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dSign']), 1)
    for type, lstSID in netdata['dSign'].items():
        cl_duonet.netfunc.PacketAddI(type, 1)
        cl_duonet.netfunc.PacketAddI(len(lstSID), 1)
        for iSID in lstSID:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceDropRollInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(16, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iDropID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPoint'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CUpdateAddUpPoint(netdata):
    cl_duonet.netfunc.PacketPrepare(108)
    cl_duonet.netfunc.PacketAddI(17, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRollPoint'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSRollDice(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    iOption = cl_duonet.netfunc.UnpackInt(1)
    cl_dice.net.C2GSRollDice(who, iDiceID, iOption)


def DN_C2GSAssembleDice(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    iOption = cl_duonet.netfunc.UnpackInt(1)
    cl_dice.net.C2GSAssembleDice(who, iDiceID, iPos, iOption)


def DN_C2GSDropDice(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    cl_dice.net.C2GSDropDice(who, iDiceID)


def DN_C2GSClearDiceRedDot(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    cl_dice.net.C2GSClearDiceRedDot(who, iDiceID)


def DN_C2GSRecycleBagDice(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    cl_dice.net.C2GSRecycleBagDice(who, iDiceID)


def DN_C2GSChooseDiceResult(who):
    iDiceID = cl_duonet.netfunc.UnpackInt(4)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    iSpecialItem = cl_duonet.netfunc.UnpackInt(2)
    cl_dice.net.C2GSChooseDiceResult(who, iDiceID, iPos, iSpecialItem)


def DN_C2GSUseDiceSpecialItem(who):
    iPos = cl_duonet.netfunc.UnpackInt(1)
    iSpecialItem = cl_duonet.netfunc.UnpackInt(2)
    lstDice = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iDiceID = cl_duonet.netfunc.UnpackInt(4)
        lstDice.append(iDiceID)
    
    cl_dice.net.C2GSUseDiceSpecialItem(who, iPos, iSpecialItem, lstDice)


def DN_C2GSAddS6Sign(who):
    type = cl_duonet.netfunc.UnpackInt(1)
    iSID = cl_duonet.netfunc.UnpackInt(2)
    cl_dice.net.C2GSAddS6Sign(who, type, iSID)


def DN_C2GSDelS6Sign(who):
    type = cl_duonet.netfunc.UnpackInt(1)
    iSID = cl_duonet.netfunc.UnpackInt(2)
    cl_dice.net.C2GSDelS6Sign(who, type, iSID)


def DN_C2GSUpdateUnLockAbilityDesc(who):
    iDiceAbilitySID = cl_duonet.netfunc.UnpackInt(2)
    iMaxUnlockQuality = cl_duonet.netfunc.UnpackInt(1)
    cl_dice.net.C2GSUpdateUnLockAbilityDesc(who, iDiceAbilitySID, iMaxUnlockQuality)

