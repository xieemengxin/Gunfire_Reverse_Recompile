# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/demonplus/p50757.pyc
# RelativePath: clientlogic/cl_platformdata/pc/demonplus/p50757.pyc
# Source Generated with Decompyle++
# File: p50757.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.demonplus import CDemonPlus as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveChangeConquerProbability(oWarrior, oLifeCycle, -5000)


class CPerform(CCustomPerform):
    m_SID = 50757
    m_Name = '桀骜不驯'
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

