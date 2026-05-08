# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4118.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4118.pyc
# Source Generated with Decompyle++
# File: p4118.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 2 }, 0, 1, 2, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7090, 0, { }, 1, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1044, None, None, None)
    if cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1029):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1009, 0)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, 999999, DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, None, None, None, None, None, None, None, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, 999999, DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, None, None, None, None, None, None, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 7090, 0, 0, None):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 7090, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4118
    m_Name = '风神气旋被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (4207,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

