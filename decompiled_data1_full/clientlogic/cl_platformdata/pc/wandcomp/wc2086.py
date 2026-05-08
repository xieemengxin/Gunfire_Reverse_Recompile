# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2086.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2086.pyc
# Source Generated with Decompyle++
# File: wc2086.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33568, 0, { }, 1)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33568, 3, 1, 1, 500)


class CWandComp(CBaseComp):
    m_SID = 2086
    m_Name = '武器等级二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

