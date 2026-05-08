# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13059.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13059.pyc
# Source Generated with Decompyle++
# File: p13059.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11123, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveDisableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11123)
        cl_action.PassiveEnableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11126, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveDisableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11126)
        cl_action.PassiveEnableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11123, 1)


class CPerform(CCustomPerform):
    m_SID = 13059
    m_Name = '八爪鱼'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1312,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

