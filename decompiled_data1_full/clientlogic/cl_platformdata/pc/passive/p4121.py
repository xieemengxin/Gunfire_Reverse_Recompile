# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4121.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4121.pyc
# Source Generated with Decompyle++
# File: p4121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, NWARRIOR_DROP_CASH, NWARRIOR_DROP_GSCASH, OBJ_SELF
from cl_newformula import Func324

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1200, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 6000, 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7945, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7946, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 200, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func324(*a) * 1 + 0)) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBTargetPosCreateDrop(oWarrior, oEventCB, NWARRIOR_DROP_CASH, (lambda *a: Func324(*a) * 1 + 0), None, None, None, None)
        cl_evact.EventCBTargetPosCreateDrop(oWarrior, oEventCB, NWARRIOR_DROP_GSCASH, (lambda *a: Func324(*a) * 1 + 0), None, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 7945, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, 999999999, DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, None, None, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4121
    m_Name = '宝箱怪初始被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

