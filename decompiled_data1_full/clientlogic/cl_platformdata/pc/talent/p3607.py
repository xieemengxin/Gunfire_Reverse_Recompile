# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3607.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3607.pyc
# Source Generated with Decompyle++
# File: p3607.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3607 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeInkPerformAttr(oWarrior, oLifeCycle, 'Att', 20000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeInkPerformAttr(oWarrior, oLifeCycle, 'Att', 40000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeInkPerformAttr(oWarrior, oLifeCycle, 'Att', 60000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        CustomAction(oWarrior, oEventCB, {
            'Max': 1,
            'Buff': 10000,
            'StateSID': 33110 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33110):
        CustomAction(oWarrior, oEventCB, {
            'Buff': 10000,
            'StateSID': 33110,
            'MonsterDie': 1,
            'CheckDis': 40 })


class CPerform(CCustomPerform):
    m_SID = 3607
    m_Name = '墨潮奔涌'
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
    m_Career = 117

