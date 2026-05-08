# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_container_talentcon.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_container_talentcon.pyc
# Source Generated with Decompyle++
# File: dn_cl_container_talentcon.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_container.talentcon

def DN_GS2CAddTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTalentSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iBasicLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxLevel'], 1)
    cl_duonet.netfunc.PacketAddPSL(netdata['sSubDesc'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRemoveTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTalentSID'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CSendRewardSID(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iRewardSID'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CAddBenediction(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iBenedictionSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iBasicLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.CustomPacketAddI(netdata['iLayer'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iReplaceSID'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CRemoveBenediction(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iBenedictionSID'], 2)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CChooseChangeTalentLevel(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CBanTalentResult(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for iTalentSID in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(iTalentSID, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDisableTalentResult(netdata):
    cl_duonet.netfunc.PacketPrepare(105)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for iTalentSID in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(iTalentSID, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSDisableTalent(who):
    lstTalent = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iTalentSID = cl_duonet.netfunc.UnpackInt(2)
        lstTalent.append(iTalentSID)
    
    cl_container.talentcon.C2GSDisableTalent(who, lstTalent)

