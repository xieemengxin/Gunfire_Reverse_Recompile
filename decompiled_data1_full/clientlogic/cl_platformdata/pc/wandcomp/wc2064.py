# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2064.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2064.pyc
# Source Generated with Decompyle++
# File: wc2064.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2005Count', 1)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2005Count', -1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2005,
'sKey': 'WC2005Count' }))) == 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33540, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33540, 0)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33540, 500, { }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33540, 10, 500)


class CWandComp(CBaseComp):
    m_SID = 2064
    m_Name = '武器加成三'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

