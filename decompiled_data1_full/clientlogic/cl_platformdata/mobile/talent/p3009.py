# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3009.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3009.pyc
# Source Generated with Decompyle++
# File: p3009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_TYPE_THROW
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32715, 800, { }, 1, None, None)
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 800, { }, 1)
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32716 }))) < 10:
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1, None)
            elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 800, { }, 1)
                if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32716 }))) < 10:
                    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32715, 800, { }, 1, None, None)
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1200, { }, 1)
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32716 }))) < 15:
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1, None)
            elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1200, { }, 1)
                if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32716 }))) < 15:
                    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32716, 1, None)


class CPerform(CCustomPerform):
    m_SID = 3009
    m_Name = '此消彼长'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 111

