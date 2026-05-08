# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1771.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1771.pyc
# Source Generated with Decompyle++
# File: st1771.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func326, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func326(*a)), 'st1771damage')
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 25:
            cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1772, 0, { }, (lambda *a: Func437(*a, **{
'sKey': 'st1771damage' }) / 2000))
            cl_evact.EventClientBehavior(oTarget, oEventCB, 1771, 0)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1771
    m_Name = '铭刻13062计数'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 25
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

