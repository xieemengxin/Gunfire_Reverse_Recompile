# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51232.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51232.pyc
# Source Generated with Decompyle++
# File: p51232.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39710, 0, { }, 1, 1, 0)
        cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2029, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39710, 0, 0, 0):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 39710, 0, 0, 0)
    elif cl_evcon.EventCBCheckLevelGoal(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39710, 0, { }, 0, 0, 0)
    else:
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 39710, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51232
    m_Name = '关卡结束高移速'
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

