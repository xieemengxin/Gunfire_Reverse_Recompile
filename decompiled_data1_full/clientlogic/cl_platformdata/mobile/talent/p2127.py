# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2127.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2127.pyc
# Source Generated with Decompyle++
# File: p2127.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func308(*a) * 4000 + 0), 0, DAM_TYPE_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckHasStateFromSelf(oWarrior, oEventCB, 32121) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32121, 300, { }, 0, None, None)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8001, 0, {
            'ThrowMsg': 1 }, None)


class CPerform(CCustomPerform):
    m_SID = 2127
    m_Name = '腐蚀支配'
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
    m_Career = 102

