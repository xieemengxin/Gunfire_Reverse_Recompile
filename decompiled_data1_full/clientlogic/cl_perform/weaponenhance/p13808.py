# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/weaponenhance/p13808.pyc
# RelativePath: clientlogic/cl_perform/weaponenhance/p13808.pyc
# Source Generated with Decompyle++
# File: p13808.pyc (Python 3.6)

from __future__ import absolute_import
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.weaponenhance import CWeaponEnhance as CCustomPerform
from cl_commondefines import ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 13808
    m_Name = '元素'
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
        'DebuffProb': (6000, 8000, 0, 0) }
    m_LimitList = ((4,), ())
    m_ExcludeList = ((), (), (1202,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

