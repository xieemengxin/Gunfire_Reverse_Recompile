# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13022.pyc
# Source Generated with Decompyle++
# File: p13022.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1427, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 13022
    m_Name = '不洁之力'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (1302, 1303, 1304, 1305, 1306, 1309, 1401, 1404, 1406, 1407, 1408, 1409, 1501, 1502, 1503, 1507, 1508, 1510, 1505, 1601, 1602, 1603), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

