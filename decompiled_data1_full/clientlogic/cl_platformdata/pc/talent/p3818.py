# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3818.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3818.pyc
# Source Generated with Decompyle++
# File: p3818.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_AMULET, MAIN_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventRecordDamFactorIndex(oWarrior, oEventCB, OBJ_ATTACK)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_AMULET):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 99)
        cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 2, 0, -99)
    else:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.EventAddRecordDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 10000)
    else:
        cl_evact.EventAddRecordDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000)


class CPerform(CCustomPerform):
    m_SID = 3818
    m_Name = '法力转化'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 119

