# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6609.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6609.pyc
# Source Generated with Decompyle++
# File: p6609.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'rwpf6609' }))):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'rwpf6609', 1)
        cl_action.CommonAddBlankRelic(oWarrior, oLifeCycle, 2)


class CPerform(CCustomPerform):
    m_SID = 6609
    m_Name = '赛季4天赋1011'
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

