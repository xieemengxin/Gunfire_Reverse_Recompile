# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_item.pyc
# RelativePath: clientlogic/cl_action/ac_item.pyc
# Source Generated with Decompyle++
# File: ac_item.pyc (Python 3.6)

from cl_only import Functor, Time2Frame
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER
import cl_msgcenter
import cl_object.reason
import cl_formula
import cl_state

def EventCBFunc(oEventCB, iGroup, dEvent, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)


def HoldItemListenMsg(oOwner, oLifeCycle, iMsg, iSub, iGroup, iOnce, iPriority):
    
    def ClearEvent(oOwner, oLifeCycle):
        cl_msgcenter.DoneEvent(oOwner, iMsg, sKey, iSub)

    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(EventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddFunction(oOwner, iMsg, func, sKey, iSub, iOnce, iPriority)
    oLifeCycle.AddDisableFunc(ClearEvent)


def ItemAddState(oOwner, oLifeCycle, iState, iTime, dArgs, iRemove):
    
    def ClearState(oOwner, oLifeCycle):
        oOwner.m_State.RemoveItem(iStateID)

    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oOwner, dArgs, dData)
    oItem = oLifeCycle.GetObject()
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key(), dData = {
        'Item': oItem.m_ID if oItem else 0 })
    dArgs = {
        'AID': oOwner.m_ID,
        'RS': oReason,
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oOwner, iTime, dData)
    else:
        iTimeType = STATE_TIME_FOREVER
        iTime = 0
    oState = cl_state.AddState(oOwner, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oOwner)
    if iRemove:
        iStateID = oState.m_ID
        oLifeCycle.AddDisableFunc(ClearState)


def ItemSetSelfForceAttr(oOwner, oLifeCycle, sAttr, iValue):
    oItem = oLifeCycle.GetObject()
    sKey = oLifeCycle.Key()
    oItem.ItemAttrForceSet(sAttr, iValue, sKey)

