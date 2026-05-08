# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2002.pyc
# Source Generated with Decompyle++
# File: wc2002.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747, Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2002,
'sKey': 'WC2002Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33539, 0)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33539, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33539, 5, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2002,
'sKey': 'WC2002Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33539, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33539, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33539, 10, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', 1)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2002,
'sKey': 'WC2002Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33539, 0)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33539, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33539, 16, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2002
    m_Name = '迅捷'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, DisableAction1),
        2: (Action2, DisableAction2),
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

