# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6901.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6901.pyc
# Source Generated with Decompyle++
# File: p6901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, 3000, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 4338, (lambda *a: Func308(*a)))


class CPerform(CCustomPerform):
    m_SID = 6901
    m_Name = '召唤师lv.1'
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

