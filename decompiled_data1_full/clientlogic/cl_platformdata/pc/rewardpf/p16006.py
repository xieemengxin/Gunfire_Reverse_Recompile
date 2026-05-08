# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16006.pyc
# Source Generated with Decompyle++
# File: p16006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_ELEMENT, DAM_TYPE_NORMAL, MAIN_HOLD, WEAPON_ELEMENTREFRESH_REMOVE, WEAPON_ELEMENTREFRESH_SET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, WEAPON_ELEMENTREFRESH_REMOVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, WEAPON_ELEMENTREFRESH_SET, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1614, 0, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckWeaponElementType(oWarrior, oEventCB, 'survivor', MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1614, 0, { }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckWeaponElementType(oWarrior, oEventCB, 'survivor', MAIN_HOLD, DAM_TYPE_ELEMENT):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 1614)


class CPerform(CCustomPerform):
    m_SID = 16006
    m_Name = '腐蚀转化'
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

