# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4423.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4423.pyc
# Source Generated with Decompyle++
# File: p4423.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import TYPE_RELIFE_PASSIVE
from cl_newformula import Func11

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeTimesKey(oWarrior, oEventCB) and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func11(*a, **{
'iVal': 2 }))):
        cl_action.CommonSetRelifeAttr(oWarrior, oEventCB.GetCBLifeCycle(), TYPE_RELIFE_PASSIVE, 300, 1, 2, { }, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func11(*a, **{
'iVal': 2 }))):
        cl_action.CommonSetRelifeAttr(oWarrior, oEventCB.GetCBLifeCycle(), TYPE_RELIFE_PASSIVE, 300, 1, 2, { }, None, None)


class CPerform(CCustomPerform):
    m_SID = 4423
    m_Name = '概率复活'
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

