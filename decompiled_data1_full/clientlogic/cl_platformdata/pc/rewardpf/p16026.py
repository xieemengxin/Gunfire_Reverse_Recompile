# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16026.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16026.pyc
# Source Generated with Decompyle++
# File: p16026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, OBJ_SELF, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1589, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1323: 1 }, 1, -1) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1589, 1, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1589, -1, -1) == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            1301: 1,
            1305: 1,
            1323: 1 }, 1, -1) == 0:
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1589, 1, -1, -1, None)
        elif cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1589, -1, -1) >= 2 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            1323: 1,
            1305: 1 }, 1, -1) == 0:
            cl_evact.EventCBSubPerformColdTimeByCover(oWarrior, oEventCB, 100)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1589, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1589, 1, -1)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1589, -1, -1) >= 2:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1629, 10, {
            'StateCount': 100 }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1589, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1589, -1, -1) < 2:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1589, 1, -1)
    else:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1305)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1589, 0)


class CPerform(CCustomPerform):
    m_SID = 16026
    m_Name = '再来一杯'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

