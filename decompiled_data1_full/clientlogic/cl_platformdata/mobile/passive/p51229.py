# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51229.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51229.pyc
# Source Generated with Decompyle++
# File: p51229.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, HPARMORSHIELD_RADIO_SUB, OBJ_SELF
from cl_newformula import Func304, Func518, Func558, Func589, Func717

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'p51229' }))) < oLifeCycle.m_Owner.GetArgValue('RecoverTimes'):
        cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'Threshold' })), HPARMORSHIELD_RADIO_SUB, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51229' }))) < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RecoverTimes') and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func558(*a))) < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Threshold') and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > 0:
        cl_action.CommonAddCustomIntData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51229', 1, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * 20 / 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 1, 0, 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51229' }))) < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RecoverTimes') or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func558(*a))) < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Threshold'):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 0, 1, 4, 0, 0, { })
    else:
        cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'Threshold' })), HPARMORSHIELD_RADIO_SUB)


class CPerform(CCustomPerform):
    m_SID = 51229
    m_Name = '#NT#S7房间挑战4额外技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'Threshold': 50,
        'RecoverTimes': 2 }
    m_DieDisable = 0

