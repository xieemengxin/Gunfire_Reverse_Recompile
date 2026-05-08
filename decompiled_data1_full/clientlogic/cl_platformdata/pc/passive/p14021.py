# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14021.pyc
# Source Generated with Decompyle++
# File: p14021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22031, 'LaunchInterval', 75, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22031, 'RotationInterval', 25, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22034, 'SpeedMul', 2, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22034, 'Acceleration', -48, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 22031, 1, 0):
        cl_evact.EventCbSetBallisticType(oWarrior, oEventCB, 5)


class CPerform(CCustomPerform):
    m_SID = 14021
    m_Name = '轮回9-敖龙增加炮弹'
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

