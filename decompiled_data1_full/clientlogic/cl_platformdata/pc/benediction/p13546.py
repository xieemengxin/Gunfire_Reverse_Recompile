# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13546.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13546.pyc
# Source Generated with Decompyle++
# File: p13546.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33946, 0, {
        'AddDam': 2000,
        'LoseHPThreshold': 300000,
        'LoseHPRatio': 20,
        'UseShenBingLoseHPRatio': 250,
        'UseJuNengLoseHPRatio': 150,
        'AttackLoseHPRatio': 50 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    if cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33944, 0, {
            'LoseHPRatio': 10 }, 1, 1, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32758, 1, 0, 0)
    else:
        cl_action.CommonListenServantMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RELIFE, -1, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33944, 0, {
        'LoseHPRatio': 10 }, 1, 1, 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32758, 1, 0, 0)
    cl_action.CommonDoneServantAttention(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RELIFE, -1)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32758, 0, { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13546
    m_Name = '自爆装置'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 114

