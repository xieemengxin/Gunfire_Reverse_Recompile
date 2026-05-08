# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6787.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6787.pyc
# Source Generated with Decompyle++
# File: p6787.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetTalentChooseTimes(oWarrior, oLifeCycle, 1, -600)


class CPerform(CCustomPerform):
    m_SID = 6787
    m_Name = '获得600铜币来刷新一次金爵'
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

