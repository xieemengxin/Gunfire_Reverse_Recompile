# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2089.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2089.pyc
# Source Generated with Decompyle++
# File: wc2089.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 6)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', -6)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2032,
'sKey': 'EnableNum' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33572, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33574, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2032,
'sKey': 'EnableNum' })) })


def TriggerAction2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33572):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33572, 6, 500)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33572, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33572, 6, 500)


class CWandComp(CBaseComp):
    m_SID = 2089
    m_Name = '施法增伤二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

