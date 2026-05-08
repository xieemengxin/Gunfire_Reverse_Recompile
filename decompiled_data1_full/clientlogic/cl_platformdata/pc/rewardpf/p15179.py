# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15179.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15179.pyc
# Source Generated with Decompyle++
# File: p15179.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_PERSISTENCE, DAM_USE_ARMOR, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func332, Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 8, 0, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 25, 1)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15179)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if (cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PFCNT15107') < 4) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PFCNT15107', 1)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8606, 0, {
            '1948Att': (lambda *a: Func589(*a) * 0.5 + 6000 + 2000 * Func332(*a)) }, None)
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 150)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PFCNT15107', 1)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8606, 0, {
            '1948Att': (lambda *a: Func589(*a) * 0.5 + 6000 + 2000 * Func332(*a)) }, None)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8606, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 8132, 0, 1, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8132, 0, { }, 0, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 8132, 1, 1, 0, None)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33474):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33474, 300, { }, 1)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33474, 1, 300)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, 800, CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 0, 1, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if (cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PFCNT15107') < 4) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PFCNT15107', 1)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8606, 0, {
                '1948Att': (lambda *a: Func589(*a) * 0.5 + 6000 + 2000 * Func332(*a)) }, None)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 150)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PFCNT15107', 1)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8606, 0, {
                '1948Att': (lambda *a: Func589(*a) * 0.5 + 6000 + 2000 * Func332(*a)) }, None)


class CPerform(CCustomPerform):
    m_SID = 15179
    m_Name = '腐蚀荆刺'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0

