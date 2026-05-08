# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2090.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2090.pyc
# Source Generated with Decompyle++
# File: wc2090.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 10)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', -10)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2032,
'sKey': 'EnableNum' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33572, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33574, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2032,
'sKey': 'EnableNum' })) })


def TriggerAction3(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33572):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33572, 10, 500)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33572, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33572, 10, 500)


class CWandComp(CBaseComp):
    m_SID = 2090
    m_Name = '施法增伤三'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

