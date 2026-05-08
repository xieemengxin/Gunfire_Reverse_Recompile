# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51295.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51295.pyc
# Source Generated with Decompyle++
# File: p51295.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE, WANDCOMP_TRIGGER_ACTION
from cl_newformula import Func651, Func765

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMP, WANDCOMP_TRIGGER_ACTION, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CurPos' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func765(*a) - 1)):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 2000 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonTriggerWandComp(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func765(*a) - 2))


class CPerform(CCustomPerform):
    m_SID = 51295
    m_Name = '响尾令牌专属词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

