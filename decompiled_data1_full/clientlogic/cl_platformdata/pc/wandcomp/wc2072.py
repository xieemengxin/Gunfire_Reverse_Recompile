# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2072.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2072.pyc
# Source Generated with Decompyle++
# File: wc2072.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33529, 0, {
        'StateCount': 2 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2072
    m_Name = '单发幸运一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

