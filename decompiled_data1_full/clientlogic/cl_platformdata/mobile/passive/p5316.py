# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5316.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5316.pyc
# Source Generated with Decompyle++
# File: p5316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, SUBLIME_DOUBLE_DAMAGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveSourceItemTmpData(oWarrior, oLifeCycle, 'PF_5316')


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9799, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8139, 1, 0, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8139, 2, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8139, 0, { }, 1, 0, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8139, 2, 1)
        cl_evact.EventCBUseTargetAsSourceWeaponFlag(oWarrior, oEventCB, 'PF_5316')


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9799, 0, 0):
        cl_evact.EventCBAddShowTipsEffect(oWarrior, oEventCB, SUBLIME_DOUBLE_DAMAGE)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8139, 1, 0, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8139, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8139, 0, { }, 1, 0, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8139, 1, 1)
        cl_evact.EventCBUseTargetAsSourceWeaponFlag(oWarrior, oEventCB, 'PF_5316')


class CPerform(CCustomPerform):
    m_SID = 5316
    m_Name = '#NT元素法杖B被动'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

