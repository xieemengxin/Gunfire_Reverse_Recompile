# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1020.pyc
# Source Generated with Decompyle++
# File: wc1020.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import CHARGECARTOON_SUBMSG_END, CHARGECARTOON_SUBMSG_START, WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION, WAND_SUBMSG_TRIGGERACTION

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
    cl_action.WandCompSetKeepValue(oWarrior, oLifeCycle, 'InCharge', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandCompAddKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InCharge', 1)
    cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.WandCompGetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InCharge'):
        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.WandCompAddKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InCharge', -1)
    if cl_condition.WandCompGetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InCharge') <= 0:
        cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'InCharge', 0)


class CWandComp(CBaseComp):
    m_SID = 1020
    m_Name = '蓄力'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

