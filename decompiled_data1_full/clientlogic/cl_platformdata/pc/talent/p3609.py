# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3609.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3609.pyc
# Source Generated with Decompyle++
# File: p3609.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PICK_INKBEAD, PICK_SPECIALINKBEAD
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 0, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1325, 'DamReduceRatio', 1000, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'AddRatio', 2500, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'StateTime', 1200, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'MaxCount', 3, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 0, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1325, 'DamReduceRatio', 2000, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'AddRatio', 4000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'StateTime', 1200, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'MaxCount', 3, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 0, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1325, 'DamReduceRatio', 3000, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'AddRatio', 4000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'StateTime', 2000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3609, 'MaxCount', 4, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33091):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33091, (lambda *a: max(Func361(*a, **{
'sid': 3611,
'sArgs': 'Times' }), 1)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
        cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33091, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), 0)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33091, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), { }, 1)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33091, (lambda *a: max(Func361(*a, **{
'sid': 3611,
'sArgs': 'Times' }), 1)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
        cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33091, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), 0)


class CPerform(CCustomPerform):
    m_SID = 3609
    m_Name = '斑斓浊色'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 117

