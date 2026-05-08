# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5791.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5791.pyc
# Source Generated with Decompyle++
# File: p5791.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func548

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1190, 0, 0, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1190, 0, { }, 1, 0, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1226, 0, { }, 1, 0, None)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12013, 1, 0):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, (lambda *a: Func548(*a)), 200, 0)
    else:
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, 1, 200, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if not cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1226, 0, None) >= 50:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1190, 0, 0, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1190, 0, { }, 1, 0, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1226, 0, { }, 1, 0, None)
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12013, 1, 0):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, (lambda *a: Func548(*a)), 200, 0)
        else:
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, 1, 200, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if not cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1226, 0, None) >= 50:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1190, 0, 0, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1190, 0, { }, 1, 0, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1226, 0, { }, 1, 0, None)
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12009, 1, 0):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, (lambda *a: Func548(*a)), 300, 0)
        else:
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1226, 1, 300, 0)


class CPerform(CCustomPerform):
    m_SID = 5791
    m_Name = '无情连击'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

