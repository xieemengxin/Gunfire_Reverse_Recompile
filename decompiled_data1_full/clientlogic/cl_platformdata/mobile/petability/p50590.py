# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50590.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50590.pyc
# Source Generated with Decompyle++
# File: p50590.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckAssistKill(oWarrior, oEventCB):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'killnum', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'killnum') >= 2:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'killnum', 0)
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'killnum') >= 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'killnum', 0)
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 50590
    m_Name = '50590词条'
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
    m_BaseArgData = {
        'killnum': 0 }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

