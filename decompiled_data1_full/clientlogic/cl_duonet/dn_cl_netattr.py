# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_netattr.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_netattr.pyc
# Source Generated with Decompyle++
# File: dn_cl_netattr.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_netattr

def DN_MakeHeroAddPacket(iHero, iType, x, y, z, dx, dy, dz, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(33)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_ExtHeroProp(iHero, dPropInfo, pid):
    cl_duonet.netfunc.PacketPrepare(34)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.PacketSend(pid)


def DN_MakeDropAddPacket(iType, iTarget, x, y, z, dPropInfo, lstDesc, dPlayer):
    cl_duonet.netfunc.PacketPrepare(35)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.PacketAddI(len(lstDesc), 1)
    for desc in lstDesc:
        cl_duonet.netfunc.PacketAttr(desc)
    
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeSummonAddPacket(iType, iSummon, x, y, z, sx, sy, sz, anglex, angley, anglez, iClientOwner, dPropInfo, lstBodyPart, dPlayer):
    cl_duonet.netfunc.PacketPrepare(36)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iSummon, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(sx, 4)
    cl_duonet.netfunc.PacketAddI(sy, 4)
    cl_duonet.netfunc.PacketAddI(sz, 4)
    cl_duonet.netfunc.PacketAddI(anglex, 2)
    cl_duonet.netfunc.PacketAddI(angley, 2)
    cl_duonet.netfunc.PacketAddI(anglez, 2)
    cl_duonet.netfunc.PacketAddI(iClientOwner, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.PacketAddI(len(lstBodyPart), 1)
    for iBodyPart in lstBodyPart:
        cl_duonet.netfunc.PacketAddI(iBodyPart, 1)
    
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeMonsterAddPacket(iType, iMonster, x, y, z, dx, dy, dz, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(37)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iMonster, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeBuildAddPacket(iType, iObstacle, x, y, z, sx, sy, sz, anglex, angley, anglez, Prefab, Area, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(38)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iObstacle, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(sx, 4)
    cl_duonet.netfunc.PacketAddI(sy, 4)
    cl_duonet.netfunc.PacketAddI(sz, 4)
    cl_duonet.netfunc.PacketAddI(anglex, 4)
    cl_duonet.netfunc.PacketAddI(angley, 4)
    cl_duonet.netfunc.PacketAddI(anglez, 4)
    cl_duonet.netfunc.PacketAddI(Prefab, 4)
    cl_duonet.netfunc.PacketAddI(Area, 1)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeNpcAddPacket(iType, iNpc, x, y, z, dx, dy, dz, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(39)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iNpc, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CPropChange(iTarget, dPropInfo, oGame, iScene, pid):
    cl_duonet.netfunc.PacketPrepare(40)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.DGamePropChange(oGame, iScene, pid, dPropInfo)


def DN_GS2CItemPropChange(iTarget, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(41)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MapMonsterAndPart(iMonsterPart, iMonster, dPlayer):
    cl_duonet.netfunc.PacketPrepare(42)
    cl_duonet.netfunc.PacketAddI(iMonsterPart, 4)
    cl_duonet.netfunc.PacketAddI(iMonster, 4)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeServantAddPacket(iType, iServant, x, y, z, dx, dy, dz, iOwner, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(43)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iServant, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAddI(iOwner, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakeDeviceAddPacket(iType, iDevice, x, y, z, dx, dy, dz, sx, sy, sz, dPropInfo, dPlayer):
    cl_duonet.netfunc.PacketPrepare(44)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iDevice, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAddI(sx, 4)
    cl_duonet.netfunc.PacketAddI(sy, 4)
    cl_duonet.netfunc.PacketAddI(sz, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_MakePetAddPacket(iType, iPet, x, y, z, dx, dy, dz, iOwner, dPropInfo, dOffset, lstAbility, dPlayer):
    cl_duonet.netfunc.PacketPrepare(45)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketAddI(iPet, 4)
    cl_duonet.netfunc.PacketAddI(x, 4)
    cl_duonet.netfunc.PacketAddI(y, 4)
    cl_duonet.netfunc.PacketAddI(z, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAddI(iOwner, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.PacketAttrOffset(dOffset)
    cl_duonet.netfunc.PacketAddI(len(lstAbility), 1)
    for iAbility in lstAbility:
        cl_duonet.netfunc.PacketAddI(iAbility, 2)
    
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CPetPropChange(iTarget, dPropInfo, oGame, iScene, pid):
    cl_duonet.netfunc.PacketPrepare(46)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAttr(dPropInfo)
    cl_duonet.netfunc.DGamePropChange(oGame, iScene, pid, dPropInfo)

