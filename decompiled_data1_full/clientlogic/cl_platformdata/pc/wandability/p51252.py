# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51252.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51252.pyc
# Source Generated with Decompyle++
# File: p51252.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_POSITIVE, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE
from cl_newformula import Func751, Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33655, 0, {
        'BaseAdd': (lambda *a: Func779(*a)) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'Wand') == cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func751(*a))):
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33655, cl_condition.CommonGetCompNumFromSrcWand(oWarrior, oEventCB.GetCBLifeCycle(), {
            2027: 1,
            2033: 1,
            2117: 1 }), 0)


class CPerform(CCustomPerform):
    m_SID = 51252
    m_Name = '词条增幅'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 3
    m_IsReverseFloting = 0

