# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2401.pyc
# Source Generated with Decompyle++
# File: p2401.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1306, 0, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32473):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32474):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32474, 1, 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32474, 0, { }, 0, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32474, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 2401
    m_Name = '渐入佳境'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 105

