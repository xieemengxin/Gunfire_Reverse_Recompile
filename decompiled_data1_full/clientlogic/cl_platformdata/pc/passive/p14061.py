# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14061.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14061.pyc
# Source Generated with Decompyle++
# File: p14061.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22852, 'TrowBall', 3, 1)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 22853)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4351, 'Reincarnation9', 1, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22851, 'BuildCount', 15, 1)


class CPerform(CCustomPerform):
    m_SID = 14061
    m_Name = '轮回9-虚空僧增加法球'
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

