# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13524.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13524.pyc
# Source Generated with Decompyle++
# File: p13524.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32673, 0, 1) == 0:
        cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, (0, None, ((303, 'Trajectory'), (lambda a0: a0))), 1, 1, 0, 1, None, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32673, (0, None, ((410, 1573), (lambda a0: 50 - a0))), { }, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 13524
    m_Name = '避无可避'
    m_MaxLevel = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 103

