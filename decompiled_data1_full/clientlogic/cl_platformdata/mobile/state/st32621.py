# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32621.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32621.pyc
# Source Generated with Decompyle++
# File: st32621.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3015) >= 2:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8505, {
                'chopsTimes': 1,
                'Att': (lambda *a: 100 + Func331(*a, **{
'sid': 3015 }) * 25) }, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8505, {
                'chopsTimes': 1 }, None)


class CState(cl_state.CState):
    m_SID = 32621
    m_Name = '#NT#玉碎昆岗射击'
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

