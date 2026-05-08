# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6518.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6518.pyc
# Source Generated with Decompyle++
# File: p6518.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func207, Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (lambda *a: Func207(*a) * 5 / 100 + 0))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (lambda *a: Func207(*a) * 10 / 100 + 0))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (lambda *a: Func207(*a) * 15 / 100 + 0))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (lambda *a: Func207(*a) * 20 / 100 + 0))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, (lambda *a: Func207(*a) * 25 / 100 + 0))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeGetCash(oWarrior, oEventCB, (lambda *a: Func308(*a) * 500 + 0), 0)


class CPerform(CCustomPerform):
    m_SID = 6518
    m_Name = '额外金币'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

