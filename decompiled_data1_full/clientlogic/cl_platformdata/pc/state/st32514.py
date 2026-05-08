# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32514.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32514.pyc
# Source Generated with Decompyle++
# File: st32514.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func354

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1414, 0, None):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func354(*a)), None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32515, 0, { }, None)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2411) == 3:
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32515, 20, 0, None, None)
            else:
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32515, 15, 0, None, None)


class CState(cl_state.CState):
    m_SID = 32514
    m_Name = '#NT#荡气回肠'
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

