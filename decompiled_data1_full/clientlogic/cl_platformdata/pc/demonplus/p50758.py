# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/demonplus/p50758.pyc
# RelativePath: clientlogic/cl_platformdata/pc/demonplus/p50758.pyc
# Source Generated with Decompyle++
# File: p50758.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.demonplus import CDemonPlus as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, 1, 0)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33171, 0, { }, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSelfSameLevel(oWarrior, oEventCB):
        cl_evact.EventCBGetTargetByEventMonster(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33171, 0, { }, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50758
    m_Name = '琉璃花木'
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
    m_DieDisable = 1
    m_WeakDisable = 0

