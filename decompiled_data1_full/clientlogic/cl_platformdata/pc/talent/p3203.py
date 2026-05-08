# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3203.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3203.pyc
# Source Generated with Decompyle++
# File: p3203.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeShield(oWarrior, oEventCB, 500)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeShield(oWarrior, oEventCB, 700)
    cl_action.CommonShieldRecover(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 3203
    m_Name = '星运庇佑'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 113

