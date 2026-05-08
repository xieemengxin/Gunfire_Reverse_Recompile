# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5035.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5035.pyc
# Source Generated with Decompyle++
# File: p5035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func3, Func361, Func385, Func407, Func638

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5035, 'NoCheck33044', 1, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, -1, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33040, (lambda *a: 25 * (100 + Func361(*a, **{
'sid': 3613,
'sArgs': 'ExtraBuff' })) // 100), None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetEventWeaponPerformPFBulletCount(oWarrior, oEventCB) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func385(*a))):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '5035Cost', (lambda *a: Func385(*a) * 2))
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '5035Cost', (lambda *a: Func385(*a) + cl_evcon.GetEventWeaponPerformPFBulletCount(oWarrior, oEventCB)))
    cl_evact.EventCBCostEventWeaponPFBullet(oWarrior, oEventCB, (lambda *a: Func385(*a)))
    cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 33044, (lambda *a: Func407(*a, **{
'sid': 33044 }) * 5 // 100), (lambda *a: Func407(*a, **{
'sid': 33044 })))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5035,
'sArgs': '5035Cost' }))) >= 5000:
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33303):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33303, (lambda *a: Func361(*a, **{
'sid': 5035,
'sArgs': '5035Cost' }) // 5000), 800)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33303, 800, {
                'StateCount': (lambda *a: Func361(*a, **{
'sid': 5035,
'sArgs': '5035Cost' }) // 5000) }, 1, 1, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '5035Cost', (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 5035,
'sArgs': '5035Cost' })),
'b': 5000 })))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraBuff', (lambda *a: min((Func638(*a) // 10) * 20, 100)))
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33040, (lambda *a: 25 * (100 + Func361(*a, **{
'sid': 3613,
'sArgs': 'ExtraBuff' }) + Func361(*a, **{
'sid': 5035,
'sArgs': 'ExtraBuff' })) // 100))


class CPerform(CCustomPerform):
    m_SID = 5035
    m_Name = '素墨清韵'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 117

