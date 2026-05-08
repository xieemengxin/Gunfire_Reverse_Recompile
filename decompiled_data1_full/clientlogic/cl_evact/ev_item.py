# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_item.pyc
# RelativePath: clientlogic/cl_evact/ev_item.pyc
# Source Generated with Decompyle++
# File: ev_item.pyc (Python 3.6)

from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, DISABLE_TYPE_STATE
from cl_only import Time2Frame
import cl_formula
import cl_object
import cl_object.reason
import cl_drop
import cl_state

def ItemCBChangeEleStateTime(oOwner, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'Debuff' not in dMsgInfo:
        return None
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle.m_Enable:
        return None
    oItem = oLifeCycle.GetObject()
    dDebuffInfo = dMsgInfo['Debuff']
    dEventData = oItem.AttrCache()
    iAdd = cl_formula.GetResultByData(oOwner, iAdd, dEventData, dMsgInfo)
    iMul = cl_formula.GetResultByData(oOwner, iMul, dEventData, dMsgInfo)
    dDebuffInfo['DebuffTime'] = dDebuffInfo['DebuffTime'] * (10000 + iMul) // 10000 + iAdd


def ItemCBChangeAttr(oWarrior, oEventCB, sAttr, iMul, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle.m_Enable:
        return None
    oItem = oLifeCycle.GetObject()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventData = oItem.AttrCache()
    if iMul:
        iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventData, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventData, dMsgInfo)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    sKey = oItem.Key()
    oLifeCycle.m_Apply[sAttr] = 1
    oWarrior.AttrChange(sAttr, iMul, iAdd, sKey)


def EventChangeCurWeaponAttr(oListener, oEventCB, sAttr, iAdd, iMul, iFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle.m_Enable:
        return None
    oItem = oLifeCycle.GetObject()
    sKey = oItem.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstAdd = oListener.m_WieldCon.GetWeapons(iFlag)
    dEventData = oItem.AttrCache()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventData, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventData, dMsgInfo)
    for oWeapon in lstAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    


def EventChangeCurWeaponMagazine(oListener, oEventCB, sAttr, iAdd, iMul, iFlag, iWeaponType):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle.m_Enable:
        return None
    oItem = oLifeCycle.GetObject()
    sKey = oItem.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstAdd = oListener.m_WieldCon.GetWeapons(iFlag)
    dEventData = oItem.AttrCache()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventData, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventData, dMsgInfo)
    for oWeapon in lstAdd:
        if not oWeapon.m_Type == iWeaponType:
            break
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    


def ItemCBDropSelf(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle.m_Enable:
        return None
    oItem = oLifeCycle.GetObject()
    if not oItem.ValidDrop():
        return None
    oItem = oItem.m_Container.GetItemByID(oItem.m_ID)
    oItem.m_Container.RemoveItem(oItem, 'EventDropSelf')
    cl_drop.DropItem(oListener, oItem)


def ItemCBAddState(oWarrior, oEventCB, iState, iTime, dArgs, iCloseRemove):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dRet = cl_formula.CalArgsFormula(oWarrior, dArgs, dEventInfo, dMsgInfo)
    ItemID = dEventInfo['ItemID']
    dData = {
        'Item': ItemID } if ItemID else { }
    oReason = cl_object.reason.CStrReason(oEventCB.Key(), None, dData)
    dArgs = {
        'AID': oWarrior.m_ID,
        'RS': oReason,
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oWarrior, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oWarrior)
    if iCloseRemove:
        oLifeCycle = dEventInfo['LifeCycle']
        iStateID = oState.m_ID
        if oLifeCycle.m_Enable:
            oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
                oWarrior.m_ID: iStateID })
        else:
            oWarrior.m_State.RemoveItem(iStateID)


def ItemCBRemoveState(oWarrior, oEventCB, iState):
    lstState = oWarrior.m_State.GetItems(iState)
    for oTarState in lstState:
        oWarrior.m_State.RemoveItem(oTarState.m_ID)
    

