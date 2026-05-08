# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15208.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15208.pyc
# Source Generated with Decompyle++
# File: p15208.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction152081, CustomAction152082, CustomAction152083
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.ImmunitySubSpdState(oWarrior, oLifeCycle)
    CustomAction152081(oWarrior, oLifeCycle, {
        'ForeverStateSID': 33514,
        'LimitStateSID': 33515 })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_REDUCESPEEDSTATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_REDUCESPEEDSTATE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction152082(oWarrior, oEventCB, {
        'ForeverStateSID': 33514,
        'LimitStateSID': 33515 })


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction152083(oWarrior, oEventCB, {
        'ForeverStateSID': 33514 })


class CPerform(CCustomPerform):
    m_SID = 15208
    m_Name = '柳暗花明套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

