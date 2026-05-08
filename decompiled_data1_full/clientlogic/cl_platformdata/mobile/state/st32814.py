# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32814.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32814.pyc
# Source Generated with Decompyle++
# File: st32814.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func407

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 32774) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32774, (lambda *a: 50 * Func331(*a, **{
'sid': 2901 })), (lambda *a: Func407(*a, **{
'sid': 32774 })), 0)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)


class CState(cl_state.CState):
    m_SID = 32814
    m_Name = '#NT#江河之力回复次数检测'
    m_DieRemove = 1
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

