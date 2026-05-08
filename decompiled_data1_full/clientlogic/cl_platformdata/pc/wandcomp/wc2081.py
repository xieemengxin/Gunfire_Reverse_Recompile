# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2081.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2081.pyc
# Source Generated with Decompyle++
# File: wc2081.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_ACTION
from cl_item.defines import MAIN_HOLD

def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD, 0, 80)


class CWandComp(CBaseComp):
    m_SID = 2081
    m_Name = '武器资源二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        3: (None, None) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

