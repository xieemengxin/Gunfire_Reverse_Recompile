# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6783.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6783.pyc
# Source Generated with Decompyle++
# File: p6783.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_TREASURE_DEAD, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 5:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1337, 0, { }, 1, 0, None)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 4:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1336, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1337, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 5:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1325, 0, { }, 1, 0, None)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 3:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1335, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1336, 0, { }, 1, 0, None)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 2:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1334, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1335, 0, { }, 1, 0, None)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 1:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1324, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1334, 0, { }, 1, 0, None)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 0:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1324, 0, { }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1323, 0, { }, 1, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_TREASURE_DEAD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 5:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1337, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 4:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1336, None, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1337, 0, { }, 1, 0, None)
            if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 5:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1325, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 3:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1335, None, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1336, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 2:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1334, None, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1335, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 1:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1324, None, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1334, 0, { }, 1, 0, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1323, None, None) == 0:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1323, 1, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1324, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6783
    m_Name = '玩家每拾取一个宝珠获得一层buff'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

