# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_perform_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_perform_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_perform_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_perform.net

def DN_GS2CSkillHalt(netdata):
    cl_duonet.netfunc.PacketPrepare(51)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['AID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['ActNum'], 2)
    cl_duonet.netfunc.SendToPlayers(netdata['dPlayer'])


def DN_GS2CSkillFail(netdata):
    cl_duonet.netfunc.PacketPrepare(51)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['AID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['ActNum'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CAddBulletChangeRule(netdata):
    cl_duonet.netfunc.PacketPrepare(101)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRuleSID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CDelBulletChangeRule(netdata):
    cl_duonet.netfunc.PacketPrepare(101)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRuleSID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPerformColdTimeAdd(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRemainTime'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCacheRemainTime'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCacheSumTime'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['ActNum'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPerformColdTimeDel(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPerformAdd(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerformID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iOwnerID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItemID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPerformType'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iAttIdx'], 1)
    cl_duonet.netfunc.PacketAttr(netdata['dInfo'])
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPerformAddUseInterval(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRemainTime'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPerformColdTimeNoAdd(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPerform'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['ActNum'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPerformRemove(netdata):
    cl_duonet.netfunc.PacketPrepare(103)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iOwnerID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPerformID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPerformType'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_C2GSBulletRuleEnable(who):
    iPerform = cl_duonet.netfunc.UnpackInt(4)
    cl_perform.net.C2GSBulletRuleEnable(who, iPerform)


def DN_C2GSBulletRuleDisable(who):
    iPerform = cl_duonet.netfunc.UnpackInt(4)
    cl_perform.net.C2GSBulletRuleDisable(who, iPerform)

