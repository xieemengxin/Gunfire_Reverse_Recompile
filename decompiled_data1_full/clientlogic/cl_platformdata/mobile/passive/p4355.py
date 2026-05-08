# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4355.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4355.pyc
# Source Generated with Decompyle++
# File: p4355.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func341

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) == 2:
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32861, 500, { }, 1, -1, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32861, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 4355
    m_Name = '火力覆盖'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

