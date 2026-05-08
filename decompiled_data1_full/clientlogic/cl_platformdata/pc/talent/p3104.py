# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3104.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3104.pyc
# Source Generated with Decompyle++
# File: p3104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_THROW
from cl_newformula import Func304, Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None) and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32661) == 0:
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 3104) <= 2:
            if oWarrior.Energy() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }))):
                if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32706):
                    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32706, 0, { }, 1)
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32706, (lambda *a: 2 + 3 * Func308(*a)), 500, 0)
                cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 300 * Func308(*a)), 0)
            else:
                cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 300 * Func308(*a)), 0)
        elif oWarrior.Energy() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }))):
            if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32706):
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32706, 0, { }, 1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32706, 14, 500, 0)
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 1000, 0)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 1000, 0)


class CPerform(CCustomPerform):
    m_SID = 3104
    m_Name = '灵火识主'
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
    m_Career = 112

