# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4825.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4825.pyc
# Source Generated with Decompyle++
# File: p4825.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 4825
    m_Name = '关键延迟'
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
        'AttSpeed': (0, -1000, 0),
        'CrazyEff': (12000, 0, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((17, 18, 19, 1, 23), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

