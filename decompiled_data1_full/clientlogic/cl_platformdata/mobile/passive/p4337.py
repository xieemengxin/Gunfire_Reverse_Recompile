# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4337.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4337.pyc
# Source Generated with Decompyle++
# File: p4337.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 2500, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 5000, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 7500, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7153: 1,
        7154: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32825, 500, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7153: 1,
        7154: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32825, 650, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7153: 1,
        7154: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32825, 800, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4337
    m_Name = '御灵师仆从E5'
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

