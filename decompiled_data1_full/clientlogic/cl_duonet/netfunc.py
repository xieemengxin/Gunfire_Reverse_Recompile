# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/netfunc.pyc
# RelativePath: clientlogic/cl_duonet/netfunc.pyc
# Source Generated with Decompyle++
# File: netfunc.pyc (Python 3.6)

__version__ = '0.0.1'
__all__ = [
    'PacketPrepare',
    'PacketAddI',
    'PacketAddLong',
    'PacketSend',
    'PacketAddPS',
    'PacketAddPSL',
    'PacketAddS',
    'PacketAddSL',
    'PacketAddBinaryS',
    'UnpackInt',
    'UnpackLong',
    'UnpackBinaryString',
    'UnpackString',
    'UnpackSL',
    'WorldBroadcast',
    'SendToPlayers',
    'DGameAddPacket',
    'DGameBroadCast',
    'DGameSceneBroadCast',
    'DGameSceneBroadCastExclude',
    'DGamePropChange',
    'DGamePacketSend',
    'DGameSendToPlayers',
    'UnpackPS',
    'UnpackPSL',
    'PacketMarshal',
    'UnpackMarshal',
    'PacketAttr',
    'UnpacketAttr',
    'PacketVarInt',
    'UnpackVarInt',
    'PacketVarLong',
    'UnpackVarLong',
    'PacketPosInt',
    'UnpackPosInt',
    'CustomPacketAddI',
    'PacketPosFloat',
    'UnpackPosFloat',
    'PacketFloat',
    'UnpackFloat',
    'UnpackRadInt',
    'SetPacketData',
    'GetPacketData',
    'LocalSend',
    'PacketBinaryStringWithLen',
    'UnpackBinaryStringWithLen',
    'PacketAttrOffset',
    'UnpacketAttrOffset',
    'CustomPacketAddLong']
from cllib.lib_net import PacketAddBinaryS
from cllib.lib_net import PacketAddI
from cllib.lib_net import PacketAddLong
from cllib.lib_net import PacketAddS
from cllib.lib_net import PacketAddSL
from cllib.lib_net import PacketPrepare
from cllib.lib_net import PacketSend
from cllib.lib_net import UnpackBinaryString
from cllib.lib_net import UnpackInt
from cllib.lib_net import UnpackLong
from cllib.lib_net import UnpackString
from cllib.lib_net import SendToPlayers
from cllib.lib_net import WorldBroadcast
from cllib.lib_net import PacketVarInt
from cllib.lib_net import PacketVarLong
from cllib.lib_net import PacketPosInt
from cllib.lib_net import PacketPosFloat
from cllib.lib_net import PacketFloat
from cllib.lib_net import UnpackVarInt
from cllib.lib_net import UnpackVarLong
from cllib.lib_net import UnpackPosInt
from cllib.lib_net import UnpackPosFloat
from cllib.lib_net import UnpackFloat
from cllib.lib_net import SetPacketData
from cllib.lib_net import GetPacketData
from cllib.lib_net import LocalSend
from cllib.lib_net import ClearCmdFlag
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM
from cl_propdata import TYPE_LONG, TYPE_INTEGER, TYPE_VARCHAR, TYPE_VECTOR, TYPE_FLOAT, TYPE_INT100, TYPE_INTD100, TYPE_FORECASTATTR, TYPE_FORECASTVAR, TYPE_ENHANCE, TYPE_NEWVECTOR, PC_SEND_BC, PC_SEND_SBC, PC_SEND_SELF, TYPE_LONGD100
from cl_rplstr import CRplStr
from cli_player import GetPlayer
from cl_only import GetTraceText, Functor
from cl_timer import Logic_Call_Out
from cl_object.logging import ErrLog
import cllib.lib_json as json

def DGameBroadCast(oGame, iCmd = 0, iFlag = -1):
    dPlayer = oGame.GetRealPlayers()
    SendToPlayers(dPlayer, iFlag, iCmd)


def DGameSceneBroadCast(oGame, iScene):
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        ClearCmdFlag()
        return None
    dPlayer = oScene.GetPlayers()
    SendToPlayers(dPlayer)


def DGameSceneBroadCastExclude(oGame, iScene, pid):
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        ClearCmdFlag()
        return None
    dPlayer = oScene.GetPlayers()
    lstPlayer = [ x for x in dPlayer if x != pid ]
    if lstPlayer:
        SendToPlayers(lstPlayer)


def DGameAddPacket(oGame, objID, iPackIdx, iPosOffset, iFaceOffset):
    obj = oGame.GetObject(objID)
    if not obj:
        ClearCmdFlag()
        raise Exception('Errrr ObjectID')
    obj.AddPacket(iPackIdx, iPosOffset, iFaceOffset)


def DGamePropChange(oGame, iScene, pid, dPropInfo):
    if dPropInfo['Player']:
        SendToPlayers(dPropInfo['Player'])
        return None
    iSend = dPropInfo['Send']
    if iSend == PC_SEND_SBC:
        DGameSceneBroadCast(oGame, iScene)
    elif iSend == PC_SEND_SELF:
        PacketSend(pid)
    elif iSend == PC_SEND_BC:
        DGameBroadCast(oGame)


def DGamePacketSend(oGame, pid):
    if not oGame:
        ClearCmdFlag()
        return None
    obj = GetPlayer(pid)
    if not obj or obj.m_GameID != oGame.m_ID:
        ClearCmdFlag()
        return None
    PacketSend(pid)


def DGameSendToPlayers(oGame, dPlayers):
    if not oGame:
        ClearCmdFlag()
        return None
    dSend = { }
    for pid in dPlayers:
        obj = GetPlayer(pid)
        if obj and obj.m_GameID == oGame.m_ID:
            dSend[pid] = 1
    
    if not dSend:
        ClearCmdFlag()
        return None
    SendToPlayers(dSend)

SIZE_TO_MAX_VALUE = {
    1: 255,
    2: 65535,
    3: 16777215,
    4: 2147483647,
    8: 0x7FFFFFFFFFFFFFFF }
SIZE_TO_FIX_VALUE = {
    1: 200,
    2: 60000,
    3: 16000000,
    4: 2000000000,
    8: 0x7CE66C50E2840000 }

def GetValidValue(iVal, iSize):
    if iVal > SIZE_TO_MAX_VALUE[iSize]:
        lstTraceText = GetTraceText()
        Logic_Call_Out(Functor(DelaySendAlert, iVal, iSize, lstTraceText), 4, 'CustomPacket')
        iVal = SIZE_TO_FIX_VALUE[iSize]
    return iVal


def CustomPacketAddI(iVal, iSize):
    PacketAddI(GetValidValue(iVal, iSize), iSize)


def CustomPacketAddLong(iVal, iSize):
    PacketAddLong(GetValidValue(iVal, iSize), iSize)


def DelaySendAlert(iVal, iSize, lstTraceText):
    sMsg = f'''{iVal} too big,size:{iSize}\n''' + '\n'.join(lstTraceText[-5:])
    ErrLog.Alert(sMsg)
    for sText in lstTraceText:
        ErrLog.Debug(sText)
    


def PacketAddPS(txt, iLen = 0):
    raise NotImplementedError('PacketAddPS')


def UnpackPS(iLen):
    raise NotImplementedError('UnpackPS')


def PacketAddPSL(txt, iLen = 1):
    if isinstance(txt, CRplStr):
        (sText, dRpl) = txt.GetPacketInfo()
        PacketAddSL(sText, iLen)
        if dRpl:
            PacketAddI(len(dRpl), 1)
            for k, v in dRpl.items():
                PacketAddSL(k, 1)
                PacketAddSL(v, 1)
            
        else:
            PacketAddI(0, 1)
    else:
        PacketAddSL(txt, iLen)
        PacketAddI(0, 1)


def UnpackPSL(iLen = 1):
    sText = UnpackSL(iLen)
    iCnt = UnpackInt(1)
    if iCnt > 0:
        dRpl = { }
        for _ in range(iCnt):
            k = UnpackSL(1)
            v = UnpackSL(1)
            dRpl[k] = v
        
        return CRplStr(sText, dRpl)
    return CRplStr(sText)


def PacketMarshal(oValue, iSize = 1):
    sValue = json.dumps(oValue)
    iDataLen = len(sValue)
    PacketAddI(iDataLen, iSize)
    PacketAddBinaryS(sValue.encode('utf-8'), iDataLen)


def UnpackMarshal(iSize):
    iLen = UnpackInt(iSize)
    sValue = UnpackString(iLen)
    return json.loads(sValue)


def PacketAttr(dValue):
    lstAttr = dValue['Attr']
    PacketAddI(len(lstAttr), 1)
    for iIdx, iType, iLen, value in lstAttr:
        PacketAddI(iIdx, 1)
        if iType in (TYPE_INTEGER, TYPE_INT100):
            PacketAddI(value, iLen)
            continue
        if iType == TYPE_LONG:
            PacketAddLong(value, iLen)
            continue
        if iType == TYPE_LONGD100:
            PacketVarLong((value + 99) // 100)
            continue
        if iType == TYPE_INTD100:
            PacketAddI((value + 99) // 100, iLen)
            continue
        if iType == TYPE_VARCHAR:
            PacketAddS(value, iLen)
            continue
        if iType == TYPE_VECTOR:
            for val in value:
                PacketAddI(val, 4)
            
        if iType == TYPE_FLOAT:
            PacketFloat(value, iLen)
            continue
        if iType == TYPE_FORECASTATTR:
            (iBase, iAdd, iMulPos, iMulNeg) = value
            PacketAddI(iBase, 4)
            PacketAddI(iAdd, 4)
            PacketAddI(iMulPos, 4)
            PacketAddI(iMulNeg, 4)
            continue
        if iType == TYPE_FORECASTVAR:
            PacketAddI(value, 4)
            continue
        if iType == TYPE_ENHANCE:
            lstEnhance = value
            PacketAddI(len(lstEnhance), 1)
            for lstEnhanceAttr in lstEnhance:
                PacketAddI(len(lstEnhanceAttr), 1)
                for val in lstEnhanceAttr:
                    PacketAddI(val, 4)
                
            
        if iType == TYPE_NEWVECTOR:
            lstVector = value
            PacketAddI(len(lstVector), 1)
            for val in lstVector:
                PacketAddI(val, 4)
            
    


def PacketAttrOffset(dValue):
    PacketAddI(len(dValue), 1)
    for iIdx, value in dValue.items():
        PacketAddI(iIdx, 1)
        PacketAddI(value + 127, 1)
    


def PacketBinaryStringWithLen(s, size):
    PacketAddI(len(s), size)
    PacketAddBinaryS(s, len(s))


def UnpackBinaryStringWithLen(size):
    l = UnpackInt(size)
    return UnpackBinaryString(l)


def UnpacketAttr():
    pass


def UnpacketAttrOffset():
    pass


def UnpackSL(iSize):
    val = UnpackInt(iSize)
    if val == 0:
        return ''
    return UnpackString(val)


def UnpackRadInt(iSize, iRad = 100):
    val = UnpackInt(iSize)
    return val // iRad

