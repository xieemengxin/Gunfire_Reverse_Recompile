# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6035.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6035.pyc
# Source Generated with Decompyle++
# File: p6035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_BOSSCANNON

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32347, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, 1, None) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSSCANNON):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32347, 1, 0)
        elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, 1, 1) and cl_evcon.CheckCareerTrigger(oWarrior, oEventCB, {
            0: 2302,
            1: 2312 }) == 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            if not cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, 1, None) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSSCANNON):
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32347, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 6035
    m_Name = '游侠【武器】4'
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

