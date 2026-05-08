# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13514.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13514.pyc
# Source Generated with Decompyle++
# File: p13514.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func541, Func553

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32722, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func541(*a))) > 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32723, 1000, { }, 1, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32723, (lambda *a: Func541(*a)), 0, 0, 1000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func553(*a, **{
'sAttr': 'HP' }))) > 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32723, 0, { }, 1, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32723, (lambda *a: Func553(*a, **{
'sAttr': 'HP' })), 0, 0, 1000)


class CPerform(CCustomPerform):
    m_SID = 13514
    m_Name = '恃强凌弱'
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
    m_DieDisable = 1
    m_Career = 103

