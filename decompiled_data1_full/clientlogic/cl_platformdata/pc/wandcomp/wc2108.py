# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2108.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2108.pyc
# Source Generated with Decompyle++
# File: wc2108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION

def TriggerAction3(oWarrior, oLifeCycle):
    if cl_condition.CommonCheckCanTriggerNextPosComp(oWarrior, oLifeCycle):
        cl_action.CommonTriggerNextPosActionComp(oWarrior, oLifeCycle, 1)


class CWandComp(CBaseComp):
    m_SID = 2108
    m_Name = '复制模块一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

