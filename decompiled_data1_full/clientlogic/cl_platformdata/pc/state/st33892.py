# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33892.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33892.pyc
# Source Generated with Decompyle++
# File: st33892.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, -1, {
        'SpecialItemSID': (lambda *a: Func429(*a, **{
'sArg': 'SpecialItemSID' })) })
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'DiceSpecial1019', 8)
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'DiceSpecial1019AddPer', 3)
    cl_action.CommonListenLevelCtrlMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_LEVEL_LAYERSTART, -1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Layer' }))) == 1:
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'DiceSpecial1019AddCost', 1)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Layer' }))) == 2:
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'DiceSpecial1019AddCost', 2)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Layer' }))) == 3:
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'DiceSpecial1019AddCost', 3)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Layer' }))) >= 4:
        cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'DiceSpecial1019AddCost', 3)


class CState(cl_state.CState):
    m_SID = 33892
    m_Name = '#NT#随机骰子'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

