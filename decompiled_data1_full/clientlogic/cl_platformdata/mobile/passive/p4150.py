# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4150.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4150.pyc
# Source Generated with Decompyle++
# File: p4150.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8031, 695, { }, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CG_END, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheekFormPointBehavior(oWarrior, oEventCB, 21):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 8031, 0)


class CPerform(CCustomPerform):
    m_SID = 4150
    m_Name = '陆吾boss开场动画'
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

