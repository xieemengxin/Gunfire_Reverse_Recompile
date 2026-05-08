# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5725.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5725.pyc
# Source Generated with Decompyle++
# File: p5725.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_ATTACK, PF_SUBMSG_FILLBULLET, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1096, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1097, 1, 0, 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1098, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1097, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1096, 1, 0, 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1098, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1098, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1097, 1, 0, 0)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1096, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        5: 3333,
        6: 3333,
        7: 3334 }, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1096, 0, { }, 1, 1, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1097, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1098, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, -1, 8, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1, 8, 0, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1097, 0, { }, 1, 1, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1098, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1096, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, -1, 9, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1, 9, 0, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1098, 0, { }, 1, 1, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1096, 0, { }, 1, 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1097, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, -1, 10, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1, 10, 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0) or cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 0, 10000)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0) or cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 0):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 0, 10000)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 0) or cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 0, 10000)


class CPerform(CCustomPerform):
    m_SID = 5725
    m_Name = '元素魔方'
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
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

