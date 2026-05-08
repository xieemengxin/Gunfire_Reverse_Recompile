# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_scene.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_scene.pyc
# Source Generated with Decompyle++
# File: dn_cl_scene.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_scene

def DN_GS2CMapDel(netdata):
    cl_duonet.netfunc.PacketPrepare(32)
    cl_duonet.netfunc.PacketAddI(netdata['iTarget'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CMapSceneEnter(netdata):
    cl_duonet.netfunc.PacketPrepare(64)
    cl_duonet.netfunc.PacketAddI(netdata['iScene'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMap'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iWarNo'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['pos'])
    cl_duonet.netfunc.PacketAddI(netdata['dx'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['dy'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['dz'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstArea']), 1)
    for iRoom in netdata['lstArea']:
        cl_duonet.netfunc.PacketAddI(iRoom, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstLine']), 1)
    for sLine in netdata['lstLine']:
        cl_duonet.netfunc.PacketAddSL(sLine, 1)
    
    cl_duonet.netfunc.PacketAddI(netdata['MaxLevel'], 1)
    cl_duonet.netfunc.CustomPacketAddI(netdata['CurLayer'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['CurLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['CurBaseLayer'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['MaxRoom'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['CurRoomPos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['LevelType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['GameType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['NewScene'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstWeaponPreLoad']), 1)
    for iWeaponSID in netdata['lstWeaponPreLoad']:
        cl_duonet.netfunc.PacketAddI(iWeaponSID, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstRelicPreLoad']), 1)
    for iRelicSID in netdata['lstRelicPreLoad']:
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstMonsterCategory']), 1)
    for iBaseMonsterSID in netdata['lstMonsterCategory']:
        cl_duonet.netfunc.PacketAddI(iBaseMonsterSID, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CMapGoto(netdata):
    cl_duonet.netfunc.PacketPrepare(65)
    cl_duonet.netfunc.PacketAddI(netdata['iTarget'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['pos'])
    cl_duonet.netfunc.DGameSceneBroadCast(netdata['oGame'], netdata['iScene'])


def DN_GS2CMapTriggerGate(netdata):
    cl_duonet.netfunc.PacketPrepare(74)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTarget'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iAction'], 2)
    cl_duonet.netfunc.DGameSceneBroadCast(netdata['oGame'], netdata['iScene'])


def DN_GS2CMapTriggerUpStone(netdata):
    cl_duonet.netfunc.PacketPrepare(74)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iTarget'], 4)
    cl_duonet.netfunc.PacketPosFloat(netdata['tPos'])
    cl_duonet.netfunc.PacketFloat(netdata['fSpeed'], 4)
    cl_duonet.netfunc.DGameSceneBroadCast(netdata['oGame'], netdata['iScene'])


def DN_C2GSLoadMapOK(who):
    iScene = cl_duonet.netfunc.UnpackInt(4)
    cl_scene.C2GSLoadMapOK(who, iScene)

