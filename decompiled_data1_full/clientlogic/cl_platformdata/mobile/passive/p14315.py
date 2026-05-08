# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14315.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14315.pyc
# Source Generated with Decompyle++
# File: p14315.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 31264, 'MaxNum', 18, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 31264, 'MinNum', 14, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 31264, 'PosNum', 30, None)
    cl_action.ConmonReplaceMonsterPFAI(oWarrior, oLifeCycle, 31262)


class CPerform(CCustomPerform):
    m_SID = 14315
    m_Name = '轮回10-精英巡海夜叉'
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

