# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2110.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2110.pyc
# Source Generated with Decompyle++
# File: wc2110.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'Enable', 1)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EffertCount', 4)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'Enable', -1)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EffertCount', -4)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2110,
'sKey': 'Enable' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33596, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33596, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2048,
'sKey': 'EffertCount' })),
            'StatusEffect': (lambda *a: Func747(*a, **{
'iWandSID': 2048,
'sKey': 'Enable' })) })


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33596, 400, {
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2110,
'sKey': 'EffertCount' })),
        'StatusEffect': (lambda *a: Func747(*a, **{
'iWandSID': 2110,
'sKey': 'Enable' })) }, 0)


class CWandComp(CBaseComp):
    m_SID = 2110
    m_Name = '近战加伤一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON, WANDTAG_PERFORM)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

