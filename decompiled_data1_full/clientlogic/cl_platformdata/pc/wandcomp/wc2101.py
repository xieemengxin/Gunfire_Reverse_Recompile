# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2101.pyc
# Source Generated with Decompyle++
# File: wc2101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION
from cl_newformula import Func758, Func759

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompSetKeepValue(oWarrior, oLifeCycle, 'RecoverRatio', 15)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: Func759(*a) * Func758(*a, **{
'sAttr': 'RecoverRatio' }) // 100), 0)


class CWandComp(CBaseComp):
    m_SID = 2101
    m_Name = '回复备弹'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

