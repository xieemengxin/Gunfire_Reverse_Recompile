# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4180.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4180.pyc
# Source Generated with Decompyle++
# File: p4180.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1500, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7955, 0, { }, 1, 0, None)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 2500)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ModelRadius', 0, 2500)


class CPerform(CCustomPerform):
    m_SID = 4180
    m_Name = '龙卷风属性变化被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

