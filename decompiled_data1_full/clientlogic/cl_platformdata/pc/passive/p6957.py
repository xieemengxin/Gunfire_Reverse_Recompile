# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6957.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6957.pyc
# Source Generated with Decompyle++
# File: p6957.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 5500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 4500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'RShield', 15)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 300)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1427, 'ColdTime', 250)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 2, 0, 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1323, 'AddStateTime', 1500)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, -1, -1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) == 0:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1323)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, -1, -1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) == 1:
        cl_evact.EventCBSetCurPerformCD(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 6957
    m_Name = '千岁队友AI属性强制值'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

