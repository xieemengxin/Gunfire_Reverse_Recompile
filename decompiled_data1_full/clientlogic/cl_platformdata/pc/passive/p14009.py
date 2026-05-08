# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14009.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14009.pyc
# Source Generated with Decompyle++
# File: p14009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 20213, 'ColdTime', -5000, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 20213, 'BackSwing', 50, None)


class CPerform(CCustomPerform):
    m_SID = 14009
    m_Name = '轮回9-大漠土狼'
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

