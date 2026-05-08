# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4116.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4116.pyc
# Source Generated with Decompyle++
# File: p4116.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSummonSameWeaponSource(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9211, 1, 0):
        if cl_evcon.CheckWeaponHasInscription(oWarrior, oEventCB, 13030) or cl_evcon.CheckWeaponHasInscription(oWarrior, oEventCB, 13034):
            cl_evact.EventCBImmuneDamageByType(oWarrior, oEventCB, DAM_MASK_ELEMENT, None)
            if cl_evcon.CheckWeaponHasInscription(oWarrior, oEventCB, 13030):
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1502, 0, { }, 1)
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1502, 1, 1)
                cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HitRange', 5000 * cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1502, 1, None), 0, 0)
                cl_evact.EventCBChangeSummonModel(oWarrior, oEventCB, 100 + 40 * cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1502, 1, None))
            
        cl_evact.PassiveCBAttackerUsePerform(oWarrior, oEventCB, 1646, 400)
    else:
        cl_evact.EventCBImmuneDamageByType(oWarrior, oEventCB, DAM_MASK_ELEMENT, None)


class CPerform(CCustomPerform):
    m_SID = 4116
    m_Name = '闪电球技能'
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

