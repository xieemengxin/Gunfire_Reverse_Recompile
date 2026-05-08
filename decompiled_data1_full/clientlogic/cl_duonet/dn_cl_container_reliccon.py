# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_container_reliccon.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_container_reliccon.pyc
# Source Generated with Decompyle++
# File: dn_cl_container_reliccon.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_container.reliccon

def DN_GS2CAddRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iValidRemove'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRollNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iValidRecycle'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iForceDisable'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNotifyType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPlaySource'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRemoveRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.DGameBroadCast(netdata['oGame'])


def DN_GS2CReplaceRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iOldRelic'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNewRelic'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAddExtraRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRandomRemoveRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRefreshRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNum'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRefreshRelicResult(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstRelic']), 1)
    for iRelicSID in netdata['lstRelic']:
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CUpdateShowQuality(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dUpdate']), 2)
    for iRelicSID, iShowQuality in netdata['dUpdate'].items():
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
        cl_duonet.netfunc.PacketAddI(iShowQuality, 1)
    
    cl_duonet.netfunc.PacketAddI(netdata['iUpgradeNum'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iUpgradeType'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAddExtendRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRollNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iValidRecycle'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRemoveExtendRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CUpdateBlankRelicNum(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRelicSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNum'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iAddNum'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CSynTempRemoveRelic(netdata):
    cl_duonet.netfunc.PacketPrepare(106)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iGamePlayType'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstRelic']), 2)
    for iRelicSID, iLevel in netdata['lstRelic']:
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_C2GSRemoveRelic(who):
    iRelicSID = cl_duonet.netfunc.UnpackInt(2)
    iOperateType = cl_duonet.netfunc.UnpackInt(1)
    cl_container.reliccon.C2GSRemoveRelic(who, iRelicSID, iOperateType)


def DN_C2GSRefreshRelic(who):
    lstRelic = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iRelicSID = cl_duonet.netfunc.UnpackInt(2)
        lstRelic.append(iRelicSID)
    
    cl_container.reliccon.C2GSRefreshRelic(who, lstRelic)


def DN_C2GSExchangeExtendRelic(who):
    iType = cl_duonet.netfunc.UnpackInt(1)
    iRelicSID = cl_duonet.netfunc.UnpackInt(2)
    cl_container.reliccon.C2GSExchangeExtendRelic(who, iType, iRelicSID)


def DN_C2GSHandleTempRemoveRelic(who):
    iGamePlayType = cl_duonet.netfunc.UnpackInt(1)
    lstRelic = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iRelicSID = cl_duonet.netfunc.UnpackInt(2)
        iType = cl_duonet.netfunc.UnpackInt(1)
        lstRelic.append((iRelicSID, iType))
    
    cl_container.reliccon.C2GSHandleTempRemoveRelic(who, iGamePlayType, lstRelic)

