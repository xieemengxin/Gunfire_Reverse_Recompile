# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3209.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3209.pyc
# Source Generated with Decompyle++
# File: p3209.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, PF_SUBMSG_CAREERPF
from cl_newformula import Func563, Func564

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32762, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32762, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 6, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32762, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') <= cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 0):
        if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') == cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 2000), 3000, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 2000), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') <= cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 0):
        if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') == cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 3000), 6000, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 3000), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') <= cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 0):
        if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32762, 'LastComb') == cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 4000), 10000, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func563(*a) * 4000), 0, 0, '')


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 0, 0):
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: Func564(*a)), 32762, 'LastComb')


class CPerform(CCustomPerform):
    m_SID = 3209
    m_Name = '无尽星空'
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
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 113

