# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4085.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4085.pyc
# Source Generated with Decompyle++
# File: p4085.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonAttentionOwnerRoomGoalCallBack(oWarrior, oLifeCycle, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1622, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, 999999, DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, None, None, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4085
    m_Name = '【第三幕】孵化物召唤一刀怪'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

