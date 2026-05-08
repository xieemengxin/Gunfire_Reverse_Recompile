# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51265.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51265.pyc
# Source Generated with Decompyle++
# File: p51265.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE, ATTACKERSUBMSG_NORMAL
from cl_newformula import Func369, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func369(*a))) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 51209, 0, 0):
        cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'w1010_Dam', (lambda *a: Func369(*a) / 20), 1)
        cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) // 100))
        if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) > 100000000:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33656, 0, { }, 1)
            cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) // 100))
    if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) > 100000000:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33656, 0, { }, 1)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL)


class CPerform(CCustomPerform):
    m_SID = 51265
    m_Name = '超载令牌专属词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

