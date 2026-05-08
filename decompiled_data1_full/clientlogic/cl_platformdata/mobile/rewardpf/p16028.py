# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16028.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16028.pyc
# Source Generated with Decompyle++
# File: p16028.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_ATTACK, STATUS_JUMP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 16028, 2, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_JUMP) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_JUMP) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None):
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    else:
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 16028
    m_Name = '腾云驾雾'
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

