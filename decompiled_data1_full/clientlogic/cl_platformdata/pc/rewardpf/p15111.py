# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15111.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15111.pyc
# Source Generated with Decompyle++
# File: p15111.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, RESCUE_SUBMSG_SUCCESS
from cl_newformula import Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 15111, 'AddCD', 12000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 15111, 'AddAttTime', 200, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 1, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15111)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SaveTime', -3000, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SaveTime', 0, 0, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33391, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33391, 0)
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCD'))
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SaveTime', -3000, 0, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a)), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, None)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33390, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAttTime'), { }, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33390, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAttTime'), { }, 0, 0, 0)
        cl_evact.EventCBCloseRelifeNotify(oWarrior, oEventCB)
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 0, 9687, {
            '$$playername1': cl_evact.EventCBGetTargetName(oWarrior, oEventCB, OBJ_SELF),
            '$$playername2': cl_evact.EventCBGetTargetName(oWarrior, oEventCB, OBJ_VICTIM) })


class CPerform(CCustomPerform):
    m_SID = 15111
    m_Name = '#NT#救人套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

