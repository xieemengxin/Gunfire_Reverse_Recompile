# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51277.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51277.pyc
# Source Generated with Decompyle++
# File: p51277.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_NEGATIVE, OBJ_SELF, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_SUBMSG_TRIGGERACTION
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CommonCheckInPointWand(oWarrior, oLifeCycle, {
        1016: 1 }):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 2, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: max(int((Func304(*a, **{
'sAttr': 'HPMax' }) * -5 // 10000) * 100), int(Func304(*a, **{
'sAttr': 'HP' }) * -100 / 100 + 100))))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CommonGetCompNumByType(oWarrior, oEventCB.GetCBLifeCycle(), 1) == 0:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CommonGetCompNumByType(oWarrior, oEventCB.GetCBLifeCycle(), 1) != 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51277
    m_Name = '献祭施法'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_NEGATIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

