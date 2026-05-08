# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2307.pyc
# Source Generated with Decompyle++
# File: p2307.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32273):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32275, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32273, 0, { }, 1)
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32275, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32273):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32275, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32273, 0, { }, 1)
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32275, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32273):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32276, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 2, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32273, 0, { }, 1)
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32276, 0, { }, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 2, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 32275):
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 32275)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32274) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32274, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32273, 0, 0, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32273, (lambda *a: -Func410(*a, **{
'sid': 32273 })), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32273, 0, 0, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32273, (lambda *a: -max(int(Func410(*a, **{
'sid': 32273 }) // 2), 1)), 0)


class CPerform(CCustomPerform):
    m_SID = 2307
    m_Name = '雷耀法纹'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 104

