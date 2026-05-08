# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16038.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16038.pyc
# Source Generated with Decompyle++
# File: p16038.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PLAY_TYPE_MULTI, RESCUE_SUBMSG_SUCCESS

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckWarPlayType(oWarrior, oLifeCycle, PLAY_TYPE_MULTI):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_SUCCESS, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), -2)


class CPerform(CCustomPerform):
    m_SID = 16038
    m_Name = '焕然新生'
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

