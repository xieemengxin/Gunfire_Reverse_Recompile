# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15166.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15166.pyc
# Source Generated with Decompyle++
# File: p15166.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func599

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33462, 0, {
        'Dam': 900 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33462, 0, {
        'Dam': 900 }, 1)
    cl_action.CommonChangePositiveElementFactor(oWarrior, oLifeCycle, 2500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33462, 0, {
        'Dam': 1500 }, 1)
    cl_action.CommonChangePositiveElementFactor(oWarrior, oLifeCycle, 2500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33462, 1, 500)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.EventCBCheckTargetHasElementState(oWarrior, oEventCB, {
        20026: 1,
        20027: 1,
        20028: 1 }, 0) or cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 5000 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        4: 3333,
        5: 3333,
        6: 3334 }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, DAM_TYPE_FIRE, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func599(*a))) > 1:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func599(*a) * 1500), DAM_MASK_ELEMENT, '')
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.EventCBCheckTargetHasElementState(oWarrior, oEventCB, {
        20026: 1,
        20027: 1,
        20028: 1 }, 0) or cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 3333,
            5: 3333,
            6: 3334 }, 1)


class CPerform(CCustomPerform):
    m_SID = 15166
    m_Name = '元素宝典'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

