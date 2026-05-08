# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13095.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13095.pyc
# Source Generated with Decompyle++
# File: p13095.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_BOTH

class CPerform(CCustomPerform):
    m_SID = 13095
    m_Name = '#聚能法杖2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = {
        'Trajectory': (0, 30000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1704,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

