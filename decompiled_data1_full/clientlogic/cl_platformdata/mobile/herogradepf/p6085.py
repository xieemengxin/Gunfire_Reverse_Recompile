# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6085.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6085.pyc
# Source Generated with Decompyle++
# File: p6085.pyc (Python 3.6)

from cl_only import Functor, Time2Frame
from cl_commondefines import TYPE_RELIFE_PF, STATE_TIME_LIMIT
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
import cl_state
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32690, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6085
    m_Name = '噬魂剑客lv.5'
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

