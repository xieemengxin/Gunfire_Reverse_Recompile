# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p44002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p44002.pyc
# Source Generated with Decompyle++
# File: p44002.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 44002
    m_Name = '#NT#轮回10新陷阱被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'BossWeakTime': 300,
        'EliteWeakTime': 500,
        'NormalWeakTime': 1000,
        'DamAdd': 3000 }
    m_DieDisable = 0

