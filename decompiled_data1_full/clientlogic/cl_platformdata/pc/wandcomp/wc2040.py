# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2040.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2040.pyc
# Source Generated with Decompyle++
# File: wc2040.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33576, 0, { }, 0)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2040,
'sKey': 'EnableNum' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33576, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33576, 1, 0)


class CWandComp(CBaseComp):
    m_SID = 2040
    m_Name = '元素扩散'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

