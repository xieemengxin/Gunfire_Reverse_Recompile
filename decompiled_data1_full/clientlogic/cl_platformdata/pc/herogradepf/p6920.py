# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6920.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6920.pyc
# Source Generated with Decompyle++
# File: p6920.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import FUNCMODE_TYPE_ADDNEWTALENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLOGIN, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'p6920') == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33775, 0, { }, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33775):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1)
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'p6920', 1)
        cl_action.CommonSwitchMode(oWarrior, oEventCB.GetCBLifeCycle(), FUNCMODE_TYPE_ADDNEWTALENT, 1, { }, 1)
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 1, 2507, { })


class CPerform(CCustomPerform):
    m_SID = 6920
    m_Name = '苍玦lv.5'
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

