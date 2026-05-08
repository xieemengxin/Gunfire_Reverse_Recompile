# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2030.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2030.pyc
# Source Generated with Decompyle++
# File: wc2030.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_WEAPON, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33568, 0, { }, 1)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 600 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33568, 0, { }, 1)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 800 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33568, 0, { }, 1)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 1000 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33568, 2, 1, 1, (lambda *a: 600 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33568, 2, 1, 1, (lambda *a: 800 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33568, 2, 1, 1, (lambda *a: 1000 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2030
    m_Name = '武器强化'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None),
        2: (Action2, None),
        3: (Action3, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

