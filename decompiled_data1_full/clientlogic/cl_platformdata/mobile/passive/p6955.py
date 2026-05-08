# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p6955.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p6955.pyc
# Source Generated with Decompyle++
# File: p6955.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 5500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 4500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'RShield', 15)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1412, 'ColdTime', 1000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1412, 'DebuffProb', 6000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1670, 'DebuffProb', 10000)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32249, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 6955
    m_Name = '雷落队友AI属性强制值'
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

