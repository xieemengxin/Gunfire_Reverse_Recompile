# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2104.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2104.pyc
# Source Generated with Decompyle++
# File: wc2104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'DamCount', 16)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'ElementCount', 4)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'DamCount', -16)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'ElementCount', -4)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2104,
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


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33574, 500, {
        'TransDamFactor': (lambda *a: Func747(*a, **{
'iWandSID': 2104,
'sKey': 'DamCount' })),
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2104,
'sKey': 'ElementCount' })) }, 0)


class CWandComp(CBaseComp):
    m_SID = 2104
    m_Name = '元素伤害三'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

