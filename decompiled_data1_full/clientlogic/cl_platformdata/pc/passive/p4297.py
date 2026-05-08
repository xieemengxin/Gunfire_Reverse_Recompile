# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4297.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4297.pyc
# Source Generated with Decompyle++
# File: p4297.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4297 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 2 }, 0, 1, 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.EventGetTargetBySummonOwner(oWarrior, oEventCB)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1711, None, { }, None)
        cl_evact.EventCBRemoveSummonBySummonOwner(oWarrior, oEventCB, 1062)


class CPerform(CCustomPerform):
    m_SID = 4297
    m_Name = '宝箱怪宝石被动'
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
    m_DieDisable = 1

