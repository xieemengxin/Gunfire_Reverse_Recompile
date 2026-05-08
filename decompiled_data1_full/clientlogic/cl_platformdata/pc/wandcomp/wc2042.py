# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2042.pyc
# Source Generated with Decompyle++
# File: wc2042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func759

def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: Func759(*a) * 15 // 100), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: Func759(*a) * 30 // 100), 0)


class CWandComp(CBaseComp):
    m_SID = 2042
    m_Name = '备弹回复'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (None, None),
        2: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

