# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6088.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6088.pyc
# Source Generated with Decompyle++
# File: p6088.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1423, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8007, 'Att', 0, 10000)


class CPerform(CCustomPerform):
    m_SID = 6088
    m_Name = '虞火lv.3'
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

