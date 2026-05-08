# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6701.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6701.pyc
# Source Generated with Decompyle++
# File: p6701.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, MONSTER_PART_LEFTGUN, MONSTER_PART_RIGHTGUN, MONSTER_PART_SHIELD, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON):
        if not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_SHIELD) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_LEFTGUN):
            pass
        if not cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_RIGHTGUN) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            if not cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2001) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2002) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2003) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2004) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 3004) or cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321):
                cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 6701
    m_Name = '武器暴击时才能造成伤害及效果'
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

