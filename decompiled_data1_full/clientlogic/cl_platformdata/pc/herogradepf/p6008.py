# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6008.pyc
# Source Generated with Decompyle++
# File: p6008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1410, 'Radius', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8001, 'Radius', 4000, 0)


class CPerform(CCustomPerform):
    m_SID = 6008
    m_Name = '源力法师lv.3'
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

