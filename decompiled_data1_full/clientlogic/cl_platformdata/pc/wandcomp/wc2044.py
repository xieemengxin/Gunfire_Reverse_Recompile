# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2044.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2044.pyc
# Source Generated with Decompyle++
# File: wc2044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func361, Func780

def TriggerAction1(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33585):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33585, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33585, 10, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def TriggerAction2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33585):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33585, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' })), { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33585, 15, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def TriggerAction3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33585):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33585, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' })), { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33585, 15, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: Func361(*a, **{
'sid': 51218,
'sArgs': 'StateTime' }) + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2044
    m_Name = '额外弹丸'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (None, None),
        2: (None, None),
        3: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

