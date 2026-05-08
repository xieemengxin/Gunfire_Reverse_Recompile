# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2506.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2506.pyc
# Source Generated with Decompyle++
# File: p2506.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1677, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32401, 0, 0, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32401, 1, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32401, 0, { }, 0, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32401, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 2506
    m_Name = '反射光墙'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 106

