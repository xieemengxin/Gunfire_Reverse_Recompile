# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5036.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5036.pyc
# Source Generated with Decompyle++
# File: p5036.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ALL_INKAREA, DOUBLESPHERE_INKAREA, SHIELD_RADIO_ADD, SHIELD_RADIO_SUB, SPHERE_INKAREA
from cl_newformula import Func304, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33306, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INKAREASQUARERECORD_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 1, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, SHIELD_RADIO_ADD, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, SHIELD_RADIO_SUB, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromAll', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), ALL_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), SPHERE_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromDoubleSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), DOUBLESPHERE_INKAREA))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33306, (lambda *a: 100 * (100 + (Func361(*a, **{
'sid': 5036,
'sArgs': 'FromAll' }) - (Func361(*a, **{
'sid': 5036,
'sArgs': 'FromSphere' }) + Func361(*a, **{
'sid': 5036,
'sArgs': 'FromDoubleSphere' })) * 5 // 10) // 4) // 100))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'Shield' }) / Func304(*a, **{
'sAttr': 'ShieldMax' })) * 100)) >= 50:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33307, 0, { }, 1, 0, 0)
    else:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33307)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33307, 0, { }, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33307)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromAll', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), ALL_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), SPHERE_INKAREA))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FromDoubleSphere', cl_action.CommonGetCurInkAreaSquareByType(oWarrior, oEventCB.GetCBLifeCycle(), DOUBLESPHERE_INKAREA))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33306, (lambda *a: 100 * (100 + (Func361(*a, **{
'sid': 5036,
'sArgs': 'FromAll' }) - (Func361(*a, **{
'sid': 5036,
'sArgs': 'FromSphere' }) + Func361(*a, **{
'sid': 5036,
'sArgs': 'FromDoubleSphere' })) * 5 // 10) // 4) // 100))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'Shield' }) / Func304(*a, **{
'sAttr': 'ShieldMax' })) * 100)) >= 50:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33307, 0, { }, 1, 0, 0)
    else:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33307)


class CPerform(CCustomPerform):
    m_SID = 5036
    m_Name = '激浊扬清'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 1
    m_Career = 117

