# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15077.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15077.pyc
# Source Generated with Decompyle++
# File: p15077.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'SaveTime', -2000, 0, None)


class CPerform(CCustomPerform):
    m_SID = 15077
    m_Name = '但行好事'
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

