# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33142.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33142.pyc
# Source Generated with Decompyle++
# File: st33142.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func604

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1310, 'MaxCover', 0, (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, 0) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': '1310_TempMaxCover' }))) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, '1310_TempMaxCover', 1)


class CState(cl_state.CState):
    m_SID = 33142
    m_Name = '#NT#组件50165临时冲刺次数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

