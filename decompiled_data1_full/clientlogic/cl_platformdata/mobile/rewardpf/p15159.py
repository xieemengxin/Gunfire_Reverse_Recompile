# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15159.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15159.pyc
# Source Generated with Decompyle++
# File: p15159.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, -1, -1):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33495, 0, { }, 1, 0, 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33495, 5)


class CPerform(CCustomPerform):
    m_SID = 15159
    m_Name = '#NT#爆能强化套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

