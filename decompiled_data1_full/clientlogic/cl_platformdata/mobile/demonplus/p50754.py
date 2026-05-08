# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/demonplus/p50754.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/demonplus/p50754.pyc
# Source Generated with Decompyle++
# File: p50754.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.demonplus import CDemonPlus as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 15000, 0, 0)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ArmorMax', 30000)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ShieldMax', 30000)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'HPMax', 30000)


class CPerform(CCustomPerform):
    m_SID = 50754
    m_Name = '精锐妖兵'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_WeakDisable = 0

