# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14415.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14415.pyc
# Source Generated with Decompyle++
# File: p14415.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func341, Func361
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MONSTER_PFAI_CATCH, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 7990, (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'AutoEnergyAdd' })), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 3, 0, 0)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 39247, 'DamReduce', (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'P39247DamReduce' })), 1)
    cl_action.CommonSetPFAIGroupWeightByPhase(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, 2, 3301, 1000)
    cl_action.CommonSetPFAIGroupWeightByPhase(oWarrior, oLifeCycle, MONSTER_PFAI_CATCH, 4, 3301, 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7985):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitEnergyAdd'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 7989):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 7990, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SkillEnergyAdd'), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 7989):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 7990, -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SkillEnergyAdd'), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) == 5:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33563, 0, { }, 1, 0, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) == 3:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 39247)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39246, 1, 0):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'UnusedSkill', 1)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_START, -1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39247, 1, 0):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'UnusedSkill', 0)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_END, -1)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1)


class CPerform(CCustomPerform):
    m_SID = 14415
    m_Name = '轮回10-妖王强化'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'AutoEnergyAdd': 0,
        'HitEnergyAdd': 0,
        'SkillEnergyAdd': 0,
        'ShieldMaxMul': 50,
        'P39247DamReduce': -2500,
        'Boss_S1': 60,
        'Boss_S2': 120,
        'Boss_S3': 180,
        'Boss_S4': 240,
        'Wily_Boss_S1': 40,
        'Wily_Boss_S2': 80,
        'Wily_Boss_S3': 120,
        'Wily_Boss_S4': 160,
        'Wily_Boss_S5': 200,
        'Wily_Boss_S6': 240,
        'Wily_Boss_S7': 280,
        'PF39247_Shield_Cure_Max': 30,
        'PF39247_Shield_Cure_Min': 10,
        'PF39247_Shield_Cure_Decrease': 10 }
    m_DieDisable = 0

