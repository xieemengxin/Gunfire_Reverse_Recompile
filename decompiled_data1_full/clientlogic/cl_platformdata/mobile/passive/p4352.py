# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4352.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4352.pyc
# Source Generated with Decompyle++
# File: p4352.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func237, Func595

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func595(*a))) == 3 or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func237(*a))) == 3 or cl_evcon.CheckHasState(oWarrior, oEventCB, 1763):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1763, 0, { }, 1, 1, None)
    elif cl_evcon.CheckHasState(oWarrior, oEventCB, 1763):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1763, 0)


class CPerform(CCustomPerform):
    m_SID = 4352
    m_Name = '八爪鱼水枪-三幕场景buff'
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

