# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6122.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6122.pyc
# Source Generated with Decompyle++
# File: p6122.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_SEASONWAND

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 700, 700, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1743, { }, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 6122
    m_Name = '飞剑'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (1743,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_SEASONWAND

