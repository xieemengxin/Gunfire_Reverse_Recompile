# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4204.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4204.pyc
# Source Generated with Decompyle++
# File: p4204.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB
from cl_newformula import Func218

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 20, HP_RADIO_SUB, 4)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Toughness', 0, 40, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 4003):
        cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, (lambda *a: Func218(*a) - 1), {
            39202: 150 })
    elif cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 4004):
        cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, (lambda *a: Func218(*a) - 1), {
            39202: 50 })
    elif cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 4005):
        cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, (lambda *a: Func218(*a) - 1), {
            39202: 100 })
    elif cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 4006):
        cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, (lambda *a: Func218(*a) - 1), {
            39202: 50 })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7976, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4204
    m_Name = '章鱼-阶段3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

