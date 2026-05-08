# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4186.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4186.pyc
# Source Generated with Decompyle++
# File: p4186.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4186, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4186
    m_Name = '风神反向气旋死亡监听'
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

