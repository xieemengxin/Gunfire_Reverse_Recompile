# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2026.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2026.pyc
# Source Generated with Decompyle++
# File: wc2026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WANDTAG_WEAPON, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 32524, { }, None, None)


class CWandComp(CBaseComp):
    m_SID = 2026
    m_Name = '伤害附加'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM, WANDTAG_WEAPON)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

