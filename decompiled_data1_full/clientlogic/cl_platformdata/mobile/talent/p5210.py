# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5210.pyc
# Source Generated with Decompyle++
# File: p5210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, STATUS_STOP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_action.CommonRemoveSameSourceState(oWarrior, oEventCB.GetCBLifeCycle(), 1003, 1620)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1603, None, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1603, 0, { }, 1, -1, None)
    elif cl_evcon.CheckLastMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_action.CommonRemoveSameSourceState(oWarrior, oEventCB.GetCBLifeCycle(), 1003, 1620)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1620, 500, { }, 1, -1, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1603, None, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1603, 500, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, -1, -1):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1603, None, None, None)
        cl_action.CommonRemoveSameSourceState(oWarrior, oEventCB.GetCBLifeCycle(), 1003, 1620)


class CPerform(CCustomPerform):
    m_SID = 5210
    m_Name = '不动如山'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 4
    m_IsRareTalent = 1
    m_Career = 0

