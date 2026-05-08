# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5713.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5713.pyc
# Source Generated with Decompyle++
# File: p5713.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1109, 1000, { }, 1, None, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1109, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1372, 1000, { }, 1, None, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1372, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5713
    m_Name = '元素圣物'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

