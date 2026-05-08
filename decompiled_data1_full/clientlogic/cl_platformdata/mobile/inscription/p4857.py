# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4857.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4857.pyc
# Source Generated with Decompyle++
# File: p4857.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 4857
    m_Name = '精准爆破'
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
        'Radius': (0, -2000, 0),
        'FillTime': (0, -4000, 0),
        'AttSpeed': (0, 4000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((2,), (), ())
    m_ExcludeList = ((9,), (4859, 4852, 4806), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

