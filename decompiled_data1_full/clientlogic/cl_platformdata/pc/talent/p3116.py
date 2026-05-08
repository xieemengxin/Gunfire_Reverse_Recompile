# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3116.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3116.pyc
# Source Generated with Decompyle++
# File: p3116.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_FIRE, ENERGY_RS_LICAREER, OBJ_SELF
from cl_newformula import Func308, Func538

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 3116) <= 2:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 300 * Func308(*a)), None)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 1300, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChangeEnergyReason(oWarrior, oEventCB, ENERGY_RS_LICAREER) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: 10 + 10 * Func308(*a))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func538(*a)))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChangeEnergyReason(oWarrior, oEventCB, ENERGY_RS_LICAREER) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func538(*a)))


class CPerform(CCustomPerform):
    m_SID = 3116
    m_Name = '野火不尽'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 112

