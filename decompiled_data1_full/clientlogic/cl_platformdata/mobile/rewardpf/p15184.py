# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15184.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15184.pyc
# Source Generated with Decompyle++
# File: p15184.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func387

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15184)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33490) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33490, 0, { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveSubSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 200)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSubSelfColdTime(oWarrior, oEventCB, (lambda *a: (Func387(*a) // 25) * 200))


class CPerform(CCustomPerform):
    m_SID = 15184
    m_Name = '#NT#后备能源套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

