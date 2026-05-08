# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2109.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2109.pyc
# Source Generated with Decompyle++
# File: wc2109.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

class CWandComp(CBaseComp):
    m_SID = 2109
    m_Name = '复制秘法'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT
    m_CopyWandTimes = 2

