# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51231.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51231.pyc
# Source Generated with Decompyle++
# File: p51231.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2001)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 31342, 1, 0):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'IsDashing', 1)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 2001, 0, {
            'LimitDis': 420,
            'Disoffset': 50,
            'PosLiveTime': 500 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 31342, 1, 0):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'IsDashing', 0)


class CPerform(CCustomPerform):
    m_SID = 51231
    m_Name = '#NT#轮回10精英冲锋兵额外被动'
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

