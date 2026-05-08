# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p6972.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p6972.pyc
# Source Generated with Decompyle++
# File: p6972.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, SIDE_TYPE_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 2, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SIGNALITEM, -1, 4)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            1033: 1 }, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((696,), (lambda a0: a0)))):
        CustomAction(oWarrior, oEventCB, {
            'Tag': 'HeroDie',
            'Time': 1000,
            'Count': 2,
            'Ratio': 70 })
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SendEmotion'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SendEmotion', 0)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            1029: 1,
            1034: 1 }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 6000 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
        1034: 1 }, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((699,), (lambda a0: a0)))):
        CustomAction(oWarrior, oEventCB, {
            'Tag': 'HeroSignal',
            'Time': 1000,
            'Count': 3,
            'Ratio': 70 })
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 5, 0, 0)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((698,), (lambda a0: a0)))):
        CustomAction(oWarrior, oEventCB, {
            'Tag': 'AISignal',
            'Time': 1000,
            'Count': 3,
            'Ratio': 70 })
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 6, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SendEmotion'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SendEmotion', 0)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            1033: 1,
            1034: 1,
            1035: 1 }, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SendEmotion'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SendEmotion', 0)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            1029: 1,
            1033: 1 }, 1)


class CPerform(CCustomPerform):
    m_SID = 6972
    m_Name = '璃队友AI表情'
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
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

