# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4373.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4373.pyc
# Source Generated with Decompyle++
# File: p4373.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF
from cl_newformula import Func418

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 50, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 18 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, -1, 100)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 19 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, -1, 200)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 21 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, -1, 300)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 22 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, -1, 400)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1208, 0, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4373
    m_Name = '穷凶极恶（轮回九）'
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
    m_DieDisable = 1

