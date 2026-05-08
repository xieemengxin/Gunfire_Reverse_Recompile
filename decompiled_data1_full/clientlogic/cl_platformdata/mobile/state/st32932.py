# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32932.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32932.pyc
# Source Generated with Decompyle++
# File: st32932.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32932, 0, 0) > 0 and cl_evcon.EventCBCheckOrderTaskRunning(oTarget, oEventCB, {
        1016: 1,
        1116: 1,
        1216: 1 }) == 0:
        cl_evact.EventAddCBNumTalentGen(oTarget, oEventCB, -1)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TALENT_CHOOSE, -1, 2, 1, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32932, -1, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 32932
    m_Name = '毫发无损特殊效果'
    m_Type = STATE_CLS_SPECIAL
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
        0: CallBack0,
        2: CallBack2 }

