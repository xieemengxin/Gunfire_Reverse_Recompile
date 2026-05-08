# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6553.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6553.pyc
# Source Generated with Decompyle++
# File: p6553.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func308, Func522

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 1, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Rewardpf6553'):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Rewardpf6553', 1)
        cl_action.CommonSetDyingSecond(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func522(*a) * (100 + 10 * Func308(*a)) / 100))


class CPerform(CCustomPerform):
    m_SID = 6553
    m_Name = '我还能苟'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

