# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15073.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15073.pyc
# Source Generated with Decompyle++
# File: p15073.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 123, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 122, 2, None, None)


class CPerform(CCustomPerform):
    m_SID = 15073
    m_Name = '飞牌摘叶'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

