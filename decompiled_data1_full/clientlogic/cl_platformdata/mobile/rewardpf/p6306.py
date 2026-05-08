# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6306.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6306.pyc
# Source Generated with Decompyle++
# File: p6306.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (0, None, ((207,), (lambda a0: a0 * 5 / 100 + 0))))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (0, None, ((207,), (lambda a0: a0 * 10 / 100 + 0))))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (0, None, ((207,), (lambda a0: a0 * 15 / 100 + 0))))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (0, None, ((207,), (lambda a0: a0 * 20 / 100 + 0))))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeGetCash(oWarrior, oEventCB, (0, None, ((308,), (lambda a0: a0 * 500 + 0))), 0)


class CPerform(CCustomPerform):
    m_SID = 6306
    m_Name = '图纸1026-1029额外金币'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

