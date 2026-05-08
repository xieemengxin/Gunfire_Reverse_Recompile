# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16082.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16082.pyc
# Source Generated with Decompyle++
# File: p16082.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1623)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1627)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1631)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1887, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1631, 0, { })
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1627, 0, { })
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1623, 0, { })


class CPerform(CCustomPerform):
    m_SID = 16082
    m_Name = '彩色弹夹'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

