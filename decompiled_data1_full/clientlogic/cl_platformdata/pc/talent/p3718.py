# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3718.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3718.pyc
# Source Generated with Decompyle++
# File: p3718.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'EnergyMax', 0, 6000, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Energy() <= 6000:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33754, 1)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 600, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() <= 6000:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33754) or cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33754) == 0:
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 0)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33754, 1)
        else:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33754, 1)
    elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33754) and cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33754) == 1:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33754, 600, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33754, 0)


class CPerform(CCustomPerform):
    m_SID = 3718
    m_Name = '归元步影'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 118

