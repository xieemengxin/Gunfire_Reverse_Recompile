# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4200.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4200.pyc
# Source Generated with Decompyle++
# File: p4200.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 10, 0, 0)
    cl_action.CommonSetSkillCheckArgs(oWarrior, oLifeCycle, 1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 5 }, 0.2, 1, 2, 1)
    cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 7 }, 0.2, 4, 5, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'dam', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'dam') + 1)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 7970) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'dam'):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 7970, 0)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 0, 500, 3)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'dam', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'dam') - 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 7970) == 0 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('dam') >= 1:
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_HERO, 1, 0, 0, 0, 0, { }, None, None, None, None, None)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
            39214: 0 })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'det', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'det') + 1)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'det', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'det') - 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('det') <= 0 and cl_evcon.CBCheckCastingSkill(oWarrior, oEventCB, 39214) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7970, 0, { }, 0, 0, None)


def DoCallBackAction10(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('det') <= 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7970, 0, { }, 0, 0, None)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('dam') >= 1:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 500, 3)


class CPerform(CCustomPerform):
    m_SID = 4200
    m_Name = '小触手被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0

