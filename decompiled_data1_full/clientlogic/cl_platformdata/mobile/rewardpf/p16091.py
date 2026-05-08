# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16091.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16091.pyc
# Source Generated with Decompyle++
# File: p16091.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1838, 1000, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1838, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 16091
    m_Name = '横行霸道'
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

