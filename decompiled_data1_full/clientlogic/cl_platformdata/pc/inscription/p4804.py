# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4804.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4804.pyc
# Source Generated with Decompyle++
# File: p4804.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 4804
    m_Name = '精准射击'
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
        'Accuracy': (80, 0, 0),
        'Stability': (80, 0, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((12, 20, 23), (), (1505, 1510, 1213, 1214, 1415, 1401, 1404, 1406, 1407, 1408, 1409, 1801, 1211, 1416))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

