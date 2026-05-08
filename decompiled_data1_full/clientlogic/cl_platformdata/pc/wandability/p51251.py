# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51251.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51251.pyc
# Source Generated with Decompyle++
# File: p51251.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_POSITIVE
from cl_newformula import Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetItemCustomLimit(oWarrior, oLifeCycle, 'ColdTime', 10, 10000000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND_ATTR_CHANGE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND_ATTR_CHANGE, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'ColdTime', 0):
        cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', 0, (lambda *a: -Func779(*a) * 100), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', 0, (lambda *a: -Func779(*a) * 100), 1)


class CPerform(CCustomPerform):
    m_SID = 51251
    m_Name = '法杖冷却'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 6
    m_IsReverseFloting = 0

