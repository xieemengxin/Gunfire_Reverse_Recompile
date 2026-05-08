# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13004.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13004.pyc
# Source Generated with Decompyle++
# File: p13004.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_item.defines import ITEM_MODE_DRILLFOCUS

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ITEM_CHANGE_MODE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemMode(oWarrior, oEventCB, ITEM_MODE_DRILLFOCUS):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1859, 0, { }, -1, -1)
    elif not cl_evcon.EventCBCheckWeaponModeByHoldType(oWarrior, oEventCB, 0, ITEM_MODE_DRILLFOCUS):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1859, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckWeaponModeByHoldType(oWarrior, oEventCB, 0, ITEM_MODE_DRILLFOCUS):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1859, 0)


class CPerform(CCustomPerform):
    m_SID = 13004
    m_Name = '逐风'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1606,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

