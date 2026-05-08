# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3111.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3111.pyc
# Source Generated with Decompyle++
# File: p3111.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, OBJ_SELF
from cl_newformula import Func331, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32631, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33456, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32631, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33456, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32631, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33456, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32631, (lambda *a: 3 + Func331(*a, **{
'sid': 3111 }) * 2), 0)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32631 }))) >= 15:
            cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 3, (lambda *a: Func410(*a, **{
'sid': 32631 }) // 15), None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32631, -15, 0)
    cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 1500, 0)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32634):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32634, 1, 800)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32634, 800, { }, 0, 0, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32634, 1, 0, 0, 800)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33456):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33456, 1, 500)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33456, 500, { }, 0, 0, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33456, 1, 0, 0, 500)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'EleAbnormal') == 0:
        if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERFORM) or cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32631, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 3111
    m_Name = '兵火交融'
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
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 112

