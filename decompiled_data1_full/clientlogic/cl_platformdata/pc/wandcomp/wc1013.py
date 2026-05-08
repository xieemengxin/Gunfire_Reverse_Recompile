# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1013.pyc
# Source Generated with Decompyle++
# File: wc1013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_CONDITION

def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, 18)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandConditionCompAddCount(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CWandComp(CBaseComp):
    m_SID = 1013
    m_Name = '射击'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        3: (Action3, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

