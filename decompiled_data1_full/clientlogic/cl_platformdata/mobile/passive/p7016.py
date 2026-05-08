# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p7016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p7016.pyc
# Source Generated with Decompyle++
# File: p7016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 2, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 1, 1, 160, 0, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveSpecialKey(oWarrior, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1744, 0, { })


class CPerform(CCustomPerform):
    m_SID = 7016
    m_Name = '轮回10连城大陨石被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

