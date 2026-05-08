# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51254.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51254.pyc
# Source Generated with Decompyle++
# File: p51254.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_POSITIVE, OBJ_SELF, WANDCOMP_SUBMSG_ADD
from cl_newformula import Func651, Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonChangeWandConditionCount(oWarrior, oLifeCycle, (lambda *a: -Func779(*a)), 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'WandCompSID' }))) == 1017:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33600, (lambda *a: -(100 * Func779(*a)) // 100), 0)
    elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'WandCompSID' }))) == 1021:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33628, (lambda *a: -(200 * Func779(*a)) // 100), 0)
    else:
        cl_evact.PassiveEventCBChangeFinishCondition(oWarrior, oEventCB, (lambda *a: -Func779(*a)), 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33600):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33600, (lambda *a: -(100 * Func779(*a)) // 100), 0)
    elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33628):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBChangeTargetStateDelayTime(oWarrior, oEventCB, 33628, (lambda *a: -(200 * Func779(*a)) // 100), 0)


class CPerform(CCustomPerform):
    m_SID = 51254
    m_Name = '条件缩短'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 10
    m_IsReverseFloting = 0

