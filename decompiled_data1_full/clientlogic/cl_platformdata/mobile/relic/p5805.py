# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5805.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5805.pyc
# Source Generated with Decompyle++
# File: p5805.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_FRIEND_HERO, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 50, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1224, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 50, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1224, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 20, OBJ_FRIEND_HERO, 0)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1224, cl_evact.EventCBGetHasStateTargetNum(oWarrior, oEventCB, 1224))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 0, None)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1224, cl_evact.EventCBGetHasStateTargetNum(oWarrior, oEventCB, 1224))


class CPerform(CCustomPerform):
    m_SID = 5805
    m_Name = '惺惺相惜'
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
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

