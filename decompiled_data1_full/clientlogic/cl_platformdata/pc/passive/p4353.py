# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4353.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4353.pyc
# Source Generated with Decompyle++
# File: p4353.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func516
from cl_commondefines import OBJ_SELF, TYPE_RELIFE_RESCUE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32850, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32744, (lambda *a: 2500 - 500 * Func516(*a, **{
'sid': 3312 })), { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32744, (lambda *a: 2500 - 500 * Func516(*a, **{
'sid': 3312 })), { }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.EventCBCheckTargetRealDead(oWarrior, oEventCB):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32744, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4353
    m_Name = '御灵师仆从Q6'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

