# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15125.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15125.pyc
# Source Generated with Decompyle++
# File: p15125.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MAIN_HOLD, SUIT_HANDLE_ELEMENT, WEAPON_ELEMENTREFRESH_REMOVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_ELEMENT, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, WEAPON_ELEMENTREFRESH_REMOVE, 31, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 33, 0, 0)
    if cl_condition.CheckOwnerHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 32, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 33, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetSuit(oWarrior, oEventCB, 15125):
        cl_action.CommonCutSeasonSuitElement(oWarrior, oEventCB.GetCBLifeCycle(), 15125)


def DoCallBackAction31(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckWeaponElementType(oWarrior, oEventCB, 'ST33313', MAIN_HOLD, DAM_TYPE_NORMAL) and cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


def DoCallBackAction32(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD) and cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


def DoCallBackAction33(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15125
    m_Name = '#NT#元素弹药套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        31: DoCallBackAction31,
        32: DoCallBackAction32,
        33: DoCallBackAction33 }
    m_BaseArgData = { }
    m_DieDisable = 0

