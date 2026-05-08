# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51275.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51275.pyc
# Source Generated with Decompyle++
# File: p51275.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_QUALITY_FOUR, ABILITY_QUALITY_THREE, ABILITY_TYPE_POSITIVE, VIRTUAL_ITEM_WANDCOMP, WANDCOMP_TRIGGER_ACTION, WAND_QUALITY_RARE
from cl_newformula import Func651, Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMP, WANDCOMP_TRIGGER_ACTION, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemQuality(oWarrior, oEventCB, WAND_QUALITY_RARE, VIRTUAL_ITEM_WANDCOMP) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 1, (lambda *a: Func779(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurPos', (lambda *a: Func651(*a, **{
'sKey': 'CurPos' })))
    cl_action.CommonTriggerWandComp(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurPos'))


class CPerform(CCustomPerform):
    m_SID = 51275
    m_Name = '重复稀有'
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
    m_QualityValue = {
        ABILITY_QUALITY_FOUR: 2,
        ABILITY_QUALITY_THREE: 1 }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

