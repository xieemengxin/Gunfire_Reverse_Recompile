# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51286.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51286.pyc
# Source Generated with Decompyle++
# File: p51286.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_NEGATIVE, VIRTUAL_ITEM_WANDCOMP, WANDCOMP_RARITY_NORMAL, WANDCOMP_RARITY_RARE, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_QUALITY_TALE
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33661, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33661, cl_action.CommonGetRarityWandCompNum(oWarrior, oLifeCycle, 1, {
        WANDCOMP_RARITY_RARE: 1,
        WANDCOMP_RARITY_NORMAL: 1 }), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemQuality(oWarrior, oEventCB, WAND_QUALITY_TALE, VIRTUAL_ITEM_WANDCOMP) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompType' }))):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33661, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemQuality(oWarrior, oEventCB, WAND_QUALITY_TALE, VIRTUAL_ITEM_WANDCOMP) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompType' }))):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33661, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51286
    m_Name = '非金勿扰'
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
    m_AbilityType = ABILITY_TYPE_NEGATIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

