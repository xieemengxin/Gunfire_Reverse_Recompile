# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4372.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4372.pyc
# Source Generated with Decompyle++
# File: p4372.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8112, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39030: 1 }, 0, 0):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 8112, 1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 8118, 0, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4372
    m_Name = '【诡谲雪山】罗睺-九九归一机制'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

