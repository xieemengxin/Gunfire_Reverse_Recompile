# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33164.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33164.pyc
# Source Generated with Decompyle++
# File: st33164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func536

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: -1500 * Func536(*a)), 0, '')
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
        cl_evact.StateCBAddSelfState(oTarget, oEventCB, 33165, 200, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33164
    m_Name = '#NT#妖化增幅-变异体质'
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
        0: CallBack0 }

