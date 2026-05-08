# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4424.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4424.pyc
# Source Generated with Decompyle++
# File: p4424.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_NORBADGER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1433) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 1262) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBADGER) == 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 3):
        cl_evact.EventCBDropRrlifeDrop(oWarrior, oEventCB, 1694)


class CPerform(CCustomPerform):
    m_SID = 4424
    m_Name = '绝地求生'
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

