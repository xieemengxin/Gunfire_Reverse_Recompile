# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32717.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32717.pyc
# Source Generated with Decompyle++
# File: st32717.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func331, Func360

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3109) == 3:
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'ThrowMsg': 1 }, None)
        else:
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8007, {
                'Att': (lambda *a: Func331(*a, **{
'sid': 3109 }) * Func360(*a, **{
'sid': 8007,
'sAttr': 'Att' }) * 0.5),
                'ThrowMsg': 1 }, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32678, 100, { }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32717
    m_Name = '#NT#火焰呼唤'
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

