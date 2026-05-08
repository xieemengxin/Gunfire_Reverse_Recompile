# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13559.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13559.pyc
# Source Generated with Decompyle++
# File: p13559.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, MONSTER_PART_FLAW, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_FLAW) and cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 1):
        cl_evact.EventCBHitUnbalance(oWarrior, oEventCB, 1300)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1854, 0, 0, 0):
        cl_evact.PassiveCallBackChangDam(oWarrior, oEventCB, DAM_MASK_ELEMENT, 5000, 0)


class CPerform(CCustomPerform):
    m_SID = 13559
    m_Name = '严寒沁髓'
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
    m_Career = 116

