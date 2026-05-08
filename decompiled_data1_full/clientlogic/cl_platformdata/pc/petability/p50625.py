# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50625.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50625.pyc
# Source Generated with Decompyle++
# File: p50625.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_ATTACK, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 48)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf7345_Dam', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 7345, {
            'Att': max(cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf7345_Dam'), 100) }, None)


class CPerform(CCustomPerform):
    m_SID = 50625
    m_Name = 'D1'
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
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

