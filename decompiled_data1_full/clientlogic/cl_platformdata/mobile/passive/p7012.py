# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p7012.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p7012.pyc
# Source Generated with Decompyle++
# File: p7012.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import COST_DEVICE_ENERGY, DEVICE_CONTROL_ACTIVE, DEVICE_CONTROL_RECYCLE, DEVICE_CONTROL_UNACTIVE, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func304, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, COST_DEVICE_ENERGY, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_ACTIVE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_UNACTIVE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_DEVICE, DEVICE_CONTROL_RECYCLE, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_COLLIDED, -1, 7, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) - Func361(*a, **{
'sid': 7012,
'sArgs': 'BEnergyCost' }))) < 0:
        if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33151, 250, { }, 0)
        elif cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1):
            cl_action.CommonSetDeciveAcitveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9482, { })
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33096, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33104, 0, { }, 1, 0, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33151, 0)
    if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33096, 0, { }, 1, 0, None)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) - Func361(*a, **{
'sid': 7012,
'sArgs': 'BEnergyCost' }))) < 0:
        if cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33151, 250, { }, 0)
        elif cl_condition.CheckDeciveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1):
            cl_action.CommonSetDeciveAcitveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9482, { })
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33096, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33104, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33096, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonSetDeciveAcitveStatus(oWarrior, oEventCB.GetCBLifeCycle(), 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8121, 200, {
            'MoveSpeedMul': -cl_action.CommonGetBarrierDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'SubSpeed') }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 7012
    m_Name = '致命装置-屏障被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        7: DoCallBackAction7 }
    m_BaseArgData = {
        'ReduceRatio': 100,
        'BEnergyCost': 200 }
    m_DieDisable = 0

