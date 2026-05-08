# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5807.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5807.pyc
# Source Generated with Decompyle++
# File: p5807.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_FRIEND_HERONOSELF, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, STATUS_DASH, STATUS_JUMP, STATUS_MOVE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 100, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 10, 100, 4)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_MOVE) or cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_JUMP) or cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_DASH):
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1223, 0, 0, None, None) < 1:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1223, 0, { }, 1, 0, None)
        cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 15, OBJ_FRIEND_HERONOSELF, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)
    else:
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1223, None, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1236, 100, { }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_MOVE) or cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_JUMP) or cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_DASH):
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1482, 0, 0, None, None) < 1:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1482, 0, { }, 1, 0, None)
        cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 0, 1, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 7)
    else:
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1482, None, None, None)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1483, 100, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5807
    m_Name = '极速支援'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

