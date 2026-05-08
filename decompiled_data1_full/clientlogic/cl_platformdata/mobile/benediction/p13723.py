# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13723.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13723.pyc
# Source Generated with Decompyle++
# File: p13723.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.benediction.customaction import CustomAction13723 as CustomAction
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        'RewardLevel': 2,
        'ChooseList': '15013|15015|15016|15043|15044|15045|15046|15047|15048|15049|15050|15018',
        'Num': 3 })


class CPerform(CCustomPerform):
    m_SID = 13723
    m_Name = '锦囊玉轴'
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
    m_Career = None

