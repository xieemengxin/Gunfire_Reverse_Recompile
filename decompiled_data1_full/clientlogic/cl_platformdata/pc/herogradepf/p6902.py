# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6902.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6902.pyc
# Source Generated with Decompyle++
# File: p6902.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8009, 'Att', 0, 10000)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32911, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6902
    m_Name = '召唤师lv.2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

