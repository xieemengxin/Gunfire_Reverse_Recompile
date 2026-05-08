# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6020.pyc
# Source Generated with Decompyle++
# File: p6020.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, EQUIP_SNIPER, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 3)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_SNIPER):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 5000 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -3000, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_WEAKNESS)


class CPerform(CCustomPerform):
    m_SID = 6020
    m_Name = '游侠lv.5'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

