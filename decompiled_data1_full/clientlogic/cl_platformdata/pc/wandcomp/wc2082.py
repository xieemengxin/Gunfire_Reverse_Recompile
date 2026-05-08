# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2082.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2082.pyc
# Source Generated with Decompyle++
# File: wc2082.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION

def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33553, 0, {
        'StatusEffect': 2 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2082
    m_Name = '鲁莽Q击一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }

