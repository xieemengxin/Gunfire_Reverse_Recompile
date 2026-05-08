# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_notify.pyc
# RelativePath: clientlogic/cl_notify.pyc
# Source Generated with Decompyle++
# File: cl_notify.pyc (Python 3.6)

from cl_only import SendAlert, CRplStr
from cl_object.logging import LogicwarningLog
import cllib.lib_flag
import cl_duonet.dn_cl_notify
import cl_platformdata
MSG_TYPE_DEFAULT = 0
MSG_TYPE_ITEMOP = 1
MSG_TYPE_KILLTIP = 2
MSG_TYPE_SAFEAREA = 3
MSG_TYPE_SYSTIPS = 4
MSG_TYPE_ANNOUNCE = 5
MSG_TYPE_COMMON = 6

def GS2CCenterTopFloatMsg(oGame, iType, sMsg, pid = 0):
    if pid:
        dPlayer = [
            pid]
    else:
        dPlayer = oGame.GetRealPlayers()
    dNetData = {
        'oGame': oGame,
        'iType': iType,
        'dPlayer': dPlayer,
        'sMsg': sMsg }
    cl_duonet.dn_cl_notify.DN_GS2CCenterTopFloatMsg(dNetData)


def GS2CLeftMidScrollMsg(oGame, iType, sMsg, pid = 0):
    GS2CCenterTopFloatMsg(oGame, iType, sMsg, pid)


def GS2CCenterBtmFloatMsg(oGame, iType, sMsg, pid = 0):
    GS2CCenterTopFloatMsg(oGame, iType, sMsg, pid)


def GS2CCenterMidScrollMsg(oGame, iType, sMsg, pid = 0):
    GS2CCenterTopFloatMsg(oGame, iType, sMsg, pid)


def GS2CMessage(oHero, sMsg):
    dNetData = {
        'oGame': oHero.m_Game,
        'sMsg': sMsg.encode('utf-8'),
        'pid': oHero.m_PlayerID,
        'iErr': 0 }
    cl_duonet.dn_cl_notify.DN_GS2CGMNotify(dNetData)


def InternalTips(oHero, sMsg, iErr = 0):
    if iErr and not (oHero.m_PlayerID):
        return None
    dNetData = {
        'oGame': oHero.m_Game,
        'sMsg': sMsg.encode('utf-8'),
        'pid': oHero.m_PlayerID,
        'iErr': iErr }
    cl_duonet.dn_cl_notify.DN_GS2CGMNotify(dNetData)
    if cllib.lib_flag.g_IsLogicLayer:
        LogicwarningLog.Info('%s %s' % (oHero.m_PlayerID, sMsg))


def GS2CDebugMsg(oGame, pid, sMsg):
    if not pid:
        return None
    if cllib.lib_flag.g_IsLogicLayer:
        LogicwarningLog.Info('%s %s' % (pid, sMsg))
    if not cllib.lib_flag.g_IsInternalRun:
        return None
    SendCommonNotify(oGame, [
        pid], 1001, {
        '$text': '[Debug]%s' % sMsg }, {
        'iTime': 500 })


def GS2CNotify(oGame, pid, sMsg):
    SendCommonNotify(oGame, [
        pid], 1001, {
        '$text': sMsg })


def GS2CDebugNotify(oGame, pid, sMsg):
    if not cllib.lib_flag.g_IsInternalRun:
        return None
    sMsg = '#R[Debug]#n' + sMsg
    SendCommonNotify(oGame, [
        pid], 1001, {
        '$text': sMsg })


def SendCommonNotify(oGame, lstPlayer, iChat, dReplaceInfo, dExtInfo = None, iTime = 0):
    dNetData = GetCommonNotifyInfo(iChat, dReplaceInfo)
    if not dNetData:
        return None
    if dExtInfo:
        dNetData.update(dExtInfo)
    dNetData['oGame'] = oGame
    dNetData['dPlayer'] = lstPlayer
    if iTime:
        dNetData['iTime'] = iTime
    cl_duonet.dn_cl_notify.DN_GS2CCommonNotify(dNetData)


def SendUnlockNotify(oGame, pid, iSID, iRewardSID, iType):
    dNetData = { }
    dNetData['oGame'] = oGame
    dNetData['pid'] = pid
    dNetData['iSID'] = iSID
    dNetData['iRewardSID'] = iRewardSID
    dNetData['iType'] = iType
    cl_duonet.dn_cl_notify.DN_GS2CUnLockItem(dNetData)


def SendWarConfirm(oGame, oHero, iConfirmID, iButtonCnt, sType, sUser, dFunc):
    iMenuIdx = oHero.NewUIMenuIdx()
    SetUICallBackFunction(oHero, iMenuIdx, dFunc)
    dNetData = {
        'oGame': oGame,
        'pid': oHero.m_PlayerID,
        'MenuIdx': iMenuIdx,
        'ConfirmID': iConfirmID,
        'ButtonCnt': iButtonCnt,
        'TypeStr': sType,
        'User': sUser }
    cl_duonet.dn_cl_notify.DN_GS2CWarConfirm(dNetData)


def ClearCommonNotify(oGame, lstPlayer, iChat):
    SendCommonNotify(oGame, lstPlayer, iChat, { }, {
        'iTime': 0 })


def SendCommonNotifyNoTransfer(oGame, lstPlayer, iTime, sRplMsg, dReplace):
    dNetData = { }
    if dReplace:
        dNetData['sMsg'] = CRplStr(sRplMsg, dReplace)
    else:
        dNetData['sMsg'] = CRplStr(sRplMsg)
    dNetData['iTime'] = iTime
    dNetData['oGame'] = oGame
    dNetData['dPlayer'] = lstPlayer
    cl_duonet.dn_cl_notify.DN_GS2CCommonNotify(dNetData)


def ClearCommonNotifyNoTransfer(oGame, lstPlayer, sRplMsg, dReplace):
    SendCommonNotifyNoTransfer(oGame, lstPlayer, 0, sRplMsg, dReplace)


def GetCommonNotifyInfo(iChat, dReplaceInfo):
    tResult = cl_platformdata.GetCommonNotify(iChat)
    if tResult is None:
        return None
    dInfo = { }
    (sMsg, iTime) = tResult
    rplMsg = CRplStr(sMsg, dReplaceInfo)
    dInfo['sMsg'] = rplMsg
    dInfo['iTime'] = iTime
    return dInfo


def GetCommonNotifyMsg(iChat, dReplaceInfo = None):
    tResult = cl_platformdata.GetCommonNotify(iChat)
    if tResult is None:
        return ''
    (sMsg, _) = tResult
    if dReplaceInfo:
        for sPara, sReplace in dReplaceInfo.items():
            sMsg = sMsg.replace(sPara, sReplace)
        
    return sMsg


def SendAdjustWeapon(oGame, pid, lstWeapon):
    dNetData = { }
    dNetData['oGame'] = oGame
    dNetData['pid'] = pid
    dNetData['lstWeapon'] = lstWeapon
    cl_duonet.dn_cl_notify.DN_GS2CAdjustWeapon(dNetData)


def GS2CChat(oGame, lstPlayer, sMsg, iSender):
    netData = {
        'sMsg': sMsg,
        'iSender': iSender,
        'dPlayer': lstPlayer,
        'oGame': oGame }
    cl_duonet.dn_cl_notify.DN_GS2CChat(netData)


def C2GSChat(oHero, sMsg):
    oGame = oHero.m_Game
    lstPlayer = oGame.GetRealPlayers()
    GS2CChat(oGame, lstPlayer, sMsg, oHero.m_ID)


def C2GSWarAnswerConfirm(oHero, iMenuIdx, iAnswer):
    if iMenuIdx not in oHero.m_UICallBack:
        return None
    dFunc = oHero.m_UICallBack[iMenuIdx]
    if iAnswer in dFunc:
        cbfunc = dFunc[iAnswer]
        cbfunc(oHero)


def SetUICallBackFunction(oHero, iMenuIdx, dFunc):
    if not dFunc:
        return None
    oHero.m_UICallBack[iMenuIdx] = dFunc

