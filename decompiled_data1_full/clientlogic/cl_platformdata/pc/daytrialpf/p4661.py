# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4661.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4661.pyc
# Source Generated with Decompyle++
# File: p4661.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1290, 0, { }, 0, 0, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1291) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1290):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1291, None, None, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1290) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1292):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1292, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1291, 0, { }, 0, 0, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1290) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1291):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1290, None, None, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1292) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1291):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1292, None, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1292, 0, { }, 0, 0, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1292) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1290):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1290, None, None, None)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1291) and cl_evcon.CheckHasState(oWarrior, oEventCB, 1292):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1291, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4661
    m_Name = '元素短路'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

