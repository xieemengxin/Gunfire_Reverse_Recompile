# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2302.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2302.pyc
# Source Generated with Decompyle++
# File: p2302.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32303, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32249, 0, {
        'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32250, 0, {
        'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32251, 0, {
        'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32006):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32249, 0, {
            'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32006):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32250, 0, {
            'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32006):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32251, 0, {
            'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 2302
    m_Name = '雷征天引'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 104

