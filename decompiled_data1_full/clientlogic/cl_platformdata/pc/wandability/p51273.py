# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51273.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51273.pyc
# Source Generated with Decompyle++
# File: p51273.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE, ATTACKERSUBMSG_NORMAL, CHARGECARTOON_SUBMSG_END, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'AdditionElement', 0):
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, 0)
        cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33603:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Count' }))) >= 5 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') <= 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardLevel', 1)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33690, 0, {
                'StatusEffect': 1 }, 1, 1, 0)
            cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33602, {
                'StatusEffect': 1 }, None, None)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Count' }))) >= 15 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') <= 1:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardLevel', 2)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AdditionElement', 1)
            cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33690, {
                'StatusEffect': 2 }, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AdditionElement'):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'AdditionElement', 1, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AdditionElement', 0)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RewardLevel') > 0:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33602, {
            'StatusEffect': 0 }, None, None)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardLevel', 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33690, 0)


class CPerform(CCustomPerform):
    m_SID = 51273
    m_Name = '蓄力令牌专属词条'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

