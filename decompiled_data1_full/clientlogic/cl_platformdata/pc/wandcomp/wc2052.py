# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2052.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2052.pyc
# Source Generated with Decompyle++
# File: wc2052.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2001Count', 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2001Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2001,
'sKey': 'WC2001Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33537, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33537, 500, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33537, 6, 500)


class CWandComp(CBaseComp):
    m_SID = 2052
    m_Name = '技能加成二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

