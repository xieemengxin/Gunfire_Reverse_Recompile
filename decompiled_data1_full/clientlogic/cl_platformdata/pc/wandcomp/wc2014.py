# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2014.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2014.pyc
# Source Generated with Decompyle++
# File: wc2014.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, OBJ_SELF, WANDTAG_OTHER, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func377, Func589, Func742, Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'RecoverRatio', 20)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'RecoverRatio', 40)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'RecoverHP', (lambda *a: Func589(*a) * Func742(*a, **{
'sArg': 'RecoverRatio' }) // 100))
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'RealRecovery', (lambda *a: min(Func742(*a, **{
'sArg': 'RecoverHP' }), Func377(*a))))
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func742(*a, **{
'sArg': 'RecoverHP' })), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 1, None)
    cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33520, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
        'StateCount': (lambda *a: Func742(*a, **{
'sArg': 'RealRecovery' }) // 5) }, 0)


class CWandComp(CBaseComp):
    m_SID = 2014
    m_Name = '紧急回复'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, None),
        2: (Action2, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

