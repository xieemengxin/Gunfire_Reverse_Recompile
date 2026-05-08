# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_wand_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_wand_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_wand_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_wand.net

def DN_GS2CWandOption(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iOption'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAddWand(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iWandSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iRareLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCD'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iConditionGrooveNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBehaviorGrooveNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['bRetDot'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['bSyncOtherPlayer'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstComp']), 1)
    for iCompPos, iComp, iCompLevel, iDismantle, iSubType, iExtCallTimes in netdata['lstComp']:
        cl_duonet.netfunc.PacketAddI(iCompPos, 1)
        cl_duonet.netfunc.PacketAddI(iComp, 2)
        cl_duonet.netfunc.PacketAddI(iCompLevel, 1)
        cl_duonet.netfunc.PacketAddI(iDismantle, 1)
        cl_duonet.netfunc.PacketAddI(iSubType, 1)
        cl_duonet.netfunc.PacketAddI(iExtCallTimes, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbilities']), 1)
    for iSID, iQuality, iFloatingRange in netdata['lstAbilities']:
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iFloatingRange, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstLockWandAbility']), 1)
    for iLockWandAbility in netdata['lstLockWandAbility']:
        cl_duonet.netfunc.PacketAddI(iLockWandAbility, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCarryAbility']), 1)
    for iSID, iQuality, iFloatingRange in netdata['lstCarryAbility']:
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iFloatingRange, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CUpdateWandComp(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstComp']), 1)
    for iCompPos, iComp, iCompLevel, iDismantle, iSubType, iExtCallTimes in netdata['lstComp']:
        cl_duonet.netfunc.PacketAddI(iCompPos, 1)
        cl_duonet.netfunc.PacketAddI(iComp, 2)
        cl_duonet.netfunc.PacketAddI(iCompLevel, 1)
        cl_duonet.netfunc.PacketAddI(iDismantle, 1)
        cl_duonet.netfunc.PacketAddI(iSubType, 1)
        cl_duonet.netfunc.PacketAddI(iExtCallTimes, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CUpdateBagComp(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['WandComp']), 1)
    for iComp, CompInfo in netdata['WandComp'].items():
        cl_duonet.netfunc.PacketAddI(iComp, 2)
        cl_duonet.netfunc.PacketAddI(len(CompInfo), 1)
        for iLevel, iNum, bRetDot in CompInfo:
            cl_duonet.netfunc.PacketAddI(iLevel, 1)
            cl_duonet.netfunc.PacketAddI(iNum, 1)
            cl_duonet.netfunc.PacketAddI(bRetDot, 1)
        
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandGroupSendOption(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iOption'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CWandCastingConditions(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCDDownFrame'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCD'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstComp']), 1)
    for iCompPos, iActive in netdata['lstComp']:
        cl_duonet.netfunc.PacketAddI(iCompPos, 1)
        cl_duonet.netfunc.PacketAddI(iActive, 1)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandConditionCompCountChange(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iComp'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandCountChange(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketVarLong(netdata['iCount'])
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandCountInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketVarLong(netdata['iCurCount'])
    cl_duonet.netfunc.PacketVarLong(netdata['iMaxCount'])
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAddWandNotify(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iUpgrade'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandPropChange(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTarget'], 4)
    cl_duonet.netfunc.PacketAttr(netdata['dPropInfo'])
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CS5PackSignInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dSign']), 1)
    for type, lstSID in netdata['dSign'].items():
        cl_duonet.netfunc.PacketAddI(type, 1)
        cl_duonet.netfunc.PacketAddI(len(lstSID), 1)
        for iSID in lstSID:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWandActCompTrigger(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(14, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCompPos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNeedCount'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iEndFrame'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTime'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWandActCompInstantTrigger(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(15, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCompPos'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CDropWandAbilities(netdata):
    cl_duonet.netfunc.PacketPrepare(110)
    cl_duonet.netfunc.PacketAddI(16, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandDropID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbilities']), 1)
    for iSID, iQuality, iFloatingRange in netdata['lstAbilities']:
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iFloatingRange, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_C2GSWandOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    iWandID = cl_duonet.netfunc.UnpackInt(4)
    cl_wand.net.C2GSWandOption(who, iOption, iWandID)


def DN_C2GSWandCompOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    iWandID = cl_duonet.netfunc.UnpackInt(4)
    iCompPos = cl_duonet.netfunc.UnpackInt(1)
    iComp = cl_duonet.netfunc.UnpackInt(2)
    iLevel = cl_duonet.netfunc.UnpackInt(1)
    cl_wand.net.C2GSWandCompOption(who, iOption, iWandID, iCompPos, iComp, iLevel)


def DN_C2GSBagCompOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    iComp = cl_duonet.netfunc.UnpackInt(2)
    iLevel = cl_duonet.netfunc.UnpackInt(1)
    cl_wand.net.C2GSBagCompOption(who, iOption, iComp, iLevel)


def DN_C2GSClearWandRedDot(who):
    iWandID = cl_duonet.netfunc.UnpackInt(4)
    cl_wand.net.C2GSClearWandRedDot(who, iWandID)


def DN_C2GSClearCompRedDot(who):
    iComp = cl_duonet.netfunc.UnpackInt(2)
    iLevel = cl_duonet.netfunc.UnpackInt(1)
    cl_wand.net.C2GSClearCompRedDot(who, iComp, iLevel)


def DN_C2GSBatchRecycleBagComp(who):
    lstComp = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iComp = cl_duonet.netfunc.UnpackInt(2)
        iLevel = cl_duonet.netfunc.UnpackInt(1)
        lstComp.append((iComp, iLevel))
    
    cl_wand.net.C2GSBatchRecycleBagComp(who, lstComp)


def DN_C2GSAddS5Sign(who):
    type = cl_duonet.netfunc.UnpackInt(1)
    iSID = cl_duonet.netfunc.UnpackInt(2)
    cl_wand.net.C2GSAddS5Sign(who, type, iSID)


def DN_C2GSDelS5Sign(who):
    type = cl_duonet.netfunc.UnpackInt(1)
    iSID = cl_duonet.netfunc.UnpackInt(2)
    cl_wand.net.C2GSDelS5Sign(who, type, iSID)


def DN_C2GSQuickAddComp(who):
    iWandID = cl_duonet.netfunc.UnpackInt(4)
    lstComp = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iCompPos = cl_duonet.netfunc.UnpackInt(1)
        iComp = cl_duonet.netfunc.UnpackInt(2)
        iLevel = cl_duonet.netfunc.UnpackInt(1)
        lstComp.append((iCompPos, iComp, iLevel))
    
    cl_wand.net.C2GSQuickAddComp(who, iWandID, lstComp)


def DN_C2GSLockWandAbility(who):
    iWandID = cl_duonet.netfunc.UnpackInt(4)
    iAbility = cl_duonet.netfunc.UnpackInt(2)
    iLock = cl_duonet.netfunc.UnpackInt(1)
    cl_wand.net.C2GSLockWandAbility(who, iWandID, iAbility, iLock)

