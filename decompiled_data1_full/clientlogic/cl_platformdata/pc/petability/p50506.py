# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50506.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50506.pyc
# Source Generated with Decompyle++
# File: p50506.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckOwnerDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 0, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 1, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (0, None, ((304, 'HPMax'), (lambda a0: a0 // 50))))
    cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (0, None, ((304, 'HPMax'), (lambda a0: a0 // 50))))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (0, None, ((304, 'HPMax'), (lambda a0: a0 // 50))))
    cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (0, None, ((304, 'HPMax'), (lambda a0: a0 // 50))))


class CPerform(CCustomPerform):
    m_SID = 50506
    m_Name = 'D6'
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
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

