# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/weaponenhance/p13802.pyc
# RelativePath: clientlogic/cl_perform/weaponenhance/p13802.pyc
# Source Generated with Decompyle++
# File: p13802.pyc (Python 3.6)

from __future__ import absolute_import
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.weaponenhance import CWeaponEnhance as CCustomPerform
from cl_commondefines import ITEMPERFORM_ENABLE_HOLD

class CPerform(CCustomPerform):
    m_SID = 13802
    m_Name = '扩容'
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
        'MaxBullet': (4000, 6000, 0, 0) }
    m_LimitList = ((), ())
    m_ExcludeList = ((10,), (), (1202, 1212, 1509, 1512, 1601, 1505, 1510))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

