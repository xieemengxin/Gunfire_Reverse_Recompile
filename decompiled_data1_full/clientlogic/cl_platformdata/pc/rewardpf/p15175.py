# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15175.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15175.pyc
# Source Generated with Decompyle++
# File: p15175.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD
from cl_newformula import Func594

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, -2000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func594(*a))) >= 0:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func594(*a)), 0)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: -Func594(*a) * 3), 0)
    elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func594(*a))) >= 0:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func594(*a)), 0)
        else:
            cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: -Func594(*a) * 3), 0)


class CPerform(CCustomPerform):
    m_SID = 15175
    m_Name = '立体防御'
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

