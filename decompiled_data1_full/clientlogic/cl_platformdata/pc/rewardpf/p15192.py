# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15192.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15192.pyc
# Source Generated with Decompyle++
# File: p15192.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15192 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import FOURSEASON_ROLLRELIC, LEVEL_TYPE_HIDE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonOpenTempRelicPlayType(oWarrior, oLifeCycle, FOURSEASON_ROLLRELIC)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_TEMPRELIC, FOURSEASON_ROLLRELIC, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonClearTempRelicPlayType(oWarrior, oLifeCycle, FOURSEASON_ROLLRELIC)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCheckHandleDisableSuit(oWarrior, oEventCB, 15198):
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'NoCanHandle', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE):
        CustomAction(oWarrior, oEventCB, {
            'MiniGame': 2430,
            'Suit': 15198 })


class CPerform(CCustomPerform):
    m_SID = 15192
    m_Name = '新旧交替套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

