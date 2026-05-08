# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2018.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2018.pyc
# Source Generated with Decompyle++
# File: wc2018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import MAIN_HOLD, WANDTAG_WEAPON, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD, 0, 40)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD, 0, 60)


class CWandComp(CBaseComp):
    m_SID = 2018
    m_Name = '武器充能'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
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

