# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_state_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_state_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_state_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_state.net

def DN_GS2CStateAdd(iWarrior, iStateID, iStateSID, iAttacker, iTime, iRemainTime, iMaxCount, iCount, dPlayer):
    cl_duonet.netfunc.PacketPrepare(104)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(iWarrior, 4)
    cl_duonet.netfunc.PacketAddI(iStateID, 4)
    cl_duonet.netfunc.PacketAddI(iStateSID, 2)
    cl_duonet.netfunc.PacketAddI(iAttacker, 4)
    cl_duonet.netfunc.PacketAddI(iTime, 4)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iMaxCount, 2)
    cl_duonet.netfunc.PacketAddI(iCount, 2)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CStateDel(iWarrior, iStateID, dPlayer):
    cl_duonet.netfunc.PacketPrepare(104)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(iWarrior, 4)
    cl_duonet.netfunc.PacketAddI(iStateID, 4)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CStateRefresh(iStateID, iTime, iRemainTime, iMaxCount, iCount, dPlayer):
    cl_duonet.netfunc.PacketPrepare(104)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(iStateID, 4)
    cl_duonet.netfunc.PacketAddI(iTime, 4)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iMaxCount, 2)
    cl_duonet.netfunc.PacketAddI(iCount, 2)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CStateRefreshCnt(iStateID, iCount, iPerCountTime, dPlayer):
    cl_duonet.netfunc.PacketPrepare(104)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(iStateID, 4)
    cl_duonet.netfunc.PacketAddI(iCount, 2)
    cl_duonet.netfunc.PacketAddI(iPerCountTime, 2)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CStateRefreshExtraInfo(iType, iWarrior, iStateID, iPerform, dExtInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(104)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(iWarrior, 4)
    cl_duonet.netfunc.PacketAddI(iStateID, 4)
    cl_duonet.netfunc.PacketAddI(iPerform, 4)
    cl_duonet.netfunc.PacketAddI(len(dExtInfo), 1)
    for sKey, iVal in dExtInfo.items():
        cl_duonet.netfunc.PacketAddSL(sKey, 1)
        cl_duonet.netfunc.PacketVarLong(iVal)
    
    cl_duonet.netfunc.SendToPlayers(dPlayer)

