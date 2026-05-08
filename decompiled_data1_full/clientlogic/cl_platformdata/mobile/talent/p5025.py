# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5025.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5025.pyc
# Source Generated with Decompyle++
# File: p5025.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, -1, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32880, 0, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32880, (lambda *a: Func410(*a, **{
'sid': 32881 })), None)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32881, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32879, 0, { }, 1, 1, None)
    cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 32879, (lambda *a: Func410(*a, **{
'sid': 32881 })), 0)


class CPerform(CCustomPerform):
    m_SID = 5025
    m_Name = '自我进化'
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
    m_IsRareTalent = 1
    m_Career = 114

