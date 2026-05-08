# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2117.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2117.pyc
# Source Generated with Decompyle++
# File: wc2117.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func308, Func332, Func379, Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1975)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1975, {
        'Radius': (lambda *a: (2 + Func308(*a)) * (1 + 0.5 * Func379(*a) // 33)),
        'Att': (lambda *a: (800 + Func589(*a) * 0.06 + 100 * Func332(*a)) * 100 * Func308(*a)) })


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1975)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1975, {
        'Radius': (lambda *a: (2 + Func308(*a)) * (1 + 0.5 * Func379(*a) // 33)),
        'Att': (lambda *a: (800 + Func589(*a) * 0.06 + 100 * Func332(*a)) * 100 * Func308(*a)) })


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1975)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 1975, {
        'Radius': (lambda *a: (2 + Func308(*a)) * (1 + 0.5 * Func379(*a) // 33)),
        'Att': (lambda *a: (800 + Func589(*a) * 0.06 + 100 * Func332(*a)) * 100 * Func308(*a)) })


class CWandComp(CBaseComp):
    m_SID = 2117
    m_Name = '腐蚀剑气'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
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

