# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2097.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2097.pyc
# Source Generated with Decompyle++
# File: wc2097.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION
from cl_newformula import Func308

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33583, 1, 1, 0, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33583, 3, 1, 1, 0)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33583, 0, {
            'Att': (lambda *a: 15 * Func308(*a) + 35) }, 1)


class CWandComp(CBaseComp):
    m_SID = 2097
    m_Name = 'Q范围'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

