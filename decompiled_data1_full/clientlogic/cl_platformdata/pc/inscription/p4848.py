# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4848.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4848.pyc
# Source Generated with Decompyle++
# File: p4848.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 4848
    m_Name = '弹道数'
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
        'Trajectory': (0, 2000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((7, 12, 19, 20), (), (1215, 1501, 1502, 1503, 1505, 1507, 1510, 1513, 1211, 1416))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

