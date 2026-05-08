# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13505.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13505.pyc
# Source Generated with Decompyle++
# File: p13505.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO, WARRIOR_MONSTER
from cl_newformula import Func303

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8001, 'Radius', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8001, 'KeepTime', 0, 500)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1410, 'Radius', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1410, 'KeepTime', 0, 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1410: 1,
        8001: 1 }, 1, 0):
        cl_evact.PassiveSetPosToSkillCollect(oWarrior, oEventCB, 'EndPos')
        cl_evact.EventCBAddSceneEventForState(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'KeepTime' })), SCENE_EVT_SHAPE_SPHERE, {
            'Radius': (lambda *a: Func303(*a, **{
'sAttr': 'Radius' })) }, 0, 1357, 0, 1, WARRIOR_HERO, -1)
        cl_evact.EventCBAddSceneEventForState(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'KeepTime' })), SCENE_EVT_SHAPE_SPHERE, {
            'Radius': (lambda *a: Func303(*a, **{
'sAttr': 'Radius' })) }, 0, 32973, 0, 1, WARRIOR_MONSTER, -1)


class CPerform(CCustomPerform):
    m_SID = 13505
    m_Name = '烟雾弥漫'
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
    m_Career = 102

