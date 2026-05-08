# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6734.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6734.pyc
# Source Generated with Decompyle++
# File: p6734.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_GOLDEN, LEVEL_TYPE_HALL, MG_SOURCE_RELIC, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1305, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_RELIC) == 0:
        cl_evact.CommonAddWarCashByReason(oWarrior, oEventCB, 600, '', 'NPC-4010-choose-event;shopbuy', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1305, None, None) == 0:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, 600, 1, JUMPFIGURE_GOLDEN, 600, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1305, 1, 0)
        else:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, 600, 1, JUMPFIGURE_GOLDEN, 600, None)


class CPerform(CCustomPerform):
    m_SID = 6734
    m_Name = '拾取秘卷，金爵会得铜币'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

