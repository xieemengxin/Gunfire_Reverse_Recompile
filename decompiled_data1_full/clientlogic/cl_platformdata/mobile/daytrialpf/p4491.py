# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4491.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4491.pyc
# Source Generated with Decompyle++
# File: p4491.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CHARGE, PF_TYPE_SHOOT
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'p4491', 1, 0)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, (lambda *a: Func410(*a, **{
'sid': 1313 }) * 4000), 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_SHOOT, None) or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CHARGE, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1312, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1312, 0, { }, 0, 0, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1313, 0, { }, 0, 0, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 1313, 5, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1312, None, None) == 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4491', None) > 0:
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1313, 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1312, 0)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1312, None, None) > 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4491', None) > 0:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1313, cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1312, 0, 0), 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1312, 0)


class CPerform(CCustomPerform):
    m_SID = 4491
    m_Name = '射击或技能击杀敌人后，下次射击或技能会造成额外伤害'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

