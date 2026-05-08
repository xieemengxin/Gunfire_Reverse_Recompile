# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_item_cnet.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_item_cnet.pyc
# Source Generated with Decompyle++
# File: dn_cl_item_cnet.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_item.cnet

def DN_GS2CItemAdd(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.PacketAttr(netdata['dInfo'])
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CItemDel(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CEquipAdd(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iBagType'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.PacketAttr(netdata['dInfo'])
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CEquipDel(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iBagType'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CBulletRefresh(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iBulletSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iAmount'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxAmount'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRefreshKey(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWarrior'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstKey']), 1)
    for iKeySID, iNum in netdata['lstKey']:
        cl_duonet.netfunc.PacketAddI(iKeySID, 2)
        cl_duonet.netfunc.PacketAddI(iNum, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CEmotion(netdata):
    cl_duonet.netfunc.PacketPrepare(102)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCur']), 1)
    for iIndex, iEmotion in netdata['lstCur']:
        cl_duonet.netfunc.PacketAddI(iIndex, 1)
        cl_duonet.netfunc.PacketAddI(iEmotion, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSItemContainerOp(who):
    iFromContainer = cl_duonet.netfunc.UnpackInt(1)
    iToContainer = cl_duonet.netfunc.UnpackInt(1)
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    iFromInfo = cl_duonet.netfunc.UnpackInt(4)
    iToInfo = cl_duonet.netfunc.UnpackInt(4)
    cl_item.cnet.C2GSItemContainerOp(who, iFromContainer, iToContainer, iTarget, iFromInfo, iToInfo)


def DN_C2GSUseRareItem(who):
    iItemID = cl_duonet.netfunc.UnpackInt(4)
    cl_item.cnet.C2GSUseRareItem(who, iItemID)


def DN_C2GSChangeItemMode(who):
    iContainer = cl_duonet.netfunc.UnpackInt(1)
    iItemID = cl_duonet.netfunc.UnpackInt(4)
    iMode = cl_duonet.netfunc.UnpackInt(1)
    iStatus = cl_duonet.netfunc.UnpackInt(1)
    cl_item.cnet.C2GSChangeItemMode(who, iContainer, iItemID, iMode, iStatus)

