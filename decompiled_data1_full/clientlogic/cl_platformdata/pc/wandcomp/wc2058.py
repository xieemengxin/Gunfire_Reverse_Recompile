# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2058.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2058.pyc
# Source Generated with Decompyle++
# File: wc2058.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33525, 300, {
        'StateCount': 100 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2058
    m_Name = '暴击加成二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

