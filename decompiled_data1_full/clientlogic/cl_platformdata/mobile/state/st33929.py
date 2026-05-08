# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33929.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33929.pyc
# Source Generated with Decompyle++
# File: st33929.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_SRC, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func402, Func404, Func516

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func516(*a, **{
'sid': 3309 }))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, None)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, 'st33929', 0)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st33929', (lambda *a: Func404(*a)))
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 36000 * Func336(*a, **{
'sKey': 'st33929' })), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33929, 5, 0, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33929', None):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: 12000 * Func402(*a) * Func336(*a, **{
'sKey': 'st33929' })), 0, DAM_MASK_SRC, 1, 1)


class CState(cl_state.CState):
    m_SID = 33929
    m_Name = '#NT#御灵师仆从Q3增伤'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        4: CallBack4 }

