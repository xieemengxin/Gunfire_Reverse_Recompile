# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4239.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4239.pyc
# Source Generated with Decompyle++
# File: p4239.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, STATE_CLS_ABNORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7985, 1, None, None)
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 33812)
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 33814)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 100, { }, -1)
    cl_action.CommonRemoveAllStateByType(oWarrior, oLifeCycle, STATE_CLS_ABNORMAL)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 8003, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4239
    m_Name = '精英骑乘怪阶段二-切换为客体模型'
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

