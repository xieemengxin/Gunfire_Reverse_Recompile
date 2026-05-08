# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4145.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4145.pyc
# Source Generated with Decompyle++
# File: p4145.pyc (Python 3.6)

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
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 13 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, 100)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 14 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, 200)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 16 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, 300)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func418(*a) * 17 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 1, None, 400)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1208, 0, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4145
    m_Name = '穷凶极恶'
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

