# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33874.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33874.pyc
# Source Generated with Decompyle++
# File: st33874.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func410, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1333, 1, 0) and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33018 }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'UseThunderCount' }))):
        cl_action.CommonSendMessage(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_THUNDERPLUS, -1, { })
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33018, (lambda *a: -Func361(*a, **{
'sid': 50007,
'sArgs': 'UseThunderCount' })), 0)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'IsThunderPlus', 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1333, 1, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'IsThunderPlus', 0):
        cl_evact.EventCBGetTargetBySkillCustomData(oTarget, oEventCB, 'CreatePlant')
        cl_evact.EventSetTargetMark(oTarget, oEventCB, 'CanThunder', 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7168: 1,
        7169: 1,
        7170: 1,
        7171: 1,
        7172: 1,
        7174: 1 }, 1, 0):
        cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'OriginalAID' })))
        if cl_evcon.CheckTargetHasMark(oTarget, oEventCB, 'CanThunder', 0):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            if cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, 'BeThunder', 0) == 0:
                cl_evact.EventCBAddTargetCDByMark(oTarget, oEventCB, 'BeThunder', 600, 0)
                cl_evact.EventCBUsePerform(oTarget, oEventCB, 1911, 0, { })


class CState(cl_state.CState):
    m_SID = 33874
    m_Name = '#NT#步步惊雷基础效果-呦呦'
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
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

