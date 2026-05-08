# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2066.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2066.pyc
# Source Generated with Decompyle++
# File: wc2066.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonSubCareerPerformColdTime(oWarrior, oLifeCycle, 0, 25)


class CWandComp(CBaseComp):
    m_SID = 2066
    m_Name = '冷却回复二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

