# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13542.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13542.pyc
# Source Generated with Decompyle++
# File: p13542.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, -1, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, -1, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 4356, 1)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32891, 0, { }, 1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 30, 0, 0, -1, -1, -1, -1, 1, -1, None)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -3000, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32867, 0, 0, 1):
        cl_evact.EventChangeDamCrazyEff(oWarrior, oEventCB, 30000, 0)
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 25000, 0, 0, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 50)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetRemovePerform(oWarrior, oEventCB, 4356)


class CPerform(CCustomPerform):
    m_SID = 13542
    m_Name = '同舟共济'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 114

