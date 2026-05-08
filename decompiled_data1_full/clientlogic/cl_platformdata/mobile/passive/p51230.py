# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51230.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51230.pyc
# Source Generated with Decompyle++
# File: p51230.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJECT_SELFOWNER, OBJ_SELF, WARRIOR_MONSTER, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7153: 1 }, 1, 0):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_NORMAL, 1, 0, 0, 0, 0, 0, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20039, cl_condition.GetPerformAttrFromOwn(oWarrior, oEventCB.GetCBLifeCycle(), 1321, 'AddStateTime', OBJECT_SELFOWNER), { }, 1, 0, 0)
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33955, 0, { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, 0)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33955, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51230
    m_Name = '#NT#铁翼欲扬先抑嘲讽'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

