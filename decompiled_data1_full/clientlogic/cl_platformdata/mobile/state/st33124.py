# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33124.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33124.pyc
# Source Generated with Decompyle++
# File: st33124.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import NWARRIOR_DROP_INKBEAD, OBJ_SELF, PF_SUBMSG_CAREERPF, PICK_INKBEAD, PICK_SPECIALINKBEAD, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func428

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 33129, 0, { }, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 33129)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33124 }))):
        if cl_evcon.CheckPickType(oTarget, oEventCB, NWARRIOR_DROP_INKBEAD):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: 1 * max(Func361(*a, **{
'sid': 3611,
'sArgs': 'Times' }), 1)), None)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 24:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -24, None)
        cl_action.CommonModifyInkValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: max(15, Func361(*a, **{
'sid': 15099,
'sArgs': '33124Return' }))), '', { })
        cl_evact.EventCBStartClientSkill(oTarget, oEventCB, 12029, '', 0, None, { })


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33124, (lambda *a: max(24, Func361(*a, **{
'sid': 15099,
'sArgs': '33124MaxCount' }))), 1, None)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


class CState(cl_state.CState):
    m_SID = 33124
    m_Name = '染墨新生'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3 }

