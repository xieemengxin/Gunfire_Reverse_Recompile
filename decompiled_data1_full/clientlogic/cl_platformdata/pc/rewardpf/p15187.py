# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15187.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15187.pyc
# Source Generated with Decompyle++
# File: p15187.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM
from cl_newformula import Func450, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33484, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_ADDIMMOBILIZE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEED, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckInPointState(oWarrior, oEventCB, {
        1003: 1,
        1012: 1 }) and cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY) and cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count') > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', (lambda *a: -Func450(*a, **{
'sid': Func651(*a, **{
'sKey': 'StateSID' }),
'sAttr': 'MoveSpeedMul' }) * 15 / 10000))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount') >= cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'))
        cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'PF15187Count', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'))
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33484, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'), 0, 0, 300)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count') > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', 15)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount') >= cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'))
        cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'PF15187Count', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'))
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33484, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'), 0, 0, 300)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count') > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', (lambda *a: Func651(*a, **{
'sKey': 'ActionSpeed' }) * 15 / 100))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount') >= cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StateCount', cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'PF15187Count'))
        cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'PF15187Count', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'))
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33484, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount'), 0, 0, 300)


class CPerform(CCustomPerform):
    m_SID = 15187
    m_Name = '彼竭我盈'
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

