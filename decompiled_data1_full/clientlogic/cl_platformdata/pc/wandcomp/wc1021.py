# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1021.pyc
# Source Generated with Decompyle++
# File: wc1021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION, WAND_SUBMSG_UPGRADE
from cl_newformula import Func749

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_UPGRADE, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33628, 0, {
        'StatusEffect': (lambda *a: Func749(*a)) }, 1)


class CWandComp(CBaseComp):
    m_SID = 1021
    m_Name = '定时'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

