# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4141.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4141.pyc
# Source Generated with Decompyle++
# File: p4141.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSubPointPerformColdTime(oWarrior, oLifeCycle, 32822, 0, 100)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 32822, 'ColdTime', -2000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 32821, 'ColdTime', -3000, 0)


class CPerform(CCustomPerform):
    m_SID = 4141
    m_Name = '三幕精英虚妄僧-阶段4'
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

