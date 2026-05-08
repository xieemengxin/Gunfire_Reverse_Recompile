# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13107.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13107.pyc
# Source Generated with Decompyle++
# File: p13107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 5322, 'RewardMinNum', 2)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 5322, 'RewardMinNum', 0)


class CPerform(CCustomPerform):
    m_SID = 13107
    m_Name = '老虎机专属一'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1314,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

