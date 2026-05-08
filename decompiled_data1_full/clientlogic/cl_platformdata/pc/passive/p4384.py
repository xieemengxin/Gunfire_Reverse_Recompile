# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4384.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4384.pyc
# Source Generated with Decompyle++
# File: p4384.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_AREA, EQUIP_TYPE_AMULET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET):
        cl_evact.EventCBSetMaxLuckyHit(oWarrior, oEventCB, 1)
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_AREA)


class CPerform(CCustomPerform):
    m_SID = 4384
    m_Name = '法器专属被动'
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

