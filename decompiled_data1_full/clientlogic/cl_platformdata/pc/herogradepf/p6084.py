# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6084.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6084.pyc
# Source Generated with Decompyle++
# File: p6084.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1422: 1,
        1430: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheackTargetFightTypeIsRealit(oWarrior, oEventCB):
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33643, 0, 1, 0) == 0:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33643, 0, { }, 1, 1, 0)
            else:
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33643, 1, 1, 0, None)
        else:
            cl_evact.EventCBGetTargetAsTargetOwner(oWarrior, oEventCB)
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33643, 0, 1, 0) == 0:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33643, 0, { }, 1, 1, 0)
            else:
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33643, 1, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6084
    m_Name = '噬魂剑客lv.4'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

