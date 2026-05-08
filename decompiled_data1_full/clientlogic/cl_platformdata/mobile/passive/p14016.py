# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14016.pyc
# Source Generated with Decompyle++
# File: p14016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, FIGHT_KEY_WUDI, MONSTER_PFAI_DODGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 5, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'IntervalTime', -8000, 0, 0)
    cl_action.CommonSetPFAIGroupWeightByType(oWarrior, oLifeCycle, MONSTER_PFAI_DODGE, 38031, 50)
    cl_action.CommonSetPFAIGroupWeightByType(oWarrior, oLifeCycle, MONSTER_PFAI_DODGE, 38032, 50)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        38031: 1,
        38032: 1 }, 1, 0):
        cl_action.CommonAddSpecialKey(oWarrior, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        38031: 1,
        38032: 1 }, 1, 0):
        cl_action.CommonRemoveSpecialKey(oWarrior, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI)


class CPerform(CCustomPerform):
    m_SID = 14016
    m_Name = '轮回9-鲶人武士'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

