# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4210.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4210.pyc
# Source Generated with Decompyle++
# File: p4210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_only import PY_FLAG_DEAD
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO
from cl_newformula import Func304, Func516, Func519

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func516(*a, **{
'sid': 2511 }))) >= 1:
        cl_evact.EventCBAddSceneEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': (lambda *a: Func304(*a, **{
'sAttr': 'Width' }) / 2 + 1) }, 0, 1, 2, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32393, 0, {
            'TalentAffection': (lambda *a: Func519(*a, **{
'sid': 32394 })) }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32393, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4210
    m_Name = '召唤物屏障被动-高压运转'
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

