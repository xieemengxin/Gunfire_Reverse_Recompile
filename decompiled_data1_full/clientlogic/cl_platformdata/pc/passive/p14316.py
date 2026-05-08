# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14316.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14316.pyc
# Source Generated with Decompyle++
# File: p14316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PFAI_CATCH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32812, 'Div', 2, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32812, 'Radius', 45, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32812, 'ScaleX', 2.5, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32812, 'ScaleY', 2.5, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 32812, 'ScaleZ', 2.5, 1)
    cl_action.CommonDirectSetPFAIGroupWeight(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, {
        2003: 10,
        1003: 10 })


class CPerform(CCustomPerform):
    m_SID = 14316
    m_Name = '轮回10-精英河童'
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

