# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32935.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32935.pyc
# Source Generated with Decompyle++
# File: st32935.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_TYPE_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func530

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CareerColdTime', (lambda *a: Func530(*a)))
        if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 32935, 'CareerColdTime') > 0:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32939, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CareerColdTime'), {
                'MoveSpeedMul': -cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) * 100 }, 0)
        else:
            cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32939, 0)


class CState(cl_state.CState):
    m_SID = 32935
    m_Name = '#NT#劳逸结合特殊效果'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 40
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

