# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p15705.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p15705.pyc
# Source Generated with Decompyle++
# File: p15705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import JUMPFIGURE_BUYGOODS, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func364

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTWARCASH, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTWARCASH, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func364(*a))) < 0:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func364(*a) * 3 // 20), 0, JUMPFIGURE_BUYGOODS, (lambda *a: -Func364(*a) * 3 // 20), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func364(*a))) < 0:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 7500,
            3: 2500 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func364(*a) * 3 // 20), 0, JUMPFIGURE_BUYGOODS, (lambda *a: -Func364(*a) * 3 // 20), 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func364(*a) // 2), 0, JUMPFIGURE_BUYGOODS, (lambda *a: -Func364(*a)), 1)


class CPerform(CCustomPerform):
    m_SID = 15705
    m_Name = '高级会员'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

