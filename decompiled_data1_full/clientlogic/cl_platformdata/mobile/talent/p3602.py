# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3602.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3602.pyc
# Source Generated with Decompyle++
# File: p3602.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ALL_INKAREA, ATTACKERSUBMSG_NORMAL, DOUBLESPHERE_INKAREA, OBJ_ATTACK, SPHERE_INKAREA
from cl_newformula import Func308, Func361, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33149, 0, {
        'MaxCount': 500 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREASQUARERECORD_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33149, 0, {
        'MaxCount': 750 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREASQUARERECORD_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33149, 0, {
        'MaxCount': 1000 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREASQUARERECORD_CHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'From1431', cl_action.CommonGetCurInkAreaSquareFromThrow(oWarrior, oEventCB.GetCBLifeCycle()))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33149, (lambda *a: (Func361(*a, **{
'sid': 3602,
'sArgs': 'From1431' }) // 8) * (Func308(*a) * 2 + 4)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromAll', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), ALL_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), SPHERE_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromDoubleSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), DOUBLESPHERE_INKAREA))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33149, (lambda *a: ((Func361(*a, **{
'sid': 3602,
'sArgs': 'FromAll' }) - (Func361(*a, **{
'sid': 3602,
'sArgs': 'FromSphere' }) + Func361(*a, **{
'sid': 3602,
'sArgs': 'FromDoubleSphere' })) * 5 // 10) // 8) * 10))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1431: 1,
        12030: 1 }, 1, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func410(*a, **{
'sid': 33149 }) * 100), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3602
    m_Name = '聚墨齐挥'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 117

