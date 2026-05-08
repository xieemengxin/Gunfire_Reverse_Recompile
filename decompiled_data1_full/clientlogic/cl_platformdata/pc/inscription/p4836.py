# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4836.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4836.pyc
# Source Generated with Decompyle++
# File: p4836.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_UNHOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 20, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBFillSourceWeaponBullet(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 4836
    m_Name = '秘法弹药'
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
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((6, 10, 14), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_UNHOLD

