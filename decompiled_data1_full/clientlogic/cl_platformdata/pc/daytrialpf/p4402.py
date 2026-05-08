# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4402.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4402.pyc
# Source Generated with Decompyle++
# File: p4402.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EXECUTETYPE_DAYTRIALPF, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 5) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0 and cl_evcon.GetMonsterSuperLevel(oWarrior, oEventCB) > 0:
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_DAYTRIALPF)
    elif cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0:
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_DAYTRIALPF)
    elif cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 1000, 5):
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_DAYTRIALPF)
    elif cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 10000, 5) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0:
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_DAYTRIALPF)


class CPerform(CCustomPerform):
    m_SID = 4402
    m_Name = '暴击一定概率秒杀怪物'
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

