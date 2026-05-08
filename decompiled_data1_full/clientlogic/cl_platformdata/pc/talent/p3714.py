# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3714.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3714.pyc
# Source Generated with Decompyle++
# File: p3714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func517

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtRecoveryEnergy', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, '3714ColdTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HitCountMax', (lambda *a: Func517(*a) * 3 // 4))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtRecoveryEnergy', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HitCountMax', (lambda *a: Func517(*a) * 3 // 4))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, '3714ColdTime', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5327, 'RepeatHitExtEnergy', 100, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtRecoveryEnergy', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HitCountMax', (lambda *a: Func517(*a) // 2))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, '3714ColdTime', 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitCount', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitCount') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitCountMax') and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, '3714ColdTime'))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCount', 0)
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtRecoveryEnergy'), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCountMax', (lambda *a: Func517(*a) * 3 // 4))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCountMax', (lambda *a: Func517(*a) // 2))


class CPerform(CCustomPerform):
    m_SID = 3714
    m_Name = '贯气通元'
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
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 118

