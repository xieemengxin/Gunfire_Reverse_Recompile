# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2025.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2025.pyc
# Source Generated with Decompyle++
# File: wc2025.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

class CWandComp(CBaseComp):
    m_SID = 2025
    m_Name = '获得印记'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (None, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

