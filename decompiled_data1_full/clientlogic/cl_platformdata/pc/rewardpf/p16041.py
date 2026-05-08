# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16041.pyc
# Source Generated with Decompyle++
# File: p16041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_USE_ALL, DAM_USE_HP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)
    cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'CanCureAll', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 32015, 0, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.QueryAttr('HPMax') == oWarrior.HP():
        cl_evact.EventChangeCureType(oWarrior, oEventCB, DAM_USE_HP, DAM_USE_ALL, -1)


class CPerform(CCustomPerform):
    m_SID = 16041
    m_Name = '光盘行动'
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

