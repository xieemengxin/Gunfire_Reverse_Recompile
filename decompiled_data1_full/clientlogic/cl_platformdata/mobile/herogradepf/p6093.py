# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6093.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6093.pyc
# Source Generated with Decompyle++
# File: p6093.pyc (Python 3.6)

from cl_only import ChooseKey, ShufferList
from cl_object.logging import WartalentLog
from cl_npc.net import GS2CRandomChoose
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32895, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6093
    m_Name = '赌侠lv.3'
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

