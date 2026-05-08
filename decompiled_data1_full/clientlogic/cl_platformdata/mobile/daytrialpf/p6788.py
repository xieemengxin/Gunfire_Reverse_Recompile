# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6788.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6788.pyc
# Source Generated with Decompyle++
# File: p6788.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_newformula import Func220

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'FireAbnormalFactor', 0, (lambda *a: (80 - Func220(*a)) * 100 // 70), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ThunderAbnormalFactor', 0, (lambda *a: (80 - Func220(*a)) * 100 // 70), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'CorrisionAbnormalFactor', 0, (lambda *a: (80 - Func220(*a)) * 100 // 70), 0)


class CPerform(CCustomPerform):
    m_SID = 6788
    m_Name = '对怪物造成的元素异常效果增强'
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

