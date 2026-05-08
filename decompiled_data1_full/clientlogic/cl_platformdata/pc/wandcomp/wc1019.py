# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1019.pyc
# Source Generated with Decompyle++
# File: wc1019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION, WAND_SUBMSG_WANDCDEND

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_WANDCDEND, 0, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckSceneFightMonster(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())
    else:
        cl_action.CommonListenGlobalMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckSceneFightMonster(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())
        cl_action.CommonDoneGlobalMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1)


class CWandComp(CBaseComp):
    m_SID = 1019
    m_Name = '作战'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

