# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2037.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2037.pyc
# Source Generated with Decompyle++
# File: wc2037.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33575):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33575, 1, 1, 0, 0):
            cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33575, 0, { }, 1)
        else:
            cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33575, 0, { }, 1)


class CWandComp(CBaseComp):
    m_SID = 2037
    m_Name = '临时主动'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

