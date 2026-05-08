# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6157.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6157.pyc
# Source Generated with Decompyle++
# File: p6157.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_IMMORTAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7951, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6157
    m_Name = '不朽的'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_IMMORTAL

