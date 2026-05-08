# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5745.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5745.pyc
# Source Generated with Decompyle++
# File: p5745.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, STATUS_STOP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1128, 0, None, None) == 0:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1128, 0, { }, 1, None, None)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1398, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1128, 0, 0, None):
                cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1128, None, None, None)
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1398, 400, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1463, None, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1463, 0, { }, 1, None, None)
    elif cl_evcon.CheckLastMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1463, None, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1463, 400, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 5745
    m_Name = '坚如磐石'
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
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

