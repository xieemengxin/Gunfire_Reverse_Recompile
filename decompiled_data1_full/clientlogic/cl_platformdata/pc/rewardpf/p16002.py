# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16002.pyc
# Source Generated with Decompyle++
# File: p16002.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, 180)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, 60)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, 15)


class CPerform(CCustomPerform):
    m_SID = 16002
    m_Name = '弹药背包'
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

