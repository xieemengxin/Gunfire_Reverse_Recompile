# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2514.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2514.pyc
# Source Generated with Decompyle++
# File: p2514.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, WARRIOR_BARRIER
from cl_newformula import Func304, Func308, Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32384, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
        'DamReduce': (lambda *a: Func308(*a) * 1000),
        'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32386, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
        'DefenseValueMax': (lambda *a: Func308(*a) * 2000),
        'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, cl_action.CommonGetSummonAttr(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BARRIER, 'Width') / 2 + 1, WARRIOR_BARRIER, 1, 0, 0, 1, 0, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_BARRIER):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32384, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
            'DamReduce': (lambda *a: Func308(*a) * 1000),
            'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func308(*a) * Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.06), None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32418, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2514
    m_Name = '钢铁合剂'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 106

