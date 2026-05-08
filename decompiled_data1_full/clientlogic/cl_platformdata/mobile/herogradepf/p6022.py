# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6022.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6022.pyc
# Source Generated with Decompyle++
# File: p6022.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import only
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20026, 1, None, None)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20027, 1, None, None)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20028, 1, None, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32298, 200, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6022
    m_Name = '游侠【防御】2'
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

