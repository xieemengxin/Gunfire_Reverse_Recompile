# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1017.pyc
# Source Generated with Decompyle++
# File: wc1017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION

def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33600, 0, { }, 1)


class CWandComp(CBaseComp):
    m_SID = 1017
    m_Name = '定时'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        3: (Action3, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = { }

