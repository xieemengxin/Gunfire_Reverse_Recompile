# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33868.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33868.pyc
# Source Generated with Decompyle++
# File: st33868.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, SKILLCACHE_INT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 2500), 0, '')


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) < 6:
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'stage') != 0:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'stage', 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'DamInterval', 0, 0)
            cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'Pierce', 0, 0)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF)
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 33877, 0)
    elif cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'stage') != 1:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'stage', 1)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 75)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'DamInterval', 0, 100)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'Pierce', 0, 50)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 4, 0, 0)
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33877, 0, { }, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'Skill') and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1330, 1, 0) and cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT) == 3:
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'L4NotAddEnergy', 1, 0)


class CState(cl_state.CState):
    m_SID = 33868
    m_Name = '破空拳影'
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
    m_OnlyShowTarget = (0,)
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4 }

