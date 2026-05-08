# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51325.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51325.pyc
# Source Generated with Decompyle++
# File: p51325.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33681, 0, { }, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowAdditionCount', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalAdditionCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighAdditionCount', 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'LowAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'NormalAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'HighAdditionCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33681, { }, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33681, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33685, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RewardLevel', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRewardRatio', 0.5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRewardRatio', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRewardRatio', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowAdditionCount', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalAdditionCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighAdditionCount', 4)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'LowAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'NormalAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'HighAdditionCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33681, { }, None, None)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33685, { }, None, None)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33681, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33685, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RewardLevel', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRewardRatio', 0.5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRewardRatio', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRewardRatio', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowAdditionCount', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalAdditionCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighAdditionCount', 5)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'LowAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'NormalAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'HighAdditionCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33681, { }, None, None)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33685, { }, None, None)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33681, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33685, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RewardLevel', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalRewardRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EliteRewardRatio', 16)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BossRewardRatio', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LowAdditionCount', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NormalAdditionCount', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HighAdditionCount', 5)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'LowAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'NormalAdditionCount', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33681, 'HighAdditionCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33681, { }, None, None)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33685, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33685, { }, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LowAdditionCount'), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NormalAdditionCount'), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HighAdditionCount'), 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33681, { }, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NormalRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EliteRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oWarrior, oEventCB) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BossRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NormalRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EliteRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oWarrior, oEventCB) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BossRewardRatio')):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosDropRelic(oWarrior, oEventCB, {
            5823: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') })
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33685, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51325
    m_Name = '秘能魔匣'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

