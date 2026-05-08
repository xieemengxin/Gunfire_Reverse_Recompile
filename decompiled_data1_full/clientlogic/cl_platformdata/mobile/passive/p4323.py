# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4323.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4323.pyc
# Source Generated with Decompyle++
# File: p4323.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9414, 1, -1):
        cl_evact.EventCBAddSourceWeaponPFBullet(oWarrior, oEventCB, 9493, 1, 0, None)
    if cl_evcon.GetPFBulletCount(oWarrior, oEventCB, 9493) == 13 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'QTEState') == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32918, 200, { }, 1, -1, None)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'QTEState', 1)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9492, 1, -1) and cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) == 2:
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 50)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9493, 1, -1):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'QTEState', 0)


class CPerform(CCustomPerform):
    m_SID = 4323
    m_Name = '毒手套能量'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

