# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2085.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2085.pyc
# Source Generated with Decompyle++
# File: wc2085.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33568, 0, { }, 1)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33568, 2, 1, 1, 400)


class CWandComp(CBaseComp):
    m_SID = 2085
    m_Name = '武器等级一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

