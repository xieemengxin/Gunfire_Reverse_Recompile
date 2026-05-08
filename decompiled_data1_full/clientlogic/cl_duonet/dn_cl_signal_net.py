# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_signal_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_signal_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_signal_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_signal.net

def DN_GS2CAddSignal(netdata):
    cl_duonet.netfunc.PacketPrepare(77)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSceneSignal']), 1)
    for iSignalID, iSignalSID, iSecond, tPos, sAdder in netdata['lstSceneSignal']:
        cl_duonet.netfunc.PacketAddI(iSignalID, 1)
        cl_duonet.netfunc.PacketAddI(iSignalSID, 2)
        cl_duonet.netfunc.PacketAddI(iSecond, 2)
        cl_duonet.netfunc.PacketPosFloat(tPos)
        cl_duonet.netfunc.PacketAddSL(sAdder, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstObjSignal']), 1)
    for iSignalID, iSignalSID, iSecond, iAttachID, sAdder in netdata['lstObjSignal']:
        cl_duonet.netfunc.PacketAddI(iSignalID, 1)
        cl_duonet.netfunc.PacketAddI(iSignalSID, 2)
        cl_duonet.netfunc.PacketAddI(iSecond, 2)
        cl_duonet.netfunc.PacketAddI(iAttachID, 4)
        cl_duonet.netfunc.PacketAddSL(sAdder, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTeamInfoSignal']), 1)
    for iSignalID, iSignalSID, iSecond, iObjectSID, sAdder, sOwner, iObjectType in netdata['lstTeamInfoSignal']:
        cl_duonet.netfunc.PacketAddI(iSignalID, 1)
        cl_duonet.netfunc.PacketAddI(iSignalSID, 2)
        cl_duonet.netfunc.PacketAddI(iSecond, 2)
        cl_duonet.netfunc.PacketAddI(iObjectSID, 4)
        cl_duonet.netfunc.PacketAddSL(sAdder, 1)
        cl_duonet.netfunc.PacketAddSL(sOwner, 1)
        cl_duonet.netfunc.PacketAddI(iObjectType, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CDelSignal(netdata):
    cl_duonet.netfunc.PacketPrepare(77)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSignal']), 1)
    for iSignalID in netdata['lstSignal']:
        cl_duonet.netfunc.PacketAddI(iSignalID, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CSignInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(77)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSignID'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPhotoInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(77)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSignID'], 2)
    cl_duonet.netfunc.PacketPosFloat(netdata['tPos'])
    cl_duonet.netfunc.PacketPosFloat(netdata['tRotate'])
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_C2GSAddSceneSignal(who):
    iSignalSID = cl_duonet.netfunc.UnpackInt(2)
    tPos = cl_duonet.netfunc.UnpackPosFloat()
    cl_signal.net.C2GSAddSceneSignal(who, iSignalSID, tPos)


def DN_C2GSAddObjSignal(who):
    iSignalSID = cl_duonet.netfunc.UnpackInt(2)
    iAttachID = cl_duonet.netfunc.UnpackInt(4)
    cl_signal.net.C2GSAddObjSignal(who, iSignalSID, iAttachID)


def DN_C2GSAddNotifySignal(who):
    iNotifyID = cl_duonet.netfunc.UnpackInt(2)
    cl_signal.net.C2GSAddNotifySignal(who, iNotifyID)


def DN_C2GSDelSignal(who):
    iSignalID = cl_duonet.netfunc.UnpackInt(1)
    cl_signal.net.C2GSDelSignal(who, iSignalID)


def DN_C2GSTeamInfoSignal(who):
    iSignalSID = cl_duonet.netfunc.UnpackInt(2)
    iObjectSID = cl_duonet.netfunc.UnpackInt(4)
    sOwner = cl_duonet.netfunc.UnpackSL(1)
    iObjectType = cl_duonet.netfunc.UnpackInt(1)
    iOwnerID = cl_duonet.netfunc.UnpackInt(4)
    cl_signal.net.C2GSTeamInfoSignal(who, iSignalSID, iObjectSID, sOwner, iObjectType, iOwnerID)


def DN_C2GSAddPhotoSignal(who):
    iPhotoID = cl_duonet.netfunc.UnpackInt(2)
    tPos = cl_duonet.netfunc.UnpackPosFloat()
    tRotate = cl_duonet.netfunc.UnpackPosFloat()
    cl_signal.net.C2GSAddPhotoSignal(who, iPhotoID, tPos, tRotate)

