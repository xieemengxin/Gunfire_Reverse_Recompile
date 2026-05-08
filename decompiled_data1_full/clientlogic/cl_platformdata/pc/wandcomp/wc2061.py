# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2061.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2061.pyc
# Source Generated with Decompyle++
# File: wc2061.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33523, 0, {
        'DamAdd': 12000 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2061
    m_Name = '封装加伤三'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON, WANDTAG_PERFORM)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

