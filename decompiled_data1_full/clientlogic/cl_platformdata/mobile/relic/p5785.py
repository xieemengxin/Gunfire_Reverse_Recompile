# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5785.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5785.pyc
# Source Generated with Decompyle++
# File: p5785.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL
from cl_newformula import Func210, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1499):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1499, 1, None)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1499, 0, { }, 1, 1, None)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1499, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1499, -1, None)
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 1499 }))):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1499, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func210(*a))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1499, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1499, (lambda *a: Func210(*a)))
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1499, 0, { }, 1, 1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1500):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1500, 1, None)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1500, 0, { }, 1, 1, None)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1500, 1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1500, -1, None)
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 1500 }))):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1500, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func210(*a))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1500, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1500, (lambda *a: Func210(*a)))


class CPerform(CCustomPerform):
    m_SID = 5785
    m_Name = '噬邪法剑'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

