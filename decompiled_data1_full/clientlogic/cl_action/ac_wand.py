# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_wand.pyc
# RelativePath: clientlogic/cl_action/ac_wand.pyc
# Source Generated with Decompyle++
# File: ac_wand.pyc (Python 3.6)

from cl_only import Time2Frame, SendAlert
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, DISABLE_TYPE_STATE, WAND_COMP_TYPE_ACTION
from cl_wand import GetWandCompCls
import cl_state
import cl_formula
import cl_object.reason

def WandCompAddArgValue(oOwner, oLifeCycle, sArg, iVal):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oOwner, iVal, dData)
    oWandComp.AddArgValue(sArg, iVal)


def WandCompSetArgValue(oOwner, oLifeCycle, sArg, iVal):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oOwner, iVal, dData)
    oWandComp.SetArgValue(sArg, iVal)


def WandCompFinishCondition(oOwner, oLifeCycle):
    oWandComp = oLifeCycle.GetObject()
    oWandComp.FinishCondition()


def WandCompAddOwnerState(oOwner, oLifeCycle, iState, iTime, dRet, iCloseRemove):
    oWandComp = oLifeCycle.GetObject()
    if not oWandComp:
        return None
    iOwner = oOwner.m_ID
    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oOwner, dRet, dData)
    dRet['Wand'] = oWandComp.m_Item
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key(), dData = {
        'Item': oWandComp.m_ID })
    dArgs = {
        'AID': iOwner,
        'RS': oReason,
        'PFLV': oWandComp.m_Level,
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oOwner, iTime, dData)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oOwner, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oOwner)
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            iOwner: oState.m_ID })


def WandCompSetKeepValue(oOwner, oLifeCycle, sKey, iVal):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oOwner, iVal, dData)
    oWandComp.SetKeepValue(sKey, iVal)


def WandCompAddKeepValue(oOwner, oLifeCycle, sKey, iVal):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oOwner, iVal, dData)
    oWandComp.AddKeepValue(sKey, iVal)


def WandConditionCompSetFinishCount(oOwner, oLifeCycle, iCount):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iCount = cl_formula.GetResultByData(oOwner, iCount, dData)
    oWandComp.SetFinishConditionCount(iCount)


def WandConditionCompAddCount(oOwner, oLifeCycle, iCount):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    iCount = cl_formula.GetResultByData(oOwner, iCount, dData)
    oWandComp.AddConditionCount(iCount)


def WandCompSetWandBaseCount(oOwner, oLifeCycle, iWand, iCount):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWand.SetWandBaseCount(iCount, sKey, bClear = True)

    oWandComp = oLifeCycle.GetObject()
    oWand = oWandComp.GetMyItem()
    if not oWand or oWand.m_SID != iWand:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iCount = cl_formula.GetResultByData(oOwner, iCount, dData)
    oWand.SetWandBaseCount(iCount, sKey, bClear = False)
    oLifeCycle.AddDisableFunc(ClearFunc)


def WandActCompTrigger(oOwner, oLifeCycle, iNeedCount, iCount, iTime):
    oWandComp = oLifeCycle.GetObject()
    dData = {
        'LifeCycle': oLifeCycle }
    if iNeedCount:
        iCount = cl_formula.GetResultByData(oOwner, iCount, dData)
    else:
        iCount = 0
    iTime = cl_formula.GetResultByData(oOwner, iTime, dData)
    oWandComp.WandActCompTriggerInfo(iNeedCount, iCount, iTime)


def WandActCompSealRightSide(oOwner, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWandComp = oLifeCycle.GetObject()
        oWand = oWandComp.GetMyItem()
        if not oWand:
            return None
        oWand.m_ActionCompSealStatus = { }

    oWandComp = oLifeCycle.GetObject()
    oWand = oWandComp.GetMyItem()
    if not oWand:
        return None
    iCurPos = oWandComp.GetCurPos()
    (_, iActionGroveNum) = oWand.GetWandGroveNum()
    sKey = oLifeCycle.Key()
    oWand.m_ActionCompSealStatus = { }
    for iPos in range(iCurPos + 1, iActionGroveNum):
        oWand.RemoveComp(WAND_COMP_TYPE_ACTION, iPos, sKey)
    
    for iPos in range(iCurPos, iActionGroveNum):
        oWand.m_ActionCompSealStatus[iPos] = 1
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def WandActCompChangeWandAttr(oOwner, oLifeCycle, sAttr, iAdd, iMul):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oWandComp = oLifeCycle.GetObject()
        oWand = oWandComp.GetMyItem()
        if not oWand:
            return None
        oWand.AttrClear(sAttr, sKey)

    oWandComp = oLifeCycle.GetObject()
    oWand = oWandComp.GetMyItem()
    if not oWand:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oOwner, iMul, dData)
    iAdd = cl_formula.GetResultByData(oOwner, iAdd, dData)
    if iMul or iAdd:
        oWand.AttrChange(sAttr, iMul, iAdd, sKey)
    else:
        oWand.AttrClear(sAttr, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def WandActCompSetWandCustomLimit(oOwner, oLifeCycle, sAttr, iMin, iMax):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oWandComp = oLifeCycle.GetObject()
        oWand = oWandComp.GetMyItem()
        if not oWand:
            return None
        oAttr = oWand.GetAttr(sAttr)
        if not oAttr:
            return None
        oAttr.RemoveCustomLimit(oWand)

    oWandComp = oLifeCycle.GetObject()
    oWand = oWandComp.GetMyItem()
    if not oWand:
        return None
    oAttr = oWand.GetAttr(sAttr)
    if not oAttr:
        return None
    oAttr.SetCustomLimit(oWand, (iMin, iMax))
    oLifeCycle.AddDisableFunc(ClearFunc)


def SealRightSide(iPos, dComp, iMaxNum, lstNewComp):
    for iOtherPos in range(iPos + 1, iMaxNum):
        dComp[iOtherPos] = 0
    
    lstNewComp[:] = [ (iOtherPos, iSID) for iOtherPos, iSID in lstNewComp if iOtherPos < iPos ]

