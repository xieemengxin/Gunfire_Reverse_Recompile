# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1006.pyc
# Source Generated with Decompyle++
# File: wc1006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COMMONACTIVE_TAG_SEASONWAND, DAM_TYPE_PERFORM, WANDTAG_PERFORM, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, (lambda *a: 30 - 5 * (Func749(*a) - 1)))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERFORM):
        if cl_evcon.EventCBCheckPerfromInActivePerformTag(oWarrior, oEventCB, COMMONACTIVE_TAG_SEASONWAND):
            cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 5)
        else:
            cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CWandComp(CBaseComp):
    m_SID = 1006
    m_Name = '技能伤害'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

