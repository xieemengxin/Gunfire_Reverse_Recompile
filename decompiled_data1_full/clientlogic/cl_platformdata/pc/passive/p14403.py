# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14403.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14403.pyc
# Source Generated with Decompyle++
# File: p14403.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39091, 'TrajectoryMul', 2, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39093, 'ChargeTime', 75, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39096, 'TrajectoryMul', 2, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByMsgInfoSummon(oWarrior, oEventCB)
    if cl_evcon.CheckTargetPointBaseSummons(oWarrior, oEventCB, {
        1033: 1 }):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7146, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 14403
    m_Name = '轮回9-连城'
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

