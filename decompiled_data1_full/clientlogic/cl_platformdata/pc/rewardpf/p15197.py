# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15197.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15197.pyc
# Source Generated with Decompyle++
# File: p15197.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33506, 300, { }, 1)
        cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, 300, 0, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33506, 300, { }, 1)
    cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, 300, 0, 0, { })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33507, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15197
    m_Name = '以逸待劳'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1

