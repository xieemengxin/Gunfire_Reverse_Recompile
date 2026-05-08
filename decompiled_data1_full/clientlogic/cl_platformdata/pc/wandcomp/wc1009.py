# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1009.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1009.pyc
# Source Generated with Decompyle++
# File: wc1009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func786

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, -1, 0, 0, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, 30)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: abs(Func786(*a))))


class CWandComp(CBaseComp):
    m_SID = 1009
    m_Name = '铜币变化'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

