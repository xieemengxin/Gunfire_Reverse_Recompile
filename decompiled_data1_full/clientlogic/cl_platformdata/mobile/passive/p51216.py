# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51216.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51216.pyc
# Source Generated with Decompyle++
# File: p51216.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func754

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonWandEnterCD(oWarrior, oLifeCycle, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonWandEnterCD(oWarrior, oLifeCycle, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonWandEnterCD(oWarrior, oLifeCycle, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', (lambda *a: Func754(*a) * 150), 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', (lambda *a: Func754(*a) * 100), 0, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', (lambda *a: Func754(*a) * 100), 0, 1)


class CPerform(CCustomPerform):
    m_SID = 51216
    m_Name = '#NT#节奏法杖被动'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

