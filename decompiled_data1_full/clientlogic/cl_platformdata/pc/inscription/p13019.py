# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13019.pyc
# Source Generated with Decompyle++
# File: p13019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBSetAndReturnWeaponAttrTimes(oWarrior, oEventCB, 'p13019', 100) >= 10:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1374, 1, 1, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1374, 600, { }, 1, None, None)
        cl_evact.PassiveCBClearWeaponAttrTimes(oWarrior, oEventCB, 'p13019')


class CPerform(CCustomPerform):
    m_SID = 13019
    m_Name = '紫翎之光'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1102,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

