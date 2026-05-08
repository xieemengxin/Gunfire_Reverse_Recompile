# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5870.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5870.pyc
# Source Generated with Decompyle++
# File: p5870.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func223

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5870):
        cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5870, None)
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func223(*a))) > 0 or cl_evcon.CheckHasState(oWarrior, oEventCB, 1875):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1875, 0, { }, 0, 0, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1875, (lambda *a: Func223(*a)), 0)
            cl_action.CommonRemoveAllTalent(oWarrior, oEventCB.GetCBLifeCycle())
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1876, 0, { }, 0, 0, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1876, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5870):
        cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5870, None)
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func223(*a))) > 0 or cl_evcon.CheckHasState(oWarrior, oEventCB, 1875):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1875, 0, { }, 0, 0, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1875, (lambda *a: Func223(*a) + 1), 0)
            cl_action.CommonRemoveAllTalent(oWarrior, oEventCB.GetCBLifeCycle())
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1876, 0, { }, 0, 0, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1876, 1)


class CPerform(CCustomPerform):
    m_SID = 5870
    m_Name = '否极泰来'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

