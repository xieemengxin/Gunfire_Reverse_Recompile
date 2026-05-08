# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2020.pyc
# Source Generated with Decompyle++
# File: wc2020.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import DAM_USE_HP, WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func223, Func304, Func374, Func742

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1969)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'OldVal', (lambda *a: Func374(*a)))
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, (lambda *a: -Func304(*a, **{
'sAttr': 'HP' }) * 10 / 100), DAM_USE_HP)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1969, {
        'Att': (lambda *a: 50 * (Func742(*a, **{
'sArg': 'OldVal' }) - Func374(*a)) * (1 + Func223(*a) * 0.125)) })


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1969)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'OldVal', (lambda *a: Func374(*a)))
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, (lambda *a: -Func304(*a, **{
'sAttr': 'HP' }) * 10 / 100), DAM_USE_HP)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1969, {
        'Att': (lambda *a: 100 * (Func742(*a, **{
'sArg': 'OldVal' }) - Func374(*a)) * (1 + Func223(*a) * 0.125)) })


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1969)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'OldVal', (lambda *a: Func374(*a)))
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, (lambda *a: -Func304(*a, **{
'sAttr': 'HP' }) * 10 / 100), DAM_USE_HP)
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1969, {
        'Att': (lambda *a: 200 * (Func742(*a, **{
'sArg': 'OldVal' }) - Func374(*a)) * (1 + Func223(*a) * 0.125)) })


class CWandComp(CBaseComp):
    m_SID = 2020
    m_Name = '生命自爆'
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
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

