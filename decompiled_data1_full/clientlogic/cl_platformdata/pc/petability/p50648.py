# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50648.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50648.pyc
# Source Generated with Decompyle++
# File: p50648.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJECT_SELFOWNER, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYMAIN, WARRIOR_PET_MINI
from cl_newformula import Func701

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINI):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func701(*a))) >= 3:
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, OBJECT_SELFOWNER):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnableCount', 0)
            cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 5)
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
            cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1445, 200, { }, 0, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnableCount') < 3 and cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'EnableCount', 1)
        cl_evact.EventCBTargetDie(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 50648
    m_Name = 'M8'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = (2001, 2002, 2421)
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

