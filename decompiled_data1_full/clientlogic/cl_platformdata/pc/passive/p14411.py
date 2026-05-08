# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14411.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14411.pyc
# Source Generated with Decompyle++
# File: p14411.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 30013)
    cl_action.CommonReplaceMonsterAIPF(oWarrior, oLifeCycle, 30011, 30013, 0)


class CPerform(CCustomPerform):
    m_SID = 14411
    m_Name = '轮回10-精英独角金龟'
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

