# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51266.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51266.pyc
# Source Generated with Decompyle++
# File: p51266.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_QUALITY_FOUR, ABILITY_TYPE_EXCLUSIVE
from cl_newformula import Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'FillTime', 0, -3000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxBullet', (lambda *a: (2 + Func749(*a) * 2) * 15 // 10), 0, 26, 999)


class CPerform(CCustomPerform):
    m_SID = 51266
    m_Name = '爆射令牌专属词条'
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
    m_QualityValue = {
        ABILITY_QUALITY_FOUR: 1 }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 1
    m_IsReverseFloting = 0

