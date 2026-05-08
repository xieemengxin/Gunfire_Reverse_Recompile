# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4422.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4422.pyc
# Source Generated with Decompyle++
# File: p4422.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1249) or cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1249, None, None) < 5:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1249, 1, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1302, 510, { }, 1, 0, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1249, 0, { }, 1, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1249, 1, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1302, 510, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4422
    m_Name = '暴击击杀移速增加'
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

