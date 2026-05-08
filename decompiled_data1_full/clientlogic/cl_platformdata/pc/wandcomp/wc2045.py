# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2045.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2045.pyc
# Source Generated with Decompyle++
# File: wc2045.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747, Func775

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', 3)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', 1)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, { }, 0)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33631, 0, { }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, { }, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', -3)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33631, 0)
    else:
        cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' })) }, None, None)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 9, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33631, 3, 300)


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', 6)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', 1)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, { }, 0)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33631, 0, { }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, { }, None, None)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', -6)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33631, 0)
    else:
        cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' })) }, None, None)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 18, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33631, 6, 300)


def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', 10)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', 1)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, { }, 0)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33631, 0, { }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, { }, None, None)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WeakenCount', -10)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableCount', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33631, 0)
    else:
        cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'EnableCount' }) + Func775(*a, **{
'sKey': 'EnableCount' })), 'EnableCount')
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }) + Func775(*a, **{
'sKey': 'WeakenCount' })) }, None, None)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 30, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33631, 10, 300)


class CWandComp(CBaseComp):
    m_SID = 2045
    m_Name = '灵力迸发'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (Action1, DisableAction1),
        2: (Action2, DisableAction2),
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

