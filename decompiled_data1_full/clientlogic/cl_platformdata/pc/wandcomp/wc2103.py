# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2103.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2103.pyc
# Source Generated with Decompyle++
# File: wc2103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'DamCount', 8)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'ElementCount', 2)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'DamCount', -8)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'ElementCount', -2)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2103,
'sKey': 'DamCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33574, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33574, {
            'TransDamFactor': (lambda *a: Func747(*a, **{
'iWandSID': 2043,
'sKey': 'DamCount' })),
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2043,
'sKey': 'ElementCount' })) })


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33574, 500, {
        'TransDamFactor': (lambda *a: Func747(*a, **{
'iWandSID': 2103,
'sKey': 'DamCount' })),
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2103,
'sKey': 'ElementCount' })) }, 0)


class CWandComp(CBaseComp):
    m_SID = 2103
    m_Name = '元素伤害二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

