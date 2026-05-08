# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14030.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14030.pyc
# Source Generated with Decompyle++
# File: p14030.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PFAI_CATCH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 20831, 'ColdTime', -5000, 0)
    cl_action.CommonSetPFAIGroupWeightByType(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, 20831, 95)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 5000, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 14030
    m_Name = '轮回9-魔化右矛兵'
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

