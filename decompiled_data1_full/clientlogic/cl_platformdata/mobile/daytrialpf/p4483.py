# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4483.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4483.pyc
# Source Generated with Decompyle++
# File: p4483.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM
from cl_newformula import Func354

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1285, 0, { }, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) and not cl_evcon.CheckSkillHitCartoon(oWarrior, oEventCB, None):
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1285, 1, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) and not cl_evcon.CheckSkillHitCartoon(oWarrior, oEventCB, None):
        cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, (lambda *a: Func354(*a) * 6 // 10), 1285, 'p1285')


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1285, None, None) >= 5 and cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) and not cl_evcon.CheckSkillHitCartoon(oWarrior, oEventCB, None):
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1285, 0)
        cl_evact.EventCBSetCartoonUpdateValue(oWarrior, oEventCB, 'p1285', cl_evact.EventCBGetStateStatistics(oWarrior, oEventCB, 1285, 'p1285'))
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 1285, 'p1285')
    if cl_evact.EventCBGetCartoonUpdateValue(oWarrior, oEventCB, 'p1285'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, cl_evact.EventCBGetCartoonUpdateValue(oWarrior, oEventCB, 'p1285'), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, -1, -1, -1, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4483
    m_Name = '爆炸击杀储存伤害'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

