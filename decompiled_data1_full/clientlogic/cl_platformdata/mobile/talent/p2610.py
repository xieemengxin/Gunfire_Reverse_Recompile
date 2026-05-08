# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2610.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2610.pyc
# Source Generated with Decompyle++
# File: p2610.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ContHitKeepTime', 1000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ContHitKeepTime', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33827) >= 20 or oWarrior.Energy() >= 3000:
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 25)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'ExplodeDelay', 0, 25)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_ENERGY, -1)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33827) < 20 and oWarrior.Energy() < 3000:
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'ExplodeDelay', 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 0, 0, 0)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COST_ENERGY, -1)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1)


class CPerform(CCustomPerform):
    m_SID = 2610
    m_Name = '#NT#觉醒占位'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 121

