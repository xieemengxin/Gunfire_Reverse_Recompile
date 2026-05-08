# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3604.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3604.pyc
# Source Generated with Decompyle++
# File: p3604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func3, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREADISAPPEAR_DUMP, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREADISAPPEAR_DUMP, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREADISAPPEAR_DUMP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '3604_Level', cl_evact.EventCBGetEventInkAreaSquare(oWarrior, oEventCB))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }))) >= 100:
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }) // 100), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '3604_Level', (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' })),
'b': 100 })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '3604_Level', cl_evact.EventCBGetEventInkAreaSquare(oWarrior, oEventCB))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }))) >= 80:
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }) // 80), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '3604_Level', (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' })),
'b': 80 })))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '3604_Level', cl_evact.EventCBGetEventInkAreaSquare(oWarrior, oEventCB))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }))) >= 60:
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' }) // 60), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '3604_Level', (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 3604,
'sArgs': '3604_Level' })),
'b': 60 })))


class CPerform(CCustomPerform):
    m_SID = 3604
    m_Name = '墨迹再生'
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

