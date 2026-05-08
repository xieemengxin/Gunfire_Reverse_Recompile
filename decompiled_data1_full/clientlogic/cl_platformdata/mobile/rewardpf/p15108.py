# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15108.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15108.pyc
# Source Generated with Decompyle++
# File: p15108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15108 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import SUIT_HANDLE_INTENSIFY

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_INTENSIFY, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CORERELIC, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_CORERELIC, -1, 7, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonClearSeasonSuitTempRelic(oWarrior, oLifeCycle, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBEnableTempRelic(oWarrior, oEventCB, 1, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBUpdateTempRelic(oWarrior, oEventCB)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonSendSeasonSuitTempRelic(oWarrior, oEventCB.GetCBLifeCycle(), 0, 2, 1)
    cl_action.CommonBanTagerRelicToTempRelic(oWarrior, oEventCB.GetCBLifeCycle(), {
        5875: 1,
        5874: 1,
        5859: 1,
        5841: 1,
        5870: 1,
        5868: 1,
        5873: 1,
        5885: 1,
        5887: 1,
        5888: 1,
        5889: 1 })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonBanTagerRelicToTempRelic(oWarrior, oEventCB.GetCBLifeCycle(), {
        5875: 1,
        5874: 1,
        5859: 1,
        5841: 1,
        5870: 1,
        5868: 1,
        5873: 1,
        5885: 1,
        5887: 1,
        5888: 1,
        5889: 1 })


def DoCallBackAction5(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'TempLevel': 2,
        'Group': 6 })


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) or cl_evcon.EventCheckRelicIsGoldBoxSuper(oWarrior, oEventCB):
        cl_action.CommonSendSeasonSuitTempRelic(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2, 1)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1)
    else:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventCBUpdateTempRelicByCoreRelic(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 15108
    m_Name = '#NT#强化秘卷套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

