# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_build_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_build_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_build_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_build.net

def DN_GS2CBuildGateStatus(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuildID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iStatus'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CBuildInteractState(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuild'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iState'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CPillarInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuild'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iStartFrame'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstLayer']), 1)
    for iLayer, fRotate, lstVent in netdata['lstLayer']:
        cl_duonet.netfunc.PacketAddI(iLayer, 1)
        cl_duonet.netfunc.PacketFloat(fRotate, 4)
        cl_duonet.netfunc.PacketAddI(len(lstVent), 1)
        for iVent, iVentID in lstVent:
            cl_duonet.netfunc.PacketAddI(iVent, 1)
            cl_duonet.netfunc.PacketAddI(iVentID, 4)
        
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPlankMove(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuild'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iStartFrame'], 4)
    cl_duonet.netfunc.PacketFloat(netdata['fSpeed'], 4)
    cl_duonet.netfunc.PacketFloat(netdata['fAcceSpeed'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['tStart'])
    cl_duonet.netfunc.PacketPosFloat(netdata['tEnd'])
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CGeyserInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuild'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['tCenter'])
    cl_duonet.netfunc.PacketPosFloat(netdata['tHalfExt'])
    cl_duonet.netfunc.PacketPosFloat(netdata['tDirection'])
    cl_duonet.netfunc.PacketAddI(netdata['iDistance'], 2)
    cl_duonet.netfunc.PacketFloat(netdata['fShowHight'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iEnableFrame'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iEnablePreTime'], 2)
    cl_duonet.netfunc.PacketFloat(netdata['fDropSpeedPercent'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CBuildMove(netdata):
    cl_duonet.netfunc.PacketPrepare(81)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iBuild'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['tStart'])
    cl_duonet.netfunc.PacketPosFloat(netdata['tEnd'])
    cl_duonet.netfunc.PacketAddI(netdata['iMoveTime'], 4)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_C2GSBuildInteract(who):
    iBuild = cl_duonet.netfunc.UnpackInt(4)
    cl_build.net.C2GSBuildInteract(who, iBuild)


def DN_C2GSBuildStopInteract(who):
    iBuild = cl_duonet.netfunc.UnpackInt(4)
    cl_build.net.C2GSBuildStopInteract(who, iBuild)

