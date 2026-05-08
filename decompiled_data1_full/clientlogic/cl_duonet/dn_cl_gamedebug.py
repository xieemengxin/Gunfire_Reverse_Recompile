# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_gamedebug.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_gamedebug.pyc
# Source Generated with Decompyle++
# File: dn_cl_gamedebug.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_gamedebug

def DN_GS2CDebugLine(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['ox'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['oy'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['oz'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['x'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['y'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['z'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['rgb'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTypeNum'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CClearDebugLine(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTypeNum'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CMonsterConfig(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketFloat(netdata['fViewR'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iViewAngle'], 2)
    cl_duonet.netfunc.PacketFloat(netdata['fGuardDis'], 4)
    cl_duonet.netfunc.PacketFloat(netdata['fSearchDis'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CMonsterDebug(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iShow'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iNo'], 2)
    cl_duonet.netfunc.PacketAddSL(netdata['sInfo'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CBuildDebug(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iShow'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iNo'], 2)
    cl_duonet.netfunc.PacketAddSL(netdata['sInfo'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CFlowDebug(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['pid'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMsg'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTotalNumber'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCurNumber'], 4)
    cl_duonet.netfunc.PacketAddSL(netdata['sMsg'], 2)
    cl_duonet.netfunc.PacketAddSL(netdata['sFunction'], 2)
    cl_duonet.netfunc.DGameBroadCast(netdata['oGame'])


def DN_GS2CServantDebug(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iShow'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iID'], 4)
    cl_duonet.netfunc.PacketAddSL(netdata['sInfo'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CSendSeed(netdata):
    cl_duonet.netfunc.PacketPrepare(83)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddBinaryS(netdata['sSeed'], 0)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSFlowDebug(who):
    pid = cl_duonet.netfunc.UnpackInt(4)
    iMsg = cl_duonet.netfunc.UnpackInt(4)
    cl_gamedebug.C2GSFlowDebug(who, pid, iMsg)


def DN_C2GSSkillDebugStart(who):
    cl_gamedebug.C2GSSkillDebugStart(who)


def DN_C2GSSkillDebug(who):
    iSkill = cl_duonet.netfunc.UnpackInt(4)
    cl_gamedebug.C2GSSkillDebug(who, iSkill)


def DN_C2GSReceiveSeed(who):
    sSeed = cl_duonet.netfunc.UnpackBinaryString(0)
    cl_gamedebug.C2GSReceiveSeed(who, sSeed)

