# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2054.pyc
# Source Generated with Decompyle++
# File: wc2054.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2002Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2002,
'sKey': 'WC2002Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33539, 0)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33539, 300, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33539, 5, 300)


class CWandComp(CBaseComp):
    m_SID = 2054
    m_Name = '移速加成一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, DisableAction1) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }

