# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8118.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8118.pyc
# Source Generated with Decompyle++
# File: st8118.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func411

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChageMulAttr(oTarget, oLifeCycle, 'ShieldMax', 800000)
    cl_action.StateCureStateAttacker(oTarget, oLifeCycle, (lambda *a: Func411(*a, **{
'sAttr': 'ShieldMax' }) * 100 / 100), 0, DAM_USE_SHIELD)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateCureStateAttacker(oTarget, oLifeCycle, (lambda *a: Func411(*a, **{
'sAttr': 'ShieldMax' }) * 0.25 / 100), 0, DAM_USE_SHIELD)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 8095, -1)
    cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: -Func411(*a, **{
'sAttr': 'Shield' })), DAM_TYPE_NORMAL, 0, 0, -1, 0, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        39030: 1 }, 0, 0):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 8118
    m_Name = '#NT#【诡谲雪山】罗睺九九归一临时护盾'
    m_DieRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10 }
    m_CBFuncAction = {
        0: CallBack0 }

