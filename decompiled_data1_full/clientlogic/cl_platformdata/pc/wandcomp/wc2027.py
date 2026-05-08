# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2027.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2027.pyc
# Source Generated with Decompyle++
# File: wc2027.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION, WARRIOR_MONSTER
from cl_newformula import Func223, Func742, Func752

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1736)
    cl_action.WandCompSetWandBaseCount(oWarrior, oLifeCycle, 1011, 3)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'DamageRatio', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 1736)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1736)
    cl_action.WandCompSetWandBaseCount(oWarrior, oLifeCycle, 1011, 3)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'DamageRatio', 2)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 1736)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1736)
    cl_action.WandCompSetWandBaseCount(oWarrior, oLifeCycle, 1011, 5)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'DamageRatio', 3)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 1736)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 0, (lambda *a: Func752(*a, **{
'iWandSID': 1011,
'iDefault': 3 })), 0, 1, 1, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1736, {
            'Cnt': (lambda *a: Func752(*a, **{
'iWandSID': 1011,
'iDefault': 3 })),
            'Att': (lambda *a: (Func223(*a) * 10000 + 40000) * Func742(*a, **{
'sArg': 'DamageRatio' })),
            'ElementExceptionRatio': 2000 }, None)
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ClearCount', 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 0, (lambda *a: Func752(*a, **{
'iWandSID': 1011,
'iDefault': 3 })), 0, 1, 1, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1736, {
            'Cnt': (lambda *a: Func752(*a, **{
'iWandSID': 1011,
'iDefault': 5 })),
            'Att': (lambda *a: (Func223(*a) * 10000 + 40000) * Func742(*a, **{
'sArg': 'DamageRatio' })),
            'ElementExceptionRatio': 2000 }, None)
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ClearCount', 1)


class CWandComp(CBaseComp):
    m_SID = 2027
    m_Name = '流星'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (Action1, DisableAction1),
        2: (Action2, DisableAction2),
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

