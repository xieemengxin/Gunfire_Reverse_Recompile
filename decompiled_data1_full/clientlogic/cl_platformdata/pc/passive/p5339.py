# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5339.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5339.pyc
# Source Generated with Decompyle++
# File: p5339.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        31839: 1 }, 1, 0):
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, -5000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5339
    m_Name = '精英蟹先锋四阶段'
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

