# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50705.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50705.pyc
# Source Generated with Decompyle++
# File: p50705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetMoveUsePerform(oWarrior, oLifeCycle, 7322)


class CPerform(CCustomPerform):
    m_SID = 50705
    m_Name = '#NT#流寇纵火者移动攻击技能'
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

