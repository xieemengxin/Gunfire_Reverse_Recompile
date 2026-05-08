# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4622.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4622.pyc
# Source Generated with Decompyle++
# File: p4622.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1242, 110, { }, 0, 0, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 100, { }, 0, 0, None)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4622
    m_Name = '非暴击击杀延迟死亡'
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

