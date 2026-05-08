# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6072.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6072.pyc
# Source Generated with Decompyle++
# File: p6072.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32508):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32508, None, None) >= 5:
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32508, 800, 800)
        else:
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32508, 1, 0)
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32508, 800, 800)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32508, 800, { }, 1, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32508, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 6072
    m_Name = '改版桃lv.2'
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

