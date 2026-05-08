# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5348.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5348.pyc
# Source Generated with Decompyle++
# File: p5348.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33926, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9421, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, 33926, 1)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1003, 50, {
                'MoveSpeedMul': -8000 }, 1, 0, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8163, 50, { }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9592, 1, 0):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 2, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9592, 1, 0):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1)
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5348
    m_Name = '#NT#龙息被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

