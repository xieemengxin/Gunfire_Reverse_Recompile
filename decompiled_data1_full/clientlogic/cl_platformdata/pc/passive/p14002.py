# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14002.pyc
# Source Generated with Decompyle++
# File: p14002.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMonsterPerformGroupAttr(oWarrior, oLifeCycle, {
        22832: 1,
        22836: 1,
        22837: 1 }, 'ColdTime', -5000, 0)


class CPerform(CCustomPerform):
    m_SID = 14002
    m_Name = '轮回9-虚无僧'
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

