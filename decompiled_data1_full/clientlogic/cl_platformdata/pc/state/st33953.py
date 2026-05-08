# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33953.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33953.pyc
# Source Generated with Decompyle++
# File: st33953.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 10000, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSelfDie(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CBCheckCastingSkill(oTarget, oEventCB, 7142):
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, -1, 8, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 8, 0, 0)
    else:
        cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 50, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, 0, 0, 0, 1, None)
    if cl_evcon.GetTargetNum(oTarget, oEventCB) > 0:
        cl_evact.EventCBHateTarget(oTarget, oEventCB)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LockTarget', cl_evact.EventGetTargeID(oTarget, oEventCB))


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'LockTarget' })))
    if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB) or cl_evcon.CheckTargetDist(oTarget, oEventCB, 15, 1, OBJECT_OWNER):
        cl_evact.EventCBAddTargetStateTime(oTarget, oEventCB, 33953, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))
        cl_evact.EventCBSetUsePerformData(oTarget, oEventCB, 'vEnd', cl_evact.EventCBGetTargetPos(oTarget, oEventCB), 0, 0)
        cl_evact.EventCBCustomUsePerform(oTarget, oEventCB, 7142, {
            'VID': cl_evact.EventGetTargeID(oTarget, oEventCB) }, { }, 0)
        cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), 1800000, 1800000, 1)
    else:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 50, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, 0, 0, 0, 1, None)
        if cl_evcon.GetTargetNum(oTarget, oEventCB) > 0 and cl_evcon.CheckTargetDist(oTarget, oEventCB, 15, 1, OBJECT_OWNER):
            cl_evact.EventCBAddTargetStateTime(oTarget, oEventCB, 33953, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'))
            cl_evact.EventCBSetUsePerformData(oTarget, oEventCB, 'vEnd', cl_evact.EventCBGetTargetPos(oTarget, oEventCB), 0, 0)
            cl_evact.EventCBCustomUsePerform(oTarget, oEventCB, 7142, {
                'VID': cl_evact.EventGetTargeID(oTarget, oEventCB) }, { }, 0)
            cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), 1800000, 1800000, 1)


def CallBack7(oEventCB, oTarget):
    cl_evact.DelayTriggerGroup(oTarget, oEventCB, 0, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DelayTime'), 0, 0, { })


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7142, 1, 0):
        cl_evact.EventCBAddSkillEndTriggerGroup(oTarget, oEventCB, 9)


def CallBack9(oEventCB, oTarget):
    cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33953
    m_Name = '#NT#铁翼延迟死亡'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20,
        'firsttime': 20 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9 }

