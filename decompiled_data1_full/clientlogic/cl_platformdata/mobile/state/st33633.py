# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33633.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33633.pyc
# Source Generated with Decompyle++
# File: st33633.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func311

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 13)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, 0):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) - 100))
        if not cl_evcon.CheckHasState(oTarget, oEventCB, 33711):
            if cl_evcon.CheckHasState(oTarget, oEventCB, 33766):
                cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 33766, 0)
            else:
                cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33605, 100, { }, 0)


class CState(cl_state.CState):
    m_SID = 33633
    m_Name = '#NT#苍玦变身随从状态'
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

