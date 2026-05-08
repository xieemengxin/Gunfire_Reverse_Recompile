# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/netdata.pyc
# RelativePath: clientlogic/cl_perform/cartoon/netdata.pyc
# Source Generated with Decompyle++
# File: netdata.pyc (Python 3.6)

from cl_duonet.netfunc import PacketFloat, UnpackFloat, UnpackPosFloat, UnpackInt, PacketPosFloat, PacketAddI
from cl_object.logging import SkillLog

def SendRay(lstRay):
    PacketAddI(len(lstRay), 1)
    for vHitPos, vNormal, iVictim, iHitPart in lstRay:
        PacketPosFloat(vHitPos)
        PacketPosFloat(vNormal)
        PacketAddI(iVictim, 4)
        PacketAddI(iHitPart, 1)
    


def RecvRay():
    iLen = UnpackInt(1)
    lstRay = []
    for _ in range(iLen):
        vHitPos = UnpackPosFloat()
        vNormal = UnpackPosFloat()
        iVictim = UnpackInt(4)
        iHitPart = UnpackInt(1)
        lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
    
    return lstRay


def PacketPosList(lstPos):
    PacketAddI(len(lstPos), 1)
    for vPos in lstPos:
        PacketPosFloat(vPos)
    


def UnpackPosList():
    iLen = UnpackInt(1)
    lstPos = []
    for _ in range(iLen):
        lstPos.append(UnpackPosFloat())
    
    return lstPos


def SkillPacketAddI(iLen):
    
    def Packet(args):
        PacketAddI(args, iLen)

    return Packet


def SkillUnpackInt(iLen):
    
    def Unpack():
        return UnpackInt(iLen)

    return Unpack


def SkillPacketPos(vPos):
    PacketPosFloat(vPos)


def SkillUnpacketPos():
    return UnpackPosFloat()


def SkillPacketListPos(lstArgs):
    PacketAddI(len(lstArgs), 1)
    for arg in lstArgs:
        PacketPosFloat(arg)
    


def SkillUnpacketListPos():
    lstArgs = []
    for _ in range(UnpackInt(1)):
        lstArgs.append(UnpackPosFloat())
    
    return lstArgs


def SkillPacketListInt(iLen):
    
    def Packet(lstArgs):
        PacketAddI(len(lstArgs), 1)
        for arg in lstArgs:
            PacketAddI(arg, iLen)
        

    return Packet


def SkillUnpackListInt(iLen):
    
    def Unpack():
        lstArgs = []
        for _ in range(UnpackInt(1)):
            lstArgs.append(UnpackInt(iLen))
        
        return lstArgs

    return Unpack


def SkillPacketFloat(iLen):
    
    def Packet(val):
        PacketFloat(val, iLen)

    return Packet


def SkillUnpackFloat(iLen):
    
    def Unpack():
        return UnpackFloat(iLen)

    return Unpack


def SendTouch(lstTouch):
    PacketAddI(len(lstTouch), 1)
    for vHitPos, vNormal, iVictim, iHitPart, iTouch in lstTouch:
        PacketPosFloat(vHitPos)
        PacketPosFloat(vNormal)
        PacketAddI(iVictim, 4)
        PacketAddI(iHitPart, 1)
        PacketAddI(iTouch, 1)
    


def RecvTouch():
    iLen = UnpackInt(1)
    lstTouch = []
    for _ in range(iLen):
        vHitPos = UnpackPosFloat()
        vNormal = UnpackPosFloat()
        iVictim = UnpackInt(4)
        iHitPart = UnpackInt(1)
        iTouch = UnpackInt(1)
        lstTouch.append((vHitPos, vNormal, iVictim, iHitPart, iTouch))
    
    return lstTouch


def SendFlaw(lstFlaw):
    PacketAddI(len(lstFlaw), 1)
    for iFlaw in lstFlaw:
        PacketAddI(iFlaw, 1)
    


def RecvFlaw():
    iLen = UnpackInt(1)
    lstFlaw = []
    for _ in range(iLen):
        iFlaw = UnpackInt(1)
        lstFlaw.append(iFlaw)
    
    return lstFlaw


def SendDict(dData):
    PacketAddI(len(dData), 1)
    for iKey, iValue in dData.items():
        PacketAddI(iKey, 4)
        PacketAddI(iValue, 4)
    


def RecvDict():
    iLen = UnpackInt(1)
    dData = { }
    for _ in range(iLen):
        iKey = UnpackInt(4)
        iValue = UnpackInt(4)
        dData[iKey] = iValue
    
    return dData

g_Proto = ([
    0,
    'Ray',
    SendRay,
    RecvRay], [
    1,
    'End',
    SkillPacketPos,
    SkillUnpacketPos], [
    2,
    'Start',
    SkillPacketPos,
    SkillUnpacketPos], [
    3,
    'LastVLST',
    SkillPacketListInt(4),
    SkillUnpackListInt(4)], [
    4,
    'Frame',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    5,
    'Over',
    None,
    None], [
    6,
    'WeaponChange',
    SkillPacketAddI(1),
    SkillUnpackInt(1)], [
    7,
    'Time',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    8,
    'SpeedVector',
    SkillPacketPos,
    SkillUnpacketPos], [
    9,
    'LockTarget',
    SkillPacketListInt(4),
    SkillUnpackListInt(4)], [
    10,
    'HitStatic',
    SkillPacketAddI(1),
    SkillUnpackInt(1)], [
    11,
    'Trigger',
    None,
    None], [
    12,
    'Direction',
    SkillPacketPos,
    SkillUnpacketPos], [
    13,
    'Distance',
    SkillPacketFloat(4),
    SkillUnpackFloat(4)], [
    14,
    'CheckStart',
    SkillPacketPos,
    SkillUnpacketPos], [
    15,
    'ClientSummonId',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    16,
    'FlyOverDis',
    None,
    None], [
    17,
    'Offset',
    SkillPacketPos,
    SkillUnpacketPos], [
    18,
    'Count',
    SkillPacketAddI(2),
    SkillUnpackInt(2)], [
    19,
    'IgnoreStatic',
    SkillPacketAddI(1),
    SkillUnpackInt(1)], [
    20,
    'EntityID',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    21,
    'Touch',
    SendTouch,
    RecvTouch], [
    22,
    'Flaw',
    SendFlaw,
    RecvFlaw], [
    23,
    'Dict',
    SendDict,
    RecvDict], [
    24,
    'Angle',
    SkillPacketFloat(4),
    SkillUnpackFloat(4)])
g_MaxProto = g_Proto[-1][0]

def InitProtoFunc():
    for iID, sKey, funcSend, funcRecv in g_Proto:
        g_ProtoKey[sKey] = (iID, funcSend, funcRecv)
    

g_ProtoKey = { }
InitProtoFunc()

def PacketSkill(dNet):
    PacketAddI(len(dNet), 1)
    for iNodeID, dNetData in dNet.items():
        PacketAddI(iNodeID, 2)
        PacketAddI(len(dNetData), 1)
        for sKey, value in dNetData.items():
            (iIndex, funcSend, _) = g_ProtoKey[sKey]
            PacketAddI(iIndex, 1)
            if funcSend:
                funcSend(value)
        
    


def UnpackSkill(oWarrior, skill = None):
    iLenData = UnpackInt(1)
    dData = { }
    for _ in range(iLenData):
        iNode = UnpackInt(2)
        iKeyCnt = UnpackInt(1)
        dNode = { }
        for _ in range(iKeyCnt):
            iIndex = UnpackInt(1)
            if iIndex > g_MaxProto:
                iPf = 0
                if skill:
                    iPf = skill if isinstance(skill, int) else skill.m_Base.get('pfid', 0)
                SkillLog.Alert('%d %d pf:%d unpack error dNode:%s dData:%s iNode:%d iKeyCnt:%d iIndex:%d' % (oWarrior.m_Game.m_ID, oWarrior.m_PlayerID, iPf, dNode, dData, iNode, iKeyCnt, iIndex))
            (_, sKey, _, funcRecv) = g_Proto[iIndex]
            if sKey in dNode:
                SkillLog.Error('repeat unpack %s' % sKey)
                continue
            if funcRecv:
                dNode[sKey] = funcRecv()
                continue
            dNode[sKey] = 1
        
        dData[iNode] = dNode
    
    return dData

g_BullectProto = ([
    0,
    'None',
    None,
    None], [
    1,
    'BulletVal',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    2,
    'ItemID',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    3,
    'FirstCostBulletFromContainer',
    None,
    None], [
    4,
    'Seed',
    SkillPacketAddI(4),
    SkillUnpackInt(4)], [
    5,
    'Result',
    SkillPacketAddI(1),
    SkillUnpackInt(1)], [
    6,
    'PerformSID',
    SkillPacketAddI(2),
    SkillUnpackInt(2)])

def UnpackBulletChange():
    iLenData = UnpackInt(1)
    dData = { }
    for _ in range(iLenData):
        iPerform = UnpackInt(4)
        iMethodLen = UnpackInt(1)
        dMethod = { }
        for _ in range(iMethodLen):
            iGroup = UnpackInt(1)
            iMethod = UnpackInt(1)
            dNode = UnpackBulletItem()
            dMethod[(iGroup, iMethod)] = dNode
        
        dData[iPerform] = dMethod
    
    return dData


def UnpackBulletItem():
    dNode = { }
    iKeyCnt = UnpackInt(1)
    for _ in range(iKeyCnt):
        iIndex = UnpackInt(1)
        (_, sKey, _, funcRecv) = g_BullectProto[iIndex]
        if sKey == 'None':
            SkillLog.Error('unexist bullet key')
            continue
        if sKey in dNode:
            SkillLog.Error('repeat unpack %s' % sKey)
        if funcRecv:
            dNode[sKey] = funcRecv()
            continue
        dNode[sKey] = 1
    
    return dNode

