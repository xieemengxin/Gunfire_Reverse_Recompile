# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1011.pyc
# Source Generated with Decompyle++
# File: wc1011.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WANDTAG_DAMAGE, WAND_COMP_TYPE_CONDITION

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasStateByAttacker(oWarrior, oEventCB, 33542, 0):
        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


class CWandComp(CBaseComp):
    m_SID = 1011
    m_Name = '狩猎标记'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_DAMAGE,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

