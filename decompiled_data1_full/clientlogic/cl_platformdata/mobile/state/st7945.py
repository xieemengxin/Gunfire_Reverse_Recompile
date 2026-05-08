# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7945.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7945.pyc
# Source Generated with Decompyle++
# File: st7945.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func307

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func307(*a) * 100 + 0)) >= 50:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7946, 0, None)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func307(*a) * 100 + 0)) >= 25:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7946, 1, None)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func307(*a) * 100 + 0)) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7946, 2, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7946, 3, None)


class CState(cl_state.CState):
    m_SID = 7945
    m_Name = '#NT#宝箱怪监听血量'
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

