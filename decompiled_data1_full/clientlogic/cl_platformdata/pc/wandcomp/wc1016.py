# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1016.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1016.pyc
# Source Generated with Decompyle++
# File: wc1016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import ATTACKERSUBMSG_NORMAL, WANDTAG_WEAPON, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, (lambda *a: 48 - Func749(*a) * 8))
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CWandComp(CBaseComp):
    m_SID = 1016
    m_Name = '射击命中'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

