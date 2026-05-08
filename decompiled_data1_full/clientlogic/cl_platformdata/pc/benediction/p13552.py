# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13552.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13552.pyc
# Source Generated with Decompyle++
# File: p13552.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckHitFlaw(oWarrior, oEventCB):
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1860, 0, 0, 0) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1864, 0, 0, 0):
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33042, 0, 1, 0):
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33042, 1, 1)
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33042, 0, { }, 1, 0, None)
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33042, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 13552
    m_Name = '#NT#时空坍缩'
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
    m_Career = 116

