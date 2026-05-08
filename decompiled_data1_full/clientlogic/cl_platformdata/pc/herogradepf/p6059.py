# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6059.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6059.pyc
# Source Generated with Decompyle++
# File: p6059.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, WARRIOR_BARRIER, WARRIOR_HERO
from cl_newformula import Func331, Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1415, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetBySummonType(oWarrior, oEventCB, WARRIOR_BARRIER)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32461, 50, { }, 0, 0, None)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, cl_action.CommonGetSummonAttr(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BARRIER, 'Width') / 2 + 1, WARRIOR_HERO, 1, 1, 0, -1, None, None, None)
        cl_evact.EventCBRemoveSelfFromTarget(oWarrior, oEventCB)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32363, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
        'StatusEffect': -50,
        'Att': cl_evact.EventCBGetPerformAttr(oWarrior, oEventCB, 'Att'),
        'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
    if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2513) >= 3:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32385, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
            'StatusEffect': -50,
            'LuckyHit': 20,
            'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
    if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2514) >= 1:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32384, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
            'DamReduce': (lambda *a: Func331(*a, **{
'sid': 2514 }) * 1000),
            'StatusEffect': -50,
            'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32386, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
            'DefenseValueMax': (lambda *a: Func331(*a, **{
'sid': 2514 }) * 2000),
            'StatusEffect': -50,
            'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6059
    m_Name = '卫士lv.4'
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

