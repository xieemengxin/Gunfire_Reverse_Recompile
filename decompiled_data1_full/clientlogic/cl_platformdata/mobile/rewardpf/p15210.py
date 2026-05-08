# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15210.pyc
# Source Generated with Decompyle++
# File: p15210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CAREERPF, PF_TYPE_SHOOT, PF_TYPE_THROW

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 50)
        elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            1921: 1,
            7141: 1 }, 1, 0) == 0:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 50)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 50)
        elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_SHOOT, 0) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 50)


class CPerform(CCustomPerform):
    m_SID = 15210
    m_Name = '炼金魔法'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

