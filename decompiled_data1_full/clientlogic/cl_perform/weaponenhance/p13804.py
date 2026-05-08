# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/weaponenhance/p13804.pyc
# RelativePath: clientlogic/cl_perform/weaponenhance/p13804.pyc
# Source Generated with Decompyle++
# File: p13804.pyc (Python 3.6)

from __future__ import absolute_import
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.weaponenhance import CWeaponEnhance as CCustomPerform
from cl_commondefines import ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 13804
    m_Name = '神速'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_EnhanceAttr = {
        'AttSpeed': (2000, 3000, 0, 0) }
    m_LimitList = ((), ())
    m_ExcludeList = ((), (), (1202, 1306, 1503, 1505, 1510, 1404, 1401, 1406, 1407, 1408, 1302, 1602, 1603, 1601, 1504, 1415))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

