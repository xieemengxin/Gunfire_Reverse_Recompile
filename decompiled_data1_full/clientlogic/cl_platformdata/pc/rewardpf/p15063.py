# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15063.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15063.pyc
# Source Generated with Decompyle++
# File: p15063.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import STATE_COUNT_MAX

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 0, 0, 0)
    cl_action.CommonChangeStateAttr(oWarrior, oLifeCycle, 32954, 5, STATE_COUNT_MAX, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32954):
        cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32954, 5, STATE_COUNT_MAX, None)


class CPerform(CCustomPerform):
    m_SID = 15063
    m_Name = '火焰舞者'
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

