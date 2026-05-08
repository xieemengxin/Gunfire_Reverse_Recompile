# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attrplus/p6202.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attrplus/p6202.pyc
# Source Generated with Decompyle++
# File: p6202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.attrplus import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 10000, 0, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 10000, 0, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 10000, 0, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', -2000, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6202
    m_Name = '#NT#铁甲'
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

