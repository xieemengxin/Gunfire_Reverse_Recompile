# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14417.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14417.pyc
# Source Generated with Decompyle++
# File: p14417.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32011, 'Radius', 12)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32011, 'Angle', 70)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 32011, 1, 0):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', -2000, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 32011, 1, 0):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 14417
    m_Name = '轮回10-精英流寇纵毒者'
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

