# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4816.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4816.pyc
# Source Generated with Decompyle++
# File: p4816.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 4816
    m_Name = '穿甲弹药'
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
        'Pierce': (1, 0, 0),
        'BulletSpeed': (0, 10000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (1008, 1205, 1002, 1003, 1010, 1004, 1006, 1209, 1303, 1304, 1212, 1201, 1213, 1509, 1007, 1016), ())
    m_ExcludeList = ((), (4894,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

