# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15034.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15034.pyc
# Source Generated with Decompyle++
# File: p15034.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1420, 'Att', 6000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1421, 'Att', 6000, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 3)


class CPerform(CCustomPerform):
    m_SID = 15034
    m_Name = '怒海神拳'
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

