# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2116.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2116.pyc
# Source Generated with Decompyle++
# File: wc2116.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import DAM_USE_ALL, OBJ_SELF, WANDTAG_OTHER, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func374, Func742, Func747, Func775, Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33612, 0, { }, 0)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33632, 0, { }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'HPChange', 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2116,
'sKey': 'HPChange' }) + Func775(*a, **{
'sKey': 'HPChange' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33612, 0)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'HPChange', (lambda *a: 0.3 * Func374(*a)))
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, (lambda *a: -Func742(*a, **{
'sArg': 'HPChange' })), DAM_USE_ALL)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33612, 0, { }, 0)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33632, 0, { }, 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'HPChange', 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2116,
'sKey': 'HPChange' }) + Func775(*a, **{
'sKey': 'HPChange' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33612, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'HPChange', (lambda *a: 0.4 * Func374(*a)))
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, (lambda *a: -Func742(*a, **{
'sArg': 'HPChange' })), DAM_USE_ALL)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33632, (lambda *a: 0.002 * Func742(*a, **{
'sArg': 'HPChange' })), 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33632, (lambda *a: 0.003 * Func742(*a, **{
'sArg': 'HPChange' })), 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2116
    m_Name = '异能转化'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, DisableAction1),
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

