# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51207.pyc
# Source Generated with Decompyle++
# File: p51207.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_SHOOT
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 8, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33554):
            cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33554, 500, -1)
        elif cl_evcon.CheckHasState(oWarrior, oEventCB, 33555):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 0, { }, 0, 0, 0)
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: Func410(*a, **{
'sid': 33555 })))
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33555, 1)
        elif cl_evcon.CheckHasState(oWarrior, oEventCB, 33554) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 33555) == 0:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 500, { }, 0, 0, 0)
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, 10000)
        elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33554):
            cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33554, 500, 0)
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: min(50000, Func410(*a, **{
'sid': 33554 }) + 10000)))
        elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33555):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 0, { }, 0, 0, 0)
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: min(50000, Func410(*a, **{
'sid': 33555 }) + 10000)))
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33555, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_SHOOT, 0) and cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 33554):
                cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33554, 500, -1)
            elif cl_evcon.CheckHasState(oWarrior, oEventCB, 33555):
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 0, { }, 0, 0, 0)
                cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: Func410(*a, **{
'sid': 33555 })))
                cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33555, 1)
            elif cl_evcon.CheckHasState(oWarrior, oEventCB, 33554) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 33555) == 0:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 500, { }, 0, 0, 0)
                cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, 10000)
            elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33554):
                cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33554, 500, 0)
                cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: min(50000, Func410(*a, **{
'sid': 33554 }) + 10000)))
            elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33555):
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33554, 0, { }, 0, 0, 0)
                cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33554, (lambda *a: min(50000, Func410(*a, **{
'sid': 33555 }) + 10000)))
                cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33555, 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, -3000)
    else:
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
            cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, -3000)
        else:
            cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51207
    m_Name = '机瞄手枪被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0

