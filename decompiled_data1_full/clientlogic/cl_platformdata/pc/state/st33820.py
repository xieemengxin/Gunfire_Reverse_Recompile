# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33820.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33820.pyc
# Source Generated with Decompyle++
# File: st33820.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func429, Func437, Func619, Func620

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 21, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 11, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -1, None)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'P15366', 0):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TargetID', (lambda *a: Func620(*a)))


def CallBack1(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetID'):
        cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'TargetID' })))
        if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
            cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
            if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
                cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })
            else:
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
                if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
                    cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })


def CallBack4(oEventCB, oTarget):
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 5, 1, 0)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TargetID'):
        cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'TargetID' })))
        if cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
            cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
            if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
                cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })
            else:
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
                if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
                    cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, { })


def CallBack5(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: -Func429(*a, **{
'sArg': 'Damage' })), 0, 1, 0)
    if not cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack11(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func619(*a, **{
'sAttr': 'Count' })))


def CallBack21(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33820
    m_Name = '#NT#连续Q骰子-雷落/行者/苍决'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        'firsttime': 40 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4,
        5: CallBack5,
        11: CallBack11,
        21: CallBack21 }

