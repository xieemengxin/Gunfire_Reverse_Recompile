# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1005.pyc
# Source Generated with Decompyle++
# File: wc1005.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, (lambda *a: 40 - 5 * Func749(*a)))
    cl_action.CommonStartCalMoveDis(oWarrior, oLifeCycle, 1, 100, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CWandComp(CBaseComp):
    m_SID = 1005
    m_Name = '移动'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

