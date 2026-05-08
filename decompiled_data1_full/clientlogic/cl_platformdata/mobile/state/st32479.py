# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32479.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32479.pyc
# Source Generated with Decompyle++
# File: st32479.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func311, Func312, Func313, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 9)


def CallBack0(oEventCB, oTarget):
    if not cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32481):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, None):
            cl_action.CommonSendStateCountChangeMessage(oTarget, oEventCB.GetCBLifeCycle())
            cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) + Func312(*a) + Func313(*a) - 100))
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32480, (lambda *a: 50 + Func429(*a, **{
'sArg': 'TalentLevel' }) * 50), { }, None)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32481, 12000, { }, None)


class CState(cl_state.CState):
    m_SID = 32479
    m_Name = '生命守护'
    m_DieRemove = 1
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

