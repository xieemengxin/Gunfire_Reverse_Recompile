# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6068.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6068.pyc
# Source Generated with Decompyle++
# File: p6068.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'EnergyMax', 0, 6000, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32463, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6068
    m_Name = '妖星lv.3'
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

