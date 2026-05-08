# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4283.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4283.pyc
# Source Generated with Decompyle++
# File: p4283.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1517):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1517, 50, { }, 1, 1, None)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1516):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1516, 1, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1518, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1516, 0, { }, 1, 1, None)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1516, 1, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1518, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1519):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1519, 50, { }, 1, 1, None)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1518):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1518, 1, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1516, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1518, 0, { }, 1, 1, None)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1518, 1, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1516, 0)


class CPerform(CCustomPerform):
    m_SID = 4283
    m_Name = '疲劳进攻'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

