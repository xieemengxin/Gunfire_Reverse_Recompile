# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4209.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4209.pyc
# Source Generated with Decompyle++
# File: p4209.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_MONSTER
from cl_newformula import Func304, Func521

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func521(*a, **{
'sid': 6056 }))) >= 1:
        cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': (lambda *a: Func304(*a, **{
'sAttr': 'Width' }) / 2 + 1) }, 0, 1, 2, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32403, 0, {
            'MoveSpeedMul': -3000 }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32403, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4209
    m_Name = '召唤物屏障被动-弱化能流'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

