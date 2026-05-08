# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2059.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2059.pyc
# Source Generated with Decompyle++
# File: wc2059.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33523, 0, {
        'DamAdd': 4000 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2059
    m_Name = '封装加伤一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON, WANDTAG_PERFORM)
    m_ActionInfo = {
        1: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }

