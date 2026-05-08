# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13119.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13119.pyc
# Source Generated with Decompyle++
# File: p13119.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, '13119ExtraRadius', 4)
    cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, '13119ExtraAddState', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveSourceItemTmpData(oWarrior, oLifeCycle, '13119ExtraRadius')
    cl_action.CommonRemoveSourceItemTmpData(oWarrior, oLifeCycle, '13119ExtraAddState')


class CPerform(CCustomPerform):
    m_SID = 13119
    m_Name = '#NT#棱刺专属1'
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
    m_LimitList = ((), (1812, 1507), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

