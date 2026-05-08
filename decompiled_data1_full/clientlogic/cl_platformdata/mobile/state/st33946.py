# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33946.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33946.pyc
# Source Generated with Decompyle++
# File: st33946.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 1)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 6)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 9)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7175: 1,
        7153: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20000, DAM_MASK_ELEMENT, '')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0):
        cl_evact.EventCBAddSkillEndTriggerGroup(oTarget, oEventCB, 2)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7175, 1, 0):
        cl_evact.EventCBAddSkillEndTriggerGroup(oTarget, oEventCB, 5)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'HPMax' }) * 35 // 100))


def CallBack5(oEventCB, oTarget):
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32744, (lambda *a: max(10, Func404(*a))), { }, None)


def CallBack6(oEventCB, oTarget):
    cl_evact.DelayTriggerGroup(oTarget, oEventCB, 7, 1, 2200, 0, 0, { })


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if not cl_evcon.EventCBCheckTargetRealDead(oTarget, oEventCB):
        cl_action.CommonRelifeServant(oTarget, oEventCB.GetCBLifeCycle())


def CallBack9(oEventCB, oTarget):
    cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33946
    m_Name = '自爆装置'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        9: CallBack9 }

