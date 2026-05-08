# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6058.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6058.pyc
# Source Generated with Decompyle++
# File: p6058.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_BARRIER, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSummonFightType(oWarrior, oEventCB, WARRIOR_BARRIER) and cl_evcon.GetSummonAttr(oWarrior, oEventCB, 'HP') <= 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1202, 200, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckBulletHit(oWarrior, oEventCB):
        cl_action.CommonSubCareerPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 10, 0)


class CPerform(CCustomPerform):
    m_SID = 6058
    m_Name = '卫士lv.3'
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

