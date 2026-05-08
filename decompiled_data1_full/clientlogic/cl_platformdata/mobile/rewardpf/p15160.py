# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15160.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15160.pyc
# Source Generated with Decompyle++
# File: p15160.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_VICTIM, PF_TYPE_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33494, 0, 1, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33494, 0, { }, 1, 1, 0)
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 600 * cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 33494, 1, None), DAM_MASK_ELEMENT, '')
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33494, 1, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15160
    m_Name = '魔力渴求'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

