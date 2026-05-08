# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51726.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51726.pyc
# Source Generated with Decompyle++
# File: p51726.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, S8THIRDACTIVE_STATE_ALLEND, S8THIRDACTIVE_STATE_START
from cl_newformula import Func14, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StartFrame'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StartFrame', (lambda *a: Func14(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StartFrame'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39775, 1, 0, 0):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39775, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39775, (lambda *a: min(Func859(*a, **{
'sAttr': 'MaxSecond' }), ((Func14(*a) - Func717(*a, **{
'sArg': 'StartFrame' })) // 25) * Func859(*a, **{
'sAttr': 'PerSecond' }))), 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StartFrame', 0)


class CPerform(CCustomPerform):
    m_SID = 51726
    m_Name = '主要技能持续时长'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'MaxSecond': 300,
            'PerSecond': 20 },
        2: {
            'MaxSecond': 600,
            'PerSecond': 40 },
        3: {
            'MaxSecond': 1200,
            'PerSecond': 80 } }

