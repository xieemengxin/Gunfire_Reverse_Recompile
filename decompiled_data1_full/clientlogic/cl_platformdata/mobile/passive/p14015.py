# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14015.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14015.pyc
# Source Generated with Decompyle++
# File: p14015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func367

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetMonsterAIPFGroupCnt(oWarrior, oLifeCycle, 1001, 22024, 65, 80)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AccuracyProb', 0, (lambda *a: 100 - Func367(*a, **{
'sAttr': 'AccuracyProb' })), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 5000, 0, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 5000, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 14015
    m_Name = '轮回9-运载八腕目'
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

