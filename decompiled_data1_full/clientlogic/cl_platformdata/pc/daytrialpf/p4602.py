# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4602.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4602.pyc
# Source Generated with Decompyle++
# File: p4602.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_HP, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func425

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON) and not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2001) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2002) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2003) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2004) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 3004) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321):
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func425(*a) * 6), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, None)
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
            cl_evact.EventClientBehavior(oWarrior, oEventCB, 14, 0)


class CPerform(CCustomPerform):
    m_SID = 4602
    m_Name = '非暴击回血'
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

