# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33191.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33191.pyc
# Source Generated with Decompyle++
# File: st33191.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 16)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, None):
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
            cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 0, { })
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            cl_evact.EventSetLimitDamage(oTarget, oEventCB, 0)
            cl_evact.EventChangeHP(oTarget, oEventCB, -cl_evact.EventCBQueryTargetAttr(oTarget, oEventCB, 'HPMax'))
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func589(*a)), CURE_TYPE_PERFORM | DAM_USE_ALL, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33191
    m_Name = '#NT#词条50555'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

