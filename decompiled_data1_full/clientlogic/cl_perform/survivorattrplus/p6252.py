# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivorattrplus/p6252.pyc
# RelativePath: clientlogic/cl_perform/survivorattrplus/p6252.pyc
# Source Generated with Decompyle++
# File: p6252.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivorattrplus import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 30000, 0, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 2000, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6252
    m_Name = '铁甲'
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

