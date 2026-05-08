# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13601.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13601.pyc
# Source Generated with Decompyle++
# File: p13601.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import PET_ENTER_BATTLE, PET_LEAVE_BATTLE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33229, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_ENTER_BATTLE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_LEAVE_BATTLE, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetCurPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33227, 0, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetEventPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33227, 0, { }, 1, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetEventPet(oWarrior, oEventCB)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33227, 1, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 13601
    m_Name = '妖力奔涌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

