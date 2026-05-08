# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5832.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5832.pyc
# Source Generated with Decompyle++
# File: p5832.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func423

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 15)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 15)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1426) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func423(*a))) > 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1426, 4500, { }, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1425, 1200, { }, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1425, (lambda *a: Func423(*a) // 100), 1, None, None)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1426) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func423(*a))) > 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1426, 2500, { }, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1425, 2500, { }, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1425, (lambda *a: Func423(*a) // 100), 1, None, None)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5832
    m_Name = '防弹痂壳'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

