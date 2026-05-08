# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50712.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50712.pyc
# Source Generated with Decompyle++
# File: p50712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'Count', 1)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1) == 0 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') >= 3:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1, 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1413, 1, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1) == 0 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') >= 3:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1, 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1413, 1, { })


class CPerform(CCustomPerform):
    m_SID = 50712
    m_Name = '#NT#降妖伏魔连环闪电被动'
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

