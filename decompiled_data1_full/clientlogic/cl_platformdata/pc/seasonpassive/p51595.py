# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51595.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51595.pyc
# Source Generated with Decompyle++
# File: p51595.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_VICTIM, PF_SUBMSG_COMMON, SCENE_EVT_SHAPE_SPHERE
from cl_newformula import Func651, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSpeed', 1000)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 1000, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 6, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSpeed', 1500)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 1500, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 6, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSpeed', 2000)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 6, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSpeed', 3000)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1991, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveSetPosToTargetPos(oWarrior, oEventCB)
        if cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'EPFPos', 0):
            cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 300, SCENE_EVT_SHAPE_SPHERE, {
                'Radius': cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'Radius') }, 0, 1, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, '51595InFireCycle', 1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33952, 304, {
            'MoveSpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'AddSpeed' })) }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB) and cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33952, 0, 0, 0, 0):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, '51595InFireCycle', 0)
        cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33952, 300, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1991, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveSetPosToTargetPos(oWarrior, oEventCB)
        if cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'EPFPos', 0):
            cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 300, SCENE_EVT_SHAPE_SPHERE, {
                'Radius': cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'Radius') }, 0, 4, 2)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, '51595InFireCycle', 1)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33952, 304, {
            'MoveSpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'AddSpeed' })) }, 1)
        if cl_evcon.EventCBGetLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Event' })), 300) == 0:
            cl_evact.EventCBRecordLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Event' })), 1)
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 0, 100)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBGetLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Event' })), 300) == 0:
        cl_evact.EventCBRecordLimitedTimeInfo(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Event' })), 1)
        cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 0, 100)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evact.EventCBGetCustomData(oWarrior, oEventCB, '51595InFireCycle'):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, '51595InFireCycle', 0)
        cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33952, 300, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'EPFPos', 0):
        cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 300, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'Radius') }, 0, 1, 2)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'EPFPos', 0):
        cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 300, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'Radius') }, 0, 4, 2)


class CPerform(CCustomPerform):
    m_SID = 51595
    m_Name = '#NT#流星-E'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0

