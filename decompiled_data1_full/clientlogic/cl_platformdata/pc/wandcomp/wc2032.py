# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2032.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2032.pyc
# Source Generated with Decompyle++
# File: wc2032.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_OTHER, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func742, Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 2)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 3)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'EnableNum', 4)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33572, 1, 1, 0, 0):
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33572, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
            'StatusEffect': (lambda *a: Func742(*a, **{
'sArg': 'EnableNum' })) }, 1)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33572, 1, 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2032
    m_Name = '威能增幅'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, None),
        2: (Action2, None),
        3: (Action3, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

