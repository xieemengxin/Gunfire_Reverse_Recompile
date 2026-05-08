# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50581.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50581.pyc
# Source Generated with Decompyle++
# File: p50581.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 4000)
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'RelifeTime', -9000, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'RelifeTime', 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50581
    m_Name = ''
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
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

