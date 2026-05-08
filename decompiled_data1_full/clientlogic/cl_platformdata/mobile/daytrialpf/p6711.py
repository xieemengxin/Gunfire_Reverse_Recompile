# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6711.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6711.pyc
# Source Generated with Decompyle++
# File: p6711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, TYPE_RELIFE_PASSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_PASSIVE, 300, 2, 1, { }, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1245, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1261, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeTimesKey(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1245, -1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1261, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 6711
    m_Name = '玩家复活'
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

