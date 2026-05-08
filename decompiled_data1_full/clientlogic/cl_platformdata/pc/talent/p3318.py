# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3318.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3318.pyc
# Source Generated with Decompyle++
# File: p3318.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DAM_USE_SHIELD, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0, 15)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, 1000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ShieldCD', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 300)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0, 15)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, 2000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ShieldCD', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 500)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 15)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, 3000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ShieldCD', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 500)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32877) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32877, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ShieldCD'), { }, 1, 0, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SaveTime'), { }, 1, -1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32877) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' })), DAM_USE_SHIELD, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32877, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ShieldCD'), { }, 1, 0, 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SaveTime'), { }, 1, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 3318
    m_Name = '特制护盾'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 114

