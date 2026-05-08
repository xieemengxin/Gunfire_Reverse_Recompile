# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_msgcenter/__init__.pyc
# RelativePath: clientlogic/cl_msgcenter/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_msgcenter.defines import *
from cl_msgcenter.mobject import CEventControl
from cl_object.logging import ErrLog
from cl_only import PythonError
if 'g_AllEventInfo' not in globals():
    g_AllEventInfo = { }

def SendMsg(iMsg, oOwner, dInfo, *args, iSub = None, oGame = -1):
    if iSub != -1:
        lstKey = g_Sub_Msg_Key[iMsg][iSub]
    else:
        lstKey = (iMsg,)
    if not oGame:
        oGame = oOwner.m_Game
    oCtrl = None
    if oOwner:
        oCtrl = oOwner.m_EvtCtrl
    for iKey in lstKey:
        if oCtrl and iKey in oCtrl.m_RegisterEvent and oCtrl.m_RegisterEvent[iKey].m_NotEmpty:
            oCtrl.m_RegisterEvent[iKey].DoEvent(oOwner, dInfo)
        if 'Halt' in dInfo:
            break
        if oGame and iKey in oGame.m_MsgCenter.m_ExtendFunc:
            lstExtend = oGame.m_MsgCenter.m_ExtendFunc[iKey]
            for func in lstExtend:
                func(oOwner, iKey, dInfo)
            
    


def SendCoreMsg(iMsg, oOwner, dInfo, *args, iSub = None, oGame = -1):
    if iSub != -1:
        lstKey = [
            g_Sub_Msg_Key[iMsg][iSub],
            iMsg]
    else:
        lstKey = [
            iMsg]
    if not oGame:
        oGame = oOwner.m_Game
    oCtrl = None
    if oOwner:
        oCtrl = oOwner.m_EvtCtrl
    for iKey in lstKey:
        if oCtrl and iKey in oCtrl.m_RegisterEvent and oCtrl.m_RegisterEvent[iKey].m_NotEmpty:
            oCtrl.m_RegisterEvent[iKey].DoCoreEvent(oOwner, dInfo)
        if 'Halt' in dInfo:
            break
        if oGame and iKey in oGame.m_MsgCenter.m_ExtendFunc:
            lstExtend = oGame.m_MsgCenter.m_ExtendFunc[iKey]
            for func in lstExtend:
                
                try:
                    func(oOwner, iKey, dInfo)
                except:
                    PythonError()

            
    


def AddFunction(obj, iMsg, func, sKey, iSub = -1, iOnce = 1, iPriority = 0):
    if not obj.m_EvtCtrl:
        ErrLog.Alert('warrior %s err,id %s,key %s' % (obj, obj.m_SID, sKey))
        return None
    obj.m_EvtCtrl.AddFunction(iMsg, func, sKey, iSub, iOnce, iPriority)


def DoneEvent(obj, iMsg, sKey, iSub = -1):
    if obj.m_EvtCtrl:
        obj.m_EvtCtrl.DoneEvent(iMsg, sKey, iSub)


def NewEventCtrl():
    return CEventControl()


def AddAttentionFunc(oListener, iTarget, iMsg, func, sKey, iSub = -1):
    oListener.m_Game.m_MsgCenter.AddAttentionFunc(oListener.m_ID, iTarget, iMsg, iSub, func, sKey)


def DoneAttention(oListener, iTarget, iMsg, sKey, iSub = -1):
    oListener.m_Game.m_MsgCenter.DoneAttention(oListener.m_ID, iTarget, iMsg, iSub, sKey)


def ClearAttention(oGame, iTarget, iKey):
    oGame.m_MsgCenter.ClearAttention(iTarget, iKey)

