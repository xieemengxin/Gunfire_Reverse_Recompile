# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14407.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14407.pyc
# Source Generated with Decompyle++
# File: p14407.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39212, 'RangeAdd', 20, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39216, 'RangeAdd', 20, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39211, 'BackSwingAdd', -72, None)


class CPerform(CCustomPerform):
    m_SID = 14407
    m_Name = '轮回9-虬蛇触手'
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

