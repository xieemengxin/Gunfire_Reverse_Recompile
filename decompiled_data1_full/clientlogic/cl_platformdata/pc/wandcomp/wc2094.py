# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2094.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2094.pyc
# Source Generated with Decompyle++
# File: wc2094.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 4)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', -4)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2036,
'sKey': 'EnableNum' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33573, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33574, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2036,
'sKey': 'EnableNum' })) })


def TriggerAction2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33573):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33573, 4, 300)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33573, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33573, 4, 300)


class CWandComp(CBaseComp):
    m_SID = 2094
    m_Name = '武器射速一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

