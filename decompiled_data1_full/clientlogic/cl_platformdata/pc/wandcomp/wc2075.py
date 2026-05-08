# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2075.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2075.pyc
# Source Generated with Decompyle++
# File: wc2075.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_ACTION

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 40)


class CWandComp(CBaseComp):
    m_SID = 2075
    m_Name = '获得铜币二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

