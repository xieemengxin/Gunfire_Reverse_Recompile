# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51300.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51300.pyc
# Source Generated with Decompyle++
# File: p51300.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_QUALITY_THREE, ABILITY_TYPE_EXCLUSIVE, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_SUBMSG_FINISHCONDITION
from cl_newformula import Func779, Func794, Func796

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'CompPos') == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func796(*a))):
        cl_evact.EventCBAddCurWandConditionCount(oWarrior, oEventCB, (lambda *a: Func779(*a)), 1, {
            cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'CompPos'): 1 }, {
            1017: 1,
            1021: 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeWandAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', 0, (lambda *a: -10 * Func794(*a)))


class CPerform(CCustomPerform):
    m_SID = 51300
    m_Name = '搭配令牌专属词条'
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
        ABILITY_QUALITY_THREE: 33 }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

