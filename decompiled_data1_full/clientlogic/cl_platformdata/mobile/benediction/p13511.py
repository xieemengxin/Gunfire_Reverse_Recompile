# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13511.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13511.pyc
# Source Generated with Decompyle++
# File: p13511.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DAM_TYPE_THUNDER, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, None)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: 3 + Func410(*a, **{
'sid': 1566 })), WARRIOR_MONSTER, 1, 1, 0, 0, 0, None, None, None)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_MASK_ELEMENT, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, 0, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 20000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 13511
    m_Name = '雷电使者'
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
    m_Career = 104

