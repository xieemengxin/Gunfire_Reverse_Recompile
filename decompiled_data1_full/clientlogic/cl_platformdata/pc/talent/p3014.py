# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3014.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3014.pyc
# Source Generated with Decompyle++
# File: p3014.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDisableSealedInscription(oWarrior, oLifeCycle, cl_action.CommonGetTalentLevel(oWarrior, oLifeCycle, 3014))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDisableSealedInscription(oWarrior, oLifeCycle, cl_action.CommonGetTalentLevel(oWarrior, oLifeCycle, 3014))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDisableSealedInscription(oWarrior, oLifeCycle, cl_action.CommonGetTalentLevel(oWarrior, oLifeCycle, 3014))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'StateSID') == 33639:
        if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33639):
            cl_action.CommonEnableSealedInscription(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3014))
        else:
            cl_action.CommonDisableSealedInscription(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3014))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33639):
        cl_action.CommonEnableSealedInscription(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3014))
    else:
        cl_action.CommonDisableSealedInscription(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3014))


class CPerform(CCustomPerform):
    m_SID = 3014
    m_Name = '上古蚀刻'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 111

