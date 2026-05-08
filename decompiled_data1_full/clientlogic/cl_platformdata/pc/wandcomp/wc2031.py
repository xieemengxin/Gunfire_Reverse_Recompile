# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2031.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2031.pyc
# Source Generated with Decompyle++
# File: wc2031.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747, Func775

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'CompScoreSum', 1)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33569, 0, {
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2031,
'sKey': 'CompScoreSum' }) + Func775(*a, **{
'sKey': 'CompScoreSum' })) }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33569, (lambda *a: Func747(*a, **{
'iWandSID': 2031,
'sKey': 'CompScoreSum' }) + Func775(*a, **{
'sKey': 'CompScoreSum' })), 'MaxCount')
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33569, { }, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'CompScoreSum', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2031,
'sKey': 'CompScoreSum' }) + Func775(*a, **{
'sKey': 'CompScoreSum' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33569, 0)
    else:
        cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33569, (lambda *a: Func747(*a, **{
'iWandSID': 2031,
'sKey': 'CompScoreSum' }) + Func775(*a, **{
'sKey': 'CompScoreSum' })), 'MaxCount')
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33569, { }, None, None)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33569, 1, 0)


class CWandComp(CBaseComp):
    m_SID = 2031
    m_Name = '琉璃之盾'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, DisableAction1) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

