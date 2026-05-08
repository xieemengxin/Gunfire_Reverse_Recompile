# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50692.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50692.pyc
# Source Generated with Decompyle++
# File: p50692.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    if cl_condition.CheckOwnerDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenOwnerMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', 1)
    if cl_condition.CheckOwnerDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenOwnerMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((669,), (lambda a0: a0 * 0.5))), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50692
    m_Name = '50692'
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
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

