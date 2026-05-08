# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15102.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15102.pyc
# Source Generated with Decompyle++
# File: p15102.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_NORMAL, MAIN_HOLD, OBJECT_OWNER, OBJECT_SERVANT, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_THROW, WEAPON_ELEMENTREFRESH_REMOVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, WEAPON_ELEMENTREFRESH_REMOVE, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 4, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    if not cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW)
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBPerformDamType(oWarrior, oEventCB, OBJECT_OWNER, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oWarrior, oEventCB, OBJECT_OWNER)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBPerformDamType(oWarrior, oEventCB, OBJECT_SERVANT, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oWarrior, oEventCB, OBJECT_SERVANT)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckWeaponElementType(oWarrior, oEventCB, 'ST33313', MAIN_HOLD, DAM_TYPE_NORMAL) and cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD) and cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, DAM_TYPE_NORMAL):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33313, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15102
    m_Name = '#NT#元素秘法套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

