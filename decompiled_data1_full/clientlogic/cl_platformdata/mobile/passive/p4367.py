# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4367.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4367.pyc
# Source Generated with Decompyle++
# File: p4367.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_HARDNESS, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, EQUIP_TYPE_CLOSEWEAPON, MONSTER_PART_HARDNESS, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERFORM):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -1000, 0, '')
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_HARDNESS)
    elif cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON) and cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -4000, 0, '')
    elif cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_HARDNESS):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -8500, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4367
    m_Name = '【诡谲雪山】罗睺-减伤配置'
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

