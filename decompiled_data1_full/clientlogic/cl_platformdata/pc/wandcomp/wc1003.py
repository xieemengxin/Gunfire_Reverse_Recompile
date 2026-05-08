# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1003.pyc
# Source Generated with Decompyle++
# File: wc1003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import ATTACKERSUBMSG_NORMAL, WANDTAG_WEAPON, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, -1)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, (lambda *a: 23 - 3 * Func749(*a)))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CWandComp(CBaseComp):
    m_SID = 1003
    m_Name = '暴击'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

