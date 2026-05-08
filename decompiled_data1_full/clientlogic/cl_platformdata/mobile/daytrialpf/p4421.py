# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4421.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4421.pyc
# Source Generated with Decompyle++
# File: p4421.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11101, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1254, 300, { }, 0, 0, None)
    if cl_evcon.GetTargetStateNum(oWarrior, oEventCB, 1254, 0) >= 3:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1255, 1000, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4421
    m_Name = '连杀不耗子弹'
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

