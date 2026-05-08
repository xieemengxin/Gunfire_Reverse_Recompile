# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4053.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4053.pyc
# Source Generated with Decompyle++
# File: p4053.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_FRIEND_HERO, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 22222, 0, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 22223, 0, None):
        cl_evact.PassiveSetPosToCartoon(oWarrior, oEventCB)
        cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 500, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 5 }, 0, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_FRIEND_HERO) == 0:
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 800, {
            'AbnormalSourceDam': 1000 }, 0, DAM_MASK_ELEMENT, None)


class CPerform(CCustomPerform):
    m_SID = 4053
    m_Name = '火系自爆范围持续伤害'
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

