# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2909.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2909.pyc
# Source Generated with Decompyle++
# File: p2909.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func309, Func331

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1427, 1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 3000 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1427, 1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 5000 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1427, 1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 7000 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func309(*a))) == 1:
        cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, 1)
    else:
        cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, (lambda *a: Func309(*a) * (Func331(*a, **{
'sid': 2909 }) - 1) * 50 / 100))


class CPerform(CCustomPerform):
    m_SID = 2909
    m_Name = '暗潮涌动'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 110

