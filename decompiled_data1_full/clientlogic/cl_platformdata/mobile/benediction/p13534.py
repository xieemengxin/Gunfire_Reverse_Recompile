# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13534.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13534.pyc
# Source Generated with Decompyle++
# File: p13534.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32955):
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32955, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1316: 1 }, 0, 0):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32955):
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32955, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32955, 0, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 13534
    m_Name = '内力燃烧'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 112

