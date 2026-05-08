# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50211.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50211.pyc
# Source Generated with Decompyle++
# File: p50211.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_DOUBLE_DAMAGE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, DEVICECOMP_TYPE_HERO, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 1) and cl_evcon.EventCBCheckDamageBuffByBarrier(oWarrior, oEventCB, 1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 0, 0, 1, 0, 0, 1, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a) * 50 // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, -1, 0, 1, 0, 0, BOX_DOUBLE_DAMAGE, None, None)


class CPerform(CCustomPerform):
    m_SID = 50211
    m_Name = '英雄核心'
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
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = (207,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

