# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3212.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3212.pyc
# Source Generated with Decompyle++
# File: p3212.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3212 as CustomAction
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_ALLGROOVE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_ALLGROOVE, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_ALLGROOVE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 0, {
            'StateCount': 30 }, 1, -1, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 0, {
            'StateCount': 20 }, 1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1 or cl_evcon.GetComb(oWarrior, oEventCB) == 2:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 0, {
            'StateCount': 50 }, 1, -1, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 0, {
            'StateCount': 35 }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) >= 4:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 50, {
            'StateCount': 50 }, 1, -1, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32752, 0, {
            'StateCount': 70 }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 3212
    m_Name = '神秘启示'
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
    m_Career = 113

