# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4873.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4873.pyc
# Source Generated with Decompyle++
# File: p4873.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.PassiveCBSetAndReturnWeaponAttrTimes(oWarrior, oEventCB, 'p4873', 150) >= 4:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1180, 1, 1, None):
            cl_evact.PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, 1180, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1180, 400, { }, 1, None, None)
        cl_evact.PassiveCBClearWeaponAttrTimes(oWarrior, oEventCB, 'p4873')


class CPerform(CCustomPerform):
    m_SID = 4873
    m_Name = '渐入佳境'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((16, 17, 18, 19, 1, 20, 23), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

