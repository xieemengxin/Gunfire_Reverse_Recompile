# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5417.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5417.pyc
# Source Generated with Decompyle++
# File: p5417.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MAIN_HOLD
from cl_newformula import Func331, Func505, Func517, Func533

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: max(int(Func505(*a) * (25 + Func331(*a, **{
'sid': 5417 }) * 25) / 100 + 0), 1)), 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32694, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32694, (lambda *a: max(int((Func517(*a) + Func533(*a)) * (25 + Func331(*a, **{
'sid': 5417 }) * 25) / 100 + 0), 1)))
    else:
        cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: max(int(Func517(*a) * (25 + Func331(*a, **{
'sid': 5417 }) * 25) / 100 + 0), 1)), MAIN_HOLD)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32694, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32694, (lambda *a: max(int(Func517(*a) * (25 + Func331(*a, **{
'sid': 5417 }) * 25) / 100 + 0), 1)))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: max(int(Func505(*a) + 0), 1)), 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32685, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32685, (lambda *a: max(int(Func517(*a) + Func533(*a) + 0), 1)))
    else:
        cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: max(int(Func517(*a) + 0), 1)), MAIN_HOLD)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32685, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32685, (lambda *a: max(int(Func517(*a) + 0), 1)))


class CPerform(CCustomPerform):
    m_SID = 5417
    m_Name = '移花接木'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 109

