# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2039.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2039.pyc
# Source Generated with Decompyle++
# File: wc2039.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33583, 1, 1, 0, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33583, 3, 1, 1, 0)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33583, 0, {
            'Att': 50 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33583, 1, 1, 0, 0):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33583, 4, 1, 1, 0)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33583, 0, {
            'Att': 80 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2039
    m_Name = '灵力膨胀'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (None, None),
        3: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

