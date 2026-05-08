# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5768.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5768.pyc
# Source Generated with Decompyle++
# File: p5768.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_VICTIM, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 20)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, None, None) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 20)
    elif cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 20):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 3333,
            4: 3333,
            5: 3334 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 20):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 3333,
            4: 3333,
            5: 3334 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, None)


class CPerform(CCustomPerform):
    m_SID = 5768
    m_Name = '元素折磨'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

