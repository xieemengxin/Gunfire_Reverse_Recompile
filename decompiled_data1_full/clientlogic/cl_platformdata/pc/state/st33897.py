# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33897.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33897.pyc
# Source Generated with Decompyle++
# File: st33897.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func341, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7154: 1,
        7153: 1 }, 0, 0):
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a))) == 2:
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'MaxCover', 0, 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'MaxCover', 0, 1)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'NewPhase' }))) == 2:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'MaxCover', 0, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'MaxCover', 0, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, 0)


class CState(cl_state.CState):
    m_SID = 33897
    m_Name = '#NT#小玖存储肩炮次数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
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
        0: CallBack0,
        1: CallBack1 }

