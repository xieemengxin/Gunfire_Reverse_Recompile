# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15054.pyc
# Source Generated with Decompyle++
# File: p15054.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1410, 'DamInterval', -2500, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8001, 'DamInterval', -2500, 0)


class CPerform(CCustomPerform):
    m_SID = 15054
    m_Name = '迷雾重重'
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

