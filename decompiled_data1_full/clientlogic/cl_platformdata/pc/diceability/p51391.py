# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51391.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51391.pyc
# Source Generated with Decompyle++
# File: p51391.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, PF_SUBMSG_COMMON, PF_TYPE_THROW
from cl_newformula import Func369, Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LoopTimes', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1986, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1986)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LoopTimes', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1986, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1986)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LoopTimes', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1986, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1986)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LoopTimes', 8)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 80)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1986, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1986)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33889, 0, 1, 0, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33889, 1, 1, 0, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33889, 0, {
                'LoopTimes': (lambda *a: Func717(*a, **{
'sArg': 'LoopTimes' })),
                'IntervalTime': (lambda *a: Func717(*a, **{
'sArg': 'IntervalTime' })),
                'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })),
                'Distance': (lambda *a: Func717(*a, **{
'sArg': 'Distance' })),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
                'BaseDam': (lambda *a: Func369(*a)) }, 1, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1986, 1, 0):
        cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-1986Cnt', -1, None)


class CPerform(CCustomPerform):
    m_SID = 51391
    m_Name = '灵力绽放'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

