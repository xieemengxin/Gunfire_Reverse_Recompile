# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p40041.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p40041.pyc
# Source Generated with Decompyle++
# File: p40041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32937):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32937, 10, None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32937, 0, {
            'StateCount': 10 }, 0)


def DisableAction1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 32937 }))) <= 10:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32937, 0)
    else:
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32937, -10, None)


class CPerform(CCustomPerform):
    m_SID = 40041
    m_Name = '天降大任-迅捷如风1特殊效果'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

