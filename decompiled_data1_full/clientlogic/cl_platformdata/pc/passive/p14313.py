# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14313.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14313.pyc
# Source Generated with Decompyle++
# File: p14313.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 32425)
    cl_action.CommonReplaceMonsterAIPF(oWarrior, oLifeCycle, 32424, 32425, 1)


class CPerform(CCustomPerform):
    m_SID = 14313
    m_Name = '轮回10-精英沙蜥'
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

