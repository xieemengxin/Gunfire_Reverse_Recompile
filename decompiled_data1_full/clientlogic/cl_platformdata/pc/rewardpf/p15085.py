# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15085.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15085.pyc
# Source Generated with Decompyle++
# File: p15085.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32980):
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32980, 1, 300, -1)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32980, 0, { }, 1, -1, None)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32957, 1, 500, -1)


class CPerform(CCustomPerform):
    m_SID = 15085
    m_Name = '#NT#武器秘卷'
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

