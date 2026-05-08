# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4345.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4345.pyc
# Source Generated with Decompyle++
# File: p4345.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'MaxCover', 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'MaxCover', 0, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'ColdTime', 0, -500)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'MaxCover', 0, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7151, 'ColdTime', 0, -1000)


class CPerform(CCustomPerform):
    m_SID = 4345
    m_Name = '御灵师仆从Q4'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

