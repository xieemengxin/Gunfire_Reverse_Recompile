# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3210.pyc
# Source Generated with Decompyle++
# File: p3210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func361, Func410, Func560, Func563

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_ALLGROOVE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32748) or cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32749) or cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32750):
        cl_evact.NextFrameTriggerGroup(oWarrior, oEventCB, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32748 }) + Func410(*a, **{
'sid': 32749 }) + Func410(*a, **{
'sid': 32750 }))) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 32899) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32899, 200, { }, 1, -1, None)
        cl_action.CommonFullQuality(oWarrior, oEventCB.GetCBLifeCycle())
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 4287,
'sArgs': 'CareerFlag' }))):
            cl_action.CommonClearAllGroove(oWarrior, oEventCB.GetCBLifeCycle(), 1)
        else:
            cl_action.CommonClearAllGroove(oWarrior, oEventCB.GetCBLifeCycle(), 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32753, 800, {
            'StateCount': (lambda *a: Func563(*a) * 20) }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32899):
        cl_evact.NextFrameTriggerGroup(oWarrior, oEventCB, 1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.NextFrameTriggerGroup(oWarrior, oEventCB, 1, None)


class CPerform(CCustomPerform):
    m_SID = 3210
    m_Name = '弃而不舍'
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
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 113

