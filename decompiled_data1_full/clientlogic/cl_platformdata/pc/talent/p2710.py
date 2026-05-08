# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2710.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2710.pyc
# Source Generated with Decompyle++
# File: p2710.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32527, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32500):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32528, 1000, { }, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 2710
    m_Name = '剑元朝华'
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
    m_Career = 109

