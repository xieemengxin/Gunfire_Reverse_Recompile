# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3312.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3312.pyc
# Source Generated with Decompyle++
# File: p3312.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPAddDam', 10000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPSubDam', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPAddDam', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPSubDam', 2000)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPAddDam', 20000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPSubDam', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPAddDam', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPSubDam', 3000)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPAddDam', 30000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighHPSubDam', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPAddDam', 15000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowHPSubDam', 4000)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33943, 0, {
        'HighHPAddDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HighHPAddDam'),
        'HighHPSubDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HighHPSubDam'),
        'LowHPAddDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LowHPAddDam'),
        'LowHPSubDam': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LowHPSubDam') }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3312
    m_Name = '适应装甲'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 114

