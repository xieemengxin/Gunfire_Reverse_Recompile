# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51222.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51222.pyc
# Source Generated with Decompyle++
# File: p51222.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE
from cl_newformula import Func651, Func750, Func794

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 0, 0, 0)
    cl_action.CommonChangeWandAttr(oWarrior, oLifeCycle, 'ColdTime', 0, (lambda *a: -100 * Func794(*a)))
    cl_action.CommonSetMinTriggerAllCompNum(oWarrior, oLifeCycle, (lambda *a: max(1, Func794(*a))))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 0, 0, 0)
    cl_action.CommonChangeWandAttr(oWarrior, oLifeCycle, 'ColdTime', 0, (lambda *a: -100 * Func794(*a)))
    cl_action.CommonSetMinTriggerAllCompNum(oWarrior, oLifeCycle, (lambda *a: max(1, Func794(*a))))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 0, 0, 0)
    cl_action.CommonChangeWandAttr(oWarrior, oLifeCycle, 'ColdTime', 0, (lambda *a: -100 * Func794(*a)))
    cl_action.CommonSetMinTriggerAllCompNum(oWarrior, oLifeCycle, (lambda *a: max(1, Func794(*a))))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompType' }))) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func750(*a))):
        cl_action.CommonChangeWandAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', 0, (lambda *a: -100 * Func794(*a)))
        cl_action.CommonSetMinTriggerAllCompNum(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: max(1, Func794(*a))))
        cl_action.CommonResetWandConditionComp(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 51222
    m_Name = '#NT#搭配法杖被动'
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

