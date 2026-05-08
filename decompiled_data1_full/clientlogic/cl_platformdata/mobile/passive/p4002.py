# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4002.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4002.pyc
# Source Generated with Decompyle++
# File: p4002.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, EXECUTETYPE_PART_SECKILL, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_NORMAL
from cl_newformula import Func302

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 3333,
            2: 3333 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 22, 0)
    cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_PART_SECKILL)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 23, 0)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -10000, DAM_TYPE_WEAPON, '')
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) * 100 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4002
    m_Name = '1207概率秒杀概率回满血'
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

