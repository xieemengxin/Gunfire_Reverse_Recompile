# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_notify.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_notify.pyc
# Source Generated with Decompyle++
# File: dn_cl_notify.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_notify

def DN_GS2CGMNotify(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iErr'], 1)
    cl_duonet.netfunc.PacketAddBinaryS(netdata['sMsg'], 0)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CDebugMsg(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddSL(netdata['sMsg'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CCenterTopFloatMsg(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddPSL(netdata['sMsg'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CCommonNotify(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddPSL(netdata['sMsg'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTime'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CChat(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddSL(netdata['sMsg'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSender'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CUnLockItem(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRewardSID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CWarConfirm(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(netdata['MenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['ConfirmID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['ButtonCnt'], 1)
    cl_duonet.netfunc.PacketAddSL(netdata['TypeStr'], 1)
    cl_duonet.netfunc.PacketAddSL(netdata['User'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAdjustWeapon(netdata):
    cl_duonet.netfunc.PacketPrepare(86)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstWeapon']), 1)
    for iWeaponSID in netdata['lstWeapon']:
        cl_duonet.netfunc.PacketAddI(iWeaponSID, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_C2GSChat(who):
    sMsg = cl_duonet.netfunc.UnpackSL(1)
    cl_notify.C2GSChat(who, sMsg)


def DN_C2GSWarAnswerConfirm(who):
    MenuIdx = cl_duonet.netfunc.UnpackInt(2)
    Answer = cl_duonet.netfunc.UnpackInt(1)
    cl_notify.C2GSWarAnswerConfirm(who, MenuIdx, Answer)

