# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4208.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4208.pyc
# Source Generated with Decompyle++
# File: p4208.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO
from cl_newformula import Func304, Func516

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func516(*a, **{
'sid': 2510 }))) >= 1:
        cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': (lambda *a: Func304(*a, **{
'sAttr': 'Width' }) / 2 + 1) }, 0, 1, 2, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32392, 0, {
            'AttSpeedMul': (lambda *a: Func516(*a, **{
'sid': 2510 }) * 1000 + 1000),
            'TalentLevel': (lambda *a: Func516(*a, **{
'sid': 2510 })) }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32392, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4208
    m_Name = '召唤物屏障被动-高速运转'
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

