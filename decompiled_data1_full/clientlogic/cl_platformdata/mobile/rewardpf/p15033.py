# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15033.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15033.pyc
# Source Generated with Decompyle++
# File: p15033.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import MAIN_HOLD
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'AttSpeed', 0, (lambda *a: 500 * Func410(*a, **{
'sid': 32505 })), MAIN_HOLD)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', (lambda *a: 500 * Func410(*a, **{
'sid': 32505 })), 0, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32505):
        cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: 500 * Func410(*a, **{
'sid': 32505 })), MAIN_HOLD)
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: 500 * Func410(*a, **{
'sid': 32505 })), 0, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, (lambda *a: 500 * Func410(*a, **{
'sid': 32505 })), MAIN_HOLD, { })


class CPerform(CCustomPerform):
    m_SID = 15033
    m_Name = '剑气互御'
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
    m_DieDisable = 0

