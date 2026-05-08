# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6959.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6959.pyc
# Source Generated with Decompyle++
# File: p6959.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func201

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 5500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 4500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'RShield', 15)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 300)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1423, 'ColdTime', 1000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1423, 'DebuffProb', 6000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1316, 'ColdTime', 1000)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1316, 'DebuffProb', 10000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckIsAIMember(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.CommonListenGlobalMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_LEVEL_LAYERSTART, -1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) == 2 and cl_evcon.CheckTalent(oWarrior, oEventCB, 3115) == 0:
        cl_action.CommonAddTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3115, 0, 2)
    elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) == 3 and cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 3115) == 2:
        cl_action.CommonAddTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3115, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 6959
    m_Name = '璃队友AI属性强制值'
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

