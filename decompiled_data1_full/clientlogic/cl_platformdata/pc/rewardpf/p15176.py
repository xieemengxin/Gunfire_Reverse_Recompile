# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15176.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15176.pyc
# Source Generated with Decompyle++
# File: p15176.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELDFINSH, -1, 3, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33477, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HpChange', cl_evact.EventCBGetTotalHPChangeByCureRatio(oWarrior, oEventCB, 2))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpChange') >= 500:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cnt', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpChange') // 500)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HpChange', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt') * 500)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33477, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt'), 800)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HpChange', (lambda *a: Func304(*a, **{
'sAttr': 'RShield' }) * 100))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpChange') >= 500:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cnt', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpChange') // 500)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HpChange', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt') * 500)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33477, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt'), 800)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 15176
    m_Name = '循环往复'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

