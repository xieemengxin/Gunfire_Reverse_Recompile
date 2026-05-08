# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6966.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6966.pyc
# Source Generated with Decompyle++
# File: p6966.pyc (Python 3.6)

from cl_platformdata.custom.passive.customaction import CustomAction6966 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, SIDE_TYPE_HERO
from cl_newformula import Func696, Func698, Func699

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 2, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SIGNALITEM, -1, 4)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            201: {
                1004: 1 },
            205: {
                1001: 1 },
            206: {
                1007: 1 },
            207: {
                1010: 1 },
            212: {
                1013: 1 },
            213: {
                1016: 1 },
            214: {
                1030: 1 },
            215: {
                1033: 1 },
            216: {
                1040: 1 },
            217: {
                1036: 1 },
            218: {
                1049: 1 },
            219: {
                1053: 1 },
            0: {
                1001: 1 } }, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func696(*a))):
        CustomAction(oWarrior, oEventCB, {
            'Tag': 'HeroDie',
            'Time': 1000,
            'Count': 2,
            'Ratio': 70 })
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SendEmotion'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SendEmotion', 0)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            201: {
                1020: 1 },
            205: {
                1022: 1 },
            206: {
                1021: 1 },
            207: {
                1025: 1 },
            212: {
                1026: 1 },
            213: {
                1027: 1 },
            214: {
                1028: 1 },
            215: {
                1029: 1 },
            216: {
                1043: 1 },
            217: {
                1039: 1 },
            218: {
                1052: 1 },
            219: {
                1057: 1 },
            0: {
                1001: 1 } }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 6000 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
        201: {
            1005: 1 },
        205: {
            1002: 1 },
        206: {
            1008: 1 },
        207: {
            1011: 1 },
        212: {
            1014: 1 },
        213: {
            1017: 1 },
        214: {
            1031: 1 },
        215: {
            1034: 1 },
        216: {
            1041: 1 },
        217: {
            1037: 1 },
        218: {
            1050: 1 },
        219: {
            1054: 1 },
        0: {
            1001: 1 } }, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func699(*a))):
        CustomAction(oWarrior, oEventCB, {
            'Tag': 'HeroSignal',
            'Time': 1000,
            'Count': 3,
            'Ratio': 70 })
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 5, 0, 0)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func698(*a))):
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
            205: {
                1001: 1,
                1002: 1,
                1003: 1 },
            201: {
                1004: 1,
                1005: 1,
                1006: 1 },
            206: {
                1007: 1,
                1008: 1,
                1009: 1 },
            207: {
                1010: 1,
                1011: 1,
                1012: 1 },
            212: {
                1013: 1,
                1014: 1,
                1015: 1 },
            213: {
                1016: 1,
                1017: 1,
                1018: 1 },
            214: {
                1030: 1,
                1031: 1,
                1032: 1 },
            215: {
                1033: 1,
                1034: 1,
                1035: 1 },
            216: {
                1040: 1,
                1041: 1,
                1042: 1 },
            217: {
                1036: 1,
                1037: 1,
                1038: 1 },
            218: {
                1049: 1,
                1050: 1,
                1051: 1 },
            219: {
                1053: 1,
                1054: 1,
                1055: 1 },
            0: {
                1001: 1 } }, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SendEmotion'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'SendEmotion', 0)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        cl_evact.EventCBSendEmote(oWarrior, oEventCB, {
            201: {
                1023: 1 },
            205: {
                1019: 1 },
            206: {
                1024: 1 },
            207: {
                1044: 1 },
            212: {
                1046: 1 },
            213: {
                1048: 1 },
            214: {
                1028: 1 },
            215: {
                1029: 1 },
            216: {
                1043: 1 },
            217: {
                1039: 1 },
            218: {
                1056: 1 },
            219: {
                1058: 1 },
            0: {
                1001: 1 } }, 1)


class CPerform(CCustomPerform):
    m_SID = 6966
    m_Name = '队友AI表情'
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

